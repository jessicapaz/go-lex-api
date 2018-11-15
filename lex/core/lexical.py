import ply.lex as lex


keywords = {
    'break': 'BREAK',
    'default': 'DEFAULT',
    'func': 'FUNC',
    'interface': 'INTERFACE',
    'select': 'SELECT',
    'case': 'CASE',
    'defer': 'DEFER',
    'go': 'GO',
    'map': 'MAP',
    'struct': 'STRUCT',
    'chan': 'CHAN',
    'else': 'ELSE',
    'goto': 'GOTO',
    'package': 'PACKAGE',
    'switch': 'SWITCH',
    'const': 'CONST',
    'fallthrough': 'FALLTHROUGH',
    'if': 'IF',
    'range': 'RANGE',
    'type': 'TYPE',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'import': 'IMPORT',
    'return': 'RETURN',
    'var': 'VAR'
}

types = {
    'bool': 'TYPE_BOOL',
    'string': 'TYPE_STRING',
    'int': 'TYPE_INT',
    'int8': 'TYPE_INT8',
    'int16': 'TYPE_INT16',
    'int32': 'TYPE_INT32',
    'int64': 'TYPE_INT64',
    'uint': 'TYPE_UINT',
    'uint8': 'TYPE_UINT8',
    'uint16': 'TYPE_UINT16',
    'uint32': 'TYPE_UINT32',
    'uint64': 'TYPE_UINT64',
    'uintptr': 'TYPE_UINTPTR',
    'float32': 'TYPE_FLOAT32',
    'float64': 'TYPE_FLOAT64',
    'complex64': 'TYPE_COMPLEX64',
    'complex128': 'TYPE_COMPLEX128',
}

tokens = ['ID','INTEGER','ARITHMETIC_OPERATOR',
        'OR', 'AND', 'NOT', 'COMPARISON_OPERATOR',
        'ASSIGNMENT_OPERATOR', 'STRING_LITERAL',
        'DELIMITER', 'FLOAT', 'COMMENT', 
        'BITWISE_OPERATOR', 'COLON', 'RPAREN', 
        'LPAREN', 'RBRACKET', 'LBRACKET', 'RBRACE', 
        'LBRACE', 'COMMA', 'SEMICOLON', 'ARITHMETICAL_ASSIGNMENT',
        'ELLIPSIS', 'UNARY_ASSIGNMENT', 'BINARY_ASSIGNMENT',
        'LOGICAL_ASSIGNMENT', 'NORMAL_ASSIGNMENT', 'ASTERISKS',
        'CHANNEL_OPERATOR'] + list(keywords.values()) + list(types.values())

def t_COMMENT(t):
    r'(\/\/.*)|(\/\*.*(\n.*)*\*\/)'
    pass

t_ARITHMETIC_OPERATOR = r'[\+\-\/\%]'
t_ASTERISKS = r'\*'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_NOT = r'\!'
t_CHANNEL_OPERATOR = r'\<\-'
t_BITWISE_OPERATOR = r'(\&(?!\&|\^|\=))|(\|(?!\|))|(\<\<(?!=))|(\>\>(?!=))|(\&\^(?!\=))|(\^)'
t_COMPARISON_OPERATOR = r'(\=\=)|(\!\=)|(\<\=)|(\>\=)|(\<(?!-))|(\>)'
t_ARITHMETICAL_ASSIGNMENT = r'(\+\=)|(\-\=)|(\*\=)|(\/\=)|(\%\=)'
t_BINARY_ASSIGNMENT = r'(\<\<\=)|(\>\>\=)|(\&\^\=)'
t_LOGICAL_ASSIGNMENT = r'(\&\=)|(\|\=)|(\^\=)'
t_NORMAL_ASSIGNMENT = r'(\:\=)|(\=(?!\=))'
t_UNARY_ASSIGNMENT = r'(\+\+)|(\-\-)'
t_STRING_LITERAL = r'\"(\\.|[^\\"\n])*\"|\`(\\.|[^\\"\n])*\`|`\\n|\\n`'
t_DELIMITER = r'(\.)'
t_ELLIPSIS = r'(\.\.\.)'
t_COLON = r'\:(?!=)'
t_RPAREN = r'\)'
t_LPAREN = r'\('
t_RBRACKET	= r'\]'
t_LBRACKET	= r'\['
t_RBRACE = r'\}'
t_LBRACE = r'\{'
t_COMMA	= r'\,'
t_SEMICOLON	= r'\;'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
        t.type = keywords[t.value]
    elif t.value in types:
        t.type = types[t.value]
    return t

def t_FLOAT(t):
    r'[0-9]*[.][0-9]+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    t.type = "Illegal character"
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

lexer = lex.lex()

def get_data(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens