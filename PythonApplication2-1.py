from collections import defaultdict
from itertools import combinations
import itertools

# 辅助函数：计算支持度
def count_support(transactions, itemset):
    count = 0
    for transaction in transactions:
        if itemset.issubset(transaction):
            count += 1
    return count

# 辅助函数：生成候选项集
def generate_candidates(frequent_itemsets, length):
    candidates = set()
    frequent_list = list(frequent_itemsets)
    for i in range(len(frequent_list)):
        for j in range(i + 1, len(frequent_list)):
            candidate = frequent_list[i] | frequent_list[j]
            if len(candidate) == length:
                candidates.add(candidate)
    return candidates

if __name__ == "__main__":
    # 加载数据
    transactions = []
    with open("data.txt", "r") as file:
   #with open("Music.txt", "r") as file: 
        for line in file:
            transaction = frozenset(map(int, line.strip().split(',')))
            transactions.append(transaction)

    min_support = 0.05  # 设置支持度阈值
   #min_support = 0.0003  # 设置较高的支持度阈值
   #min_support = 0.0006  # 设置较高的支持度阈值
   #min_support = 0.0009  # 设置较高的支持度阈值 
    min_support_count = int(min_support * len(transactions))

    # 初始项集
    itemset_support_count = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            itemset_support_count[frozenset([item])] += 1

    frequent_itemsets = {itemset for itemset, support in itemset_support_count.items() if support >= min_support_count}

    # 保存结果的文件
    with open("Group11_Data_min_support=0.05.txt", "w") as result_file:
        # Apriori算法主循环
        k = 2
        while frequent_itemsets:
            # 写入当前的频繁项集和其支持度到文件
            result_file.write("Frequent Itemsets with support count:\n")
            for itemset in frequent_itemsets:
                result_file.write(f"{itemset}: {itemset_support_count[itemset]}\n")

            # 显示当前的频繁项集和其支持度到控制台
            print("Frequent Itemsets with support count:")
            for itemset in frequent_itemsets:
                print(f"{itemset}: {itemset_support_count[itemset]}")

            # 生成候选项集
            candidates = generate_candidates(frequent_itemsets, k)
            if not candidates:
                break

            # 计算候选项集的支持度
            candidate_support_count = defaultdict(int)
            for candidate in candidates:
                candidate_support_count[candidate] = count_support(transactions, candidate)

            # 更新频繁项集
            frequent_itemsets = {candidate for candidate, support in candidate_support_count.items() if support >= min_support_count}
            itemset_support_count.update(candidate_support_count)
            k += 1