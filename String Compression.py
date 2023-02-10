class Solution:
  def compress(self, chars):
    output , i = 0, 0

    while i < len(chars):
      charachter = chars[i]
      tally = 0
      while i < len(chars) and chars[i] == charachter:
        tally += 1
        i += 1
      chars[output] = charachter
      output += 1
      if tally > 1:
        for c in str(tally):
          chars[output] = c
          output += 1

    return output