from classes.message import Message


class Proposer:
    def __init__(self, _id: int, sim: 'Simulation'):
        """
        Constructor for Proposer class.
        :param _id: Id for the acceptor.
        :param sim: Simulation object.
        """
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

    def receive_message(self, m: Message) -> None:
        """
        receives a Message.
        :param m: The Message to receive.
        :return: None.
        """
        if m.type == 'PROPOSE':
            self.handle_propose(m)
            print(f'{self.sim.current_tick:04}: -> P{m.dst.id} {m.type} {m.value}')
        elif m.type == 'REJECTED':
            self.handle_rejected(m)
        elif m.type == 'PROMISE':
            prior = m.prior
            # Only print prior if there is a prior.
            if prior is None:
                print(f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} (Prior: None)')
            else:
                self.value = prior['v']
                print(f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} (Prior: n={prior["n"]}, v={prior["v"]})')
            self.poll(m)
        elif m.type == 'ACCEPTED':
            print(f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id} v={self.value}')
            self.poll(m)

    def poll(self, m: Message) -> None:
        """
        Checks if proposed value is accepted.
        :param m: The Message to check.
        :return: None.
        """
        if m.id == self.p_id and m.type == self.state:
            self.accepted.add(m.src)
        # If a majority of the Acceptors did not return with REJECTED we accepted it.
        if len(self.accepted) > len(self.sim.a) // 2:
            if self.state == 'PROMISE':
                self.handle_promise(m)
            elif self.state == 'ACCEPTED':
                self.handle_accepted(m)
            self.accepted = set()
            self.rejected = set()

    def handle_rejected(self, m: Message) -> None:
        """
        Handles the REJECTED Message type.
        :param m: The Message to check.
        :return: None.
        """
        if m.id == self.p_id:
            self.rejected.add(m.src)
        # If a majority of the Acceptors did return with REJECTED we reject it and start over.
        if len(self.rejected) > len(self.sim.a) // 2:
            self.handle_propose(m)
            self.accepted = set()
            self.rejected = set()
        print(f'{self.sim.current_tick:04}: A{m.src.id} -> P{m.dst.id} {m.type} n={m.id}')

    def handle_accepted(self, m: Message) -> None:
        """
        Handles the ACCEPTED Message type.
        :param m: The Message to check.
        :return: None.
        """
        self.sim.accepted = m.value
        self.sim.accepted_n = m.id

    def handle_promise(self, m: Message) -> None:
        """
        Handles the PROMISE Message type.
        :param m: The Message to check.
        :return: None.
        """
        self.state = 'ACCEPTED'
        for acceptor in self.sim.a:
            respond_m = Message(self, acceptor, 'ACCEPT', self.value, self.p_id, None)
            self.n.queue_message(respond_m)

    def handle_propose(self, m) -> None:
        """
        Handles the PROPOSE Message type.
        :param m: The Message to check.
        :return: None.
        """
        self.proposed_value = m.value
        self.value = m.value
        self.state = 'PROMISE'
        self.sim.propose_counter += 1
        self.p_id = self.sim.propose_counter

        for acceptor in self.sim.a:
            respond_m = Message(self, acceptor, 'PREPARE', None, self.p_id, None)
            self.n.queue_message(respond_m)

    def __str__(self) -> str:
        """
        Makes the Proposer printable.
        :return: String like representation of this Acceptor.
        """
        return f'P{self.id}'
