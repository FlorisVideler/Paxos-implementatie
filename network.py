from message import Message
from typing import Optional


class Network:
    def __init__(self) -> None:
        self.queue = []

    def queue_message(self, m: Message) -> None:
        self.queue.append(m)

    def extract_message(self) -> Optional[None, Message]:
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
