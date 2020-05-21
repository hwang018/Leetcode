class Solution:
    def freqAlphabets(self, s: str) -> str:
        #each time encounter #, means the 3 positions are reserved
        #so first is to identify positions of #
        s_list = list(s)
        ind_hash = []

        keys1 = ['1','2','3','4','5','6','7','8','9']
        vals1 = ['a','b','c','d','e','f','g','h','i']
        part1_dict = dict(zip(keys1,vals1))

        keys2 = ['10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
        vals2 = ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']        
        part2_dict = dict(zip(keys2,vals2))
        
        
        invalid = []
        
        key_positions = {}
        
        for i,each in enumerate(s_list):
            if each == '#':
                #there should be 2 elements before # to be reserved
                val = s_list[i-2]+s_list[i-1]
                translated = part2_dict[val]
                
                key_positions[i]=translated
                
                invalid.extend([i-2,i-1,i])
            
        res = []
        
        for i,each in enumerate(s_list):
            if i not in invalid:
                translated = part1_dict[each]
                res.append(translated)
            elif i in key_positions.keys():
                res.append(key_positions[i])
            else:
                continue
        return ''.join(res)