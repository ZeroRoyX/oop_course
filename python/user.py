from account import Account
from card import Card

class User(Account):
    card = Card()

    def __init__(self, id, name, document, email, password, card):
        super().__init__(id, name, document, email, password)
        self.card = card
