if __name__ == '__main__':
    print("原始文本，输入end后结束")
    current = input()
    total_text = ""
    while current != "end":
        current = current.replace("\n","")
        total_text =  total_text + current
        current = input()

    print("\n")
    print("---------------------------------------以下是处理后结果--------------------------------------------")
    print("\n")
    print(total_text)
    current = input()

