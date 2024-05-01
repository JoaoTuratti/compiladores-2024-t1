import ply.lex as lex

tokens = ('ID', 'LIT_INT', 'LIT_REAL', 'LIT_STRING', 'DIR_PROGRAM', 'DIR_VAR', 'DIR_PROC', 'DIR_FUNC', 'DIR_BEGIN', 'DIR_END', 
    'DIR_TYPE', 'DIR_CONST', 'DIR_WITH', 'STMT_IF', 'STMT_THEN', 'STMT_ELSE', 'STMT_WHILE', 'STMT_REPEAT', 'STMT_FOR', 'STMT_DO', 
    'STMT_UNTIL', 'STMT_TO', 'STMT_DOWNTO', 'STMT_CASE', 'TYPE_ARRAY', 'TYPE_SET', 'TYPE_RECORD', 'TYPE_FILE', 'TYPE_INT', 'TYPE_REAL', 
    'TYPE_CHAR', 'TYPE_BOOL', 'TYPE_STRING', 'FN_READ', 'FN_READLN', 'FN_WRITE', 'FN_WRITELN', 'OP_NIL', 'OP_ATRIB', 'OP_SUM', 'OP_MUL', 
    'OP_REL', 'OP_LOGIC', 'OP_RANGE', 'OP_OPAR', 'OP_CPAR', 'OP_OBRA', 'OP_CBRA', 'OP_COMMA', 'OP_EOC', 'OP_PERIOD', 'OP_COLON', 
    'COMMENT'
)

# expressões regulares 
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIV = r'/'
t_OPAR = r'\('
t_CPAR = r'\)'
t_OBRA = r'\['
t_CBRA = r'\]'
t_COMMA = r','
t_EOC = r';'
t_PERIOD = r'\.'
t_COLON = r':'
t_ID = r'[a-zA-Z][a-zA-Z]'

# characters ignorados
t_ignore = ' \t\r'

def t_LIT_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LIT_float(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_LIT_STRING(t):
    r'(\"[^\"]*\"|\'' + r'[^]*' + r'\')'
    t.value = t.value[1:-1]
    return t

# ratreador de linhas
def t_newline(t):
    r'\n+'
    t.lexer.line += len(t.value)

# mensagem de erro
def t_error(t):
    print("character invalido '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Palavras Reservadas
reserved = {
    # Diretivas
    'program': 'DIR_PROGRAM',
    'var': 'DIR_VAR',
    'procedure': 'DIR_PROC',
    'function': 'DIR_FUNC',
    'begin': 'DIR_BEGIN',
    'end': 'DIR_END',
    'type': 'DIR_TYPE',
    'of': 'DIR_OF',
    'const': 'DIR_CONST',
    'with': 'DIR_WITH',
    # Comandos
    'if': 'STMT_IF',
    'then': 'STMT_THEN',
    'else': 'STMT_ELSE',
    'while': 'STMT_WHILE',
    'repeat': 'STMT_REPEAT',
    'for': 'STMT_FOR',
    'do': 'STMT_DO',
    'until': 'STMT_UNTIL',
    'to': 'STMT_TO',
    'downto': 'STMT_DOWNTO',
    'case': 'STMT_CASE',
    # Tipos de dados
    'array': 'TYPE_ARRAY',
    'set': 'TYPE_SET',
    'record': 'TYPE_RECORD',
    'file': 'TYPE_FILE',
    'integer': 'TYPE_INT',
    'real': 'TYPE_REAL',
    'character': 'TYPE_CHAR',
    'boolean': 'TYPE_BOOL',
    'string': 'TYPE_STRING',
    # Funções built-in
    'read': 'FN_READ',
    'readln': 'FN_READLN',
    'write': 'FN_WRITE',
    'writeln': 'FN_WRITELN',
    'nil': 'OP_NIL',
    # Operadores
    'div': 'OP_MUL',
    'mod': 'OP_MUL',
    'and': 'OP_LOGIC',
    'or': 'OP_LOGIC',
    'not': 'OP_LOGIC', 
    # Outros Operadores
    '{': 'COMMENT',
    '}': 'COMMENT',
    '(*': 'COMMENT',
    '*)': 'COMMENT',
    '//': 'COMMENT',
    '(': 'OP_OPAR',
    ')': 'OP_CPAR',
    '[': 'OP_OBRA',
    ']': 'OP_CBRA',
    ',': 'OP_COMMA',
    ';': 'OP_EOC',
    '.': 'OP_PERIOD',
    ':': 'OP_COLON',
}

lexer = lex.lex()
