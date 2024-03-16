from abc import ABC
from pynput.mouse import Button, Controller as MouseController


class Action(ABC):
    mouse = MouseController()
    MOUSE_CLICK_DELAY = 0.01
    RIGHT = Button.right
    LEFT = Button.left

    def perform(self):
        pass

    @classmethod
    def get_position(cls):
        return cls.mouse.position


class ActionMove(Action):
    def __init__(self, pos):
        self.pos = pos

    def perform(self):
        self.mouse.position = self.pos

    def __repr__(self):
        return f"ActionMove(x={self.pos[0]}, y={self.pos[1]})"

class ActionClick(Action):
    def __init__(self, button=Action.LEFT, pos=None):
        self.pos = pos
        self.button = button

    def perform(self):
        if self.pos:
            self.mouse.position = self.pos
        self.mouse.click(self.button)

    def __repr__(self):
        res = ""
        if self.pos:
            res = f"x={self.pos[0]}, y={self.pos[1]}, "
        return f"ActionClick({res}button={self.button})"

class ActionPressRelease(Action):
    def __init__(self, pos, release=False, button=Action.LEFT):
        self.pos = pos
        self.release = release
        self.button = button

    def perform(self):
        if self.pos:
            self.mouse.position = self.pos
        if self.release:
            self.mouse.release(self.button)
        else:
            self.mouse.press(self.button)

    def __repr__(self):
        return f"ActionPressRelease(x={self.pos[0]}, y={self.pos[1]}, release={self.release}, button={self.button})"

class ActionScroll(Action):
    def __init__(self, pos, scroll):
        self.pos = pos
        self.scroll = scroll

    def perform(self):
        if self.pos:
            self.mouse.position = self.pos
        self.mouse.scroll(0, self.scroll)

    def __repr__(self):
        return f"ActionScroll(x={self.pos[0]}, y={self.pos[1]}, scroll={self.scroll})"
