
from PIL import Image, ImageDraw
from  math import  cos, sin

"""
1. calculate position(width, depth)for each state 
2. draw position
3. draw transition(according position)
"""
RADIUS= 20



def drawPositions( draw, nfa_layout):
    for q in nfa_layout.positions:

        x, y = nfa_layout.positions[q]
        __draw_cycle(draw, x, y, nfa_layout.radius)

    accept_x, accept_y = nfa_layout.acceptPosition()

    __draw_double_cycle(draw, accept_x, accept_y, nfa_layout.radius)


def drawTransitions( draw, nfa_layout):
    for q1_x, q1_y, q2_x, q2_y, s ,type in nfa_layout.get_transition_position():
        if type == "line":
            __draw_arrow_and_text(draw, q1_x, q1_y, q2_x, q2_y, s)
        else:
            __drawArc(draw, q1_x, q1_y, q2_x, q2_y)


def __drawArc( draw, x1, y1, x2, y2):
    draw.arc((x1, y1, x2, y2), start=180, end=0, fill='black', width=1)

    __arrow(draw, x1, y1 + RADIUS * 2, 0, -10)

def __draw_arrow_and_text( draw, x1, y1, x2, y2, symbol):

    draw_arrow(draw, x1, y1, x2, y2)

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2)/ 2 + 10
    __draw_symbol(draw,mid_x, mid_y, symbol)

def __nomalization( dx, dy):
    absolute = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    if dx == 0:
        return (0, dy/(abs(dy)) * 10)

    if dy == 0:
        return (dx/abs(dx) * 10, 0)

    return (dx / (absolute + 0.0) * 10, dy / (absolute + 0.0) * 10)

def __arrow( draw, end_x, end_y, dx, dy):
    cos = 0.866
    sin = 0.500
    dx, dy =  __nomalization(dx, dy)

    ### draw arrow
    upper_arrow_x, upperarrow_y = end_x + dx * cos - dy * sin, end_y + dx * sin + dy * cos

    lower_arrow_x, lower_arrow_y = end_x + dx * cos + dy * sin, end_y + dx * (-sin) + dy * cos

    draw.line((upper_arrow_x, upperarrow_y, end_x, end_y), fill=(0, 0, 0), width=1)
    draw.line((lower_arrow_x, lower_arrow_y, end_x, end_y), fill=(0, 0, 0), width=1)


def draw_arrow( draw, x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=1)

    dx = x1 - x2
    dy = y1 - y2
    __arrow(draw, x2, y2, dx, dy)



def drawNewNFA( nfa_layout, file = None):
    width, depth = nfa_layout.pic_width, nfa_layout.pic_depth

    im = Image.new('RGB', (width, depth), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    drawPositions(draw, nfa_layout)

    drawTransitions(draw, nfa_layout)

    if file == None:
        file ='./new_nfa_draw.jpg'

    im.save(file ,  format='JPEG', subsampling=0, quality=95)

def __draw_symbol( draw, x, y, str_text):
    draw.text((x, y), str_text, fill="black")

def __draw_double_cycle( draw, x, y, r):
    __draw_cycle(draw, x, y, r)
    __draw_cycle(draw, x, y, r - 10)


def __draw_cycle( draw, x, y, r):
    leftUpPoint = (x - r, y - r)
    rightDownPoint = (x + r, y + r)
    twoPointList = [leftUpPoint, rightDownPoint]
    draw.ellipse(twoPointList, fill=(255, 255, 255), outline=(0,0,0), width=1)

    return draw
