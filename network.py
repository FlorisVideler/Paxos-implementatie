from message import Message


class Network:
    queue = []

    def queue_message(self, m: Message):
        self.queue.append(m)

    def extract_message(self):
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
