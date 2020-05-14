'''
given a non-empty string s, may delete at most 1 character, 
judge if you can make it a palindrome.
naively using single loop to test removal each element will have timeexceed error
'''
def validPalindrome(s):
    #think it as an onion, at some layer there might be a non-symmetry element
    #use 2 pointers to track elements to compare
    left_p, right_p = 0, len(s)-1
    s_list = list(s)
    while left_p < right_p:
        #do compare 2 elements
        if s_list[left_p]==s_list[right_p]:
            left_p+=1
            right_p-=1
            #then moved to inner substring
        else:
            #found the non-symmetric place, can remove either place
            test1 = s_list[:left_p]+s_list[left_p+1:]
            test2 = s_list[:right_p]+s_list[right_p+1:]
            return test1[::-1]==test1 or test2[::-1]==test2
        
    return True
        
            