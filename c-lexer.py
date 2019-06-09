# c-lexer.py
"""Demonstration of the lexer by creating a lexer for the C language

This is just a bit of a proof that the lexer works, and I figured it
would be fun.

This is probably missing some, but i'm tired.
"""

import lexer

toks = {
    'lparen': r'\(',
    'rparen': r'\)',
    'lbrack': r'\[',
    'rbrack': r'\]',
    'lcurl': r'\{',
    'rcurl': r'\}',
    'int': r'int',
    'char': r'char',
    'float': r'float',
    'double': r'double',
    'struct': r'struct',
    'semi': r';',
    'amp': r'&',
    'arrow': r'-\>',
    'dot': r'\.',
    'eq': r'=',
    'ne': r'!=',
    'lt': r'\<',
    'le': r'\<=',
    'gt': r'\>',
    'ge': r'\>=',
    'star': r'\*',
    'string': r'"[^"]*"',
    'return': 'return',
    'num': r'-?\d+',
    'id': r'[_a-zA-Z][_a-zA-Z0-9]*'
}

skip = {
    'whitespace': r'\s+'
}

clex = lexer.Lex(toks, skip)

a = clex.all_tokens('''

int main(int argc, char** argv){

    printf("hello world");
    return 0;
}

''')

print(a)