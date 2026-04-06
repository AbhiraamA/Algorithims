# Algorithms Reference

One algorithm per file, organized by data structure / category.
Every file is self-contained with complexity notes and a runnable `__main__` block.

```
algorithms/
│
├── array_sorting/
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── heap_sort.py
│   ├── counting_sort.py
│   ├── radix_sort.py
│   └── shell_sort.py
│
├── array_searching/
│   ├── linear_search.py
│   ├── binary_search.py          # iterative, recursive, first/last occurrence
│   ├── jump_search.py
│   ├── interpolation_search.py
│   └── exponential_search.py
│
├── linked_list/
│   ├── reverse.py
│   ├── detect_cycle.py           # Floyd's tortoise & hare
│   ├── find_middle.py
│   ├── merge_sorted_lists.py
│   ├── remove_nth_from_end.py
│   ├── is_palindrome.py
│   └── add_two_numbers.py
│
├── trees/
│   ├── _tree_node.py             # shared TreeNode class + builder
│   ├── inorder_traversal.py
│   ├── preorder_traversal.py
│   ├── postorder_traversal.py
│   ├── level_order_traversal.py
│   ├── height.py
│   ├── is_balanced.py
│   ├── is_valid_bst.py
│   ├── lowest_common_ancestor.py
│   ├── diameter.py
│   ├── max_path_sum.py
│   ├── bst_insert.py
│   └── bst_delete.py
│
├── graphs/
│   ├── bfs.py                    # + shortest path reconstruction
│   ├── dfs.py                    # iterative + recursive
│   ├── dijkstra.py               # + path reconstruction
│   ├── bellman_ford.py           # handles negative weights + cycle detection
│   ├── topological_sort.py       # Kahn's BFS + DFS variant
│   ├── union_find.py             # path compression + union by rank
│   ├── number_of_islands.py
│   └── detect_cycle.py
│
├── heaps/
│   ├── min_heap.py
│   ├── max_heap.py
│   ├── kth_largest.py
│   ├── merge_k_sorted.py
│   └── median_from_stream.py
│
├── strings/
│   ├── kmp_search.py
│   ├── rabin_karp.py
│   ├── longest_common_subsequence.py
│   ├── longest_palindromic_substring.py
│   ├── minimum_window_substring.py
│   ├── find_all_anagrams.py
│   └── edit_distance.py
│
└── dynamic_programming/
    ├── fibonacci.py
    ├── knapsack.py
    ├── coin_change.py
    ├── longest_increasing_subsequence.py
    ├── maximum_subarray.py           # Kadane's algorithm
    ├── house_robber.py               # + circular variant
    ├── unique_paths.py               # + with obstacles
    ├── word_break.py                 # + all segmentations
    ├── partition_equal_subset.py
    └── matrix_chain_multiplication.py
```

## Running any file

```bash
python array_sorting/merge_sort.py
python graphs/dijkstra.py
python dynamic_programming/knapsack.py
# etc.
```

## Complexity Quick-Reference

| Algorithm                | Time Avg     | Space    |
|--------------------------|--------------|----------|
| Bubble / Selection Sort  | O(n²)        | O(1)     |
| Insertion Sort           | O(n²)        | O(1)     |
| Merge Sort               | O(n log n)   | O(n)     |
| Quick Sort               | O(n log n)   | O(log n) |
| Heap Sort                | O(n log n)   | O(1)     |
| Counting / Radix Sort    | O(n + k)     | O(k)     |
| Binary Search            | O(log n)     | O(1)     |
| BFS / DFS                | O(V + E)     | O(V)     |
| Dijkstra                 | O((V+E)logV) | O(V)     |
| Bellman-Ford             | O(V * E)     | O(V)     |
| Union-Find (amortized)   | O(α(n))      | O(n)     |
| KMP                      | O(n + m)     | O(m)     |
| LIS (patience sort)      | O(n log n)   | O(n)     |
| Knapsack                 | O(n * W)     | O(W)     |
| Kadane's (max subarray)  | O(n)         | O(1)     |
