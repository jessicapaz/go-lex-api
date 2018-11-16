import core.ply.yacc as yacc
from core.lexical import tokens


    
def p_expression(p):
    '''expression : INTEGER
                  | FLOAT
                  | STRING_LITERAL
                  | ID
                  | LPAREN expression RPAREN
    '''
    if p[1] == '(' and p[3] == ')':
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_binary_operators(p):
    '''expression : expression ARITHMETIC_OPERATOR expression
    '''
    # if p[2] == '+':
        # p[0] = p[1] + p[3]
    # elif p[2] == '-':
        # p[0] = p[1] - p[3]
    # elif p[2] == '/':
        # p[0] = p[1] / p[3]
    # elif p[2] == '*':
        # p[0] = p[1] * p[3]
    # elif p[2] == '%':
        # p[0] = p[1] % p[3]

def p_expression_list(p):
    '''expression_list : expression 
                       | expression expression_list
    '''

def p_logical_operators(p):
    '''expression : expression OR expression
                  | expression AND expression
    '''
    # if p[2] == '&&':
    #     p[0] = p[1] and p[3]
    # elif p[2] == '||':
    #     p[0] = p[1] or p[3]
        
def p_negation_operator(p):
    '''expression : NOT expression
    '''
    # p[0] = not p[2]




def p_comparison_operators(p):
    '''expression : expression COMPARISON_OPERATOR expression
    '''
    # if p[2] == '>':
    #     p[0] = p[1] > p[3]
    # elif p[2] == '<':
    #     p[0] = p[1] < p[3]
    # elif p[2] == '>=':
    #     p[0] = p[1] >= p[3]
    # elif p[2] == '<=':
    #     p[0] = p[1] <= p[3]
    # elif p[2] == '==':
    #     p[0] = p[1] == p[3]
    # elif p[2] == '!=':
    #     p[0] = p[1] != p[3]
    
def p_arithmetical_assignments(p):
    '''arithmetical_assignment : ID ARITHMETICAL_ASSIGNMENT expression 
    '''
def p_unary_assignment(p):
    '''unary_assignment : ID UNARY_ASSIGNMENT
    '''

def p_assign_exp(p):
    '''expression : arithmetical_assignment
                  | unary_assignment
    '''

def p_type(p):
    '''type : ID 
            | type_lit
            | LPAREN type RPAREN
    '''

def p_type_exp(p):
    '''expression : type'''

def p_type(p):
    '''type : TYPE_BOOL
            | TYPE_STRING
            | TYPE_INT
            | TYPE_INT8
            | TYPE_INT16
            | TYPE_INT32
            | TYPE_INT64
            | TYPE_UINT
            | TYPE_UINT8
            | TYPE_UINT16
            | TYPE_UINT32
            | TYPE_UINT64
            | TYPE_UINTPTR
            | TYPE_FLOAT32
            | TYPE_FLOAT64
            | TYPE_COMPLEX64
            | TYPE_COMPLEX128
    '''

def p_type_lit(p):
    '''type_lit : array_type
                | slice_type
                | struct_type
                | pointer_type
                | function_type
                | interface_type
                | map_type
                | channel_type
    '''

def p_exp_type_lit(p):
    '''type : type_lit
    '''

def p_array_type(p):
    '''array_type : LBRACKET expression RBRACKET type
    '''

def p_slice_type(p):
    '''slice_type : LBRACKET RBRACKET type
    '''

def p_struct_type(p):
    '''struct_type : STRUCT LBRACE RBRACE
                  | STRUCT LBRACE field_decl RBRACE
    ''' 

def p_field_decl(p):
    '''field_decl : identifier_list type string_lit
                  | identifier_list type 
                  | embedded_field string_lit
                  | embedded_field
    '''

def p_identifier_list(p):
    '''identifier_list : ID
                       | ID COMMA identifier_list
    '''

def p_embedded_field(p):
    '''embedded_field : ASTERISKS ID
    '''

def p_string_lit(p):
    '''string_lit : STRING_LITERAL
    '''

def p_pointer_type(p):
    '''pointer_type : ASTERISKS type
    '''

def p_function_type(p):
    '''function_type : FUNC signature
    '''

def p_signature(p):
    '''signature : parameters
                 | parameters result
    '''

def p_result(p):
    '''result : parameters
              | type
              | LPAREN type RPAREN
    '''

def p_parameters(p):
    '''parameters : LPAREN RPAREN
                  | LPAREN parameter_list RPAREN
    '''

