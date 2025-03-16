# Generated from c:/coding/PPL/Assignment1/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl.
    def enterDecl(self, ctx:MiniGoParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl.
    def exitDecl(self, ctx:MiniGoParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#data_type.
    def enterData_type(self, ctx:MiniGoParser.Data_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#data_type.
    def exitData_type(self, ctx:MiniGoParser.Data_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal.
    def enterLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal.
    def exitLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#comment.
    def enterComment(self, ctx:MiniGoParser.CommentContext):
        pass

    # Exit a parse tree produced by MiniGoParser#comment.
    def exitComment(self, ctx:MiniGoParser.CommentContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr0.
    def enterExpr0(self, ctx:MiniGoParser.Expr0Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr0.
    def exitExpr0(self, ctx:MiniGoParser.Expr0Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr1.
    def enterExpr1(self, ctx:MiniGoParser.Expr1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr1.
    def exitExpr1(self, ctx:MiniGoParser.Expr1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr2.
    def enterExpr2(self, ctx:MiniGoParser.Expr2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr2.
    def exitExpr2(self, ctx:MiniGoParser.Expr2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr3.
    def enterExpr3(self, ctx:MiniGoParser.Expr3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr3.
    def exitExpr3(self, ctx:MiniGoParser.Expr3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr4.
    def enterExpr4(self, ctx:MiniGoParser.Expr4Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr4.
    def exitExpr4(self, ctx:MiniGoParser.Expr4Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr5.
    def enterExpr5(self, ctx:MiniGoParser.Expr5Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr5.
    def exitExpr5(self, ctx:MiniGoParser.Expr5Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr6.
    def enterExpr6(self, ctx:MiniGoParser.Expr6Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr6.
    def exitExpr6(self, ctx:MiniGoParser.Expr6Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr7.
    def enterExpr7(self, ctx:MiniGoParser.Expr7Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expr7.
    def exitExpr7(self, ctx:MiniGoParser.Expr7Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expr_list.
    def enterExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expr_list.
    def exitExpr_list(self, ctx:MiniGoParser.Expr_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#lhs.
    def enterLhs(self, ctx:MiniGoParser.LhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#lhs.
    def exitLhs(self, ctx:MiniGoParser.LhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assigning.
    def enterAssigning(self, ctx:MiniGoParser.AssigningContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assigning.
    def exitAssigning(self, ctx:MiniGoParser.AssigningContext):
        pass


    # Enter a parse tree produced by MiniGoParser#vardecl.
    def enterVardecl(self, ctx:MiniGoParser.VardeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#vardecl.
    def exitVardecl(self, ctx:MiniGoParser.VardeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#constdecl.
    def enterConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#constdecl.
    def exitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arraydecl.
    def enterArraydecl(self, ctx:MiniGoParser.ArraydeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arraydecl.
    def exitArraydecl(self, ctx:MiniGoParser.ArraydeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#parameter.
    def enterParameter(self, ctx:MiniGoParser.ParameterContext):
        pass

    # Exit a parse tree produced by MiniGoParser#parameter.
    def exitParameter(self, ctx:MiniGoParser.ParameterContext):
        pass


    # Enter a parse tree produced by MiniGoParser#parameterlst.
    def enterParameterlst(self, ctx:MiniGoParser.ParameterlstContext):
        pass

    # Exit a parse tree produced by MiniGoParser#parameterlst.
    def exitParameterlst(self, ctx:MiniGoParser.ParameterlstContext):
        pass


    # Enter a parse tree produced by MiniGoParser#receiver.
    def enterReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass

    # Exit a parse tree produced by MiniGoParser#receiver.
    def exitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcdecl.
    def enterFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcdecl.
    def exitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#fielddecl.
    def enterFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#fielddecl.
    def exitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structdecl.
    def enterStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structdecl.
    def exitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_para_list.
    def enterMethod_para_list(self, ctx:MiniGoParser.Method_para_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_para_list.
    def exitMethod_para_list(self, ctx:MiniGoParser.Method_para_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#methoddecl.
    def enterMethoddecl(self, ctx:MiniGoParser.MethoddeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#methoddecl.
    def exitMethoddecl(self, ctx:MiniGoParser.MethoddeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interfacedecl.
    def enterInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interfacedecl.
    def exitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#end_stm.
    def enterEnd_stm(self, ctx:MiniGoParser.End_stmContext):
        pass

    # Exit a parse tree produced by MiniGoParser#end_stm.
    def exitEnd_stm(self, ctx:MiniGoParser.End_stmContext):
        pass



del MiniGoParser