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

decl: expr0 | statement | funcdecl | structdecl | interfacedecl ;
statement: assigning | vardecl | arraydecl | constdecl | ifelse_stat | forloop_stat | continue_stat | break_stat | funccall_stat | return_stat ;

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
assigning: lhs ASSIGN1 expr0 end_stm ;

//* var declare statement */
vardecl: VAR_ ID (data_type | data_type? ASSIGN expr0) end_stm ;

//* const */
constdecl: CONST_ ID ASSIGN expr0 end_stm ;

arraydecl: VAR_ ID ('[' expr0 ']')+ data_type ASSIGN arr_literal end_stm ;

//* function. Note that we have not implemented function body yet */
parameter: ID (data_type | ID) ;
parameterlst: parameter (COMMA parameter)* ;
receiver: ID ID ;
funcdecl: FUNC_ ('('receiver')')? ID '(' parameterlst? ')' data_type? '{' blockcode '}' end_stm ;

//* struct */
fielddecl: ID (data_type ('[' expr0 ']')* | ID | INTERFACE_) end_stm ;
structdecl: TYPE_ ID STRUCT_ '{' end_stm? fielddecl* '}' end_stm ;

//* interface */
method_para_list: ID data_type? (',' ID data_type?)* ;
methoddecl: ID '(' method_para_list? ')' data_type? end_stm ;
interfacedecl: TYPE_ ID INTERFACE_ '{' end_stm? methoddecl* '}' end_stm ;

//* if statement */
if_: IF_ '(' expr0 ')' '{' blockcode '}' end_stm? ;
elseif_: ELSE_ IF_ '(' expr0 ')' '{' blockcode '}' end_stm? ;
else_: ELSE_ '{' blockcode '}' ;
ifelse_stat: if_ elseif_* else_? end_stm;

//* for statement */
forloop_stat: FOR_  ( expr0
                    | assigning expr0 ';' lhs assigning expr0
                    | ID ',' ID ASSIGN1 RANGE_ ID
                    ) '{' blockcode '}' end_stm ;

//* break statement */
break_stat: BREAK_ end_stm;

//* continue statement */
continue_stat: CONTINUE_ end_stm;

//* call statement */
funccall_stat: expr6 '(' expr_list ')' end_stm ;

//* return statement */
return_stat: RETURN_ end_stm ;

blockcode: end_stm? statement* ;
arr_elem: expr0 | arr_elem_list ;
arr_elem_list: '{' (arr_elem (',' arr_elem)*)? '}' ;
arr_literal: ('[' expr0 ']')+ data_type arr_elem_list ;
struct_literal: ID '{' parameterlst? '}' ;
data_type: INT_ | FLOAT_ | STRING_ | BOOLEAN_ ;
literal: INTEGER | FLOAT | STRING | TRUE_ | FALSE_ | struct_literal ;
end_stm: (SEMICOLON | NL)+ | EOF;

//* comment */
SINGLE_LINE_CMT: '//' ~[\n]* ('\n' | EOF) -> skip;
MULTI_LINE_CMT: '/*' (MULTI_LINE_CMT | .)*? '*/'  -> skip;

NL: '\n' ;

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

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