# Apriori Algorithm Implementations
This repository contains implementations of the Apriori algorithm for mining frequent itemsets in a dataset. The implementations include using packages and without packages, with varying min_support values.

## Contents
1.With Packages: Implementation using packages with min_support = 0.05 on Data.txt.
2.Without Packages: Implementation without packages with min_support = 0.05 on Data.txt.
3.Music Dataset: Implementation without packages with varying min_support values on Music.txt.

## Apriori Algorithm Overview
The Apriori algorithm is an influential algorithm for mining frequent itemsets for Boolean association rules. Key steps include:
1.Initialization: Identify individual items meeting the minimum support threshold.
2.Generation: Generate candidate itemsets of size k-1
3.Pruning: Remove candidate itemsets that do not meet the minimum support threshold.
4.Iteration: Repeat the process until no more frequent itemsets are found.

## With Packages
Implementation: Utilizes libraries to simplify the process of identifying frequent itemsets.
Input: Data.txt
Parameters: min_support = 0.05

## Without Packages
Implementation: Manually processes data to identify frequent itemsets.
Input: Data.txt
Parameters: min_support = 0.05

## Music Dataset
Implementation: Similar to the above but applied to Music.txt with different min_support values.

https://github.com/LIN-SHU-FAN/Advanced-Topics-in-the-Design-and-Analysis-of-Algorithms-Assignment/tree/main?tab=readme-ov-file
