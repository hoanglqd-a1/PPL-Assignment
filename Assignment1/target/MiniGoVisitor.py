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


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr0.
    def visitExpr0(self, ctx:MiniGoParser.Expr0Context):
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


    # Visit a parse tree produced by MiniGoParser#expr_list.
    def visitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assigning.
    def visitAssigning(self, ctx:MiniGoParser.AssigningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arraydecl.
    def visitArraydecl(self, ctx:MiniGoParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameterlst.
    def visitParameterlst(self, ctx:MiniGoParser.ParameterlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fielddecl.
    def visitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_para_list.
    def visitMethod_para_list(self, ctx:MiniGoParser.Method_para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methoddecl.
    def visitMethoddecl(self, ctx:MiniGoParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_.
    def visitIf_(self, ctx:MiniGoParser.If_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseif_.
    def visitElseif_(self, ctx:MiniGoParser.Elseif_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_.
    def visitElse_(self, ctx:MiniGoParser.Else_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifelse_stat.
    def visitIfelse_stat(self, ctx:MiniGoParser.Ifelse_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forloop_stat.
    def visitForloop_stat(self, ctx:MiniGoParser.Forloop_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stat.
    def visitBreak_stat(self, ctx:MiniGoParser.Break_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stat.
    def visitContinue_stat(self, ctx:MiniGoParser.Continue_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccall_stat.
    def visitFunccall_stat(self, ctx:MiniGoParser.Funccall_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stat.
    def visitReturn_stat(self, ctx:MiniGoParser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockcode.
    def visitBlockcode(self, ctx:MiniGoParser.BlockcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_elem.
    def visitArr_elem(self, ctx:MiniGoParser.Arr_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_elem_list.
    def visitArr_elem_list(self, ctx:MiniGoParser.Arr_elem_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_literal.
    def visitArr_literal(self, ctx:MiniGoParser.Arr_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_para.
    def visitStruct_para(self, ctx:MiniGoParser.Struct_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_para_lst.
    def visitStruct_para_lst(self, ctx:MiniGoParser.Struct_para_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_data_type.
    def visitPrimitive_data_type(self, ctx:MiniGoParser.Primitive_data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_type.
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#end_stm.
    def visitEnd_stm(self, ctx:MiniGoParser.End_stmContext):
        return self.visitChildren(ctx)



del MiniGoParser