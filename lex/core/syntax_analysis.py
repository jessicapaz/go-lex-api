import ply.yacc as yacc
from lexical import tokens

""" TEM QUE QUEBRAR OS TOKENS, AMORZINHO (NO CASO, JÉSSICA)! """
def p_assignment_expression(p):
    '''assignment_expression : ID ASSIGNMENT_OPERATOR expression 
    '''


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
                  | ID
                  | LPAREN expression RPAREN
    '''
    # if p[1] == '(' and p[3] == ')':
    #     p[0] = p[2]
    # else:
    #     p[0] = p[1]


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