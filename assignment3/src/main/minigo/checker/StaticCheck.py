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
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"
    
getName = lambda x: x.name

class StaticChecker(BaseVisitor,Utils):
    stage = 1
    @staticmethod
    def matchType(node1: AST, node2: AST):
        return type(node1) is type(node2)
    
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))]
 
    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        self.stage = 1
        env = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.decl, [])
        self.stage = 2
        bodyStmt = list(filter(lambda x: not (isinstance(x, VarDecl) or isinstance(x, ConstDecl))))
        reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, bodyStmt, env)
        return env
    
    def visitVarDecl(self, ast: VarDecl, c):
        if self.stage != 1:
            return 
        
        res = self.lookup(ast.varName, c, getName)
        if res:
            raise Redeclared(Variable(), ast.varName)
        if ast.varInit:
            initType = self.visit(ast.varInit, c)
            if ast.varType is None:
                ast.varType = initType
            if not type(ast.varType) is type(initType):
                raise TypeMismatch(ast)
        return Symbol(ast.varName, ast.varType, ast)
    
    def visitConstDecl(self, ast: ConstDecl, c):
        if self.stage != 1:
            return
        
        res = self.lookup(ast.conName, c, getName)
        if res:
            raise Redeclared(ConstDecl(), ast.conName)
        initType = self.visit(ast.iniExpr, c)
        if not ast.conType:
            ast.conType = initType
        if not type(ast.conType) is type(initType):
            raise TypeMismatch(ast)
        return Symbol(ast.conName, ast.conType, ast)
    
    def visitFuncDecl(self,ast: FuncDecl, c):
        res = self.lookup(ast.name, c, getName)
        if   self.stage == 1:
            if res:
                raise Redeclared(Function(), ast.name)
            return Symbol(ast.name, None, ast)
        elif self.stage == 2:
            paramlst = reduce(lambda acc, ele: [self.visitParamDecl(ele, acc)] + acc, ast.params, [])
            res.mtype = MType(paramlst, ast.retType)
            reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.body, paramlst + c)
            return
    
    def visitParamDecl(self, ast: ParamDecl, c):
        res = self.lookup(ast.parName, c, getName)
        if res:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, MType(None, ast.parType), ast)
    
    def visitMethodDecl(self, ast: MethodDecl, c: List[Symbol]):
        if   self.stage == 1:
            return 
        elif self.stage == 2:
            holder = self.visit(ast.receiver, c)
            if not (holder and isinstance(holder, StructType)):
                raise Undeclared(Identifier(), ast.recType)
            
            func = ast.fun      
            if next(filter(lambda x: x.fun.name == ast.fun.name, holder.value.methods)):
                raise Redeclared(Method(), ast.fun.name)
            
            paramlst = reduce(lambda acc, ele: self.visit(ele) + acc, func.params, [])
            reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, func.body, paramlst + [Symbol(ast.receiver, ast.recType, None)] + c)        
            holder.value.methods.append(ast)

    def visitPrototype(self, ast, c):
        res = self.lookup(ast.name, c, getName)
        if res:
            raise Redeclared(Prototype(), ast.name)
        typelst = reduce(lambda acc, ele: self.visit(ele) + acc, ast.params, [])
        return Symbol(ast.name, MType(typelst, ast.retType), ast)

    def visitInterfaceType(self, ast: InterfaceType, c):
        res = self.lookup(ast.name, c, getName)
        if   self.stage == 1:
            if res:
                raise Redeclared(InterfaceType(), ast.name)
            return Symbol(ast.name, ast, ast)
        elif self.stage == 2:
            reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.methods, [])
            
    def visitStructType(self, ast: StructType, c):
        res = self.lookup(ast.name, c, getName)
        if res:
            raise Redeclared(StructType(), ast.name)
        fields = []
        userDefineTypes = filter(lambda x: x.value == StructType, c)
        for field, typ in ast.elements:
            if field in fields:
                raise Redeclared(Field(), field)
            if typ not in [IntType(), FloatType(), StringType(), BoolType()]:
                if isinstance(typ, Id) and typ.name not in list(map(lambda x: x.mtype.rettype,userDefineTypes)):
                    raise Undeclared(Identifier(), typ.name)
            fields.append(field)
        return Symbol(ast.name, ast, ast)

    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return StringLiteral()
    
    def visitBooleanLiteral(self, ast, c):
        return BooleanLiteral()
    
    def visitVoidType(self, ast, c):
        return VoidType()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        return ArrayLiteral()
    
    def visitStructLiteral(self, ast: StructLiteral, c):
        return StructLiteral(ast.name, [])
    
    def visitNilLiteral(self, ast: NilLiteral, c):
        return NilLiteral()
    
    def visitId(self,ast,c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype