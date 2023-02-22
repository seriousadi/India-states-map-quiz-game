import os

#
dir_name = r"D:\programming channels work\python file\resources\Images\India's map\India's states highlited"
states = os.listdir(dir_name)

state_names = [state.replace('.png', '').lower() for state in states]
print(state_names)


class gameLogic():
    def __init__(self):
        pass

    def checker(self, entered_key):

        if self.name_equalizer(entered_key) in state_names:
            return True
        else:
            return False

    def name_equalizer(self, state_name):
        modified_entered_key = state_name.replace('&', 'and').lower()
        return modified_entered_key