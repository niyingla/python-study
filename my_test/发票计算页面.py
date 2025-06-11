import tkinter as tk  # 导入 Tkinter 库

def add_amount():  # 定义添加金额的函数
    try:
        user_input = entry.get()  # 获取输入框中的文本
        amount = int(user_input)  # 将输入的文本转换为浮动数字
        amounts.append(amount)  # 将金额添加到金额列表中
        amounts_label.config(text="当前金额列表: " + ", ".join(map(str, amounts)))  # 更新显示金额列表的标签
        entry.delete(0, tk.END)  # 清空输入框

    except ValueError:  # 如果输入无效（非数字），输出错误信息
        print("请输入有效的金额！")

def calculate_total():  # 定义计算总金额的函数
    user_input = entry.get()  # 获取输入框中的文本
    entry.delete(0, tk.END)  # 清空输入框
    #判断没输入内容
    if not user_input:
            total_label.config(text="请输入总金额")  # 更新显示总金额的标签
            return
    results.clear()
    total_amount = int(user_input)  # 将输入的文本转换为浮动数字
    comp = min_comp(amounts, total_amount)
    total_label.config(text=comp)  # 更新显示总金额的标签

    """ 组合总和
       amountList: 金额列表
       targetSum: 目标金额
       n: 组合长度
       """

def find_combinations(amount_list, target_sum, n):
    amount_list.sort()
    backtrack(amount_list, [], 0, 0, n, target_sum)

"""
计算组合
array: 金额列表
combination: 当前组合
start: 开始索引
currentSum: 当前总和
n: 组合长度
targetSum: 目标总和
"""

def backtrack(amount_list, combination, start, current_sum, n, target_sum):
    # 判断是否满足条件
    if current_sum >= target_sum and len(combination) == n:
        results.append(combination[:])
        return
    # 判断是否超出范围
    for i in range(start, len(amount_list)):
        combination.append(amount_list[i])
        backtrack(amount_list, combination, i + 1, current_sum + amount_list[i], n, target_sum)
        combination.pop()



def min_comp(input_list, total):
    last_results = []
    # 循环array的长度次
    for i in range(1, len(input_list) + 1):
        find_combinations(amounts, total, i)
        if len(results) > 0:
            for result in results:
                last_results.append(result)
    # 判断是否为空
    if len(last_results) == 0:
        return "没有符合条件的组合"
    # 对sortResults 进行排序 排序规则就是每个元素求和的最小值
    last_results.sort(key=lambda x: sum(x), reverse=False)
    return f"最小的组合是: {last_results[0]},总和是：{sum(last_results[0])}"


root = tk.Tk()  # 创建主窗口对象
root.title("发票最小组合计算")  # 设置窗口标题
root.geometry("888x666")  # 设置窗口大小为 555x888

entry = tk.Entry(root, font=('Helvetica', 14))  # 创建一个输入框，设置字体
entry.pack(pady=10)  # 将输入框添加到窗口，并设置上下间距

amounts = []  # 初始化金额列表
results = []

add_button = tk.Button(root, text="添加金额", command=add_amount, font=('Helvetica', 14))  # 创建添加金额按钮
add_button.pack(side=tk.LEFT, padx=60)  # 将按钮添加到窗口，并设置上下间距

calculate_button = tk.Button(root, text="计算金额", command=calculate_total, font=('Helvetica', 14))  # 创建计算金额按钮
calculate_button.pack(side=tk.RIGHT, padx=60)  # 将按钮添加到窗口，并设置上下间距

amounts_label = tk.Label(root, text="金额列表: ", font=('Helvetica', 12), anchor='w', justify='left', height=10)  # 创建显示金额列表的标签
amounts_label.pack(padx=10,pady=20,  fill=tk.X)  # 将金额列表标签添加到窗口，并设置间距和填充方式

#entry键也触发 add_amount按钮
entry.bind("<Return>", lambda event: add_amount())  # 绑定回车键触发 add_amount 函数

total_label = tk.Label(root, text="总金额: 0", font=('Helvetica', 16), height=20)  # 创建显示总金额的标签
#指定显示框大小 显示大一点
total_label.pack(pady=15, padx=10, fill=tk.X)
#total_label.pack(pady=20, padx=15, fill=tk.X) # 将总金额标签添加到窗口，并设置上下间距


root.mainloop()  # 启动 Tkinter 事件循环