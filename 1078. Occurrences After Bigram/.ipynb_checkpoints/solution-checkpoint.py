class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        #maintain a window to search
        word_list = text.split(' ')
        max_ind = len(word_list)-1
        curr = 0
        res = []
        while curr+2<=max_ind:
            if word_list[curr] == first:
                if word_list[curr+1] == second:
                    if word_list[curr+2]:
                        res.append(word_list[curr+2])
            curr+=1
        return res