class Solution:
	def fibonacci(self, n):
		if n==0 or n==1:
			return 1
		else:
			return self.fibonacci(n-1)+ self.fibonacci(n-2)
print(Solution().fibonacci(10))