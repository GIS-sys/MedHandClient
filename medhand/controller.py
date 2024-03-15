import mouse
import time

from action import ActionClick, ActionMove
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
        #return ActionMove(pos=add(cur_mouse_pos, (x, y)))
        return ActionClick(pos=add(cur_mouse_pos, (x, y)), right=True)

    @staticmethod
    def take_action(action):
        # TODO
        print(action)
        if isinstance(action, ActionMove):
            mouse.move(action.x, action.y, duration=0, absolute=True)
        elif isinstance(action, ActionClick):
            mouse.move(action.x, action.y, duration=0, absolute=True)
            mouse.press(button=button_name(action.right))
            time.sleep(MOUSE_CLICK_DELAY)
            mouse.release(button=button_name(action.right))
