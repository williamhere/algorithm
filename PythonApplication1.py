from apyori import apriori

# 讀取 data.txt 文件
file_path = 'data.txt'
with open(file_path, 'r') as file:
    transactions = [line.strip().split(',') for line in file.readlines()]

# 運行Apriori算法
results = list(apriori(transactions, min_support=0.05, min_confidence=0.2, min_lift=1.0, min_length=2))

# 保存结果的文件
with open("result1.txt", "w") as result_file:
    result_file.write("Frequent Itemsets with support count:\n")
    # 顯示结果
    print("Frequent Itemsets with support count:")
    for item in results:
        pair = item.items
        items = [x for x in pair]
        support_count = int(item.support * len(transactions))
        # 將结果寫入文件
        result_file.write(f"frozenset({items}): {support_count}\n")
        # 在控制台上顯示结果
        print(f"frozenset({items}): {support_count}")