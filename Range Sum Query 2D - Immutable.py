class NumMatrix:
  def __init__(self, matrix):
    if not matrix:
      return
    x, y,  = len(matrix), len(matrix[0])
    self.prefix = [[0] * (y + 1) for _ in range(x + 1)]
    for i in range(x):
      for j in range(y):
        self.prefix[i + 1][j + 1] = \
            matrix[i][j] + self.prefix[i][j + 1] + \
            self.prefix[i + 1][j] - self.prefix[i][j]
  def sumRegion(self, row1, col1, row2, col2):
    return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - \
        self.prefix[row2 + 1][col1] + self.prefix[row1][col1]