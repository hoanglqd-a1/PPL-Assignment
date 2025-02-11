/** MSSV: 2211081 */
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
lastTokenType = None

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

decl: statement | funcdecl | structdecl | interfacedecl ;
statement: assigning | vardecl | arraydecl | constdecl | ifelse_stat | forloop_stat | continue_stat | break_stat | funccall_stat | return_stat ;

//* expression */
expr0: expr1 ('||' expr1)* ;
expr1: expr2 ('&&' expr2)* ;
expr2: expr3 (COMPARISON_OP expr3)* ;
expr3: expr4 ((ADD | SUB) expr4)* ;
expr4: expr5 ((MUL | DIV | MOD) expr5)* ;
expr5: ('-' | '!')? expr6 ;
expr6: expr7 ('.' ID | '[' expr0 ']' | '(' expr_list ')')* ;
expr7: '(' expr0 ')' | ID | literal ;
expr_list: (expr0 (',' expr0)*)? ;

//* left hand side */
lhs: expr6 ;

//* assigning value statement */
assigning: lhs assign expr0 end_stm ;

//* var declare statement */
vardecl: VAR_ ID (data_type | data_type? EQUAL expr0) end_stm ;

//* const */
constdecl: CONST_ ID EQUAL expr0 end_stm ;

//* array */
arraydecl: VAR_ ID ('[' expr0 ']')+ data_type (EQUAL arr_literal)? end_stm ;

//* function. Note that we have not implemented function body yet */
parameter: ID (',' ID)* (data_type | ID) ;
parameterlst: parameter (COMMA parameter)* ;
receiver: ID ID ;
funcdecl: FUNC_ ('('receiver')')? ID '(' parameterlst? ')' data_type? '{' blockcode '}' end_stm ;

//* struct */
fielddecl: ID (data_type ('[' expr0 ']')* | ID | INTERFACE_) end_stm ;
structdecl: TYPE_ ID STRUCT_ '{' end_stm? fielddecl* '}' end_stm ;

//* interface */
methoddecl: ID '(' parameterlst? ')' data_type? end_stm ;
interfacedecl: TYPE_ ID INTERFACE_ '{' end_stm? methoddecl* '}' end_stm ;

//* if statement */
if_: IF_ '(' expr0 ')' '{' blockcode '}' end_stm? ;
elseif_: ELSE_ IF_ '(' expr0 ')' '{' blockcode '}' end_stm? ;
else_: ELSE_ '{' blockcode '}' ;
ifelse_stat: if_ elseif_* else_? end_stm;

//* for statement */
forloop_stat: FOR_  ( expr0
                    | ID ASSIGN expr0 ';' expr0 ';' ID UPT_ASSIGN expr0
                    | ID ',' ID ASSIGN RANGE_ (ID | arr_literal)
                    ) '{' blockcode '}' end_stm ;

//* break statement */
break_stat: BREAK_ end_stm;

//* continue statement */
continue_stat: CONTINUE_ end_stm;

//* call statement */
funccall_stat: expr6 '(' expr_list ')' end_stm ;

//* return statement */
return_stat: RETURN_ expr0? end_stm ;

assign: UPT_ASSIGN | ASSIGN ;
blockcode: end_stm? statement* ;
arr_elem: expr0 | arr_elem_list ;
arr_elem_list: '{' (arr_elem (',' arr_elem)*)? '}' ;
arr_literal: ('[' expr0 ']')+ data_type arr_elem_list ;
struct_para: ID ':' literal ;
struct_para_lst: struct_para (',' struct_para)*;
struct_literal: ID '{' struct_para_lst? '}' ;
primitive_data_type: INT_ | FLOAT_ | STRING_ | BOOLEAN_ ;
data_type: primitive_data_type | ID ;
literal: INTEGER | FLOAT | STRING | TRUE_ | FALSE_ | struct_literal | arr_literal ;
end_stm: SEMICOLON | EOF;

//* comment */
SINGLE_LINE_CMT: '//' ~[\n]* -> skip;
MULTI_LINE_CMT: '/*' (MULTI_LINE_CMT | .)*? '*/'  -> skip;

NL: '\n' {
if self.lastTokenType in ['ID', 'INTEGER', 'FLOAT', 'TRUE_', 'FALSE_', 'STRING', 'INT_', 'FLOAT_', 'BOOLEAN_', 'STRING_', 'RETURN_', 'CONTINUE_', 'BREAK_', 'RPAREN', 'RSB', 'RCB']:
    self.text = ';'
    self.type = self.SEMICOLON
    self.lastTokenType = 'SEMICOLON'
else:
    self.skip()
};

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

