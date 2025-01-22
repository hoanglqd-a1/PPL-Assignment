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

program  : decl+ EOF ;

decl: funcdecl | vardecl  ;

vardecl: 'var' ID 'int' ';' ;

arraydecl: 'var' ID ('[' INTEGER ']')+ (INT_ | FLOAT_ | STRING_ | BOOLEAN_);

funcdecl: 'func' ID '(' ')' '{' '}' ';' ;

NL: '\n' -> skip; //skip newlines

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

COMMENT: '\\\\' | '\\*' | '*\\' ;

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
OP1: '+' | '-' | '*' | '/' | '%' ;
OP2: '==' | '!=' | '<' | '<=' | '>' | '>=' ;
OP3: '&&' | '||' | '!' ;
OP4: '=' | '+=' | '-=' | '*=' | '/=' | '%=' ;
OP5: '.' ;

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