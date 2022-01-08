# Reinforcement_Learning_Tarot
This repository is dedicated to the application of MCTS - paranoid method to the 3-player tarot game.
Tarot is often called as French Tarot, it's a card game with imperfect information. It can be played from 3 to 5 player but for this application, we will only focus on the 3-player version. 

![download](https://user-images.githubusercontent.com/62259863/148639464-330682c1-ae5c-44b7-9346-57d7f0f7fd40.jpg) 

# Tarot presentation. 
## Deck 

The deck consists of 78 cards. The four suits are the standard ones of diamonds, hearts, spades and clubs, and each suit contains fourteen cards ranking from high to low:
King, Queen, Knight, Jack, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1.

In addition to the four standard suits there is a extra suit of twenty-one trumps numbered from 21 (high) to 1 (low).
Finally, there is a special card called the excuse, or the fool, marked with a star in the corner.

Three cards, the 1 of trump (called the petit), the 21 of trump and the excuse are particularly important in the game and are known as bouts ("ends") or sometimes in books as oudlers.
Not only are the bouts worth points, but having them in your tricks also reduces the total number of points you need to win.

## Values of the cards
In each hand one player, the taker plays alone against the other two in partnership. The taker's objective is to accumulate enough card points to win the hand by taking tricks.

For every card in every trick taken, you get the following card points:
- Bouts (21, 1, excuse):	4.5 points each
- Kings:	4.5 points each
- Queens:	3.5 points each
- Knights:	2.5 points each
- Jacks:	1.5 points each
- Other cards:	0.5 points each

The number of points the taker needs to win depends on the number of bouts the taker has in his tricks:
- With 3 bouts the taker needs at least 36 card points to win.
- With 2 bouts the taker needs at least 41 card points to win.
- With 1 bout the taker needs at least 51 card points to win.
 -With 0 bouts the taker needs at least 56 card points to win.

## The plays of the cards / The rules 

Each player is obliged to follow the requested suit, if he can't then he has to play trump, if he can't either, then he plays another card. 
Moreover, when you have to play a trump, you must if possible, play a higher trump than the highest trump played so far for this trick. If you can't, you must still play a trump.  

Each trick is won by the highest trump, if the trick does not contain a trump then it is won by the highest card of the requested suit. 
The player who wins the trick starts the next one.

The only exception is the excuse, it can be played any time, but it never wins the trick 

More rules about the Tarot: https://www.pagat.com/tarot/frtarot.html#introduction


# MCTS - Paranoid 
Search Policies for Multi-Player MCTS

In the tarot game, instead of maximizing their own win rate, not-taker will try to minimize the win rate of the taker. This is the main hypothesis of the paranoid search policy.


# Sources : 
- https://project.dke.maastrichtuniversity.nl/games/files/phd/Nijssen_thesis.pdf
