class Solution:
    def isAnagram(self, s, t) :
        if len(s) != len(t) :
            return False
        CountS, CountT = {}, {}
        for i in range(len(s)) :
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
        for c in CountS :
            if CountS[c] != CountT.get(c, 0) :
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        n = len(strs)
        used = [False] * n
        for i in range(n):
            if used[i] :
                continue
            used[i] = True
            rows = []
            rows.append(strs[i])
            for j in range(i+1, n) :
                if not used[j] and self.isAnagram(strs[i], strs[j]) :
                    rows.append(strs[j])
                    used[j] = True
            result.append(rows)
        return result