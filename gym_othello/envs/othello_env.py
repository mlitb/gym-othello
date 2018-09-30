import gym
from gym import error, spaces, utils
from gym.utils import seeding


class OthelloEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super().__init__()


    def step(self, action):
        super().reset(action)


    def reset(self):
        super().reset()


    def render(self, mode='human', close=False):
        super().render(mode, close)
