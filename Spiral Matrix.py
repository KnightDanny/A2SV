class Solution:
  def spiralOrder(self, matrix):
    if not matrix:
      return []

    m , n, output = len(matrix), len(matrix[0]),[] 
    a1 , b1, a2 , b2 = 0, 0 , m - 1 , n - 1 
   
    while len(output) < m * n:
      j = b1
      while j <= b2 and len(output) < m * n:
        output.append(matrix[a1][j])
        j += 1
      i = a1 + 1
      while i <= a2 - 1 and len(output) < m * n:
        output.append(matrix[i][b2])
        i += 1
      j = b2
      while j >= b1 and len(output) < m * n:
        output.append(matrix[a2][j])
        j -= 1
      i = a2 - 1
      while i >= a1 + 1 and len(output) < m * n:
        output.append(matrix[i][b1])
        i -= 1
      a1 += 1
      b1 += 1
      a2 -= 1
      b2 -= 1

    return output