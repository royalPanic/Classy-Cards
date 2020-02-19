# Do nothing, successfully
# Peter Brown, 2020-01-07

from typing import cast, List, Tuple
import functools

# functools.total_ordering allows us to get all six ordered comparison
# operators without implementing any but __eq__ and __lt__.
@functools.total_ordering
class Card(object):
    """Class to represent a playing card.  A Card once created 
    is immutable."""

    # Assume aces low
    RANKS:Tuple[str, ...] = ('', 'A', '2', '3', '4', '5', '6', '7',
        '8', '9', '10', 'J', 'Q', 'K')
    MIN_VAL:int = 1
    MAX_VAL:int = len(RANKS) - 1
    SUITS:Tuple[str, ...] = ('clubs', 'diamonds', 'hearts', 'spades')

    def _invariant(self) -> bool:
        """Class invariant."""
        return self.MIN_VAL <= self._rank <= self.MAX_VAL \
            and self._suit in self.SUITS

    def __init__(self, rank:str, suit:str) -> None:
        """Construct a Card with a given SUIT and rank."""
        # Pre:
        assert rank in self.RANKS[self.MIN_VAL:self.MAX_VAL+1] \
            and suit in self.SUITS
        self._rank = self.RANKS.index(rank)
        self._suit = suit
        # Post:
        assert self._invariant()

    # Query methods
    def rank(self) -> str:
        return self.RANKS[self._rank]

    def suit(self) -> str:
        return self._suit

    def __str__(self) -> str:
        return self.rank() + ' of ' + self.suit()

    def __eq__(self, other:object) -> bool:
        same:bool = isinstance(other, Card)
        if same: # other is a Card
            othercard:Card = cast(Card, other)
            same = (self._rank == othercard._rank and 
                    self._suit == othercard._suit)
        return same
    
    def __lt__(self, other): # type: (Card) -> bool
        return self._rank < other._rank or \
            (self._rank == other._rank and self._suit < other._suit)

    @staticmethod
    def makeDeck(): # type () -> List[Card]:
        deck:List[Card] = []
        for suit in Card.SUITS:
            for rank in Card.RANKS[1:]:
                deck.append(Card(rank, suit))
        # Post:
        assert len(deck) == 52
        return deck