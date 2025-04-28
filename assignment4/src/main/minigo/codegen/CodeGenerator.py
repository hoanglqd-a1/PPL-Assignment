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
from typing import Dict, List
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class Control:
    frame : Frame
    env : List[List[Symbol]]
    isLeft : bool
    def __init__(self, env, name, frame = None, isLeft = None):
        self.env = env
        self.name = name
        self.frame = frame
        self.isLeft = isLeft
    def newFrame(self, name, retType):
        if self.frame is not None:
            raise Exception("Logical error")
        return Control(self.env, self.name, Frame(name, retType), self.isLeft)
    def enterScope(self, isProc):
        self.frame.enterScope(isProc)
        return Control([[]] + self.env, self.name, self.frame, self.isLeft)
    def setLeft(self, isLeft):
        return Control(self.env, self.name, self.frame, isLeft)
    def setName(self, name):
        return Control(self.env, name, self.frame, self.isLeft)

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
        self.emit : Dict[str, Emitter] = {}

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
        self.emit[self.className] = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)

    def emitObjectInit(self, o: Control):
        emit = self.emit[o.name]
        o = o.newFrame("<init>", VoidType())
        frame = o.frame
        emit.printout(emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        o = o.enterScope(True)
        emit.printout(emit.emitVAR(frame.getNewIndex(), "this", ClassType(o.name), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        emit.printout(emit.emitLABEL(frame.getStartLabel(), frame))
        emit.printout(emit.emitREADVAR("this", ClassType(o.name), 0, frame))
        emit.printout(emit.emitINVOKESPECIAL(frame))
    
        emit.printout(emit.emitLABEL(frame.getEndLabel(), frame))
        emit.printout(emit.emitRETURN(VoidType(), frame))
        emit.printout(emit.emitENDMETHOD(frame))
        o.frame.exitScope()

    def visitProgram(self, ast: Program, c):
        env = Control([c], self.className)
        # env['env'] = [c]
        Type = list(filter(lambda x: type(x) in [StructType, InterfaceType], ast.decl))
        env = reduce(lambda acc, ele: self.visit(ele, acc), Type, env)
        self.emit[env.name].printout(self.emit[env.name].emitPROLOG(self.className, "java.lang.Object"))
        notType = list(filter(lambda x: type(x) not in [StructType, InterfaceType], ast.decl))
        env = reduce(lambda acc, ele: self.visit(ele, acc), notType, env)
        self.emitObjectInit(env)
        self.emit[env.name].printout(self.emit[env.name].emitEPILOG())
        return env

    def visitFuncDecl(self, ast: FuncDecl, o: Control):
        env = o.newFrame(ast.name, ast.retType)
        isMain = ast.name == "main"
        emit = self.emit[o.name]
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        env.env[0].append(Symbol(ast.name, mtype, CName(self.className)))
        env = env.enterScope(True)
        emit.printout(emit.emitMETHOD(ast.name, mtype, True, env.frame))
        emit.printout(emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        if isMain:
            emit.printout(emit.emitVAR(env.frame.getNewIndex(), "args", ArrayType([None],StringType()), env.frame.getStartLabel(), env.frame.getEndLabel(), env.frame))
        else:
            env = reduce(lambda acc,e: self.visit(e, acc), ast.params, env)
        env = self.visit(ast.body, env)
        emit.printout(emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        if type(ast.retType) is VoidType:
            emit.printout(emit.emitRETURN(VoidType(), env.frame))
        emit.printout(emit.emitENDMETHOD(env.frame))
        env.frame.exitScope()
        return o
    
    def visitMethodDecl(self, ast: MethodDecl, o: Control):
        env = o.setName(ast.recType.name)
        emit = self.emit[env.name]
        func = ast.fun
        sym = next(filter(lambda x: x.name == ast.recType.name, o.env[-1]), None)
        assert isinstance(sym, Symbol), "Logical error"
        assert isinstance(sym.mtype, StructType), "Logical error"
        sym.mtype.methods.append(ast)
        recType = ClassType(ast.recType.name)
        mtype = MType(list(map(lambda x: x.parType, func.params)), func.retType)
        env = env.newFrame(func.name, func.retType)
        emit.printout(emit.emitMETHOD(func.name, mtype, False, env.frame))
        env = env.enterScope(True)
        emit.printout(emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        index = env.frame.getNewIndex()
        env.env[0].append(Symbol(ast.receiver, recType, Index(index)))
        emit.printout(emit.emitVAR(index, ast.receiver, recType, env.frame.getStartLabel(), env.frame.getEndLabel(), env.frame))
        env = env.enterScope(False)
        emit.printout(emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        env = reduce(lambda acc, e: self.visit(e, acc), func.params, env)
        env = self.visit(func.body, env)
        emit.printout(emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        env.frame.exitScope()
        if type(func.retType) is VoidType:
            emit.printout(emit.emitRETURN(VoidType(), env.frame))
        emit.printout(emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        emit.printout(emit.emitENDMETHOD(env.frame))
        env.frame.exitScope()
        emit.emitEPILOG()
        return o

    def visitParamDecl(self, ast: ParamDecl, o: Control):
        emit = self.emit[o.name]
        index = o.frame.getNewIndex()
        parType = self.visit(ast.parType, o)
        emit.printout(emit.emitVAR(index, ast.parName, parType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        o.env[0].append(Symbol(ast.parName, parType, Index(index)))
        return o

    def visitVarDecl(self, ast: VarDecl, o: Control):
        emit = self.emit[o.name]
        if not o.frame: # global var
            o.env[0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
            emit.printout(emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value) if ast.varInit else None))
        else:
            frame = o.frame
            index = frame.getNewIndex()
            varType = self.visit(ast.varType, o) if ast.varType else None
            if ast.varType:
                emit.printout(emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            if ast.varInit:
                varInitCode, varInitType = self.visit(ast.varInit, o.setLeft(False))
                if not varType:
                    emit.printout(emit.emitVAR(index, ast.varName, varInitType, frame.getStartLabel(), frame.getEndLabel(), frame))
                if not varType or isinstance(varType, ClassType):
                    varType = varInitType
                emit.printout(varInitCode)
                if isinstance(varInitType, IntType) and isinstance(varType, FloatType):
                    emit.printout(emit.emitI2F(o.frame))
                emit.printout(emit.emitWRITEVAR(ast.varName, varType, index, frame))
            o.env[0].append(Symbol(ast.varName, varType, Index(index)))
            if ast.varInit:
                if isinstance(varInitType, ArrayType) and isinstance(varType, ArrayType) and isinstance(ast.varInit, ArrayLiteral):
                    emit.printout(self.writeArray(Id(ast.varName), ast.varInit, o))
                elif isinstance(varInitType, ClassType) and isinstance(ast.varInit, StructLiteral):
                    emit.printout(self.writeStruct(Id(ast.varName), ast.varInit, o))
        return o
    
    def visitConstDecl(self, ast: ConstDecl, o: Control):
        emit = self.emit[o.name]
        if not o.frame: # global var
            o.env[0].append(Symbol(ast.conName, self.visit(ast.conType, o), CName(self.className)))
            emit.printout(emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, str(ast.iniExpr.value) if ast.iniExpr else None))
        else:
            frame = o.frame
            index = frame.getNewIndex()
            varType = self.visit(ast.conType, o) if ast.conType else None
            varInitCode, varInitType = self.visit(ast.iniExpr, o.setLeft(False))
            emit.printout(emit.emitVAR(index, ast.conName, varType if varType else varInitType, frame.getStartLabel(), frame.getEndLabel(), frame))
            if not varType or isinstance(varType, ClassType):
                varType = varInitType
            emit.printout(varInitCode)
            if isinstance(varInitType, IntType) and isinstance(varType, FloatType):
                emit.printout(emit.emitI2F(o.frame))
            emit.printout(emit.emitWRITEVAR(ast.conName, varType, index, frame))
            o.env[0].append(Symbol(ast.conName, varType, Index(index)))
            if isinstance(varInitType, ArrayType) and isinstance(varType, ArrayType) and isinstance(ast.iniExpr, ArrayLiteral):
                # readVar = emit.emitREADVAR(ast.conName, varType, index, o.frame)
                # emit.printout(self.writeArray(readVar, varType, ast.conName, ast.iniExpr.value, o))
                emit.printout(self.writeArray(Id(ast.conName), ast.iniExpr, o))
            elif isinstance(varInitType, ClassType) and isinstance(ast.iniExpr, StructLiteral):
                emit.printout(self.writeStruct(Id(ast.conName), ast.iniExpr, o))
        return o
    
    def visitFuncCall(self, ast: FuncCall, o: Control):
        emit = self.emit[o.name]
        sym : Symbol = next(filter(lambda x: x.name == ast.funName, o.env[-1]),None)
        # env = o.copy()
        # env['isLeft'] = False
        env = o.setLeft(False)
        code = reduce(lambda acc, ele: acc + self.visit(ele, env)[0], ast.args, "")
        code += emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o.frame)
        if not isinstance(sym.mtype.rettype, VoidType):
            return code, sym.mtype.rettype
        else:
            emit.printout(code)
            return o
        # env = o.setLeft(False)
        # [emit.printout(self.visit(x, env)[0]) for x in ast.args]
        # emit.printout(emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o.frame))
        # return (o, sym.mtype.rettype) if not isinstance(sym.mtype.rettype, VoidType) else o

    def visitMethCall(self, ast: MethCall, o: Control):
        emit = self.emit[o.name]
        receiver, typ = self.visit(ast.receiver, o.setLeft(False))
        assert isinstance(typ, ClassType), "Logical error"
        sym = next(filter(lambda x: x.name == typ.name, o.env[-1]), None)
        assert isinstance(sym, Symbol), "Logical error"
        assert isinstance(sym.mtype, StructType), "Logical error"
        fun = next(filter(lambda x: x.fun.name == ast.metName, sym.mtype.methods), None).fun
        parType = list(map(lambda x: x.parType, fun.params))
        retType = fun.retType
        mtype = MType(parType, retType)        
        args = reduce(lambda acc, ele: acc + self.visit(ele, o)[0], ast.args, "")
        code = emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, o.frame)
        if not isinstance(retType, VoidType):
            return receiver + args + code, retType
        else:
            emit.printout(receiver)
            emit.printout(args)
            emit.printout(code)
            return o

    def visitIntType(self, ast: IntType, o: Control):
        return IntType()
    
    def visitFloatType(self, ast: FloatType, o: Control):
        return FloatType()
    
    def visitStringType(self, ast: StringType, o: Control):
        return StringType()
    
    def visitBoolType(self, ast: BoolType, o: Control):
        return BoolType()
    
    def visitArrayType(self, ast: ArrayType, o: Control):
        return ast
    
    def visitInterfaceType(self, ast: InterfaceType, o: Control):
        o.env[0].append(Symbol(ast.name, ast, CName(ast.name)))
        return o
    
    def visitStructType(self, ast: StructType, o: Control):
        o.env[0].append(Symbol(ast.name, ast, CName(ast.name)))
        self.emit[ast.name] = Emitter(self.path + "/" + ast.name + ".j")
        env = o.setName(ast.name)
        emit = self.emit[ast.name]
        emit.printout(emit.emitPROLOG(ast.name, "java.lang.Object"))
        list(map(lambda x: emit.printout(emit.emitFIELD(x[0], x[1], False, None, env.frame)), ast.elements))
        self.emitObjectInit(env)
        emit.emitEPILOG()
        return o
    
    def visitBlock(self, ast: Block, o: Control):
        emit = self.emit[o.name]
        env = o.enterScope(False)
        emit.printout(emit.emitLABEL(env.frame.getStartLabel(), env.frame))
        env = reduce(lambda acc, e: self.visit(e, acc), ast.member, env)
        emit.printout(emit.emitLABEL(env.frame.getEndLabel(), env.frame))
        env.frame.exitScope()
        return o
    
    def visitAssign(self, ast: Assign, o: Control):
        emit = self.emit[o.name]
        _, rtype = self.visit(ast.rhs, o.setLeft(False))
        if isinstance(ast.lhs, Id) and next(filter(lambda x: x.name == ast.lhs.name, [j for i in o.env for j in i]), None) is None:
            index = o.frame.getNewIndex()
            emit.printout(emit.emitVAR(index, ast.lhs.name, rtype, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            o.env[0].append(Symbol(ast.lhs.name, rtype, Index(index)))
        emit.printout(self.assign(ast.lhs, ast.rhs, o))
        if isinstance(rtype, ArrayType) and isinstance(ast.rhs, ArrayLiteral):
            emit.printout(self.writeArray(ast.lhs, ast.rhs, o))
        elif isinstance(rtype, ClassType) and isinstance(ast.rhs, StructLiteral):
            emit.printout(self.writeStruct(ast.lhs, ast.rhs, o))
        return o

    def visitIf(self, ast: If, o: Control):
        pass

    def visitForBasic(self, ast: ForBasic, o: Control):
        pass

    def visitForStep(self, ast: ForStep, o: Control):
        pass

    def visitForEach(self, ast: ForEach, o: Control):
        pass

    def visitBreak(self, ast: Break, o: Control):
        pass 

    def visitContinue(self, ast: Continue, o: Control):
        pass

    def visitReturn(self, ast: Return, o: Control):
        emit = self.emit[o.name]
        if ast.expr:
            code, typ = self.visit(ast.expr, o.setLeft(False))
            emit.printout(code)
            emit.printout(emit.emitRETURN(typ, o.frame))
        else:
            emit.printout(emit.emitRETURN(VoidType(), o.frame))
        return o

    def visitId(self, ast: Id, o: Control):
        emit = self.emit[o.name]
        # sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o.env for j in i]), None)
        if type(sym.mtype) in [InterfaceType, StructType]:
            return ClassType(sym.mtype.name)
        if o.isLeft is None:
            raise Exception("Illegal Access")
        if not o.isLeft:
            if type(sym.value) is Index:
                return emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o.frame), sym.mtype
            else:
                return emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o.frame), sym.mtype
        else:
            if type(sym.value) is Index:
                return "", emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o.frame), sym.mtype
            else:
                return "", emit.emitPUTSTATIC(f"{self.className}/{sym.name}",sym.mtype,o.frame), sym.mtype
            
    def visitArrayCell(self, ast: ArrayCell, o: Control):
        emit = self.emit[o.name]
        arr, typ = self.visit(ArrayCell(ast.arr, ast.idx[:-1]), o.setLeft(False)) if len(ast.idx) > 1 else self.visit(ast.arr, o.setLeft(False))
        index, _ = self.visit(ast.idx[-1], o.setLeft(False))
        cellType = ArrayType(typ.dimens[1:], typ.eleType) if len(typ.dimens) > 1 else typ.eleType
        if o.isLeft:
            return arr + index, emit.emitASTORE(cellType, o.frame), cellType
        else:
            return arr + index + emit.emitALOAD(cellType, o.frame), cellType

    def visitFieldAccess(self, ast: FieldAccess, o: Control):
        emit = self.emit[o.name]
        receiver, typ = self.visit(ast.receiver, o.setLeft(False))
        assert isinstance(typ, ClassType), "Logical error"
        sym = next(filter(lambda x: x.name == typ.name, o.env[-1]), None)
        fieldType = next(filter(lambda x: x[0] == ast.field, sym.mtype.elements), None)[1]
        if isinstance(fieldType, StructType): fieldType = ClassType(fieldType.name)
        if not o.isLeft:
            return receiver + emit.emitGETFIELD(f"{typ.name}.{ast.field}", fieldType, o.frame), fieldType
        else:
            return receiver, emit.emitPUTFIELD(f"{typ.name}.{ast.field}", fieldType, o.frame), fieldType
        
    def visitBinaryOp(self, ast: BinaryOp, o: Control):
        emit = self.emit[o.name]
        if ast.op in ["&&", "||"]:
            outLabel = o.frame.getNewLabel()
            cond, then, else_, _ = self.visitCond(ast, o)
            return cond + then + emit.emitPUSHICONST(1, o.frame) + emit.emitGOTO(outLabel, o.frame) + else_ + emit.emitPUSHICONST(0, o.frame) + emit.emitLABEL(outLabel, o.frame), BoolType()
        left, ltype = self.visit(ast.left, o.setLeft(False))
        right, rtype = self.visit(ast.right, o.setLeft(False))
        assert not isinstance(ltype, BoolType) and not isinstance(rtype, BoolType), "Logical error"
        if ast.op in ["==", "!=", "<", "<=", ">", ">="]:
            return left + right + emit.emitREOP(ast.op, ltype, o.frame), BoolType()
        elif ast.op == "+" and isinstance(ltype, StringType) and isinstance(rtype, StringType):
            raise Exception("Not yet implemented")
        else:
            retType = FloatType() if isinstance(ltype, FloatType) else rtype
            if type(retType) != type(ltype):
                left += emit.emitI2F(o.frame)
            if type(retType) != type(rtype):
                right += emit.emitI2F(o.frame)
            if ast.op in ["+", "-"]:
                return left + right + emit.emitADDOP(ast.op, retType, o.frame), retType
            elif ast.op in ["*", "/"]:
                return left + right + emit.emitMULOP(ast.op, retType, o.frame), retType
            elif ast.op == "%":
                return left + right + emit.emitMOD(o.frame), IntType()
            else:
                raise Exception(f"Logical error: {ast}")

    def visitUnaryOp(self, ast: UnaryOp, o: Control):
        emit = self.emit[o.name]
        if ast.op == "!":
            outLabel = o.frame.getNewLabel()
            cond, then, else_, _ = self.visitCond(ast, o)
            return cond + then + emit.emitPUSHICONST(1, o.frame) + emit.emitGOTO(outLabel, o.frame) + else_ + emit.emitPUSHICONST(0, o.frame) + emit.emitLABEL(outLabel, o.frame), BoolType()
        else:
            expr, typ = self.visit(ast.body, o)
            return expr + emit.emitNEGOP(typ, o.frame), typ

    def visitCond(self, ast, o: Control):
        emit = self.emit[o.name]
        trueLabel = o.frame.getNewLabel()
        falseLabel = o.frame.getNewLabel()
        if isinstance(ast, BinaryOp):
            if ast.op in ["==", "!=", "<", "<=", ">", ">="]:
                left, ltype = self.visit(ast.left, o.setLeft(False))
                right, _ = self.visit(ast.right, o.setLeft(False))
                return left + right + emit.emitRELOP(ast.op, ltype, trueLabel, falseLabel, o.frame), emit.emitLABEL(trueLabel, o.frame), emit.emitLABEL(falseLabel, o.frame), BoolType()
            elif ast.op == "||":
                left, then1, else1, _ = self.visitCond(ast.left, o)
                right, then2, else2, _ = self.visitCond(ast.right, o)
                return left, then1 + emit.emitLABEL(trueLabel, o.frame) + then2, else1 + right + emit.emitLABEL(falseLabel, o.frame) + else2, BoolType()
            elif ast.op == "&&":
                left, then1, else1, _ = self.visitCond(ast.left, o)
                right, then2, else2, _ = self.visitCond(ast.right, o)
                return left, then1 + right + emit.emitLABEL(trueLabel, o.frame) + then2, else1 + emit.emitLABEL(falseLabel, o.frame) + else2, BoolType()

        elif isinstance(ast, UnaryOp):
            if ast.op == "!":
                cond, then1, else1, _ = self.visitCond(ast.body, o)
                return cond, then1 + emit.emitGOTO(falseLabel, o.frame) + emit.emitLABEL(trueLabel, o.frame), else1 + emit.emitGOTO(trueLabel, o.frame) + emit.emitLABEL(falseLabel, o.frame), BoolType()

        elif isinstance(ast, BooleanLiteral):
            label = trueLabel if ast.value else falseLabel
            return emit.emitGOTO(label, o.frame), emit.emitLABEL(trueLabel, o.frame), emit.emitLABEL(falseLabel, o.frame), BoolType()

        raise Exception(ast)

    def visitIntLiteral(self, ast: IntLiteral, o: Control):
        return self.emit[o.name].emitPUSHICONST(ast.value, o.frame), IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o: Control):
        return self.emit[o.name].emitPUSHFCONST(ast.value, o.frame), FloatType()
    
    def visitStringLiteral(self, ast: StringLiteral, o: Control):
        return self.emit[o.name].emitPUSHSTRCONST(ast.value, o.frame), StringType()
    
    def visitBoolLiteral(self, ast: BooleanLiteral, o:Control):
        if ast.value:
            return self.emit[o.name].emitPUSHICONST(1, o.frame), BoolType()
        else:
            return self.emit[o.name].emitPUSHICONST(0, o.frame), BoolType()
    
    def visitStructLiteral(self, ast: StructLiteral, o: Control):
        return self.emit[o.name].emitPUSHSTRUCTLIT(ast.name, o.frame), ClassType(ast.name)
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o: Control):
        typ = ast.eleType
        dimens_code = reduce(lambda acc, ele: acc + self.visit(ele, o)[0], ast.dimens, "")
        return dimens_code + self.emit[o.name].emitPUSHARRAYCONST(typ, len(ast.dimens), o.frame), ArrayType(ast.dimens, typ)
    
    def visitNilLiteral(self, ast: NilLiteral, o: Control):
        return self.emit[o.name].emitPUSHNIL(o.frame), VoidType()
    
    def writeArray(self, lhs, rhs: ArrayLiteral, o: Control):
        code = ""
        dimens = self.getDimens(rhs.value)
        eleNum = reduce(lambda acc, ele: acc * ele, dimens, 1)
        for i in range(eleNum):
            indicesLst = []
            DIV = 1        
            for j in reversed(dimens):
                DIV *= j
                indicesLst.append(i % DIV)
                i //= DIV
            indicesLst.reverse()
            ele = rhs.value
            for idx in indicesLst:
                ele = ele[idx]
            indicesLst = list(map(lambda x: IntLiteral(x), indicesLst))
            code += self.assign(ArrayCell(lhs, indicesLst), ele, o)
        return code
    
    def getElements(self, elements, o: Control):
        if not isinstance(elements, list):
            return self.visit(elements, o)[0]
        return list(map([self.getElements(x, o)[0] for x in elements], elements))
    
    def getDimens(self, value):
        if not isinstance(value, list):
            return []
        return [len(value)] + self.getDimens(value[0])
    
    def writeStruct(self, lhs, rhs: StructLiteral, o: Control):
        code = ""
        for field, value in rhs.elements:
            code += self.assign(FieldAccess(lhs, field), value, o)
        return code
    
    def assign(self, lhs, rhs, o: Control):
        emit = self.emit[o.name]
        loadrhs, rtype = self.visit(rhs, o.setLeft(False))
        loadlhs, storelhs, ltype = self.visit(lhs, o.setLeft(True))
        i2f = emit.emitI2F(o.frame) if isinstance(ltype, FloatType) and isinstance(rtype, IntType) else ""
        return loadlhs + loadrhs + i2f + storelhs