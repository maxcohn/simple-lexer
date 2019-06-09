#test.py

tok = {
    'for': r'for',
    'symbol': r'[_a-zA-Z]\w+',
    'lparen': r'\('
    
}

skip = {
    'whitespace': r'\s+'
}

import lexer

l = lexer.Lex(tok, skip)

l.all_tokens("(for god")