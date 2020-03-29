## definiton of nfa
from collections import defaultdict

EPSILON = "epsilon"

class NFAManager():

    def __init__(self):
        pass

    def mergeOR(self, nfa_list):
        redefine_nfa_list = [nfa_obj.redefine_states(str(i)) for i, nfa_obj in enumerate(nfa_list)]

        nfa_obj = NFA().acceptState(0).accept(1).append(redefine_nfa_list)

        for subnfa in redefine_nfa_list:
            nfa_obj.addTransitions(nfa_obj.start, EPSILON, subnfa.start)
            nfa_obj.addTransitions(nfa_obj.accept, EPSILON, subnfa.accept)

        return nfa_obj

    def mergeSTAR(self):
        pass

    def mergeConcatenation(self):
        pass



# how to generate code according to NFA definition??? there should be some algorithms
class NFA():
    def __init__(self):
        self.start = None
        self.accept = None
        ## (state, symbol)->list of states
        self.transitions = defaultdict(list)
        self.states = set([])

        ## state->list of symbols reaching out
        self.state_out = defaultdict(list)


    def append(self, nfa_list):
        for nfa in nfa_list:
            self.__append_single(nfa)

        return self

    def __append_single(self, nfa):
        self.transitions.update(nfa.transitions)
        self.state_out.update(nfa.state_out)
        self.states.update(nfa.states)

        return self


    def gen_new_state(self, c , state):
        return c + state

    def redefine_states(self, c):
        nfa_obj = NFA().startState(self.gen_new_state(c, self.startState())).acceptState(self.gen_new_state(c, self.accept))

        for key,state_list in self.transitions.items():
            state, symbol = key[0], key[1]
            new_state = self.gen_new_state(c, state)
            for s in state_list:
                new_s = self.gen_new_state(c, s)
                nfa_obj.addTransitions(new_state, symbol, new_s)

        return nfa_obj

    def startState(self, start):
        if isinstance(start, int):
            start = str(start)

        self.start = start
        self.states.add(start)
        return self

    def acceptState(self, accept):
        if isinstance(accept, int):
            accept = str(accept)
        self.accept = accept
        self.states.add(accept)

        return self

    ## q1 accepting s , go to q2
    def addTransitions(self, q1, s, q2):
        self.states.add(q1)
        self.states.add(q2)

        self.state_out[q1].append(s)

        self.transitions[(q1, s)].append(q2)

        return self


    def curSymbol(self, q):
        symbol_list =self.state_out[q]

        return symbol_list[0]

    def nextState(self, q):
        symbol_list = self.state_out[q]
        next = self.transitions[(q, symbol_list[0])]

        return next[0]








