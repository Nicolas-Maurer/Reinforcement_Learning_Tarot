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

During the deal, six cards are dealt face down to the centre of the table to form the talon or "the dog".
This means that in a 3-player game of tarot, each player has 24 cards in his hand when the deal is over.
 
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


# MCTS 

To predict the best card to play we will use the MCTS method, where each node will represent a potential card. The main difficulty lies in the fact that the Tarot is an imperfect information game, each player only know it's own cards, "the dog" and the history of played card (if they can remember it).




# Paranoid 
In the tarot game, instead of maximizing their own win rate, not-taker will try to minimize the win rate of the taker. This is the main hypothesis of the paranoid search policy.

Source: https://project.dke.maastrichtuniversity.nl/games/files/phd/Nijssen_thesis.pdf

"The child i with the highest value vᵢ is selected as follows :

![image](https://latex.codecogs.com/svg.latex?%5Cdpi%7B120%7D%20%5Clarge%20v_i%20%3D%20%281%20-%20%5Chat%7Bx_i%7D%29%20&plus;%20C%20%5Ctext%5Cspace%20%5Csqrt%20%5Cfrac%7Bln%28n_p%29%7D%7Bn_i%7D)

Similar to the UCT formula (Formula 2.8), x¯i denotes the win rate of node i. ni
and np denote the total number of times child i and its parent p have been visited,
respectively. C is a constant, which balances exploration and exploitation.

The major difference with the standard UCT formula is that, at the MIN nodes, x¯i
does not represent the win rate at child i of the current player, but of the root player.
Essentially, (1−x¯i) indicates the win rate of the coalition of the opponents. Analogous
to paranoid in the minimax framework, the opponents do not consider their own win
rate."

