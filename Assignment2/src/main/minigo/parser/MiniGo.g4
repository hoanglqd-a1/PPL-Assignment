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

program: decllst EOF ;

decllst: decl decllst | decl ;
decl: assigning
    | funcdecl 
    | structdecl 
    | interfdecl 
    ;
statement: assigning 
        | vardecl 
        | arraydecl 
        | constdecl 
        | ifelse_stat 
        | forloop_stat 
        | continue_stat 
        | break_stat 
        | funccall_stat 
        | return_stat 
        ;

//* expression */
expr: expr OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2 ;
expr2: expr2 COMPARISON_OP expr3 | expr3 ;
expr3: expr3 ADD expr4 | expr3 SUB expr4 | expr4 ;
expr4: expr4 MUL expr5 | expr4 DIV expr5 | expr4 MOD expr5 | expr5 ;
expr5: NOT expr6 | SUB expr6 | expr6;
expr6: expr6 DOT ID | expr6 LSB expr RSB | expr6 LP exprlst RP | expr7 ;
expr7: LP expr RP | ID | literal ;
exprlst: exprlstprime | ;
exprlstprime: expr COMMA exprlstprime | expr ;

//* left hand side */
lhs: lhs DOT ID | lhs LSB expr RSB | ID ;

//* assigning value statement */
assigning: lhs assign expr end_stm ;

//* var declare statement */
vardecl: VAR_ ID data_type end_stm 
        | VAR_ ID EQUAL expr end_stm 
        | VAR_ ID data_type EQUAL expr end_stm
        ;

//* const */
constdecl: CONST_ ID EQUAL expr end_stm ;

//* array */
arraydecl: VAR_ ID arridxlst data_type end_stm 
        | VAR_ ID arridxlst data_type EQUAL arr_literal end_stm ;
arridxlst: arridx arridxlst | arridx ;
arridx: LSB expr RSB ;

//* function. Note that we have not implemented function body yet */
funcdecl: FUNC_ receiver? ID funcparam data_type? blockcode end_stm ;
funcparam: LP paramlst RP ;
paramlst: paramlstprime | ;
paramlstprime: param COMMA paramlstprime | param ;
param: idlst data_type ;
receiver: LP ID ID RP;
idlst: ID COMMA idlst | ID ;


//* struct */
structdecl: TYPE_ ID STRUCT_ structfield end_stm ;
structfield: LCB fielddecllst RCB ;
fielddecllst: fielddecl fielddecllst | ;
fielddecl: ID data_type arridxlst? end_stm
        | ID ID end_stm
        | ID INTERFACE_ end_stm
        ;

//* interface */
interfdecl: TYPE_ ID INTERFACE_ interfmeth end_stm ;
interfmeth: LCB interfmethlst RCB ;
interfmethlst: interfmethmem interfmethlst | ;
interfmethmem: ID funcparam data_type? end_stm ;

//* if statement */
ifelse_stat: if_ elseif_lst else_ end_stm;
if_: IF_ condition blockcode end_stm? ;
elseif_: ELSE_ IF_ condition blockcode end_stm? ;
elseif_lst: elseif_ elseif_lst | ;
else_: ELSE_ blockcode | ;
condition: LP expr RP ;

//* for statement */
forloop_stat: FOR_ expr blockcode end_stm
            | FOR_ ID ASSIGN expr SEMICOLON expr SEMICOLON ID UPT_ASSIGN expr blockcode end_stm
            | FOR_ ID COMMA ID ASSIGN RANGE_ id__arr blockcode end_stm
            ;
id__arr: ID | arr_literal ;

//* break statement */
break_stat: BREAK_ end_stm;

//* continue statement */
continue_stat: CONTINUE_ end_stm;

//* call statement */
funccall_stat: expr6 LP exprlst RP end_stm ;

//* return statement */
return_stat: RETURN_ end_stm | RETURN_ expr end_stm;

assign: UPT_ASSIGN | ASSIGN ;
blockcode: LCB stmtlst RCB ;
stmtlst: statement stmtlst | ;
arr_literal: arridxlst data_type arrelemlst ;
arrelemlst: LCB arreleml RCB ;
arreleml: arrelem COMMA arreleml | arrelem ;
arrelem: expr | arrelemlst ;
struct_literal: ID LCB structparamlst RCB ;
structparamlst: structparamlstprime | ;
structparamlstprime: structparam COMMA structparamlstprime | structparam ;
structparam: ID COLON literal ;
data_type: primitive_datatype | ID ;
primitive_datatype: INT_ | FLOAT_ | STRING_ | BOOLEAN_ ;
literal: INTEGER | FLOAT | STRING | TRUE_ | FALSE_ | struct_literal | arr_literal ;
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
AND: '&&' {self.lastTypeToken = 'AND'};
OR: '||' {self.lastTypeToken = 'OR'};
NOT: '!' {self.lastTypeToken = 'NOT'};
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
LP: '(' {self.lastTokenType = 'LP'};
RP: ')' {self.lastTokenType = 'RP'};
LSB: '[' {self.lastTokenType = 'LSB'};
RSB: ']' {self.lastTokenType = 'RSB'};
LCB: '{' {self.lastTokenType = 'LCB'};
RCB: '}' {self.lastTokenType = 'RCB'};
COMMA: ',' {self.lastTokenType = 'COMMA'};
SEMICOLON: ';' {self.lastTokenType = 'SEMICOLON'};
COLON: ':' {self.lastTokenType = 'COLON'};

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