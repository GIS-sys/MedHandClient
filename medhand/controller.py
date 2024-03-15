import mouse

from action import ActionMoveDelta


class Controller:
    MEMORY_SIZE = 5
    history = []

    @staticmethod
    def process(data):
        action = Controller.decideAction(data)
        Controller.takeAction(action)
        Controller.history = ([(data, action)] + Controller.history)[:Controller.MEMORY_SIZE]

    @staticmethod
    def decideAction(data):
        print(Controller.history)
        x, y, z = data.x, data.y, data.z
        return ActionMoveDelta(dx=x, dy=y)

    @staticmethod
    def takeAction(action):
        print(action)
        if isinstance(action, ActionMoveDelta):
            mouse.move(action.dx, action.dy, duration=0, absolute=False)
