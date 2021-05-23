from computer import Computer
from message import Message


class Proposer(Computer):
    def __init__(self, _id, sim):
        self.proposed_value = None
        self.id = _id
        self.sim = sim
        self.n = sim.n
        self.value = None
        self.p_id = 0
        self.accepted = set()
        self.rejected = set()
        self.state = 'PROPOSE'
        self.failed = False

    def deliver_message(self, m: Message):
        if m.type == 'PROPOSE':
            self.state = 'PROPOSE'
            self.proposed_value = m.value
            self.value = m.value
            self.handle_propose()
            return f' -> P{m.dst.id} {m.type} {m.value}'
        elif m.type == 'REJECTED':
            if m.id == self.p_id:
                self.rejected.add(m.src)
            if len(self.rejected) > len(self.sim.a) // 2:
                self.handle_propose()
                self.accepted = set()
                self.rejected = set()
            return f'A{m.src.id} -> P{m.dst.id} {m.type} n={m.id}'
        elif m.type == 'PROMISE':
            if m.id == self.p_id and m.type == self.state:
                self.accepted.add(m.src)
            if len(self.accepted) > len(self.sim.a) // 2:
                self.handle_promise(m)
                self.accepted = set()
                self.rejected = set()
            prior = m.prior
            if prior is None:
                return f'A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} (Prior: None)'
            else:
                self.value = prior['v']
                return f'A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} (Prior: n={prior["n"]}, v={prior["v"]})'
        elif m.type == 'ACCEPTED':
            if m.id == self.p_id and m.type == self.state:
                self.accepted.add(m.src)
            if len(self.accepted) > len(self.sim.a) // 2:
                # Put this in function
                self.sim.accepted = m.value
                self.sim.accepted_n = m.id
            #     if len(self.n.queue) == 0:
            #         for learner in self.n.l:
            #             respond_m = Message(self, learner, 'SUCCESS', m.value, m.id, None)
            #             self.n.queue_message(respond_m)
                self.accepted = set()
                self.rejected = set()
            return f'A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} v={self.value}'

    def handle_promise(self, m):
        self.state = 'ACCEPTED'
        for acceptor in self.sim.a:
            respond_m = Message(self, acceptor, 'ACCEPT', self.value, self.p_id, None)
            self.n.queue_message(respond_m)
        # respond_m = Message(self, m.src, 'ACCEPT', self.value, self.id)
        # self.n.queue_message(respond_m)

    def handle_propose(self):
        self.state = 'PROMISE'
        self.sim.propose_counter += 1
        self.p_id = self.sim.propose_counter

        for acceptor in self.sim.a:
            respond_m = Message(self, acceptor, 'PREPARE', None, self.p_id, None)
            self.n.queue_message(respond_m)

    def __str__(self):
        return f'P{self.id}'
