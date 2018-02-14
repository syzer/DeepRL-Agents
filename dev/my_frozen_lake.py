# todo https://gym.openai.com/evaluations/eval_lEi8I8v2QLqEgzBxcvRIaA/
import gym

env = gym.make('FrozenLake-v0')
env.reset() # => observation
env.render()


def random_action():
    return env.action_space.sample()


env.step(random_action())
# print(env.action_space)
# print(env.observation_space)

env.render()
# return observations
# (1, 0.0, False, {'prob': 0.3333333333333333})


observation, reward, done, info = env.step(random_action())
# print(observation) # observation in the frozen lake is is the how far we got

print(env.action_space)

env.render()
action = 1 if observation > 0 else 2
env.step(action)
action = 1 if observation > 0 else 2
env.step(action)
action = 1 if observation > 0 else 2
env.step(action)
env.render()

# SFFF       (S: starting point, safe)
# FHFH       (F: frozen surface, safe)
# FFFH       (H: hole, fall to your doom)
# HFFG       (G: goal, where the frisbee is located)
