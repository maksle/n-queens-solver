# n-Queens solver

Based on algorithms in the book `Artificial Intelligence: A Modern Approach, 3rd edition` by Stuart Russell and Peter Norvig.

The solver uses the *local beam search* algorithm, which is an adaptation of another algorithm called beam search. It starts off with some randomly generated states and does greedy stochastic hill climbing search on each one. If one of them finds a solution, that's returned. Otherwise, the k best results are used for the next search. This algorithm requires parallel searches, so the solver utilizes multiprocessing.

The solution for an 8x8 board is instantaneous, but it took a few minutes on 4 cores to find a solution for 128x128. Supposedly, this algorithm has been used to solve the millions queens problem in under 2 seconds, but it was probably a more optimized solution, and written in a language like C++.

## Example
```
n_queens import search

local_beam_search(8)
>>> [(0, 5), (1, 3), (2, 6), (3, 0), (4, 2), (5, 4), (6, 1), (7, 7)]
 -  -  -  -  -  Q  -  - 

 -  -  -  Q  -  -  -  - 

 -  -  -  -  -  -  Q  - 

 Q  -  -  -  -  -  -  - 

 -  -  Q  -  -  -  -  - 

 -  -  -  -  Q  -  -  - 

 -  Q  -  -  -  -  -  - 

 -  -  -  -  -  -  -  Q
```
