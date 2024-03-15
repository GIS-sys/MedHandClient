from abc import ABC

from utils import add, button_name


class Action(ABC):
    pass


# TODO

class ActionMove(Action):
    def __init__(self, pos):
        self.x, self.y = pos

    def __repr__(self):
        return f"ActionMoveDelta(x={self.x}, y={self.y})"

class ActionClick(Action):
    def __init__(self, pos, right=False):
        self.x, self.y = pos
        self.right = right

    def __repr__(self):
        return f"ActionClick(x={self.x}, y={self.y}, button={button_name(self.right)})"


#class ActionClickRMB(Action):
#    def __init__(self, dx, dy):
#        self.dx = dx
#        self.dy = dy
#
#    def __repr__(self):
#        return f"ActionMoveDelta(dx={self.dx}, dy={self.dy})"
#
#class ActionMoveDelta(Action):
#    def __init__(self, dx, dy):
#        self.dx = dx
#        self.dy = dy
#
#    def __repr__(self):
#        return f"ActionMoveDelta(dx={self.dx}, dy={self.dy})"
#
#
