import codmin_lexer
import codmin_parser
import codmin_interp

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = codmin_lexer.BasicLexer()
    parser = codmin_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('COD > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            codmin_interp.BasicExecute(tree, env)