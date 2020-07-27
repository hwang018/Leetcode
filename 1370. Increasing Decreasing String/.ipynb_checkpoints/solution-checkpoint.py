class Solution:
    def sortString(self, s: str) -> str:
        res = []
        s_list = list(s)
        
        i=0
        while len(s_list) > 0:
            if i%2==0:
                temp = list(set(s_list))
                temp.sort()
                res+=temp
                for v in temp:
                    s_list.remove(v)
                i+=1
            else:
                temp = list(set(s_list))
                temp.sort(reverse=True)
                res+=temp
                for v in temp:
                    s_list.remove(v)
                i+=1
        return "".join(res)