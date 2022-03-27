import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame:
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("hearts", 7)
        self.card2 = Card("hearts", 1)
        self.card3 = Card("clubs", 10)
        self.cards = [self.card1, self.card2, self.card3]
    
    def test_check_for_ace_false(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(False, result)

    def test_check_for_ace_true(self):
        result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, result)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card3)
        self.assertEqual(self.card3, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual(18, result)
