Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

Idea:
Use 2 pointers to track, i,j = 0,1 as starting indices
use while loop, while j <= max_ind 
do corner case of len=0, len=1
then for all other cases, len>=2, so we set i,j = 0,1 initially
then we just track each substring, if at end of each substring, let i = j
update power value as max(power,curr_count)