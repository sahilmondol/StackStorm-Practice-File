import sys

from st2common.runners.base_action import Action

class Greet(Action):
    def run(self, message):
        print(message)

        if message >= 0:
            return (True, message)
        return (False, message)