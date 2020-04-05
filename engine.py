
from drawer import  drawNewNFA
from  parser import  ParserEngine
from layout import  NFALayout

def drawNFA(input, file = None):
    parserEngine = ParserEngine()

    tree = parserEngine.run(input)

    nfa = tree.get_nfa()

    nfa_layout = NFALayout(nfa)

    drawNewNFA(nfa_layout, file )
