from computer import Computer
from message import Message
import numpy as np

class Learner(Computer):
    def __init__(self, _id, sim):
        self.id = _id
        self.sim = sim
        self.matrices = {}
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'

    def deliver_message(self, m: Message):
        if m.type == 'SUCCESS':
            self.handle_success(m)
            print('LEARNER', m.value)

    def handle_success(self, m: Message):
        m_split = m.value.split(':')
        lang = m_split[0]
        data = m_split[1]
        if lang not in self.matrices:
            self.matrices[lang] = np.zeros((28, 28))
        self.matrices[lang][self.allowed_chars.index(data[0]), self.allowed_chars.index(data[1])] += 1
        self.count_matrices()

    def count_matrices(self):
        n = 0
        for i in self.matrices:
            n += np.sum(self.matrices[i])
        print('LN', n)