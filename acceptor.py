from computer import Computer
from message import Message


class Acceptor(Computer):
    def __init__(self, _id, sim):
        self.id = _id
        self.sim = sim
        self.n = sim.n
        self.prior_promised_id = 0
        self.prior_promised_value = None
        self.failed = False

    def deliver_message(self, m: Message):
        if m.type == 'PREPARE':
            self.handle_prepare(m)
            return f'P{m.src.id} -> A{self.id} {m.type} n={m.id}'
        elif m.type == 'ACCEPT':
            self.handle_accept(m)
            return f'P{m.src.id} -> A{self.id} {m.type} n={m.id} v={m.value}'

    def handle_accept(self, m):
        if m.id < self.prior_promised_id:
            respond_m = Message(self, m.src, 'REJECTED', None, m.id)
        else:
            self.prior_promised_id = m.id
            self.prior_promised_value = m.value
            respond_m = Message(self, m.src, 'ACCEPTED', m.value, m.id)
        self.n.queue_message(respond_m)

    def handle_prepare(self, m):
        if m.id < self.prior_promised_id:
            respond_m = Message(self, m.src, 'REJECTED', None, m.id)
        else:
            self.prior_promised_id = m.id
            respond_m = Message(self, m.src, 'PROMISE', None, m.id)
        self.n.queue_message(respond_m)

    def __str__(self):
        return f'A{self.id}'
