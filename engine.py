
from drawer import NFALayout, NFADrawer
from  parser import  ParserEngine
## todo give a input convert it,and then draw NFA
def convertREtoNFA(input):
    parserEngine = ParserEngine()

    tree = parserEngine.run(input)

    nfa = tree.get_nfa()

    nfa_layout = NFALayout(nfa)

    drawer = NFADrawer()

    drawer.drawNewNFA(nfa_layout)
