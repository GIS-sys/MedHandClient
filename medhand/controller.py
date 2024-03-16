from pynput.mouse import Button, Controller as MouseController
import time

from action import *
from utils import add, button_name


class Controller:
    MEMORY_SIZE = 5
    history = []
    mouse = MouseController()

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
        cur_mouse_pos = Controller.mouse.position
        if z == 1:
            return ActionMove(pos=add(cur_mouse_pos, (x, y)))
        if z == 2:
            return ActionClick(pos=add(cur_mouse_pos, (x, y)), right=False)
        if z == 3:
            return ActionPressRelease(pos=add(cur_mouse_pos, (x, y)), release=False, right=False) #TODO
        return ActionScroll(pos=add(cur_mouse_pos, (x, y)), scroll=z) # TODO

    @staticmethod
    def take_action(action):
        # TODO
        print(action)
        if isinstance(action, ActionMove):
            Controller.mouse.position = (action.x, action.y)
        elif isinstance(action, ActionPressRelease):
            Controller.mouse.position = (action.x, action.y)
            if action.release:
                Controller.mouse.release(button_name(action.right))
            else:
                Controller.mouse.press(button=button_name(action.right))
        elif isinstance(action, ActionScroll):
            Controller.mouse.position = (action.x, action.y)
            Controller.mouse.scroll(0, action.scroll)
        elif isinstance(action, ActionClick):
            Controller.mouse.position = (action.x, action.y)
            Controller.mouse.press(button_name(action.right))
            time.sleep(Controller.MOUSE_CLICK_DELAY)
            Controller.mouse.release(button_name(action.right))
