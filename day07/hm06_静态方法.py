# 需求： 1. 设计一个 Game 类
# 2. 属性: • 定义一个 top_score 类属性 -> 记录游戏的历史最高分
# • 定义一个 player_name 实例属性 -> 记录当前游戏的玩家姓名
# 3. 方法: • 静态方法 show_help() -> 显示游戏帮助信息
# • 类方法 show_top_score() -> 显示历史最高分
# • 实例方法 start_game() -> 开始当前玩家的游戏
# 4. 主程序步骤:
# ① 查看帮助信息
# ② 查看历史最高分
# ③ 创建游戏对象，开始游戏
# 定义类
class Game(object):
    """游戏类"""
    # 类属性
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        """静态方法,显示帮助信息"""
        print('请点击游戏开始,进行下一步...')

    @classmethod
    def show_top_score(cls):
        """类方法"""
        print(f'显示历史最高:{cls.top_score}')

    def start_game(self):
        """实例方法"""
        print('开始游戏')
        Game.top_score = 999
        print('结束游戏')


if __name__ == '__main__':  # 程序步骤
    Game.show_help()  # 调静态方法
    Game.show_top_score()  # 调用类方法
    game1 = Game('小明')  # 创建对象
    game1.start_game()  # 调用玩游戏方法
    Game.show_top_score()  # 玩家玩完之后的分数
