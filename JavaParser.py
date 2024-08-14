import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'IF', 'SWITCH', 'FOR', 'WHILE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON', 'COLON', 'COMMA',
    'IDENTIFIER', 'NUMBER', 'GREATER', 'LESS', 'PLUS', 'MINUS', 'STAR', 'SLASH',
    'EQUALS', 'NOT', 'CASE', 'DEFAULT', 'BREAK',
    'INT', 'CHAR', 'FLOAT', 'DOUBLE', 'LSQPAREN', 'RSQPAREN', 'SINGLEQT', 'NEW'
)

# Regular expressions for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_GREATER = r'>'
t_LESS = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_EQUALS = r'='
t_NOT = r'!'
t_LSQPAREN = r'\['
t_RSQPAREN = r'\]'
t_SINGLEQT = r"'"

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'

# Ignore whitespace and tabs
t_ignore = ' \t\n'

# Token specifications for keywords
def t_IF(t):
    r'if'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_INT(t):
    r'int'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_NEW(t):
    r'new'
    return t

# Error handling for unrecognized characters
def t_error(t):
    print("Illegal character: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Grammar rules

# If statement
def p_if_statement(p):
    '''
    if_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE
    '''
    p[0] = 'Valid Java if statement'

# Switch statement
def p_switch_statement(p):
    '''
    switch_statement : SWITCH LPAREN IDENTIFIER RPAREN LBRACE cases RBRACE
    '''
    p[0] = 'Valid Java switch statement'

def p_cases(p):
    '''
    cases : CASE NUMBER COLON statements BREAK SEMICOLON
          | DEFAULT COLON statements BREAK SEMICOLON
          | cases cases
    '''
    pass

# For statement
def p_for_statement(p):
    '''
    for_statement : FOR LPAREN expression SEMICOLON condition SEMICOLON expression RPAREN LBRACE statements RBRACE
    '''
    p[0] = 'Valid Java for statement'

# While statement
def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN condition RPAREN LBRACE statements RBRACE
    '''
    p[0] = 'Valid Java while statement'

# Array declaration statement
def p_arr_statement(p):
    '''
    arr_statement : key LSQPAREN RSQPAREN IDENTIFIER EQUALS LBRACE data RBRACE SEMICOLON
                  | key LSQPAREN RSQPAREN IDENTIFIER SEMICOLON
                  | key IDENTIFIER LSQPAREN RSQPAREN SEMICOLON
                  | key IDENTIFIER LSQPAREN RSQPAREN EQUALS LBRACE data RBRACE SEMICOLON
                  | INT LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW INT LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | CHAR LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW CHAR LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | FLOAT LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW FLOAT LSQPAREN NUMBER RSQPAREN SEMICOLON
                  | DOUBLE LSQPAREN RSQPAREN IDENTIFIER EQUALS NEW DOUBLE LSQPAREN NUMBER RSQPAREN SEMICOLON
    '''
    p[0] = 'Valid Java array declaration'

def p_key(p):
    '''
    key : INT
        | CHAR
        | FLOAT
        | DOUBLE
    '''
    pass

def p_data(p):
    '''
    data : NUMBER
         | NUMBER COMMA
         | SINGLEQT IDENTIFIER SINGLEQT
         | SINGLEQT IDENTIFIER SINGLEQT COMMA
         | data data
    '''
    pass

# Common grammar rules
def p_condition(p):
    '''
    condition : expression GREATER expression
              | expression LESS expression
              | expression GREATER EQUALS expression
              | expression LESS EQUALS expression
              | expression EQUALS EQUALS expression
              | expression NOT EQUALS expression
              | NUMBER
              | IDENTIFIER
    '''
    pass

def p_expression(p):
    '''
    expression : IDENTIFIER
               | expression PLUS expression
               | NUMBER
               | expression MINUS expression
               | expression STAR expression
               | expression SLASH expression
               | expression EQUALS expression
    '''
    pass

def p_statements(p):
    '''
    statements : SEMICOLON
               | statements statements
               | if_statement
               | switch_statement
               | for_statement
               | while_statement
               | arr_statement
               | expression SEMICOLON
    '''
    pass

# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Run the parser in a loop
while True:
    try:
        s = input('construct > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
