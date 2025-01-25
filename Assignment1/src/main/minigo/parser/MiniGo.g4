/** MSSV: 2211081 */
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: decl+ EOF ;

decl: expr0 | comment | assigning | vardecl | constdecl | funcdecl | structdecl | interfacedecl ;

data_type: INT_ | FLOAT_ | STRING_ | BOOLEAN_ ;
literal: INTEGER | FLOAT | STRING | TRUE_ | FALSE_ ;

//* comment */
comment: SINGLE_LINE_CMT | MULTI_LINE_CMT ;

//* expression */
expr0: expr1 ('||' expr1)* ;
expr1: expr2 ('&&' expr2)* ;
expr2: expr3 (COMPARISON_OP expr3)* ;
expr3: expr4 ((ADD || SUB) expr4)* ;
expr4: expr5 ((MUL | DIV | MOD) expr5)* ;
expr5: ('-' | '!')? expr6 ;
expr6: expr7 ('.' ID | '[' expr0 ']' | '(' expr_list ')')* ;
expr7: '(' expr0 ')' | ID | literal ;
expr_list: (expr0 (',' expr0)*)? ;

//* left hand side */
lhs: expr6 ;

//* assigning value statement */
assigning: lhs ASSIGN1 literal end_stm ;

//* var declare statement. Note that we have not implemented constant expression yet */
vardecl: VAR_ ID (data_type | data_type? ASSIGN literal) end_stm ;

//* const. Note that we have not implemented constant expression yet */
constdecl: CONST_ ID ASSIGN literal end_stm ;

arraydecl: VAR_ ID ('[' INTEGER ']')+ data_type end_stm ;

//* function. Note that we have not implemented function body yet */
parameter: ID data_type ;
parameterlst: parameter COMMA parameterlst | parameter ;
receiver: ID ID ;
funcdecl: FUNC_ ('('receiver')')? ID '(' parameterlst? ')' data_type? '{' '}' end_stm ;

fielddecl: ID data_type end_stm ;
structdecl: TYPE_ ID STRUCT_ '{' end_stm? fielddecl* '}' end_stm ;

method_para_list: ID data_type? (',' ID data_type?)* ;
methoddecl: ID '(' method_para_list? ')' data_type? end_stm ;
interfacedecl: TYPE_ ID INTERFACE_ '{' end_stm? methoddecl* '}' end_stm ;

end_stm: (SEMICOLON | NL)+ ;
NL: '\n' ;

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

SINGLE_LINE_CMT: '//' ~[\n]* '\n' ;
MULTI_LINE_CMT: '/*' (. | MULTI_LINE_CMT)*? '*/' ;

/** Keywords */
IF_: 'if' ;
ELSE_: 'else' ;
FOR_: 'for' ;
RETURN_: 'return' ;
FUNC_: 'func' ;
TYPE_: 'type' ;
STRUCT_: 'struct' ;
INTERFACE_: 'interface' ;
STRING_: 'string' ;
INT_: 'int' ;
FLOAT_: 'float' ;
BOOLEAN_: 'boolean' ;
CONST_: 'const' ;
VAR_: 'var' ;
CONTINUE_: 'continue' ;
BREAK_: 'break' ;
RANGE_: 'range' ;
NIL_: 'nil' ;
TRUE_: 'true' ;
FALSE_: 'false' ;

/** Operators */
COMPARISON_OP: '==' | '!=' | '<' | '<=' | '>' | '>=' ;
OP3: '&&' | '||' | '!' ;
ASSIGN1: ':=' | '+=' | '-=' | '*=' | '/=' | '%=' ;
OP5: '.' ;
ASSIGN: '=' ;
ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;
MOD: '%' ;

/** Seperators */
LPAREN: '(' ;
RPAREN: ')' ;
LSB: '[' ;
RSB: ']' ;
LCB: '{' ;
RCB: '}' ;
COMMA: ',' ;
SEMICOLON: ';' ;

/** Literals */
fragment Digit: [0-9] ;
FLOAT: Digit+ '.' (Digit+)? ([eE] [+-]? Digit+)? ;

fragment DecInt: '0' | [1-9] [0-9]* ;
fragment BinInt: '0' [bB] [01]+ ;
fragment OctInt: '0' [oO] [0-7]+ ;
fragment HexInt: '0' [xX] [0-9a-fA-F]+ ;
INTEGER: DecInt | BinInt | OctInt | HexInt ;

fragment Char: ~[\\"] ;
fragment EscapeChar: '\\' [\\"rtn] ;
STRING: '"' (Char | EscapeChar)* '"' ;

ID: [_A-Za-z] [_A-Za-z0-9]* ;

ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' (Char | EscapeChar)* '\\' ~[\\"rtn] {self.text = self.text[1:]};
UNCLOSE_STRING: '"' (Char | EscapeChar)* {self.text = self.text.split("\\n")[0][1:]};