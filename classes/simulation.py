from classes.proposer import Proposer
from classes.acceptor import Acceptor
from classes.learner import Learner
from classes.network import Network
from classes.message import Message


class Simulation:
    def __init__(self, input_file: str):
        """
        Constructor for Simulation class.
        :param input_file: Path to the input file.
        """
        self.p = []
        self.a = []
        self.l = []
        self.n = Network()
        self.t_max = 0
        self.events = []
        self.propose_counter = 0
        self.accepted = None
        self.accepted_n = 0
        self.current_tick = 0
        self.read_input_file(input_file)

    def read_input_file(self, input_file: str) -> None:
        """
        Loads the input file.
        :param input_file: Path to the input file.
        :return: None.
        """
        with open(input_file, 'r') as file:
            events = file.readlines()
            events = list(map(lambda x: x.rstrip('\n').split(' ', 3), events))
            n_p, n_a, n_l, t_max = events[0]
            events.pop(0)
            self.events = events
            self.t_max = int(t_max)
            self.setup_computers(n_p, n_a, n_l)

    def setup_computers(self, n_p: int, n_a: int, n_l: int) -> None:
        """
        Initializes all the computers.
        :param n_p: Number of Proposers.
        :param n_a: Number of Acceptors.
        :param n_l: Number of Learners.
        :return: None.
        """
        for i in range(int(n_p)):
            self.p.append(Proposer(i + 1, self))

        for i in range(int(n_a)):
            self.a.append(Acceptor(i + 1, self))

        for i in range(int(n_l)):
            self.l.append(Learner(i + 1, self))

    def start(self) -> None:
        """
        Runs the simulations.
        :return: None.
        """
        for tick in range(self.t_max):
            self.current_tick = tick
            tick_done = False  # Tick is done when a message is send!
            for event in self.events:
                if int(event[0]) == tick:
                    event_type = event[1]
                    # Handle if a computer fails.
                    if event_type == 'FAIL':
                        if event[2] == 'PROPOSER':
                            print(f'{tick:04}: P{int(event[3])} **kapot**')
                            self.p[int(event[3]) - 1].failed = True
                        elif event[2] == 'ACCEPTOR':
                            print(f'{tick:04}: A{int(event[3])} **kapot**')
                            self.a[int(event[3]) - 1].failed = True
                    # Handle if a computer recovers.
                    elif event_type == 'RECOVER':
                        if event[2] == 'PROPOSER':
                            print(f'{tick:04}: P{int(event[3])} **gerepareerd**')
                            self.p[int(event[3]) - 1].failed = False
                        elif event[2] == 'ACCEPTOR':
                            print(f'{tick:04}: A{int(event[3])} **gerepareerd**')
                            self.a[int(event[3]) - 1].failed = False
                    # Handle if a proposal is made.
                    elif event_type == 'PROPOSE':
                        tick_done = True
                        m = Message(None, self.p[int(event[2]) - 1], event[1], event[3], None, None)
                        m.dst.receive_message(m)
            if not tick_done:
                self.msg_from_queue()
        for proposer in self.p:
            if proposer.value is not None:
                print(
                    f'P{proposer.id} heeft wel consensus (voorgesteld: {proposer.proposed_value}, geaccepteerd: {self.accepted})')
            else:
                print(f'P{proposer.id} heeft geen consensus')
                        
    def msg_from_queue(self) -> None:
        """
        Handles getting messages from the queue.
        :return: None
        """
        m = self.n.extract_message()
        if m:
            m.dst.receive_message(m)
        else:
            print(f'{self.current_tick:04}: ')


    def success(self) -> None:
        """
        Communicates with the Learners.
        :return:
        """
        for learner in self.l:
            learner.receive_message(Message(self, learner, 'SUCCESS', self.accepted, None, None))

        for acceptor in self.a:
            acceptor.prior_promised_value = None
            acceptor.prior_promised_id = 0
