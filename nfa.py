## definiton of nfa
from collections import defaultdict

EPSILON = "epsilon"

def mergeOR(nfa_list):
    redefine_nfa_list = [nfa_obj.redefine_states(str(i)) for i, nfa_obj in enumerate(nfa_list)]

    nfa_obj = NFA().startState(0).acceptState(1).append(redefine_nfa_list)

    for subnfa in redefine_nfa_list:
        nfa_obj.addTransitions(nfa_obj.start, EPSILON, subnfa.start)
        nfa_obj.addTransitions(subnfa.accept, EPSILON, nfa_obj.accept)

    return nfa_obj

def mergeConcatenation(nfa_list):
    redefine_nfa_list = [nfa_obj.redefine_states(str(i)) for i, nfa_obj in enumerate(nfa_list)]

    new_nfa = redefine_nfa_list[0].append(redefine_nfa_list[1:])
    pre_nfa = new_nfa
    for i in range(1, len(redefine_nfa_list)):
        each_nfa = redefine_nfa_list[i]
        new_nfa.addTransitions(pre_nfa.accept, EPSILON, each_nfa.start)

        pre_nfa = each_nfa
        if i == len(redefine_nfa_list) - 1:
            new_nfa.accept = each_nfa.accept

    return new_nfa

def mergeStar(nfa):
    nfa.addTransitions(nfa.accept, EPSILON, nfa.start)

    return nfa


# how to generate code according to NFA definition??? there should be some algorithms
class NFA():
    def __init__(self):
        self.start = None
        self.accept = None
        ## (state, symbol)->list of states
        self.transitions = defaultdict(list)
        self.states = set([])

        ## state->list of symbols reaching out
        self.state_out = defaultdict(set)


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
        nfa_obj = NFA().startState(self.gen_new_state(c, self.start)).acceptState(self.gen_new_state(c, self.accept))

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
        if isinstance(q1, int):
            q1 = str(q1)
        if isinstance(q2, int):
            q2 = str(q2)

        self.states.add(q1)
        self.states.add(q2)

        self.state_out[q1].add(s)

        self.transitions[(q1, s)].append(q2)

        return self


    def curSymbol(self, q):
        symbol_list =self.state_out[q]

        return symbol_list[0]

    def nextState(self, q):
        symbol_list = self.state_out[q]
        next = self.transitions[(q, symbol_list[0])]

        return next[0]

    def nextStates(self, q):
        symbol_list = self.state_out[q]
        ans = []
        for symbol in symbol_list:
            ans.extend(self.transitions[(q, symbol)])
        return ans







