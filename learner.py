from computer import Computer
from message import Message

class Learner(Computer):
    def __init__(self, _id, sim):
        self.id = _id
        self.sim = sim