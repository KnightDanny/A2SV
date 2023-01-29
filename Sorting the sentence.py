class Solution(object):
    def sortSentence(self, s):
  

        split = s.split(" ")
        original_sen = ""
        
        for x in range(0,len(split)):
            
            idx = x
            
            for y in range(x+1,len(split)):
            
                if split[y][-1] < split[idx][-1]:
                    idx = j
            
            if i != idx:
                split[idx], split[x] = split[x], split[idx]
            
            original_sen += split[i][:-1] + ' '
        
        return (original_sen[:-1])