from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.decl_lst()))

    def visitDecl_lst(self,ctx:MiniGoParser.Decl_lstContext):
        if ctx.decl_lst():
            return [self.visit(ctx.decl())] + self.visit(ctx.decl_lst())
        
        return [self.visit(ctx.decl())]
        
    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        decl = (
            ctx.var_decl()      or
            ctx.const_decl()    or
            ctx.func_decl()     or
            ctx.struct_decl()   or
            ctx.interf_decl()   
        )

        return self.visit(decl)
    
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1())
        
        return BinaryOp(ctx.OR().getText(),self.visit(ctx.expr()),self.visit(ctx.expr1()))
        
    def visitExpr1(self,ctx:MiniGoParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2())
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.expr1()),self.visit(ctx.expr2()))

    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        return BinaryOp(self.visit(ctx.compare_op()),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
    
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        #ctx.getChild(1) == ADD || SUB
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
    
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        #ctx.getChild(1) == MUL || DIV || MOD
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr4),self.visit(ctx.expr5()))
    
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        #ctx.getChild(0) == NOT | SUB
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.expr6()))
    
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        
        tail_node = ctx.tail()
        if isinstance(tail_node, MiniGoParser.Field_access_tailContext):
            return FieldAccess(self.visit(ctx.expr6(),self.visit(tail_node)))
        
        if isinstance(tail_node, MiniGoParser.Arr_elem_accessContext):
            return ArrayCell(self.visit(ctx.expr6(),self.visit(tail_node)))
        
        head_node = ctx.expr6()
        if head_node.expr6() and isinstance(head_node.tail(),MiniGoParser.Field_access_tailContext()):
            return MethCall(self.visit(head_node.expr6()),self.visit(head_node.tail()),self.visit(tail_node))

        return FuncCall(self.visit(head_node),self.visit(tail_node))
    
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr()),ctx.RP()
        
        if ctx.literal():
            return self.visit(ctx.literal())
        
        return Id(ctx.ID().getText())
    
    def visitTail(self, ctx:MiniGoParser.TailContext):
        #ctx.getChild() == field_access_tail | arr_elem_access | funccall_tail
        return self.visit(ctx.getChild(0))
    
    def visitField_access_tail(self, ctx:MiniGoParser.Field_access_tailContext):
        return Id(ctx.ID().getText())
    
    def visitArr_elem_access(self, ctx:MiniGoParser.Arr_elem_accessContext):
        return self.visit(ctx.expr())
    
    def visitFunccall_tail(self, ctx:MiniGoParser.Funccall_tailContext):
        return self.visit(ctx.expr_lst())

    def visitExpr_lst(self, ctx:MiniGoParser.Expr_lstContext):
        return self.visit(ctx.expr_lstprime()) if ctx.getChildCount() == 1 else None
    
    def visitExpr_lstprime(self, ctx:MiniGoParser.Expr_lstprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_lstprime())

    def visitAssigning_stmt(self, ctx:MiniGoParser.Assigning_stmtContext):
        return Assign([self.visit(ctx.lhs()),self.visit(ctx.expr())])
    
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())

        if ctx.field_access_tail():
            return FieldAccess(self.visit(ctx.expr6()),self.visit(ctx.field_access_tail()))
        
        return ArrayCell(self.visit(ctx.expr6()),self.visit(ctx.arr_elem_access()))
    
    def visitType_Var_decl(self, ctx:MiniGoParser.Type_Var_declContext):
        return VarDecl(ctx.ID().getText(),self.visit(ctx.data_type()),None)

    def visitValue_Var_decl(self, ctx:MiniGoParser.Value_Var_declContext):
        return VarDecl(ctx.ID().getText(),None,self.visit(ctx.expr()))

    def visitTypeValue_Var_decl(self, ctx:MiniGoParser.TypeValue_Var_declContext):
        return VarDecl(ctx.ID().getText(),self.visit(ctx.data_type()),self.visit(ctx.expr()))
    
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        if not ctx.data_type():   
            return ConstDecl(ctx.ID().getText(),None,self.visit(ctx.expr()))
        
        return ConstDecl(ctx.ID().getText(),self.visit(ctx.data_type()),self.visit(ctx.expr()))
    
    def visitFunc_decl(self,ctx:MiniGoParser.Func_declContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.funcparam())
        retType = self.visit(ctx.data_type()) if ctx.data_type() else VoidType()
        body = self.visit(ctx.blockcode())
        if ctx.receiver():
            receiver, recType = self.visit(ctx.receiver())
            return MethodDecl(receiver,recType,FuncDecl(name,params,retType,body))
        
        return FuncDecl(name,params,retType,body)
    
    def visitFuncparam(self, ctx:MiniGoParser.FuncparamContext):
        return self.visit(ctx.param_lst())
    
    def visitParam_lst(self, ctx:MiniGoParser.Param_lstContext):
        return self.visit(ctx.param_lstprime()) if ctx.param_lstprime() else []
    
    def visitParam_lstprime(self, ctx:MiniGoParser.Param_lstprimeContext):
        if ctx.param_lstprime():
            return [self.visit(ctx.param())] + self.visit(ctx.param_lstprime())
        
        return [self.visit(ctx.param())]
    
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        id_lst = self.visit(ctx.id_nnlst())
        datatype = self.visit(ctx.data_type())
        ParamDecl_lst = []
        for id in id_lst:
            ParamDecl_lst.append(ParamDecl(id,datatype))
        
        return ParamDecl_lst
    
    def visitId_nnlst(self, ctx:MiniGoParser.Id_nnlstContext):
        if ctx.id_nnlst():
            return [ctx.ID().getText()] + self.visit(ctx.id_nnlst())
        
        return [ctx.ID().getText()]
    
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return ctx.ID(0).getText(),ctx.ID(1).getText()       

    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return StructType(ctx.ID().getText(),self.visit(ctx.structfield()),[])
    
    def visitStructfield(self, ctx:MiniGoParser.StructfieldContext):
        return self.visit(ctx.fielddecl_nnlst())
    
    def visitFielddecl_nnlst(self, ctx:MiniGoParser.Fielddecl_nnlstContext):
        if ctx.fielddecl_nnlst():
            return [self.visit(ctx.fielddecl())] + self.visit(ctx.fielddecl_nnlst())
        
        return [self.visit(ctx.fielddecl())]
    
    def visitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        return [ctx.ID().getText(),self.visit(ctx.data_type())]

    def visitBlockcode(self, ctx:MiniGoParser.BlockcodeContext):
        return Block(self.visit(ctx.blockcodestmt_nnlst()))
    
    def visitBlockcodestmt_nnlst(self, ctx:MiniGoParser.Blockcodestmt_nnlstContext):
        if ctx.blockcodestmt_nnlst():
            return [self.visit(ctx.blockcodestmt())] + self.visit(ctx.blockcodestmt_nnlst())
        
        return [self.visit(ctx.blockcodestmt())]
    
    def visitBlockcodestmt(self, ctx:MiniGoParser.BlockcodestmtContext):
        stmt = (
            ctx.assigning_stmt()    or
            ctx.var_decl()          or
            ctx.const_decl()        or
            ctx.assigning_stmt()    or
            ctx.ifelse_stmt()       or
            ctx.forloop_stmt()      or
            ctx.continue_stmt()     or
            ctx.return_stmt()       or
            ctx.break_stmt()        or
            ctx.funccall_stmt()     or
            ctx.return_stmt()       
        )
        
        return self.visit(stmt)
    
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        if ctx.arridx_lst():
            return ArrayType(self.visit(ctx.arridx_lst()),self.visit(ctx.prime_datatype()))
        
        return self.visit(ctx.prime_datatype())
    
    def visitPrime_datatype(self, ctx:MiniGoParser.Prime_datatypeContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        
        return self.visit(ctx.primitive_datatype())
    
    def visitPrimitive_datatype(self, ctx:MiniGoParser.Primitive_datatypeContext):
        if ctx.INT_():
            return IntType()
        elif ctx.FLOAT_():
            return FloatType()
        elif ctx.STRING_():
            return StringType()
        elif ctx.BOOLEAN_():
            return BoolType()
        else:
            raise Exception("Unknown data type")
        
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INTEGER():
            return IntLiteral(int(ctx.INTEGER().getText()))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.TRUE_():
            return BooleanLiteral(True)
        elif ctx.FALSE_():
            return BooleanLiteral(False)
        elif ctx.NIL_():
            return NilLiteral()
        else:
            return self.visit(ctx.getChild(0))
        
        