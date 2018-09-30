from gym.envs.registration import register

register(
    id='OthelloVsSelf-v0',
    entry_point='gym_othello.envs:OthelloEnv',
    kwargs={'self_play' : True},
)
register(
    id='OthelloVsBot-v0',
    entry_point='gym_othello.envs:OthelloEnv',
    kwargs={'self_play' : False},
)