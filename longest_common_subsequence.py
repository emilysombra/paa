'''
def dp_lcs(str1, str2):
    lengths = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i, x in enumerate(str1):
        for j, y in enumerate(str2):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    result = ''
    j = len(str2)
    for i in range(1, len(str1)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += str1[i-1]

    return result

if __name__ == '__main__':
    a = 'DBZJOIAQTXIOJVHAAFSM'
    b = 'BZHVRRVEOTDIQAXIYUTQTWGSXIOVUR'
    print(dp_lcs(a, b))
    print(len(dp_lcs(a, b)))
'''

# Dynamic Programming implementation of LCS problem 
  
def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 
#end of function lcs 
  
  
# Driver program to test the above function 
X = "DBZJOIAQTXIOJVHAAFSM"
Y = "BZHVRRVEOTDIQAXIYUTQTWGSXIOVUR"
print("Length of LCS is ", lcs(X, Y)) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)