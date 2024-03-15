from abc import ABC


class Action(ABC):
    pass

class ActionMoveDelta(Action):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"ActionMoveDelta(dx={self.dx}, dy={self.dy})"
