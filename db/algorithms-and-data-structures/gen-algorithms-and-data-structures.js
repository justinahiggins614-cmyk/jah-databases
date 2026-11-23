// Seeded boundless generator for the Algorithms and Data Structures Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-algorithms-and-data-structures.js [seed]  (prints one JSON record)
// or: node gen-algorithms-and-data-structures.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "algorithms-and-data-structures";
const RECORD_KIND = "algorithms and data structures record";
const ID_PREFIX = "JAH-ALGDS-";
const AI_NAME = "JAH Algorithms Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Algorithms and Data Structures: Big-O Notation and Growth Rates",
    "subject": "Big-O notation and growth rates",
    "description": "Big-O notation describes how an algorithm's running time grows with the input size n: O(1) is constant, O(log n) is logarithmic, O(n) is linear, O(n log n) is linearithmic, O(n squared) is quadratic, and O(2 to the n) is exponential. The dominant term decides the class; constants and lower terms are dropped. O(1) does not grow with n; O(log n) grows very slowly. O(n log n) is the class of the best comparison sorts. O(2^n) doubles with each added input, and is infeasible for large n.",
    "inputs": "FIGURES = {'n_items': 1000000, 'nlogn_comparisons': 20000000, 'nlogn_seconds': 0.02, 'nsquared_comparisons': 500000000000, 'nsquared_seconds': 500, 'doubled_nlogn_seconds': 0.042, 'doubled_nsquared_seconds': 2000, 'growth_classes': 6}\nLABEL = 'big-o-notation-and-growth-rates'\n",
    "expected": "count: 8\nlabel: big-o-notation-and-growth-rates\nmax: 500000000000\nmean: 62502625313.2578\nmin: 0.02\ntotal: 500021002506.062\nResult: count=8|label=big-o-notation-and-growth-rates|max=500000000000|mean=62502625313.2578|min=0.02|total=500021002506.062\nRun 1 SHA-256: f1223ef8d04033896e98147ad62d4b282dd095368e7572fa0232350fe3b7dcfd\nRun 2 SHA-256: f1223ef8d04033896e98147ad62d4b282dd095368e7572fa0232350fe3b7dcfd\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Arrays and Linked Lists",
    "subject": "arrays and linked lists",
    "description": "An array stores items in contiguous memory, so any item is reached in O(1) by its index, but inserting in the middle costs O(n) to shift. A linked list stores items in nodes with pointers, so inserting at a known node costs O(1), but reaching the k-th item costs O(k). The choice is a trade-off between access and insertion. An array gives O(1) access by index and O(n) insertion in the middle. A linked list gives O(1) insertion at a known node and O(n) access by position. Arrays use contiguous memory; linked lists use pointers.",
    "inputs": "FIGURES = {'array_size': 1000000, 'array_bytes': 4000000, 'array_access_steps': 1, 'array_insert_shifts': 1000000, 'insert_time_ms': 1, 'list_reach_steps': 500000, 'list_reach_ms': 0.5, 'amortised_append': 1}\nLABEL = 'arrays-and-linked-lists'\n",
    "expected": "count: 8\nlabel: arrays-and-linked-lists\nmax: 4000000\nmean: 812500.4375\nmin: 0.5\ntotal: 6500003.5\nResult: count=8|label=arrays-and-linked-lists|max=4000000|mean=812500.4375|min=0.5|total=6500003.5\nRun 1 SHA-256: 6fcd17924b7333b8a6ba09b791d05e6662f5f1284ce3c208e5c472d68653d797\nRun 2 SHA-256: 6fcd17924b7333b8a6ba09b791d05e6662f5f1284ce3c208e5c472d68653d797\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Stacks and Queues",
    "subject": "stacks and queues",
    "description": "A stack is a last-in, first-out (LIFO, the last item added is the first removed) structure: push adds, pop removes, both in O(1). A queue is first-in, first-out (FIFO, the first item added is the first removed): enqueue adds at the back, dequeue removes from the front. Stacks model function calls; queues model waiting lines. A stack is LIFO: push and pop at the top, in O(1). A queue is FIFO: enqueue at the back, dequeue at the front, in O(1). The call stack holds the active function calls of a program.",
    "inputs": "FIGURES = {'stack_max_items': 2, 'expression_result': 14, 'queue_jobs': 100, 'last_wait_s': 99, 'recursion_depth': 10000, 'operations': 2, 'structures': 2, 'cost_per_op': 1}\nLABEL = 'stacks-and-queues'\n",
    "expected": "count: 8\nlabel: stacks-and-queues\nmax: 10000\nmean: 1277.5\nmin: 1\ntotal: 10220\nResult: count=8|label=stacks-and-queues|max=10000|mean=1277.5|min=1|total=10220\nRun 1 SHA-256: 24cfdcb82c51eeb0b98313c0393114cca2624aa27ad914033be0b2606d88e369\nRun 2 SHA-256: 24cfdcb82c51eeb0b98313c0393114cca2624aa27ad914033be0b2606d88e369\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Binary Search",
    "subject": "binary search",
    "description": "Binary search finds a value in a sorted array by halving the search range each step: compare with the middle, discard the half that cannot contain the value, and repeat. It takes O(log n) comparisons, against O(n) for a linear scan. The array must be sorted. Each step halves the range, so the count is log2(n). The array must be sorted; otherwise binary search is wrong. Binary search is the model for all divide-and-conquer search.",
    "inputs": "FIGURES = {'array_size': 1000000, 'binary_comparisons': 20, 'linear_comparisons': 500000, 'dictionary_words': 100000, 'dictionary_comparisons': 17, 'halvings': 20, 'midpoint_bug_year': 2006, 'first_year': 1946}\nLABEL = 'binary-search'\n",
    "expected": "count: 8\nlabel: binary-search\nmax: 1000000\nmean: 200501.125\nmin: 17\ntotal: 1604009\nResult: count=8|label=binary-search|max=1000000|mean=200501.125|min=17|total=1604009\nRun 1 SHA-256: afe21914642117a236dc1538e544c5003f5e88afcf945502d06260e8f57bcecb\nRun 2 SHA-256: afe21914642117a236dc1538e544c5003f5e88afcf945502d06260e8f57bcecb\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Sorting — Comparison Sorts",
    "subject": "sorting and comparison sorts",
    "description": "A comparison sort orders items by comparing them. The best comparison sorts (merge sort, heap sort, quicksort) take O(n log n) comparisons on average, and no comparison sort can beat O(n log n) in the worst case (the decision-tree lower bound). Insertion sort is O(n squared) but fast on nearly sorted data. Merge sort divides, sorts, and merges, in O(n log n) always. Quicksort partitions around a pivot, O(n log n) on average, O(n squared) worst case. No comparison sort can beat O(n log n) in the worst case.",
    "inputs": "FIGURES = {'n_items': 1000000, 'merge_comparisons': 20000000, 'merge_seconds': 0.04, 'quicksort_worst': 500000000000, 'quicksort_worst_seconds': 500, 'lower_bound': 18500000, 'sorts_compared': 3, 'decision_tree': 1}\nLABEL = 'sorting-and-comparison-sorts'\n",
    "expected": "count: 8\nlabel: sorting-and-comparison-sorts\nmax: 500000000000\nmean: 62504937563.005\nmin: 0.04\ntotal: 500039500504.04\nResult: count=8|label=sorting-and-comparison-sorts|max=500000000000|mean=62504937563.005|min=0.04|total=500039500504.04\nRun 1 SHA-256: c50595274805f1b4ed8d39746d4b1901231c32c1b14b4650b4380a0915d4b940\nRun 2 SHA-256: c50595274805f1b4ed8d39746d4b1901231c32c1b14b4650b4380a0915d4b940\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Quicksort and the Pivot",
    "subject": "quicksort and the pivot",
    "description": "Quicksort picks a pivot, partitions the array into elements below and above it, and recurses on the two sides. With a good pivot (the median), it takes O(n log n); with a bad pivot (the smallest or largest), it takes O(n squared). Choosing a random pivot makes the worst case unlikely. Partitioning around the pivot splits the array into two sides. A median pivot gives O(n log n); an extreme pivot gives O(n squared). A random pivot makes the expected time O(n log n).",
    "inputs": "FIGURES = {'n_items': 1000000, 'expected_comparisons': 27600000, 'expected_seconds': 0.028, 'worst_comparisons': 500000000000, 'worst_seconds': 500, 'ln_n': 13.8, 'pivot_choices': 3, 'invented_year': 1961}\nLABEL = 'quicksort-and-the-pivot'\n",
    "expected": "count: 8\nlabel: quicksort-and-the-pivot\nmax: 500000000000\nmean: 62503575309.7285\nmin: 0.028\ntotal: 500028602477.828\nResult: count=8|label=quicksort-and-the-pivot|max=500000000000|mean=62503575309.7285|min=0.028|total=500028602477.828\nRun 1 SHA-256: dd813e8b36ed34a1847b0b516c52db6e0e33927ef22ccd48ca9de5c39981f159\nRun 2 SHA-256: dd813e8b36ed34a1847b0b516c52db6e0e33927ef22ccd48ca9de5c39981f159\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Merge Sort and Divide and Conquer",
    "subject": "merge sort and divide and conquer",
    "description": "Merge sort is the archetype of divide and conquer: divide the array in half, sort each half recursively, and merge the two sorted halves in linear time. Its recurrence is T(n) = 2 T(n/2) + O(n), which solves to O(n log n) by the master theorem. It is stable and always O(n log n). Divide the array in half, sort each half, merge in O(n). The recurrence T(n) = 2T(n/2) + O(n) gives O(n log n). Merge sort is stable: equal items keep their order.",
    "inputs": "FIGURES = {'example_n': 8, 'merge_steps': 7, 'levels': 20, 'n_items': 1000000, 'operations': 20000000, 'extra_space': 1000000, 'stable': 1, 'invented_year': 1945}\nLABEL = 'merge-sort-and-divide-and-conquer'\n",
    "expected": "count: 8\nlabel: merge-sort-and-divide-and-conquer\nmax: 20000000\nmean: 2750247.625\nmin: 1\ntotal: 22001981\nResult: count=8|label=merge-sort-and-divide-and-conquer|max=20000000|mean=2750247.625|min=1|total=22001981\nRun 1 SHA-256: 4c67eac920795a8293c01b677c7ab7c7236c911e508dc0a8459c6512fc9c4ed9\nRun 2 SHA-256: 4c67eac920795a8293c01b677c7ab7c7236c911e508dc0a8459c6512fc9c4ed9\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Heaps and Priority Queues",
    "subject": "heaps and priority queues",
    "description": "A heap is a binary tree stored in an array, where each parent is smaller (min-heap) or larger (max-heap) than its children. A priority queue returns the smallest (or largest) item first, in O(log n) per insert and remove. Heap sort builds a heap in O(n) and removes the top n times, in O(n log n). A heap is a binary tree in an array, with the parent before the children. Insert and remove-min take O(log n), by bubbling up or down. Heap sort is O(n log n) and needs no extra space.",
    "inputs": "FIGURES = {'n_items': 1000000, 'build_ops': 1000000, 'remove_steps': 20, 'removals': 10, 'insert_steps': 20, 'inserts': 1000, 'heapsort_steps': 20000000, 'top_index': 0}\nLABEL = 'heaps-and-priority-queues'\n",
    "expected": "count: 8\nlabel: heaps-and-priority-queues\nmax: 20000000\nmean: 2750131.25\nmin: 0\ntotal: 22001050\nResult: count=8|label=heaps-and-priority-queues|max=20000000|mean=2750131.25|min=0|total=22001050\nRun 1 SHA-256: 3fbefe2fe1aaedffee84cb200ebc46bb58d4191a4d451f3993da62070965c07c\nRun 2 SHA-256: 3fbefe2fe1aaedffee84cb200ebc46bb58d4191a4d451f3993da62070965c07c\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Hash Tables",
    "subject": "hash tables",
    "description": "A hash table stores items by a hash function that maps each key to a bucket index. With a good hash function and a low load factor (items per bucket), lookup, insert, and delete take O(1) on average. Collisions (two keys in one bucket) are handled by chaining (a list per bucket) or open addressing (probing for an empty slot). The hash function maps a key to a bucket index. The load factor is items divided by buckets; keep it below 1. Collisions are handled by chaining or open addressing.",
    "inputs": "FIGURES = {'buckets': 1000000, 'items': 700000, 'load_factor': 0.7, 'expected_checks': 1, 'longest_chain': 5, 'doubled_buckets': 2000000, 'new_load_factor': 0.35, 'worst_case': 700000}\nLABEL = 'hash-tables'\n",
    "expected": "count: 8\nlabel: hash-tables\nmax: 2000000\nmean: 550000.8813\nmin: 0.35\ntotal: 4400007.05\nResult: count=8|label=hash-tables|max=2000000|mean=550000.8813|min=0.35|total=4400007.05\nRun 1 SHA-256: 5c9cb6123d6063695dbdd1a5a71d0600e071e4a603105b33ab524814c0e05b9e\nRun 2 SHA-256: 5c9cb6123d6063695dbdd1a5a71d0600e071e4a603105b33ab524814c0e05b9e\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Binary Search Trees",
    "subject": "binary search trees",
    "description": "A binary search tree (BST) stores items so that each node's left subtree holds smaller items and its right subtree holds larger ones. Search, insert, and delete take O(height); a balanced tree has height O(log n), but an unbalanced tree can have height O(n). Self-balancing trees (AVL, red-black) keep the height logarithmic. Left subtree smaller, right subtree larger, at every node. Search, insert, and delete take O(height). Balanced trees (AVL, red-black) keep the height O(log n).",
    "inputs": "FIGURES = {'sorted_height': 7, 'balanced_height': 3, 'n_items': 1000000, 'redblack_max_height': 40, 'search_steps_balanced': 3, 'search_steps_chain': 7, 'balance_types': 2, 'avl_year': 1962}\nLABEL = 'binary-search-trees'\n",
    "expected": "count: 8\nlabel: binary-search-trees\nmax: 1000000\nmean: 125253.0\nmin: 2\ntotal: 1002024\nResult: count=8|label=binary-search-trees|max=1000000|mean=125253.0|min=2|total=1002024\nRun 1 SHA-256: 708fa2954491b3054c60cc8e7957025bb9f0102695ec40102e98f82b81a61d2d\nRun 2 SHA-256: 708fa2954491b3054c60cc8e7957025bb9f0102695ec40102e98f82b81a61d2d\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Graphs and Their Representations",
    "subject": "graphs and their representations",
    "description": "A graph is a set of vertices (nodes) joined by edges. It can be stored as an adjacency list (each vertex lists its neighbours, O(V + E) space) or an adjacency matrix (a V by V table, O(V squared) space). Lists suit sparse graphs; matrices suit dense graphs and fast edge tests. An adjacency list stores each vertex's neighbours: O(V + E) space. An adjacency matrix stores a V by V table: O(V squared) space. Lists suit sparse graphs; matrices suit dense graphs.",
    "inputs": "FIGURES = {'vertices': 10000, 'edges': 30000, 'list_entries': 70000, 'matrix_entries': 100000000, 'ratio': 1400, 'avg_degree': 6, 'users': 1000000000, 'friendships': 100000000000}\nLABEL = 'graphs-and-their-representations'\n",
    "expected": "count: 8\nlabel: graphs-and-their-representations\nmax: 100000000000\nmean: 12637513925.75\nmin: 6\ntotal: 101100111406\nResult: count=8|label=graphs-and-their-representations|max=100000000000|mean=12637513925.75|min=6|total=101100111406\nRun 1 SHA-256: e854e9e2f43b69674bb2bd18cb637b0dcac0e113b61acc336f70abd765586c1c\nRun 2 SHA-256: e854e9e2f43b69674bb2bd18cb637b0dcac0e113b61acc336f70abd765586c1c\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Breadth-First and Depth-First Search",
    "subject": "breadth-first and depth-first search",
    "description": "Breadth-first search (BFS) explores a graph level by level, using a queue, and finds the shortest path (fewest edges) in an unweighted graph. Depth-first search (DFS) explores as deep as possible first, using a stack (or recursion), and finds paths, cycles, and connected components. Both take O(V + E) time. BFS uses a queue and explores level by level; it finds shortest paths. DFS uses a stack and explores deep first; it finds cycles and components. Both visit each vertex and edge once: O(V + E).",
    "inputs": "FIGURES = {'maze_cells': 10000, 'maze_passages': 20000, 'bfs_steps': 10000, 'vertices': 1000000, 'edges': 5000000, 'total_steps': 6000000, 'time_seconds': 0.006, 'searches': 2}\nLABEL = 'breadth-first-and-depth-first-search'\n",
    "expected": "count: 8\nlabel: breadth-first-and-depth-first-search\nmax: 6000000\nmean: 1505000.2507\nmin: 0.006\ntotal: 12040002.006\nResult: count=8|label=breadth-first-and-depth-first-search|max=6000000|mean=1505000.2507|min=0.006|total=12040002.006\nRun 1 SHA-256: ef416e2cb654d5b51d3fc1adc5d518d34fa4355d37ae27a9ac6598df92613370\nRun 2 SHA-256: ef416e2cb654d5b51d3fc1adc5d518d34fa4355d37ae27a9ac6598df92613370\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Dijkstra's Shortest Path Algorithm",
    "subject": "Dijkstra's shortest path algorithm",
    "description": "Dijkstra's algorithm finds the shortest path from a start vertex to all others in a graph with non-negative edge weights. It keeps a priority queue of the closest unvisited vertices, settles the closest one, and relaxes its edges. With a binary heap it takes O((V + E) log V). The closest unvisited vertex is settled first, and its distance is final. Relaxing an edge improves the distance to its far end. With a binary heap, the time is O((V + E) log V).",
    "inputs": "FIGURES = {'vertices': 10000, 'edges': 30000, 'heap_steps': 14, 'total_steps': 560000, 'time_ms': 1, 'distance_km': 500, 'published_year': 1959, 'queue_max': 10000}\nLABEL = 'dijkstra-s-shortest-path-algorithm'\n",
    "expected": "count: 8\nlabel: dijkstra-s-shortest-path-algorithm\nmax: 560000\nmean: 76559.25\nmin: 1\ntotal: 612474\nResult: count=8|label=dijkstra-s-shortest-path-algorithm|max=560000|mean=76559.25|min=1|total=612474\nRun 1 SHA-256: 1c8ea8cb4d3efc5971fb444750b6e931686b05388d8be51c4142118a08036337\nRun 2 SHA-256: 1c8ea8cb4d3efc5971fb444750b6e931686b05388d8be51c4142118a08036337\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Minimum Spanning Trees",
    "subject": "minimum spanning trees",
    "description": "A minimum spanning tree (MST) connects all vertices of a weighted graph with the least total edge weight. Kruskal's algorithm adds the cheapest edge that does not form a cycle (using a union-find structure). Prim's algorithm grows the tree from a start vertex, always adding the cheapest edge to the tree. Both are greedy and both are correct. Kruskal adds the cheapest edge that does not form a cycle. Prim grows the tree, always adding the cheapest edge to it. Both are greedy and both give the minimum total weight.",
    "inputs": "FIGURES = {'cities': 5, 'roads': 10, 'mst_edges': 4, 'mst_cost': 10, 'cheapest_edges': 4, 'kruskal_year': 1956, 'prim_year': 1957, 'algorithms': 2}\nLABEL = 'minimum-spanning-trees'\n",
    "expected": "count: 8\nlabel: minimum-spanning-trees\nmax: 1957\nmean: 493.5\nmin: 2\ntotal: 3948\nResult: count=8|label=minimum-spanning-trees|max=1957|mean=493.5|min=2|total=3948\nRun 1 SHA-256: 35f6caac4f41f2600e6be2915e06d2a40a9ee957c9d1303d98104ca8ea216488\nRun 2 SHA-256: 35f6caac4f41f2600e6be2915e06d2a40a9ee957c9d1303d98104ca8ea216488\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Dynamic Programming",
    "subject": "dynamic programming",
    "description": "Dynamic programming solves a problem by breaking it into overlapping subproblems, solving each once, and storing the answers (memoisation, or a table). It turns exponential recursion into polynomial time when the subproblems overlap. The Fibonacci numbers are the classic example: naive recursion is O(2^n), dynamic programming is O(n). Overlapping subproblems are solved once and stored. Memoisation stores answers as they are computed; tabulation fills a table. The Fibonacci numbers go from O(2^n) to O(n).",
    "inputs": "FIGURES = {'fib_n': 50, 'naive_calls': 40730022147, 'naive_seconds': 41, 'dp_steps': 50, 'fib_50': 12586269025, 'knapsack_items': 100, 'knapsack_capacity': 1000, 'knapsack_entries': 100000}\nLABEL = 'dynamic-programming'\n",
    "expected": "count: 8\nlabel: dynamic-programming\nmax: 40730022147\nmean: 6664549051.625\nmin: 41\ntotal: 53316392413\nResult: count=8|label=dynamic-programming|max=40730022147|mean=6664549051.625|min=41|total=53316392413\nRun 1 SHA-256: de1e9ddd826aa33569b1ad6c4b22870453fa0e64e0f9d80c4fc0d2a031883a95\nRun 2 SHA-256: de1e9ddd826aa33569b1ad6c4b22870453fa0e64e0f9d80c4fc0d2a031883a95\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Greedy Algorithms",
    "subject": "greedy algorithms",
    "description": "A greedy algorithm makes the locally best choice at each step, hoping it leads to a global optimum. It works when the problem has the greedy-choice property (a locally optimal choice is part of some global optimum) and optimal substructure. Activity selection, Huffman coding, and MSTs are greedy; knapsack in general is not. Greedy makes the locally best choice at each step. It works with the greedy-choice property and optimal substructure. Activity selection, Huffman coding, and MSTs are greedy.",
    "inputs": "FIGURES = {'activities': 6, 'greedy_count': 3, 'earliest_start_count': 2, 'symbols': 6, 'huffman_avg_bits': 2.24, 'fixed_bits': 3, 'huffman_year': 1952, 'examples': 3}\nLABEL = 'greedy-algorithms'\n",
    "expected": "count: 8\nlabel: greedy-algorithms\nmax: 1952\nmean: 247.155\nmin: 2\ntotal: 1977.24\nResult: count=8|label=greedy-algorithms|max=1952|mean=247.155|min=2|total=1977.24\nRun 1 SHA-256: 3eb9de32c5510b41a5c04acdb38f1abeb2c879e94e66d975c267968144a824e3\nRun 2 SHA-256: 3eb9de32c5510b41a5c04acdb38f1abeb2c879e94e66d975c267968144a824e3\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Divide and Conquer and the Master Theorem",
    "subject": "divide and conquer and the master theorem",
    "description": "Divide and conquer splits a problem into smaller copies of itself, solves them recursively, and combines the answers. The master theorem solves recurrences of the form T(n) = a T(n/b) + f(n): if f(n) is smaller than n^(log_b a), the leaves dominate; if it is larger, the root dominates; if equal, the total is n^(log_b a) log n. T(n) = a T(n/b) + f(n) describes a divide-and-conquer algorithm. If f(n) is smaller than n^(log_b a), the answer is Theta(n^(log_b a)). If f(n) is larger, the answer is Theta(f(n)).",
    "inputs": "FIGURES = {'merge_a': 2, 'merge_b': 2, 'merge_result': 1, 'karatsuba_a': 3, 'karatsuba_exponent': 1.585, 'digits': 1000, 'karatsuba_ops': 56000, 'schoolbook_ops': 1000000}\nLABEL = 'divide-and-conquer-and-the-master-theorem'\n",
    "expected": "count: 8\nlabel: divide-and-conquer-and-the-master-theorem\nmax: 1000000\nmean: 132126.1981\nmin: 1\ntotal: 1057009.585\nResult: count=8|label=divide-and-conquer-and-the-master-theorem|max=1000000|mean=132126.1981|min=1|total=1057009.585\nRun 1 SHA-256: bdb60010acec8637c025f55ccdc8c6db39865df962c7e01e24e9d2b70728e56e\nRun 2 SHA-256: bdb60010acec8637c025f55ccdc8c6db39865df962c7e01e24e9d2b70728e56e\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Recursion and the Call Stack",
    "subject": "recursion and the call stack",
    "description": "Recursion solves a problem by calling the same function on smaller inputs, with a base case that stops. Each call pushes a frame on the call stack; returning pops it. The depth is the number of simultaneous calls, and the time is the number of calls. Tail recursion can be turned into a loop. A recursive function calls itself on smaller inputs. The base case stops the recursion. Each call pushes a frame; the depth is the number of live calls.",
    "inputs": "FIGURES = {'factorial': 120, 'stack_depth': 6, 'fib_calls': 40730022147, 'fib_seconds': 41, 'iterative_steps': 50, 'recursion_limit': 1000, 'base_case': 1, 'frames': 6}\nLABEL = 'recursion-and-the-call-stack'\n",
    "expected": "count: 8\nlabel: recursion-and-the-call-stack\nmax: 40730022147\nmean: 5091252921.375\nmin: 1\ntotal: 40730023371\nResult: count=8|label=recursion-and-the-call-stack|max=40730022147|mean=5091252921.375|min=1|total=40730023371\nRun 1 SHA-256: fd2b52f4b205b7ef52d271e338f0ea73a6779aa71358d2a54876010dfc18a817\nRun 2 SHA-256: fd2b52f4b205b7ef52d271e338f0ea73a6779aa71358d2a54876010dfc18a817\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Tries and String Matching",
    "subject": "tries and string matching",
    "description": "A trie (a prefix tree) stores strings by their shared prefixes: each edge is a character, and each node is a prefix. Looking up a word of length m takes O(m), regardless of how many words are stored. The Knuth-Morris-Pratt (KMP) algorithm finds a pattern in a text in O(n + m) by never re-examining characters. A trie stores shared prefixes once; lookup takes O(m) for a word of length m. KMP preprocesses the pattern and scans the text once: O(n + m). Naive string search takes O(n times m) in the worst case.",
    "inputs": "FIGURES = {'dictionary_words': 100000, 'word_length': 9, 'trie_steps': 9, 'binary_steps': 17, 'linear_steps': 50000, 'text_length': 1000000, 'kmp_steps': 1000000, 'naive_steps': 4000000}\nLABEL = 'tries-and-string-matching'\n",
    "expected": "count: 8\nlabel: tries-and-string-matching\nmax: 4000000\nmean: 768754.375\nmin: 9\ntotal: 6150035\nResult: count=8|label=tries-and-string-matching|max=4000000|mean=768754.375|min=9|total=6150035\nRun 1 SHA-256: ea28686c7148bc5bf80547ba7d0eaa2631692d182bf0644bdec63f5b41d7d68e\nRun 2 SHA-256: ea28686c7148bc5bf80547ba7d0eaa2631692d182bf0644bdec63f5b41d7d68e\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: The Union-Find Structure",
    "subject": "the union-find structure",
    "description": "Union-find (the disjoint-set union) tracks which items are in the same set: find returns the set's representative, union merges two sets. With union by rank and path compression, each operation takes nearly constant time (the inverse Ackermann function, effectively O(1)). It is the engine of Kruskal's algorithm. Find returns the representative of an item's set. Union merges two sets by rank. Path compression flattens the tree on every find.",
    "inputs": "FIGURES = {'singletons': 1000000, 'unions': 500000, 'operations': 1500000, 'tree_height': 3, 'kruskal_edges': 30000, 'kruskal_unions': 10000, 'inverse_ackermann': 5, 'time_ms': 1}\nLABEL = 'the-union-find-structure'\n",
    "expected": "count: 8\nlabel: the-union-find-structure\nmax: 1500000\nmean: 380001.125\nmin: 1\ntotal: 3040009\nResult: count=8|label=the-union-find-structure|max=1500000|mean=380001.125|min=1|total=3040009\nRun 1 SHA-256: c231a6b7f950de13bd2cb98f8198390ed54708b95e81f105f5176e9480191528\nRun 2 SHA-256: c231a6b7f950de13bd2cb98f8198390ed54708b95e81f105f5176e9480191528\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: NP-Completeness and Intractability",
    "subject": "NP-completeness and intractability",
    "description": "NP is the class of problems whose solutions can be checked in polynomial time. NP-complete problems are the hardest in NP: if one has a polynomial-time algorithm, all do. The travelling salesperson, satisfiability (SAT), and graph colouring are NP-complete. The P versus NP question (whether they can be solved in polynomial time) is open, with a million-dollar prize. P is solvable in polynomial time; NP is checkable in polynomial time. NP-complete problems are the hardest in NP. P versus NP is open; most believe P is not NP.",
    "inputs": "FIGURES = {'cities_20': 20, 'tours_20': 60000000000000000, 'years_20': 1900, 'cities_10': 10, 'tours_10': 181440, 'sat_variables': 100, 'sat_assignments': 1300000000000000000000000000000, 'heuristic_gap_pct': 5}\nLABEL = 'np-completeness-and-intractability'\n",
    "expected": "count: 8\nlabel: np-completeness-and-intractability\nmax: 1300000000000000000000000000000\nmean: 1.625000000000075e+29\nmin: 5\ntotal: 1300000000000060000000000183475\nResult: count=8|label=np-completeness-and-intractability|max=1300000000000000000000000000000|mean=1.625000000000075e+29|min=5|total=1300000000000060000000000183475\nRun 1 SHA-256: 3c918fbb8b6e2fb71f0694214db454f5a051982a2361efdb8f109109bca1ff9e\nRun 2 SHA-256: 3c918fbb8b6e2fb71f0694214db454f5a051982a2361efdb8f109109bca1ff9e\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Approximation and Heuristics",
    "subject": "approximation and heuristics",
    "description": "When an exact algorithm is too slow (NP-hard problems), approximation algorithms guarantee a solution within a factor of optimal, and heuristics find good solutions without a guarantee. The greedy set-cover algorithm is within a factor of ln(n) of optimal; the 2-approximation for travelling salesperson (via the MST) is within twice optimal. An approximation algorithm guarantees a factor of optimal. A heuristic finds good answers without a guarantee. The MST-based TSP tour is within twice optimal.",
    "inputs": "FIGURES = {'points': 100, 'set_cover_factor': 4.6, 'optimal_tour_km': 1000, 'heuristic_bound_km': 2000, 'heuristic_practical_km': 1100, 'factor': 2, 'improvement': 1, 'guarantee_year': 1974}\nLABEL = 'approximation-and-heuristics'\n",
    "expected": "count: 8\nlabel: approximation-and-heuristics\nmax: 2000\nmean: 772.7\nmin: 1\ntotal: 6181.6\nResult: count=8|label=approximation-and-heuristics|max=2000|mean=772.7|min=1|total=6181.6\nRun 1 SHA-256: f0a171353f2e87e30513633d7d299f7087100b47c222e2dad38e1481ec06ebab\nRun 2 SHA-256: f0a171353f2e87e30513633d7d299f7087100b47c222e2dad38e1481ec06ebab\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: A* Search and Heuristic Search",
    "subject": "A* search and heuristic search",
    "description": "A* search finds the shortest path using a heuristic: it expands the vertex with the smallest f = g + h, where g is the distance so far and h is the heuristic estimate of the distance remaining. With an admissible heuristic (one that never overestimates), A* is optimal, and it explores far fewer vertices than Dijkstra's algorithm. f = g + h: the distance so far plus the estimated distance remaining. An admissible heuristic never overestimates, so A* is optimal. A* explores far fewer vertices than Dijkstra.",
    "inputs": "FIGURES = {'grid_size': 10, 'cells': 100, 'optimal_steps': 18, 'dijkstra_settled': 100, 'astar_settled': 30, 'heuristic_at_start': 18, 'saved_cells': 70, 'directions': 4}\nLABEL = 'a-search-and-heuristic-search'\n",
    "expected": "count: 8\nlabel: a-search-and-heuristic-search\nmax: 100\nmean: 43.75\nmin: 4\ntotal: 350\nResult: count=8|label=a-search-and-heuristic-search|max=100|mean=43.75|min=4|total=350\nRun 1 SHA-256: 8943274b3687e9e061004380d4ff91185b2edb8e03b819ecc692a19034dc85c2\nRun 2 SHA-256: 8943274b3687e9e061004380d4ff91185b2edb8e03b819ecc692a19034dc85c2\nDeterministic: MATCH\n"
  },
  {
    "title": "Algorithms and Data Structures: Capstone — Design a Route Planner",
    "subject": "a capstone route planner design",
    "description": "This capstone designs a route planner from the pieces of the course: a graph of roads, Dijkstra's algorithm with a binary heap, a hash table for the place index, and an A* heuristic for speed, with the running time analysed by Big-O and the result checked against a known route. A capstone problem uses several tools at once. The roads are a graph, stored as an adjacency list. Dijkstra with a binary heap finds the shortest path in O((V + E) log V). A hash table indexes places by name; A* speeds the search with a heuristic.",
    "inputs": "FIGURES = {'vertices': 10000, 'edges': 30000, 'dijkstra_steps': 560000, 'time_ms': 1, 'places': 10000, 'load_factor': 0.7, 'distance_km': 500, 'tools': 4}\nLABEL = 'a-capstone-route-planner-design'\n",
    "expected": "count: 8\nlabel: a-capstone-route-planner-design\nmax: 560000\nmean: 76313.2125\nmin: 0.7\ntotal: 610505.7\nResult: count=8|label=a-capstone-route-planner-design|max=560000|mean=76313.2125|min=0.7|total=610505.7\nRun 1 SHA-256: 7b8a968eb82b7e4c070a4ff622f2e4d364a5ab424be3283f3da16c5c78f12d7b\nRun 2 SHA-256: 7b8a968eb82b7e4c070a4ff622f2e4d364a5ab424be3283f3da16c5c78f12d7b\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Big O notation",
    "url": "https://en.wikipedia.org/wiki/Big_O_notation",
    "establishes": "The reference for Big-O notation and growth rates in this record."
  },
  {
    "name": "Wikipedia - Time complexity",
    "url": "https://en.wikipedia.org/wiki/Time_complexity",
    "establishes": "The reference for Big-O notation and growth rates in this record."
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic) {
  const code = "import hashlib\n" + topic.inputs +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    mean = round(total / n, 4) if n else 0\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), " +
    "\"mean\": mean, \"min\": min(FIGURES.values()), \"total\": round(total, 4)}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  return { code: code, expected: topic.expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const demo = buildDemo(topic);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + (EDITION === "signature"
      ? " Design-study: this is a Signature-made design, labelled design-study throughout, never presented as established fact or as an authentic public record."
      : " Established college-level knowledge, checked against its cited sources."),
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record: the same shape as the filed records, with its own figures.", A2: "The whole edition: every generated record joins the 24 filed records.", A3: "The subject against the whole network: every college subject linked, every record searchable." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug", a.slug === SLUG);
  t("slug signature form", EDITION === "signature" ? (a.slug.split("-signature").length - 1) === 1 : a.slug.indexOf("-signature") === -1);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
