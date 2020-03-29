
from PIL import Image, ImageDraw

from nfa import  NFA
## todo make  sequence NFA perfect
## todo how to automatically deploy the picture
## todo how to merge NFA
class NFADrawer():
    def __init__(self):
        #by default now
        self.r = 30

    def drawNFA(self, nfa_obj):
        im = Image.new('RGB', (500, 300), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        x0, y0 = 150, 150

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