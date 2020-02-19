# Class to represent an Uno card
# Peter Brown, 2020-02-18

from typing import cast, List, Tuple
# import superclass
from Card import Card

class UnoCard(Card):
    """Class to represent an Uno card."""
    COLOR_RANKS:Tuple[str, ...] = ('0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two')
    WILD_RANKS:Tuple[str, str] = ('Draw Four', '')
    RANKS:Tuple[str, ...] = COLOR_RANKS + WILD_RANKS
    MIN_VAL:int = 0
    MAX_COLOR_VAL:int = len(COLOR_RANKS) - 1
    MAX_VAL:int = len(RANKS) - 1
    COLOR_SUITS:Tuple[str, ...] = ('Red', 'Yellow', 'Green', 'Blue')
    WILD_SUITS:Tuple[str] = ('Wild',)
    SUITS:Tuple[str, ...] = COLOR_SUITS + WILD_SUITS

    def _invariant(self) -> bool:
        valid_color:bool = self._suit in self.COLOR_SUITS and \
            (self.MIN_VAL <= self._rank <= self.MAX_COLOR_VAL)
        valid_wild:bool = self._suit == 'Wild' and \
            self.MAX_COLOR_VAL < self._rank <= self.MAX_VAL
        return valid_color or valid_wild

    def __init__(self, rank:str, suit:str) -> None:
        # Just call the Card constructor
        super().__init__(rank, suit)
