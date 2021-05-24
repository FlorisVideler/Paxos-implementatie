from message import Message
from typing import Optional


class Acceptor:
    def __init__(self, _id: int, sim: 'Simulation') -> None:
        self.id = _id
        self.sim = sim
        self.n = sim.n
        self.prior_promised_id = 0
        self.prior_promised_value = None
        self.failed = False

    def get_prior(self) -> Optional[dict]:
        if self.prior_promised_value is None:
            return None
        else:
            return {'n': self.prior_promised_id, 'v': self.prior_promised_value}

    def deliver_message(self, m: Message) -> None:
        if m.type == 'PREPARE':
            self.handle_prepare(m)
            print(f'{self.sim.current_tick:04}: P{m.src.id} -> A{self.id} {m.type} n={m.id}')
        elif m.type == 'ACCEPT':
            self.handle_accept(m)
            print(f'{self.sim.current_tick:04}: P{m.src.id} -> A{self.id} {m.type} n={m.id} v={m.value}')

    def handle_accept(self, m: Message) -> None:
        if m.id < self.prior_promised_id:
            respond_m = Message(self, m.src, 'REJECTED', None, m.id, None)
        else:
            self.prior_promised_id = m.id
            self.prior_promised_value = m.value
            respond_m = Message(self, m.src, 'ACCEPTED', m.value, m.id, None)
        self.n.queue_message(respond_m)

    def handle_prepare(self, m: Message) -> None:
        if m.id < self.prior_promised_id:
            respond_m = Message(self, m.src, 'REJECTED', None, m.id, None)
        else:
            respond_m = Message(self, m.src, 'PROMISE', None, m.id, self.get_prior())
            self.prior_promised_id = m.id
        self.n.queue_message(respond_m)

    def __str__(self) -> str:
        return f'A{self.id}'
