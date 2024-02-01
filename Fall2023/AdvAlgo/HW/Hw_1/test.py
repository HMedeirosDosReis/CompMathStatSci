class Palindrome:
    def __init__(self):
        self.strPalindrome = ""
        self.strFront = "" 
        self.strEnd = ""
        
def findLongestPalindrome(strInput):
    vecVecIntermediate = [[Palindrome() for _ in range(len(strInput) + 1)] for _ in range(len(strInput))]
    
    for i in range(len(strInput)):
        vecVecIntermediate[i][1].strPalindrome = strInput[i]
        vecVecIntermediate[i][1].strFront = ""
        vecVecIntermediate[i][1].strEnd = ""
        
    for i in range(len(strInput) - 1):
        if strInput[i] == strInput[i+1]:
            vecVecIntermediate[i][2].strPalindrome = strInput[i:i+2] 
            vecVecIntermediate[i][2].strFront = ""
            vecVecIntermediate[i][2].strEnd = ""
        else:
            vecVecIntermediate[i][2].strPalindrome = strInput[i]
            vecVecIntermediate[i][2].strEnd = strInput[i+1]
    
    for L in range(3, len(strInput) + 1):
        for n in range(len(strInput) - L + 1):
            findPos = 0
            p2 = vecVecIntermediate[n][L-1]
            p2.strEnd += strInput[n + L - 1]
            
            findPos = p2.strFront.find(p2.strEnd)
            if findPos != -1:
                charFind = p2.strFront[findPos]
                p2.strPalindrome = charFind + p2.strPalindrome + charFind 
                p2.strFront = p2.strFront[:findPos]
                
                findPos = p2.strEnd.find(charFind)
                p2.strEnd = p2.strEnd[findPos + 1:]
                
            p3 = vecVecIntermediate[n+1][L-1]
            p3.strFront = strInput[n] + p3.strFront
            
            findPos = p3.strFront.find(p3.strEnd)
            if findPos != -1:
                charFind = p3.strFront[findPos]
                p3.strPalindrome = charFind + p3.strPalindrome + charFind
                p3.strFront = p3.strFront[:findPos]
                
                findPos = p3.strEnd.find(charFind)
                p3.strEnd = p3.strEnd[findPos + 1:]
                
            vecP = [p2, p3]
            nMaxIndex = 0
            for index in range(1, len(vecP)):
                if len(vecP[index].strPalindrome) > len(vecP[nMaxIndex].strPalindrome):
                    nMaxIndex = index
                    
            vecVecIntermediate[n][L] = vecP[nMaxIndex]
    
    return vecVecIntermediate[0][len(strInput)].strPalindrome

def test_findLongestPalindrome():
    test_cases = ["a", "aa", "ab", "abbac", "abcdefghijkjhgfed", "character", "GEEKS FOR GEEKS"]
    
    for strTestCase in test_cases:
        strPalindrome = findLongestPalindrome(strTestCase)
        print(f"Test case {strTestCase}, result {strPalindrome}")
        
test = [[11,12,13],[21,22,23],[31,32,33]]
print(test[0][1])
print(test[1][1])
print(test[2][1])
s="abca"
print(s[3])
for i in range(len(s)-1):
    print(i)
