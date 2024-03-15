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

class ActionPressRelease(Action):
    def __init__(self, pos, release=False, right=False):
        self.x, self.y = pos
        self.release = release
        self.right = right

    def __repr__(self):
        return f"ActionPressRelease(x={self.x}, y={self.y}, release={self.release}, right={self.right})"

class ActionScroll(Action):
    def __init__(self, pos, scroll):
        self.x, self.y = pos
        self.scroll = scroll

    def __repr__(self):
        return f"ActionScroll(x={self.x}, y={self.y}, scroll={self.scroll})"
