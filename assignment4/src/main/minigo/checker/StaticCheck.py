"""
 * @author nhphung
"""
# from utils.AST import *
# from utils.Visitor import *
# from utils.Utils import Utils
from AST import *
from Visitor import *
from Utils import Utils
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
    env = []
    def __init__(self, env, stage, scope, rettype=None):
        self.env = env
        self.stage = stage
        self.scope = scope
        self.rettype = rettype
    def add(self, x):
        if not isinstance(x, Symbol): return self
        return Env([x] + self.env, self.stage, self.scope, self.rettype)
    def upScope(self):
        return Env(self.env, self.stage, self.scope+1, self.rettype)

class StaticChecker(BaseVisitor,Utils):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = Env([Symbol("getInt", MType([], IntType())),
                                Symbol("putInt", MType([IntType()], VoidType())),
                                Symbol("putIntLn", MType([IntType()], VoidType())),
                                Symbol("getFloat", MType([], FloatType())),
                                Symbol("putFloat", MType([FloatType()], VoidType())),
                                Symbol("putFloatLn", MType([FloatType()], VoidType())),
                                Symbol("getBool", MType([], BoolType())),
                                Symbol("putBool", MType([BoolType()], VoidType())),
                                Symbol("putBoolLn", MType([BoolType()], VoidType())),
                                Symbol("getString", MType([], StringType())),
                                Symbol("putString", MType([StringType()], VoidType())),
                                Symbol("putStringLn", MType([StringType()], VoidType())),
                                Symbol("putLn", MType([], VoidType())),
                                ],
                               1, 0)

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast: Program, c: Env):
        c.stage = 1
        c = reduce(cumulative(self), ast.decl, c)
        c.stage = 2
        FuncAndType = list(filter(lambda x: type(x) in [FuncDecl, MethodDecl, StructType, InterfaceType], ast.decl))
        list(map(lambda x: self.visit(x, c), FuncAndType))
        c.stage = 3
        c = reduce(cumulative(self), ast.decl, c)
        return c
    
    def visitVarDecl(self, ast: VarDecl, c: Env):
        res = self.lookup(ast.varName, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(Variable(), ast.varName)
            return Symbol(ast.varName, None, ast, c.scope)
        if res and c.scope > 0 and c.scope == res.scope:
            raise Redeclared(Variable(), ast.varName)
        if ast.varType and not self.isType(ast.varType, c):
            raise TypeMismatch(ast)
        varType = self.visit(ast.varType, c) if ast.varType else None
        if ast.varInit:
            initType = self.visit(ast.varInit, c)
            if varType is None:
                varType = initType
            if not self.assignmentMatchType(varType, initType, c):
                raise TypeMismatch(ast)
            if isinstance(varType, InterfaceType):
                varType = initType
        if isinstance(varType, VoidType):
            raise TypeMismatch(ast)
        if res and c.scope == 0:
            res.mtype = varType
        return Symbol(ast.varName, varType, ast, c.scope)
    
    def visitConstDecl(self, ast: ConstDecl, c: Env): 
        res = self.lookup(ast.conName, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(Constant(), ast.conName)
            return Symbol(ast.conName, None, ast, c.scope)
        if res and c.scope > 0 and c.scope == res.scope:
            raise Redeclared(Constant(), ast.conName)
        if ast.conType and not self.isType(ast.conType, c):
            raise TypeMismatch(ast)
        conType = self.visit(ast.conType, c) if ast.conType else None
        initType = self.visit(ast.iniExpr, c)
        if conType is None:
            conType = initType
        if not self.assignmentMatchType(conType, initType, c) or isinstance(conType, VoidType):
            raise TypeMismatch(ast)
        if isinstance(conType, InterfaceType):
            conType = initType
        if res and c.scope == 0:
            res.mtype = conType
        return Symbol(ast.conName, conType, ast, c.scope)
    
    def visitFuncDecl(self, ast: FuncDecl, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(Function(), ast.name)
            return Symbol(ast.name, None, ast, c.scope)
        assert c.stage > 1
        paramlst = reduce(lambda acc, ele: acc.add(self.visitParamDecl(ele, Env(acc.env+c.env, c.stage, c.scope+1))), ast.params, Env([], c.stage, c.scope+1))
        assert res is not None
        if c.stage == 2:
            if not self.isType(ast.retType, c):
                raise TypeMismatch(ast)
            retType = self.visit(ast.retType, c)
            res.mtype = MType(list(map(lambda x: x.mtype, paramlst.env[::-1])), retType)
        elif c.stage == 3:
            c = self.visit(ast.body, Env(paramlst.env + c.env, 3, c.scope+2, res.mtype.rettype))
    
    def visitParamDecl(self, ast: ParamDecl, c: Env):
        res = self.lookup(ast.parName, c.env, getName)
        if res and res.scope == c.scope:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, self.visit(ast.parType, c), ast, c.scope)
    
    def visitMethodDecl(self, ast: MethodDecl, c: Env):
        if c.stage == 1:
            return
        assert isinstance(ast.recType, Id)
        # container = self.lookup(ast.recType.name, c.env, getName)
        # if not (container and isinstance(container.value, StructType)):
        #     raise Undeclared(Identifier(), ast.recType)
        if not self.isType(ast.recType, c):
            raise TypeMismatch(ast)
        rectype = self.visit(ast.recType, c)
        func = ast.fun
        if c.stage == 2:
            if next(filter(lambda x: x[0] == func.name, rectype.elements), None):
                raise Redeclared(Method(), func.name)
            if next(filter(lambda x: x.fun.name == func.name, rectype.methods), None):
                raise Redeclared(Method(), func.name)
            if not self.isType(func.retType, c):
                raise TypeMismatch(ast)
            rectype.methods.append(ast)
        elif c.stage == 3:
            paramlst = reduce(lambda acc, ele: acc.add(self.visit(ele, Env(acc.env+c.env, c.stage, c.scope+2))), func.params, Env([], c.stage, c.scope+2))
            c = self.visit(func.body, Env(paramlst.env + [Symbol(ast.receiver, self.visit(ast.recType, c), ast.receiver, c.scope+1)] + c.env, 3, c.scope+3, func.retType))

    def visitPrototype(self, ast, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if res and res.scope == c.scope:
            raise Redeclared(Prototype(), ast.name)
        typelst = reduce(cumulative(self), ast.params, c)
        if not self.isType(ast.retType, c):
            raise TypeMismatch(ast)
        retType = self.visit(ast.retType, c)
        return Symbol(ast.name, MType(typelst, retType), ast, c.scope)
    
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
        for dimen in ast.dimens:
            if not isinstance(self.visit(dimen, c), IntType):
                raise TypeMismatch(ast)
        newDimen = list(map(lambda x: IntLiteral(self.staticCalculate(x, c)), ast.dimens))
        return ArrayType(newDimen, self.visit(ast.eleType, c))

    def visitInterfaceType(self, ast: InterfaceType, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(Type(), ast.name)
            return Symbol(ast.name, ast, ast, c.scope)
        elif c.stage == 2:
            reduce(cumulative(self), ast.methods, c.upScope())
            
    def visitStructType(self, ast: StructType, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res and c.scope == 0:
                raise Redeclared(Type(), ast.name)
            return Symbol(ast.name, ast, ast, c.scope)
        elif c.stage == 2:
            fields = []
            for field, typ in ast.elements:
                if field in fields:
                    raise Redeclared(Field(), field)
                # if typ not in [IntType(), FloatType(), StringType(), BoolType()]:
                #     if isinstance(typ, Id) and typ.name not in list(map(lambda x: x.mtype.rettype, userDefineTypes)):
                #         raise Undeclared(Identifier(), typ.name)
                if not self.isType(typ, c):
                    raise TypeMismatch(ast)
                fields.append(field)
    
    def visitBlock(self, ast: Block, c: Env):
        for stmt in ast.member:
            if isinstance(stmt, FuncCall):
                self.visitFuncCall(stmt, c, True)
            elif isinstance(stmt, MethCall):
                self.visitMethCall(stmt, c, True)
            else:
                c = c.add(self.visit(stmt, c))
        return c
    
    def visitAssign(self, ast: Assign, c: Env):
        rhs = self.visit(ast.rhs, c)
        try:
            lhs = self.visit(ast.lhs, c)
            if not self.assignmentMatchType(lhs, rhs, c):
                raise TypeMismatch(ast)
        except Undeclared as u:
            if isinstance(u.k, Identifier) and isinstance(ast.lhs, Id) and u.n == ast.lhs.name:
                return Symbol(u.n, rhs, ast, c.scope)
            raise u
        except Exception as e:
            raise e
        
    def visitIf(self, ast: If, c: Env):
        typ = self.visit(ast.expr, c)
        if not isinstance(typ, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c.upScope())
        if ast.elseStmt: self.visit(ast.elseStmt, c.upScope())

    def visitForBasic(self, ast: ForBasic, c: Env):
        typ = self.visit(ast.cond, c)
        if not isinstance(typ, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c.upScope())

    def visitForStep(self, ast: ForStep, c: Env):
        loopVar = None
        if isinstance(ast.init, VarDecl):
            loopVar = self.visit(ast.init, c.upScope())
            c = c.add(loopVar)
        elif isinstance(ast.init, Assign):
            if not isinstance(ast.init.lhs, Id):
                raise TypeMismatch(ast)
            self.visit(ast.init.lhs, c)
            self.visit(ast.init, c)
            loopVar = self.lookup(ast.init.lhs.name, c.env, getName)
        cond = self.visit(ast.cond, c)
        if not isinstance(cond, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.upda, c)
        if not isinstance(ast.upda.lhs, Id) or ast.upda.lhs.name != loopVar.name:
            raise TypeMismatch(ast)
        self.visit(ast.loop, c.upScope())

    def visitForEach(self, ast: ForEach, c: Env):
        arr = self.visit(ast.arr, c)
        if not isinstance(arr, ArrayType):
            raise TypeMismatch(ast)
        idx = self.visit(ast.idx, c)
        if not isinstance(idx, IntType):
            raise TypeMismatch(ast)
        value = self.visit(ast.value, c)
        eleType = ArrayType(arr.dimens[1:], arr.eleType) if len(arr.dimens) > 1 else arr.eleType
        if not self.matchType(eleType, value, c):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c.upScope())

    def visitBreak(self, ast: Break, c: Env):
        return
    
    def visitContinue(self, ast: Continue, c: Env):
        return
    
    def visitReturn(self, ast: Return, c: Env):
        rettype = self.visit(ast.expr, c) if ast.expr else VoidType()
        if not self.matchType(rettype, c.rettype, c):
            raise TypeMismatch(ast)

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
        field = next(filter(lambda x: x[0] == ast.field, typ.elements), None)
        if not field:
            raise Undeclared(Field(), ast.field)
        return self.visit(field[1], c)
    
    def visitBinaryOp(self, ast: BinaryOp, c: Env):
        typ1 = self.visit(ast.left, c)
        typ2 = self.visit(ast.right, c)
        if ast.op in ["&&", "||"]:
            if isinstance(typ1, BoolType) and isinstance(typ2, BoolType):
                return BoolType()
        if ast.op in ["==", "!=", ">", "<", ">=", "<="]:
            if self.matchType(typ1, typ2, c) and type(typ1) in [IntType, FloatType, StringType]:
                return BoolType()
        if ast.op == '+':
            if isinstance(typ1, StringType) and isinstance(typ2, StringType):
                return StringType()
            if type(typ1) in [IntType, FloatType] and type(typ2) in [IntType, FloatType]:
                return typ2 if isinstance(typ1, IntType) else typ1
        if ast.op in ['-', '*', '/']:
            if type(typ1) in [IntType, FloatType] and type(typ2) in [IntType, FloatType]:
                return typ2 if isinstance(typ1, IntType) else typ1
        if ast.op == '%':
            if isinstance(typ1, IntType) and isinstance(typ2, IntType):
                return IntType()
        raise TypeMismatch(ast)
    
    def visitUnaryOp(self, ast: UnaryOp, c: Env):
        typ = self.visit(ast.body, c)
        if ast.op == "!":
            if not isinstance(typ, BoolType):
                raise TypeMismatch(ast)
        if ast.op == "-":
            if type(typ) not in [IntType, FloatType]:
                raise TypeMismatch(ast)
            return typ
        return typ
    
    def visitFuncCall(self, ast: FuncCall, c: Env, isVoid = False):
        func = self.lookup(ast.funName, c.env, getName)
        if not (func and isinstance(func.mtype, MType)):
            raise Undeclared(Function(), ast.funName)
        if len(func.mtype.partype) != len(ast.args):
            raise TypeMismatch(ast)
        for partype, arg in zip(func.mtype.partype, ast.args):
            if not self.matchType(partype, self.visit(arg, c), c):
                raise TypeMismatch(ast)
        if isinstance(func.mtype.rettype, VoidType) and not isVoid:
            raise TypeMismatch(ast)
        if not isinstance(func.mtype.rettype, VoidType) and isVoid:
            raise TypeMismatch(ast)
        return func.mtype.rettype
    
    def visitMethCall(self, ast: MethCall, c: Env, isVoid = False):
        receiver = self.visit(ast.receiver, c)
        if not receiver:
            raise Undeclared(Identifier(), ast.receiver)
        if isinstance(receiver, StructType):
            meth = next(filter(lambda x: x.fun.name == ast.metName, receiver.methods), None)
            if not meth:
                raise Undeclared(Method(), ast.metName)
            func = meth.fun
            if len(func.params) != len(ast.args):
                raise TypeMismatch(ast)
            for param, arg in zip(func.params, ast.args):
                if not self.matchType(param.parType, self.visit(arg, c), c):
                    raise TypeMismatch(ast)
            if isinstance(func.retType, VoidType) and not isVoid:
                raise TypeMismatch(ast)
            if not isinstance(func.retType, VoidType) and isVoid:
                raise TypeMismatch(ast)
            return func.retType
        elif isinstance(receiver, InterfaceType):
            prototype = next(filter(lambda x: x.name == ast.metName, receiver.methods), None)
            if not prototype:
                raise Undeclared(Method(), ast.metName)
            if len(prototype.params) != len(ast.args):
                raise TypeMismatch(ast)
            for typ, arg in zip(prototype.params, ast.args):
                if not self.matchType(self.visit(typ, c), self.visit(arg, c), c):
                    raise TypeMismatch(ast)
            if isinstance(prototype.retType, VoidType) and not isVoid:
                raise TypeMismatch(ast)
            if not isinstance(prototype.retType, VoidType) and isVoid:
                raise TypeMismatch(ast)
            return prototype.retType
        else:
            raise TypeMismatch(ast)
            
    
    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()
    
    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        dimens = list(map(lambda x: self.visit(x, c), ast.dimens))
        if next(filter(lambda x: not isinstance(x, IntType), dimens), None):
            raise TypeMismatch(ast)
        newDimens = list(map(lambda x: IntLiteral(self.staticCalculate(x, c)), ast.dimens))
        # if not self.checkArrayLiteral(newDimens, ast.eleType, ast.value, c):
        #     raise TypeMismatch(ast)
        return ArrayType(newDimens, self.visit(ast.eleType, c))
    
    def visitStructLiteral(self, ast: StructLiteral, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if not res:
            raise Undeclared(StructType(), ast.name)
        fieldlst = []
        for f, typ in ast.elements:
            try:
                ftype = next(filter(lambda x: x[0] == f, res.mtype.elements))[1]
            except StopIteration:
                raise TypeMismatch(ast)
            if not self.matchType(ftype, self.visit(typ, c), c):
                raise TypeMismatch(ast)
            if f in fieldlst:
                raise TypeMismatch(ast)
            fieldlst.append(f)
        return res.mtype
    
    def visitNilLiteral(self, ast: NilLiteral, c):
        return VoidType()
    
    def matchType(self, typ1, typ2, c):
        if isinstance(typ1, Id):
            typ1 = self.visit(typ1, c)
        if isinstance(typ2, Id):
            typ2 = self.visit(typ2, c)
        if type(typ1) is InterfaceType and type(typ2) is StructType:
            for proto in typ1.methods:
                meth = next(filter(lambda x: x.fun.name == proto.name, typ2.methods), None)
                if not meth: return False
                methType = list(map(lambda x: x.parType, meth.fun.params))
                if len(methType) != len(proto.params): return False
                if any(map(lambda pair: not self.matchType(pair[0], pair[1], c), list(zip(methType, proto.params)))) or not self.matchType(proto.retType, meth.fun.retType, c):
                    return False
            return True
        if type(typ1) is StructType and type(typ2) is InterfaceType:
            for proto in typ2.methods:
                meth = next(filter(lambda x: x.fun.name == proto.name, typ1.methods), None)
                if not meth:
                    return False
                methType = list(map(lambda x: x.parType, meth.fun.params))
                if any(map(lambda pair: not self.matchType(pair[0], pair[1], c), list(zip(methType, proto.params)))) or not self.matchType(proto.retType, meth.fun.retType, c):
                    return False
            return True
        if isinstance(typ1, MType) and isinstance(typ2, MType):
            try:
                for partype1, partype2 in zip(typ1.partype, typ2.partype):
                    if not self.matchType(partype1, partype2, c):
                        return False
                return self.matchType(typ1.rettype, typ2.rettype, c)
            except:
                return False
        if isinstance(typ1, Id) and isinstance(typ2, Id):
            return typ1.name == typ2.name
        if isinstance(typ1, StructType) and isinstance(typ2, StructType):
            return typ1.name == typ2.name
        if isinstance(typ1, InterfaceType) and isinstance(typ2, InterfaceType):
            return typ1.name == typ2.name
        if isinstance(typ1, ArrayType) and isinstance(typ2, ArrayType):
            for dimen1, dimen2 in zip(typ1.dimens, typ2.dimens):
                if dimen1.value != dimen2.value:
                    return False
            return self.matchType(typ1.eleType, typ2.eleType, c)
        return type(typ1) == type(typ2)
    def assignmentMatchType(self, typ1, typ2, c):
        if isinstance(typ1, ArrayType) and isinstance(typ2, ArrayType):
            for dimen1, dimen2 in zip(typ1.dimens, typ2.dimens):
                if dimen1.value != dimen2.value:
                    return False
            return self.assignmentMatchType(typ1.eleType, typ2.eleType, c)
        if isinstance(typ1, FloatType) and isinstance(typ2, IntType):
            return True
        return self.matchType(typ1, typ2, c)

    def isType(self, typ, c):
        if type(typ) in [IntType, FloatType, StringType, BoolType, VoidType]:
            return True
        if isinstance(typ, ArrayType):
            return self.isType(typ.eleType, c)
        if isinstance(typ, Id):
            res = self.lookup(typ.name, c.env, getName)
            if not res:
                raise Undeclared(Identifier(), typ.name)
            return isinstance(res.mtype, StructType) or isinstance(res.mtype, InterfaceType)
        return False
    def staticCalculate(self, ast: Expr, c: Env):
        try:
            if isinstance(ast, BinaryOp):
                if ast.op == '&&':
                    return self.staticCalculate(ast.left, c) and self.staticCalculate(ast.right, c)
                if ast.op == '||':
                    return self.staticCalculate(ast.left, c) or self.staticCalculate(ast.right, c)
                if ast.op == '+':
                    return self.staticCalculate(ast.left, c) + self.staticCalculate(ast.right, c)
                if ast.op == '-':
                    return self.staticCalculate(ast.left, c) - self.staticCalculate(ast.right, c)
                if ast.op == '*':
                    return self.staticCalculate(ast.left, c) * self.staticCalculate(ast.right, c)
                if ast.op == '/':
                    return self.staticCalculate(ast.left, c) / self.staticCalculate(ast.right, c)
                if ast.op == '%':
                    return self.staticCalculate(ast.left, c) % self.staticCalculate(ast.right, c)
                if ast.op == '==':
                    return self.staticCalculate(ast.left, c) == self.staticCalculate(ast.right, c)
                if ast.op == '!=':
                    return self.staticCalculate(ast.left, c) != self.staticCalculate(ast.right, c)
                if ast.op == '>':
                    return self.staticCalculate(ast.left, c) > self.staticCalculate(ast.right, c)
                if ast.op == '<':
                    return self.staticCalculate(ast.left, c) < self.staticCalculate(ast.right, c)
                if ast.op == '>=':
                    return self.staticCalculate(ast.left, c) >= self.staticCalculate(ast.right, c)
                if ast.op == '<=':
                    return self.staticCalculate(ast.left, c) <= self.staticCalculate(ast.right, c)
            if isinstance(ast, UnaryOp):
                if ast.op == '-':
                    return - self.staticCalculate(ast.body, c)
                if ast.op == '!':
                    return not self.staticCalculate(ast.body, c)
        except:
            return None
        if isinstance(ast, Id): 
            res = self.lookup(ast.name, c.env, getName)
            if not isinstance(res.value, ConstDecl):
                raise TypeMismatch(ast)
            return self.staticCalculate(res.value.iniExpr, c)
        if type(ast) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral]:
            return ast.value
        if type(ast) in [StructLiteral]:
            return self.visit(ast, c)
        return None
    # def checkArrayLiteral(self, dimens: list[IntLiteral], eleType, value: NestedList, c):
    #     if not dimens:
    #         if isinstance(value, list): return False
    #         if isinstance(self.visit(value, c), type(eleType)): return True
    #         return False
    #     if not isinstance(value, list): return False
    #     if dimens[0].value < 0: return False
    #     if len(value) != dimens[0].value: return False
    #     for val in value:
    #         if not self.checkArrayLiteral(dimens[1:], eleType, val, c): return False
    #     return True