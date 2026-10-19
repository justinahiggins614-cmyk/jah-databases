#!/usr/bin/env python3
"""Entries for The Unsolved Operations Research Database
(unsolved-operations-research) and its Signature half
(unsolved-operations-research-signature).

34 famous unsolved problems in operations research, ladder-ordered by
accessibility (rank 1 = most approachable, rank 34 = most complex).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USOR- / JAH-USORS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "operations-research",
 "disp": "operations research",
 "name": "The Unsolved Operations Research Database",
 "sig_name": "The Unsolved Operations Research Signature Database",
 "prefix": "JAH-USOR-",
 "sig_prefix": "JAH-USORS-",
 "ai": "JAH Unsolved Operations Research Archivist",
 "tagline": ("Thirty-four famous open problems in operations research, from the traveling salesman to "
             "unified optimization under uncertainty: real, fact-checked, each with its full story and a "
             "clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of operations "
                 "research: Signature-generated proposed solutions with assumptions declared, confirm and "
                 "refute conditions stated, and limits honestly marked. Clearly labeled Signature-made, "
                 "never established science."),
 "pub_line": ("Public records - 34 famous open problems in operations research, real and fact-checked: the "
              "traveling salesman, vehicle routing, bin packing, job shop scheduling, cutting stock, "
              "facility location, inventory under nonstationary demand, optimal stopping, bandits, online "
              "matching, and the newsvendor frontier - every record carrying the problem statement, "
              "background, why it matters, key points, requirements, standards, citations, and a working "
              "solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "operations research problems approached as a covenant between the known and the unknown, each "
              "carrying the full Signature-generated proposed solution with its assumptions declared, its "
              "confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (traveling salesman, vehicle "
                 "routing, bin packing, job shop, cutting stock, facility location, nonstationary inventory, "
                 "optimal stopping, bandits, online matching, newsvendor) -> Compounded (branch and bound, "
                 "cutting planes, column generation, mixed-integer nonlinear programming, stochastic "
                 "programming, robust optimization, multi-objective frontiers, strategic dynamic pricing, "
                 "network revenue management, the bullwhip effect, project scheduling, crew scheduling) -> "
                 "Advanced (semidefinite rank bounds, simulation optimization, ranking and selection, MDP "
                 "sample complexity, queueing network limits, imperfect maintenance, reliability allocation, "
                 "truthful mechanisms, Nash computation, simulation warmup, unified optimization under "
                 "uncertainty)."),
 "search_ph": ("Search traveling salesman, vehicle routing, scheduling, inventory, bandits, branch and bound, "
               "stochastic programming, bullwhip, Nash equilibrium, revenue management..."),
 "chat_ph": "Ask about the great open problems of operations research...",
 "greet_pub": ("I am the JAH Unsolved Operations Research Archivist. Ask me about the great open problems of "
               "operations research - from the traveling salesman, scheduling, and inventory through "
               "stochastic programming, the bullwhip effect, and revenue management, to Nash computation and "
               "unified optimization under uncertainty."),
 "greet_sig": ("I am the JAH Unsolved Operations Research Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of operations research - every approach labeled "
               "as a proposal, never established science."),
 "role_pub": ("unsolved operations research archivist - the great open problems of operations research, from "
              "the traveling salesman, scheduling, and inventory through stochastic programming, the bullwhip "
              "effect, and revenue management, to Nash computation and unified optimization under uncertainty; "
              "teaches progressively along the ladder from foundations through compounded to advanced; answers "
              "from many angles - definition, example, analogy, application, history, math - using only "
              "archive data from this system"),
 "role_sig": ("unsolved operations research archivist - Signature editions: his original Signature solution "
              "method applied to the 34 great open problems of operations research, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through "
              "compounded to advanced; answers from many angles - definition, example, analogy, application, "
              "history, math - using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved operations research studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Hillier and Lieberman, Introduction to Operations Research; Bertsimas and Tsitsiklis, Introduction to Linear Optimization).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "or-tsp",
 "name": "The Traveling Salesman Exact Solution Problem",
 "group": "Optimization",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Given a set of cities and the distances between them, what is the shortest possible tour that visits each city exactly once - and can it be found efficiently as the instance grows?",
 "background": "The traveling salesman problem (TSP) is the archetypal hard combinatorial problem: Dantzig, Fulkerson and Johnson solved a 49-city instance in 1954 with cutting planes, launching integer programming. The problem is NP-hard, so no known polynomial algorithm exists, and the million-dollar P versus NP question is whether one ever will. In practice, Concorde has solved instances above 85,000 cities to proven optimality, and heuristics like Lin-Kernighan find near-optimal tours fast. Yet the gap between practical success and theoretical understanding is total: nobody knows whether exact solution must take exponential time, and approximation guarantees for the general (non-metric) TSP are essentially nonexistent.",
 "why_it_matters": "Routing is civilization's plumbing: delivery fleets, chip wiring, DNA sequencing, telescope scheduling. The TSP is the clean mathematical core of all of it, and its hardness boundary governs what logistics can ever promise.",
 "sig_lens": "The Signature lens reads the TSP as a ledger of tours: instead of hunting one perfect tour, keep books on the whole frontier of good tours and their certified gaps.",
 "sig_solution": LABEL + " Assumptions: (1) P versus NP stays open, so exactness must be certified, not assumed; (2) practitioners need good tours with known gaps more than optimal tours with unknown cost. Reasoning path: shift the deliverable from the tour to the tour-plus-gap certificate, and invest exact-solution effort where the gap is largest. Proposed mechanism: a gap-ledger protocol that always ships the best tour found with a proven lower bound, directs exact solvers at the instances with the widest gaps, and reports the distribution of gaps across the workload. Confirm: gap-led allocation closes more real routing gaps per compute dollar. Kill: lower bounds stay too weak to guide allocation. Does NOT claim: a polynomial exact algorithm - it manages the hardness, it does not remove it.",
 "pointer": "The Signature system's proposed approach ships every tour with its certified gap and aims exact solvers at the widest gaps; the companion Signature Edition record specifies the gap-ledger protocol.",
 "key_points": [
  "The TSP is NP-hard; whether a polynomial exact algorithm exists is the P versus NP question.",
  "Concorde has solved instances above 85,000 cities to proven optimality.",
  "Heuristics find near-optimal tours fast, but without optimality certificates.",
  "General (non-metric) TSP has essentially no approximation guarantees.",
 ],
 "requirements": [
  "A proven lower bound accompanying every reported tour.",
  "Exact-solver effort directed at widest-gap instances.",
  "Workload-level reporting of gap distributions, not just best tours.",
 ],
 "citations": [
  "Dantzig G, Fulkerson R, Johnson S (1954) Solution of a large-scale traveling-salesman problem. Operations Research 2: 393-410.",
  "Applegate D et al. (2006) The Traveling Salesman Problem: A Computational Study. Princeton University Press.",
 ],
 "demo": {"coords": [[0,0],[3,1],[5,4],[1,5],[4,2]]},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "or-vrp",
 "name": "The Vehicle Routing Exact Problem",
 "group": "Optimization",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "How should a fleet of capacity-limited vehicles be routed to serve scattered customers at minimum cost - and why does the exact optimum stay out of reach for realistically sized fleets?",
 "background": "Dantzig and Ramser formulated the truck dispatching problem in 1959, and the vehicle routing problem (VRP) has grown into the richest family in combinatorial optimization: capacitated, time-windowed, multi-depot, stochastic, and dynamic variants. Exact methods (branch-cut-and-price) now solve capacitated instances with a few hundred customers, but real operations run thousands of stops with time windows, driver rules, and live traffic. The variants multiply faster than the algorithms: each realistic constraint (split deliveries, pickup-and-delivery, electric charging) spawns a subfield. Metaheuristics dominate practice while exact methods cover only the smaller, cleaner cases.",
 "why_it_matters": "Every parcel, every grocery delivery, every service technician route is a VRP. The gap between exact methods and real instances is measured in fuel, hours, and emissions.",
 "sig_lens": "The Signature lens reads routing as promises with wheels: the plan is a set of commitments, and the protocol must price the cost of breaking each one.",
 "sig_solution": LABEL + " Assumptions: (1) real instances exceed exact-method reach; (2) the binding constraints are operational (drivers, windows), not just combinatorial. Reasoning path: decompose the monster - solve an exact core (assignment and sequencing) and handle live constraints with a fast repair layer, keeping the exact core's certificate. Proposed mechanism: a core-and-repair protocol that solves the capacitated skeleton exactly, then applies time-window and traffic repairs with bounded degradation, reporting the repair cost explicitly. Confirm: core-and-repair beats pure heuristics on cost with certificates intact. Kill: repair costs dominate and the certificate becomes meaningless. Does NOT claim: exact solution of full real-world VRPs - it bounds the compromise.",
 "pointer": "The Signature system's proposed approach solves an exact routing core and repairs operational constraints with bounded cost; the companion Signature Edition record specifies the core-and-repair protocol.",
 "key_points": [
  "The VRP family spans capacitated, time-windowed, multi-depot, and dynamic variants.",
  "Exact branch-cut-and-price reaches a few hundred customers; practice needs thousands.",
  "Each realistic constraint spawns its own subfield and algorithm.",
  "Metaheuristics dominate practice without optimality certificates.",
 ],
 "requirements": [
  "An exactly solved core subproblem with a valid lower bound.",
  "Bounded-degradation repair for operational constraints.",
  "Explicit reporting of repair costs against the core certificate.",
 ],
 "citations": [
  "Dantzig GB, Ramser JH (1959) The truck dispatching problem. Management Science 6(1): 80-91.",
  "Toth P, Vigo D (2014) Vehicle Routing: Problems, Methods, and Applications, 2nd ed. SIAM.",
 ],
 "demo": {"coords": [[0,0],[2,3],[6,1],[4,5],[7,3]]},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "or-bin-packing",
 "name": "The Bin Packing Online Problem",
 "group": "Optimization",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "When items arrive one by one and each must be placed immediately, how close to optimal can any online packing strategy get - and what is the true competitive limit?",
 "background": "Bin packing - fit items into the fewest unit-capacity bins - is NP-hard offline, but the online version (items arrive sequentially, placement is irrevocable) is the practical one: loading trucks, allocating cloud VMs, cutting stock on the fly. The classic First Fit algorithm uses at most about 1.7 times optimal bins; the lower bound for any online algorithm sat at 1.54 for decades until Balogh, Békési and Galambos pushed the analysis. The exact optimal competitive ratio remains unknown - the gap between the best algorithm's guarantee and the best lower bound is small but unclosed. Real variants (item departures, fragmentation costs) widen it further.",
 "why_it_matters": "Cloud servers, shipping containers, and memory allocators all pack online. The competitive ratio is the tax paid for deciding without the future - and nobody knows the minimum tax.",
 "sig_lens": "The Signature lens reads online packing as deciding under a blindfold: the protocol must price the blindness explicitly and buy information where it is cheapest.",
 "sig_solution": LABEL + " Assumptions: (1) the optimal competitive ratio is unknown but bounded; (2) real arrivals carry predictable structure the worst case ignores. Reasoning path: blend worst-case guarantees with learned arrival forecasts - keep the competitive bound as a floor and let forecasts improve the average. Proposed mechanism: a forecast-hedged protocol that runs a bounded-regret online packer as the default and switches to forecast-guided placement only when the forecast's recent accuracy clears a bar, with automatic fallback. Confirm: hedged packing beats pure online on real workloads without losing the worst-case bound. Kill: forecasts mislead and the fallback triggers too late. Does NOT claim: the optimal competitive ratio - it earns the average case while keeping the worst case.",
 "pointer": "The Signature system's proposed approach hedges online packing with accuracy-gated forecasts; the companion Signature Edition record specifies the forecast-hedged protocol.",
 "key_points": [
  "Online bin packing is NP-hard offline and irrevocable online.",
  "First Fit guarantees about 1.7 times optimal; the true optimum ratio is unclosed.",
  "The lower bound near 1.54 stood for decades.",
  "Real variants with departures and fragmentation widen the gap.",
 ],
 "requirements": [
  "A worst-case competitive bound as the non-negotiable floor.",
  "Arrival forecasts with measured recent accuracy.",
  "Automatic fallback to the pure online rule when forecasts fail.",
 ],
 "citations": [
  "Johnson DS (1973) Near-optimal bin packing algorithms. MIT PhD thesis.",
 ],
 "demo": {"coords": [[0,0],[1,2],[4,0],[3,3],[5,1]]},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "or-job-shop",
 "name": "The Job Shop Scheduling Problem",
 "group": "Optimization",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Given jobs that each need a sequence of machine operations, what schedule minimizes the makespan - and why do even tiny instances defeat exact methods?",
 "background": "Job shop scheduling - n jobs, m machines, each job with its own machine order - is NP-hard in almost every variant, and famously hard in practice: the 10-job 10-machine Fisher-Thompson instance resisted exact solution for over 25 years. Shifting-bottleneck heuristics (Adams, Balas and Zawack, 1988) and tabu search handle industrial sizes, but optimal makespans for benchmark instances are still being settled decades later. The difficulty is disjunctive: each machine ordering decision interacts with all others, and the search space explodes combinatorially. Real shops add release dates, setups, breakdowns, and rework - each making the model more faithful and less solvable.",
 "why_it_matters": "Factories live or die on schedules: makespan is throughput, and throughput is revenue. The gap between heuristic schedules and optimal ones is idle machines and late orders.",
 "sig_lens": "The Signature lens reads the job shop as a set of bottlenecks taking turns: find the machine that constrains the makespan and schedule everything else around it.",
 "sig_solution": LABEL + " Assumptions: (1) exact optima are unreachable for real shops; (2) one or two bottlenecks usually bind the makespan. Reasoning path: identify the bottleneck machines dynamically, optimize their sequences exactly, and schedule the rest heuristically around them. Proposed mechanism: a bottleneck-first protocol that computes machine criticality scores, solves the top bottlenecks as exact subproblems, and fills the remaining schedule with dispatching rules - re-identifying bottlenecks as the schedule evolves. Confirm: bottleneck-first schedules beat pure dispatching on makespan across benchmarks. Kill: bottlenecks shift faster than the protocol re-identifies them. Does NOT claim: optimal makespans - it concentrates exact effort where it pays.",
 "pointer": "The Signature system's proposed approach solves bottleneck machines exactly and schedules around them; the companion Signature Edition record specifies the bottleneck-first protocol.",
 "key_points": [
  "Job shop scheduling is NP-hard in nearly all variants.",
  "The 10x10 Fisher-Thompson instance took 25 years to solve exactly.",
  "Shifting-bottleneck and tabu search dominate practice.",
  "Real shops add setups, breakdowns, and rework that defeat exact models.",
 ],
 "requirements": [
  "Dynamic bottleneck identification as the schedule evolves.",
  "Exact solution of bottleneck-machine subproblems.",
  "Makespan-gap reporting against lower bounds.",
 ],
 "citations": [
  "Adams J, Balas E, Zawack D (1988) The shifting bottleneck procedure for job shop scheduling. Management Science 34(3).",
 ],
 "demo": {"coords": [[0,0],[4,1],[2,4],[6,2],[1,6]]},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "or-cutting-stock",
 "name": "The Cutting Stock Problem",
 "group": "Optimization",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "How should standard-size rolls be cut into ordered widths to minimize waste - and does the famous integer rounding property actually hold?",
 "background": "Gilmore and Gomory (1961) turned cutting stock into the showcase for column generation: the linear programming relaxation gives bounds so tight that the optimum is almost always within one roll of the LP value - the integer rounding property (IRP), also called the modified integer rounding property. Whether the gap can ever exceed one roll was open for decades; counterexamples with larger gaps were eventually found, but they are rare and pathological. In practice the LP bound is the workhorse of paper, steel, and textile industries. The theoretical question - characterizing exactly when the property holds - remains open, as does extending the tightness to multi-dimensional cutting and packing.",
 "why_it_matters": "Paper mills, steel service centers, and fabric cutters waste material by the ton. The LP bound is the industry's measuring stick; understanding its exactness is understanding the waste floor.",
 "sig_lens": "The Signature lens reads cutting as a rounding ledger: the LP relaxation tells the truth within one roll, and the protocol must account for that last roll explicitly.",
 "sig_solution": LABEL + " Assumptions: (1) the LP bound is nearly always within one roll of optimal; (2) pathological counterexamples exist but are rare. Reasoning path: treat the LP value as the plan and the rounding gap as a managed residual - optimize the residual directly instead of re-solving. Proposed mechanism: a residual-ledger protocol that solves the Gilmore-Gomory LP, then runs a dedicated residual optimizer on the at-most-one-roll gap, with the rare large-gap cases flagged for exact methods. Confirm: residual-focused optimization closes the gap faster than full re-solves. Kill: real instances hit pathological gaps more often than theory suggests. Does NOT claim: a proof of the rounding property - it manages the gap as observed.",
 "pointer": "The Signature system's proposed approach optimizes the LP rounding residual directly; the companion Signature Edition record specifies the residual-ledger protocol.",
 "key_points": [
  "Gilmore-Gomory column generation made cutting stock tractable via the LP relaxation.",
  "The integer rounding property says the gap is almost always at most one roll.",
  "Counterexamples exist but are rare and pathological.",
  "Multi-dimensional extensions lack the same tightness guarantees.",
 ],
 "requirements": [
  "The Gilmore-Gomory LP bound as the planning baseline.",
  "A dedicated residual optimizer for the rounding gap.",
  "Flagging of large-gap cases for exact methods.",
 ],
 "citations": [
  "Gilmore PC, Gomory RE (1961) A linear programming approach to the cutting-stock problem. Operations Research 9(6).",
 ],
 "demo": {"coords": [[0,0],[5,2],[2,5],[6,4],[3,1]]},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "or-facility-location",
 "name": "The Facility Location Approximation Gap",
 "group": "Optimization",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Where should facilities be opened to serve customers at minimum total cost - and how close to optimal can efficient algorithms provably get?",
 "background": "Uncapacitated facility location - choose sites to minimize opening plus service costs - admits a 1.488-approximation (Li, 2013), while the lower bound sits at 1.463: a thin but unclosed gap. Capacitated variants are harder, with constant-factor approximations only under relaxations. The problem is the clean core of logistics network design: warehouses, hospitals, fire stations. Local search, LP rounding, and primal-dual methods all achieve similar ratios, suggesting the frontier is near - but near is not closed, and the capacitated and robust variants have much wider gaps. Real instances add multi-period, stochastic demand that the theory barely touches.",
 "why_it_matters": "Warehouse and hospital networks are decade-long commitments worth billions. The approximation gap is the uncertainty tax on every network design decision.",
 "sig_lens": "The Signature lens reads location as a commitment ledger: opening a facility is a bet on future demand, and the protocol must keep the bet revisable.",
 "sig_solution": LABEL + " Assumptions: (1) the 1.463-1.488 gap is thin but real; (2) demand uncertainty dominates the approximation gap in practice. Reasoning path: optimize the robust network, not the point forecast - choose locations that stay near-optimal across demand scenarios. Proposed mechanism: a commitment-ledger protocol that evaluates candidate networks across a scenario ensemble, selects the minimax-regret design, and stages openings so early commitments preserve future options. Confirm: regret-minimizing networks outperform point-optimal ones under demand shifts. Kill: scenario ensembles miss the true future and the robustness is misdirected. Does NOT claim: closing the approximation gap - it manages the larger uncertainty that swamps it.",
 "pointer": "The Signature system's proposed approach designs minimax-regret networks across demand scenarios; the companion Signature Edition record specifies the commitment-ledger protocol.",
 "key_points": [
  "Uncapacitated facility location: 1.488-approximation versus 1.463 lower bound.",
  "Capacitated and robust variants have much wider open gaps.",
  "The problem is the core of warehouse and hospital network design.",
  "Real instances add multi-period stochastic demand the theory barely covers.",
 ],
 "requirements": [
  "Scenario ensembles spanning plausible demand futures.",
  "Minimax-regret selection across the ensemble.",
  "Staged commitments preserving future network options.",
 ],
 "citations": [
  "Li S (2013) A 1.488 approximation algorithm for the uncapacitated facility location problem. Information and Computation 222.",
 ],
 "demo": {"coords": [[0,0],[3,4],[6,0],[2,2],[5,5]]},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "or-inventory-nonstationary",
 "name": "The Inventory Policy Under Nonstationary Demand Problem",
 "group": "Stochastic Models",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "When demand distribution shifts over time - seasons, trends, shocks - what ordering policy is optimal, and can the classic (s, S) policies survive nonstationarity?",
 "background": "Scarf (1960) proved (s, S) policies optimal for stationary stochastic demand with fixed ordering costs: order up to S when inventory falls to s. Nonstationary demand breaks the proof - the optimal policy becomes time-dependent and computationally brutal, a high-dimensional dynamic program. Practitioners use rolling-horizon heuristics, demand forecasting bolted onto stationary policies, or robust policies, but the optimality gap is unmeasured in most deployments. The deeper issue is joint: forecasting error and inventory optimization interact, and optimizing them separately (forecast then order) is provably suboptimal versus integrated approaches that remain largely theoretical.",
 "why_it_matters": "Inventory is working capital: too much ties up cash, too little loses sales. Nonstationary demand - everything from fashion to pandemic supplies - is the normal case, not the exception.",
 "sig_lens": "The Signature lens reads inventory as a bet against the future that must be re-placed daily: the policy is a standing instruction, and the instruction needs a revision rule.",
 "sig_solution": LABEL + " Assumptions: (1) stationary-optimal policies degrade under drift; (2) forecast-then-order is suboptimal but universal. Reasoning path: integrate forecasting and ordering in a rolling-horizon optimizer that re-solves as demand reveals itself, with the forecast uncertainty feeding the safety stock directly. Proposed mechanism: a revision-rule protocol that re-solves the ordering problem each period with updated demand distributions, sizes safety stock from forecast error bands (not point forecasts), and audits the forecast-then-order gap quarterly. Confirm: integrated rolling-horizon policies beat bolted-on forecasts on cost. Kill: forecast error bands are miscalibrated and the safety stocks mislead. Does NOT claim: optimality under nonstationarity - it manages the drift adaptively.",
 "pointer": "The Signature system's proposed approach re-solves ordering each period with forecast-error-sized safety stocks; the companion Signature Edition record specifies the revision-rule protocol.",
 "key_points": [
  "(s, S) policies are optimal only under stationary demand (Scarf, 1960).",
  "Nonstationary optima are time-dependent dynamic programs, computationally brutal.",
  "Forecast-then-order is provably suboptimal versus integrated approaches.",
  "The optimality gap of deployed heuristics is rarely measured.",
 ],
 "requirements": [
  "Per-period re-solution with updated demand distributions.",
  "Safety stocks sized from forecast error bands.",
  "Quarterly audits of the forecast-then-order optimality gap.",
 ],
 "citations": [
  "Scarf H (1960) The optimality of (s, S) policies in the dynamic inventory problem. Stanford University Press.",
 ],
 "demo": {"coords": [[0,0],[2,1],[5,3],[1,4],[4,6]]},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "or-secretary",
 "name": "The Secretary Problem and Optimal Stopping",
 "group": "Decision Analysis",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "When candidates arrive in random order and each must be accepted or rejected on the spot, what stopping rule maximizes the chance of picking the best - and how far do the elegant answers extend?",
 "background": "The classical secretary problem has a beautiful answer: interview the first 37 percent (1/e) to calibrate, then hire the first candidate better than all seen - maximizing the probability of hiring the best at about 37 percent. But the extensions are where reality lives and elegance dies: unknown numbers of candidates, cardinal values instead of rankings, recall allowed, multiple hires, adversarial orderings. Each variant has partial answers; the general theory of optimal stopping under realistic frictions (costly interviews, candidate dropout, correlated values) is fragmented. Practitioners in hiring, house-hunting, and procurement use the 37 percent rule as folklore far outside its assumptions.",
 "why_it_matters": "Hiring, procurement, and search are all optimal-stopping problems with real money on the line. Folklore rules applied outside their assumptions are expensive superstitions.",
 "sig_lens": "The Signature lens reads stopping as a calibration ledger: the exploration phase buys information, and the protocol must show the purchase was worth it.",
 "sig_solution": LABEL + " Assumptions: (1) the 1/e rule needs its assumptions (known n, random order, rank-only); (2) real searches violate them routinely. Reasoning path: replace folklore with a calibrated stopping calculator that takes the actual parameters (uncertain n, interview costs, recall options) and computes the stopping rule for the case at hand. Proposed mechanism: a stopping-calculator protocol that estimates the arrival process, prices the exploration phase, and outputs a case-specific threshold rule with its success probability - refusing to output the 1/e rule when assumptions fail. Confirm: calibrated rules beat folklore on simulated realistic searches. Kill: the arrival process proves unestimable and the calculator is garbage-in. Does NOT claim: a universal stopping rule - it computes the right rule per case.",
 "pointer": "The Signature system's proposed approach computes case-specific stopping rules from actual parameters; the companion Signature Edition record specifies the stopping-calculator protocol.",
 "key_points": [
  "The classical 1/e rule maximizes best-candidate probability under strict assumptions.",
  "Realistic variants (unknown n, costs, recall, adversarial order) fragment the theory.",
  "The 37 percent rule is applied as folklore far outside its assumptions.",
  "Optimal stopping with frictions lacks a unified practical theory.",
 ],
 "requirements": [
  "Estimated arrival-process parameters, not assumed ones.",
  "Case-specific threshold rules with stated success probabilities.",
  "Refusal to emit folklore rules when assumptions fail.",
 ],
 "citations": [
  "Ferguson TS (1989) Who solved the secretary problem? Statistical Science 4(3).",
 ],
 "demo": {"coords": [[0,0],[6,2],[3,5],[5,1],[1,3]]},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "or-bandits",
 "name": "The Multi-Armed Bandit Lower Bound Problem",
 "group": "Stochastic Models",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "When learning while earning - testing options that also pay - what is the minimum unavoidable regret, and do practical algorithms achieve it?",
 "background": "Lai and Robbins (1985) established the logarithmic lower bound: any consistent bandit policy suffers regret growing at least like log n, with a constant depending on the gaps between arms. UCB and Thompson sampling achieve the bound asymptotically, which sounds like closure - but the constants matter, finite-time performance differs wildly, and the extensions (contextual, nonstationary, adversarial bandits) reopen everything. The adversarial bandit lower bounds (Auer et al., 2002) and the best-of-both-worlds quest show the frontier is alive. Practitioners face a further gap: the theory assumes stationary rewards, while ad auctions and recommendations drift.",
 "why_it_matters": "Clinical trials, ad placement, and dynamic pricing are all bandits: every exploration costs real money or real health. Knowing the minimum price of learning tells you when to stop paying it.",
 "sig_lens": "The Signature lens reads bandits as tuition accounting: exploration is tuition paid for information, and the ledger must show what each lesson cost.",
 "sig_solution": LABEL + " Assumptions: (1) the Lai-Robbins bound is asymptotic; finite-time constants decide practice; (2) real rewards drift. Reasoning path: run bandits with a tuition ledger - track cumulative regret against the theoretical minimum in real time and stop exploring when the tuition exceeds the lesson's value. Proposed mechanism: a tuition-ledger protocol that computes running regret versus the instance-dependent lower bound, switches from exploration to exploitation when marginal information value drops below cost, and reports the tuition paid per deployment. Confirm: ledgered bandits waste less exploration on solved problems. Kill: lower-bound estimates are too loose to guide stopping. Does NOT claim: beating the lower bound - it stops paying tuition when the lessons stop being worth it.",
 "pointer": "The Signature system's proposed approach ledgers exploration tuition against the theoretical minimum; the companion Signature Edition record specifies the tuition-ledger protocol.",
 "key_points": [
  "Lai-Robbins: regret grows at least logarithmically with an instance-dependent constant.",
  "UCB and Thompson sampling achieve the bound asymptotically.",
  "Finite-time constants and nonstationary rewards reopen the practical problem.",
  "Adversarial bandits have their own active frontier.",
 ],
 "requirements": [
  "Running regret tracked against the instance-dependent lower bound.",
  "Exploration-stopping rules based on marginal information value.",
  "Per-deployment tuition reports.",
 ],
 "citations": [
  "Lai TL, Robbins H (1985) Asymptotically efficient adaptive allocation rules. Advances in Applied Mathematics 6(1).",
  "Auer P et al. (2002) The nonstochastic multiarmed bandit problem. SIAM J. Computing 32(1).",
 ],
 "demo": {"coords": [[0,0],[4,4],[7,1],[2,6],[6,5]]},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "or-online-matching",
 "name": "The Online Bipartite Matching Problem",
 "group": "Optimization",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "When one side of a market arrives online - ad impressions, ride requests - how well can any algorithm match them without seeing the future?",
 "background": "Karp, Vazirani and Vazirani (1990) proved the elegant RANKING algorithm achieves a 1 - 1/e competitive ratio for online bipartite matching, and that no randomized algorithm beats it - a rare closed problem. But the applications immediately break the closure: vertex weights (ad values), stochastic arrivals, reusable resources (a driver serves many rides), and fairness constraints each reopen the question. The AdWords problem, display advertising, and ride-sharing run on these extensions, where the optimal competitive ratios are partially known and the gaps matter in billions of dollars. The frontier is a patchwork of special cases, not a theory.",
 "why_it_matters": "Ad markets and ride platforms match supply to demand online at planetary scale. Each basis point of competitive ratio is real money and real served demand.",
 "sig_lens": "The Signature lens reads online matching as triage: with the future hidden, the protocol must decide which arrivals are worth the match and which to let pass.",
 "sig_solution": LABEL + " Assumptions: (1) the 1-1/e bound is tight for the vanilla problem only; (2) real arrivals carry learnable structure. Reasoning path: keep the RANKING guarantee as the floor and layer arrival forecasting on top, with the forecast's value measured, not assumed. Proposed mechanism: a triage protocol that runs the optimal worst-case matcher by default, engages forecast-guided matching only when arrival predictions clear an accuracy bar, and reports the competitive ratio achieved versus the theoretical floor. Confirm: triage matching beats pure worst-case on real arrival streams. Kill: arrival structure proves unlearnable and the forecasting layer is dead weight. Does NOT claim: beating 1-1/e in the worst case - it earns the average case above the floor.",
 "pointer": "The Signature system's proposed approach floors matching on the optimal worst-case algorithm and layers gated forecasts; the companion Signature Edition record specifies the triage protocol.",
 "key_points": [
  "RANKING achieves 1-1/e competitively and no algorithm beats it - a closed case.",
  "Weights, stochastic arrivals, reusability, and fairness each reopen the problem.",
  "AdWords and ride-sharing run on these partially-mapped extensions.",
  "The frontier is a patchwork of special cases.",
 ],
 "requirements": [
  "The optimal worst-case matcher as the non-negotiable floor.",
  "Arrival forecasts gated on measured accuracy.",
  "Achieved-versus-theoretical competitive ratio reporting.",
 ],
 "citations": [
  "Karp RM, Vazirani UV, Vazirani VV (1990) An optimal algorithm for on-line bipartite matching. STOC.",
 ],
 "demo": {"coords": [[0,0],[1,5],[4,2],[6,6],[3,1]]},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "or-newsvendor",
 "name": "The Newsvendor Problem Extensions",
 "group": "Stochastic Models",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "The single-period newsvendor has a clean critical-fractile answer - so why do its realistic extensions (risk aversion, competition, behavioral biases) resist clean solutions?",
 "background": "The newsvendor - order once before uncertain demand, balancing overage against underage costs - solves via the critical fractile: order the quantile where the underage-to-total cost ratio falls. It is the atom of inventory theory. But reality adds: risk-averse objectives (the fractile assumes risk neutrality), competing newsvendors, behavioral pull-to-center bias (Schweitzer and Cachon, 2000, showed humans systematically order between mean and optimum), censored demand (lost sales hide true demand), and multi-product substitution. Each extension has partial answers; the integrated problem - behavioral, competitive, censored, risk-averse ordering - has no closed form and no agreed normative benchmark.",
 "why_it_matters": "Fashion, perishables, and event inventory are newsvendor problems with real spoilage and stockouts. The behavioral gap alone - humans ordering off-optimum - costs the industry systematically.",
 "sig_lens": "The Signature lens reads the newsvendor as a bet slip: the order quantity is a wager, and the protocol must show the odds, the stake, and the bettor's bias.",
 "sig_solution": LABEL + " Assumptions: (1) the critical fractile is the right benchmark, not the observed behavior; (2) censored demand hides the distribution being optimized. Reasoning path: debias the inputs (uncensor demand, correct pull-to-center) before optimizing, and report the order with its assumption ledger. Proposed mechanism: a bet-slip protocol that uncensors demand data, applies behavioral debiasing to human-set orders, computes the fractile on the corrected distribution, and prints the expected cost of the behavioral deviation. Confirm: debiased ordering cuts the behavioral cost gap. Kill: uncensoring introduces more error than the bias it removes. Does NOT claim: a closed form for the full behavioral-competitive problem - it prices the deviations from the clean benchmark.",
 "pointer": "The Signature system's proposed approach debiases newsvendor inputs and prices behavioral deviations; the companion Signature Edition record specifies the bet-slip protocol.",
 "key_points": [
  "The critical fractile solves the risk-neutral single-period problem cleanly.",
  "Humans exhibit pull-to-center bias, ordering between mean and optimum.",
  "Censored demand (lost sales) hides the true demand distribution.",
  "Risk aversion, competition, and substitution lack integrated closed forms.",
 ],
 "requirements": [
  "Demand uncensoring before any optimization.",
  "Behavioral debiasing with measured bias parameters.",
  "Expected-cost reporting of deviations from the fractile benchmark.",
 ],
 "citations": [
  "Schweitzer ME, Cachon GP (2000) Decision bias in the newsvendor problem. Management Science 46(3).",
 ],
 "demo": {"coords": [[0,0],[5,5],[2,1],[4,3],[6,0]]},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "or-branch-bound",
 "name": "The Branch and Bound Node Selection Problem",
 "group": "Optimization",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "In branch-and-bound search, which node should be explored next - and is there a selection rule that is provably near-optimal across problem classes?",
 "background": "Branch-and-bound is the engine of integer programming: relax, bound, branch, prune. Node selection (best-bound, depth-first, hybrid) dramatically affects performance - the same instance can solve in seconds or hours depending on the rule. Yet selection theory is thin: best-bound minimizes the number of nodes in an idealized model, depth-first finds feasible solutions fast, and modern solvers use elaborate hybrids tuned by hand. Machine-learning-guided selection is emerging but brittle. The fundamental question - a selection rule with guarantees across heterogeneous instances - is open, and practitioners rely on solver defaults they cannot explain.",
 "why_it_matters": "Every integer program solved in industry - scheduling, routing, network design - runs branch-and-bound. Node selection is the steering wheel, and it is currently steered by folklore.",
 "sig_lens": "The Signature lens reads node selection as search triage: the protocol must spend the search budget where the bound is most likely to move.",
 "sig_solution": LABEL + " Assumptions: (1) no universal selection rule exists yet; (2) instance features predict which rule wins. Reasoning path: learn a per-instance selection policy from solved-instance features, but keep a safe default the learner cannot override into pathology. Proposed mechanism: a triage protocol that extracts cheap instance features, consults a learned selection policy with a best-bound safety fallback, and logs the policy's choices for post-hoc audit. Confirm: learned-with-fallback selection beats fixed rules on heterogeneous benchmarks. Kill: the learner overfits benchmark features and the fallback fires constantly. Does NOT claim: an optimal universal rule - it adapts per instance with a safety net.",
 "pointer": "The Signature system's proposed approach learns per-instance node selection with a best-bound safety fallback; the companion Signature Edition record specifies the triage protocol.",
 "key_points": [
  "Node selection can change solve times from seconds to hours on the same instance.",
  "Best-bound is node-minimal in idealized models; depth-first finds solutions fast.",
  "Modern solvers use hand-tuned hybrids with thin theoretical backing.",
  "ML-guided selection is emerging but brittle across instance classes.",
 ],
 "requirements": [
  "Cheap instance features computed before selection begins.",
  "A learned policy with a provable safety fallback.",
  "Audit logs of selection decisions for post-hoc analysis.",
 ],
 "citations": [
  "Wolsey LA (2020) Integer Programming, 2nd ed. Wiley.",
 ],
 "demo": {"coords": [[0,0],[3,2],[6,5],[1,4],[5,1]]},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "or-cutting-planes",
 "name": "The Cutting Plane Closure Problem",
 "group": "Optimization",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Which families of cutting planes should be generated, in what order, to close the integrality gap fastest - and can the closure process itself be optimized?",
 "background": "Cutting planes tighten LP relaxations toward integer optima: Gomory cuts, cover cuts, flow cuts, each a subfield. Modern solvers generate dozens of cut families, but the orchestration - which cuts, how many rounds, when to stop cutting and start branching - is heuristic art. Cut selection affects both bound improvement and LP solve time (too many cuts bloat the tableau). The theory of cut closure (how many rounds to reach the integer hull) gives worst-case bounds that are astronomically loose. Learning-based cut selection is new and promising but unproven at scale.",
 "why_it_matters": "Cutting planes are half of branch-and-cut, the dominant exact method. Better cut orchestration directly converts to solved instances and saved compute.",
 "sig_lens": "The Signature lens reads cuts as chisels: each cut removes infeasible space, and the protocol must track what each chisel stroke actually bought.",
 "sig_solution": LABEL + " Assumptions: (1) cut families have instance-dependent value; (2) cut bloat is a real cost. Reasoning path: price every cut round - bound improvement per unit of LP time - and stop cutting when the price exceeds branching. Proposed mechanism: a chisel-ledger protocol that scores each cut family by bound-gain-per-second on the current instance, allocates cut rounds to the winners, and switches to branching when marginal gains fall below a threshold. Confirm: ledgered cut orchestration closes gaps faster on benchmarks. Kill: scoring overhead exceeds the gains. Does NOT claim: optimal cut selection - it prices the strokes adaptively.",
 "pointer": "The Signature system's proposed approach prices cut rounds by bound-gain-per-second and stops cutting when branching pays better; the companion Signature Edition record specifies the chisel-ledger protocol.",
 "key_points": [
  "Cut orchestration (which families, how many rounds) is heuristic art.",
  "Too many cuts bloat LPs; too few leave gaps open.",
  "Closure theory gives worst-case bounds too loose to guide practice.",
  "Learning-based cut selection is promising but unproven at scale.",
 ],
 "requirements": [
  "Per-round measurement of bound improvement versus LP time cost.",
  "Adaptive allocation of cut rounds to winning families.",
  "A principled cut-to-branch switching threshold.",
 ],
 "citations": [
  "Conforti M, Cornuejols G, Zambelli G (2014) Integer Programming. Springer.",
 ],
 "demo": {"coords": [[0,0],[2,4],[5,1],[4,6],[7,3]]},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "or-column-generation",
 "name": "The Column Generation Convergence Problem",
 "group": "Optimization",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Column generation solves huge LPs by generating variables on demand - but why does it tail off so badly, and can the convergence be fixed in general?",
 "background": "Column generation (Gilmore-Gomory, Dantzig-Wolfe) handles problems with astronomically many variables by pricing new columns into a restricted master problem. The curse is the tailing-off effect: rapid early progress, then hundreds of iterations crawling toward optimality as dual values oscillate. Stabilization methods (bundle methods, interior-point stabilization, du Merle et al.) tame the oscillation but add complexity and parameters. The convergence rate theory is weak - no general bounds predict the tail length - and practitioners stop early on dual gaps they cannot certify. Degeneracy in the master problem is the deep cause, and it is structural, not incidental.",
 "why_it_matters": "Crew scheduling, vehicle routing, and cutting stock all run column generation. The tail consumes most of the compute while contributing the least progress.",
 "sig_lens": "The Signature lens reads the tail as oscillation debt: the duals wobble, and the protocol must damp the wobble instead of chasing it.",
 "sig_solution": LABEL + " Assumptions: (1) tailing-off is structural (degeneracy), not a tuning failure; (2) stabilization helps but is fiddly. Reasoning path: detect oscillation early and switch stabilization regimes automatically, with the switch governed by measured dual stability. Proposed mechanism: a damping protocol that monitors dual oscillation amplitude, engages stabilization when amplitude exceeds a threshold, and certifies the final dual gap before termination - never stopping on iteration counts. Confirm: adaptive damping cuts tail iterations on benchmark decompositions. Kill: stabilization overhead dominates on easy instances. Does NOT claim: a general convergence rate - it manages the oscillation it can measure.",
 "pointer": "The Signature system's proposed approach damps dual oscillation adaptively and certifies dual gaps; the companion Signature Edition record specifies the damping protocol.",
 "key_points": [
  "Tailing-off: fast early progress, then hundreds of crawling iterations.",
  "Dual oscillation from master degeneracy is the structural cause.",
  "Stabilization methods help but add complexity and parameters.",
  "No general convergence-rate theory predicts tail length.",
 ],
 "requirements": [
  "Dual-oscillation monitoring during column generation.",
  "Automatic stabilization engagement on measured instability.",
  "Termination on certified dual gaps, never on iteration counts.",
 ],
 "citations": [
  "Desaulniers G, Desrosiers J, Solomon MM (2005) Column Generation. Springer.",
 ],
 "demo": {"coords": [[0,0],[6,1],[3,4],[5,6],[1,2]]},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "or-minlp",
 "name": "The Mixed Integer Nonlinear Programming Problem",
 "group": "Optimization",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "How can problems with both discrete choices and nonlinear physics be solved to global optimality - and where is the boundary of the tractable?",
 "background": "MINLP - integer variables plus nonlinear functions - is the natural language of engineering design: discrete equipment choices with nonlinear thermodynamics, network topology with nonlinear flows. Convex MINLP is manageable (outer approximation, Benders); nonconvex MINLP needs spatial branch-and-bound with convex relaxations (McCormick envelopes), and the relaxations are often too weak to close gaps. Global solvers (BARON, SCIP) handle moderate instances; industrial ones remain out of reach. The boundary between tractable and hopeless is unmapped: problem structure (separability, sparsity) matters enormously but unpredictably.",
 "why_it_matters": "Chemical plants, power grids, and supply chains are MINLPs. The gap between local optima (easy) and global optima (hard) is the difference between a good design and the best one.",
 "sig_lens": "The Signature lens reads MINLP as two hard problems shaking hands: the protocol must let the discrete and continuous sides negotiate instead of fighting.",
 "sig_solution": LABEL + " Assumptions: (1) nonconvex relaxations are often too weak; (2) structure (separability, sparsity) decides tractability. Reasoning path: profile the nonlinearity first - measure separability and relaxation tightness - then choose the weapon (convex methods, spatial branching, or heuristic) the profile licenses. Proposed mechanism: a negotiation protocol that builds tightness profiles of the nonlinear terms, applies spatial branching only where relaxations are loose, and reports the global-optimality gap honestly where it cannot close. Confirm: profile-guided MINLP closes more gaps per hour on engineering instances. Kill: profiling costs more than it saves. Does NOT claim: tractability of general nonconvex MINLP - it aims the weapons where they work.",
 "pointer": "The Signature system's proposed approach profiles nonlinearity tightness and aims global methods where relaxations are loose; the companion Signature Edition record specifies the negotiation protocol.",
 "key_points": [
  "Convex MINLP is manageable; nonconvex needs spatial branch-and-bound.",
  "McCormick relaxations are often too weak to close gaps.",
  "Global solvers handle moderate instances; industrial scale stays out of reach.",
  "The tractability boundary is unmapped and structure-dependent.",
 ],
 "requirements": [
  "Nonlinearity tightness profiles before solver selection.",
  "Spatial branching concentrated where relaxations are loose.",
  "Honest global-optimality gap reporting where closure fails.",
 ],
 "citations": [
  "Belotti P et al. (2013) Mixed-integer nonlinear optimization. Acta Numerica 22.",
 ],
 "demo": {"coords": [[0,0],[4,3],[1,5],[6,2],[3,6]]},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "or-stochastic-programming",
 "name": "The Stochastic Programming Scenario Problem",
 "group": "Stochastic Models",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "How many scenarios - and which ones - suffice to represent uncertainty faithfully in a stochastic program without exploding its size?",
 "background": "Stochastic programming optimizes expected costs over scenario trees, but the tree is the problem: too few scenarios and the solution is fiction; too many and the extensive form is unsolvable. Scenario generation (sampling, moment matching) and reduction (heuristics to prune trees) are more art than science - stability tests (Kaut and Wallace, 2007) check whether the optimal value is stable across trees, but stability of the value does not imply stability of the decision. The fundamental question - how to certify that a scenario set supports the decision being made - is open, and practitioners routinely optimize against trees that would not survive scrutiny.",
 "why_it_matters": "Energy planning, finance, and logistics bet billions on stochastic programs. A scenario tree that misrepresents uncertainty manufactures confident, wrong decisions.",
 "sig_lens": "The Signature lens reads scenarios as witnesses: the tree must be cross-examined for whether it can support the verdict being asked of it.",
 "sig_solution": LABEL + " Assumptions: (1) value stability does not imply decision stability; (2) scenario count is usually chosen by computational budget, not fidelity. Reasoning path: test the tree against the decision - perturb and regrow scenarios and check whether the recommended decision survives. Proposed mechanism: a witness protocol that requires decision-stability testing (the first-stage decision must persist across independently grown trees), reports the stability margin, and refuses to recommend decisions that flip across trees. Confirm: stability-tested recommendations perform better out-of-sample. Kill: stability testing costs more than the original solve. Does NOT claim: the true distribution - it certifies the decision against tree variation.",
 "pointer": "The Signature system's proposed approach certifies stochastic decisions by tree-regrowth stability; the companion Signature Edition record specifies the witness protocol.",
 "key_points": [
  "Scenario trees trade fidelity against solvability with no principled exchange rate.",
  "Value stability across trees does not imply decision stability.",
  "Scenario reduction is heuristic; its effect on decisions is unmeasured.",
  "Practitioners optimize against trees chosen by budget, not fidelity.",
 ],
 "requirements": [
  "Decision-stability testing across independently grown scenario trees.",
  "Stability margins reported with every recommendation.",
  "Refusal to recommend decisions that flip across trees.",
 ],
 "citations": [
  "Kaut M, Wallace SW (2007) Evaluation of scenario-generation methods for stochastic programming. Pacific J. Optimization 3(2).",
 ],
 "demo": {"coords": [[0,0],[5,2],[2,6],[6,4],[3,1]]},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "or-robust-optimization",
 "name": "The Robust Optimization Conservatism Problem",
 "group": "Stochastic Models",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Robust optimization protects against worst cases - but how can it avoid paying for protection against cases that will never happen?",
 "background": "Robust optimization (Ben-Tal and Nemirovski; Bertsimas and Sim) replaces distributions with uncertainty sets and optimizes the worst case inside them - no probabilities needed. The price is conservatism: box uncertainty sets protect against simultaneous worst cases in all dimensions, an event of negligible probability, yielding solutions far more expensive than necessary. Budgeted uncertainty sets (Bertsimas and Sim, 2004) limit how many parameters can go bad at once, taming the conservatism with a tunable parameter Gamma. But choosing the set shape and size remains more art than science, and the gap between robust and stochastic solutions is poorly characterized - practitioners cannot tell what the robustness costs them.",
 "why_it_matters": "Robustness without calibration is paranoia with a budget: overprotected supply chains and portfolios leave money on the table systematically.",
 "sig_lens": "The Signature lens reads robustness as insurance: the premium must be priced against the risk, and the policy must exclude alien invasions.",
 "sig_solution": LABEL + " Assumptions: (1) worst-case protection against impossible coincidences is waste; (2) set choice is currently unpriced art. Reasoning path: price the robustness - compute what the protection costs versus the stochastic optimum, and let decision-makers buy exactly the coverage they want. Proposed mechanism: an insurance protocol that reports the price of robustness (robust cost minus nominal cost) for a menu of uncertainty sets, ties set size to historical violation frequencies, and requires the premium to be signed off. Confirm: priced robustness cuts over-conservatism without increasing violations. Kill: historical frequencies mislead about future extremes. Does NOT claim: optimal uncertainty sets - it makes the premium explicit and revisable.",
 "pointer": "The Signature system's proposed approach prices robustness as an insurance premium on a menu of sets; the companion Signature Edition record specifies the insurance protocol.",
 "key_points": [
  "Box uncertainty sets overprotect against negligible-probability coincidences.",
  "Budgeted sets tame conservatism via the tunable Gamma parameter.",
  "Set shape and size choice remains unpriced art.",
  "The robust-versus-stochastic cost gap is rarely measured.",
 ],
 "requirements": [
  "Price-of-robustness reporting against the nominal optimum.",
  "Uncertainty sets calibrated to historical violation frequencies.",
  "Signed-off robustness premiums per decision.",
 ],
 "citations": [
  "Bertsimas D, Sim M (2004) The price of robustness. Operations Research 52(1).",
 ],
 "demo": {"coords": [[0,0],[3,5],[6,2],[2,1],[5,4]]},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "or-multiobjective",
 "name": "The Multi-Objective Pareto Frontier Problem",
 "group": "Decision Analysis",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "When cost, quality, and sustainability conflict, how can the full set of undominated tradeoffs be computed - and how should a decision-maker choose among them?",
 "background": "Multi-objective optimization seeks the Pareto frontier: solutions no other solution beats on all objectives. Computing the full frontier is intractable beyond two or three objectives - the frontier grows exponentially and visualization fails. Scalarization (weighted sums) finds only convex parts of the frontier; evolutionary algorithms (NSGA-II, Deb et al., 2002) approximate it without guarantees. The deeper problem is decision support: even a computed frontier needs a choice, and preference elicitation (what the decision-maker actually values) is its own unsolved problem - stated preferences shift under framing, and revealed preferences contradict them.",
 "why_it_matters": "Every real decision trades objectives: cost against resilience, profit against emissions. Optimizing one objective while ignoring the rest is not optimization - it is negligence with mathematics.",
 "sig_lens": "The Signature lens reads the frontier as a menu: the optimizer's job is to present the real choices honestly, and the chooser's job is to own the choice.",
 "sig_solution": LABEL + " Assumptions: (1) full frontiers are intractable beyond low dimensions; (2) preference elicitation is unstable. Reasoning path: compute a representative, diverse frontier approximation and support the choice with interactive tradeoff exploration rather than a single answer. Proposed mechanism: a menu protocol that generates a diverse set of Pareto candidates, presents them through interactive tradeoff sliders showing what each choice sacrifices, and records the final selection with its sacrificed alternatives. Confirm: menu-supported decisions show less post-hoc regret. Kill: decision-makers satisfice on the first reasonable option and the menu is theater. Does NOT claim: the true frontier or true preferences - it makes the tradeoff explicit and owned.",
 "pointer": "The Signature system's proposed approach presents diverse Pareto menus with interactive tradeoff exploration; the companion Signature Edition record specifies the menu protocol.",
 "key_points": [
  "Full Pareto frontiers are intractable beyond two or three objectives.",
  "Weighted-sum scalarization misses non-convex frontier regions.",
  "Evolutionary methods approximate without guarantees.",
  "Preference elicitation is unstable under framing.",
 ],
 "requirements": [
  "Diverse (not just optimal) Pareto candidate sets.",
  "Interactive tradeoff exploration showing sacrificed alternatives.",
  "Recorded selections with their opportunity costs.",
 ],
 "citations": [
  "Deb K et al. (2002) A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE TEVC 6(2).",
 ],
 "demo": {"coords": [[0,0],[4,1],[1,3],[5,5],[2,6]]},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "or-dynamic-pricing",
 "name": "The Dynamic Pricing With Strategic Customers Problem",
 "group": "Decision Analysis",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "When customers anticipate price changes and time their purchases strategically, what pricing policy is optimal - and can it avoid training customers to wait?",
 "background": "Classical dynamic pricing assumes myopic customers; real ones strategize - waiting for the sale, abandoning carts to trigger discounts. The strategic-customer literature (Besanko and Winston; Aviv and Pazgal) shows optimal policies must account for customer patience and beliefs, turning pricing into a game. Commitment (announced price paths) can beat flexibility, but commitment is hard to make credible. Learning customer strategicness from data is confounded: observed waiting mixes patience with ignorance. The result is an arms race of promotions that trains exactly the waiting behavior sellers want to avoid - the industry's open secret.",
 "why_it_matters": "Airlines, retailers, and hotels price dynamically against strategic buyers. Mispricing the game does not just lose margin - it teaches customers that waiting pays.",
 "sig_lens": "The Signature lens reads pricing as a repeated game: every discount is a move that teaches the opponent, and the protocol must track what is being taught.",
 "sig_solution": LABEL + " Assumptions: (1) customers learn from the price path; (2) commitment beats flexibility but is hard to credibly make. Reasoning path: model the teaching effect explicitly - estimate how each promotion shifts future waiting propensity - and price the long game, not the period. Proposed mechanism: a repeated-game protocol that tracks a customer-waiting index, penalizes promotions that raise it, and tests commitment devices (price guarantees, announced paths) against flexible pricing in controlled experiments. Confirm: game-aware pricing sustains margins better than myopic optimization. Kill: waiting propensity proves unmeasurable and the index is noise. Does NOT claim: a solved game - it prices the teaching effect into each move.",
 "pointer": "The Signature system's proposed approach tracks what each promotion teaches customers and prices the long game; the companion Signature Edition record specifies the repeated-game protocol.",
 "key_points": [
  "Strategic customers time purchases, breaking myopic pricing models.",
  "Optimal policies must account for patience and beliefs - a game, not an optimization.",
  "Commitment can beat flexibility but is hard to make credible.",
  "Promotions train the waiting behavior sellers want to avoid.",
 ],
 "requirements": [
  "A measured customer-waiting index tracked over time.",
  "Promotion decisions priced with their teaching effect.",
  "Controlled experiments comparing commitment versus flexible pricing.",
 ],
 "citations": [
  "Aviv Y, Pazgal A (2008) Optimal pricing of seasonal products in the presence of forward-looking consumers. M&SOM 10(3).",
 ],
 "demo": {"coords": [[0,0],[6,3],[2,5],[4,1],[1,4]]},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "or-revenue-management",
 "name": "The Revenue Management Network Problem",
 "group": "Decision Analysis",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Airlines sell itineraries that consume multiple flight legs - how should shared capacity be allocated across a network when each product uses several scarce resources?",
 "background": "Single-leg revenue management (EMSR, Littlewood) is textbook-solved; the network problem - bid prices per leg, itinerary valuation across legs - is not. Displacement costs (accepting a connecting passenger displaces local ones) couple the legs, and the standard decomposition methods (deterministic LP bid prices, probabilistic bid prices) are approximations with unmeasured gaps. Choice behavior (customers buy down to cheaper options when denied) further entangles the network. Airlines run these approximations daily on billions in revenue; the optimality gap of network RM is one of the industry's most expensive unknowns.",
 "why_it_matters": "Network revenue management prices the world's airline seats. The approximation gap is a direct tax on airline revenue - and on passengers who pay its prices.",
 "sig_lens": "The Signature lens reads the network as shared plumbing: every itinerary drinks from several pipes, and the protocol must price each sip at its displacement cost.",
 "sig_solution": LABEL + " Assumptions: (1) leg coupling through displacement is the core difficulty; (2) choice behavior entangles the network further. Reasoning path: measure the approximation gap directly via simulation, then allocate exact effort to the legs where the gap concentrates. Proposed mechanism: a plumbing protocol that computes displacement-cost bid prices, simulates the policy against the true choice model to measure the gap, and re-optimizes bid prices on the legs contributing most to the gap. Confirm: gap-targeted re-optimization lifts network revenue over static bid prices. Kill: the true choice model proves unknowable and the simulation misleads. Does NOT claim: optimal network control - it aims exact effort at the measured gap.",
 "pointer": "The Signature system's proposed approach measures the network RM gap by simulation and re-optimizes where it concentrates; the companion Signature Edition record specifies the plumbing protocol.",
 "key_points": [
  "Single-leg RM is solved; network coupling through displacement is not.",
  "Deterministic and probabilistic bid prices are approximations with unmeasured gaps.",
  "Buy-down choice behavior entangles legs further.",
  "The optimality gap is an expensive industry unknown.",
 ],
 "requirements": [
  "Displacement-cost bid prices per network leg.",
  "Simulation-measured optimality gaps against choice models.",
  "Gap-concentrated re-optimization of bid prices.",
 ],
 "citations": [
  "Talluri KT, van Ryzin GJ (2004) The Theory and Practice of Revenue Management. Springer.",
 ],
 "demo": {"coords": [[0,0],[2,2],[5,5],[6,1],[3,4]]},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "or-bullwhip",
 "name": "The Supply Chain Bullwhip Quantification Problem",
 "group": "Stochastic Models",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Why do small demand fluctuations amplify into wild order swings upstream - and can the amplification be measured and tamed in real supply chains?",
 "background": "Forrester (1961) observed the bullwhip: order variance grows moving upstream from retailer to factory. Lee, Padmanabhan and Whang (1997) identified four causes - demand signal processing, rationing gaming, order batching, and price fluctuations - each with countermeasures (information sharing, everyday low pricing). Yet quantification in real chains remains hard: the amplification is confounded with genuine demand shifts, seasonality, and promotions, and most firms lack the end-to-end visibility to measure it. The beer game (Sterman, 1989) shows the effect is behavioral as much as structural - humans amplify even with full information.",
 "why_it_matters": "The bullwhip manufactures phantom demand that idles factories and then starves them: inventory gluts followed by shortages, the most expensive rhythm in operations.",
 "sig_lens": "The Signature lens reads the bullwhip as an echo chamber: each tier shouts what it heard, and the protocol must replace shouting with a shared signal.",
 "sig_solution": LABEL + " Assumptions: (1) amplification has structural and behavioral causes; (2) most chains lack end-to-end visibility to measure it. Reasoning path: instrument the chain with shared demand signals, measure amplification tier by tier, and attack the largest measured cause first. Proposed mechanism: an echo-measurement protocol that computes order-to-demand variance ratios at each tier from shared point-of-sale data, attributes amplification to the four Lee causes via designed experiments, and deploys countermeasures in measured-priority order. Confirm: measured-priority countermeasures dampen amplification more than blanket information sharing. Kill: firms refuse to share the data the measurement needs. Does NOT claim: elimination of the bullwhip - it measures the echo and damps the loudest cause first.",
 "pointer": "The Signature system's proposed approach measures amplification tier by tier and attacks the largest cause first; the companion Signature Edition record specifies the echo-measurement protocol.",
 "key_points": [
  "Order variance amplifies upstream from retailer to factory (Forrester, 1961).",
  "Four causes identified: signal processing, rationing gaming, batching, price fluctuation.",
  "Real-chain quantification is confounded with genuine demand shifts.",
  "The beer game shows the effect is behavioral even with full information.",
 ],
 "requirements": [
  "Shared point-of-sale data across tiers.",
  "Tier-by-tier variance-ratio measurement.",
  "Cause attribution via designed experiments before countermeasures.",
 ],
 "citations": [
  "Lee HL, Padmanabhan V, Whang S (1997) Information distortion in a supply chain: the bullwhip effect. Management Science 43(4).",
  "Sterman JD (1989) Modeling managerial behavior: misperceptions of feedback in a dynamic decision making experiment. Management Science 35(3).",
 ],
 "demo": {"coords": [[0,0],[5,4],[1,2],[4,6],[2,5]]},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "or-rcpsp",
 "name": "The Resource Constrained Project Scheduling Problem",
 "group": "Optimization",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "How should project activities be scheduled when each needs scarce resources - crews, cranes, budget - and precedence constraints chain them together?",
 "background": "RCPSP - schedule activities with precedence and renewable resource limits to minimize makespan - is NP-hard and notoriously difficult: even 60-activity instances challenge exact methods, while real projects run thousands of activities. Branch-and-bound, constraint programming, and metaheuristics all compete; the PSPLIB benchmarks have stood for decades with many instances still open. Real projects add multi-mode activities (fast/cheap tradeoffs), resource calendars, and uncertainty - each a subfield. The practice-theory gap is stark: commercial project software uses simple priority rules while the literature chases exact optima on toy sizes.",
 "why_it_matters": "Construction, shipbuilding, and shutdown maintenance are RCPSPs with nine-figure budgets. The scheduling gap is idle cranes, late delivery, and penalty clauses.",
 "sig_lens": "The Signature lens reads the project as a resource parliament: activities compete for scarce seats, and the protocol must schedule the contention, not just the precedence.",
 "sig_solution": LABEL + " Assumptions: (1) exact methods stall far below real project sizes; (2) resource contention, not precedence, usually binds. Reasoning path: solve the resource contention explicitly - identify the contested resources and sequence their claimants - then fit precedence around the contention schedule. Proposed mechanism: a contention protocol that profiles resource criticality, sequences claimants on bottleneck resources via exact subproblems, and schedules remaining activities with priority rules around the contention core. Confirm: contention-first schedules beat pure priority rules on makespan. Kill: contention shifts unpredictably as the project executes. Does NOT claim: optimal project schedules - it aims exact effort at the binding contention.",
 "pointer": "The Signature system's proposed approach sequences bottleneck-resource claimants exactly and schedules around them; the companion Signature Edition record specifies the contention protocol.",
 "key_points": [
  "RCPSP is NP-hard; exact methods stall around 60 activities.",
  "PSPLIB benchmarks have open instances decades old.",
  "Multi-mode, calendars, and uncertainty each spawn subfields.",
  "Commercial software uses simple priority rules far from the literature.",
 ],
 "requirements": [
  "Resource-criticality profiling before scheduling.",
  "Exact sequencing of bottleneck-resource claimants.",
  "Makespan-gap reporting against lower bounds.",
 ],
 "citations": [
  "Kolisch R, Sprecher A (1997) PSPLIB - a project scheduling problem library. EJOR 96(1).",
 ],
 "demo": {"coords": [[0,0],[3,6],[6,3],[2,2],[5,0]]},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "or-crew-scheduling",
 "name": "The Crew Scheduling Set Partitioning Problem",
 "group": "Optimization",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "How should airline crews be assigned to flights so every flight is covered exactly once at minimum cost under labyrinthine labor rules?",
 "background": "Crew scheduling is the flagship of column generation: pairings (crew itineraries) are generated by the millions, and a set-partitioning master problem selects the covering set. The labor rules - duty limits, rest requirements, base constraints - make pairing generation itself a constrained shortest-path problem. Integrated problems (crew scheduling with rostering, with aircraft routing, with disruptions) multiply the difficulty. Solutions save airlines tens of millions, yet the models are brittle: a weather disruption invalidates the optimal plan, and recovery (disruption management) is a separate, less mature field. The integration frontier - planning that anticipates disruption - is largely open.",
 "why_it_matters": "Crew costs are an airline's second-largest expense. The scheduling gap is paid in crew salaries, deadheads, and disruption chaos.",
 "sig_lens": "The Signature lens reads crew schedules as promises to people: the optimizer must price not just cost but the human cost of the plan's brittleness.",
 "sig_solution": LABEL + " Assumptions: (1) set-partitioning solves the static problem well; (2) disruption brittleness is the real cost driver. Reasoning path: build recovery into the plan - generate pairings with slack positioned where disruptions historically strike, and price the slack explicitly. Proposed mechanism: a promise protocol that solves the set-partitioning core, then injects disruption-informed slack (swap options, reserve positioning) at measured cost, reporting the robustness premium. Confirm: slack-positioned plans recover cheaper from real disruptions. Kill: disruptions strike where history did not predict. Does NOT claim: disruption-proof schedules - it prices robustness against the plan's brittleness.",
 "pointer": "The Signature system's proposed approach positions disruption-informed slack in crew plans and prices it; the companion Signature Edition record specifies the promise protocol.",
 "key_points": [
  "Set-partitioning with column generation is the flagship exact approach.",
  "Labor rules make pairing generation a constrained shortest-path problem.",
  "Integrated planning (rostering, aircraft, disruption) multiplies difficulty.",
  "Disruption recovery is less mature than static planning.",
 ],
 "requirements": [
  "Disruption-history analysis positioning slack where strikes concentrate.",
  "Explicit robustness-premium reporting against the static optimum.",
  "Recovery-option generation alongside the base plan.",
 ],
 "citations": [
  "Barnhart C et al. (2003) Airline crew scheduling. In Handbook of Transportation Science.",
 ],
 "demo": {"coords": [[0,0],[4,5],[7,2],[3,1],[6,6]]},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "or-sdp-rank",
 "name": "The Semidefinite Programming Rank Problem",
 "group": "Optimization",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Semidefinite relaxations give powerful bounds for combinatorial problems - but when does the relaxation return a low-rank (hence meaningful) solution, and when is it just a loose fantasy?",
 "background": "Semidefinite programming - optimizing over positive semidefinite matrices - gives the celebrated Goemans-Williamson 0.878-approximation for max-cut and strong bounds across combinatorial optimization. But the SDP solution is a high-dimensional matrix, not a combinatorial object: rounding extracts the answer, and the rounding loses what the relaxation cannot certify. The rank of the SDP optimum matters enormously - low rank means the relaxation nearly solved the problem; high rank means the bound is loose. Barvinok and Pataki bound the rank, but the bounds are worst-case and uninformative in practice. When SDP relaxations are tight versus loose remains poorly understood, and practitioners cannot predict which problems will benefit.",
 "why_it_matters": "SDP is the strongest generic bounding technology in optimization. Knowing when its bounds are tight tells you whether to trust the relaxation or look elsewhere.",
 "sig_lens": "The Signature lens reads SDP rank as a truthfulness meter: low rank means the relaxation is telling the truth about the problem, and the protocol must check the meter before believing.",
 "sig_solution": LABEL + " Assumptions: (1) SDP tightness is instance-dependent and unpredictable; (2) rank is the observable signal of tightness. Reasoning path: measure the rank profile of the SDP solution and condition all downstream decisions on it - trust low-rank relaxations, distrust high-rank ones. Proposed mechanism: a truthfulness protocol that computes the numerical rank of each SDP solution, routes low-rank cases to rounding with confidence, diverts high-rank cases to alternative bounds, and logs the rank-versus-gap relationship to learn tightness predictors. Confirm: rank-routed pipelines close more gaps than blind SDP. Kill: rank proves uncorrelated with gap in practice. Does NOT claim: a characterization of SDP tightness - it measures the meter and acts on it.",
 "pointer": "The Signature system's proposed approach routes SDP solutions by their rank-truthfulness signal; the companion Signature Edition record specifies the truthfulness protocol.",
 "key_points": [
  "SDP gives the Goemans-Williamson 0.878 max-cut approximation and strong general bounds.",
  "The SDP optimum is a matrix; rounding extracts the combinatorial answer with loss.",
  "Low rank signals tightness; high rank signals a loose bound.",
  "Tightness predictability across problems is poorly understood.",
 ],
 "requirements": [
  "Numerical rank computation on every SDP solution.",
  "Rank-conditioned routing: round low-rank, divert high-rank.",
  "Logged rank-versus-gap data to learn tightness predictors.",
 ],
 "citations": [
  "Goemans MX, Williamson DP (1995) Improved approximation algorithms for maximum cut. JACM 42(6).",
 ],
 "demo": {"coords": [[0,0],[2,3],[6,6],[4,1],[1,5]]},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "or-simulation-optimization",
 "name": "The Simulation Optimization Convergence Problem",
 "group": "Stochastic Models",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "When the objective can only be estimated by noisy simulation, what optimization methods converge - and how can convergence be certified when every evaluation is random?",
 "background": "Simulation optimization - optimizing systems evaluable only via Monte Carlo (supply chains, call centers, hospitals) - faces noise at every step: gradient estimates are random, comparisons are statistical, and the optimum itself is a random variable. Methods range from ranking-and-selection through stochastic approximation to surrogate-based Bayesian optimization, each with convergence theory under assumptions (diminishing step sizes, growing sample budgets) that practitioners violate routinely. The certification problem is fundamental: with noisy evaluations, you cannot verify optimality, only bound the probability you are wrong - and the bounds are usually too weak to use.",
 "why_it_matters": "Hospitals, factories, and logistics networks are optimized by simulation. Unverifiable optima are expensive guesses wearing the authority of algorithms.",
 "sig_lens": "The Signature lens reads simulation noise as fog: the optimizer must navigate by instruments that work in fog, and report how thick the fog was.",
 "sig_solution": LABEL + " Assumptions: (1) optimality cannot be verified under noise, only bounded probabilistically; (2) practitioners violate theoretical assumptions routinely. Reasoning path: replace convergence claims with indifference-zone guarantees - certify that the chosen solution is within delta of optimal with stated confidence, and budget simulation to shrink delta. Proposed mechanism: a fog-navigation protocol that allocates simulation budget by the value of information, terminates on achieved indifference-zone guarantees (not iteration counts), and reports the fog thickness (standard errors) alongside every recommendation. Confirm: protocol-guided optimization meets its stated guarantees in practice. Kill: the guarantees prove too weak to be decision-useful. Does NOT claim: certified optimality - it certifies near-optimality with stated confidence.",
 "pointer": "The Signature system's proposed approach certifies indifference-zone guarantees and budgets simulation by information value; the companion Signature Edition record specifies the fog-navigation protocol.",
 "key_points": [
  "Noisy evaluations make optimality unverifiable; only probabilistic bounds exist.",
  "Convergence theory needs assumptions practitioners routinely violate.",
  "Ranking-and-selection, stochastic approximation, and surrogates each have gaps.",
  "Standard stopping rules (iteration counts) certify nothing.",
 ],
 "requirements": [
  "Indifference-zone (delta, confidence) guarantees as the deliverable.",
  "Simulation budgets allocated by value of information.",
  "Fog-thickness (standard error) reporting with every recommendation.",
 ],
 "citations": [
  "Fu MC (2015) Handbook of Simulation Optimization. Springer.",
 ],
 "demo": {"coords": [[0,0],[5,1],[3,4],[6,5],[2,2]]},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "or-ranking-selection",
 "name": "The Ranking and Selection Problem",
 "group": "Stochastic Models",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Given many simulated alternatives, how can the best be selected with a guaranteed probability of correct selection - without simulating everything forever?",
 "background": "Ranking and selection (R&S) is the cleanest corner of simulation optimization: choose the best among k alternatives with probability of correct selection at least 1-alpha. Classical procedures (Rinott, Bechhofer) need an indifference zone - a minimum meaningful difference - and allocate samples in stages. Modern optimal-computing-budget-allocation (OCBA, Chen et al.) maximizes the selection probability per simulation dollar, but the guarantees assume normality and known structures that real simulations violate. The scaling problem is severe: with thousands of alternatives (drug compounds, designs), even OCBA drowns, and screening methods that prune losers early lack tight guarantees.",
 "why_it_matters": "Drug discovery, engineering design, and policy simulation all select among alternatives by simulation. Wrong selection wastes the entire downstream investment.",
 "sig_lens": "The Signature lens reads selection as a tournament: the protocol must run fair brackets, eliminate losers early, and certify the champion.",
 "sig_solution": LABEL + " Assumptions: (1) classical guarantees need an indifference zone and distributional assumptions; (2) thousands of alternatives drown naive procedures. Reasoning path: screen aggressively but accountably - eliminate clear losers with statistical certificates, then concentrate budget on the surviving contenders. Proposed mechanism: a tournament protocol with certified screening rounds (losers eliminated only with stated error control), OCBA-style budget allocation among survivors, and a final champion certified with its probability of correct selection. Confirm: tournament selection meets its stated guarantees on benchmark suites. Kill: screening errors compound and the true best is eliminated early. Does NOT claim: assumption-free guarantees - it certifies within stated assumptions and reports violations.",
 "pointer": "The Signature system's proposed approach runs certified screening tournaments with budget-optimal finals; the companion Signature Edition record specifies the tournament protocol.",
 "key_points": [
  "Classical R&S guarantees need indifference zones and distributional assumptions.",
  "OCBA maximizes selection probability per simulation dollar.",
  "Thousands of alternatives drown even efficient procedures.",
  "Screening methods prune losers early but lack tight guarantees.",
 ],
 "requirements": [
  "Certified screening with stated error control per round.",
  "Budget-optimal allocation among surviving contenders.",
  "Champion certification with probability of correct selection.",
 ],
 "citations": [
  "Chen CH et al. (2000) Simulation budget allocation for further enhancing the efficiency of ordinal optimization. DEDS 10(3).",
 ],
 "demo": {"coords": [[0,0],[1,4],[4,6],[6,2],[3,3]]},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "or-mdp-sample",
 "name": "The Markov Decision Process Sample Complexity Problem",
 "group": "Stochastic Models",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "How many samples does reinforcement learning need to find a near-optimal policy - and do the theoretical bounds bear any resemblance to practical requirements?",
 "background": "The sample complexity of MDPs - how many environment interactions suffice for epsilon-optimal policies - has seen dramatic theoretical progress: from exponential to polynomial bounds, with recent minimax-optimal rates (Azar et al., 2013; Jin et al.). But the bounds hide enormous constants and depend on the discount factor as 1/(1-gamma)^3 or worse, making them vacuous for practical gamma near 1. Function approximation (the deep RL case) largely escapes the theory: linear MDP assumptions buy results, but neural networks have no such guarantees. Practitioners tune by reward curves; the theory cannot tell them whether they have sampled enough.",
 "why_it_matters": "Samples are expensive: robot hours, patient trials, market experiments. Sample-complexity theory should tell practitioners when to stop collecting; instead it tells them numbers with no practical meaning.",
 "sig_lens": "The Signature lens reads samples as tuition: the theory should issue a receipt showing what was bought, not a bound nobody can cash.",
 "sig_solution": LABEL + " Assumptions: (1) minimax bounds have vacuous constants for practical discount factors; (2) function approximation escapes the clean theory. Reasoning path: replace worst-case bounds with instance-adaptive stopping - estimate the policy's suboptimality from data and stop when the estimate clears the bar. Proposed mechanism: a tuition-receipt protocol that tracks empirical Bellman residuals and policy-improvement plateaus, estimates remaining suboptimality, and stops sampling when the estimate plus confidence clears the target - reporting the receipt. Confirm: receipt-stopped training matches fixed-budget performance at lower sample cost. Kill: suboptimality estimates prove unreliable and stopping is premature. Does NOT claim: minimax optimality - it stops on measured, not worst-case, grounds.",
 "pointer": "The Signature system's proposed approach stops RL sampling on measured suboptimality receipts; the companion Signature Edition record specifies the tuition-receipt protocol.",
 "key_points": [
  "Minimax-optimal sample complexity rates exist but with vacuous constants.",
  "Bounds scale as 1/(1-gamma)^3 or worse - meaningless near gamma equals 1.",
  "Deep RL with function approximation largely escapes the theory.",
  "Practitioners cannot tell from theory whether they have sampled enough.",
 ],
 "requirements": [
  "Empirical suboptimality estimation during training.",
  "Stopping rules on measured residuals, not fixed budgets.",
  "Per-run tuition receipts: samples spent versus suboptimality achieved.",
 ],
 "citations": [
  "Azar MG et al. (2013) Minimax PAC bounds on the sample complexity of reinforcement learning. JMLR 14.",
 ],
 "demo": {"coords": [[0,0],[6,4],[2,1],[5,6],[3,3]]},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "or-queueing-network",
 "name": "The Queueing Network Product Form Limit Problem",
 "group": "Stochastic Models",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Jackson networks have elegant product-form solutions - but real networks violate the assumptions, so where exactly does the elegance stop describing reality?",
 "background": "Jackson (1957) proved that networks of exponential queues with Poisson arrivals factor into independent per-node distributions - the product form - enabling exact analysis of complex systems. BCMP extended it to multiple classes. But real networks have general service times, correlated arrivals, finite buffers, and blocking - each breaking product form. Approximation methods (decomposition, diffusion limits) fill the gap without guarantees, and the error of using product-form formulas outside their assumptions is unquantified in practice. Heavy-traffic theory (Harrison, Reiman) gives limits but not the pre-limit accuracy engineers need.",
 "why_it_matters": "Call centers, data centers, and hospitals are queueing networks. Product-form formulas are used far outside their assumptions because nothing better is tractable - and nobody knows the error.",
 "sig_lens": "The Signature lens reads product form as a map of flat country: useful where the terrain is flat, dangerous in the mountains - the protocol must check the terrain.",
 "sig_solution": LABEL + " Assumptions: (1) product-form assumptions fail in real networks; (2) the approximation error is unquantified. Reasoning path: measure the assumption violations directly and bound their effect on the performance estimates - report the answer with its terrain warning. Proposed mechanism: a terrain-check protocol that tests each product-form assumption (exponentiality, independence, infinite buffers) on system data, quantifies violations, and attaches error bands to product-form estimates scaled by violation severity. Confirm: terrain-checked estimates predict real performance better than blind product-form. Kill: violation effects prove non-monotone and the bands mislead. Does NOT claim: exact analysis of general networks - it bounds the map's error by the terrain.",
 "pointer": "The Signature system's proposed approach tests product-form assumptions and bands estimates by violation severity; the companion Signature Edition record specifies the terrain-check protocol.",
 "key_points": [
  "Jackson networks factor beautifully under exponential assumptions.",
  "General service times, correlated arrivals, and blocking break product form.",
  "Approximation errors from misapplied formulas are unquantified.",
  "Heavy-traffic limits do not give the pre-limit accuracy engineers need.",
 ],
 "requirements": [
  "Assumption-violation testing on real system data.",
  "Error bands on product-form estimates scaled by violation severity.",
  "Terrain warnings when violations exceed usable thresholds.",
 ],
 "citations": [
  "Jackson JR (1957) Networks of waiting lines. Operations Research 5(4).",
 ],
 "demo": {"coords": [[0,0],[3,1],[6,3],[2,5],[5,2]]},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "or-maintenance",
 "name": "The Maintenance Optimization With Imperfect Information Problem",
 "group": "Stochastic Models",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "When equipment health is only partially observable - noisy sensors, hidden degradation - what maintenance policy is optimal, and can it be computed?",
 "background": "Classical maintenance optimization (age replacement, block replacement) assumes the equipment age or state is known. Reality is partially observable: vibration sensors are noisy, degradation is hidden, inspections are imperfect. The POMDP formulation is the right model and is computationally brutal - exact solutions scale to toy problems. Practitioners use threshold policies on sensor readings, scheduled maintenance, or run-to-failure, with the optimality gap unmeasured. The emerging condition-based maintenance field adds prognostics (remaining-useful-life prediction) but the integration of noisy prognostics with optimal stopping remains theoretically thin.",
 "why_it_matters": "Unplanned downtime is among industry's largest controllable costs. Maintenance policies based on known-state theory applied to hidden-state reality are systematically mistimed.",
 "sig_lens": "The Signature lens reads maintenance as betting against a hidden clock: the protocol must maintain a belief about the clock and act on the belief, not the noise.",
 "sig_solution": LABEL + " Assumptions: (1) the POMDP is the right model and is intractable; (2) threshold policies on raw sensors are mistimed. Reasoning path: maintain an explicit belief distribution over equipment health, update it with each sensor reading, and trigger maintenance on belief thresholds - not sensor thresholds. Proposed mechanism: a hidden-clock protocol that runs a particle-filter belief over degradation state, computes the belief-threshold policy via approximate dynamic programming, and reports the value of information of each sensor. Confirm: belief-threshold policies beat sensor-threshold policies on simulated degradation. Kill: the degradation model is wrong and beliefs mislead worse than raw sensors. Does NOT claim: optimal POMDP solutions - it acts on principled beliefs with honest model risk.",
 "pointer": "The Signature system's proposed approach maintains health beliefs and triggers maintenance on belief thresholds; the companion Signature Edition record specifies the hidden-clock protocol.",
 "key_points": [
  "Classical age-replacement assumes known state; reality is partially observable.",
  "The POMDP formulation is correct and computationally brutal.",
  "Threshold-on-sensor policies are mistimed relative to hidden degradation.",
  "Prognostics integration with optimal stopping is theoretically thin.",
 ],
 "requirements": [
  "Explicit belief distributions over equipment health state.",
  "Belief updates from each sensor reading via filtering.",
  "Value-of-information reporting per sensor to guide instrumentation.",
 ],
 "citations": [
  "Wang H (2002) A survey of maintenance policies of deteriorating systems. EJOR 139(3).",
 ],
 "demo": {"coords": [[0,0],[4,2],[7,5],[1,3],[5,1]]},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "or-reliability-allocation",
 "name": "The Reliability Allocation Problem",
 "group": "Optimization",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Given a system of components and a reliability budget, how should redundancy and component reliability be allocated to maximize system reliability per dollar?",
 "background": "Reliability allocation - apportioning system reliability targets to subsystems (AGREE method, 1957) and choosing redundancy levels - is textbook in principle and treacherous in practice. Component reliabilities are uncertain (estimated from limited test data), failures are dependent (common causes), and the cost-reliability curves are guesses. The optimization is nonconvex with integer redundancy choices; heuristics dominate. The deeper problem is epistemic: the allocated reliabilities are only as good as the component estimates, and the propagation of estimation uncertainty through the allocation is rarely quantified - so the system reliability number is a tower built on sand.",
 "why_it_matters": "Aerospace, nuclear, and medical systems live on reliability allocations. Unquantified uncertainty in the allocation is unquantified risk in the system.",
 "sig_lens": "The Signature lens reads reliability as a chain of promises: each component promises uptime, and the protocol must audit the promises, not just sum them.",
 "sig_solution": LABEL + " Assumptions: (1) component reliability estimates carry unquantified uncertainty; (2) common-cause dependence breaks independence math. Reasoning path: propagate the uncertainty honestly - allocate against distributional component reliabilities, not point estimates, and price the epistemic risk. Proposed mechanism: a promise-audit protocol that represents component reliabilities as distributions, optimizes the allocation against a risk-averse system objective, models common-cause coupling explicitly, and reports the system reliability as a distribution with its epistemic spread. Confirm: audited allocations meet field reliability more reliably than point-estimate ones. Kill: the uncertainty distributions are themselves guesses and the audit is theater. Does NOT claim: true system reliability - it reports the promise with its audit trail.",
 "pointer": "The Signature system's proposed approach allocates reliability against distributional estimates with common-cause modeling; the companion Signature Edition record specifies the promise-audit protocol.",
 "key_points": [
  "AGREE allocation apportions targets but assumes known component reliabilities.",
  "Component estimates from limited testing carry large unquantified uncertainty.",
  "Common-cause failures break independence assumptions.",
  "Uncertainty propagation through allocations is rarely quantified.",
 ],
 "requirements": [
  "Distributional (not point) component reliability estimates.",
  "Risk-averse system objectives accounting for epistemic spread.",
  "Explicit common-cause coupling models.",
 ],
 "citations": [
  "AGREE (1957) Reliability of Military Electronic Equipment. US Department of Defense.",
 ],
 "demo": {"coords": [[0,0],[2,5],[5,2],[6,6],[3,4]]},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "or-mechanism-design",
 "name": "The Truthful Mechanism Design Problem",
 "group": "Decision Analysis",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "How can an auction or allocation be designed so that participants do best by telling the truth - and what must be sacrificed when truthfulness conflicts with other goals?",
 "background": "Myerson (1981) characterized optimal auctions: under regularity, the revenue-maximizing truthful auction is known. But the assumptions - independent private values, risk neutrality, single parameter - fail in the wild: values are correlated, bidders are budget-constrained, and multi-item auctions lack clean characterizations. The revelation principle says any implementable outcome has a truthful implementation, but the truthful version may be impractical. Approximate mechanism design trades exact truthfulness for tractability, and the approximation of incentives (how much can bidders gain by lying) is its own open frontier. Real auctions (spectrum, ads) run on theory's edge.",
 "why_it_matters": "Spectrum auctions raise tens of billions; ad auctions run the internet's economy. Mechanisms that can be gamed transfer wealth from the honest to the strategic.",
 "sig_lens": "The Signature lens reads mechanisms as games with rules: the protocol must measure how much lying pays, not just declare that honesty is optimal.",
 "sig_solution": LABEL + " Assumptions: (1) Myerson's characterization needs its assumptions; (2) approximate truthfulness is the practical frontier. Reasoning path: quantify the incentive to lie - compute the maximum gain from misreporting - and design to minimize it subject to the other objectives. Proposed mechanism: a rules-audit protocol that stress-tests mechanisms against strategic bidder models, reports the measured incentive-compatibility gap, and selects among candidate mechanisms by the gap, not just by idealized revenue. Confirm: gap-minimized mechanisms show less strategic manipulation in practice. Kill: bidder models miss real strategic behavior and the audit is blind. Does NOT claim: perfectly truthful practical mechanisms - it minimizes the measured payoff to lying.",
 "pointer": "The Signature system's proposed approach measures the incentive-compatibility gap and designs against it; the companion Signature Edition record specifies the rules-audit protocol.",
 "key_points": [
  "Myerson characterized optimal auctions under restrictive assumptions.",
  "Correlated values, budgets, and multi-item settings lack clean answers.",
  "Approximate mechanism design trades exact truthfulness for tractability.",
  "Real spectrum and ad auctions operate on theory's edge.",
 ],
 "requirements": [
  "Strategic stress-testing of every candidate mechanism.",
  "Measured incentive-compatibility gaps, not assumed truthfulness.",
  "Mechanism selection on the gap alongside revenue and efficiency.",
 ],
 "citations": [
  "Myerson RB (1981) Optimal auction design. Mathematics of Operations Research 6(1).",
 ],
 "demo": {"coords": [[0,0],[6,2],[3,6],[5,3],[1,1]]},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "or-nash-computation",
 "name": "The Nash Equilibrium Computation Problem",
 "group": "Decision Analysis",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Nash equilibria are guaranteed to exist - but can they be computed efficiently, and what does the answer say about game theory's predictive power?",
 "background": "Daskalakis, Goldberg and Papadimitriou (2009) proved computing Nash equilibria is PPAD-complete: as hard as the hardest problems in a class believed to lack polynomial algorithms. The implication is sharp - if equilibria cannot be found efficiently, their predictive power for real strategic behavior is questionable. Approximation helps in special cases (two-player zero-sum is polynomial via linear programming), and learning dynamics (fictitious play, no-regret) converge in some classes but cycle in others. The frontier asks which game classes admit efficient equilibrium computation and whether the right solution concept for applications is Nash at all.",
 "why_it_matters": "Game theory advises on auctions, security, and markets. If its central solution concept is uncomputable, the advice rests on objects nobody can find.",
 "sig_lens": "The Signature lens reads equilibrium as a destination nobody can navigate to: the protocol must ask whether the journey (learning dynamics) reaches somewhere useful instead.",
 "sig_solution": LABEL + " Assumptions: (1) PPAD-completeness is a real barrier, not a technicality; (2) learning dynamics are the practical reality. Reasoning path: shift the solution concept from computed equilibria to the outcomes of plausible learning dynamics - analyze where the dynamics go, not where Nash points sit. Proposed mechanism: a dynamics-first protocol that simulates no-regret learning dynamics on the game at hand, characterizes the attractors empirically, and bases recommendations on dynamic outcomes with convergence diagnostics. Confirm: dynamics-based recommendations predict real strategic outcomes better than Nash computations. Kill: dynamics prove as unpredictable as equilibria are uncomputable. Does NOT claim: a way around PPAD - it changes the question to one with an actionable answer.",
 "pointer": "The Signature system's proposed approach bases game advice on learning-dynamics outcomes rather than Nash points; the companion Signature Edition record specifies the dynamics-first protocol.",
 "key_points": [
  "Computing Nash equilibria is PPAD-complete (Daskalakis et al., 2009).",
  "Uncomputable equilibria cast doubt on predictive power.",
  "Two-player zero-sum is polynomial; general games are not.",
  "Learning dynamics converge in some classes, cycle in others.",
 ],
 "requirements": [
  "Simulation of plausible learning dynamics per game instance.",
  "Empirical attractor characterization with convergence diagnostics.",
  "Recommendations based on dynamic outcomes, not Nash points.",
 ],
 "citations": [
  "Daskalakis C, Goldberg PW, Papadimitriou CH (2009) The complexity of computing a Nash equilibrium. SIAM J. Computing 39(1).",
 ],
 "demo": {"coords": [[0,0],[4,6],[1,2],[6,1],[3,5]]},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "or-simulation-warmup",
 "name": "The Discrete Event Simulation Warmup Problem",
 "group": "Stochastic Models",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "A simulation starts empty but the real system never is - how long must the warmup run before collected statistics can be trusted, and can the answer be automated?",
 "background": "Steady-state simulation faces initialization bias: early statistics reflect the empty start, not the long-run system. Deletion methods (drop the first d observations) need d chosen well - too short and bias remains, too long and data is wasted. Methods abound (Welch's graphical procedure, MSER, Schruben's tests), but automation is fragile: the tests have their own parameters, multiple replications complicate the decision, and terminating simulations have no warmup problem at all (a fact often forgotten, causing needless deletion). The deeper issue is that stationarity itself is assumed, not tested - and nonstationary systems make the whole warmup question ill-posed.",
 "why_it_matters": "Every steady-state simulation study - factories, networks, hospitals - stands on its warmup decision. Wrong warmup means biased results presented with unwarranted confidence.",
 "sig_lens": "The Signature lens reads warmup as clearing the stage: the protocol must verify the actors are in position before the performance is reviewed.",
 "sig_solution": LABEL + " Assumptions: (1) warmup choice trades bias against wasted data; (2) stationarity is assumed, rarely tested. Reasoning path: automate the deletion decision with multiple independent tests and require their agreement, plus an explicit stationarity check. Proposed mechanism: a stage-clearing protocol that runs a battery of warmup detectors (MSER, Schruben variants, batch-means stability), deletes only on majority agreement, and tests stationarity of the retained data - flagging the study if the system is not stationary. Confirm: protocol-chosen warmups reduce bias versus fixed rules on benchmark models. Kill: the detectors disagree chronically and the protocol dithers. Does NOT claim: a universal warmup length - it earns the deletion per study.",
 "pointer": "The Signature system's proposed approach deletes warmup only on detector agreement with stationarity checks; the companion Signature Edition record specifies the stage-clearing protocol.",
 "key_points": [
  "Initialization bias contaminates early simulation statistics.",
  "Deletion length trades bias against wasted data with no universal answer.",
  "Warmup detectors have their own fragile parameters.",
  "Terminating simulations need no warmup - a fact often forgotten.",
 ],
 "requirements": [
  "A battery of independent warmup detectors per study.",
  "Deletion only on detector majority agreement.",
  "Stationarity testing of retained data with nonstationarity flags.",
 ],
 "citations": [
  "Law AM (2014) Simulation Modeling and Analysis, 5th ed. McGraw-Hill.",
 ],
 "demo": {"coords": [[0,0],[5,3],[2,6],[6,4],[4,1]]},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "or-unified-uncertainty",
 "name": "The Unified Optimization Under Uncertainty Problem",
 "group": "Decision Analysis",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Stochastic programming, robust optimization, and online learning each handle uncertainty differently - is there a unified framework, or are the paradigms irreconcilable?",
 "background": "Operations research built three churches for uncertainty: stochastic programming (optimize the expectation over scenarios), robust optimization (optimize the worst case over sets), and online/stochastic approximation (adapt as data arrives). Each has its faithful, its theorems, and its blind spots - and the choice among them is rarely principled. Distributionally robust optimization (Delage and Ye; Esfahani and Kuhn) bridges stochastic and robust by optimizing worst-case over ambiguity sets of distributions, and it is the most promising unification to date. But the bridges are partial: dynamic (multi-stage) unification, computational tractability of the bridges, and guidance on which paradigm fits which problem remain open.",
 "why_it_matters": "Every real decision faces uncertainty, and the paradigm choice shapes the answer more than the data does. An unprincipled choice among churches is faith, not science.",
 "sig_lens": "The Signature lens reads the three churches as dialects of one language: the protocol must translate the decision-maker's actual risk attitude into the right dialect.",
 "sig_solution": LABEL + " Assumptions: (1) no single paradigm dominates; (2) the choice is currently unprincipled. Reasoning path: elicit the decision-maker's risk attitude explicitly (what losses are unacceptable versus merely costly), then route to the paradigm - or blend - that matches it. Proposed mechanism: a translation protocol that profiles risk attitude through structured elicitation, maps the profile to a distributionally robust formulation with calibrated ambiguity size, and reports how the recommendation shifts across paradigms as a sensitivity analysis. Confirm: translated formulations show fewer paradigm-regret surprises. Kill: elicited risk attitudes prove unstable and the translation misleads. Does NOT claim: a mathematical unification of the paradigms - it routes decisions to the right church with the translation made explicit.",
 "pointer": "The Signature system's proposed approach translates risk attitudes into calibrated uncertainty paradigms; the companion Signature Edition record specifies the translation protocol.",
 "key_points": [
  "Stochastic, robust, and online paradigms handle uncertainty incompatibly.",
  "Distributionally robust optimization is the most promising bridge.",
  "Dynamic unification and tractability of bridges remain open.",
  "Paradigm choice is rarely principled in practice.",
 ],
 "requirements": [
  "Structured risk-attitude elicitation per decision.",
  "Calibrated ambiguity sets matched to the elicited attitude.",
  "Cross-paradigm sensitivity analysis on every recommendation.",
 ],
 "citations": [
  "Esfahani PM, Kuhn D (2018) Data-driven distributionally robust optimization. Mathematical Programming 171.",
 ],
 "demo": {"coords": [[0,0],[3,4],[6,1],[1,6],[5,5]]},
},
]
