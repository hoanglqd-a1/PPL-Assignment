"""
 * @author nhphung
"""
from utils.AST import * 
from utils.Visitor import *
from utils.Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None, scope=0):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.scope = scope

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"
    
getName = lambda x: x.name
cumulative = lambda caller: lambda acc, ele: acc.add(caller.visit(ele, acc))

class Env:
    def __init__(self, env, stage, scope):
        self.env = env
        self.stage = stage
        self.scope = scope
    def add(self, x):
        if not isinstance(x, Symbol): return self
        return Env([x] + self.env, self.stage, self.scope)

class StaticChecker(BaseVisitor,Utils):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = Env([Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))],
                               1, 0)
 
    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast: Program, c: Env):
        c.stage = 1
        c = reduce(cumulative(self), ast.decl, c)
        c.stage = 2
        bodyStmt = list(filter(lambda x: not (isinstance(x, VarDecl) or isinstance(x, ConstDecl)), ast.decl))
        list(map(lambda x: self.visit(x, c), bodyStmt))
        return c
    
    def visitVarDecl(self, ast: VarDecl, c: Env):
        res = self.lookup(ast.varName, c.env, getName)
        if res and res.scope == c.scope:
            raise Redeclared(Variable(), ast.varName)
        if ast.varInit:
            initType = self.visit(ast.varInit, c)
            if ast.varType is None:
                ast.varType = initType
            if not type(ast.varType) is type(initType):
                raise TypeMismatch(ast)
        return Symbol(ast.varName, ast.varType, ast, c.scope)
    
    def visitConstDecl(self, ast: ConstDecl, c: Env):        
        res = self.lookup(ast.conName, c.env, getName)
        if res and res.scope == c.scope:
            raise Redeclared(Constant(), ast.conName)
        initType = self.visit(ast.iniExpr, c)
        if not ast.conType:
            ast.conType = initType
        if type(ast.conType) is not type(initType):
            raise TypeMismatch(ast)
        return Symbol(ast.conName, ast.conType, ast, c.scope)
    
    def visitFuncDecl(self, ast: FuncDecl, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(Function(), ast.name)
            return Symbol(ast.name, None, ast, c.scope)
        elif c.stage == 2:
            paramlst = reduce(lambda acc, ele: acc.add(self.visitParamDecl(ele, acc)), ast.params, Env([], 2, c.scope+1))
            res.mtype = MType(list(map(lambda x: x.mtype, paramlst.env)), ast.retType)
            c = self.visit(ast.body, Env(paramlst.env + c.env, 2, c.scope))
            returnStmts = list(filter(lambda x: x.name == "return", c.env))
            for retStmt in returnStmts:
                if retStmt.mtype != ast.retType:
                    raise TypeMismatch(retStmt.value)
            return
    
    def visitParamDecl(self, ast: ParamDecl, c: Env):
        res = self.lookup(ast.parName, c.env, getName)
        if res:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType, ast, c.scope)
    
    def visitMethodDecl(self, ast: MethodDecl, c: Env):
        if c.stage == 1:
            return 
        elif c.stage == 2:
            holder = self.visit(ast.receiver, c)
            if not (holder and isinstance(holder, StructType)):
                raise Undeclared(Identifier(), ast.recType)
            
            func = ast.fun
            if next(filter(lambda x: x.fun.name == ast.fun.name, holder.methods)):
                raise Redeclared(Method(), ast.fun.name)
            
            paramlst = reduce(cumulative(self), func.params, Env([], 2, c.scope+1))
            c = self.visit(func.body, Env(paramlst.env + [Symbol(ast.receiver, ast.recType, None, c.scope+1)] + c.env, 2, c.scope))
            retStmts = list(filter(lambda x: x.name == "return", c.env))
            for retStmt in retStmts:
                if retStmt.mtype != func.retType:
                    raise TypeMismatch(retStmt.value)
            holder.methods.append(ast)

    def visitPrototype(self, ast, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if res:
            raise Redeclared(Prototype(), ast.name)
        typelst = reduce(lambda acc, ele: self.visit(ele, acc) + acc, ast.params, [])
        return Symbol(ast.name, MType(typelst, ast.retType), ast, c.scope)
    
    def visitIntType(self, ast: IntType, c: Env):
        return IntType()
    
    def visitFloatType(self, ast: FloatType, c: Env):
        return FloatType()
    
    def visitStringType(self, ast: StringType, c: Env):
        return StringType()
    
    def visitBoolType(self, ast: BoolType, c: Env):
        return BoolType()
    
    def visitVoidType(self, ast: VoidType, c: Env):
        return VoidType()
    
    def visitArrayType(self, ast: ArrayType, c: Env):
        return ArrayType(self.visit(ast.eleType, c))

    def visitInterfaceType(self, ast: InterfaceType, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res: return
            return Symbol(ast.name, ast, ast, c.scope)
        
        elif c.stage == 2:
            reduce(cumulative(self), ast.methods, Env([], 2, c.scope+1))
            
    def visitStructType(self, ast: StructType, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res: return
            return Symbol(ast.name, ast, ast, c.scope)
            
        elif c.stage == 2:
            fields = []
            userDefineTypes = filter(lambda x: x.value is StructType, c)
            for field, typ in ast.elements:
                if field in fields:
                    raise Redeclared(Field(), field)
                if typ not in [IntType(), FloatType(), StringType(), BoolType()]:
                    if isinstance(typ, Id) and typ.name not in list(map(lambda x: x.mtype.rettype, userDefineTypes)):
                        raise Undeclared(Identifier(), typ.name)
                fields.append(field)
    
    def visitBlock(self, ast: Block, c: Env):
        # return reduce(cumulative(self), ast.member, Env(c.env, c.stage, c.scope+1))
        c = Env(c.env, c.stage, c.scope+1)
        for stmt in ast.member:
            if isinstance(stmt, FuncCall):
                self.visitFuncCall(stmt, c, True)
            elif isinstance(stmt, MethCall):
                self.visitMethCall(stmt, c, True)
            else:
                c.add(self.visit(stmt, c))
    
    def visitAssign(self, ast: Assign, c: Env):
        rhs = self.visit(ast.rhs, c)
        try:
            lhs = self.visit(ast.lhs, c)
            if not self.matchType(lhs, rhs):
                raise TypeMismatch(ast)
            
        except Undeclared as u:
            if u.k is Identifier():
                return Symbol(u.n, rhs, ast, c.scope)
            raise u
        except Exception as e:
            raise e
        
    def visitIf(self, ast: If, c: Env):
        typ = self.visit(ast.expr, c)
        if not isinstance(typ, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c)
        self.visit(ast.elseStmt, c)

    def visitForBasic(self, ast: ForBasic, c: Env):
        typ = self.visit(ast.cond, c)
        if not isinstance(typ, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForStep(self, ast: ForStep, c: Env):
        loopVar = None
        if isinstance(ast.init, VarDecl):
            loopVar = self.visit(ast.init, Env([], c.stage, c.scope+1))
            c = c.add(loopVar)
        elif isinstance(ast.init, Assign):
            if not isinstance(ast.init.lhs, Id):
                raise TypeMismatch(ast)
            self.visit(ast.init, c)
            loopVar = self.lookup(ast.init.lhs.name, c.env, getName)
        cond = self.visit(ast.cond, c)
        if not isinstance(cond, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.upda, c)
        if not isinstance(ast.upda.lhs, Id) or ast.upda.lhs.name != loopVar.name:
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)

    def visitForEach(self, ast: ForEach, c: Env):
        arr = self.visit(ast.arr, c)
        if not isinstance(arr, ArrayType):
            raise TypeMismatch(ast)
        idx = Symbol(ast.idx, IntType(), ast.idx, c.scope+1)
        value = Symbol(ast.value, arr.eleType, ast.value, c.scope+1)
        self.visit(ast.loop, c.add(idx).add(value))

    def visitBreak(self, ast: Break, c: Env):
        return
    
    def visitContinue(self, ast: Continue, c: Env):
        return
    
    def visitReturn(self, ast: Return, c: Env):
        return Symbol("return", self.visit(ast.expr, c) if ast.expr else VoidType(), ast, c.scope)

    def visitId(self, ast: Id, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype
    
    def visitArrayCell(self, ast: ArrayCell, c: Env):
        arr = self.visit(ast.arr, c)
        if not isinstance(arr, ArrayType):
            raise TypeMismatch(ast)
        shape = arr.dimens
        for idx in ast.idx:
            if not isinstance(self.visit(idx, c), IntType):
                raise TypeMismatch(ast)
            shape = shape[1:]
        return arr.eleType if shape == [] else ArrayType(shape, arr.eleType)
    
    def visitFieldAccess(self, ast: FieldAccess, c: Env):
        typ = self.visit(ast.receiver, c)
        if not isinstance(typ, StructType):
            raise TypeMismatch(ast)
        field = next(filter(lambda x: x[0] == ast.field, typ.elements))
        if not field:
            raise Undeclared(Field(), ast.field)
        return field[1]
    
    def visitBinaryOp(self, ast: BinaryOp, c: Env):
        typ1 = self.visit(ast.left, c)
        typ2 = self.visit(ast.right, c)
        if ast.op in ["&&", "||"]:
            if not isinstance(typ1, BoolType) or not isinstance(typ2, BoolType):
                raise TypeMismatch(ast)
        if ast.op in ["+", "==", "!=", ">", "<", ">=", "<="]:
            if not self.matchType(typ1, typ2) or type(typ1) not in [IntType, FloatType, StringType]:
                raise TypeMismatch(ast)
        if ast.op in ["-", "*", "/", "%"]:
            if not self.matchType(typ1, typ2) or type(typ1) not in [IntType, FloatType]:
                raise TypeMismatch(ast)
        return typ1
    
    def visitUnaryOp(self, ast: UnaryOp, c: Env):
        typ = self.visit(ast.expr, c)
        if ast.op == "!":
            if not isinstance(typ, BoolType):
                raise TypeMismatch(ast)
        if ast.op == "-":
            if type(typ) not in [IntType, FloatType]:
                raise TypeMismatch(ast)
            return typ
        return typ
    
    def visitFuncCall(self, ast: FuncCall, c: Env, isVoid = False):
        func = self.lookup(ast.name, c.env, getName)
        if not func:
            raise Undeclared(Function(), ast.name)
        if len(func.params) != len(ast.args):
            raise TypeMismatch(ast)
        for partype, arg in zip(func.mtype.partype, ast.args):
            if not self.matchType(partype, self.visit(arg, c)):
                raise TypeMismatch(ast)
        if func.mtype.rettype is VoidType() and not isVoid:
            raise TypeMismatch(ast)
        if func.mtype.rettype is not VoidType() and isVoid:
            raise TypeMismatch(ast)
        return func.mtype.rettype
    
    def visitMethCall(self, ast: MethCall, c: Env, isVoid = False):
        receiver = self.visit(ast.receiver)
        if not isinstance(receiver, StructType):
            raise TypeMismatch(ast)
        meth = next(filter(lambda x: x.fun.name == ast.metName, receiver.methods))
        func = meth.fun
        if len(func.params) != len(ast.args):
            raise TypeMismatch(ast)
        for param, arg in zip(func.params, ast.args):
            if not self.matchType(param.parType, self.visit(arg, c)):
                raise TypeMismatch(ast)
        if func.retType is VoidType() and not isVoid:
            raise TypeMismatch(ast)
        if func.retType is not VoidType() and isVoid:
            raise TypeMismatch(ast)
        return func.retType
    
    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        return ArrayType(ast.dimens, ast.eleType)
    
    def visitStructLiteral(self, ast: StructLiteral, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if not res:
            raise Undeclared(StructType(), ast.name)
        fieldlst = []
        for f, typ in ast.elements:
            if [f, self.visit(typ, c)] not in res.mtype.elements:
                raise TypeMismatch(ast)
            if f in fieldlst:
                raise TypeMismatch(ast)
            fieldlst.append(f)
        return res.mtype
    
    def visitNilLiteral(self, ast: NilLiteral, c):
        return VoidType()
    
    def matchType(self, typ1, typ2):
        if type(typ1) is InterfaceType and type(typ2) is StructType:
            typ2meth = list(map(getName, typ2.methods))
            for meth in typ1.methods:
                if meth.name not in typ2meth:
                    return False
            return True
        if type(typ1) is StructType and type(typ2) is InterfaceType:
            typ1meth = list(map(getName, typ1.methods))
            for meth in typ2.methods:
                if meth.name not in typ1meth:
                    return False
            return True
        return type(typ1) is type(typ2)