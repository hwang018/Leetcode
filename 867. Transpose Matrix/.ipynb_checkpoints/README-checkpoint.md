Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Idea:
To do a matrix transpose without numpy, givn a list of list,
the transpose is to take j in cols: each j position or the row vector
Thus to loop all sublist in A, each time creating another vector.