class Solution(object):
    def sortSentence(self, s):
  

        split = s.split(" ")
        original_sen = ""
        
        for x in range(0,len(split)):
            
            idx = x
            
            for y in range(x+1,len(split)):
            
                if split[y][-1] < split[idx][-1]:
                    idx = y
            
            if x != idx:
                split[idx], split[x] = split[x], split[idx]
            
            original_sen += split[x][:-1] + ' '
        
        return (original_sen[:-1])
