'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
# from utils.Utils import *
# from checker.StaticCheck import *
# from checker.StaticError import *
from AST import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class Control:
    frame : Frame
    env : list
    def __init__(self, env, frame=None, isLeft=None):
        self.env = env
        self.frame = frame
        self.isLeft = isLeft
    def enterScope(self):
        return Control([[]] + self.env, self.frame, self.isLeft)
    def setLeft(self, isLeft):
        return Control(self.env, self.frame, isLeft)

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None

    def init(self):
        mem =  [Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putBool",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putString",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putLn",MType([],VoidType()),CName("io",True)),]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def visitProgram(self, ast, c):
        env = Control([c])
        # env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)
        self.emitObjectInit()
        self.emit.printout(self.emit.emitEPILOG())
        return env

    def visitFuncDecl(self, ast, o: Control):
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        # o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
        o.env[0].append(Symbol(ast.name, mtype, CName(self.className)))
        # env = o.copy()
        # env['env'] = [[]] + env['env']
        env = o.enterScope()
        env.frame = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    def visitVarDecl(self, ast: VarDecl, o: Control):
        if not o.frame: # global var
            o.env[0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value) if ast.varInit else None))
        else:
            frame = o.frame
            index = frame.getNewIndex()
            o.env[0].append(Symbol(ast.varName, ast.varType, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            if ast.varInit:
                # self.emit.printout(self.emit.emitPUSHICONST(ast.varInit.value, frame))
                # self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index,  frame))
                varInitCode, varInitType = self.visit(ast.varInit, o)
                self.emit.printout(varInitCode)
                if isinstance(varInitType, IntType) and isinstance(ast.varType, FloatType):
                    self.emit.printout(self.emit.emitI2F(o.frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
                if isinstance(varInitType, ArrayType) and isinstance(ast.varType, ArrayType) and isinstance(ast.varInit, ArrayLiteral):
                    self.emit.printout(self.writeArray(index, ast.varType, ast.varName, ast.varInit.value, o))
        return o
    
    def visitFuncCall(self, ast, o: Control):
        sym = next(filter(lambda x: x.name == ast.funName, o.env[-1]),None)
        # env = o.copy()
        # env['isLeft'] = False
        env = o.setLeft(False)
        [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
        self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o.frame))
        return o
    
    def visitBlock(self, ast, o: Control):
        # env = o.copy()
        # env['env'] = [[]] + env['env']
        env = o.enterScope()
        env.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        env = reduce(lambda acc,e: self.visit(e,acc),ast.member,env)
        self.emit.printout(self.emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        env.frame.exitScope()
        return o
    
    def visitId(self, ast, o: Control):
        # sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o.env for j in i]),None)
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o.frame),sym.mtype
        else:         
            return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o.frame),sym.mtype

    def visitIntLiteral(self, ast: IntLiteral, o: Control):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o: Control):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()
    
    def visitStringLiteral(self, ast: StringLiteral, o: Control):
        return self.emit.emitPUSHSTRCONST(ast.value, StringType(), o.frame), StringType()
    
    def visitBoolLiteral(self, ast: BooleanLiteral, o:Control):
        if ast.value:
            return self.emit.emitPUSHICONST(1, o.frame), IntType()
        else:
            return self.emit.emitPUSHICONST(0, o.frame), IntType()
        
    def visitArrayLiteral(self, ast: ArrayLiteral, o: Control):
        typ = ast.eleType
        dimens_code = reduce(lambda acc, ele: acc + self.visit(ele, o)[0], ast.dimens, "")
        return dimens_code + self.emit.emitPUSHARRAYCONST(typ, len(ast.dimens), o.frame), ArrayType(ast.dimens, typ)
    
    def writeArray(self, index, inType, name, value, o: Control):
        code = ""
        dimens = self.getDimens(value)
        eleNum = reduce(lambda acc, ele: acc * ele, dimens, 1)
        for i in range(eleNum):
            indicesLst = []
            DIV = 1
            for j in reversed(dimens):
                DIV *= j
                indicesLst.append(i % DIV)
                i //= DIV
            indicesLst.reverse()
            code += self.emit.emitREADVAR(name, inType, index, o.frame)
            code = reduce(lambda acc, ele: acc + self.emit.emitPUSHICONST(ele, o.frame) + self.emit.jvm.emitAALOAD(inType, o.frame), indicesLst[:-1], code)
            code += self.emit.emitPUSHICONST(indicesLst[-1], o.frame)
            ele = value
            for idx in indicesLst:
                ele = ele[idx]
            code += self.visit(ele, o)[0]
            code += self.emit.emitASTORE(inType.eleType, o.frame)
        return code
    
    def getDimens(self, value):
        if not isinstance(value, list):
            return []
        return [len(value)] + self.getDimens(value[0])
    
