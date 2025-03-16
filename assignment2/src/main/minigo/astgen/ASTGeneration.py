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
            ctx.interface_decl()   
        )

        assert decl is not None

        return self.visit(decl)
    
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        stmt = (
            ctx.var_decl()          or
            ctx.const_decl()        or
            ctx.assigning_stmt()    or
            ctx.ifelse_stmt()       or
            ctx.break_stmt()        or
            ctx.forloop_stmt()      or
            ctx.continue_stmt()     or
            ctx.break_stmt()        or
            ctx.funccall_stmt()     or
            ctx.return_stmt()       
        )

        return self.visit(stmt)
    
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
        if not ctx.expr4():
            return self.visit(ctx.expr5())
        #ctx.getChild(1) == MUL || DIV || MOD
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
    
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        #ctx.getChild(0) == NOT | SUB
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.expr5()))
    
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        returnAnswer = None
        if ctx.expr7():
            returnAnswer = self.visit(ctx.expr7())
        elif ctx.field_access_tail():
            returnAnswer = FieldAccess(self.visit(ctx.expr6()),self.visit(ctx.field_access_tail()))
        else:
            node = self.visit(ctx.expr6())
            if isinstance(node,Id):
                returnAnswer = FuncCall(node.name,self.visit(ctx.funccall_tail()))
            elif isinstance(node,FieldAccess):
                returnAnswer = MethCall(node.receiver,node.field,self.visit(ctx.funccall_tail()))
            else:
                returnAnswer = FuncCall(str(node),self.visit(ctx.funccall_tail()))
        
        if ctx.arridx_nnlst():
            returnAnswer = ArrayCell(returnAnswer,self.visit(ctx.arridx_nnlst()))
        
        return returnAnswer
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        
        if ctx.literal():
            return self.visit(ctx.literal())
        
        return Id(ctx.ID().getText())
    
    def visitField_access_tail(self, ctx:MiniGoParser.Field_access_tailContext):
        return ctx.ID().getText()
    
    def visitArridx_nnlst(self, ctx:MiniGoParser.Arridx_nnlstContext):
        if ctx.arridx_nnlst():
            return [self.visit(ctx.arridx())] + self.visit(ctx.arridx_nnlst())
        
        return [self.visit(ctx.arridx())]
    
    def visitArridx(self, ctx:MiniGoParser.ArridxContext):
        return self.visit(ctx.expr())
    
    def visitFunccall_tail(self, ctx:MiniGoParser.Funccall_tailContext):
        return self.visit(ctx.expr_lst())

    def visitExpr_lst(self, ctx:MiniGoParser.Expr_lstContext):
        return self.visit(ctx.expr_lstprime()) if ctx.expr_lstprime() else []
    
    def visitExpr_lstprime(self, ctx:MiniGoParser.Expr_lstprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_lstprime())

    def visitAssigning_stmt(self, ctx:MiniGoParser.Assigning_stmtContext):
        # return Assign([self.visit(ctx.lhs()),self.visit(ctx.expr())])
        assign = ctx.assign().getText()
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())
        if assign == ":=":
            return Assign(lhs,expr)
        elif assign == "+=":
            return Assign(lhs,BinaryOp('+',lhs,expr))
        elif assign == "-=":
            return Assign(lhs,BinaryOp('-',lhs,expr))
        elif assign == "*=":
            return Assign(lhs,BinaryOp('*',lhs,expr))
        elif assign == "/=":
            return Assign(lhs,BinaryOp('/',lhs,expr))
        elif assign == "%=":
            return Assign(lhs,BinaryOp('%',lhs,expr))
        else:
            raise Exception("Unknown assignment operator: " + assign)
    
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())

        if ctx.field_access_tail():
            return FieldAccess(self.visit(ctx.expr6()),self.visit(ctx.field_access_tail()))
        
        return ArrayCell(self.visit(ctx.expr6()),self.visit(ctx.arridx_nnlst()))
    
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visit(ctx.withInit_var_decl() if ctx.withInit_var_decl() else ctx.withoutInit_var_decl())
    def visitWithInit_var_decl(self, ctx:MiniGoParser.WithInit_var_declContext):
        return VarDecl(ctx.ID().getText(),self.visit(ctx.data_type()) if ctx.data_type() else None,self.visit(ctx.expr()))

    def visitWithoutInit_var_decl(self, ctx:MiniGoParser.WithoutInit_var_declContext):
        return VarDecl(ctx.ID().getText(),self.visit(ctx.data_type()),None)
    
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return ConstDecl(ctx.ID().getText(),self.visit(ctx.data_type()) if ctx.data_type() else None,self.visit(ctx.expr()))
    
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
            return self.visit(ctx.param()) + self.visit(ctx.param_lstprime())
        
        return self.visit(ctx.param())
    
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
        return ctx.ID(0).getText(),Id(ctx.ID(1).getText())   

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
    
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return InterfaceType(ctx.ID().getText(),self.visit(ctx.interfacemeth()))

    def visitInterfacemeth(self, ctx:MiniGoParser.InterfacemethContext):
        return self.visit(ctx.interfacemeth_nnlst())
    
    def visitInterfacemeth_nnlst(self, ctx:MiniGoParser.Interfacemeth_nnlstContext):
        if ctx.interfacemeth_nnlst():
            return [self.visit(ctx.interfacemethmem())] + self.visit(ctx.interfacemeth_nnlst())
        
        return [self.visit(ctx.interfacemethmem())]
    
    def visitInterfacemethmem(self, ctx:MiniGoParser.InterfacemethmemContext):
        param_lst = self.visit(ctx.funcparam())
        type_lst  = []
        for param in param_lst:
            assert isinstance(param,ParamDecl)
            type_lst.append(param.parType)

        return Prototype(ctx.ID().getText(),type_lst,self.visit(ctx.data_type()) if ctx.data_type() else VoidType())
    
    def visitIfelse_stmt(self, ctx:MiniGoParser.Ifelse_stmtContext):
        if_condition, then_blockcode = self.visit(ctx.if_())
        elseif_stmt_lst = self.visit(ctx.elseif_lst())
        else_stmt = self.visit(ctx.else_()) if ctx.else_() else None
        for elseif_stmt in reversed(elseif_stmt_lst):
            elseif_condition, elseif_thenblockcode = elseif_stmt
            else_stmt = If(elseif_condition,elseif_thenblockcode,else_stmt)
        
        return If(if_condition,then_blockcode,else_stmt)
    
    def visitIf_(self, ctx:MiniGoParser.If_Context):
        return self.visit(ctx.condition()),self.visit(ctx.blockcode())
    
    def visitElseif_lst(self, ctx:MiniGoParser.Elseif_lstContext):
        if not ctx.elseif_():
            return []
        
        return [self.visit(ctx.elseif_())] + self.visit(ctx.elseif_lst())
    
    def visitElseif_(self, ctx:MiniGoParser.Elseif_Context):
        return self.visit(ctx.condition()),self.visit(ctx.blockcode())
    
    def visitElse_(self, ctx:MiniGoParser.Else_Context):
        return self.visit(ctx.blockcode())
    
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visit(ctx.expr())
    
    def visitForBasic(self, ctx:MiniGoParser.ForBasicContext):
        return ForBasic(self.visit(ctx.expr()),self.visit(ctx.blockcode()))
    
    def visitForStep(self, ctx:MiniGoParser.ForStepContext):
        return ForStep(self.visit(ctx.forloop_init()),self.visit(ctx.expr()),self.visit(ctx.assigning_stmt()),self.visit(ctx.blockcode()))
    
    def visitForEach(self, ctx:MiniGoParser.ForEachContext):
        return ForEach(Id(ctx.ID(0).getText()),Id(ctx.ID(1).getText()),self.visit(ctx.expr()),self.visit(ctx.blockcode()))

    def visitForloop_init(self, ctx:MiniGoParser.Forloop_initContext):
        return self.visit(ctx.withInit_var_decl() if ctx.withInit_var_decl() else ctx.assigning_stmt())

    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return Continue()
    
    def visitFunccall_stmt(self, ctx:MiniGoParser.Funccall_stmtContext):
        if ctx.expr6():
            return MethCall(self.visit(ctx.expr6()),ctx.ID().getText(),self.visit(ctx.funccall_tail()))
        
        return FuncCall(ctx.ID().getText(),self.visit(ctx.funccall_tail()))
    
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)
    
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return ctx.getChild(0).getText()
    
    def visitBlockcode(self, ctx:MiniGoParser.BlockcodeContext):
        return Block(self.visit(ctx.stmt_nnlst()))
    
    def visitStmt_nnlst(self, ctx:MiniGoParser.Stmt_nnlstContext):
        if ctx.stmt_nnlst():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_nnlst())
        
        return [self.visit(ctx.stmt())]
    
    def visitArr_literal(self, ctx:MiniGoParser.Arr_literalContext):
        return ArrayLiteral(self.visit(ctx.arridx_nnlst()),self.visit(ctx.prime_datatype()),self.visit(ctx.arrvalue()))
    
    def visitArrvalue(self, ctx:MiniGoParser.ArrvalueContext):
        return self.visit(ctx.arrelem_lst())
    
    def visitArrelem_lst(self, ctx:MiniGoParser.Arrelem_lstContext):
        if ctx.arrelem_lst():
            return [self.visit(ctx.arrelem())] + self.visit(ctx.arrelem_lst())
        
        return [self.visit(ctx.arrelem())]
    
    def visitArrelem(self, ctx:MiniGoParser.ArrelemContext):
        return self.visit(ctx.expr()) if ctx.expr() else self.visit(ctx.arrvalue())
    
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return StructLiteral(ctx.ID().getText(),self.visit(ctx.structparam_lst()))
    
    def visitStructparam_lst(self, ctx:MiniGoParser.Structparam_lstContext):
        return self.visit(ctx.structparam_lstprime()) if ctx.structparam_lstprime() else []
    
    def visitStructparam_lstprime(self, ctx:MiniGoParser.Structparam_lstprimeContext):
        if ctx.structparam_lstprime():
            return [self.visit(ctx.structparam())] + self.visit(ctx.structparam_lstprime())
        
        return [self.visit(ctx.structparam())]
    
    def visitStructparam(self, ctx:MiniGoParser.StructparamContext):
        return (ctx.ID().getText(),self.visit(ctx.expr()))
        
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        if ctx.arridx_nnlst():
            return ArrayType(self.visit(ctx.arridx_nnlst()),self.visit(ctx.prime_datatype()))
        
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
            return IntLiteral(int(ctx.INTEGER().getText(),0))
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
        
    def visitCompare_op(self, ctx:MiniGoParser.Compare_opContext):
        return ctx.getChild(0).getText()