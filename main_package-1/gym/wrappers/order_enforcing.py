import gym


class OrderEnforcing(gym.Wrapper):
    def __init__(self, env):
        super(OrderEnforcing, self).__init__(env)
        self._has_reset = False

    def step(self, action, is_safe, self_prediction, self_heading_prediction):
        assert self._has_reset, "Cannot call env.step() before calling reset()"
        observation, reward, done, info, ttc = self.env.step(action, is_safe, self_prediction, self_heading_prediction)
        return observation, reward, done, info, ttc

    def reset(self, **kwargs):
        self._has_reset = True
        return self.env.reset(**kwargs)
