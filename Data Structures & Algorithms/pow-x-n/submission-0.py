class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        half = self.myPow(x, abs(n)//2)

        if n % 2:
            res = half * half * x
        else:
            res = half * half
        
        return res if n>0 else 1/res