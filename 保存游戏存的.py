import os

# 保存数据的文件
save_file = "game_save.txt"

# 保存数据到文本文件
def save_game(health, score):
    with open(save_file, "w") as file:
        file.write(f"{health}\n{score}\n")
    print("游戏已保存！")

# 从文本文件
def load_game():
    if os.path.exists(save_file):
        with open(save_file, "r") as file:
            lines = file.readlines()
            health = int(lines[0].strip())
            score = int(lines[1].strip())
        print(f"游戏已加载！ 生命值: {health}, 分数: {score}")
        return health, score
    else:
        print("未找到已保存的游戏，开始新游戏。")
        return 100, 0  # 默认生命值和分数

# 游戏
def play_game():
    health, score = load_game()

    while True:
        print("\n--- 主菜单 ---")
        print("1. 开始游戏")
        print("2. 保存游戏") 
        choice = input("请选择一个选项: ")

        if choice == "1":
            print("游戏中...")
            health -= 10
            score += 20
            print(f"生命值: {health}, 当前分数: {score}")
            if health <= 0:
                print("你死了,游戏结束！")
                health, score = 100, 0 