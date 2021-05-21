class Message:
    def __init__(self, src, dst, _type, value, _id, prior):
        self.src = src
        self.dst = dst
        self.type = _type
        self.value = value
        self.id = _id
        self.prior = prior

    def __str__(self):
        return f'{self.src} -> {self.dst} {self.type} {self.id} {self.value} {self.prior}'

    def __repr__(self):
        return f'{self.src} -> {self.dst} {self.type} {self.id} {self.value} {self.prior}'
