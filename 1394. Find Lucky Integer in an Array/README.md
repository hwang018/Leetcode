Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

Idea: using Counter we can easily get frequency dictionary of a list.
Then loop through each item in list, check if value == frequency. Store all satisfactory items in a list. 