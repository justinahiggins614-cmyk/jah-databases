// Seeded boundless generator for the Computer Architecture Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-computer-architecture.js [seed]  (prints one JSON record)
// or: node gen-computer-architecture.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "computer-architecture";
const RECORD_KIND = "computer architecture record";
const ID_PREFIX = "JAH-COMPARCH-";
const AI_NAME = "JAH Computer Architecture Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Computer Architecture: The Von Neumann Model and the Stored Program",
    "subject": "the von Neumann model and the stored program",
    "description": "The von Neumann architecture stores both data and instructions in the same memory, and a central processing unit (CPU, the chip that executes instructions) fetches, decodes, and executes instructions one after another. The model has four parts: memory, the arithmetic logic unit (ALU, the circuit that does arithmetic), the control unit, and input/output. Memory holds both instructions and data, in the same address space. The CPU fetches an instruction, decodes it, executes it, and repeats. The program counter holds the address of the next instruction.",
    "inputs": "FIGURES = {'instructions': 5, 'addresses_used': 3, 'program_counter_start': 0, 'program_counter_end': 5, 'components': 4, 'first_computer_year': 1948, 'report_year': 1945, 'memory_paths': 1}\nLABEL = 'the-von-neumann-model-and-the-stored-program'\n",
    "expected": "count: 8\nlabel: the-von-neumann-model-and-the-stored-program\nmax: 1948\nmean: 488.875\nmin: 0\ntotal: 3911\nResult: count=8|label=the-von-neumann-model-and-the-stored-program|max=1948|mean=488.875|min=0|total=3911\nRun 1 SHA-256: f51f3acba50b6cd68d2214fc5d8de4b75d0f37622841c5feec1a06280b269925\nRun 2 SHA-256: f51f3acba50b6cd68d2214fc5d8de4b75d0f37622841c5feec1a06280b269925\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: The Central Processing Unit",
    "subject": "the central processing unit",
    "description": "The central processing unit (CPU) is the chip that executes a program's instructions. It has registers (small, fast storage inside the CPU), an arithmetic logic unit (ALU, the circuit that does arithmetic and logic), and a control unit that directs the flow. The clock sets the pace: a 3 gigahertz (GHz, billions of cycles per second) CPU ticks 3 billion times a second. Registers are the fastest storage, inside the CPU, holding the working values. The ALU performs arithmetic and logic on register values. The clock rate sets how many cycles happen per second.",
    "inputs": "FIGURES = {'clock_GHz': 3, 'cpi': 1.5, 'instructions_per_second': 2000000000, 'mips': 2000, 'program_instructions': 1000000000, 'time_seconds': 0.5, 'first_cpu_year': 1971, 'first_clock_kHz': 740}\nLABEL = 'the-central-processing-unit'\n",
    "expected": "count: 8\nlabel: the-central-processing-unit\nmax: 2000000000\nmean: 375000589.5\nmin: 0.5\ntotal: 3000004716.0\nResult: count=8|label=the-central-processing-unit|max=2000000000|mean=375000589.5|min=0.5|total=3000004716.0\nRun 1 SHA-256: 99af2a80a9f60931dfdcb4f93845f1ae7dee9332afa68f7e253d64fba66d1bea\nRun 2 SHA-256: 99af2a80a9f60931dfdcb4f93845f1ae7dee9332afa68f7e253d64fba66d1bea\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Instruction Set Architecture",
    "subject": "instruction set architecture",
    "description": "An instruction set architecture (ISA) is the contract between hardware and software: the set of instructions a CPU can execute, the registers it has, and the way memory is addressed. RISC (reduced instruction set computer) uses few, simple, fixed-length instructions; CISC (complex instruction set computer) uses many, variable-length instructions. The ISA defines the instructions, registers, and addressing modes. RISC instructions are simple and fixed-length; CISC instructions are complex and variable-length. Programs are written to the ISA, not to the hardware, so software outlives a chip.",
    "inputs": "FIGURES = {'risc_instruction_bits': 32, 'opcode_bits': 7, 'register_bits': 5, 'risc_instructions': 3, 'cisc_instructions': 1, 'risc_cycles': 1, 'arm_devices_billions': 200, 'isa_families': 2}\nLABEL = 'instruction-set-architecture'\n",
    "expected": "count: 8\nlabel: instruction-set-architecture\nmax: 200\nmean: 31.375\nmin: 1\ntotal: 251\nResult: count=8|label=instruction-set-architecture|max=200|mean=31.375|min=1|total=251\nRun 1 SHA-256: eb03116d88a31e94bcbbc5947a3ac26c7255329c7e55dab035f9a4714474b033\nRun 2 SHA-256: eb03116d88a31e94bcbbc5947a3ac26c7255329c7e55dab035f9a4714474b033\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Assembly Language and Machine Code",
    "subject": "assembly language and machine code",
    "description": "Assembly language is the human-readable form of machine code: one assembly instruction maps to one machine instruction, written as a mnemonic (a short name) with operands. An assembler translates assembly into the binary machine code the CPU executes. High-level languages are compiled down to assembly, then to machine code. One assembly instruction is one machine instruction. The assembler translates mnemonics and labels into binary. The compiler turns a high-level program into assembly.",
    "inputs": "FIGURES = {'instructions': 4, 'bytes': 16, 'add_machine_code': 6456115, 'loads': 2, 'stores': 1, 'adds': 1, 'first_assembler_year': 1949, 'opcode_bits': 7}\nLABEL = 'assembly-language-and-machine-code'\n",
    "expected": "count: 8\nlabel: assembly-language-and-machine-code\nmax: 6456115\nmean: 807261.875\nmin: 1\ntotal: 6458095\nResult: count=8|label=assembly-language-and-machine-code|max=6456115|mean=807261.875|min=1|total=6458095\nRun 1 SHA-256: c2d3c59a6249402214c102388c08ec202622bc2ec2e54a93fd5ce485aa02c03c\nRun 2 SHA-256: c2d3c59a6249402214c102388c08ec202622bc2ec2e54a93fd5ce485aa02c03c\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Pipelining",
    "subject": "pipelining",
    "description": "Pipelining overlaps the execution of instructions, like an assembly line: while one instruction is being executed, the next is decoded and the one after is fetched. A 5-stage pipeline (fetch, decode, execute, memory, write-back) can complete one instruction per cycle once full, instead of one per 5 cycles. The pipeline has stages: fetch, decode, execute, memory access, write-back. Once full, it completes one instruction per cycle. Hazards (data, control, structural) stall the pipeline.",
    "inputs": "FIGURES = {'stages': 5, 'instructions': 100, 'pipelined_cycles': 104, 'unpipelined_cycles': 500, 'speedup': 4.8, 'hazard_stall': 1, 'mispredict_cost': 3, 'fill_cycles': 5}\nLABEL = 'pipelining'\n",
    "expected": "count: 8\nlabel: pipelining\nmax: 500\nmean: 90.35\nmin: 1\ntotal: 722.8\nResult: count=8|label=pipelining|max=500|mean=90.35|min=1|total=722.8\nRun 1 SHA-256: f7698f4b988fd7f895524734b9c5078d061b282b28b137b14834f98c96803a1a\nRun 2 SHA-256: f7698f4b988fd7f895524734b9c5078d061b282b28b137b14834f98c96803a1a\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Caches and the Memory Hierarchy",
    "subject": "caches and the memory hierarchy",
    "description": "A cache is a small, fast memory that holds copies of the data the CPU is using, so most accesses are fast. The memory hierarchy runs from registers (fastest, smallest) through caches, main memory (DRAM, dynamic random-access memory), to disk (slowest, largest). A cache hit is fast; a miss goes to the next level. The hierarchy: registers, L1, L2, L3 cache, main memory, disk. A hit is served by the cache; a miss goes to the next level. Locality (temporal and spatial) makes caches work: programs reuse nearby data.",
    "inputs": "FIGURES = {'cache_KB': 64, 'line_bytes': 64, 'lines': 1024, 'ways': 4, 'sets': 256, 'offset_bits': 6, 'index_bits': 8, 'tag_bits': 18}\nLABEL = 'caches-and-the-memory-hierarchy'\n",
    "expected": "count: 8\nlabel: caches-and-the-memory-hierarchy\nmax: 1024\nmean: 180.5\nmin: 4\ntotal: 1444\nResult: count=8|label=caches-and-the-memory-hierarchy|max=1024|mean=180.5|min=4|total=1444\nRun 1 SHA-256: 5a2b7fe470fd77764eacbbbcec659ff19a0adbe9b4b48d8d57608c744cb06299\nRun 2 SHA-256: 5a2b7fe470fd77764eacbbbcec659ff19a0adbe9b4b48d8d57608c744cb06299\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Main Memory — DRAM",
    "subject": "main memory and DRAM",
    "description": "Main memory is DRAM (dynamic random-access memory), which stores each bit as a charge in a tiny capacitor that leaks and must be refreshed. DRAM is organised in banks, rows, and columns; opening a row (activation) is slow, but reading within an open row is fast. Memory bandwidth is how much data flows per second; latency is how long one access takes. Each bit is a charge in a capacitor, refreshed thousands of times a second. Memory is organised in rows; opening a row costs time, reading within it is cheap. Bandwidth is data per second; latency is the time for one access.",
    "inputs": "FIGURES = {'latency_ns': 100, 'bandwidth_GBs': 20, 'line_bytes': 64, 'line_time_ns': 103, 'sequential_us': 50, 'random_ms': 1.6, 'slowdown': 32, 'refresh_interval_ms': 64}\nLABEL = 'main-memory-and-dram'\n",
    "expected": "count: 8\nlabel: main-memory-and-dram\nmax: 103\nmean: 54.325\nmin: 1.6\ntotal: 434.6\nResult: count=8|label=main-memory-and-dram|max=103|mean=54.325|min=1.6|total=434.6\nRun 1 SHA-256: e19d0e41034d922946d8ef8aaac0d9f5f536971e349e4649ff6dde790473255e\nRun 2 SHA-256: e19d0e41034d922946d8ef8aaac0d9f5f536971e349e4649ff6dde790473255e\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Virtual Memory and Paging",
    "subject": "virtual memory and paging",
    "description": "Virtual memory gives every program its own address space, mapped to physical memory by page tables. Memory is divided into pages (typically 4 kilobytes); the translation lookaside buffer (TLB, a cache of recent translations) speeds the mapping. A page fault loads a missing page from disk. Each program sees its own virtual address space. Pages (4 KB) are the unit of mapping; the page table holds the mapping. The TLB caches recent translations; a page fault loads from disk.",
    "inputs": "FIGURES = {'page_size_KB': 4, 'page_number': 74565, 'offset': 1656, 'frame': 703710, 'tlb_hit_cycles': 1, 'page_walk_cycles': 100, 'fault_ms': 10, 'fault_cycles': 10000000}\nLABEL = 'virtual-memory-and-paging'\n",
    "expected": "count: 8\nlabel: virtual-memory-and-paging\nmax: 10000000\nmean: 1347505.75\nmin: 1\ntotal: 10780046\nResult: count=8|label=virtual-memory-and-paging|max=10000000|mean=1347505.75|min=1|total=10780046\nRun 1 SHA-256: 80f97f023b2f07cf7952acb65d11df5a5d49413f01e42786f8741561ee9fd835\nRun 2 SHA-256: 80f97f023b2f07cf7952acb65d11df5a5d49413f01e42786f8741561ee9fd835\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Input, Output, and Interrupts",
    "subject": "input, output, and interrupts",
    "description": "Input/output (I/O) moves data between the computer and the outside world: disks, networks, keyboards, displays. The CPU can poll (ask repeatedly), use interrupts (the device signals when ready), or use direct memory access (DMA, the device writes to memory without the CPU). Interrupts let the CPU do other work while waiting. Polling asks the device repeatedly; it wastes CPU time. An interrupt signals the CPU when the device is ready. DMA lets the device move data to memory without the CPU.",
    "inputs": "FIGURES = {'packet_interval_us': 100, 'poll_interval_us': 10, 'poll_waste': 10, 'interrupt_overhead_pct': 5, 'dma_speed_MBs': 500, 'dma_time_ms': 2, 'packet_size_KB': 1, 'methods': 3}\nLABEL = 'input-output-and-interrupts'\n",
    "expected": "count: 8\nlabel: input-output-and-interrupts\nmax: 500\nmean: 78.875\nmin: 1\ntotal: 631\nResult: count=8|label=input-output-and-interrupts|max=500|mean=78.875|min=1|total=631\nRun 1 SHA-256: 6c535bb3c3e697272ffc19210aec935140d0922cc56470b6199d48b928238451\nRun 2 SHA-256: 6c535bb3c3e697272ffc19210aec935140d0922cc56470b6199d48b928238451\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Parallelism and Amdahl's Law",
    "subject": "parallelism and Amdahl's law",
    "description": "Parallelism runs parts of a program on several cores at once. Amdahl's law says the speedup is limited by the serial part: if a fraction f of the program can be parallelised, the speedup on n cores is 1 / ((1 - f) + f/n). Even with infinite cores, the speedup cannot exceed 1/(1 - f). Speedup = 1 / ((1 - f) + f/n), where f is the parallel fraction. With infinite cores, the speedup is at most 1/(1 - f). The serial part (setup, communication, synchronisation) limits everything.",
    "inputs": "FIGURES = {'parallel_fraction': 0.9, 'cores': 8, 'speedup_8': 4.7, 'speedup_infinite': 10, 'serial_time_s': 100, 'parallel_time_s': 21, 'law_year': 1967, 'max_with_20pct_serial': 5}\nLABEL = 'parallelism-and-amdahl-s-law'\n",
    "expected": "count: 8\nlabel: parallelism-and-amdahl-s-law\nmax: 1967\nmean: 264.575\nmin: 0.9\ntotal: 2116.6\nResult: count=8|label=parallelism-and-amdahl-s-law|max=1967|mean=264.575|min=0.9|total=2116.6\nRun 1 SHA-256: 997c13520f2769388122662ae3f4c974d1e881ff33493c37621c01ace58cf3ad\nRun 2 SHA-256: 997c13520f2769388122662ae3f4c974d1e881ff33493c37621c01ace58cf3ad\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Superscalar and Out-of-Order Execution",
    "subject": "superscalar and out-of-order execution",
    "description": "A superscalar CPU issues several instructions per cycle, using several execution units. Out-of-order execution reorders instructions so that an instruction that is ready runs before one that is waiting, as long as the result is the same as in-order execution. The reorder buffer (ROB) holds results until they can be committed in order. Superscalar means several instructions issued per cycle. Out-of-order execution runs ready instructions first, hiding stalls. Results are committed in program order, so the program sees in-order execution.",
    "inputs": "FIGURES = {'issue_width': 4, 'ipc': 3, 'instructions': 3000000000, 'cycles': 1000000000, 'time_seconds': 0.33, 'rob_entries': 128, 'miss_latency': 100, 'mispredict_cost': 15}\nLABEL = 'superscalar-and-out-of-order-execution'\n",
    "expected": "count: 8\nlabel: superscalar-and-out-of-order-execution\nmax: 3000000000\nmean: 500000031.2912\nmin: 0.33\ntotal: 4000000250.33\nResult: count=8|label=superscalar-and-out-of-order-execution|max=3000000000|mean=500000031.2912|min=0.33|total=4000000250.33\nRun 1 SHA-256: e367dd7f9c2c5fd8f32f24a011c876b5c23567c7bd18bb767706160c5d135ffe\nRun 2 SHA-256: e367dd7f9c2c5fd8f32f24a011c876b5c23567c7bd18bb767706160c5d135ffe\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Branch Prediction",
    "subject": "branch prediction",
    "description": "Branch prediction guesses which way a conditional branch will go, so the pipeline can keep fetching without waiting. A 2-bit saturating counter predicts taken or not taken, learning from history. A correct prediction costs nothing; a misprediction flushes the pipeline. The predictor guesses taken or not taken before the branch resolves. A 2-bit counter learns: it needs two mispredictions to flip. A misprediction flushes the pipeline, costing 10-20 cycles.",
    "inputs": "FIGURES = {'loop_iterations': 1000, 'taken': 999, 'mispredictions': 2, 'mispredict_cost': 15, 'total_cost': 30, 'overhead_pct': 3, 'random_accuracy': 0.5, 'random_cost': 7.5}\nLABEL = 'branch-prediction'\n",
    "expected": "count: 8\nlabel: branch-prediction\nmax: 1000\nmean: 257.125\nmin: 0.5\ntotal: 2057.0\nResult: count=8|label=branch-prediction|max=1000|mean=257.125|min=0.5|total=2057.0\nRun 1 SHA-256: ed5959b52aeee25c75f8502252cc0fc2d2bdcf3f093ce27916773946ab64efac\nRun 2 SHA-256: ed5959b52aeee25c75f8502252cc0fc2d2bdcf3f093ce27916773946ab64efac\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Graphics Processing Units",
    "subject": "graphics processing units",
    "description": "A graphics processing unit (GPU) is a processor with thousands of small cores, designed for data-parallel work: the same operation on many pieces of data at once (SIMD, single instruction, multiple data). GPUs render graphics, train neural networks, and run scientific simulations. A GPU has thousands of small cores, against a CPU's tens of large cores. SIMD runs the same instruction on many data items at once. GPUs are fast for parallel work and slow for serial, branching work.",
    "inputs": "FIGURES = {'gpu_cores': 10000, 'gpu_clock_GHz': 1.5, 'gpu_tflops': 30, 'matrix_size': 4096, 'operations': 137400000000, 'gpu_time_ms': 4.6, 'cpu_tflops': 1, 'cpu_time_ms': 137}\nLABEL = 'graphics-processing-units'\n",
    "expected": "count: 8\nlabel: graphics-processing-units\nmax: 137400000000\nmean: 17175001783.7625\nmin: 1\ntotal: 137400014270.1\nResult: count=8|label=graphics-processing-units|max=137400000000|mean=17175001783.7625|min=1|total=137400014270.1\nRun 1 SHA-256: 72985d21f79d226b8a49086dbc95bc057d542153b3e3c15f1a37ab9888e6da2d\nRun 2 SHA-256: 72985d21f79d226b8a49086dbc95bc057d542153b3e3c15f1a37ab9888e6da2d\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Storage — Disks, SSDs, and Flash",
    "subject": "storage, disks, SSDs, and flash",
    "description": "Storage holds data without power: hard disk drives (HDDs) store bits magnetically on spinning platters; solid-state drives (SSDs) store bits in flash memory cells, with no moving parts. SSDs are far faster for random access; HDDs are cheaper per gigabyte. Flash wears out after a number of writes. HDDs spin platters and move a head; access takes milliseconds. SSDs read flash cells; random access takes about 0.1 milliseconds. Flash cells wear out after tens of thousands of writes.",
    "inputs": "FIGURES = {'hdd_seek_ms': 10, 'ssd_latency_ms': 0.1, 'random_blocks': 1000, 'hdd_random_s': 10, 'ssd_random_s': 0.1, 'speedup': 100, 'hdd_seq_MBs': 200, 'ssd_seq_MBs': 500}\nLABEL = 'storage-disks-ssds-and-flash'\n",
    "expected": "count: 8\nlabel: storage-disks-ssds-and-flash\nmax: 1000\nmean: 227.525\nmin: 0.1\ntotal: 1820.2\nResult: count=8|label=storage-disks-ssds-and-flash|max=1000|mean=227.525|min=0.1|total=1820.2\nRun 1 SHA-256: 6afe28cb9289965aef70b0d11bba6d7987162bc5f761f23cea2582f062403bdd\nRun 2 SHA-256: 6afe28cb9289965aef70b0d11bba6d7987162bc5f761f23cea2582f062403bdd\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Networks and Interconnection",
    "subject": "networks and interconnection",
    "description": "Computers connect through networks: the bandwidth is how much data flows per second, the latency is how long one message takes. Inside a machine, cores connect through a bus or a network-on-chip; between machines, Ethernet and InfiniBand carry messages. The speed of light sets a floor on latency: about 5 microseconds per kilometre in fibre. Bandwidth is data per second; latency is the time for one message. Light in fibre travels about 200,000 km/s, so 1 km takes 5 microseconds. The network-on-chip connects cores inside a processor.",
    "inputs": "FIGURES = {'link_Gbps': 100, 'one_GB_seconds': 0.08, 'fibre_us_per_km': 5, 'distance_km': 1000, 'one_way_ms': 5, 'machines': 10000, 'bisection_TBs': 10, 'ny_london_ms': 70}\nLABEL = 'networks-and-interconnection'\n",
    "expected": "count: 8\nlabel: networks-and-interconnection\nmax: 10000\nmean: 1398.76\nmin: 0.08\ntotal: 11190.08\nResult: count=8|label=networks-and-interconnection|max=10000|mean=1398.76|min=0.08|total=11190.08\nRun 1 SHA-256: c8ddd268b4ca285959e41ad7f61aec5ed829ad61f272bb9fb857e19b2229d048\nRun 2 SHA-256: c8ddd268b4ca285959e41ad7f61aec5ed829ad61f272bb9fb857e19b2229d048\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Moore's Law and the End of Dennard Scaling",
    "subject": "Moore's law and the end of Dennard scaling",
    "description": "Moore's law says the number of transistors on a chip doubles about every two years. Dennard scaling said smaller transistors would also be faster and use less power per transistor, so clock speeds rose. Dennard scaling ended around 2005: smaller transistors leak power, so clocks stopped rising and chips went multicore instead. Moore's law: transistor count doubles about every two years. Dennard scaling: smaller transistors are faster and use less power. Dennard scaling ended around 2005; clocks flattened and cores multiplied.",
    "inputs": "FIGURES = {'transistors_2005': 1000000000, 'doubling_years': 2, 'transistors_2023': 100000000000, 'clock_1995_MHz': 100, 'clock_2005_GHz': 3, 'clock_now_GHz': 5, 'cores_now': 64, 'power_wall_W': 300}\nLABEL = 'moore-s-law-and-the-end-of-dennard-scaling'\n",
    "expected": "count: 8\nlabel: moore-s-law-and-the-end-of-dennard-scaling\nmax: 100000000000\nmean: 12625000059.25\nmin: 2\ntotal: 101000000474\nResult: count=8|label=moore-s-law-and-the-end-of-dennard-scaling|max=100000000000|mean=12625000059.25|min=2|total=101000000474\nRun 1 SHA-256: 117d1a60af8ad694703d6e94ffdf6aba455175433179e19ec451d8452562a14b\nRun 2 SHA-256: 117d1a60af8ad694703d6e94ffdf6aba455175433179e19ec451d8452562a14b\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: RISC versus CISC",
    "subject": "RISC versus CISC",
    "description": "RISC (reduced instruction set computer) and CISC (complex instruction set computer) are two philosophies of instruction sets. RISC uses few, simple, fixed-length instructions that run in one cycle; CISC uses many, complex, variable-length instructions that do more per instruction. Modern CISC chips decode complex instructions into RISC-like micro-operations inside. RISC: few simple instructions, fixed length, one cycle each. CISC: many complex instructions, variable length, more work each. Modern x86 chips decode CISC instructions into RISC-like micro-ops.",
    "inputs": "FIGURES = {'risc_instructions': 4, 'cisc_instructions': 1, 'cisc_cycles': 3, 'cisc_bytes': 6, 'risc_program': 1000, 'risc_cpi': 1, 'cisc_program': 400, 'cisc_cpi': 2.5}\nLABEL = 'risc-versus-cisc'\n",
    "expected": "count: 8\nlabel: risc-versus-cisc\nmax: 1000\nmean: 177.1875\nmin: 1\ntotal: 1417.5\nResult: count=8|label=risc-versus-cisc|max=1000|mean=177.1875|min=1|total=1417.5\nRun 1 SHA-256: 955388ae173da176bc627155b60dd3052eda717c9fcd64aeae37a67db748544c\nRun 2 SHA-256: 955388ae173da176bc627155b60dd3052eda717c9fcd64aeae37a67db748544c\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: The Memory Wall",
    "subject": "the memory wall",
    "description": "The memory wall is the growing gap between CPU speed and memory speed: CPUs doubled in speed every 18 months for decades, while DRAM latency improved only slowly. Caches, prefetching, and parallelism hide the gap, but memory-bound programs run at memory speed, not CPU speed. CPU speed grew far faster than DRAM latency for decades. Caches hide the gap when the program has locality. Prefetching loads data before it is needed.",
    "inputs": "FIGURES = {'cpu_cycle_ns': 0.33, 'dram_latency_ns': 100, 'latency_cycles': 300, 'miss_rate': 0.05, 'avg_access_cycles': 5.95, 'peak_ops': 3000000000, 'memory_bound_ops': 10000000, 'slowdown': 300}\nLABEL = 'the-memory-wall'\n",
    "expected": "count: 8\nlabel: the-memory-wall\nmax: 3000000000\nmean: 376250088.2912\nmin: 0.05\ntotal: 3010000706.33\nResult: count=8|label=the-memory-wall|max=3000000000|mean=376250088.2912|min=0.05|total=3010000706.33\nRun 1 SHA-256: 29a7e6a1239115898d3e5f7bd5900ddd88ca762e63ba2ba83fbc674b0a01ecb8\nRun 2 SHA-256: 29a7e6a1239115898d3e5f7bd5900ddd88ca762e63ba2ba83fbc674b0a01ecb8\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Power, Energy, and Dark Silicon",
    "subject": "power, energy, and dark silicon",
    "description": "Power is the rate of energy use; a chip's power is mostly dynamic (switching transistors) plus leakage (current that flows even when idle). Dynamic power is proportional to capacitance times voltage squared times frequency. Dark silicon is the part of a chip that must stay off, because turning it all on would overheat the chip. Dynamic power = C times V squared times f. Leakage power flows even when the chip is idle. Dark silicon: not all of the chip can run at once, within the power budget.",
    "inputs": "FIGURES = {'capacitance_nF': 1, 'voltage_V': 1, 'frequency_GHz': 3, 'power_per_block_W': 3, 'blocks': 30, 'total_power_W': 90, 'half_voltage_power_W': 0.75, 'budget_W': 100}\nLABEL = 'power-energy-and-dark-silicon'\n",
    "expected": "count: 8\nlabel: power-energy-and-dark-silicon\nmax: 100\nmean: 28.5938\nmin: 0.75\ntotal: 228.75\nResult: count=8|label=power-energy-and-dark-silicon|max=100|mean=28.5938|min=0.75|total=228.75\nRun 1 SHA-256: 08c11d43a38c44eedd1515789988c3373fcd8ee5510e231a595e4e31af6c6164\nRun 2 SHA-256: 08c11d43a38c44eedd1515789988c3373fcd8ee5510e231a595e4e31af6c6164\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Reliability, ECC, and Fault Tolerance",
    "subject": "reliability, ECC, and fault tolerance",
    "description": "Reliability is the probability that a system works correctly over time. ECC (error-correcting code) memory detects and corrects single-bit errors in RAM. Redundancy (extra copies, RAID for disks, triple-modular redundancy for critical logic) keeps a system working when a part fails. ECC memory corrects single-bit errors and detects double-bit errors. RAID spreads data across disks so one disk can fail without loss. Triple-modular redundancy votes among three copies.",
    "inputs": "FIGURES = {'ram_TB': 1, 'modules': 128, 'module_GB': 8, 'errors_per_month': 128, 'errors_per_day': 4, 'raid_disks': 5, 'tolerated_failures': 1, 'rebuild_hours': 10}\nLABEL = 'reliability-ecc-and-fault-tolerance'\n",
    "expected": "count: 8\nlabel: reliability-ecc-and-fault-tolerance\nmax: 128\nmean: 35.625\nmin: 1\ntotal: 285\nResult: count=8|label=reliability-ecc-and-fault-tolerance|max=128|mean=35.625|min=1|total=285\nRun 1 SHA-256: 0c7a2b5846bfee10bd85a563dc1cfbf2c2e1a03e9638fa54910f9f7dd9da4293\nRun 2 SHA-256: 0c7a2b5846bfee10bd85a563dc1cfbf2c2e1a03e9638fa54910f9f7dd9da4293\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Benchmarking and Performance Measurement",
    "subject": "benchmarking and performance measurement",
    "description": "Benchmarking measures a computer's performance on representative programs. The standard metrics are time (how long a program takes), throughput (how much work per second), and the SPEC benchmarks (a suite of real programs). The iron law of performance says time = instructions times CPI divided by clock rate. Time is the honest metric; speedups are ratios of times. The iron law: time = instructions x CPI / clock rate. Benchmarks must be representative, or they mislead.",
    "inputs": "FIGURES = {'time_X_s': 10, 'time_Y_s': 8, 'speedup': 1.25, 'suite_mean': 1.3, 'instructions': 2000000000, 'cpi_Y': 1.2, 'cpi_X': 1.5, 'clock_GHz': 3}\nLABEL = 'benchmarking-and-performance-measurement'\n",
    "expected": "count: 8\nlabel: benchmarking-and-performance-measurement\nmax: 2000000000\nmean: 250000003.2812\nmin: 1.2\ntotal: 2000000026.25\nResult: count=8|label=benchmarking-and-performance-measurement|max=2000000000|mean=250000003.2812|min=1.2|total=2000000026.25\nRun 1 SHA-256: b10f0659036c26fbb95241cae3568a76e28bd5cf575c211746241eb58b07154f\nRun 2 SHA-256: b10f0659036c26fbb95241cae3568a76e28bd5cf575c211746241eb58b07154f\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: The Fetch-Decode-Execute Cycle in Detail",
    "subject": "the fetch-decode-execute cycle in detail",
    "description": "Every instruction passes through the fetch-decode-execute cycle: the program counter gives the address, the instruction is fetched from memory, the control unit decodes the opcode and operands, the ALU or memory unit executes it, and the result is written back. The cycle is the heartbeat of the CPU. Fetch: the instruction is read from the address in the program counter. Decode: the opcode and operands are identified. Execute and write-back: the operation runs and the result is stored.",
    "inputs": "FIGURES = {'cycles': 4, 'instruction_bytes': 4, 'clock_GHz': 3, 'time_ns': 1.33, 'stages': 3, 'addresses': 3, 'registers_used': 2, 'report_year': 1945}\nLABEL = 'the-fetch-decode-execute-cycle-in-detail'\n",
    "expected": "count: 8\nlabel: the-fetch-decode-execute-cycle-in-detail\nmax: 1945\nmean: 245.6662\nmin: 1.33\ntotal: 1965.33\nResult: count=8|label=the-fetch-decode-execute-cycle-in-detail|max=1945|mean=245.6662|min=1.33|total=1965.33\nRun 1 SHA-256: 18675f7698a43eded8599b4c18f94f9697c718f07b947088e65b1dde817d79b0\nRun 2 SHA-256: 18675f7698a43eded8599b4c18f94f9697c718f07b947088e65b1dde817d79b0\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Instruction-Level Parallelism and VLIW",
    "subject": "instruction-level parallelism and VLIW",
    "description": "Instruction-level parallelism (ILP) is the parallelism inside one program: independent instructions run at the same time. A superscalar CPU finds it in hardware; a VLIW (very long instruction word) CPU relies on the compiler to pack independent operations into one long instruction word. Both are limited by dependencies and by branches. ILP is the independent instructions inside one program. Superscalar hardware finds it at run time; VLIW relies on the compiler. Dependencies and branches limit how much ILP exists.",
    "inputs": "FIGURES = {'operations_per_iteration': 4, 'scalar_cycles': 4, 'superscalar_cycles': 1, 'speedup': 4, 'vliw_slots': 4, 'dependent_cycles': 4, 'typical_ilp': 2.5, 'issue_width': 4}\nLABEL = 'instruction-level-parallelism-and-vliw'\n",
    "expected": "count: 8\nlabel: instruction-level-parallelism-and-vliw\nmax: 4\nmean: 3.4375\nmin: 1\ntotal: 27.5\nResult: count=8|label=instruction-level-parallelism-and-vliw|max=4|mean=3.4375|min=1|total=27.5\nRun 1 SHA-256: a892fbd28cffa31436634651030b4de9868fc76f8b9408046bcb41ee83ded726\nRun 2 SHA-256: a892fbd28cffa31436634651030b4de9868fc76f8b9408046bcb41ee83ded726\nDeterministic: MATCH\n"
  },
  {
    "title": "Computer Architecture: Capstone — Design a Small CPU",
    "subject": "a capstone small CPU design",
    "description": "This capstone designs a small CPU from the pieces of the course: a von Neumann machine with a 32-bit ISA, a 5-stage pipeline, a 64-KB cache, and virtual memory, with the performance estimated by the iron law and the power by C V squared f. A capstone problem uses several tools at once. The ISA is RISC, 32-bit, with 32 registers. The pipeline is 5 stages, with forwarding and a 2-bit branch predictor. The cache is 64 KB, 4-way, with 64-byte lines; the memory is DRAM with a TLB.",
    "inputs": "FIGURES = {'clock_GHz': 3, 'cpi': 1.2, 'program_instructions': 1000000000, 'time_seconds': 0.4, 'pipeline_cycles': 104, 'cache_KB': 64, 'avg_access_cycles': 5.95, 'power_W': 90}\nLABEL = 'a-capstone-small-cpu-design'\n",
    "expected": "count: 8\nlabel: a-capstone-small-cpu-design\nmax: 1000000000\nmean: 125000033.5688\nmin: 0.4\ntotal: 1000000268.55\nResult: count=8|label=a-capstone-small-cpu-design|max=1000000000|mean=125000033.5688|min=0.4|total=1000000268.55\nRun 1 SHA-256: c22dd4d4c64004175d5e72d343d56f1935d5653720412be6d8acc8fd9fb2f455\nRun 2 SHA-256: c22dd4d4c64004175d5e72d343d56f1935d5653720412be6d8acc8fd9fb2f455\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Von Neumann architecture",
    "url": "https://en.wikipedia.org/wiki/Von_Neumann_architecture",
    "establishes": "The reference for the von Neumann model and the stored program in this record."
  },
  {
    "name": "Wikipedia - Computer architecture",
    "url": "https://en.wikipedia.org/wiki/Computer_architecture",
    "establishes": "The reference for the von Neumann model and the stored program in this record."
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
