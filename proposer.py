from message import Message


class Proposer:
    def __init__(self, _id: int, sim: 'Simulation') -> None:
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

    def deliver_message(self, m: Message) -> None:
        if m.type == 'PROPOSE':
            self.handle_propose(m)
            print(f'{self.sim.current_tick:04}: -> P{m.dst.id} {m.type} {m.value}')
        elif m.type == 'REJECTED':
            self.handle_rejected(m)
        elif m.type == 'PROMISE':
            self.poll(m)
        elif m.type == 'ACCEPTED':
            self.poll(m)

    def poll(self, m: Message) -> None:
        if m.id == self.p_id and m.type == self.state:
            self.accepted.add(m.src)
        if len(self.accepted) > len(self.sim.a) // 2:
            if self.state == 'PROMISE':
                self.handle_promise(m)
            elif self.state == 'ACCEPTED':
                self.handle_accepted(m)
            self.accepted = set()
            self.rejected = set()

    def handle_rejected(self, m: Message) -> None:
        if m.id == self.p_id:
            self.rejected.add(m.src)
        if len(self.rejected) > len(self.sim.a) // 2:
            self.handle_propose(m)
            self.accepted = set()
            self.rejected = set()
        print(f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id}')

    def handle_accepted(self, m: Message) -> None:
        print(f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} v={self.value}')
        self.sim.accepted = m.value
        self.sim.accepted_n = m.id

    def handle_promise(self, m: Message) -> None:
        self.state = 'ACCEPTED'
        prior = m.prior
        if prior is None:
            print(f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} (Prior: None)')
        else:
            self.value = prior['v']
            print(
                f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} (Prior: n={prior["n"]}, v={prior["v"]})')
        for acceptor in self.sim.a:
            respond_m = Message(self, acceptor, 'ACCEPT', self.value, self.p_id, None)
            self.n.queue_message(respond_m)

    def handle_propose(self, m) -> None:
        self.proposed_value = m.value
        self.value = m.value
        self.state = 'PROMISE'
        self.sim.propose_counter += 1
        self.p_id = self.sim.propose_counter

        for acceptor in self.sim.a:
            respond_m = Message(self, acceptor, 'PREPARE', None, self.p_id, None)
            self.n.queue_message(respond_m)

    def __str__(self) -> str:
        return f'P{self.id}'
