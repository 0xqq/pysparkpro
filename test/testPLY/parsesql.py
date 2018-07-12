#!/usr/bin/python
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'TABLE',
    'COLUMN',
    'STAR',
    'COMMA',
    'END',
)

t_SELECT = r'select|SELECT'
t_FROM = r'from|FROM'
t_WHERE = r'where|WHERE'
t_TABLE = r'b'
t_COLUMN = r'a'
t_STAR = r'\*'
t_COMMA = r','
t_END = r';'

t_ignore = ' \t'


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)


lex.lex()

NONE, SELECT, INSERT, DELETE, UPDATE = range(5)
states = ['NONE', 'SELECT', 'INSERT', 'DELETE', 'UPDATE']
current_state = NONE


def p_statement_expr(t):
    'statement : expression'
    print(states[current_state], t[1])


def p_expr_select(t):
    'expression : SELECT columns FROM TABLE END'
    global current_state
    current_state = SELECT
    print(t[3])


def p_recursive_columns(t):
    '''recursive_columns : recursive_columns COMMA COLUMN'''
    t[0] = ', '.join([t[1], t[3]])


def p_recursive_columns_base(t):
    '''recursive_columns : COLUMN'''
    t[0] = t[1]


def p_columns(t):
    '''columns : STAR
               | recursive_columns'''
    t[0] = t[1]


def p_error(t):
    print('Syntax error at "%s"' % t.value if t else 'NULL')
    global current_state
    current_state = NONE


parser = yacc.yacc()

while True:
    try:
        inpu = input('sql> ')
    except:
        break
    result = parser.parse(inpu)
    print(result)
