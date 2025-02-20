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

program: decl_lst EOF ;

decl_lst: decl decl_lst | decl ;


decl: var_decl
    | array_decl
    | const_decl
    | func_decl 
    | struct_decl 
    | interf_decl 
    ;

//* expression */
expr: expr OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2 ;
expr2: expr2 compare_op expr3 | expr3 ;
expr3: expr3 ADD expr4 | expr3 SUB expr4 | expr4 ;
expr4: expr4 MUL expr5 | expr4 DIV expr5 | expr4 MOD expr5 | expr5 ;
expr5: NOT expr5 | SUB expr5 | expr6 ;
expr6: expr6 tail | expr7 ; 
expr7: LP expr RP | literal | ID ;

tail: field_access_tail | arr_elem_access | funccall_tail ;
field_access_tail: DOT ID ;
arr_elem_access: LSB expr RSB ;
funccall_tail: LP expr_lst RP ;
expr_lst: expr_lstprime | ;
expr_lstprime: expr COMMA expr_lstprime | expr ;

//* assigning value statement */
assigning_stmt: lhs assign expr end_stm ;

//* left hand side */
lhs: expr6 field_access_tail | expr6 arr_elem_access | ID;

//* var declare statement */
var_decl: VAR_ ID data_type end_stm                 #Type_Var_decl
        | VAR_ ID EQUAL expr end_stm                #Value_Var_decl
        | VAR_ ID data_type EQUAL expr end_stm      #TypeValue_Var_decl
        ;

//* const */
const_decl: CONST_ ID data_type? EQUAL expr end_stm ;

//* array */
array_decl: VAR_ ID arridx_lst data_type end_stm 
        |  VAR_ ID arridx_lst data_type EQUAL arr_literal end_stm ;
arridx_lst: arridx arridx_lst | arridx ;
arridx: LSB expr RSB ;

//* function. Note that we have not implemented function body yet */
func_decl: FUNC_ receiver? ID funcparam data_type? blockcode end_stm ;
funcparam: LP paramlst RP ;
paramlst: param_lstprime | ;
param_lstprime: param COMMA param_lstprime | param ;
param: id_nnlst data_type ;
id_nnlst: ID COMMA id_nnlst | ID ;
receiver: LP ID ID RP;


//* struct decl */
struct_decl: TYPE_ ID STRUCT_ structfield end_stm ;
structfield: LCB fielddecl_nnlst RCB ;
fielddecl_nnlst: fielddecl fielddecl_nnlst | fielddecl;
fielddecl: ID data_type end_stm ;

//* struct literal */
struct_literal: ID LCB structparam_lst RCB ;
structparam_lst: structparam_lstprime | ;
structparam_lstprime: structparam COMMA structparam_lstprime | structparam ;
structparam: ID COLON expr ;

//* interface */
interf_decl: TYPE_ ID INTERFACE_ interfmeth end_stm ;
interfmeth: LCB interfmeth_nnlst RCB ;
interfmeth_nnlst: interfmethmem interfmeth_nnlst | interfmethmem ;
interfmethmem: ID funcparam data_type? end_stm ;

//* if statement */
ifelse_stmt: if_ elseif_lst else_ end_stm;
if_: IF_ condition blockcode end_stm? ;
elseif_: ELSE_ IF_ condition blockcode end_stm? ;
elseif_lst: elseif_ elseif_lst | ;
else_: ELSE_ blockcode | ;
condition: LP expr RP ;

//* for statement */
forloop_stmt: FOR_ expr blockcode end_stm
            | FOR_ forloop_init SEMICOLON expr SEMICOLON forloop_update blockcode end_stm
            | FOR_ ID COMMA ID ASSIGN RANGE_ id__arr blockcode end_stm
            ;
forloop_init: ID ASSIGN expr ;
forloop_update: ID uptassign expr ;
id__arr: ID | arr_literal ;

//* break statement */
break_stmt: BREAK_ end_stm;

//* continue statement */
continue_stmt: CONTINUE_ end_stm;

//* call statement */
funccall_stmt: expr6 funccall_tail end_stm ;

//* return statement */
return_stmt: RETURN_ end_stm | RETURN_ expr end_stm;

assign: uptassign | ASSIGN ;
blockcode: LCB blockcodestmt_nnlst RCB ;
blockcodestmt_nnlst: blockcodestmt blockcodestmt_nnlst | blockcodestmt ;
blockcodestmt: assigning_stmt
        | var_decl 
        | array_decl 
        | const_decl 
        | ifelse_stmt 
        | forloop_stmt 
        | continue_stmt 
        | break_stmt 
        | funccall_stmt 
        | return_stmt 
        ;
arr_literal: arridx_lst data_type arrvalue ;
arrvalue: LCB arrelem_lst RCB ;
arrelem_lst: arrelem COMMA arrelem_lst | arrelem ;
arrelem: expr | arrvalue ;
data_type: arridx_lst? primitive_datatype | arridx_lst? ID ;
primitive_datatype: INT_ | FLOAT_ | STRING_ | BOOLEAN_ ;
literal: INTEGER | FLOAT | STRING | TRUE_ | FALSE_ | struct_literal | arr_literal ;
uptassign: ADDASSIGN | SUBASSIGN | MULASSIGN | DIVASSIGN | MODASSIGN ;
compare_op: EQCOM | DIFFCOM | LESSCOM | LEQCOM | GRECOM | GEQCOM ;
end_stm: SEMICOLON | EOF;

//* comment */
SINGLE_LINE_CMT: '//' ~[\n]* -> skip;
MULTI_LINE_CMT: '/*' (MULTI_LINE_CMT | .)*? '*/'  -> skip;

