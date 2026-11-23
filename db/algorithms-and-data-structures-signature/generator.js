// Seeded boundless generator for the The Signature Algorithms and Data Structures Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-algorithms-and-data-structures-signature.js [seed]  (prints one JSON record)
// or: node gen-algorithms-and-data-structures-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "algorithms-and-data-structures-signature";
const RECORD_KIND = "algorithms and data structures record";
const ID_PREFIX = "JAH-ALGDSS-";
const AI_NAME = "JAH Algorithms Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Growth Chart",
    "subject": "a Signature growth chart design",
    "description": "The Growth Chart is a Signature-made design for teaching Big-O notation: a chart where a learner plots the growth curves of constant, logarithmic, linear, linearithmic, quadratic, and exponential time, and watches the curves separate as n grows. Big-O describes how running time grows with input size. The six growth curves are plotted together on one chart. The input size is set on a slider, and the times are shown. Doubling n is shown multiplying the quadratic time by 4 and the linear time by 2.",
    "inputs": "FIGURES = {'n_items': 1000000, 'nlogn_comparisons': 20000000, 'nlogn_seconds': 0.02, 'nsquared_comparisons': 500000000000, 'nsquared_seconds': 500, 'doubled_nlogn_seconds': 0.042, 'doubled_nsquared_seconds': 2000, 'growth_classes': 6}\nLABEL = 'a-signature-growth-chart-design'\n",
    "expected": "count: 8\nlabel: a-signature-growth-chart-design\nmax: 500000000000\nmean: 62502625313.2578\nmin: 0.02\ntotal: 500021002506.062\nResult: count=8|label=a-signature-growth-chart-design|max=500000000000|mean=62502625313.2578|min=0.02|total=500021002506.062\nRun 1 SHA-256: c176445c06b197a77e5609dfcb579f7cf8c8a84e95b48993af00fe34672d8166\nRun 2 SHA-256: c176445c06b197a77e5609dfcb579f7cf8c8a84e95b48993af00fe34672d8166\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Array-List Seesaw",
    "subject": "a Signature array-list seesaw design",
    "description": "The Array-List Seesaw is a Signature-made design for teaching arrays and linked lists: a seesaw where a learner weighs access against insertion, with the array winning access and the list winning insertion. An array gives O(1) access by index; a linked list gives O(1) insertion at a known node. Access is weighed on one side, insertion on the other. The array wins access (1 step); the list wins insertion (1 step). The dynamic array's amortised append is shown as O(1).",
    "inputs": "FIGURES = {'array_size': 1000000, 'array_bytes': 4000000, 'array_access_steps': 1, 'array_insert_shifts': 1000000, 'insert_time_ms': 1, 'list_reach_steps': 500000, 'list_reach_ms': 0.5, 'amortised_append': 1}\nLABEL = 'a-signature-array-list-seesaw-design'\n",
    "expected": "count: 8\nlabel: a-signature-array-list-seesaw-design\nmax: 4000000\nmean: 812500.4375\nmin: 0.5\ntotal: 6500003.5\nResult: count=8|label=a-signature-array-list-seesaw-design|max=4000000|mean=812500.4375|min=0.5|total=6500003.5\nRun 1 SHA-256: 481595ad5d47b7e110b2fbfeee545fae04083938e3439eee1d21c6a5d334ba32\nRun 2 SHA-256: 481595ad5d47b7e110b2fbfeee545fae04083938e3439eee1d21c6a5d334ba32\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Stack Machine",
    "subject": "a Signature stack machine design",
    "description": "The Stack Machine is a Signature-made design for teaching stacks and queues: a machine where a learner evaluates expressions with a stack and serves jobs with a queue, watching the stack hold operands and the queue hold jobs in order. A stack is last-in, first-out; a queue is first-in, first-out. The stack is shown holding operands until the operator arrives. The queue is shown holding jobs in arrival order. The call stack is shown holding the active function calls.",
    "inputs": "FIGURES = {'stack_max_items': 2, 'expression_result': 14, 'queue_jobs': 100, 'last_wait_s': 99, 'recursion_depth': 10000, 'operations': 2, 'structures': 2, 'design_version': 1}\nLABEL = 'a-signature-stack-machine-design'\n",
    "expected": "count: 8\nlabel: a-signature-stack-machine-design\nmax: 10000\nmean: 1277.5\nmin: 1\ntotal: 10220\nResult: count=8|label=a-signature-stack-machine-design|max=10000|mean=1277.5|min=1|total=10220\nRun 1 SHA-256: cb78e95c6115180066a791ad9d0c099360eb3cfe4795573cce2781e11a211ee3\nRun 2 SHA-256: cb78e95c6115180066a791ad9d0c099360eb3cfe4795573cce2781e11a211ee3\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Halving Finder",
    "subject": "a Signature halving finder design",
    "description": "The Halving Finder is a Signature-made design for teaching binary search: a finder where a learner searches a sorted array, and the tool halves the range at each step, showing the range shrinking from a million to one in 20 steps. Binary search takes O(log n) comparisons. The range is shown shrinking by half at each step. The comparison count is shown against the linear scan's. The invariant is shown: the value, if present, is inside the range.",
    "inputs": "FIGURES = {'array_size': 1000000, 'binary_comparisons': 20, 'linear_comparisons': 500000, 'dictionary_words': 100000, 'dictionary_comparisons': 17, 'halvings': 20, 'midpoint_bug_year': 2006, 'design_version': 1}\nLABEL = 'a-signature-halving-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-halving-finder-design\nmax: 1000000\nmean: 200258.0\nmin: 1\ntotal: 1602064\nResult: count=8|label=a-signature-halving-finder-design|max=1000000|mean=200258.0|min=1|total=1602064\nRun 1 SHA-256: 04d0483e8278ab4ee7922ad5ff7d48d99c64e080b8d3c2066a35d1d9e8f2ac10\nRun 2 SHA-256: 04d0483e8278ab4ee7922ad5ff7d48d99c64e080b8d3c2066a35d1d9e8f2ac10\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Sorting Race",
    "subject": "a Signature sorting race design",
    "description": "The Sorting Race is a Signature-made design for teaching sorting: a race where a learner runs merge sort, quicksort, and insertion sort on the same data, and the tool shows the comparison counts and the times, with the O(n log n) sorts far ahead. No comparison sort can beat O(n log n). The three sorts run on the same data, and their counts are shown. The decision-tree lower bound is shown as the finish line. Quicksort's worst case is shown as a stumble.",
    "inputs": "FIGURES = {'n_items': 1000000, 'merge_comparisons': 20000000, 'merge_seconds': 0.04, 'quicksort_worst': 500000000000, 'quicksort_worst_seconds': 500, 'lower_bound': 18500000, 'sorts_compared': 3, 'design_version': 1}\nLABEL = 'a-signature-sorting-race-design'\n",
    "expected": "count: 8\nlabel: a-signature-sorting-race-design\nmax: 500000000000\nmean: 62504937563.005\nmin: 0.04\ntotal: 500039500504.04\nResult: count=8|label=a-signature-sorting-race-design|max=500000000000|mean=62504937563.005|min=0.04|total=500039500504.04\nRun 1 SHA-256: 0407d5e5ef6cf30a0f049b0935ffa5f19819ca6ddf5511599c100e2acfb18f17\nRun 2 SHA-256: 0407d5e5ef6cf30a0f049b0935ffa5f19819ca6ddf5511599c100e2acfb18f17\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Pivot Chooser",
    "subject": "a Signature pivot chooser design",
    "description": "The Pivot Chooser is a Signature-made design for teaching quicksort: a chooser where a learner picks the pivot (first, random, or median-of-three), and the tool shows the partitions, the comparison count, and the time. A good pivot gives O(n log n); a bad pivot gives O(n squared). The pivot rule is chosen, and the partitions are shown. The comparison count is shown for each rule. The sorted-data trap is shown for the first-element pivot.",
    "inputs": "FIGURES = {'n_items': 1000000, 'expected_comparisons': 27600000, 'expected_seconds': 0.028, 'worst_comparisons': 500000000000, 'worst_seconds': 500, 'ln_n': 13.8, 'pivot_choices': 3, 'design_version': 1}\nLABEL = 'a-signature-pivot-chooser-design'\n",
    "expected": "count: 8\nlabel: a-signature-pivot-chooser-design\nmax: 500000000000\nmean: 62503575064.7285\nmin: 0.028\ntotal: 500028600517.828\nResult: count=8|label=a-signature-pivot-chooser-design|max=500000000000|mean=62503575064.7285|min=0.028|total=500028600517.828\nRun 1 SHA-256: 73d6237dadbc4311770c6f5099a44e663ef2a9d50ba11d08fba6c54d5ffe4686\nRun 2 SHA-256: 73d6237dadbc4311770c6f5099a44e663ef2a9d50ba11d08fba6c54d5ffe4686\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Merge Tree",
    "subject": "a Signature merge tree design",
    "description": "The Merge Tree is a Signature-made design for teaching merge sort: a tree where a learner watches the array split in half recursively, and the sorted halves merge back, level by level, with the work at each level shown. Merge sort is divide and conquer: T(n) = 2T(n/2) + O(n). The recursion tree is drawn, with the splits and the merges. The work at each level is shown: n operations at each of log n levels. Stability is shown: equal items keep their order.",
    "inputs": "FIGURES = {'example_n': 8, 'merge_steps': 7, 'levels': 20, 'n_items': 1000000, 'operations': 20000000, 'extra_space': 1000000, 'stable': 1, 'design_version': 1}\nLABEL = 'a-signature-merge-tree-design'\n",
    "expected": "count: 8\nlabel: a-signature-merge-tree-design\nmax: 20000000\nmean: 2750004.625\nmin: 1\ntotal: 22000037\nResult: count=8|label=a-signature-merge-tree-design|max=20000000|mean=2750004.625|min=1|total=22000037\nRun 1 SHA-256: 4d5c1006f223991e11300b1bb4d482c65a5589148838815aa6614977d0a79dcc\nRun 2 SHA-256: 4d5c1006f223991e11300b1bb4d482c65a5589148838815aa6614977d0a79dcc\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Heap Playground",
    "subject": "a Signature heap playground design",
    "description": "The Heap Playground is a Signature-made design for teaching heaps: a playground where a learner builds a heap, inserts items, and removes the smallest, watching the items bubble up and down. A heap is a binary tree in an array, with the smallest item at the top. The heap is drawn as a tree and as an array, side by side. Insertions bubble up; removals bubble down. The smallest item is always at index 0.",
    "inputs": "FIGURES = {'n_items': 1000000, 'build_ops': 1000000, 'remove_steps': 20, 'removals': 10, 'insert_steps': 20, 'inserts': 1000, 'heapsort_steps': 20000000, 'top_index': 0}\nLABEL = 'a-signature-heap-playground-design'\n",
    "expected": "count: 8\nlabel: a-signature-heap-playground-design\nmax: 20000000\nmean: 2750131.25\nmin: 0\ntotal: 22001050\nResult: count=8|label=a-signature-heap-playground-design|max=20000000|mean=2750131.25|min=0|total=22001050\nRun 1 SHA-256: 376f33b16e0e8e456ea7926770843dd43fdf26bd0fd6ddeee72749129d574d1d\nRun 2 SHA-256: 376f33b16e0e8e456ea7926770843dd43fdf26bd0fd6ddeee72749129d574d1d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Hash Bucket Board",
    "subject": "a Signature hash bucket board design",
    "description": "The Hash Bucket Board is a Signature-made design for teaching hash tables: a board where a learner hashes keys into buckets, watches the load factor, and sees collisions handled by chaining. A hash table gives average O(1) lookup with a good hash function and a low load factor. Keys are hashed into buckets, and the buckets are shown filling. The load factor is shown, and rehashing halves it. A bad hash is shown piling all keys into one bucket.",
    "inputs": "FIGURES = {'buckets': 1000000, 'items': 700000, 'load_factor': 0.7, 'expected_checks': 1, 'longest_chain': 5, 'doubled_buckets': 2000000, 'new_load_factor': 0.35, 'worst_case': 700000}\nLABEL = 'a-signature-hash-bucket-board-design'\n",
    "expected": "count: 8\nlabel: a-signature-hash-bucket-board-design\nmax: 2000000\nmean: 550000.8813\nmin: 0.35\ntotal: 4400007.05\nResult: count=8|label=a-signature-hash-bucket-board-design|max=2000000|mean=550000.8813|min=0.35|total=4400007.05\nRun 1 SHA-256: af3330d7f0a32c2ca9ce96e670f868b0473c4b5ce1db58a03e7690b853d61d8a\nRun 2 SHA-256: af3330d7f0a32c2ca9ce96e670f868b0473c4b5ce1db58a03e7690b853d61d8a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Search Tree Balancer",
    "subject": "a Signature search tree balancer design",
    "description": "The Search Tree Balancer is a Signature-made design for teaching binary search trees: a balancer where a learner inserts keys in order and watches the tree degenerate into a chain, then inserts them balanced and watches the height stay logarithmic. A balanced tree has height O(log n). Inserting in order is shown building a chain of height n. Inserting balanced is shown building a tree of height log n. AVL and red-black rotations are shown restoring balance.",
    "inputs": "FIGURES = {'sorted_height': 7, 'balanced_height': 3, 'n_items': 1000000, 'redblack_max_height': 40, 'search_steps_balanced': 3, 'search_steps_chain': 7, 'balance_types': 2, 'design_version': 1}\nLABEL = 'a-signature-search-tree-balancer-design'\n",
    "expected": "count: 8\nlabel: a-signature-search-tree-balancer-design\nmax: 1000000\nmean: 125007.875\nmin: 1\ntotal: 1000063\nResult: count=8|label=a-signature-search-tree-balancer-design|max=1000000|mean=125007.875|min=1|total=1000063\nRun 1 SHA-256: 21feda1514c64359c6b0136bf6ea536a0ea0309023c3bcd996d01449f5d52433\nRun 2 SHA-256: 21feda1514c64359c6b0136bf6ea536a0ea0309023c3bcd996d01449f5d52433\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Graph Atlas",
    "subject": "a Signature graph atlas design",
    "description": "The Graph Atlas is a Signature-made design for teaching graphs: an atlas where a learner draws a road network, and the tool shows it as an adjacency list and as an adjacency matrix, with the sizes compared. Lists suit sparse graphs; matrices suit dense graphs. The graph is drawn, and both representations are shown. The sizes are compared: V + 2E against V squared. Edge tests are shown fast in the matrix and slow in the list.",
    "inputs": "FIGURES = {'vertices': 10000, 'edges': 30000, 'list_entries': 70000, 'matrix_entries': 100000000, 'ratio': 1400, 'avg_degree': 6, 'users': 1000000000, 'friendships': 100000000000}\nLABEL = 'a-signature-graph-atlas-design'\n",
    "expected": "count: 8\nlabel: a-signature-graph-atlas-design\nmax: 100000000000\nmean: 12637513925.75\nmin: 6\ntotal: 101100111406\nResult: count=8|label=a-signature-graph-atlas-design|max=100000000000|mean=12637513925.75|min=6|total=101100111406\nRun 1 SHA-256: 265ef06919299bf0c78c3e137de1f7037321d95433ca36a395d0c1cc1cacbf50\nRun 2 SHA-256: 265ef06919299bf0c78c3e137de1f7037321d95433ca36a395d0c1cc1cacbf50\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Maze Explorer",
    "subject": "a Signature maze explorer design",
    "description": "The Maze Explorer is a Signature-made design for teaching BFS and DFS: an explorer where a learner runs breadth-first and depth-first search through the same maze, watching BFS find the shortest path level by level and DFS plunge deep first. Both take O(V + E) time. BFS is shown level by level, finding the shortest path. DFS is shown plunging deep, finding cycles and components. The step counts are shown equal: V + E each.",
    "inputs": "FIGURES = {'maze_cells': 10000, 'maze_passages': 20000, 'bfs_steps': 10000, 'vertices': 1000000, 'edges': 5000000, 'total_steps': 6000000, 'time_seconds': 0.006, 'searches': 2}\nLABEL = 'a-signature-maze-explorer-design'\n",
    "expected": "count: 8\nlabel: a-signature-maze-explorer-design\nmax: 6000000\nmean: 1505000.2507\nmin: 0.006\ntotal: 12040002.006\nResult: count=8|label=a-signature-maze-explorer-design|max=6000000|mean=1505000.2507|min=0.006|total=12040002.006\nRun 1 SHA-256: 626fbac6ce671bbc0a288a4ed9efaf135b21a8c439fd81f210b203db42b2b025\nRun 2 SHA-256: 626fbac6ce671bbc0a288a4ed9efaf135b21a8c439fd81f210b203db42b2b025\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Shortest Path Navigator",
    "subject": "a Signature shortest path navigator design",
    "description": "The Shortest Path Navigator is a Signature-made design for teaching Dijkstra's algorithm: a navigator where a learner watches the closest unvisited vertex settle first, its distance final, and the edges relax, until the shortest paths are found. Dijkstra takes O((V + E) log V) with a binary heap. The closest unvisited vertex is settled first, and its distance is final. Relaxing an edge is shown improving the distance to its far end. The priority queue is shown holding the frontier.",
    "inputs": "FIGURES = {'vertices': 10000, 'edges': 30000, 'heap_steps': 14, 'total_steps': 560000, 'time_ms': 1, 'distance_km': 500, 'published_year': 1959, 'queue_max': 10000}\nLABEL = 'a-signature-shortest-path-navigator-design'\n",
    "expected": "count: 8\nlabel: a-signature-shortest-path-navigator-design\nmax: 560000\nmean: 76559.25\nmin: 1\ntotal: 612474\nResult: count=8|label=a-signature-shortest-path-navigator-design|max=560000|mean=76559.25|min=1|total=612474\nRun 1 SHA-256: 3ead1b9fe401b31bcad287a9c1b2f9c213db6b1186f6e91ff0628acba1a29158\nRun 2 SHA-256: 3ead1b9fe401b31bcad287a9c1b2f9c213db6b1186f6e91ff0628acba1a29158\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Spanning Tree Builder",
    "subject": "a Signature spanning tree builder design",
    "description": "The Spanning Tree Builder is a Signature-made design for teaching minimum spanning trees: a builder where a learner adds the cheapest edge that does not form a cycle (Kruskal) or grows the tree by its cheapest edge (Prim), and watches the total stay minimal. Both are greedy and both are correct. Kruskal's edges are added cheapest first, skipping cycles. Prim's tree grows by its cheapest edge. Both are shown reaching the same total.",
    "inputs": "FIGURES = {'cities': 5, 'roads': 10, 'mst_edges': 4, 'mst_cost': 10, 'cheapest_edges': 4, 'kruskal_year': 1956, 'prim_year': 1957, 'algorithms': 2}\nLABEL = 'a-signature-spanning-tree-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-spanning-tree-builder-design\nmax: 1957\nmean: 493.5\nmin: 2\ntotal: 3948\nResult: count=8|label=a-signature-spanning-tree-builder-design|max=1957|mean=493.5|min=2|total=3948\nRun 1 SHA-256: 2c389622c7ed04fafeaacbf83431cd906796beb1fc29ffb25c8b58c21153caee\nRun 2 SHA-256: 2c389622c7ed04fafeaacbf83431cd906796beb1fc29ffb25c8b58c21153caee\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The DP Table Filler",
    "subject": "a Signature dynamic programming table filler design",
    "description": "The DP Table Filler is a Signature-made design for teaching dynamic programming: a filler where a learner watches a table fill cell by cell, each cell computed once from the cells before it, turning exponential recursion into polynomial time. Overlapping subproblems are solved once and stored. The table is shown filling cell by cell. Each cell is computed from the cells before it, once. The naive recursion is shown beside it, with its repeated work.",
    "inputs": "FIGURES = {'fib_n': 50, 'naive_calls': 40730022147, 'naive_seconds': 41, 'dp_steps': 50, 'fib_50': 12586269025, 'knapsack_items': 100, 'knapsack_capacity': 1000, 'knapsack_entries': 100000}\nLABEL = 'a-signature-dynamic-programming-table-filler-design'\n",
    "expected": "count: 8\nlabel: a-signature-dynamic-programming-table-filler-design\nmax: 40730022147\nmean: 6664549051.625\nmin: 41\ntotal: 53316392413\nResult: count=8|label=a-signature-dynamic-programming-table-filler-design|max=40730022147|mean=6664549051.625|min=41|total=53316392413\nRun 1 SHA-256: 79831703fbbd1b61c81e1904a4f08ba797dc7d32a13de5dd9ef637f621617f20\nRun 2 SHA-256: 79831703fbbd1b61c81e1904a4f08ba797dc7d32a13de5dd9ef637f621617f20\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Greedy Choice Tester",
    "subject": "a Signature greedy choice tester design",
    "description": "The Greedy Choice Tester is a Signature-made design for teaching greedy algorithms: a tester where a learner tries greedy rules on a problem and sees which give the optimum and which fail. Greedy works with the greedy-choice property and optimal substructure; without them it fails. Each greedy rule is tried, and the result is compared with optimal. The earliest-finishing rule is shown optimal for activity selection. The earliest-starting rule is shown giving only 2 activities.",
    "inputs": "FIGURES = {'activities': 6, 'greedy_count': 3, 'earliest_start_count': 2, 'symbols': 6, 'huffman_avg_bits': 2.24, 'fixed_bits': 3, 'huffman_year': 1952, 'examples': 3}\nLABEL = 'a-signature-greedy-choice-tester-design'\n",
    "expected": "count: 8\nlabel: a-signature-greedy-choice-tester-design\nmax: 1952\nmean: 247.155\nmin: 2\ntotal: 1977.24\nResult: count=8|label=a-signature-greedy-choice-tester-design|max=1952|mean=247.155|min=2|total=1977.24\nRun 1 SHA-256: 50b8db21cc562ac1fbd0ea0f8dd8d066f8dfbe744cfca45f9a079e5a4ca05fbc\nRun 2 SHA-256: 50b8db21cc562ac1fbd0ea0f8dd8d066f8dfbe744cfca45f9a079e5a4ca05fbc\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Recurrence Solver",
    "subject": "a Signature recurrence solver design",
    "description": "The Recurrence Solver is a Signature-made design for teaching divide and conquer: a solver where a learner enters a recurrence T(n) = a T(n/b) + f(n), and the tool applies the master theorem, showing which case holds and the answer. The master theorem covers the recurrences of divide-and-conquer algorithms. The recurrence is entered, and the case is identified. The answer is shown, with the comparison of f(n) and n^(log_b a). Merge sort, binary search, and Karatsuba are shown as examples.",
    "inputs": "FIGURES = {'merge_a': 2, 'merge_b': 2, 'merge_result': 1, 'karatsuba_a': 3, 'karatsuba_exponent': 1.585, 'digits': 1000, 'karatsuba_ops': 56000, 'schoolbook_ops': 1000000}\nLABEL = 'a-signature-recurrence-solver-design'\n",
    "expected": "count: 8\nlabel: a-signature-recurrence-solver-design\nmax: 1000000\nmean: 132126.1981\nmin: 1\ntotal: 1057009.585\nResult: count=8|label=a-signature-recurrence-solver-design|max=1000000|mean=132126.1981|min=1|total=1057009.585\nRun 1 SHA-256: c604f93936f06b0a378491b285e5600486eedddb8109b8174656c381ffeef775\nRun 2 SHA-256: c604f93936f06b0a378491b285e5600486eedddb8109b8174656c381ffeef775\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Call Stack Visualiser",
    "subject": "a Signature call stack visualiser design",
    "description": "The Call Stack Visualiser is a Signature-made design for teaching recursion: a visualiser where a learner watches the frames pile up as a function calls itself, and unwind as the answers return. Each call pushes a frame; the depth is the number of live calls. Each call is shown pushing a frame. The answers are shown returning and popping the frames. The naive Fibonacci recursion is shown exploding, and the loop shown replacing it.",
    "inputs": "FIGURES = {'factorial': 120, 'stack_depth': 6, 'fib_calls': 40730022147, 'fib_seconds': 41, 'iterative_steps': 50, 'recursion_limit': 1000, 'base_case': 1, 'frames': 6}\nLABEL = 'a-signature-call-stack-visualiser-design'\n",
    "expected": "count: 8\nlabel: a-signature-call-stack-visualiser-design\nmax: 40730022147\nmean: 5091252921.375\nmin: 1\ntotal: 40730023371\nResult: count=8|label=a-signature-call-stack-visualiser-design|max=40730022147|mean=5091252921.375|min=1|total=40730023371\nRun 1 SHA-256: edb3bcf720a8d530c0fa3271bfef9d9829244e5917124d51a0520a4a6bd88503\nRun 2 SHA-256: edb3bcf720a8d530c0fa3271bfef9d9829244e5917124d51a0520a4a6bd88503\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Trie Walker",
    "subject": "a Signature trie walker design",
    "description": "The Trie Walker is a Signature-made design for teaching tries: a walker where a learner types a word letter by letter, and the tool walks the trie, showing the shared prefixes and the words below. A trie stores strings by their shared prefixes, and lookup takes O(m) for a word of length m. Each letter is shown following one edge. The shared prefixes are shown stored once. Autocomplete is shown as the subtree below the typed prefix.",
    "inputs": "FIGURES = {'dictionary_words': 100000, 'word_length': 9, 'trie_steps': 9, 'binary_steps': 17, 'linear_steps': 50000, 'text_length': 1000000, 'kmp_steps': 1000000, 'naive_steps': 4000000}\nLABEL = 'a-signature-trie-walker-design'\n",
    "expected": "count: 8\nlabel: a-signature-trie-walker-design\nmax: 4000000\nmean: 768754.375\nmin: 9\ntotal: 6150035\nResult: count=8|label=a-signature-trie-walker-design|max=4000000|mean=768754.375|min=9|total=6150035\nRun 1 SHA-256: 7de4af3a663427679f2abef18af045c9997018d2f7eccab7023c1c108586f8e2\nRun 2 SHA-256: 7de4af3a663427679f2abef18af045c9997018d2f7eccab7023c1c108586f8e2\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Set Merger",
    "subject": "a Signature set merger design",
    "description": "The Set Merger is a Signature-made design for teaching union-find: a merger where a learner merges sets, and the tool shows the trees flattening by path compression, with each operation taking nearly constant time. Union-find tracks which items are in the same set. Sets are merged, and the trees are shown. Path compression is shown flattening the tree on every find. Kruskal's algorithm is shown using the merger.",
    "inputs": "FIGURES = {'singletons': 1000000, 'unions': 500000, 'operations': 1500000, 'tree_height': 3, 'kruskal_edges': 30000, 'kruskal_unions': 10000, 'inverse_ackermann': 5, 'time_ms': 1}\nLABEL = 'a-signature-set-merger-design'\n",
    "expected": "count: 8\nlabel: a-signature-set-merger-design\nmax: 1500000\nmean: 380001.125\nmin: 1\ntotal: 3040009\nResult: count=8|label=a-signature-set-merger-design|max=1500000|mean=380001.125|min=1|total=3040009\nRun 1 SHA-256: ac667bb925909ec15059c989540e650b0dba9534d3b24a366859341d46a8e370\nRun 2 SHA-256: ac667bb925909ec15059c989540e650b0dba9534d3b24a366859341d46a8e370\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Intractability Map",
    "subject": "a Signature intractability map design",
    "description": "The Intractability Map is a Signature-made design for teaching NP-completeness: a map where a learner places a problem, and the tool shows whether it is in P, in NP, or NP-complete, with the tour counts and the SAT assignments counted. NP-complete problems are the hardest in NP. Problems are placed in P, NP, or NP-complete. The tour count for the travelling salesperson is shown exploding. The P versus NP question is shown open, with its prize.",
    "inputs": "FIGURES = {'cities_20': 20, 'tours_20': 60000000000000000, 'years_20': 1900, 'cities_10': 10, 'tours_10': 181440, 'sat_variables': 100, 'sat_assignments': 1300000000000000000000000000000, 'heuristic_gap_pct': 5}\nLABEL = 'a-signature-intractability-map-design'\n",
    "expected": "count: 8\nlabel: a-signature-intractability-map-design\nmax: 1300000000000000000000000000000\nmean: 1.625000000000075e+29\nmin: 5\ntotal: 1300000000000060000000000183475\nResult: count=8|label=a-signature-intractability-map-design|max=1300000000000000000000000000000|mean=1.625000000000075e+29|min=5|total=1300000000000060000000000183475\nRun 1 SHA-256: dea97be6fe7dd9a4963b1b18fe62c0fec3e28e78975b5cf50222bb63f3ac2bb6\nRun 2 SHA-256: dea97be6fe7dd9a4963b1b18fe62c0fec3e28e78975b5cf50222bb63f3ac2bb6\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Approximation Gauge",
    "subject": "a Signature approximation gauge design",
    "description": "The Approximation Gauge is a Signature-made design for teaching approximation algorithms: a gauge where a learner runs a heuristic, and the tool shows the answer against the optimal, with the guarantee as the worst case and the practical gap as the usual case. An approximation algorithm guarantees a factor of optimal. The heuristic answer is shown against the optimal. The guarantee is shown as the worst case. The practical gap is shown as usually far smaller.",
    "inputs": "FIGURES = {'points': 100, 'set_cover_factor': 4.6, 'optimal_tour_km': 1000, 'heuristic_bound_km': 2000, 'heuristic_practical_km': 1100, 'factor': 2, 'improvement': 1, 'guarantee_year': 1974}\nLABEL = 'a-signature-approximation-gauge-design'\n",
    "expected": "count: 8\nlabel: a-signature-approximation-gauge-design\nmax: 2000\nmean: 772.7\nmin: 1\ntotal: 6181.6\nResult: count=8|label=a-signature-approximation-gauge-design|max=2000|mean=772.7|min=1|total=6181.6\nRun 1 SHA-256: c05a535d800b59be147d2ece86d53f06fc27a46b7df214f5e4be75bd1dfd5549\nRun 2 SHA-256: c05a535d800b59be147d2ece86d53f06fc27a46b7df214f5e4be75bd1dfd5549\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The A* Pathfinder",
    "subject": "a Signature A* pathfinder design",
    "description": "The A* Pathfinder is a Signature-made design for teaching A* search: a pathfinder where a learner watches the frontier expand by f = g + h, with the heuristic guiding the search toward the goal, and the settled count shown against Dijkstra's. A* is optimal with an admissible heuristic. The frontier is shown ordered by f = g + h. The settled count is shown against Dijkstra's 100 cells. A bad heuristic (h = 0) is shown becoming Dijkstra.",
    "inputs": "FIGURES = {'grid_size': 10, 'cells': 100, 'optimal_steps': 18, 'dijkstra_settled': 100, 'astar_settled': 30, 'heuristic_at_start': 18, 'saved_cells': 70, 'directions': 4}\nLABEL = 'a-signature-a-pathfinder-design'\n",
    "expected": "count: 8\nlabel: a-signature-a-pathfinder-design\nmax: 100\nmean: 43.75\nmin: 4\ntotal: 350\nResult: count=8|label=a-signature-a-pathfinder-design|max=100|mean=43.75|min=4|total=350\nRun 1 SHA-256: 7b69ab5ffcd9bd996574b518dcc81fbeeed06d29238d60ed5f5d8942ade2d2f8\nRun 2 SHA-256: 7b69ab5ffcd9bd996574b518dcc81fbeeed06d29238d60ed5f5d8942ade2d2f8\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Algorithms Capstone Console",
    "subject": "a Signature algorithms capstone console design",
    "description": "The Algorithms Capstone Console is a Signature-made design for teaching end-to-end algorithm design: a console where a learner builds a route planner from its parts (graph, Dijkstra, hash table, A*), analyses the running time, and checks the result. A capstone problem uses several tools at once. The console assembles the parts: graph, Dijkstra, hash table, A*. Each part is analysed and checked separately. The assembly is scored as a whole design, with the route stated and checked.",
    "inputs": "FIGURES = {'vertices': 10000, 'edges': 30000, 'dijkstra_steps': 560000, 'time_ms': 1, 'places': 10000, 'load_factor': 0.7, 'distance_km': 500, 'tools': 4}\nLABEL = 'a-signature-algorithms-capstone-console-design'\n",
    "expected": "count: 8\nlabel: a-signature-algorithms-capstone-console-design\nmax: 560000\nmean: 76313.2125\nmin: 0.7\ntotal: 610505.7\nResult: count=8|label=a-signature-algorithms-capstone-console-design|max=560000|mean=76313.2125|min=0.7|total=610505.7\nRun 1 SHA-256: 2e7fb7c67de4d0929ccfdbde36b1c6133b67eea9e1b836a3ca160d94c0725435\nRun 2 SHA-256: 2e7fb7c67de4d0929ccfdbde36b1c6133b67eea9e1b836a3ca160d94c0725435\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Big O notation",
    "url": "https://en.wikipedia.org/wiki/Big_O_notation",
    "establishes": "The reference for a Signature growth chart design in this record."
  },
  {
    "name": "Wikipedia - Time complexity",
    "url": "https://en.wikipedia.org/wiki/Time_complexity",
    "establishes": "The reference for a Signature growth chart design in this record."
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
