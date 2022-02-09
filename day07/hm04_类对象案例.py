class Student(object):
    """学生类"""
    """定义类属性"""
    num = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        """创建对象自动递增"""
        Student.num += 1

    @classmethod
    def show_num(cls):
        """类方法,学生数量"""
        print(f'班级总人数为:{cls.num}')

    def __str__(self):
        """自定义打印对象信息"""
        return f"学生姓名:{self.name},考试分数:{self.score}"


# 创建对象
# 查看班级总人数
Student.show_num()
xs1 = Student('张三', 59)
xs2 = Student('李四', 88)
xs3 = Student('王五', 98)
# 调用对象
print(xs1)
print(xs2)
print(xs3)
# 查看总人数
Student.show_num()
