
from  parser import  ParserEngine

from  lexer import  LexicalAnalyzer
from graphviz_draw import  drawGraphNFA
from new_parser import RegExParser
from  idgen import  IDGenerator
def drawNFA(input, file = None):
    parserEngine = ParserEngine()

    tree = parserEngine.run(input)

    nfa = tree.get_nfa()

    drawGraphNFA(nfa, file)


def drawNewNFA(reInput, file = None):
    lex = LexicalAnalyzer()

    lex.run(reInput)

    parser = RegExParser(lex)

    tree = parser.regex()

    print(tree)
    idgenerator = IDGenerator()
    nfa = tree.get_nfa(idgenerator)

    drawGraphNFA(nfa, file)