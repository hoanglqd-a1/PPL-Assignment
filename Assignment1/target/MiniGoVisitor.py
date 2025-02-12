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


    # Visit a parse tree produced by MiniGoParser#decl_stmtlst.
    def visitDecl_stmtlst(self, ctx:MiniGoParser.Decl_stmtlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_stmt.
    def visitDecl_stmt(self, ctx:MiniGoParser.Decl_stmtContext):
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


    # Visit a parse tree produced by MiniGoParser#exprlst.
    def visitExprlst(self, ctx:MiniGoParser.ExprlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprlstprime.
    def visitExprlstprime(self, ctx:MiniGoParser.ExprlstprimeContext):
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


    # Visit a parse tree produced by MiniGoParser#arridxlst.
    def visitArridxlst(self, ctx:MiniGoParser.ArridxlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arridx.
    def visitArridx(self, ctx:MiniGoParser.ArridxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcparam.
    def visitFuncparam(self, ctx:MiniGoParser.FuncparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlst.
    def visitParamlst(self, ctx:MiniGoParser.ParamlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlstprime.
    def visitParamlstprime(self, ctx:MiniGoParser.ParamlstprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#idlst.
    def visitIdlst(self, ctx:MiniGoParser.IdlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structfield.
    def visitStructfield(self, ctx:MiniGoParser.StructfieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fielddecllst.
    def visitFielddecllst(self, ctx:MiniGoParser.FielddecllstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fielddecl.
    def visitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfdecl.
    def visitInterfdecl(self, ctx:MiniGoParser.InterfdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfmeth.
    def visitInterfmeth(self, ctx:MiniGoParser.InterfmethContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfmethlst.
    def visitInterfmethlst(self, ctx:MiniGoParser.InterfmethlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfmethmem.
    def visitInterfmethmem(self, ctx:MiniGoParser.InterfmethmemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifelsestmt.
    def visitIfelsestmt(self, ctx:MiniGoParser.IfelsestmtContext):
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


    # Visit a parse tree produced by MiniGoParser#forloopstmt.
    def visitForloopstmt(self, ctx:MiniGoParser.ForloopstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#id__arr.
    def visitId__arr(self, ctx:MiniGoParser.Id__arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccallstmt.
    def visitFunccallstmt(self, ctx:MiniGoParser.FunccallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockcode.
    def visitBlockcode(self, ctx:MiniGoParser.BlockcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockcodestmtlst.
    def visitBlockcodestmtlst(self, ctx:MiniGoParser.BlockcodestmtlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockcodestmt.
    def visitBlockcodestmt(self, ctx:MiniGoParser.BlockcodestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_literal.
    def visitArr_literal(self, ctx:MiniGoParser.Arr_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrelemlst.
    def visitArrelemlst(self, ctx:MiniGoParser.ArrelemlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arreleml.
    def visitArreleml(self, ctx:MiniGoParser.ArrelemlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrelem.
    def visitArrelem(self, ctx:MiniGoParser.ArrelemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structparamlst.
    def visitStructparamlst(self, ctx:MiniGoParser.StructparamlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structparamlstprime.
    def visitStructparamlstprime(self, ctx:MiniGoParser.StructparamlstprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structparam.
    def visitStructparam(self, ctx:MiniGoParser.StructparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_type.
    def visitData_type(self, ctx:MiniGoParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitive_datatype.
    def visitPrimitive_datatype(self, ctx:MiniGoParser.Primitive_datatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#uptassign.
    def visitUptassign(self, ctx:MiniGoParser.UptassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compare_op.
    def visitCompare_op(self, ctx:MiniGoParser.Compare_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#end_stm.
    def visitEnd_stm(self, ctx:MiniGoParser.End_stmContext):
        return self.visitChildren(ctx)



del MiniGoParser