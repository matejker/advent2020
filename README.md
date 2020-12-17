# Advent of Code 2020
My first attempt with AoC, my only ambition is to solve both problems everyday.
Furthermore, I picked up a few nice problems and their solutions and theory. 

## Day 11 - Game of "Seats"
The theme for [day 11 was the _Seating System_](https://adventofcode.com/2020/day/11) which was a nice adaptation of _Cellular Automata_ or it's most famous
variation - _the Game of Life_. (I am playing with some adaptations with GoL [here](https://github.com/matejker/game-of-life))

> Simulate your seating area by applying the seating rules repeatedly until no seats change state [1]

I rewrite it into JavaScript and visualise it. 
Here is a live demo for my puzzle: [Part 1](https://matejker.github.io/game-of-life/aoc.html), 
[Part 2](https://matejker.github.io/game-of-life/aoc.html)

## Day 13 - Chinese Reminder Theorem
Mathematically the most interesting problem was [day 13 - _Shuttle Search_](https://adventofcode.com/2020/day/13). 
The solution and idea leads into the _Chinese Reminder Theorem_.
Let `m_1,..,m_n` be a set of pairwise coprimes, for system of `n` equation:
```
x = a_1 (mod m_1)
  .
  .
  .
x = a_n (mod m_n)
```
then there exist unique solution for `x` modulo `M = m_1...m_n`. The solution is  
![](https://user-images.githubusercontent.com/45606539/102273203-e003a680-3f19-11eb-8f87-a881c0445c3d.png)  
where `b_i = M / m_i` and `b'_i = b_i^-1 (mod m_i)` [4, 5].

> the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at 
that subsequent minute. [1]

In the puzzle, all the bus IDs are (surprise-surprise) primes, therefore, we want to have:
```
x = - a_1 (mod busID_1) <=> x + a_i = 0 (mod busID_1)
  .
  .
  .
x = - a_n (mod busID_n) <=> x + a_i = 0 (mod busID_n)  
```
Therefore the search by sieving: 
```python
multiple = x = buslines[0][1]
for t, bus in buslines[1:]:
    while (x + t) % bus:
        x += multiple
    multiple *= bus
```
## Day 15 - Van Eck's sequence
[_Rambunctious Recitation_](https://adventofcode.com/2020/day/15) or a game with Elves was based on very nice sequence - _Van Eck's sequence_ or _Don't Know 
sequence_ [3].
> For n >= 1, if there exists an m < n such that a(m) = a(n),  
take the largest such m and set a(n+1) = n-m; otherwise a(n+1) = 0.  
Start with a(1)=0. [2]

Which creates a nice sequence of:
```
0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3, 0, 3, 2, 9, 0, 4, 9, 3, 6, 14...
```
One of the nice properties of this sequence is that `a(n) < n` (or even stronger `a(n) + a(n+1) < n` [2]), therefore the 
graph is below the identity `x = y`. However, the given AoC sequence has given different initial values, I tried to plot 
it and test it. Obviously, the `a(n) > n` for a first few `n` as (in my case) the sequence was defined `1, 2, 16, 19, 18, 0` 
but asymptotically it _should_ be bellow `n`.
![](https://user-images.githubusercontent.com/45606539/102198900-d9921200-3eba-11eb-8078-93d4c61ccb8e.png) 
Open questions:
 - What is the slope of the _Van Eck's sequence_ defined by `1, 2, 16, 19, 18, 0`? Is it different than the original one?

## References
[1] Eric Wastl (2020), _Advent of Code 2020_, https://adventofcode.com/2020  
[2] The OEIS Foundation (2010), _Van Eck's sequence_, https://oeis.org/A181391  
[3] Numberphile (2019), _Don't Know (the Van Eck Sequence)_, https://www.youtube.com/watch?v=etMJxB-igrc  
[4] Ben Lynn (?), _The Chinese Remainder Theorem_, https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
[5] Wikipedia (?), _The Chinese Remainder Theorem # Search by sieving_, https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    