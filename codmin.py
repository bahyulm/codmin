import vcl_lexer
import vcl_parser
import vcl_interp

from sys import *

#DENGAN MASUKAN EKSTENSI .COD
lexer = codmin_lexer.BasicLexer()
parser = codmin_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    codmin_interp.BasicExecute(tree, env)