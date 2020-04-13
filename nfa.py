from collections import defaultdict

EPSILON = "epsilon"

class NFA():
    def __init__(self):
        self.start = None
        self.accept = None
        ## (state, symbol)->list of states
        self.transitions = defaultdict(list)
        self.states = set([])

    def append(self, nfa_list):
        for nfa in nfa_list:
            self.addSingle(nfa)

        return self
    def addSingle(self, nfa):
        self.transitions.update(nfa.transitions)
        self.states.update(nfa.states)

        return self


    def startState(self, start):


        self.start = start
        self.states.add(start)
        return self

    def acceptState(self, accept):

        self.accept = accept
        self.states.add(accept)

        return self

    ## q1 accepting s , go to q2
    def addTransitions(self, q1, s, q2):
        if isinstance(q1, int):
            q1 = str(q1)
        if isinstance(q2, int):
            q2 = str(q2)

        self.states.add(q1)
        self.states.add(q2)

        self.transitions[(q1, s)].append(q2)

        return self







