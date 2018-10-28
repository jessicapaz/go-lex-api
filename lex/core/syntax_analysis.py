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
    print(result)