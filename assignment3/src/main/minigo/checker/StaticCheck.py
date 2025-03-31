"""
 * @author nhphung
"""
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
    def __init__(self, env, stage, scope):
        self.env = env
        self.stage = stage
        self.scope = scope
    def add(self, x: Symbol):
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
        print(c.scope)
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
    
    def visitFuncDecl(self,ast: FuncDecl, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(Function(), ast.name)
            return Symbol(ast.name, None, ast, c.scope)
        elif c.stage == 2:
            paramlst = reduce(lambda acc, ele: acc.add(self.visitParamDecl(ele, acc)), ast.params, Env([], 2, c.scope))
            res.mtype = MType(paramlst, ast.retType)
            self.visit(ast.body, Env(paramlst.env + c.env, 2, c.scope+1))
            return
    
    def visitParamDecl(self, ast: ParamDecl, c: Env):
        res = self.lookup(ast.parName, c.env, getName)
        if res:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, MType(None, ast.parType), ast, c.scope)
    
    def visitMethodDecl(self, ast: MethodDecl, c: Env):
        if c.stage == 1:
            return 
        elif c.stage == 2:
            holder = self.visit(ast.receiver, c)
            if not (holder and isinstance(holder, StructType)):
                raise Undeclared(Identifier(), ast.recType)
            
            func = ast.fun      
            if next(filter(lambda x: x.fun.name == ast.fun.name, holder.value.methods)):
                raise Redeclared(Method(), ast.fun.name)
            
            paramlst = reduce(cumulative(self), func.params, Env([], 2, c.scope+1))
            self.visit(func.body, Env(paramlst.env + [Symbol(ast.receiver, ast.recType, None, c.scope+1)] + c.env, 2, c.scope+1))  
            holder.value.methods.append(ast)

    def visitPrototype(self, ast, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if res:
            raise Redeclared(Prototype(), ast.name)
        typelst = reduce(lambda acc, ele: self.visit(ele, acc) + acc, ast.params, [])
        return Symbol(ast.name, MType(typelst, ast.retType), ast, c.scope)

    def visitInterfaceType(self, ast: InterfaceType, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(InterfaceType(), ast.name)
            return Symbol(ast.name, ast, ast, c.scope)
        
        elif c.stage == 2:
            reduce(cumulative(self), ast.methods, Env([], 2, c.scope+1))
            
    def visitStructType(self, ast: StructType, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if c.stage == 1:
            if res:
                raise Redeclared(StructType(), ast.name)
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
        
    def visitArrayType(self, ast: ArrayType, c):
        return ast

    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return ast
    
    def visitBooleanLiteral(self, ast, c):
        return ast
    
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        return ast
    
    def visitNilLiteral(self, ast: NilLiteral, c):
        return ast
    
    def visitBlock(self, ast: Block, c):
        return reduce(cumulative(self), ast.member, c)
    
    def visitAssign(self, ast: Assign, c):
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
    
    def visitId(self, ast: Id, c: Env):
        res = self.lookup(ast.name, c.env, getName)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype
    
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