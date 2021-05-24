from computer import Computer
from message import Message
import numpy as np


class Learner(Computer):
    def __init__(self, _id, sim):
        self.id = _id
        self.failed = False
        self.sim = sim
        self.matrices = {}
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'

    def deliver_message(self, m: Message):
        if m.type == 'SUCCESS':
            print(f'{self.sim.current_tick:04}: L{self.id} PREDICTED n={self.handle_success(m)}')

    def handle_success(self, m: Message):
        m_split = m.value.split(':')
        lang = m_split[0]
        data = m_split[1]
        if lang not in self.matrices:
            self.matrices[lang] = np.zeros((28, 28))
        if len(data) == 1:
            data += ' '
        self.matrices[lang][self.allowed_chars.index(data[0]), self.allowed_chars.index(data[1])] += 1
        return self.count_matrices()

    def count_matrices(self):
        n = 0
        for i in self.matrices:
            n += np.sum(self.matrices[i])
        return n
