import ply.yacc as yacc
from lexical import tokens



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
    '''
                
                # | pointer_type
                # | function_type
                # | interface_type
                # | map_type
                # | channel_type

def p_exp_type_lit(p):
    '''expression : type_lit
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
    '''embedded_field : '*' ID
    '''

def p_string_lit(p):
    '''string_lit : STRING_LITERAL
    '''



# def p_declaration(p):
#     '''declaration : const_decl
#                     | type_decl
#                     | var_decl
#     '''

# def p_const_decl(p):
#     '''const_decl : CONST const_spec
#                   | CONST LPAREN const_spec RPAREN
#     '''

# def p_const_spec(p):
#     '''const_spec : identifier_list ASSIGNMENT_OPERATOR expression_list
#                   | identifier_list type ASSIGNMENT_OPERATOR expression_list
#     '''

# def p_const_exp(p):
#     '''expression : const_decl
#     '''

# def p_type_decl(p):
#     '''type_decl : TYPE type_spec 
#                  | TYPE LPAREN type_spec RPAREN
#     '''

# def p_type_spec(p):
#     '''type_spec : alias_decl 
#                 | type_decl
#     '''

# def p_alias_decl(p):
#     '''alias_decl : ID ASSIGMENT_OPERATOR 
#     '''

# def p_block(p):
#     '''block : statement
#     '''

# def p_statement(p):
#     '''statement : if_statement'''

# def p_if_statement(p):
#     '''if_statement : IF expression LBRACE expression RBRACE
#     '''
def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
