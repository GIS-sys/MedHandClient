import mouse
import time

from action import *
from utils import add, button_name


class Controller:
    MEMORY_SIZE = 5
    history = []

    MOUSE_CLICK_DELAY = 0.01

    @staticmethod
    def process(data):
        action = Controller.decide_action(data)
        Controller.take_action(action)
        Controller.history = ([(data, action)] + Controller.history)[:Controller.MEMORY_SIZE]

    @staticmethod
    def decide_action(data):
        # TODO
        #print(Controller.history)
        x, y, z = data.x, data.y, data.z
        cur_mouse_pos = mouse.get_position()
        if z == 1:
            return ActionMove(pos=add(cur_mouse_pos, (x, y)))
        if z == 2:
            return ActionClick(pos=add(cur_mouse_pos, (x, y)), right=True)
        if z == 3:
            return ActionPressRelease(pos=add(cur_mouse_pos, (x, y)), release=False, right=False) #TODO
        return ActionScroll(pos=add(cur_mouse_pos, (x, y)), scroll=z) # TODO

    @staticmethod
    def take_action(action):
        # TODO
        print(action)
        if isinstance(action, ActionMove):
            mouse.move(action.x, action.y, duration=0, absolute=True)
        elif isinstance(action, ActionPressRelease):
            mouse.move(action.x, action.y, duration=0, absolute=True)
            if action.release:
                mouse.release(button=button_name(action.right))
            else:
                mouse.press(button=button_name(action.right))
        elif isinstance(action, ActionScroll):
            mouse.move(action.x, action.y, duration=0, absolute=True)
            mouse.wheel(action.scroll)
        elif isinstance(action, ActionClick):
            mouse.move(action.x, action.y, duration=0, absolute=True)
            mouse.press(button=button_name(action.right))
            time.sleep(MOUSE_CLICK_DELAY)
            mouse.release(button=button_name(action.right))