def p_parameter_list(p):
    '''parameter_list : parameter_decl
                      | parameter_decl COMMA parameter_list
    '''

def p_parameter_decl(p):
    '''parameter_decl : identifier_list
                      | identifier_list type
                      | ELLIPSIS type
                      | identifier_list ELLIPSIS type
    '''

def p_interface_type(p):
    '''interface_type : INTERFACE LBRACE method_spec RBRACE
    '''

def p_method_spec(p):
    '''method_spec : method_name signature 
                    | interface_type_name
    '''

def p_method_name(p):
    '''method_name : ID
    '''

def p_interface_type_name(p):
    '''interface_type_name : ID
    '''

def p_map_type(p):
    '''map_type : MAP LBRACKET key_type RBRACKET type
    '''

def p_key_type(p):
    '''key_type : type
    '''

def p_channel_type(p):
    '''channel_type : CHAN type
                    | CHAN CHANNEL_OPERATOR type
                    | CHANNEL_OPERATOR CHAN type
    '''

def p_declaration(p):
    '''declaration : const_decl
                   | type_decl
                   | var_decl
                   | func_decl
                   | import_decl

    '''

def p_decl_exp(p):
    '''expression : declaration
    '''



# def p_import_spec(p):
#     '''import_spec : string_lit
#     '''

def p_const_decl(p):
    '''const_decl : CONST const_spec
                  | CONST LPAREN const_spec RPAREN
    '''
def p_const_spec(p):
    '''const_spec : identifier_list NORMAL_ASSIGNMENT expression_list
                  | identifier_list type NORMAL_ASSIGNMENT expression_list
    '''

def p_type_decl(p):
    '''type_decl : TYPE type_spec
                 | TYPE LPAREN type_spec RPAREN
    '''

def p_type_spec(p):
    '''type_spec : alias_decl 
                 | type_def
    '''

def p_alias_decl(p):
    '''alias_decl : ID NORMAL_ASSIGNMENT type
    '''

def p_type_def(p):
    '''type_def : ID type
    '''

def p_var_decl(p):
    '''var_decl : VAR var_spec
                | VAR LPAREN var_spec RPAREN
    '''

def p_var_spec(p):
    '''var_spec : identifier_list type 
                | identifier_list type NORMAL_ASSIGNMENT expression_list
                | identifier_list NORMAL_ASSIGNMENT expression_list 
    '''

def p_func_decl(p):
    '''func_decl : FUNC ID signature
                 | FUNC ID signature block
    '''

def p_import_decl(p):
    '''import_decl : IMPORT string_lit
                   | IMPORT LPAREN string_lit RPAREN
    '''

def p_statement(p):
    '''statement : if_statement
                 | for_statement
                 | assignment_statement
                 | return_statement
    '''

def p_sta_exp(p):
    '''expression : statement
    '''

def p_block(p):
    '''block : LBRACE expression_list RBRACE
    '''

def p_if_statement(p):
    '''if_statement : IF expression block
                    | IF expression block ELSE block
    '''


def p_for_statement(p):
    '''for_statement : FOR expression block
                     | FOR for_clause block
                     | FOR range_clause block
    '''

def p_for_clause(p):
    '''for_clause : assignment_statement SEMICOLON expression SEMICOLON expression
    '''

def p_assignment_statement(p):
    '''assignment_statement : expression_list NORMAL_ASSIGNMENT expression_list
    '''

def p_range_clause(p):
    '''range_clause : expression_list NORMAL_ASSIGNMENT RANGE expression
                    | identifier_list NORMAL_ASSIGNMENT RANGE expression
    '''

def p_return_statement(p):
    '''return_statement : RETURN expression_list
    '''

def p_program(p):
    '''program : expression_list
    '''

def p_error(p):
    print(f"{p.type} : {p.lineno}|{p.lexpos};")

parser = yacc.yacc(start="program")

# while True:
#     tok = parser.token()
#     if not tok:
#         break
#     print(tok)

# print(dir(parser))

s = '''
import "fmt"

if 2 < 2 {
    if x 2 < 2 {
        3 + 3212
    }
    func teste (i int){
        return x = i + 2
    }
    for i=2; 2<2; i++{
        2 + 2 @#
    }
}
'''

import sys
import io



def get_errors(code):
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    r = parser.parse(code)


    sys.stdout = old_stdout

    whatWasPrinted = buffer.getvalue()
    return whatWasPrinted.rstrip().split('\n')
