class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1,n+1):
            if i % 15 == 0: answer += ["FizzBuzz"]
            elif i % 5 == 0: answer += ["Buzz"]
            elif i % 3 == 0: answer += ["Fizz"]
            else: answer += [str(i)]
        return answer
