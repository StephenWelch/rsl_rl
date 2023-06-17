
class PETS:
    def __init__(self):
        ...
    def init_storage(self, num_envs, num_transitions_per_env, actor_obs_shape, critic_obs_shape, action_shape):
        """
        Creates rollout storage
        :param num_envs:
        :param num_transitions_per_env:
        :param actor_obs_shape:
        :param critic_obs_shape:
        :param action_shape:
        :return:
        """
        ...

    def test_mode(self):
        """
        Configure algorithm for testing/evaluation
        :return:
        """
        ...

    def train_mode(self):
        """
        Configure algorithm for training
        :return:
        """
        ...

    def act(self, obs, critic_obs):
        """
        Poll the algorithm for an action given an observation
        :param obs:
        :param critic_obs:
        :return:
        """

    def process_env_step(self, rewards, dones, infos):
        """
        Processes an environment step
        :param rewards:
        :param dones:
        :param infos:
        :return:
        """

    def compute_returns(self, last_critic_obs):
        """
        Computes returns over the episode
        :param last_critic_obs:
        :return:
        """
        ...

    def update(self):
        """
        Updates algorithm parameters.
        :return:
        """
        ...
