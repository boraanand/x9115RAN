"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
from collections import defaultdict


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def face_hist(self):
        """Builds a histogram of the faces that appear in the hand.

        Stores the result in attribute suits.
        """
        self.faces = {}
        for card in self.cards:
            self.faces[card.rank] = self.faces.get(card.rank, 0) + 1
        
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        return self.has_n_ofkind(2)
        
    def has_n_ofkind(self, n):
        """Returns True if the hand has a n of same kind (pair, 3 of a kind, 4 of a kind), False otherwise.
      
        Note that this works correctly for hands with more than n cards.
        """
        self.face_hist()
        for val in self.faces.values():
            if val >= n:
                return True
        return False
    
    def has_twopairs(self):
        """Returns True if the hand has a n of same kind (pair, 3 of a kind, 4 of a kind), False otherwise.
      
        Note that this works correctly for hands with more than n cards.
        """
        self.face_hist()
        num_pairs = 0
        for val in self.faces.values():
            if val >= 2:
                num_pairs += 1
                if num_pairs == 2:
                    return True
        return False

    def has_threeofakind(self):
        return self.has_n_ofkind(3)


    def isStraight(self, cards):
        if cards[0] == (cards[1] - 1) == (cards[2] - 2) == (cards[3] - 3) == (cards[4] - 4):
            return True
        return False
    
    
    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.face_hist()
        cards = self.faces.keys()
        if self.faces.get(1):
            cards.append(14) #Ace can form a sequence with 2,3,4,5 and with 10, Jack, Queen, King
        for i in range(0, len(cards)-4):
            if self.isStraight(cards[i:i+5]):
                return True
        return False

    def has_fullhouse(self):
        """Returns True if the hand has a full house, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_twopairs() & self.has_threeofakind()

    def has_fourofakind(self):
        return self.has_n_ofkind(4)

    def has_straightflush(self):
        """Returns True if the hand has a straight flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
#         Group cards by suit
        groups= defaultdict( list )
        for obj in self.cards:
            groups[obj.suit].append( obj )
        new_list = groups.values()
        
        for suit_cards in new_list: 
#           For a particular suit, check for straight
            items=[c_suit.rank for c_suit in suit_cards]
            if items[0] == 1:
                items.append(14)
            for i in range(0, len(items)-4):
                if self.isStraight(items[i:i+5]):
                    return True
        return False

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print "Has flush:",hand.has_flush()
        print "Has pair:",hand.has_pair()
        print "Has two pairs:",hand.has_twopairs()
        print "Has 3 of a kind:",hand.has_threeofakind()
        print "Has straight:",hand.has_straight()
        print "Has full house:",hand.has_fullhouse()
        print "Has 4 of a kind:",hand.has_fourofakind()
        print "Has straight flush:",hand.has_straightflush()
        print ''