/** Keywords */
IF_: 'if' {self.lastTokenType = 'IF_'};
ELSE_: 'else' {self.lastTokenType = 'ELSE_'};
FOR_: 'for' {self.lastTokenType = 'FOR_'};
RETURN_: 'return' {self.lastTokenType = 'RETURN_'};
FUNC_: 'func' {self.lastTokenType = 'FUNC_'};
TYPE_: 'type' {self.lastTokenType = 'TYPE_'};
STRUCT_: 'struct' {self.lastTokenType = 'STRUCT_'};
INTERFACE_: 'interface' {self.lastTokenType = 'INTERFACE_'};
STRING_: 'string' {self.lastTokenType = 'STRING_'};
INT_: 'int' {self.lastTokenType = 'INT_'};
FLOAT_: 'float' {self.lastTokenType = 'FLOAT_'};
BOOLEAN_: 'boolean' {self.lastTokenType = 'BOOLEAN_'};
CONST_: 'const' {self.lastTokenType = 'CONST_'};
VAR_: 'var' {self.lastTokenType = 'VAR_'};
CONTINUE_: 'continue' {self.lastTokenType = 'CONTINUE_'};
BREAK_: 'break' {self.lastTokenType = 'BREAK_'};
RANGE_: 'range' {self.lastTokenType = 'RANGE_'};
NIL_: 'nil' {self.lastTokenType = 'NIL_'};
TRUE_: 'true' {self.lastTokenType = 'TRUE_'};
FALSE_: 'false' {self.lastTokenType = 'FALSE_'};

/** Operators */
COMPARISON_OP: '==' | '!=' | '<' | '<=' | '>' | '>=' {self.lastTypeToken = 'COMPARISON_OP'};
BOOLEAN_OP: '&&' | '||' | '!' {self.lastTokenType = 'BOOLEAN_OP'};
UPT_ASSIGN: '+=' | '-=' | '*=' | '/=' | '%=' {self.lastTokenType = 'UPT_ASSIGN'};
ASSIGN: ':=' {self.lastTokenType = 'ASSIGN'};
DOT: '.' {self.lastTokenType = 'DOT'};
EQUAL: '=' {self.lastTokenType = 'EQUAL'};
ADD: '+' {self.lastTokenType = 'ADD'};
SUB: '-' {self.lastTokenType = 'SUB'};
MUL: '*' {self.lastTokenType = 'MUL'};
DIV: '/' {self.lastTokenType = 'DIV'};
MOD: '%' {self.lastTokenType = 'MOD'};

/** Seperators */
LPAREN: '(' {self.lastTokenType = 'LPAREN'};
RPAREN: ')' {self.lastTokenType = 'RPAREN'};
LSB: '[' {self.lastTokenType = 'LSB'};
RSB: ']' {self.lastTokenType = 'RSB'};
LCB: '{' {self.lastTokenType = 'LCB'};
RCB: '}' {self.lastTokenType = 'RCB'};
COMMA: ',' {self.lastTokenType = 'COMMA'};
SEMICOLON: ';' {self.lastTokenType = 'SEMICOLON'};

/** Literals */
fragment Digit: [0-9] ;
FLOAT: Digit+ '.' (Digit+)? ([eE] [+-]? Digit+)? {self.lastTokenType = 'FLOAT'};

fragment DecInt: '0' | [1-9] [0-9]* ;
fragment BinInt: '0' [bB] [01]+ ;
fragment OctInt: '0' [oO] [0-7]+ ;
fragment HexInt: '0' [xX] [0-9a-fA-F]+ ;
INTEGER: (DecInt | BinInt | OctInt | HexInt) {self.lastTokenType = 'INTEGER'};

fragment Char: ~[\\"] ;
fragment EscapeChar: '\\' [\\"rtn] ;
STRING: '"' (Char | EscapeChar)* '"' {self.lastTokenType = 'STRING'};

ID: [_A-Za-z] [_A-Za-z0-9]* {self.lastTokenType = 'ID'};

ERROR_CHAR: . {self.lastTokenType = 'ERROR_CHAR'};
ILLEGAL_ESCAPE: '"' (Char | EscapeChar)* '\\' ~[\\"rtn] {self.text = self.text[1:]} {self.lastTokenType = 'ILLEGAL_ESCAPE'};
UNCLOSE_STRING: '"' (Char | EscapeChar)* {self.text = self.text.replace('\r','\n').split('\n')[0][1:]} {self.lastTokenType = 'UNCLOSE_STRING'};