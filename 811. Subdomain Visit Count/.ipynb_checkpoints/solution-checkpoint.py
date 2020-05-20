class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #just some string decomposation into list
        count_domains = [a.split(" ") for a in cpdomains]
        
        from collections import defaultdict
        res = defaultdict(int)
        
        for each in count_domains:
            count = int(each[0])
            domains = each[1].split(".")
            for i in range(len(domains)):
                res[".".join(domains[i:])]+=count
                
        ans = ["{} {}".format(count,domn) for domn,count in res.items()]
        return ans