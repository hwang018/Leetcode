Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Idea:
Focus on finding the boundary, we only need to compare i-1 and i element.
When a reversal happens, note down the anchor point, thus obtaining the distance to the last anchor point.
Use another variable to store the maximum distances so far.