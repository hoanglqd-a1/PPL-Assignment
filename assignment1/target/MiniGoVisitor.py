# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_lst.
    def visitDecl_lst(self, ctx:MiniGoParser.Decl_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#tail.
    def visitTail(self, ctx:MiniGoParser.TailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_access_tail.
    def visitField_access_tail(self, ctx:MiniGoParser.Field_access_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arridx_nnlst.
    def visitArridx_nnlst(self, ctx:MiniGoParser.Arridx_nnlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arridx.
    def visitArridx(self, ctx:MiniGoParser.ArridxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccall_tail.
    def visitFunccall_tail(self, ctx:MiniGoParser.Funccall_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_lst.
    def visitExpr_lst(self, ctx:MiniGoParser.Expr_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr_lstprime.
    def visitExpr_lstprime(self, ctx:MiniGoParser.Expr_lstprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#withInit_var_decl.
    def visitWithInit_var_decl(self, ctx:MiniGoParser.WithInit_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#withoutInit_var_decl.
    def visitWithoutInit_var_decl(self, ctx:MiniGoParser.WithoutInit_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcparam.
    def visitFuncparam(self, ctx:MiniGoParser.FuncparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_lst.
    def visitParam_lst(self, ctx:MiniGoParser.Param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_lstprime.
    def visitParam_lstprime(self, ctx:MiniGoParser.Param_lstprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id_nnlst.
    def visitId_nnlst(self, ctx:MiniGoParser.Id_nnlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structfield.
    def visitStructfield(self, ctx:MiniGoParser.StructfieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fielddecl_nnlst.
    def visitFielddecl_nnlst(self, ctx:MiniGoParser.Fielddecl_nnlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fielddecl.
    def visitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacemeth.
    def visitInterfacemeth(self, ctx:MiniGoParser.InterfacemethContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacemeth_nnlst.
    def visitInterfacemeth_nnlst(self, ctx:MiniGoParser.Interfacemeth_nnlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacemethmem.
    def visitInterfacemethmem(self, ctx:MiniGoParser.InterfacemethmemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assigning_stmt.
    def visitAssigning_stmt(self, ctx:MiniGoParser.Assigning_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifelse_stmt.
    def visitIfelse_stmt(self, ctx:MiniGoParser.Ifelse_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_.
    def visitIf_(self, ctx:MiniGoParser.If_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif_.
    def visitElseif_(self, ctx:MiniGoParser.Elseif_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif_lst.
    def visitElseif_lst(self, ctx:MiniGoParser.Elseif_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_.
    def visitElse_(self, ctx:MiniGoParser.Else_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ForBasic.
    def visitForBasic(self, ctx:MiniGoParser.ForBasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ForStep.
    def visitForStep(self, ctx:MiniGoParser.ForStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ForEach.
    def visitForEach(self, ctx:MiniGoParser.ForEachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forloop_init.
    def visitForloop_init(self, ctx:MiniGoParser.Forloop_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccall_stmt.
    def visitFunccall_stmt(self, ctx:MiniGoParser.Funccall_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockcode.
    def visitBlockcode(self, ctx:MiniGoParser.BlockcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_nnlst.
    def visitStmt_nnlst(self, ctx:MiniGoParser.Stmt_nnlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_literal.
    def visitArr_literal(self, ctx:MiniGoParser.Arr_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrvalue.
    def visitArrvalue(self, ctx:MiniGoParser.ArrvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrelem_lst.
    def visitArrelem_lst(self, ctx:MiniGoParser.Arrelem_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrelem.
    def visitArrelem(self, ctx:MiniGoParser.ArrelemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structparam_lst.
    def visitStructparam_lst(self, ctx:MiniGoParser.Structparam_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structparam_lstprime.
    def visitStructparam_lstprime(self, ctx:MiniGoParser.Structparam_lstprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structparam.
    def visitStructparam(self, ctx:MiniGoParser.StructparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_type.
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#prime_datatype.
    def visitPrime_datatype(self, ctx:MiniGoParser.Prime_datatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_datatype.
    def visitPrimitive_datatype(self, ctx:MiniGoParser.Primitive_datatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compare_op.
    def visitCompare_op(self, ctx:MiniGoParser.Compare_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#end_stm.
    def visitEnd_stm(self, ctx:MiniGoParser.End_stmContext):
        return self.visitChildren(ctx)



del MiniGoParser