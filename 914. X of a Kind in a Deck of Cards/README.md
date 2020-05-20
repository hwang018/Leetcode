In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.

Idea:
Just use Counter to find the frequencies of items and reduce the frequencies to find their gcd.
Greatest common divisor. If this gcd is >= 2, means that the frequencies can be grouped into basic lists of size of gcd.