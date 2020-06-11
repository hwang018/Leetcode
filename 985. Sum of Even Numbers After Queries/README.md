We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

 
Idea:
Naive implementation line by line will have time error. 
We maintain the current sum of even values, only modify it according to even/odd scenarios.
First store S as sum of all even vals from A.
Then check each query value, val+A[ind] will have 4 combinations in total, deal with each case and modify S.
