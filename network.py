from message import Message
from typing import Optional


class Network:
    def __init__(self):
        """
        Constructor for Network class.
        """
        self.queue = []

    def queue_message(self, m: Message) -> None:
        """
        Adds a Message to the queue.
        :param m: Message to add to the queue
        :return: None
        """
        self.queue.append(m)

    def extract_message(self) -> Optional[Message]:
        """
        Gets the oldest Message from the queue.
        :return: Either a Message or None
        """
        index = 0
        while self.queue:
            m = self.queue[index]
            if m.src.failed is False and m.dst.failed is False:
                self.queue.pop(index)
                return m
            else:
                if index + 1 < len(self.queue):
                    index += 1
                else:
                    return None
