import time

from action import *
from utils import add


class Controller:
    MEMORY_SIZE = 5
    history = []

    @staticmethod
    def process(data):
        actions = Controller.decide_actions(data)
        Controller.take_actions(actions)
        Controller.history = ([(data, actions)] + Controller.history)[:Controller.MEMORY_SIZE]

    @staticmethod
    def decide_actions(data):
        x, y, z = data.x, data.y, data.z
        cur_mouse_pos = Action.get_position()
        # TODO
        print(Controller.history)
        print(f"{cur_mouse_pos=}")
        if z == 1:
            return [ActionMove(pos=add(cur_mouse_pos, (x, y)))]
        if z == 2:
            return [ActionClick(pos=add(cur_mouse_pos, (x, y)), button=Action.LEFT)]
        if z == 3:
            return [ActionPressRelease(pos=add(cur_mouse_pos, (x, y)), release=False, button=Action.LEFT)]
        return [ActionScroll(pos=add(cur_mouse_pos, (x, y)), scroll=z)]

    @staticmethod
    def take_actions(actions):
        print("Performing actions", actions)
        for action in actions:
            action.perform()
