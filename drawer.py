
from PIL import Image, ImageDraw
from  math import  cos, sin

"""
1. calculate position(width, depth)for each state 
2. draw position
3. draw transition(according position)
"""
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



class NFADrawer():
    def __init__(self):
        pass

    def drawPositions(self, draw, nfa_layout):
        for q in nfa_layout.positions:

            x, y = nfa_layout.positions[q]
            self.__draw_cycle(draw, x, y, nfa_layout.radius)

        accept_x, accept_y = nfa_layout.acceptPosition()

        self.__draw_double_cycle(draw, accept_x, accept_y, nfa_layout.radius)


    def drawTransitions(self, draw, nfa_layout):
        for q1_x, q1_y, q2_x, q2_y, s ,type in nfa_layout.get_transition_position():
            if type == "line":
                self.__draw_arrow_and_text(draw, q1_x, q1_y, q2_x, q2_y, s)
            else:
                self.__drawArc(draw, q1_x, q1_y, q2_x, q2_y)


    def __drawArc(self, draw, x1, y1, x2, y2):
        draw.arc((x1, y1, x2, y2), start=180, end=0, fill='black', width=1)

        self.__arrow(draw, x1, y1 + RADIUS * 2, 0, -10)
    def __draw_arrow_and_text(self, draw, x1, y1, x2, y2, symbol):

        self.draw_arrow(draw, x1, y1, x2, y2)

        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2)/ 2 + 10
        self.__draw_symbol(draw,mid_x, mid_y, symbol)

    def __nomalization(self, dx, dy):
        absolute = abs(dx) if abs(dx) > abs(dy) else abs(dy)

        if dx == 0:
            return (0, dy/(abs(dy)) * 10)

        if dy == 0:
            return (dx/abs(dx) * 10, 0)

        return (dx / (absolute + 0.0) * 10, dy / (absolute + 0.0) * 10)

    def __arrow(self, draw, end_x, end_y, dx, dy):
        cos = 0.866
        sin = 0.500
        dx, dy =  self.__nomalization(dx, dy)

        ### draw arrow
        upper_arrow_x, upperarrow_y = end_x + dx * cos - dy * sin, end_y + dx * sin + dy * cos

        lower_arrow_x, lower_arrow_y = end_x + dx * cos + dy * sin, end_y + dx * (-sin) + dy * cos

        draw.line((upper_arrow_x, upperarrow_y, end_x, end_y), fill=(0, 0, 0), width=1)
        draw.line((lower_arrow_x, lower_arrow_y, end_x, end_y), fill=(0, 0, 0), width=1)


    def draw_arrow(self, draw, x1, y1, x2, y2):
        draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=1)

        dx = x1 - x2
        dy = y1 - y2
        self.__arrow(draw, x2, y2, dx, dy)



    def drawNewNFA(self, nfa_layout, file = None):
        width, depth = nfa_layout.pic_width, nfa_layout.pic_depth

        im = Image.new('RGB', (width, depth), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        self.drawPositions(draw, nfa_layout)

        self.drawTransitions(draw, nfa_layout)

        if file == None:
            file ='./new_nfa_draw.jpg'

        im.save(file ,  format='JPEG', subsampling=0, quality=95)

    def __draw_symbol(self, draw, x, y, str_text):
        draw.text((x, y), str_text, fill="black")

    def __draw_double_cycle(self, draw, x, y, r):
        self.__draw_cycle(draw, x, y, r)
        self.__draw_cycle(draw, x, y, r - 10)


    def __draw_cycle(self, draw, x, y, r):
        leftUpPoint = (x - r, y - r)
        rightDownPoint = (x + r, y + r)
        twoPointList = [leftUpPoint, rightDownPoint]
        draw.ellipse(twoPointList, fill=(255, 255, 255), outline=(0,0,0), width=1)

        return draw
