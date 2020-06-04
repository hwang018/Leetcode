There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Idea:
Greedy solution, 2N people in total, each person have 2 options, A or B, the larger the difference, the more "Worthy" to 
take the cheaper option. 
Therefore just to sort the difference, then arrange first half to one city, last half to another city to get optimal total cost.
