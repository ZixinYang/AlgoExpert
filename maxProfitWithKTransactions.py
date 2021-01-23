def solution(prices, k):
    # Write your code here.
	if not prices: return 0
	if len(prices)==2 and k==1: return max(0, prices[-1]-prices[0])
	profits = [[0 for i in range(len(prices))] for j in range(k+1)]
	for i in range(1, k+1):
		MAX = float("-inf")
		for j in range(1, len(prices)):
			MAX = max(-prices[j-1]+profits[i-1][j-1], MAX)
			profits[i][j] = max(profits[i][j-1], prices[j] + MAX)
	return profits[-1][-1]
