
from PIL import Image, ImageDraw

from nfa import  NFA



class NFADrawer():
    def __init__(self):
        #by default now
        self.r = 30

    def drawImage(self, nfa_obj):
        im = Image.new('RGB', (500, 300), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        x0, y0 = 150, 150

        self.__draw_recursive(nfa_obj, nfa_obj.start, draw, x0, y0)
        im.save('./pillow_imagedraw.jpg', quality=95)

    def __draw_recursive(self, nfa_obj, cur_state, draw, x, y):
        if cur_state == nfa_obj.accept:
            self.__draw_cycle(draw, x, y, self.r)

        else:
            self.__draw_cyle_and_right_arrow(draw, x, y, self.r)
            next = nfa_obj.nextState(cur_state)

            self.__draw_recursive(nfa_obj, next, draw, x + 3*self.r, y)


    def __draw_cyle_and_right_arrow(self, draw, x, y , r):
        self.__draw_cycle(draw, x, y, r)

        self.__draw_right_arrow(draw, x + r, y, r)

    def __draw_cycle(self, draw, x, y, r):
        leftUpPoint = (x - r, y - r)
        rightDownPoint = (x + r, y + r)
        twoPointList = [leftUpPoint, rightDownPoint]
        draw.ellipse(twoPointList, fill=(255, 255, 255), outline=(0,0,0))

        return draw

    def __draw_right_arrow(self, draw, x0, y, line_len):
        draw.line((x0, y, x0 + line_len, y), fill=(0, 0, 0), width=1)
    def __draw_start_state(self):
        pass

    def __draw_final_state(self):
        pass