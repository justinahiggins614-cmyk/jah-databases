// Seeded boundless generator for the The Signature Computer Architecture Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-computer-architecture-signature.js [seed]  (prints one JSON record)
// or: node gen-computer-architecture-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "computer-architecture-signature";
const RECORD_KIND = "computer architecture record";
const ID_PREFIX = "JAH-COMPARCHS-";
const AI_NAME = "JAH Computer Architecture Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Stored-Program Workbench",
    "subject": "a Signature stored-program workbench design",
    "description": "The Stored-Program Workbench is a Signature-made design for teaching the von Neumann model: a workbench where a learner writes a tiny program, and the tool steps through the fetch-decode-execute cycle, showing the program counter, the instruction, and the memory changing. The stored program means instructions and data share one memory. The program counter, the fetched instruction, and the memory are shown at each step. Each cycle is shown: fetch, decode, execute, and the counter advancing. The von Neumann bottleneck is shown as the single memory path.",
    "inputs": "FIGURES = {'instructions': 5, 'addresses_used': 3, 'program_counter_start': 0, 'program_counter_end': 5, 'components': 4, 'cycles': 5, 'memory_paths': 1, 'design_version': 1}\nLABEL = 'a-signature-stored-program-workbench-design'\n",
    "expected": "count: 8\nlabel: a-signature-stored-program-workbench-design\nmax: 5\nmean: 3.0\nmin: 0\ntotal: 24\nResult: count=8|label=a-signature-stored-program-workbench-design|max=5|mean=3.0|min=0|total=24\nRun 1 SHA-256: 564a81045fd01e33133ed69efc4cdc009ddced8e78193149bcaf3f2a59f3efad\nRun 2 SHA-256: 564a81045fd01e33133ed69efc4cdc009ddced8e78193149bcaf3f2a59f3efad\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The CPU Speed Calculator",
    "subject": "a Signature CPU speed calculator design",
    "description": "The CPU Speed Calculator is a Signature-made design for teaching CPU performance: a calculator where a learner sets the clock rate, the cycles per instruction, and the instruction count, and the tool gives the time, the instructions per second, and the MIPS. Time is instructions times CPI divided by clock rate. The clock, CPI, and instruction count are set on sliders. The time, the instructions per second, and the MIPS are shown. Doubling the clock is shown halving the time, if the CPI stays the same.",
    "inputs": "FIGURES = {'clock_GHz': 3, 'cpi': 1.5, 'instructions_per_second': 2000000000, 'mips': 2000, 'program_instructions': 1000000000, 'time_seconds': 0.5, 'doubled_clock_GHz': 6, 'halved_time_s': 0.25}\nLABEL = 'a-signature-cpu-speed-calculator-design'\n",
    "expected": "count: 8\nlabel: a-signature-cpu-speed-calculator-design\nmax: 2000000000\nmean: 375000251.4062\nmin: 0.25\ntotal: 3000002011.25\nResult: count=8|label=a-signature-cpu-speed-calculator-design|max=2000000000|mean=375000251.4062|min=0.25|total=3000002011.25\nRun 1 SHA-256: 3ebbfe8971ea462ad34fd7736e9d58b2685d244db5c747097a2be40fe40e2cdc\nRun 2 SHA-256: 3ebbfe8971ea462ad34fd7736e9d58b2685d244db5c747097a2be40fe40e2cdc\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The ISA Decoder",
    "subject": "a Signature instruction set decoder design",
    "description": "The ISA Decoder is a Signature-made design for teaching instruction sets: a decoder where a learner enters a 32-bit instruction, and the tool splits it into opcode, registers, and function, showing what the instruction does. An ISA is the contract between hardware and software. The 32 bits are split into their fields and labelled. Each field is explained: opcode, source registers, destination, function. RISC and CISC instructions are compared side by side.",
    "inputs": "FIGURES = {'risc_instruction_bits': 32, 'opcode_bits': 7, 'register_bits': 5, 'function_bits': 3, 'fields': 5, 'risc_instructions': 3, 'cisc_instructions': 1, 'design_version': 1}\nLABEL = 'a-signature-instruction-set-decoder-design'\n",
    "expected": "count: 8\nlabel: a-signature-instruction-set-decoder-design\nmax: 32\nmean: 7.125\nmin: 1\ntotal: 57\nResult: count=8|label=a-signature-instruction-set-decoder-design|max=32|mean=7.125|min=1|total=57\nRun 1 SHA-256: 755576ac63e4e0f7994f2850ed77c8f921f48918de5d4db393f235c76666eeea\nRun 2 SHA-256: 755576ac63e4e0f7994f2850ed77c8f921f48918de5d4db393f235c76666eeea\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Assembler Studio",
    "subject": "a Signature assembler studio design",
    "description": "The Assembler Studio is a Signature-made design for teaching assembly language: a studio where a learner writes assembly, and the tool assembles it to machine code, showing each instruction's binary and hexadecimal form. One assembly instruction is one machine instruction. Assembly is written, and the machine code appears beside it. Each instruction's binary and hexadecimal forms are shown. Labels are resolved to addresses, and the sizes are shown.",
    "inputs": "FIGURES = {'instructions': 4, 'bytes': 16, 'add_machine_code': 6456115, 'loads': 2, 'stores': 1, 'adds': 1, 'first_assembler_year': 1949, 'design_version': 1}\nLABEL = 'a-signature-assembler-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-assembler-studio-design\nmax: 6456115\nmean: 807261.125\nmin: 1\ntotal: 6458089\nResult: count=8|label=a-signature-assembler-studio-design|max=6456115|mean=807261.125|min=1|total=6458089\nRun 1 SHA-256: 19d70286b7d058d8df26375166e8cbced6b96f3c4d1a94983fcb79d931c4c774\nRun 2 SHA-256: 19d70286b7d058d8df26375166e8cbced6b96f3c4d1a94983fcb79d931c4c774\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Pipeline Assembly Line",
    "subject": "a Signature pipeline assembly line design",
    "description": "The Pipeline Assembly Line is a Signature-made design for teaching pipelining: an assembly line where a learner watches instructions move through the five stages (fetch, decode, execute, memory, write-back), with hazards shown as stalls and forwarding shown as a shortcut. Once full, the line completes one instruction per cycle. Each instruction is shown moving through the five stages. Hazards are shown as stalls, and forwarding as a shortcut. The cycle count is shown against the unpipelined count.",
    "inputs": "FIGURES = {'stages': 5, 'instructions': 100, 'pipelined_cycles': 104, 'unpipelined_cycles': 500, 'speedup': 4.8, 'hazard_stall': 1, 'mispredict_cost': 3, 'design_version': 1}\nLABEL = 'a-signature-pipeline-assembly-line-design'\n",
    "expected": "count: 8\nlabel: a-signature-pipeline-assembly-line-design\nmax: 500\nmean: 89.85\nmin: 1\ntotal: 718.8\nResult: count=8|label=a-signature-pipeline-assembly-line-design|max=500|mean=89.85|min=1|total=718.8\nRun 1 SHA-256: a34b98406fbb1cf783a7cbb1e95523606c9b8e602c82416690a8c3594c857dbe\nRun 2 SHA-256: a34b98406fbb1cf783a7cbb1e95523606c9b8e602c82416690a8c3594c857dbe\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Cache Explorer",
    "subject": "a Signature cache explorer design",
    "description": "The Cache Explorer is a Signature-made design for teaching caches: an explorer where a learner sets the cache size, line size, and associativity, and the tool shows the sets, the tags, and the average access time for a given hit rate. A cache is a small fast memory holding copies of the data in use. The size, line size, and associativity are set, and the sets and tags are computed. The address is split into tag, index, and offset. The average access time is shown for the hit rate.",
    "inputs": "FIGURES = {'cache_KB': 64, 'line_bytes': 64, 'lines': 1024, 'ways': 4, 'sets': 256, 'offset_bits': 6, 'index_bits': 8, 'tag_bits': 18}\nLABEL = 'a-signature-cache-explorer-design'\n",
    "expected": "count: 8\nlabel: a-signature-cache-explorer-design\nmax: 1024\nmean: 180.5\nmin: 4\ntotal: 1444\nResult: count=8|label=a-signature-cache-explorer-design|max=1024|mean=180.5|min=4|total=1444\nRun 1 SHA-256: 5de2f106f76e99bb1ea6b2e763e4391bf11ad45d6153bfd3fec9e2970e21aa65\nRun 2 SHA-256: 5de2f106f76e99bb1ea6b2e763e4391bf11ad45d6153bfd3fec9e2970e21aa65\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The DRAM Row Viewer",
    "subject": "a Signature DRAM row viewer design",
    "description": "The DRAM Row Viewer is a Signature-made design for teaching main memory: a viewer where a learner opens a DRAM row, reads within it, and watches the latency paid once for sequential reads and once per line for random reads. DRAM stores each bit as a charge in a capacitor. A row is opened, and the reads within it are shown. Sequential reads pay the latency once; random reads pay it per line. The bandwidth and the latency are shown separately.",
    "inputs": "FIGURES = {'latency_ns': 100, 'bandwidth_GBs': 20, 'line_bytes': 64, 'line_time_ns': 103, 'sequential_us': 50, 'random_ms': 1.6, 'slowdown': 32, 'refresh_interval_ms': 64}\nLABEL = 'a-signature-dram-row-viewer-design'\n",
    "expected": "count: 8\nlabel: a-signature-dram-row-viewer-design\nmax: 103\nmean: 54.325\nmin: 1.6\ntotal: 434.6\nResult: count=8|label=a-signature-dram-row-viewer-design|max=103|mean=54.325|min=1.6|total=434.6\nRun 1 SHA-256: 5bdce979a25349dfeecd0ac62624d6e89d29b4ebb8b5eeccf0a371f00060e4c9\nRun 2 SHA-256: 5bdce979a25349dfeecd0ac62624d6e89d29b4ebb8b5eeccf0a371f00060e4c9\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Page Table Mapper",
    "subject": "a Signature page table mapper design",
    "description": "The Page Table Mapper is a Signature-made design for teaching virtual memory: a mapper where a learner enters a virtual address, and the tool splits it into page and offset, looks up the frame, and builds the physical address. Virtual memory gives each program its own address space. The virtual address is split into page number and offset. The page table gives the frame; the offset passes through. The TLB hit, the page walk, and the page fault are shown with their costs.",
    "inputs": "FIGURES = {'page_size_KB': 4, 'page_number': 74565, 'offset': 1656, 'frame': 703710, 'tlb_hit_cycles': 1, 'page_walk_cycles': 100, 'fault_ms': 10, 'fault_cycles': 10000000}\nLABEL = 'a-signature-page-table-mapper-design'\n",
    "expected": "count: 8\nlabel: a-signature-page-table-mapper-design\nmax: 10000000\nmean: 1347505.75\nmin: 1\ntotal: 10780046\nResult: count=8|label=a-signature-page-table-mapper-design|max=10000000|mean=1347505.75|min=1|total=10780046\nRun 1 SHA-256: a80e14dfd8181dd8234212f38854a2667304b5555ca4cc911311b9a1155474da\nRun 2 SHA-256: a80e14dfd8181dd8234212f38854a2667304b5555ca4cc911311b9a1155474da\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The I/O Switchboard",
    "subject": "a Signature input/output switchboard design",
    "description": "The I/O Switchboard is a Signature-made design for teaching input and output: a switchboard where a learner chooses polling, interrupts, or DMA (direct memory access) for a device, and the tool shows the CPU time each costs. Interrupts let the CPU work while waiting; DMA removes the CPU from the data path. Polling, interrupts, and DMA are chosen for the same device. The CPU time of each is shown. An interrupt storm is shown starving the CPU.",
    "inputs": "FIGURES = {'packet_interval_us': 100, 'poll_interval_us': 10, 'poll_waste': 10, 'interrupt_overhead_pct': 5, 'dma_speed_MBs': 500, 'dma_time_ms': 2, 'methods': 3, 'design_version': 1}\nLABEL = 'a-signature-input-output-switchboard-design'\n",
    "expected": "count: 8\nlabel: a-signature-input-output-switchboard-design\nmax: 500\nmean: 78.875\nmin: 1\ntotal: 631\nResult: count=8|label=a-signature-input-output-switchboard-design|max=500|mean=78.875|min=1|total=631\nRun 1 SHA-256: b54a53b8a71749ca55a2b766be707808b79d115bf594c3c8008d5267d1eb20d4\nRun 2 SHA-256: b54a53b8a71749ca55a2b766be707808b79d115bf594c3c8008d5267d1eb20d4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Amdahl Slider",
    "subject": "a Signature Amdahl slider design",
    "description": "The Amdahl Slider is a Signature-made design for teaching Amdahl's law: a slider where a learner sets the parallel fraction and the core count, and the tool shows the speedup, with the serial part capping it. Speedup is 1 divided by the serial part plus the parallel part over n. The parallel fraction and the core count are set on sliders. The speedup is shown, against the ideal linear speedup. The infinite-core limit is shown as the cap.",
    "inputs": "FIGURES = {'parallel_fraction': 0.9, 'cores': 8, 'speedup_8': 4.7, 'speedup_infinite': 10, 'serial_time_s': 100, 'parallel_time_s': 21, 'law_year': 1967, 'max_with_20pct_serial': 5}\nLABEL = 'a-signature-amdahl-slider-design'\n",
    "expected": "count: 8\nlabel: a-signature-amdahl-slider-design\nmax: 1967\nmean: 264.575\nmin: 0.9\ntotal: 2116.6\nResult: count=8|label=a-signature-amdahl-slider-design|max=1967|mean=264.575|min=0.9|total=2116.6\nRun 1 SHA-256: 50186fb3281141f36123448023c786f45a88f04fc81c9649b81ea8d534b707df\nRun 2 SHA-256: 50186fb3281141f36123448023c786f45a88f04fc81c9649b81ea8d534b707df\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Out-of-Order Scheduler",
    "subject": "a Signature out-of-order scheduler design",
    "description": "The Out-of-Order Scheduler is a Signature-made design for teaching superscalar execution: a scheduler where a learner watches instructions issue several per cycle, with ready instructions running before waiting ones, and results committed in order. The reorder buffer holds results until they can be committed. Several instructions issue per cycle, using several units. A waiting instruction is passed by later independent ones. Results are committed in program order.",
    "inputs": "FIGURES = {'issue_width': 4, 'ipc': 3, 'instructions': 3000000000, 'cycles': 1000000000, 'time_seconds': 0.33, 'rob_entries': 128, 'miss_latency': 100, 'mispredict_cost': 15}\nLABEL = 'a-signature-out-of-order-scheduler-design'\n",
    "expected": "count: 8\nlabel: a-signature-out-of-order-scheduler-design\nmax: 3000000000\nmean: 500000031.2912\nmin: 0.33\ntotal: 4000000250.33\nResult: count=8|label=a-signature-out-of-order-scheduler-design|max=3000000000|mean=500000031.2912|min=0.33|total=4000000250.33\nRun 1 SHA-256: 5a777d844ded1d59d32abc631c0ba8eba4b0a45a0e0761c56d36f9407eee963d\nRun 2 SHA-256: 5a777d844ded1d59d32abc631c0ba8eba4b0a45a0e0761c56d36f9407eee963d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Branch Predictor Trainer",
    "subject": "a Signature branch predictor trainer design",
    "description": "The Branch Predictor Trainer is a Signature-made design for teaching branch prediction: a trainer where a learner runs a loop, and the tool shows the 2-bit counter learning the pattern, the mispredictions, and their cost. A correct prediction costs nothing; a misprediction flushes the pipeline. The 2-bit counter is shown learning from history. Each prediction is shown right or wrong, with the cost. A random branch is shown defeating the predictor.",
    "inputs": "FIGURES = {'loop_iterations': 1000, 'taken': 999, 'mispredictions': 2, 'mispredict_cost': 15, 'total_cost': 30, 'overhead_pct': 3, 'random_accuracy': 0.5, 'random_cost': 7.5}\nLABEL = 'a-signature-branch-predictor-trainer-design'\n",
    "expected": "count: 8\nlabel: a-signature-branch-predictor-trainer-design\nmax: 1000\nmean: 257.125\nmin: 0.5\ntotal: 2057.0\nResult: count=8|label=a-signature-branch-predictor-trainer-design|max=1000|mean=257.125|min=0.5|total=2057.0\nRun 1 SHA-256: fe3d89c162f1b60ac63b5cb4eaf35b2a41f046516aa2458ceb42dfc3c19a9954\nRun 2 SHA-256: fe3d89c162f1b60ac63b5cb4eaf35b2a41f046516aa2458ceb42dfc3c19a9954\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The GPU Core Grid",
    "subject": "a Signature GPU core grid design",
    "description": "The GPU Core Grid is a Signature-made design for teaching graphics processors: a grid where a learner watches thousands of small cores divide a matrix multiply, with the time falling as the core count rises. A GPU is fast for parallel work and slow for serial work. The cores are shown as a grid, each working on its piece. The time is shown against the core count. A serial program is shown running slower on the GPU than on the CPU.",
    "inputs": "FIGURES = {'gpu_cores': 10000, 'gpu_clock_GHz': 1.5, 'gpu_tflops': 30, 'matrix_size': 4096, 'operations': 137400000000, 'gpu_time_ms': 4.6, 'cpu_tflops': 1, 'cpu_time_ms': 137}\nLABEL = 'a-signature-gpu-core-grid-design'\n",
    "expected": "count: 8\nlabel: a-signature-gpu-core-grid-design\nmax: 137400000000\nmean: 17175001783.7625\nmin: 1\ntotal: 137400014270.1\nResult: count=8|label=a-signature-gpu-core-grid-design|max=137400000000|mean=17175001783.7625|min=1|total=137400014270.1\nRun 1 SHA-256: f0ed22839dd2c8f10b0c3b4961b79545da385e1f2e52d5416b08fe4d9d872f81\nRun 2 SHA-256: f0ed22839dd2c8f10b0c3b4961b79545da385e1f2e52d5416b08fe4d9d872f81\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Storage Comparator",
    "subject": "a Signature storage comparator design",
    "description": "The Storage Comparator is a Signature-made design for teaching storage: a comparator where a learner runs the same reads on a hard disk and an SSD, and the tool shows the times, with the disk paying a seek per block and the SSD paying only its small latency. SSDs are far faster for random access. The same reads are run on both devices. Random reads are shown 100 times faster on the SSD. Sequential reads are shown closer, 200 MB/s against 500 MB/s.",
    "inputs": "FIGURES = {'hdd_seek_ms': 10, 'ssd_latency_ms': 0.1, 'random_blocks': 1000, 'hdd_random_s': 10, 'ssd_random_s': 0.1, 'speedup': 100, 'hdd_seq_MBs': 200, 'ssd_seq_MBs': 500}\nLABEL = 'a-signature-storage-comparator-design'\n",
    "expected": "count: 8\nlabel: a-signature-storage-comparator-design\nmax: 1000\nmean: 227.525\nmin: 0.1\ntotal: 1820.2\nResult: count=8|label=a-signature-storage-comparator-design|max=1000|mean=227.525|min=0.1|total=1820.2\nRun 1 SHA-256: 1c927f9adc84570e5fd4bf394ef61d5bfe48417aa326eec8a597aec76f8d0072\nRun 2 SHA-256: 1c927f9adc84570e5fd4bf394ef61d5bfe48417aa326eec8a597aec76f8d0072\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Network Latency Ruler",
    "subject": "a Signature network latency ruler design",
    "description": "The Network Latency Ruler is a Signature-made design for teaching networks: a ruler where a learner measures a message's travel time against distance, with the speed of light in fibre as the floor. Bandwidth can be bought; latency cannot go below the speed of light. The distance is set, and the latency floor is shown. The transfer time is shown from the data and the bandwidth. The bisection bandwidth of a data centre is computed.",
    "inputs": "FIGURES = {'link_Gbps': 100, 'one_GB_seconds': 0.08, 'fibre_us_per_km': 5, 'distance_km': 1000, 'one_way_ms': 5, 'machines': 10000, 'bisection_TBs': 10, 'ny_london_ms': 70}\nLABEL = 'a-signature-network-latency-ruler-design'\n",
    "expected": "count: 8\nlabel: a-signature-network-latency-ruler-design\nmax: 10000\nmean: 1398.76\nmin: 0.08\ntotal: 11190.08\nResult: count=8|label=a-signature-network-latency-ruler-design|max=10000|mean=1398.76|min=0.08|total=11190.08\nRun 1 SHA-256: c234cb646342369ebdab2ea27947f9a77583a30414da58a44dd5c2c5aff3c71a\nRun 2 SHA-256: c234cb646342369ebdab2ea27947f9a77583a30414da58a44dd5c2c5aff3c71a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Transistor Timeline",
    "subject": "a Signature transistor timeline design",
    "description": "The Transistor Timeline is a Signature-made design for teaching Moore's law: a timeline where a learner watches the transistor count double, the clocks rise and then flatten, and the cores multiply, with the power wall marked at 2005. Moore's law is an observation, not a law of nature. The transistor count is plotted doubling every two years. The clock curve rises to 3 GHz and flattens near 5 GHz. The core count is shown rising from 1 to 64.",
    "inputs": "FIGURES = {'transistors_2005': 1000000000, 'doubling_years': 2, 'transistors_2023': 100000000000, 'clock_1995_MHz': 100, 'clock_2005_GHz': 3, 'clock_now_GHz': 5, 'cores_now': 64, 'power_wall_W': 300}\nLABEL = 'a-signature-transistor-timeline-design'\n",
    "expected": "count: 8\nlabel: a-signature-transistor-timeline-design\nmax: 100000000000\nmean: 12625000059.25\nmin: 2\ntotal: 101000000474\nResult: count=8|label=a-signature-transistor-timeline-design|max=100000000000|mean=12625000059.25|min=2|total=101000000474\nRun 1 SHA-256: 7a55a3a7391663ca2aaed9e5e6193e128153ccdbc6607025ec3631a7ed0e69a4\nRun 2 SHA-256: 7a55a3a7391663ca2aaed9e5e6193e128153ccdbc6607025ec3631a7ed0e69a4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The RISC-CISC Balance",
    "subject": "a Signature RISC-CISC balance design",
    "description": "The RISC-CISC Balance is a Signature-made design for teaching the RISC-CISC debate: a balance where a learner weighs a RISC program against a CISC program, with the instruction count on one side and the cycles per instruction on the other, and the total time balancing. The total work is the instruction count times the cycles per instruction. The RISC program is shown with many instructions at 1 CPI. The CISC program is shown with few instructions at 2.5 CPI. The totals are shown equal: 1,000 cycles each.",
    "inputs": "FIGURES = {'risc_instructions': 4, 'cisc_instructions': 1, 'cisc_cycles': 3, 'cisc_bytes': 6, 'risc_program': 1000, 'risc_cpi': 1, 'cisc_program': 400, 'cisc_cpi': 2.5}\nLABEL = 'a-signature-risc-cisc-balance-design'\n",
    "expected": "count: 8\nlabel: a-signature-risc-cisc-balance-design\nmax: 1000\nmean: 177.1875\nmin: 1\ntotal: 1417.5\nResult: count=8|label=a-signature-risc-cisc-balance-design|max=1000|mean=177.1875|min=1|total=1417.5\nRun 1 SHA-256: 042c241d11dbc1d446b04fcecb9021b7887182048987b6c4a98295713033173d\nRun 2 SHA-256: 042c241d11dbc1d446b04fcecb9021b7887182048987b6c4a98295713033173d\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Memory Wall Gap",
    "subject": "a Signature memory wall gap design",
    "description": "The Memory Wall Gap is a Signature-made design for teaching the memory wall: a gap where a learner watches the CPU speed rise and the memory latency stay nearly still, with the gap widening, and the cache shown narrowing it. Caches hide the gap when the program has locality. The CPU speed and the memory latency are plotted over time, with the gap widening. A cache miss is shown costing 300 cycles. The hit rate is shown narrowing the gap.",
    "inputs": "FIGURES = {'cpu_cycle_ns': 0.33, 'dram_latency_ns': 100, 'latency_cycles': 300, 'miss_rate': 0.05, 'avg_access_cycles': 5.95, 'peak_ops': 3000000000, 'memory_bound_ops': 10000000, 'slowdown': 300}\nLABEL = 'a-signature-memory-wall-gap-design'\n",
    "expected": "count: 8\nlabel: a-signature-memory-wall-gap-design\nmax: 3000000000\nmean: 376250088.2912\nmin: 0.05\ntotal: 3010000706.33\nResult: count=8|label=a-signature-memory-wall-gap-design|max=3000000000|mean=376250088.2912|min=0.05|total=3010000706.33\nRun 1 SHA-256: a4c9ccbc73335d2f1a9f7c2e7a5ed8388d7cabd65e0ee0d3e68b8d868ba01284\nRun 2 SHA-256: a4c9ccbc73335d2f1a9f7c2e7a5ed8388d7cabd65e0ee0d3e68b8d868ba01284\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Power Budget Meter",
    "subject": "a Signature power budget meter design",
    "description": "The Power Budget Meter is a Signature-made design for teaching power: a meter where a learner sets the voltage, the frequency, and the number of blocks, and the tool shows the power, with halving the voltage quartering it. Dynamic power is capacitance times voltage squared times frequency. The voltage, frequency, and block count are set. The power is shown, growing with the square of the voltage. The dark silicon is shown: the blocks that must stay off within the budget.",
    "inputs": "FIGURES = {'capacitance_nF': 1, 'voltage_V': 1, 'frequency_GHz': 3, 'power_per_block_W': 3, 'blocks': 30, 'total_power_W': 90, 'half_voltage_power_W': 0.75, 'budget_W': 100}\nLABEL = 'a-signature-power-budget-meter-design'\n",
    "expected": "count: 8\nlabel: a-signature-power-budget-meter-design\nmax: 100\nmean: 28.5938\nmin: 0.75\ntotal: 228.75\nResult: count=8|label=a-signature-power-budget-meter-design|max=100|mean=28.5938|min=0.75|total=228.75\nRun 1 SHA-256: 7bb2a2eca24ce351a6c7a7f2478ec83ce3de999bd8a20fdcf1081077c49bd805\nRun 2 SHA-256: 7bb2a2eca24ce351a6c7a7f2478ec83ce3de999bd8a20fdcf1081077c49bd805\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The ECC Guardian",
    "subject": "a Signature error-correcting guardian design",
    "description": "The ECC Guardian is a Signature-made design for teaching reliability: a guardian where a learner flips a bit in memory, and the tool shows the ECC (error-correcting code) detecting and correcting it, with the error rate of a large server shown. ECC corrects single-bit errors and detects double-bit errors. A bit is flipped, and the ECC is shown correcting it. The error rate of a large server is shown: about 4 a day for 1 TB. RAID is shown tolerating a disk failure.",
    "inputs": "FIGURES = {'ram_TB': 1, 'modules': 128, 'module_GB': 8, 'errors_per_month': 128, 'errors_per_day': 4, 'raid_disks': 5, 'tolerated_failures': 1, 'rebuild_hours': 10}\nLABEL = 'a-signature-error-correcting-guardian-design'\n",
    "expected": "count: 8\nlabel: a-signature-error-correcting-guardian-design\nmax: 128\nmean: 35.625\nmin: 1\ntotal: 285\nResult: count=8|label=a-signature-error-correcting-guardian-design|max=128|mean=35.625|min=1|total=285\nRun 1 SHA-256: 17ec45fc4c5e6c455e393eb0bbbf0e026317f10662926e226eb328bb52b4e8d6\nRun 2 SHA-256: 17ec45fc4c5e6c455e393eb0bbbf0e026317f10662926e226eb328bb52b4e8d6\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Benchmark Scoreboard",
    "subject": "a Signature benchmark scoreboard design",
    "description": "The Benchmark Scoreboard is a Signature-made design for teaching performance measurement: a scoreboard where a learner runs two machines on the same programs, and the tool shows the times, the speedups, and the iron-law breakdown. Time is the honest metric; speedups are ratios of times. Two machines run the same programs, and the times are shown. The speedup is the ratio of the times. The iron law breaks the time into instructions, CPI, and clock.",
    "inputs": "FIGURES = {'time_X_s': 10, 'time_Y_s': 8, 'speedup': 1.25, 'suite_mean': 1.3, 'instructions': 2000000000, 'cpi_Y': 1.2, 'cpi_X': 1.5, 'clock_GHz': 3}\nLABEL = 'a-signature-benchmark-scoreboard-design'\n",
    "expected": "count: 8\nlabel: a-signature-benchmark-scoreboard-design\nmax: 2000000000\nmean: 250000003.2812\nmin: 1.2\ntotal: 2000000026.25\nResult: count=8|label=a-signature-benchmark-scoreboard-design|max=2000000000|mean=250000003.2812|min=1.2|total=2000000026.25\nRun 1 SHA-256: 385093219c937aac7cc9e3a38af95b69331c9b6934f3b6790a39c7354de6aa69\nRun 2 SHA-256: 385093219c937aac7cc9e3a38af95b69331c9b6934f3b6790a39c7354de6aa69\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Cycle Stepper",
    "subject": "a Signature fetch-decode-execute cycle stepper design",
    "description": "The Cycle Stepper is a Signature-made design for teaching the fetch-decode-execute cycle: a stepper where a learner steps through a program one cycle at a time, watching the program counter advance, the instruction decode, and the result write back. The cycle is the heartbeat of the CPU. Each cycle is shown: fetch, decode, execute, write-back. The program counter advances by the instruction size each cycle. The time is shown: 4 cycles at 3 GHz take 1.33 nanoseconds.",
    "inputs": "FIGURES = {'cycles': 4, 'instruction_bytes': 4, 'clock_GHz': 3, 'time_ns': 1.33, 'stages': 3, 'addresses': 3, 'registers_used': 2, 'design_version': 1}\nLABEL = 'a-signature-fetch-decode-execute-cycle-stepper-design'\n",
    "expected": "count: 8\nlabel: a-signature-fetch-decode-execute-cycle-stepper-design\nmax: 4\nmean: 2.6662\nmin: 1\ntotal: 21.33\nResult: count=8|label=a-signature-fetch-decode-execute-cycle-stepper-design|max=4|mean=2.6662|min=1|total=21.33\nRun 1 SHA-256: 54d2eab7112e201999ec5537f1c262d3a76eae9121690661d7564f84304070a9\nRun 2 SHA-256: 54d2eab7112e201999ec5537f1c262d3a76eae9121690661d7564f84304070a9\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The VLIW Scheduler",
    "subject": "a Signature VLIW scheduler design",
    "description": "The VLIW Scheduler is a Signature-made design for teaching instruction-level parallelism: a scheduler where a learner packs independent operations into long instruction words, and the tool shows the cycles saved, with dependency chains shown blocking the packing. A VLIW CPU relies on the compiler to find the parallelism. Independent operations are packed into one word. The cycles are counted against the scalar count. A dependency chain is shown blocking the packing.",
    "inputs": "FIGURES = {'operations_per_iteration': 4, 'scalar_cycles': 4, 'superscalar_cycles': 1, 'speedup': 4, 'vliw_slots': 4, 'dependent_cycles': 4, 'typical_ilp': 2.5, 'issue_width': 4}\nLABEL = 'a-signature-vliw-scheduler-design'\n",
    "expected": "count: 8\nlabel: a-signature-vliw-scheduler-design\nmax: 4\nmean: 3.4375\nmin: 1\ntotal: 27.5\nResult: count=8|label=a-signature-vliw-scheduler-design|max=4|mean=3.4375|min=1|total=27.5\nRun 1 SHA-256: a4d69f2e43a357a0f1d84360037f9dd9b2c189d35f2772ce2207efde1728facc\nRun 2 SHA-256: a4d69f2e43a357a0f1d84360037f9dd9b2c189d35f2772ce2207efde1728facc\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Architecture Capstone Console",
    "subject": "a Signature architecture capstone console design",
    "description": "The Architecture Capstone Console is a Signature-made design for teaching end-to-end CPU design: a console where a learner assembles a small CPU from its parts (ISA, pipeline, cache, memory, power), estimates its performance by the iron law, and checks each part. A capstone problem uses several tools at once. The console assembles the parts: ISA, pipeline, cache, memory, power. Each part is estimated and checked separately. The assembly is scored as a whole design, with the performance stated.",
    "inputs": "FIGURES = {'clock_GHz': 3, 'cpi': 1.2, 'program_instructions': 1000000000, 'time_seconds': 0.4, 'pipeline_cycles': 104, 'cache_KB': 64, 'avg_access_cycles': 5.95, 'power_W': 90}\nLABEL = 'a-signature-architecture-capstone-console-design'\n",
    "expected": "count: 8\nlabel: a-signature-architecture-capstone-console-design\nmax: 1000000000\nmean: 125000033.5688\nmin: 0.4\ntotal: 1000000268.55\nResult: count=8|label=a-signature-architecture-capstone-console-design|max=1000000000|mean=125000033.5688|min=0.4|total=1000000268.55\nRun 1 SHA-256: 6df1b38804b9835c1c75ce6f209021755292e0b9f6965ee6edd7bfbc42628882\nRun 2 SHA-256: 6df1b38804b9835c1c75ce6f209021755292e0b9f6965ee6edd7bfbc42628882\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Von Neumann architecture",
    "url": "https://en.wikipedia.org/wiki/Von_Neumann_architecture",
    "establishes": "The reference for a Signature stored-program workbench design in this record."
  },
  {
    "name": "Wikipedia - Computer architecture",
    "url": "https://en.wikipedia.org/wiki/Computer_architecture",
    "establishes": "The reference for a Signature stored-program workbench design in this record."
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
