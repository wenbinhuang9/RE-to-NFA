
from PIL import Image, ImageDraw

from nfa import NFA

"""
1. calculate position(width, depth)for each state 
2. draw position
3. draw transition(according position)

todo 
1. add test for star ??? 
2. todo when to draw the arc ??? 
"""

## generate NFA layout here, that is calculate position for each NFA automatically

class NFALayout():
    def __init__(self, nfa):
        self.radius = 20
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
        self.pic_width, self.pic_depth = self.calPosition( self.width, self.depth)

        self.pic_width += self.radius * 2
        self.pic_depth += self.radius * 2


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
                type = self.get_transition_draw_type(q1, q2)
                if type == "line":
                    ans.append([q1_x + self.radius, q1_y, q2_x - self.radius, q2_y, s, type])
                else:
                    ans.append([q2_x, q2_y - 2*self.radius, q1_x, q1_y - 2*self.radius + self.curved_height, s, type])
        return ans

    def get_transition_draw_type(self,q1, q2):
        if q1 < q2:
            return "line"
        return "arc"


class NFADrawer():
    def __init__(self):
        #by default now
        self.r = 30

    def drawPositions(self, draw, nfa_layout):
        for q in nfa_layout.positions:

            x, y = nfa_layout.positions[q]
            self.__draw_cycle(draw, x, y, nfa_layout.radius)

        accept_x, accept_y = nfa_layout.acceptPosition()

        self.__draw_double_cycle(draw, accept_x, accept_y, nfa_layout.radius)


    def drawTransitions(self, draw, nfa_layout):
        for q1_x, q1_y, q2_x, q2_y, s , type in nfa_layout.get_transition_position():
            if type == "line":
                self.__draw_new_right_arrow(draw, q1_x, q1_y, q2_x, q2_y, s)
            else:
                self.__drawArc(draw,  q1_x, q1_y, q2_x, q2_y)

    def __drawArc(self, draw, x1, y1, x2, y2):
        draw.arc((x1, y1, x2, y2), start=180, end=0, fill='black', width=1)

    def __draw_new_right_arrow(self, draw, x1, y1, x2, y2, symbol):
        draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=1)

        mid_x = (x1 + x2) / 2
        self.__draw_symbol(draw,mid_x, y1 + 10, symbol)

        ### draw arrow
        end_x, end_y = x2, y2
        upper_arrow_x, upperarrow_y = end_x - 10, y2 + 10
        lower_arrow_x, lower_arrow_y = end_x - 10, y2 - 10

        draw.line((upper_arrow_x, upperarrow_y, end_x, end_y), fill=(0, 0, 0), width=1)
        draw.line((lower_arrow_x, lower_arrow_y, end_x, end_y), fill=(0, 0, 0), width=1)

    def drawNewNFA(self, nfa_layout):
        width, depth = nfa_layout.pic_width, nfa_layout.pic_depth

        im = Image.new('RGB', (width, depth), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        self.drawPositions(draw, nfa_layout)

        self.drawTransitions(draw, nfa_layout)

        im.save('./new_nfa_draw.jpg', quality=95)


    def drawNFA(self, nfa_obj):
        im = Image.new('RGB', (500, 300), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        x0, y0 = 50, 150

        self.__draw_recursive(nfa_obj, nfa_obj.start, draw, x0, y0)
        im.save('./pillow_imagedraw.jpg', quality=95)

    def __draw_recursive(self, nfa_obj, cur_state, draw, x, y):
        if cur_state == nfa_obj.accept:
            self.__draw_double_cycle(draw, x, y, self.r)

        else:
            symbol = nfa_obj.curSymbol(cur_state)
            self.__draw_cycle_and_right_arrow(draw, x, y, self.r, symbol)
            next = nfa_obj.nextState(cur_state)
            self.__draw_recursive(nfa_obj, next, draw, x + 3*self.r, y)

    def __draw_symbol(self, draw, x, y, str_text):
        draw.text((x, y), str_text, fill="black")

    def __draw_double_cycle(self, draw, x, y, r):
        self.__draw_cycle(draw, x, y, r)
        self.__draw_cycle(draw, x, y, r - 10)

    def __draw_cycle_and_right_arrow(self, draw, x, y , r, symbol):
        self.__draw_cycle(draw, x, y, r)

        self.__draw_right_arrow(draw, x + r, y, r, symbol)

    def __draw_cycle(self, draw, x, y, r):
        leftUpPoint = (x - r, y - r)
        rightDownPoint = (x + r, y + r)
        twoPointList = [leftUpPoint, rightDownPoint]
        draw.ellipse(twoPointList, fill=(255, 255, 255), outline=(0,0,0), width=1)

        return draw

    def __draw_right_arrow(self, draw, x0, y, line_len, symbol):
        draw.line((x0, y, x0 + line_len, y), fill=(0, 0, 0), width=1)

        mid_x = (line_len/2 + x0)
        self.__draw_symbol(draw,mid_x, y + 10, symbol)

        ### draw arrow
        end_x, end_y = x0 + line_len, y
        upper_arrow_x, upperarrow_y = end_x - 10, y + 10
        lower_arrow_x, lower_arrow_y = end_x - 10, y - 10

        draw.line((upper_arrow_x, upperarrow_y, end_x, end_y), fill=(0, 0, 0), width=1)
        draw.line((lower_arrow_x, lower_arrow_y, end_x, end_y), fill=(0, 0, 0), width=1)