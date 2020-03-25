## definiton of nfa

EPSILON = "epsilon"

from collections import defaultdict
# how to generate code according to NFA definition??? there should be some algorithms
class NFA():
    def __init__(self):
        self.start = None
        self.accept = None
        self.transitions = defaultdict(list)
        self.states = None

        ## record each state's outing symbol
        self.state_out = defaultdict(list)

    def initStates(self, len):
        states_list = [i for i in range(len)]

        self.states = set(states_list)
        return self

    def startState(self, start):
        self.start = start
        return self

    def acceptState(self, accept):
        self.accept = accept

        return self

    ## q1 accepting s , go to q2
    def addTransitions(self, q1, s, q2):
        self.state_out[q1].append(s)

        self.transitions[(q1, s)].append(q2)

        return self

    ##todo support nfa
    def nextState(self, q):
        symbol_list = self.state_out[q]
        next = self.transitions[(q, symbol_list[0])]

        return next[0]








