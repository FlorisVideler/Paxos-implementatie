from message import Message
import numpy as np


class Learner:
    def __init__(self, _id: int, sim: 'Simulation') -> None:
        self.id = _id
        self.failed = False
        self.sim = sim
        self.matrices = {}
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyz *'

    def deliver_message(self, m: Message) -> None:
        if m.type == 'SUCCESS':
            print(f'{self.sim.current_tick:04}: L{self.id} PREDICTED n={self.handle_success(m)}')

    def handle_success(self, m: Message) -> float:
        m_split = m.value.split(':')
        lang = m_split[0]
        data = m_split[1]
        if lang not in self.matrices:
            self.matrices[lang] = np.zeros((28, 28))
        if len(data) == 1:
            data += ' '
        self.matrices[lang][self.allowed_chars.index(data[0]), self.allowed_chars.index(data[1])] += 1
        return self.count_matrices()

    def count_matrices(self) -> float:
        n = 0
        for i in self.matrices:
            n += np.sum(self.matrices[i])
        return n
