1450. Number of Students Doing Homework at a Given Time

Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

Idea:
Since at all positions i
startTime[i]<=endTimep[i]
for each of such time range, just to check if they contain the querytime
then loop once on 2 lists, to find the accumulated count.