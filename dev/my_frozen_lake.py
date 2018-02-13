import gym
env = gym.make('FrozenLake-v0')
env.reset()
env.render()
env.reset()
env.render()

# SFFF       (S: starting point, safe)
# FHFH       (F: frozen surface, safe)
# FFFH       (H: hole, fall to your doom)
# HFFG       (G: goal, where the frisbee is located)
