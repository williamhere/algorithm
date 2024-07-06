import time
import os


def apriori(transactions, min_support_count):

    #資料前處裡
    transactions = list(map(set, transactions))

    itemsets = {}
    for transaction in transactions:
        for item in transaction:
            item = tuple([item])
            if item in itemsets:
                itemsets[item] += 1
            else:
                itemsets[item] = 1

    num_transactions = len(transactions)
    frequent_itemsets = {}
    length = 1


    #演算法
    c=1
    while itemsets:
        print(f"執行演算法第",c,"次")
        frequent_itemsets[length] = {itemset: count for itemset, count in itemsets.items() if count >= min_support_count}
        if not frequent_itemsets[length]:
            break

        next_itemsets = {}
        items = list(frequent_itemsets[length].keys())
        for i, itemset1 in enumerate(items):
            for itemset2 in items[i+1:]:
                new_itemset = tuple(sorted(set(itemset1).union(itemset2)))
                if len(new_itemset) == length + 1:
 
                    if all(tuple(sorted(set(new_itemset) - {item})) in frequent_itemsets[length] for item in new_itemset):
                        support = sum(1 for transaction in transactions if set(new_itemset).issubset(transaction))
                        if support >= min_support_count:
                            next_itemsets[new_itemset] = support

        itemsets = next_itemsets
        length += 1
        c += 1
    return frequent_itemsets

def load_transactions(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split(',') for line in file]  
    return data

def main():
    file_path = 'test.txt'
    min_support = 0.5
    base_name = os.path.splitext(file_path)[0]
    
    #資料前處理
    transactions = load_transactions(file_path)
    num_transactions = len(transactions)
    min_support_count = int(min_support * num_transactions)
    print(num_transactions)

    #演算法
    frequent_itemsets = apriori(transactions, min_support_count)

    print("write")


    #輸出資料
    output_file = f'Group11_{base_name}_min_support={min_support}.txt'
    with open(output_file, 'w') as file:
       #file.write(f"min_support={min_support}:\n")
        file.write('Itemset\t\tSupport\n')
        for length in range(1, 10):
            itemsets = frequent_itemsets.get(length, {})
            for itemset, support in sorted(itemsets.items()):
                formatted_itemset = ', '.join(itemset)
                file.write(f'({formatted_itemset})\t{support}\n')
        file.write("\n")
    
    print("done")

if __name__ == "__main__":
    start_time = time.time()
    main()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"time : {elapsed_time:.6f} s")