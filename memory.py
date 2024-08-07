import numpy as np


class ReplayBuffer:
    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.states = []
        self.values = []
        self.probs = []
        self.actions = []
        self.rewards = []
        self.dones = []

    def sample(self):
        return (
            np.array(self.states),
            np.array(self.values),
            np.array(self.actions),
            np.array(self.probs),
            np.array(self.rewards),
            np.array(self.dones),
        )

    def generate_batches(self):
        n_states = len(self.states)
        n_batches = int(n_states // self.batch_size)
        ids = np.arange(n_states, dtype=np.int64)
        np.random.shuffle(ids)
        batches = [
            ids[i * self.batch_size : (i + 1) * self.batch_size]
            for i in range(n_batches)
        ]
        return batches

    def store_transition(self, state, value, action, probs, reward, done):
        self.states.append(state)
        self.values.append(value)
        self.actions.append(action)
        self.probs.append(probs)
        self.rewards.append(reward)
        self.dones.append(done)

    def clear_memory(self):
        self.states = []
        self.probs = []
        self.actions = []
        self.rewards = []
        self.dones = []
        self.values = []
