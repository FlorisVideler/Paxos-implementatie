from typing import Optional


class Message:
    def __init__(self, src: object, dst: object, _type: str, value: Optional[str], _id: Optional[int], prior: Optional[dict]):
        """
        Constructor for Message class.
        :param src: Where the Message came from.
        :param dst: Where the message needs to go.
        :param _type: The type of message.
        :param value: The value of the Message.
        :param _id: The id of the Message.
        :param prior: The prior accepted value.
        """
        self.src = src
        self.dst = dst
        self.type = _type
        self.value = value
        self.id = _id
        self.prior = prior

    def __str__(self) -> str:
        """
        Makes the Message printable.
        :return: String like representation of this Message.
        """
        return f'{self.src} -> {self.dst} {self.type} {self.id} {self.value} {self.prior}'

    def __repr__(self) -> str:
        """
        :return: String like representation of this Message.
        """
        return f'{self.src} -> {self.dst} {self.type} {self.id} {self.value} {self.prior}'
