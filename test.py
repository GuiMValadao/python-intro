class Solution:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2       
    
    def sum(self ) -> int:
        #print(num1 + num2)

        return self.num1 + self.num2



#num1 = int(input())
#num2 = int(input())
sol = Solution(int(input()), int(input())).sum()
print(sol)