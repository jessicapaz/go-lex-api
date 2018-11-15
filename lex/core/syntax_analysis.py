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

    '''
def p_decl_exp(p):
    '''expression : declaration
    '''

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



# def p_block(p):
#     '''block : LBRACE statement_list RBRACE
#     '''

# def p_statement_list(p):
#     '''statement_list : statement
#                       | statement statement_list
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
