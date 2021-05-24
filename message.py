from typing import Optional


class Message:
    def __init__(self, src: object, dst: object, _type: str, value: Optional[None, str], _id: int, prior: Optional[None, dict]) -> None:
        self.src = src
        self.dst = dst
        self.type = _type
        self.value = value
        self.id = _id
        self.prior = prior

    def __str__(self) -> str:
        return f'{self.src} -> {self.dst} {self.type} {self.id} {self.value} {self.prior}'

    def __repr__(self) -> str:
        return f'{self.src} -> {self.dst} {self.type} {self.id} {self.value} {self.prior}'
