import time

from action import *
import config
from utils import add, signed_power


MOVEMENT_SENSITIVITY = config.CONTROLLER_MOVEMENT_SENSITIVITY
MOVEMENT_AMORTIZATION = config.CONTROLLER_MOVEMENT_AMORTIZATION
GRAVITY = config.CONTROLLER_GRAVITY

class Controller:
    class HistoryElement:
        def __init__(self, data, actions, timestamp):
            self.data = data
            self.actions = actions
            self.timestamp = timestamp

        def __repr__(self):
            return f"HistoryElement(data={self.data}, actions={self.actions}, timestamp={self.timestamp})"

    HISTORY_SIZE = config.CONTROLLER_HISTORY_SIZE
    history = []
    mode = None

    @staticmethod
    def process(data, timestamp):
        # update history, but add element without action (yet)
        new_history_element = Controller.HistoryElement(data=data, timestamp=timestamp, actions=None)
        Controller.history = [new_history_element] + Controller.history
        # decide new action
        actions = Controller.decide_actions()
        # perform action; if it failed - delete element from history, else update action and keep history finite
        try:
            Controller.take_actions(actions)
            Controller.history[0].actions = actions
            Controller.history = Controller.history[:Controller.HISTORY_SIZE]
        except:
            Controller.history = Controller.history[1:]

    @staticmethod
    def decide_actions():
        new_data, new_timestamp = Controller.history[0].data, Controller.history[0].timestamp
        cur_mouse_pos = Action.get_position()
        # DEBUG
        print(new_data, new_timestamp)
        print(Controller.history)
        print(f"{cur_mouse_pos=}")
        # TODO
        #if data.z == 1:
        #    return [ActionMove(pos=add(cur_mouse_pos, (data.x, data.y)))]
        #if data.z == 2:
        #    return [ActionClick(pos=add(cur_mouse_pos, (data.x, data.y)), button=Action.LEFT)]
        #if data.z == 3:
        #    return [ActionPressRelease(pos=add(cur_mouse_pos, (data.x, data.y)), release=False, button=Action.LEFT)]
        #return [ActionScroll(pos=add(cur_mouse_pos, (data.x, data.y)), scroll=data.z)]
        #return []
        delta_time = 0
        if len(Controller.history) > 1:
            delta_time = new_timestamp - Controller.history[1].timestamp
        speed = (
            -signed_power(new_data.ax / GRAVITY, MOVEMENT_AMORTIZATION) * MOVEMENT_SENSITIVITY * delta_time,
            -signed_power(new_data.ay / GRAVITY, MOVEMENT_AMORTIZATION) * MOVEMENT_SENSITIVITY * delta_time,
        )
        return [ActionMove(pos=add(cur_mouse_pos, speed))]

    @staticmethod
    def take_actions(actions):
        print("Performing actions", actions)
        for action in actions:
            action.perform()
