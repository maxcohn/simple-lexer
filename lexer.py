# lexer.py

"""Inspired by ply and sly"""

import re

class Lex():

    """Creates a lexical analyzer based on the input token definitions

    Note: Order of the tokens in the dictionary matter. I thought that hashing
    would break that, but it doesn't seem to have... yet.
    """

    def __init__(self, tokens: dict, skip: dict):
        """Constructor for lexical analyzer

        The lexer requires input in the form of a dictionary in the following format:

        {
            'token_name': r'regex'
        }

        Args:
            tokens (str, str): Dictionary of token-regex pairs
            skip (str, str): Dictionary of token-regex pairs that are to be skipped
        """

        # create the master regular expression based on the given tokens
        self.master_skip = self.__create_regex(skip)
        self.master_regex = self.__create_regex(tokens)


    def __create_regex(self, tokens: dict):
        """Builds the master regex that we're going to use to capture tokens
        
        Args:
            tokens (str, str): Dictionary of token-regex pairs
        """

        # store each token's individual regex
        regex_parts = []

        for tok_name in tokens.keys():
            regex = tokens[tok_name]

            # try to compile the regular expression to make sure it is valid
            try:
                re.compile(regex)
            except re.error:
                print(f'The regular expression for "{tok_name}" is not valid ({regex}).')
                return None #TODO change this to be less awful

            # create a named group for the token
            regex_parts.append(f'(?P<{tok_name}>{regex})')
        
        # compile the master regex which consists of all parts with alternations between

        # I had seen this technique and doubted it's efficiency, but I realized that all it
        # does is creates a few more transitions in the nfa
        return re.compile('|'.join(regex_parts))
        
    
    def all_tokens(self, source: str):
        """Returns all tokens that were found in the given string

        Args:
            source: The text where we're looking for tokens

        Returns:
            list[tuple]: List of tuples representing tokens (token, lexeme)

        """

        tokens = [] # list of all found tokens
        pos = 0 # current position in source

        # loop through all text
        while pos < len(source):
            # check if the next token is one we need to skip
            is_skip = self.master_skip.match(source, pos)
            if is_skip is not None:
                pos = is_skip.end()
                continue
            
            # check if the next token is an actual token
            is_tok = self.master_regex.match(source, pos)
            if is_tok is not None:
                pos = is_tok.end()
                tok_type = ''

                # check to see which named group in the dict has the match
                for k in is_tok.groupdict().keys():
                    if is_tok.groupdict()[k] is not None:
                        tok_type = k
                        tokens.append( (tok_type, is_tok.group(0)) )
                        break

                continue
            
            # No token found, report error and increase position
            print(f'No token found at position {pos}')
            pos += 1
            
        return tokens