NL: '\r'? '\n' {
if self.lastTokenType in ['ID', 'INTEGER', 'FLOAT', 'TRUE_', 'FALSE_', 'STRING', 'INT_', 'FLOAT_', 'BOOLEAN_', 'STRING_', 'RETURN_', 'CONTINUE_', 'BREAK_', 'RP', 'RSB', 'RCB']:
    self.text = ';'
    self.type = self.SEMICOLON
    self.lastTokenType = 'SEMICOLON'
else:
    self.skip()
};

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs 

/** Keywords */
IF_         : 'if' {self.lastTokenType = 'IF_'};
ELSE_       : 'else' {self.lastTokenType = 'ELSE_'};
FOR_        : 'for' {self.lastTokenType = 'FOR_'};
RETURN_     : 'return' {self.lastTokenType = 'RETURN_'};
FUNC_       : 'func' {self.lastTokenType = 'FUNC_'};
TYPE_       : 'type' {self.lastTokenType = 'TYPE_'};
STRUCT_     : 'struct' {self.lastTokenType = 'STRUCT_'};
INTERFACE_  : 'interface' {self.lastTokenType = 'INTERFACE_'};
STRING_     : 'string' {self.lastTokenType = 'STRING_'};
INT_        : 'int' {self.lastTokenType = 'INT_'};
FLOAT_      : 'float' {self.lastTokenType = 'FLOAT_'};
BOOLEAN_    : 'boolean' {self.lastTokenType = 'BOOLEAN_'};
CONST_      : 'const' {self.lastTokenType = 'CONST_'};
VAR_        : 'var' {self.lastTokenType = 'VAR_'};
CONTINUE_   : 'continue' {self.lastTokenType = 'CONTINUE_'};
BREAK_      : 'break' {self.lastTokenType = 'BREAK_'};
RANGE_      : 'range' {self.lastTokenType = 'RANGE_'};
NIL_        : 'nil' {self.lastTokenType = 'NIL_'};
TRUE_       : 'true' {self.lastTokenType = 'TRUE_'};
FALSE_      : 'false' {self.lastTokenType = 'FALSE_'};

/** Operators */
EQCOM   : '==' {self.lastTokenType = 'EQCOM'};
DIFFCOM : '!=' {self.lastTokenType = 'DIFFCOM'};
LESSCOM : '<' {self.lastTokenType = 'LESSCOM'};
LEQCOM  : '<=' {self.lastTokenType = 'LEQCOM'};
GRECOM  : '>' {self.lastTokenType = 'GRECOM'};
GEQCOM  : '>=' {self.lastTokenType = 'GEQCOM'};
AND     : '&&' {self.lastTokenType = 'AND'};
OR      : '||' {self.lastTokenType = 'OR'};
NOT     : '!' {self.lastTokenType = 'NOT'};
ADDASSIGN   : '+=' {self.lastTokenType = 'ADDASSIGN'};
SUBASSIGN   : '-=' {self.lastTokenType = 'SUBASSIGN'};
MULASSIGN   : '*=' {self.lastTokenType = 'MULASSIGN'};
DIVASSIGN   : '/=' {self.lastTokenType = 'DIVASSIGN'};
MODASSIGN   : '%=' {self.lastTokenType = 'MODASSIGN'};
ASSIGN      : ':=' {self.lastTokenType = 'ASSIGN'};
DOT     : '.' {self.lastTokenType = 'DOT'};
EQUAL   : '=' {self.lastTokenType = 'EQUAL'};
ADD     : '+' {self.lastTokenType = 'ADD'};
SUB     : '-' {self.lastTokenType = 'SUB'};
MUL     : '*' {self.lastTokenType = 'MUL'};
DIV     : '/' {self.lastTokenType = 'DIV'};
MOD     : '%' {self.lastTokenType = 'MOD'};

/** Seperators */
LP  : '(' {self.lastTokenType = 'LP'};
RP  : ')' {self.lastTokenType = 'RP'};
LSB : '[' {self.lastTokenType = 'LSB'};
RSB : ']' {self.lastTokenType = 'RSB'};
LCB : '{' {self.lastTokenType = 'LCB'};
RCB : '}' {self.lastTokenType = 'RCB'};
COMMA       : ',' {self.lastTokenType = 'COMMA'};
SEMICOLON   : ';' {self.lastTokenType = 'SEMICOLON'};
COLON       : ':' {self.lastTokenType = 'COLON'};

/** Literals */
fragment Digit: [0-9] ;
FLOAT: Digit+ '.' (Digit+)? ([eE] [+-]? Digit+)? {self.lastTokenType = 'FLOAT'};

fragment DecInt: '0' | [1-9] [0-9]* ;
fragment BinInt: '0' [bB] [01]+ ;
fragment OctInt: '0' [oO] [0-7]+ ;
fragment HexInt: '0' [xX] [0-9a-fA-F]+ ;
INTEGER: (DecInt | BinInt | OctInt | HexInt) {self.lastTokenType = 'INTEGER'};

fragment Char: ~[\\\n"] ;
fragment EscapeChar: '\\' [\\"rtn] ;
STRING: '"' (Char | EscapeChar)* '"' {self.lastTokenType = 'STRING'};

ID: [_A-Za-z] [_A-Za-z0-9]* {self.lastTokenType = 'ID'};

ERROR_CHAR: . {self.lastTokenType = 'ERROR_CHAR'};
ILLEGAL_ESCAPE: '"' (Char | EscapeChar)* '\\' ~[\\"rtn] {self.lastTokenType = 'ILLEGAL_ESCAPE'};
UNCLOSE_STRING: '"' (Char | EscapeChar)* {self.text = self.text.replace('\r','\n').split('\n')[0]} {self.lastTokenType = 'UNCLOSE_STRING'};