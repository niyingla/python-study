class CombinationSum:

    def __init__(self):
        self.results = []

    """ 组合总和 
    amountList: 金额列表
    targetSum: 目标金额
    n: 组合长度
    """

    def findCombinations(self, amountList, targetSum, n):
        amountList.sort()
        self.backtrack(amountList, [], 0, 0, n, targetSum)

    """ 
    计算组合
    array: 金额列表
    combination: 当前组合
    start: 开始索引
    currentSum: 当前总和
    n: 组合长度
    targetSum: 目标总和
    """

    def backtrack(self, amountList, combination, start, currentSum, n, targetSum):
        # 判断是否满足条件
        if currentSum >= targetSum and len(combination) == n:
            self.results.append(combination[:])
            return
        # 判断是否超出范围
        for i in range(start, len(amountList)):
            combination.append(amountList[i])
            self.backtrack(amountList, combination, i + 1, currentSum + amountList[i], n, targetSum)
            combination.pop()

    def getResults(self):
        return self.results


if __name__ == '__main__':
    lastResults = []
    # array = [120,148,136,33,188, 68, 62, 168, 61, 191, 146]
    # 按键输入
    print("请输入金额数组，用逗号隔开:")
    try:
        amountList = list(map(int, input().split(",")))
    except:
        print("请输入正确的数组格式")
        input("Press any key to exit")
        exit(0)
    print("请输入目标金额:")
    # 按键输入
    targetSum = int(input())
    # targetSum = 560
    # 循环array的长度次
    for i in range(1, len(amountList)+1):
        cs = CombinationSum()
        cs.findCombinations(amountList, targetSum, i)
        if len(cs.getResults()) > 0:
            for result in cs.getResults():
                lastResults.append(result)

    # 判断是否为空
    if len(lastResults) == 0:
        print("没有符合条件的组合")
        input("Press any key to exit")
        exit(0)

    # 对sortResults 进行排序 排序规则就是每个元素求和的最小值
    lastResults.sort(key=lambda x: sum(x), reverse=False)
    print(f"最小的组合是: {lastResults[0]},总和是：{sum(lastResults[0])}")
    # 输入任意键
    input("Press any key to exit")
