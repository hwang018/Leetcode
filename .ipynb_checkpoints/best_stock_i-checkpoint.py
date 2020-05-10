def maxProfit(prices):
    '''
    calculate the max profit, given stock tick points
    by finding lowest and highest ticks
    single pass solution
    '''
    n = len(prices)
    if n < 2:
        return 0
    #create maxprofit, minstock
    maxprofit,minstock = float('-inf'),prices[0]
    for p in prices:
        maxprofit = max(maxprofit,p-minstock)
        minstock = min(minstock,p)
    return maxprofit