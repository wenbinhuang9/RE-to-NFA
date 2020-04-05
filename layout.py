RADIUS = 20
## generate NFA layout here, that is calculate position for each NFA automatically
class NFALayout():
    def __init__(self, nfa):
        self.radius = RADIUS
        self.space_between_levels = 60
        self.space_adjacent_cycles = 40

        self.x0 = 50
        self.y0 = 50

        self.curved_height = 50

        self.nfa = nfa
        self.width = None
        self.depth = None

        self.positions = {}

        self.pic_width = None
        self.pic_depth = None

        max_depth_width = [0, 0]
        visit = set([])
        visit.add(nfa.start)
        self.calLayout(nfa.start, 0, 0, max_depth_width, visit)

        self.width, self.depth = max_depth_width[0], max_depth_width[1]
        self.width += 1
        self.depth += 1
        self.pic_width, self.pic_depth = self.calPosition( self.width, self.depth)

        self.pic_width += self.radius * 2
        self.pic_depth += self.radius * 2

        self.calAcceptStateLayout()

    def calLayout(self, q, width, depth, max_depth_width, visit):
        max_width, max_depth = max_depth_width[0], max_depth_width[1]
        max_depth_width[0] = max(max_width, width)
        max_depth_width[1] = max(max_depth, depth)

        self.positions[q] = self.calPosition(width, depth)

        next_states = self.nfa.nextStates(q)

        for i, s in enumerate(next_states):
            if s not in visit:
                visit.add(s)

                self.calLayout(s, width + 1, depth + i, max_depth_width, visit)


    def calAcceptStateLayout(self):
        accept = self.nfa.accept
        self.positions[accept] = self.calPosition(self.width, self.depth/2)

    def startPosition(self):
        return self.positions[self.nfa.start]

    def acceptPosition(self):
        return self.positions[self.nfa.accept]

    def calPosition(self, width, depth):
        x = self.x0 + width * (self.radius + self.space_adjacent_cycles + self.radius)
        y = self.y0 + depth * (self.radius + self.space_between_levels + self.radius)

        return (x, y)

    def get_transition_position(self):
        ans = []
        for key, value in self.nfa.transitions.items():
            q1, s = key[0], key[1]
            for q2 in value:
                q1_x, q1_y = self.positions[q1]
                q2_x, q2_y = self.positions[q2]
                if q1_x < q2_x:
                    ans.append([q1_x + self.radius, q1_y, q2_x - self.radius, q2_y, s, "line"])
                else:
                    ## draw arc here for star transition
                    ans.append([q2_x + self.radius, q2_y - 2 * self.radius, q1_x - self.radius, q1_y + 2 * self.radius, s, "arc"])
        return ans
