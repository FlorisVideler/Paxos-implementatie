from proposer import Proposer
from acceptor import Acceptor
from network import Network
from message import Message


class Simulation:
    p = []
    a = []
    e = []
    n = Network()
    t_max = 0
    events = []
    propose_counter = 0

    def __init__(self, input_file):
        self.read_input_file(input_file)

    def read_input_file(self, input_file):
        with open(input_file, 'r') as file:
            events = file.readlines()
            events = list(map(lambda x: x.rstrip().split(' '), events))
            n_p, n_a, t_max = events[0]
            events.pop(0)
            self.events = events
            self.t_max = int(t_max)
            self.setup_computers(n_p, n_a)

    def setup_computers(self, n_p, n_a):
        for i in range(int(n_p)):
            self.p.append(Proposer(i+1, self))

        for i in range(int(n_a)):
            self.a.append(Acceptor(i+1, self))

    def start(self):
        for tick in range(self.t_max):
            if tick == 21:
                print()
            tick_done = False
            tick_output = f'{tick}: '
            for event in self.events:
                if int(event[0]) == tick:
                    tick_done = True
                    event_type = event[1]
                    if event_type == 'FAIL':
                        if event[2] == 'PROPOSER':
                            tick_output += f'P{int(event[3])} kapot'
                            self.p[int(event[3])-1].failed = True
                        elif event[2] == 'ACCEPTOR':
                            tick_output += f'A{int(event[3])} kapot'
                            self.a[int(event[3]) - 1].failed = True
                    elif event_type == 'RECOVER':
                        if event[2] == 'PROPOSER':
                            tick_output += f'P{int(event[3])} gerepareerd'
                            self.p[int(event[3]) - 1].failed = False
                        elif event[2] == 'ACCEPTOR':
                            tick_output += f'A{int(event[3])} gerepareerd'
                            self.a[int(event[3]) - 1].failed = False
                    elif event_type == 'PROPOSE':
                        m = Message(None, self.p[int(event[2]) - 1], event[1], int(event[3]), None)
                        tick_output += m.dst.deliver_message(m)
            if not tick_done:
                m = self.n.extract_message()
                if m:
                    tick_output += m.dst.deliver_message(m)
            print(tick_output)
