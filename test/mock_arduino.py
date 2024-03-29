import os
from pathlib import Path
import requests
from requests_futures.sessions import FuturesSession
import time

import sys
sys.path.append('medhand')
import config


class Action:
    HTTP_HOST = f"http://localhost:{config.MAIN_PORT}/new_data"
    SESSION = FuturesSession()
    SEPARATOR = ","
    BLOCKING = True

    def __init__(self, line):
        args = line.split(self.SEPARATOR)
        self.ax, self.ay, self.az = map(int, args[0:3])
        self.gx, self.gy, self.gz = map(int, args[3:6])
        self.t = float(args[6])

    def send(self):
        data = {"ax": self.ax, "ay": self.ay, "az": self.az, "gx": self.gx, "gy": self.gy, "gz": self.gz}
        print("Sending:", data)
        if self.BLOCKING:
            r = requests.post(self.HTTP_HOST, json=data)
            print(r.status_code)
        else:
            self.SESSION.post(self.HTTP_HOST, json=data)
        time.sleep(self.t)


class Scene:
    FOLDER = f"{os.path.dirname(os.path.realpath(__file__))}/scenes/"

    def _get_possible_scenes(self):
        self.possible_scenes = []
        for path in Path(self.FOLDER).rglob('*'):
            self.possible_scenes.append([path.resolve(), path.name])

    def _choose_scene(self):
        for i, path in enumerate(self.possible_scenes):
            print(f"{i}: {path[0]}")
        while True:
            number_str = input("Choose and enter corresponding number: ")
            try:
                number = int(number_str)
            except ValueError:
                continue
            if number < 0 or number >= len(self.possible_scenes):
                continue
            self.chosen_scene_index = number
            break

    def _read_actions(self):
        with open(self.possible_scenes[self.chosen_scene_index][0], "r") as f:
            self.actions = []
            for line in f:
                line = line.strip()
                if line == "" or line.startswith(("#", "//")):
                    continue
                self.actions.append(Action(line))

    def __init__(self):
        self._get_possible_scenes()
        self._choose_scene()
        self._read_actions()


scene = Scene()
for action in scene.actions:
    action.send()
