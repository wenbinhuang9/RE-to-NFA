from  lexer import  LexicalAnalyzer
from graphviz_draw import  drawGraphNFA
from parser import RegExParser
from  idgen import  IDGenerator

def drawNFA(reInput, file = None):
    lex = LexicalAnalyzer()

    lex.run(reInput)

    parser = RegExParser(lex)

    tree = parser.regex()

    idgenerator = IDGenerator()
    nfa = tree.get_nfa(idgenerator)

    drawGraphNFA(nfa, file)