import random
# 引数の回数100面ダイスを振る
def roll_dice(times):
    if not (1 <= times <= 10):
        raise ValueError("ダイスを振る回数は1以上10以下で指定してください。")
    
    total = 0
    for i in range(1, times + 1):
        roll = random.randint(1, 100)
        print(f"{i}個目：{roll}")
        total += roll
    
    print(f"\n合計：{total}")
    return total

# テスト用コード
def main():
    print("\n100面ダイスを振るテスト:")
    result=roll_dice(3)  # 例として3回振る
    print(f"テスト結果: {result}")
if __name__ == "__main__":
    main()

