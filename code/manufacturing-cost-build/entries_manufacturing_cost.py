#!/usr/bin/env python3
"""Entries for the Manufacturing Cost databases (2026-10-17 order #3).

RAW SWEEP over the full manifest (2,390 databases) PLUS every shard index
title in jah-databases-data-1 (795 index files, 1,130,741 index lines):
slugs 'manufacturing-cost' / 'manufacturing-cost-signature' are free; the
nearest neighbors are 'manufacturing-engineers', 'manufacturing-fabrication-
control' (JAH-MFC-), 'manufacturing-robotics-data-types-signature', and
'public-manufacturing-engineers' - all engineering-process archives, none a
cost-to-make vs sell-price costing database. The paste's rule was applied by
name/purpose/record schema/capabilities: cost accounting of manufacture
(BOM costing, labor, overhead, tooling amortization, scale, should-cost,
margin math) is a distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  manufacturing-cost             - The Manufacturing Cost Database
                                   (public-harvest: real, fact-checked cost
                                   accounting - BOM costing, labor costing,
                                   overhead allocation, tooling amortization,
                                   economies of scale, should-cost analysis,
                                   margin math from unit cost through
                                   wholesale to retail, make-vs-buy costing;
                                   standard references Horngren Datar Rajan
                                   Cost Accounting 16th ed 2018; Cooper and
                                   Kaplan Harvard Business Review 1988;
                                   Boothroyd Dewhurst Knight Product Design
                                   for Manufacture and Assembly 3rd ed 2011;
                                   Wright Journal of the Aeronautical Sciences
                                   1936; Juran Quality Handbook 5th ed 1999;
                                   APICS Dictionary 17th ed 2022; BLS Employer
                                   Costs for Employee Compensation; US Census
                                   Annual Survey of Manufactures; and the
                                   other landmarks cited per record)
  manufacturing-cost-signature   - The Manufacturing Cost Signature Database
                                   (his original Signature Cost Method:
                                   every unit cost a sworn accounting, the
                                   BOM a covenant of parts, margin the honor
                                   earned between maker and buyer, scale the
                                   discipline that turns cents into
                                   abundance; src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-MFG- (public) and JAH-MFGS- (signature), verified free in
the manifest id_prefix values and in every shard index (zero hits; the
taken JAH-MFC- belongs to the unrelated manufacturing-fabrication-control
database, so the MFG form was chosen instead).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_manufacturing_cost.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
No military or defense-grade content of any kind.
"""

SIG_TAIL = ("Signature original - his original Signature Cost Method: every "
            "unit cost a sworn accounting, the BOM a covenant of parts, "
            "margin the honor earned between maker and buyer, and scale the "
            "discipline that turns cents into abundance. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_HORNGREN = ("Horngren CT, Datar SM, Rajan MV. Cost Accounting: A "
                "Managerial Emphasis. 16th ed. Pearson; 2018.")
CIT_COOPER = ("Cooper R, Kaplan RS. Measure Costs Right: Make the Right "
              "Decisions. Harvard Business Review; September-October 1988.")
CIT_BOOTHROYD = ("Boothroyd G, Dewhurst P, Knight WA. Product Design for "
                 "Manufacture and Assembly. 3rd ed. CRC Press; 2011.")
CIT_WRIGHT = ("Wright TP. Factors Affecting the Cost of Airplanes. Journal "
              "of the Aeronautical Sciences; 1936;3(4):122-128.")
CIT_JURAN = ("Juran JM, Godfrey AB. Juran's Quality Handbook. 5th ed. "
             "McGraw-Hill; 1999.")
CIT_APICS = ("APICS Dictionary. 17th ed. Association for Supply Chain "
             "Management; 2022.")
CIT_BLS = ("U.S. Bureau of Labor Statistics. Employer Costs for Employee "
           "Compensation; 2024 release.")
CIT_CENSUS = ("U.S. Census Bureau. Annual Survey of Manufactures; 2022.")
CIT_OHNO = ("Ohno T. Toyota Production System: Beyond Large-Scale "
            "Production. Productivity Press; 1988.")
CIT_USITC = ("U.S. International Trade Commission. Harmonized Tariff "
             "Schedule of the United States; 2024.")

SIG_LENS = ("Signature original interpretation: his Signature Cost Method "
            "treats every unit cost as a sworn accounting - the bill of "
            "materials a covenant of parts, labor the honored hours of real "
            "hands, overhead the shared roof honestly divided, tooling the "
            "seed paid once and harvested across volume, margin the honor "
            "earned between maker and buyer, and scale the discipline that "
            "turns cents into abundance. Every number below is reframed "
            "through that lens and clearly labeled Signature-made.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is a Manufacturing Cost",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A manufacturing cost is the full price of bringing one unit into "
            "existence, and it always has exactly three elements: direct "
            "material, direct labor, and manufacturing overhead. Direct "
            "material is everything that becomes part of the product - resin, "
            "steel, wire, screws, packaging that ships with it. Direct labor "
            "is the hands that touch the product: assembly, machining, "
            "welding, test. Manufacturing overhead is everything else the "
            "factory needs to run - rent, supervision, utilities, machine "
            "depreciation, maintenance - shared across every unit made. Add "
            "the three and you get total manufacturing cost, the number from "
            "which every price, margin, and make-or-buy decision flows. A "
            "simple example runs through this whole database: a small device "
            "with $4.20 of material, $2.80 of labor, and $3.50 of overhead "
            "carries a unit manufacturing cost of $10.50. Nothing about "
            "selling, marketing, or profit lives in this number - it is the "
            "cost of making, nothing more, and getting it right is the "
            "foundation of every record that follows."
        ),
        "how_it_works": (
            "Cost accountants build the unit cost the way a mason builds a "
            "wall: layer by layer, each layer measured. First they list "
            "every material in the bill of materials with its quantity and "
            "price and sum them into direct material. Then they measure the "
            "labor time each operation needs, multiply by the burdened labor "
            "rate, and sum into direct labor. Then they take the period's "
            "overhead pool and divide it by an allocation base - labor hours, "
            "machine hours, or material dollars - to get an overhead rate, "
            "and apply that rate to the product. The three layers stack into "
            "prime cost (material plus labor) and conversion cost (labor "
            "plus overhead), and the full stack is the total manufacturing "
            "cost. Standards like Horngren's Cost Accounting define each "
            "layer so two factories mean the same thing when they say "
            "unit cost."
        ),
        "key_points": [
            "The three elements are direct material, direct labor, and manufacturing overhead - every cost lands in exactly one.",
            "Prime cost (material + labor) and conversion cost (labor + overhead) are the two standard sub-totals.",
            "Example stack: $4.20 material + $2.80 labor + $3.50 overhead = $10.50 unit manufacturing cost.",
            "Selling, marketing, administration, and profit are NOT manufacturing cost - they sit above it in the margin stack.",
            "A wrong unit cost corrupts every decision downstream: pricing, quoting, make-vs-buy, and volume planning.",
        ],
        "requirements": [
            "A bill of materials with quantities for the material layer.",
            "Measured labor times and a burdened labor rate for the labor layer.",
            "An overhead pool and an allocation base for the overhead layer.",
            "A consistent definition of one unit of output.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting: A Managerial Emphasis - the three-element cost structure.",
            "APICS Dictionary - standard definitions of direct material, direct labor, and manufacturing overhead.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "bom",
        "name": "The Bill of Materials",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The bill of materials, the BOM, is the recipe of a product: the "
            "complete list of every part, material, and subassembly needed to "
            "build one unit, each line carrying a quantity per unit and a "
            "unit price. Cost the BOM and you cost the material layer of the "
            "product. A five-line BOM for a small device might read: housing "
            "1.10 dollars times one, screws 0.04 dollars times four for "
            "0.16, circuit board 2.30 dollars times one, label 0.05 dollars "
            "times one, and shipping box 0.35 dollars times one - rolling up "
            "to 3.96 dollars of direct material per unit. Real BOMs run to "
            "hundreds or thousands of lines with revision control, because a "
            "changed part is a changed cost. The BOM is also where phantom "
            "costs hide: a line that says quantity one but the process scraps "
            "one in ten, or a fastener pack bought in thousands but costed "
            "per each. Every costing record in this database starts from a "
            "BOM, and every BOM cost is only as honest as its quantities and "
            "its prices."
        ),
        "how_it_works": (
            "A BOM is structured as levels: level zero is the finished "
            "product, level one lists the subassemblies and purchased parts "
            "that go straight into it, level two breaks the subassemblies "
            "into their parts, and so on down to raw stock. To cost it, "
            "multiply each line's quantity-per by its unit price to get "
            "extended cost, then sum the extensions - that sum is the "
            "material roll-up. Engineering owns the structure and the "
            "quantities; purchasing owns the prices; the costing system "
            "multiplies and rolls up. Revisions matter: when a part changes "
            "revision, its price and quantity-per can change too, so BOM "
            "revisions and cost revisions move together. Phantom and bulk "
            "items get their own handling so a box of 1,000 screws is costed "
            "at one-thousandth of its price per screw used."
        ),
        "key_points": [
            "A BOM line = part number + quantity-per-unit + unit price; extended cost = quantity times price.",
            "Example roll-up: 1.10 + 0.16 + 2.30 + 0.05 + 0.35 = 3.96 dollars of material per unit.",
            "Multilevel BOMs nest subassemblies inside the top product; the roll-up explodes every level.",
            "BOM accuracy is cost accuracy: wrong quantities or stale prices corrupt the material layer.",
            "Revision control ties engineering changes to cost changes so the cost always matches the build.",
        ],
        "requirements": [
            "An item master with current unit prices for every purchased part.",
            "Quantity-per-unit values that reflect the real process, including planned scrap.",
            "BOM revision discipline so cost revisions track engineering revisions.",
            "A roll-up routine that explodes all levels to raw cost.",
        ],
        "standards": [
            "APICS Dictionary - bill of materials structures and terminology.",
            "Horngren Datar Rajan Cost Accounting - material cost flow through the BOM.",
        ],
        "citations": [CIT_APICS, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "material_cost",
        "name": "Direct Material Costing",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Direct material costing turns raw stock into a per-unit number, "
            "and the honest version counts three things: what you buy, what "
            "you use, and what you throw away. A sheet-steel bracket shows "
            "the pattern: the blank weighs 0.8 kilograms but the sheet "
            "purchased per blank weighs 1.0 kilogram because the skeleton "
            "around the part is scrap. At 2.50 dollars per kilogram the "
            "purchased steel costs 2.50 dollars, the 0.2 kilograms of scrap "
            "recovers 0.06 dollars at the scrap price of 0.30 dollars per "
            "kilogram, and the net material cost lands at 2.44 dollars per "
            "bracket with 80 percent material utilization. Price times "
            "quantity is only the start; yield, scrap recovery, minimum "
            "order quantities, and price breaks all move the real number. "
            "Commodity materials ride market prices - steel, copper, resin "
            "and plastic pellet prices move monthly - so material costing is "
            "a living number, re-priced on a schedule, never a one-time "
            "fact."
        ),
        "how_it_works": (
            "Start with the gross requirement: the weight, length, area, or "
            "count of raw stock the process consumes per unit, including the "
            "skeleton, offcuts, and sprues the process necessarily wastes. "
            "Multiply by the current purchase price to get gross material "
            "cost. Subtract the scrap credit - scrap weight times the scrap "
            "recovery price - to reach net material cost. Utilization, the "
            "ratio of part weight to purchased weight, is the efficiency "
            "score of the nesting or cutting plan; raising it from 70 to 85 "
            "percent cuts material cost directly. Purchasing keeps price "
            "breaks by volume tier, so the same part costs less per unit at "
            "10,000 than at 1,000, and the costing must state which tier it "
            "assumed."
        ),
        "key_points": [
            "Net material cost = (gross stock times price) minus (scrap weight times scrap price).",
            "Example: 1.0 kg at 2.50/kg minus 0.2 kg scrap at 0.30/kg = 2.44 dollars per bracket at 80 percent utilization.",
            "Utilization is the lever: better nesting and cutting plans buy material cost down with no design change.",
            "Commodity prices move, so material cost carries a price-date and a re-price schedule.",
            "Volume price breaks mean the same BOM costs different amounts at different order sizes.",
        ],
        "requirements": [
            "Gross stock quantities per unit from the process plan.",
            "Current purchase prices with their effective dates.",
            "Scrap weights and realistic scrap recovery prices.",
            "The volume tier the cost assumes.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - direct material cost flow and scrap accounting.",
            "U.S. Census Bureau Annual Survey of Manufactures - material cost benchmarks by industry.",
        ],
        "citations": [CIT_HORNGREN, CIT_CENSUS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "labor_cost",
        "name": "Direct Labor Costing",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Direct labor costing prices the hands that touch the product, "
            "and the honest rate is never just the wage. An operator paid "
            "24.00 dollars per hour actually costs the employer far more: "
            "payroll taxes, health insurance, retirement, paid time off, "
            "and workers compensation stack on top. The U.S. Bureau of Labor "
            "Statistics reports benefits averaging roughly 31 percent of "
            "total compensation, so the burdened rate is 24.00 times 1.31, "
            "or 31.44 dollars per hour. A six-minute assembly cycle is one "
            "tenth of an hour, so the labor cost per unit is 3.14 dollars. "
            "Direct labor is measured in time - minutes per unit, hours per "
            "batch - and priced at the burdened rate, which is why the two "
            "levers are speed (better methods, better tooling) and rate "
            "(the true cost of an hour). Confusing the wage with the cost of "
            "an hour understates labor by nearly a third, and that error "
            "compounds across every unit ever made."
        ),
        "how_it_works": (
            "Industrial engineering measures the work: time studies or "
            "predetermined time systems set the standard minutes per unit "
            "for each operation. Finance builds the burdened rate: base wage "
            "plus the benefit load, payroll taxes, and any shift premiums, "
            "divided by productive hours. Multiply standard time by the "
            "burdened rate for the direct labor cost per unit. Overtime, "
            "training time, and idle time are handled honestly: they raise "
            "the effective rate or sit in overhead, but they never vanish. "
            "Automation changes the mix - the labor minutes fall while the "
            "overhead rate for the machine rises - which is why labor "
            "costing and overhead allocation are two halves of one "
            "decision."
        ),
        "key_points": [
            "The burdened rate, not the wage, is the true price of an hour: 24.00 dollars times 1.31 = 31.44 dollars per hour.",
            "Example: 0.10 hour per unit at 31.44 dollars per hour = 3.14 dollars of direct labor per unit.",
            "BLS data puts benefits near 31 percent of compensation - ignoring the load understates labor by nearly a third.",
            "Labor cost = standard time per unit times burdened rate; the levers are method speed and the true hourly rate.",
            "Overtime, training, and idle time raise the effective rate or move to overhead - they never disappear.",
        ],
        "requirements": [
            "Standard times per operation from time study or engineered standards.",
            "A burdened labor rate built from wage plus benefits, taxes, and premiums.",
            "Productive hours defined honestly, excluding paid non-working time.",
            "A rule for where overtime and idle time land in the cost.",
        ],
        "standards": [
            "U.S. Bureau of Labor Statistics Employer Costs for Employee Compensation - benefit load data.",
            "Horngren Datar Rajan Cost Accounting - direct labor cost flow.",
        ],
        "citations": [CIT_BLS, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "overhead_intro",
        "name": "Manufacturing Overhead: What It Is",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Manufacturing overhead is the cost of the roof over the work: "
            "everything the factory needs that cannot be traced to one unit. "
            "Rent, supervision, utilities, machine depreciation, maintenance, "
            "quality staff, material handling, factory insurance - none of "
            "them become part of the product, but no product exists without "
            "them. Because overhead cannot be traced, it is allocated: the "
            "period's overhead pool is divided by an allocation base to make "
            "a rate, and each product absorbs overhead in proportion to its "
            "use of that base. A plant with 1,200,000 dollars of annual "
            "overhead and 60,000 direct labor hours uses a rate of 20.00 "
            "dollars per labor hour; a job needing 2.5 labor hours absorbs "
            "50.00 dollars of overhead. The choice of base is the whole "
            "game: labor hours favor automated products, machine hours "
            "favor hand-built ones. Overhead is real money - in modern "
            "plants it often exceeds direct labor - and a bad base quietly "
            "over-costs some products and under-costs others."
        ),
        "how_it_works": (
            "Accountants gather indirect costs into one or more overhead "
            "pools for the period, choosing pools that behave alike - "
            "machining overhead separate from assembly overhead, for "
            "example. They pick an allocation base that plausibly drives "
            "each pool: labor hours, machine hours, or material dollars. "
            "The predetermined rate is budgeted pool divided by budgeted "
            "base, set before the period starts so quotes do not wait for "
            "actuals. Each job or unit multiplies its base usage by the rate "
            "to absorb overhead. At period end, applied overhead is compared "
            "to actual overhead; the difference is over- or under-applied "
            "overhead, closed to cost of goods sold or prorated. The rate "
            "is a plan, the variance is the report card."
        ),
        "key_points": [
            "Overhead = indirect factory costs; it is allocated, never traced, via pool divided by base.",
            "Example: 1,200,000 dollars over 60,000 labor hours = 20.00 dollars per hour; 2.5 hours absorbs 50.00 dollars.",
            "The base choice reshapes product costs: labor-hour bases punish hand work, machine-hour bases punish automation.",
            "Predetermined rates are set from budgets before the period; variances report how reality differed.",
            "Modern plants often carry overhead larger than direct labor, so the allocation base deserves real thought.",
        ],
        "requirements": [
            "A defined overhead pool with indirect costs gathered consistently.",
            "An allocation base that plausibly drives the pool.",
            "Budgeted pool and base figures set before the period.",
            "A variance treatment for over- or under-applied overhead.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - overhead allocation and predetermined rates.",
            "APICS Dictionary - overhead, allocation base, and applied overhead definitions.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "cost_stack",
        "name": "The Standard Cost Stack",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The standard cost stack is the full ladder from raw elements to "
            "cost of goods sold, and every rung has a name. Direct material "
            "4.20 plus direct labor 2.80 is prime cost: 7.00 dollars. Direct "
            "labor 2.80 plus manufacturing overhead 3.50 is conversion cost: "
            "6.30 dollars. All three elements together are total "
            "manufacturing cost: 10.50 dollars per unit. Then inventory does "
            "its work: add beginning work-in-process of 1.00 dollar per "
            "equivalent unit and subtract ending work-in-process of 0.50 to "
            "get cost of goods manufactured: 11.00 dollars. Add beginning "
            "finished goods of 2.00 and subtract ending finished goods of "
            "1.50 to reach cost of goods sold: 11.50 dollars per unit sold. "
            "Each rung answers a different question - what did materials "
            "cost, what did the factory add, what did we finish, what did we "
            "sell - and skipping a rung is how costs quietly double-count or "
            "vanish."
        ),
        "how_it_works": (
            "Costs flow like water through the factory accounts. Material, "
            "labor, and overhead enter work-in-process as production runs. "
            "When units finish, their cost transfers to finished goods at "
            "the unit manufacturing cost. When units sell, finished goods "
            "releases cost of goods sold. The stack reconciles the period: "
            "total manufacturing cost plus beginning WIP minus ending WIP "
            "equals cost of goods manufactured; cost of goods manufactured "
            "plus beginning finished goods minus ending finished goods "
            "equals cost of goods sold. Standard costing fixes each rung at "
            "a budgeted standard so variances - price, efficiency, spending "
            "- pop out by rung instead of hiding in one total."
        ),
        "key_points": [
            "Prime cost = material + labor (7.00); conversion cost = labor + overhead (6.30); total manufacturing cost = 10.50.",
            "Inventory rungs: COGM = 10.50 + 1.00 - 0.50 = 11.00; COGS = 11.00 + 2.00 - 1.50 = 11.50.",
            "Each rung answers one question: elements, factory-added cost, finished cost, sold cost.",
            "Standard costing freezes the rungs at budget so variances surface by layer.",
            "Skipping rungs is how costs double-count or vanish between periods.",
        ],
        "requirements": [
            "Standard costs for material, labor, and overhead per unit.",
            "Beginning and ending inventory valuations for WIP and finished goods.",
            "A cost flow that moves costs only when units move.",
            "Variance accounts that catch price, efficiency, and spending differences.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - cost of goods manufactured and sold schedules.",
            "APICS Dictionary - prime cost, conversion cost, and standard cost definitions.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "cogs_unit",
        "name": "Cost of Goods Sold vs Unit Cost",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Unit cost and cost of goods sold are siblings, not twins. Unit "
            "cost is what one unit took to make; cost of goods sold is what "
            "the units you actually sold took to make. A run of 10,000 units "
            "at a total manufacturing cost of 105,000 dollars carries a unit "
            "cost of 10.50 dollars. Sell 9,000 of them and cost of goods "
            "sold is 94,500 dollars, while 10,500 dollars of finished goods "
            "inventory waits on the shelf. Confuse the two and the errors "
            "are classic: dividing the period's total cost by units sold "
            "instead of units made, or treating unsold inventory as an "
            "expense. The difference also drives the inventory question that "
            "follows every production plan - each unsold unit parks 10.50 "
            "dollars of cash on a shelf, which is why overproduction is a "
            "cost even when the factory looks efficient."
        ),
        "how_it_works": (
            "Unit cost comes from the production run: total manufacturing "
            "cost for the period divided by equivalent units produced, "
            "counting partially complete units at their stage of "
            "completion. Cost of goods sold comes from the sales ledger: "
            "units sold times their unit cost, pulled from finished goods "
            "inventory under FIFO, average, or standard cost flow. The "
            "reconciliation is a balance check: beginning finished goods "
            "plus cost of goods manufactured minus ending finished goods "
            "must equal cost of goods sold, and the ending inventory must "
            "be countable on the shelf. Auditors live on this "
            "reconciliation because it is where phantom profit and hidden "
            "loss both leave footprints."
        ),
        "key_points": [
            "Unit cost = period manufacturing cost divided by units produced; COGS = units sold times unit cost.",
            "Example: 105,000 dollars over 10,000 units = 10.50 per unit; 9,000 sold = 94,500 COGS; 10,500 stays in inventory.",
            "Dividing total cost by units sold instead of units made is the classic error - it inflates the unit cost.",
            "Unsold units park cash: 1,000 unsold units at 10.50 = 10,500 dollars sitting on the shelf.",
            "The finished-goods reconciliation (beginning + made - ending = sold) is the audit checkpoint.",
        ],
        "requirements": [
            "Equivalent-unit counts that handle partially finished work honestly.",
            "A stated inventory cost flow: FIFO, average, or standard.",
            "Physical inventory counts that tie to the book balance.",
            "Separation of production volume from sales volume in every report.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - equivalent units and inventory cost flows.",
            "U.S. Census Bureau Annual Survey of Manufactures - inventory and cost benchmarks.",
        ],
        "citations": [CIT_HORNGREN, CIT_CENSUS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "landed_cost",
        "name": "Landed Cost: Freight, Duty, and Currency",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The price on the supplier's quote is not the price you pay. "
            "Landed cost is the true per-unit cost with everything it took "
            "to get the goods to your dock: the FOB price, ocean or air "
            "freight, insurance, import duty, brokerage fees, and currency "
            "movement between quote and payment. A shipment quoted at 10,000 "
            "dollars FOB for 5,000 units looks like 2.00 dollars per unit - "
            "until 1,800 dollars of freight, 150 dollars of insurance, and "
            "1,200 dollars of duty at a 12 percent tariff rate land on top, "
            "bringing the total to 13,150 dollars, or 2.63 dollars per unit. "
            "That is 31.5 percent more than the quote suggested. Duty rates "
            "come from the Harmonized Tariff Schedule published by the U.S. "
            "International Trade Commission and vary wildly by product "
            "class. Smart costing never compares a domestic quote to a "
            "foreign FOB price; it compares domestic price to foreign landed "
            "cost, or it is comparing a photograph to the real thing."
        ),
        "how_it_works": (
            "Build the landed stack line by line. Start with the FOB or "
            "ex-works price in the quoted currency, converted at a stated "
            "exchange rate with a stated date. Add international freight - "
            "per container, per kilogram, or per cubic meter - plus cargo "
            "insurance. Apply the duty rate from the correct tariff "
            "classification to the dutiable value, which is usually the "
            "transaction value. Add customs brokerage, harbor fees, and "
            "inland freight to the plant. Divide the grand total by the "
            "units in the shipment for the landed unit cost. Because "
            "freight is mostly fixed per shipment, landed cost per unit "
            "falls as shipment size rises - the quiet economy of the full "
            "container."
        ),
        "key_points": [
            "Landed cost = FOB + freight + insurance + duty + brokerage + inland freight, divided by units.",
            "Example: 10,000 + 1,800 + 150 + 1,200 = 13,150 dollars; 5,000 units = 2.63 per unit vs 2.00 FOB.",
            "The quote understated reality by 31.5 percent - the classic offshore comparison trap.",
            "Duty rates come from the Harmonized Tariff Schedule and depend on correct product classification.",
            "Freight is largely fixed per shipment, so landed unit cost falls with larger shipments.",
        ],
        "requirements": [
            "The FOB price with currency and exchange-rate date stated.",
            "Freight and insurance quotes for the actual shipment size.",
            "The correct tariff classification and duty rate.",
            "Brokerage, harbor, and inland freight estimates.",
        ],
        "standards": [
            "U.S. International Trade Commission Harmonized Tariff Schedule - duty classification and rates.",
            "APICS Dictionary - landed cost definition.",
        ],
        "citations": [CIT_USITC, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "quotation",
        "name": "Reading a Supplier Quotation",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A supplier quotation is a small contract wearing a price tag, "
            "and the unit price is only one of its terms. The full anatomy "
            "reads: unit price, tooling and NRE charges, minimum order "
            "quantity, lead time, price validity period, payment terms, and "
            "what is included or excluded - packaging, freight, testing, "
            "certificates. Consider a quote at 2.40 dollars per unit with "
            "6,000 dollars of tooling, a 2,000-unit minimum, six-week lead "
            "time, and thirty-day validity. At the minimum quantity the "
            "effective unit cost is 2.40 plus 3.00 dollars of amortized "
            "tooling: 5.40 dollars. At 10,000 units the tooling spreads to "
            "0.60 and the effective cost is 3.00 dollars. Same quote, two "
            "different costs - the quantity you actually buy decides which "
            "one is real. Reading quotes means converting every term into "
            "its effect on your unit cost at your volume, then comparing "
            "suppliers on that basis, never on the headline price alone."
        ),
        "how_it_works": (
            "Normalize each quote to an effective unit cost at your planned "
            "volume. Add amortized tooling and NRE: the one-time charge "
            "divided by the units you will actually buy. Add the freight "
            "and packaging terms, or confirm they are included. Adjust for "
            "payment terms - 2 percent 10 net 30 is a real discount if you "
            "can take it. Note the validity window, because a thirty-day "
            "quote re-priced at ninety days is a different quote. Then "
            "score the non-price terms: lead time reliability, quality "
            "history, and capacity risk. The cheapest headline price with "
            "the worst delivery record is usually the most expensive "
            "supplier you will ever hire."
        ),
        "key_points": [
            "A quote's terms - tooling, MOQ, lead time, validity, inclusions - move the real cost as much as the price.",
            "Example: 2.40 + 6,000/2,000 = 5.40 effective at MOQ; 2.40 + 6,000/10,000 = 3.00 at volume.",
            "Always normalize to effective unit cost at YOUR planned volume before comparing suppliers.",
            "Payment terms, freight inclusion, and validity windows are cost terms in disguise.",
            "Non-price terms - delivery reliability, quality history - are the tiebreakers that prevent expensive mistakes.",
        ],
        "requirements": [
            "The full written quote with all terms, not just the unit price.",
            "Your planned purchase volume for the amortization math.",
            "Freight, packaging, and payment-term adjustments.",
            "A supplier scorecard for the non-price terms.",
        ],
        "standards": [
            "APICS Dictionary - quotation and sourcing terminology.",
            "Horngren Datar Rajan Cost Accounting - relevant cost in sourcing decisions.",
        ],
        "citations": [CIT_APICS, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "make_buy_intro",
        "name": "Make vs Buy: The First Question",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Make vs buy is the oldest question in manufacturing - build the "
            "part in-house or purchase it - and the first version of the "
            "answer is about avoidable cost. Only costs that disappear if "
            "you stop making the part count. Consider a bracket: making it "
            "costs 3.00 dollars of material, 1.50 of labor, and 0.75 of "
            "variable overhead that truly goes away - 5.25 dollars of "
            "avoidable cost. A supplier offers it at 5.80 dollars. Making "
            "saves 0.55 dollars per unit. The 40,000 dollars of fixed "
            "factory overhead allocated to the bracket stays whether you "
            "make or buy, so it is irrelevant to the decision - counting it "
            "would punish the make option for costs that never leave. This "
            "first-pass answer ignores quality, capacity, lead time, and "
            "strategy; those join in the advanced record. But the discipline "
            "starts here: compare the buy price only to the costs that "
            "actually vanish."
        ),
        "how_it_works": (
            "List every cost element of making the part and mark each as "
            "avoidable or unavoidable. Direct material, direct labor, and "
            "variable overhead tied to the part are usually avoidable. "
            "Allocated fixed overhead, depreciation on equipment with no "
            "alternative use, and sunk tooling are usually unavoidable - "
            "they stay either way. Sum the avoidable costs into the "
            "relevant make cost and compare it to the supplier's price plus "
            "any buy-side costs like incoming inspection or freight. If the "
            "buy price beats the avoidable make cost, buying wins on cost; "
            "if not, making wins. Document which costs you called "
            "unavoidable, because that judgment is where the analysis is "
            "won or lost."
        ),
        "key_points": [
            "Only avoidable costs count: compare the buy price to costs that truly disappear if you stop making.",
            "Example: avoidable make cost 5.25 vs buy price 5.80 - making saves 0.55 per unit.",
            "Allocated fixed overhead is irrelevant - it stays whether you make or buy.",
            "Sunk tooling and idle equipment with no alternative use do not enter the decision.",
            "This is the cost-only first pass; quality, capacity, and strategy join in the advanced analysis.",
        ],
        "requirements": [
            "A cost element list for the part, marked avoidable or unavoidable.",
            "A firm supplier price at your volume with buy-side costs added.",
            "Honest treatment of fixed overhead and sunk costs.",
            "Documentation of the avoidability judgments.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - relevant cost and the make-or-buy decision.",
            "APICS Dictionary - make-or-buy decision definitions.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
]

ENTRIES.extend([
    {
        "key": "bom_rollup",
        "name": "Multilevel BOM Rollups",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Real products are not flat lists - they are trees. A multilevel "
            "BOM nests subassemblies inside the finished product, and the "
            "cost roll-up explodes every level down to raw cost. Take a "
            "device: its sensor subassembly holds two 1.10-dollar parts and "
            "four 0.04-dollar screws, 2.36 dollars of material, plus 0.40 "
            "dollars of subassembly labor for a subassembly cost of 2.76 "
            "dollars. The top level adds that subassembly to a 2.30-dollar "
            "circuit board, a 0.35-dollar box, and a 0.05-dollar label for "
            "5.46 dollars of material at the top. The roll-up must handle "
            "shared subassemblies used in many products, phantom assemblies "
            "that exist for engineering logic but never get stocked, and "
            "scrap factors at each level - a 2 percent scrap rate at three "
            "levels compounds to more than 6 percent. Where-used analysis "
            "runs the tree in reverse: one part change ripples to every "
            "product that contains it, which is how a single resin price "
            "increase reprices half the catalog overnight."
        ),
        "how_it_works": (
            "The roll-up walks the tree bottom-up. Each purchased part "
            "contributes its price times quantity-per. Each manufactured "
            "subassembly contributes its own rolled material cost plus its "
            "labor and overhead at that level. Scrap and yield factors "
            "inflate quantities at each level: a level needing 100 good "
            "units with 98 percent yield must start 102.04 units. Phantom "
            "assemblies pass their children straight through without adding "
            "a stocking level. The system explodes the full tree, multiplies "
            "quantities down every branch, and sums to the top-level "
            "material cost - then labor and overhead layers are applied at "
            "the levels where the work actually happens."
        ),
        "key_points": [
            "Multilevel BOMs nest subassemblies; the roll-up explodes every level to raw cost bottom-up.",
            "Example: subassembly 2.76 + board 2.30 + box 0.35 + label 0.05 = 5.46 dollars top-level material.",
            "Scrap compounds across levels: 2 percent loss at three levels exceeds 6 percent total.",
            "Phantom assemblies pass children through without a stocking level; shared subassemblies roll once, cost many.",
            "Where-used analysis runs the tree in reverse so one part change reprices every affected product.",
        ],
        "requirements": [
            "A multilevel BOM with correct parent-child links and quantities-per.",
            "Scrap and yield factors stated at each manufacturing level.",
            "Phantom and shared-subassembly flags handled by the roll-up logic.",
            "Current prices at every purchased leaf of the tree.",
        ],
        "standards": [
            "APICS Dictionary - multilevel bill of materials, roll-up, and where-used.",
            "Horngren Datar Rajan Cost Accounting - cost accumulation through production stages.",
        ],
        "citations": [CIT_APICS, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "labor_standards",
        "name": "Labor Standards and Time Studies",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A labor standard is the engineered answer to how long a job "
            "should take, and everything in labor costing hangs on it. "
            "Time studies, predetermined time systems, and work sampling "
            "measure the work; allowances for fatigue, personal needs, and "
            "unavoidable delays turn observed time into standard time. A "
            "line with a standard of 0.10 hour per unit that produces 480 "
            "units earns 48.0 standard hours; if the crew actually worked "
            "52.0 hours, efficiency is 92.3 percent and the 3.7-hour gap is "
            "the efficiency variance in plain sight. Standards do three "
            "jobs at once: they price the labor in every quote, they set "
            "the pace the floor is measured against, and they expose method "
            "problems as variances instead of mysteries. A standard built "
            "on wishful thinking corrupts all three - quotes go out too "
            "cheap, the floor can never win, and the variance report cries "
            "wolf until nobody reads it."
        ),
        "how_it_works": (
            "Analysts break the job into elements, time each element across "
            "enough cycles to be statistically sound, and rate the "
            "operator's pace against a normal 100 percent. Observed time "
            "times the rating factor gives normal time; adding the allowance "
            "percentage gives standard time per unit. Earned hours - units "
            "produced times standard time - measure what the crew should "
            "have needed; comparing earned to actual hours yields "
            "efficiency. Labor efficiency variance is the hour gap valued "
            "at the standard rate, and labor rate variance is the pay gap "
            "at actual hours. Standards get re-studied when methods, "
            "tooling, or designs change - a standard that outlives its "
            "method is a fiction with a variance report."
        ),
        "key_points": [
            "Standard time = observed time times rating factor, plus allowances for fatigue and delays.",
            "Example: 480 units at 0.10 hour standard = 48.0 earned hours; 52.0 actual = 92.3 percent efficiency.",
            "Standards serve quoting, floor measurement, and variance analysis - one number, three jobs.",
            "Efficiency variance = (earned hours - actual hours) times standard rate; rate variance prices pay differences.",
            "Restudy standards when methods change; a stale standard corrupts quotes and demoralizes the floor.",
        ],
        "requirements": [
            "Time-study data with rated pace and stated allowances.",
            "Enough cycles observed for statistical confidence.",
            "A restudy trigger tied to method, tooling, or design changes.",
            "Variance reporting that separates efficiency from rate effects.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - direct labor efficiency and rate variances.",
            "APICS Dictionary - standard time and engineered labor standards.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "machine_hour_rate",
        "name": "Machine-Hour Overhead Rates",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Where machines do the work, overhead should follow machine "
            "hours, not labor hours - that is the whole argument for "
            "machine-hour rates. A machining center's annual cost stacks up "
            "honestly: 120,000 dollars of depreciation, 45,000 of "
            "maintenance, 30,000 of power, 95,000 of operator cost, 60,000 "
            "of floor space, and 130,000 of tooling and consumables - "
            "480,000 dollars a year. Over 2,000 productive hours that is "
            "240.00 dollars per machine hour, so a job running 0.25 hour "
            "absorbs 60.00 dollars of machine cost. Costing that job on "
            "labor hours instead would charge it a fraction of its true "
            "hunger for capital. The rate's honesty depends on productive "
            "hours - scheduled hours minus setup, maintenance, and idle "
            "time - because a 240-dollar rate computed on fantasy hours is "
            "a subsidy for somebody else's product. Machine-hour rates are "
            "how automated factories tell the truth about what their "
            "equipment really costs per minute."
        ),
        "how_it_works": (
            "Build a cost pool per machine or machine group: depreciation "
            "or lease cost, maintenance contracts and parts, power at "
            "measured draw, tooling and consumables, the operator's burdened "
            "cost if dedicated, and the floor space at the plant rate. "
            "Estimate realistic productive hours - two shifts at 85 percent "
            "utilization is a plan, three shifts at 100 percent is a dream. "
            "Divide pool by hours for the rate. Each job's routing carries "
            "its machine minutes; multiply by the rate to absorb cost. "
            "Track utilization variance: idle machine time is the "
            "under-applied overhead of automation, and it belongs in "
            "management's inbox, not hidden in product costs."
        ),
        "key_points": [
            "Machine-hour rate = annual machine cost pool divided by realistic productive hours.",
            "Example: 480,000 dollars over 2,000 hours = 240.00 per hour; a 0.25-hour job absorbs 60.00 dollars.",
            "The pool must include depreciation, maintenance, power, tooling, operator, and floor space.",
            "Productive hours must be honest - fantasy hours create fantasy rates that subsidize someone.",
            "Idle machine time surfaces as under-applied overhead: the utilization report card of automation.",
        ],
        "requirements": [
            "A complete annual cost pool per machine or machine group.",
            "Realistic productive hours net of setup, maintenance, and idle time.",
            "Routings with machine minutes per operation.",
            "Utilization tracking that exposes idle capacity.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - departmental and machine-hour overhead rates.",
            "APICS Dictionary - machine-hour rate and productive capacity.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "tooling_nre",
        "name": "Tooling and NRE Amortization",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Tooling and non-recurring engineering - molds, dies, fixtures, "
            "test jigs, first-article engineering - are paid once and "
            "harvested across every unit the tool ever makes. Amortization "
            "is the arithmetic of that harvest: divide the one-time cost by "
            "the units it will serve. An 80,000-dollar injection mold "
            "spread over 200,000 parts adds 0.40 dollars per part; the same "
            "mold over only 50,000 parts adds 1.60 dollars per part. The "
            "denominator is a forecast, and forecasts are where tooling "
            "math gets dangerous: amortize over fantasy volume and the unit "
            "cost looks cheap until the orders stop. Honest practice "
            "amortizes over committed or conservatively forecasted volume, "
            "revisits the rate when forecasts change, and treats tooling "
            "life limits - a mold rated for 500,000 shots - as a hard "
            "ceiling. Tooling is the reason low-volume products carry "
            "shocking unit costs and the reason volume is the cheapest "
            "cost-reduction program ever invented."
        ),
        "how_it_works": (
            "Capitalize the tooling and NRE spend - design hours, tool "
            "build, tryout, and qualification - into a tool asset. Choose "
            "the amortization base: units expected over the tool's life or "
            "the contract quantity, whichever is smaller and more certain. "
            "Divide to get the per-unit tooling adder and apply it to every "
            "unit the tool produces. If volume falls short, the unamortized "
            "balance is a period loss, not a product cost - writing it into "
            "remaining units would price them out of the market. Multi-"
            "cavity and family tools split their cost across the parts they "
            "produce together, and replacement tooling starts a fresh "
            "amortization clock."
        ),
        "key_points": [
            "Tooling amortization = one-time tool cost divided by the units the tool will actually serve.",
            "Example: 80,000 dollars over 200,000 parts = 0.40 per part; over 50,000 = 1.60 per part.",
            "The denominator is a forecast - amortizing over fantasy volume manufactures fake cheapness.",
            "Tool life ratings are hard ceilings; unamortized balances on dead volume are period losses.",
            "Low volume is why unit costs shock: the same tool at a tenth the volume costs ten times per unit.",
        ],
        "requirements": [
            "The full capitalized tooling and NRE spend, including tryout and qualification.",
            "A conservative volume forecast or contract quantity for the denominator.",
            "Tool life limits from the toolmaker.",
            "A policy for unamortized balances when volume falls short.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - amortization of non-recurring costs.",
            "APICS Dictionary - non-recurring engineering and tooling definitions.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "injection_molding",
        "name": "Injection Molding Cost Anatomy",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "An injection-molded part's cost has four chambers: machine "
            "time, resin, tooling amortization, and secondary work. Machine "
            "time is rate times cycle: a 45-dollar-per-hour press running a "
            "24-second cycle with 2 cavities makes 300 parts per hour, so "
            "machine cost is 0.15 dollars per part. Resin is weight times "
            "price: 0.04 kilograms at 3.20 dollars per kilogram is 0.128 "
            "dollars, plus the runner and sprue the process wastes. Tooling "
            "amortization adds the mold's per-part share, and secondary "
            "operations - degating, pad printing, assembly - add their own "
            "labor and machine slices. The levers are visible in the "
            "anatomy: cut cycle time and machine cost per part falls; add "
            "cavities and it falls again; lighten the part and resin cost "
            "falls; raise volume and tooling per part falls. A part that "
            "costs 0.43 dollars at 10,000 units can cost 0.28 at 200,000 - "
            "same part, same mold, different arithmetic."
        ),
        "how_it_works": (
            "Start with the press rate for the tonnage class, including "
            "operator, overhead, and profit if quoted. Compute parts per "
            "hour as cavities times 3,600 divided by cycle seconds, then "
            "machine cost per part as rate divided by parts per hour. Weigh "
            "the part plus runner, multiply by resin price per kilogram, "
            "and add regrind credit if runners are reground. Add the "
            "tooling amortization per part from the mold cost over "
            "forecasted volume. Add secondary operations at their own "
            "rates. Validate against the shot: clamp tonnage must suit the "
            "projected area, and the cycle must include realistic cooling "
            "time - a quote with a 12-second cycle on a thick-walled part "
            "is selling warp and sink along with the parts."
        ),
        "key_points": [
            "Four chambers: machine time, resin, tooling amortization, and secondary operations.",
            "Example: 45/hr press, 24 s cycle, 2 cavities = 300 parts/hr = 0.15 machine cost; 0.04 kg at 3.20/kg = 0.128 resin.",
            "Levers: shorter cycles, more cavities, lighter parts, higher volume - each attacks one chamber.",
            "Runner and sprue waste count in resin cost; regrind credit only if runners are actually reground.",
            "Sanity-check the cycle: thick walls need cooling time, and impossible cycles signal impossible quotes.",
        ],
        "requirements": [
            "Press rate for the tonnage class with operator and overhead included.",
            "Realistic cycle time with cooling, and the cavity count.",
            "Part plus runner weight and current resin price.",
            "Mold cost and forecasted volume for the tooling adder.",
        ],
        "standards": [
            "Boothroyd Dewhurst Knight Product Design for Manufacture and Assembly - molding cost drivers.",
            "APICS Dictionary - injection molding and cycle time terminology.",
        ],
        "citations": [CIT_BOOTHROYD, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "machining",
        "name": "Machining Cost Anatomy",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A machined part's cost is setup spread over the batch plus "
            "cycle time at the machine rate, with tool wear riding along. "
            "The anatomy is unforgiving at low volume: 45 minutes of setup "
            "at 85 dollars per hour is 63.75 dollars before the first chip "
            "falls. A batch of 200 parts with a 3.2-minute cycle runs 640 "
            "minutes - 10.67 hours - at 85 dollars per hour for 906.67 "
            "dollars of run cost. Total 970.42 dollars over 200 parts is "
            "4.85 dollars per part, and more than 6 percent of that is setup "
            "alone. The levers: bigger batches dilute setup, faster cycles "
            "cut run cost, simpler geometry cuts both, and near-net-shape "
            "stock - castings, extrusions, or plate instead of billet - "
            "removes cycle time that never needed to exist. Quoting machined "
            "parts without stating the batch size is quoting a number "
            "without its denominator."
        ),
        "how_it_works": (
            "Estimate setup time - fixturing, tool loading, first-article "
            "proving - and multiply by the machine-hour rate for setup "
            "cost. Estimate cycle time per part from the operations: facing, "
            "turning, milling, drilling, finishing passes, and handling. "
            "Multiply cycle by the rate for run cost per part. Add tooling "
            "consumption: inserts and end mills have a cost per edge and a "
            "parts-per-edge life. Sum setup plus run plus tooling for batch "
            "cost and divide by batch quantity. Then interrogate the "
            "geometry: every tolerance tighter than the function needs, "
            "every undercut, every deep pocket is cycle time priced into "
            "the part forever."
        ),
        "key_points": [
            "Machined cost = (setup cost + run cost + tooling) divided by batch quantity.",
            "Example: 63.75 setup + 906.67 run = 970.42 over 200 parts = 4.85 dollars per part.",
            "Setup dominates small batches: batch size is the denominator that decides everything.",
            "Tool wear is a real per-part cost: inserts have a price per edge and a parts-per-edge life.",
            "Design levers: looser tolerances where function allows, simpler geometry, near-net-shape stock.",
        ],
        "requirements": [
            "Setup time estimate with first-article proving included.",
            "Cycle time per part from the operation sequence.",
            "The machine-hour rate with tooling and overhead.",
            "The batch quantity the quote assumes - stated, never implied.",
        ],
        "standards": [
            "Boothroyd Dewhurst Knight Product Design for Manufacture and Assembly - machining cost drivers.",
            "Horngren Datar Rajan Cost Accounting - batch-level cost treatment.",
        ],
        "citations": [CIT_BOOTHROYD, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "electronics_assembly",
        "name": "Electronics Assembly Costing",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A printed circuit board assembly's cost stacks five layers: the "
            "bare board, the components, placement, through-hole and hand "
            "work, and test. The anatomy of one board: bare PCB fabrication "
            "1.80 dollars, 42 surface-mount placements at 0.012 dollars "
            "each for 0.504 dollars, 6 plated through-hole joints at 0.08 "
            "dollars each for 0.48 dollars, and functional test at 0.35 "
            "dollars - 3.13 dollars before a single component is purchased. "
            "Components themselves are a separate BOM roll-up, and they "
            "dominate: one expensive microcontroller can outweigh the entire "
            "assembly stack. The levers are count-driven: fewer unique part "
            "numbers cut setup and feeder time, single-sided SMT avoids the "
            "second reflow pass, and designing out through-hole parts "
            "removes the wave-solder island entirely. Test is the layer "
            "buyers try to delete and factories beg to keep - an untested "
            "board ships its defects to the customer at full retail price."
        ),
        "how_it_works": (
            "Cost the bare board from layer count, size, finish, and volume "
            "- each added layer and each exotic finish has a price. Roll up "
            "the component BOM with placement quantities. Apply the SMT "
            "rate per placement, often tiered by package size: fine-pitch "
            "and 0201 parts cost more per placement than commodity chips. "
            "Add through-hole at per-joint rates for wave or selective "
            "solder, plus hand-solder minutes for the odd parts. Add test: "
            "flying probe, in-circuit, or functional, each with a per-board "
            "time at the test rate. Yield matters twice: board fabrication "
            "yield and assembly first-pass yield both inflate the effective "
            "cost per good board."
        ),
        "key_points": [
            "Five layers: bare board, components, SMT placement, through-hole/hand work, and test.",
            "Example stack: 1.80 board + 0.504 SMT + 0.48 PTH + 0.35 test = 3.13 dollars before components.",
            "Component cost usually dominates - one costly IC can exceed the whole assembly stack.",
            "Design levers: fewer unique parts, single-sided SMT, eliminate through-hole where possible.",
            "Test is not optional cost - untested boards export defects to customers at full price.",
        ],
        "requirements": [
            "Bare-board specs: layers, size, finish, and volume tier.",
            "Component BOM with package sizes for tiered placement rates.",
            "Through-hole joint counts and hand-solder minutes.",
            "Test method and per-board test time; fabrication and assembly yields.",
        ],
        "standards": [
            "APICS Dictionary - printed circuit board assembly terminology.",
            "Horngren Datar Rajan Cost Accounting - multi-stage cost accumulation.",
        ],
        "citations": [CIT_APICS, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "yield_scrap",
        "name": "Yield, Scrap, and Rework Costing",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Yield is the tax the process levies on every good unit, and it "
            "must be priced in. A line with 96 percent first-pass yield, 3 "
            "percent reworkable at 1.50 dollars each, and 1 percent true "
            "scrap turns 10.00 dollars of input cost into an effective cost "
            "of 10.46 dollars per good unit: the 10.00 dollars plus 0.045 "
            "dollars of rework, divided by 0.96 good units. The formula is "
            "honest about where the money goes - rework labor and the dead "
            "scrap both ride on the survivors. Three disciplines control "
            "it: prevention that stops defects, detection that catches them "
            "before value is added, and disposition that decides rework vs "
            "scrap without sentiment. The most expensive defect is the one "
            "found late: scrap after final assembly throws away every "
            "operation's cost, while scrap at incoming inspection throws "
            "away only material. Yield costing is why quality is not a "
            "department - it is a line item."
        ),
        "how_it_works": (
            "Measure first-pass yield at each operation: good units out "
            "divided by units in. Track the rework stream separately - its "
            "rate and its cost per unit reworked. Track true scrap: units "
            "with no recovery value. Effective unit cost equals input cost "
            "plus rework cost, divided by first-pass yield, with scrap "
            "credit subtracted if scrap has recovery value. Roll the "
            "effective cost forward as the input cost of the next "
            "operation, because downstream operations inherit upstream "
            "yield losses. Report yield cost as its own line - dollars per "
            "period lost to scrap and rework - so improvement programs can "
            "see the prize they are chasing."
        ),
        "key_points": [
            "Effective cost = (input cost + rework cost) divided by first-pass yield, minus scrap credit.",
            "Example: (10.00 + 0.045) / 0.96 = 10.46 dollars per good unit from 10.00 of input.",
            "Late defects cost the most: scrap after final assembly wastes every operation's cost.",
            "Prevention, detection, and disposition are the three disciplines that move the number.",
            "Yield cost deserves its own report line so improvement programs can see the prize.",
        ],
        "requirements": [
            "First-pass yield measured at each operation.",
            "Rework rate and true cost per reworked unit.",
            "Scrap quantities with recovery values where they exist.",
            "Cost roll-forward so downstream stages inherit upstream yield loss.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - spoilage, rework, and scrap accounting.",
            "Juran JM Godfrey AB Juran's Quality Handbook - cost of poor quality framework.",
        ],
        "citations": [CIT_HORNGREN, CIT_JURAN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "scale",
        "name": "Economies of Scale",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Making more of the same thing costs less per unit, and the "
            "reasons compound: fixed costs spread thinner, learning makes "
            "labor faster, purchasing earns volume breaks, and processes "
            "built for volume waste less. The learning curve gives the "
            "phenomenon a number. T. P. Wright's 1936 study of airplane "
            "production found that each doubling of cumulative output cut "
            "labor hours per unit by a constant percentage - the famous 80 "
            "percent curve means the second unit takes 80 percent of the "
            "first unit's time, the fourth takes 80 percent of the "
            "second's. A 10.0-hour first unit becomes 8.0 hours at unit two "
            "and 6.4 hours at unit four. The curve is steepest early, which "
            "is why prototypes are brutally expensive and mature products "
            "are cheap. Scale also has a dark side: the volume that buys "
            "the low cost demands the forecast accuracy to sell it, and "
            "inventory built for scale that never sells is just expensive "
            "storage."
        ),
        "how_it_works": (
            "Fit the learning curve from early production data: plot unit "
            "labor hours against cumulative units on log-log axes and read "
            "the slope - that slope is the learning rate. Forecast future "
            "unit costs by extending the curve, but cap the learning where "
            "the process hits its engineered standard time; learning "
            "approaches the standard, it does not pass through it. Layer "
            "the other scale effects separately: spread fixed costs over "
            "planned volume, apply purchasing's volume-break schedule, and "
            "price the process changes volume enables - dedicated tooling, "
            "automation, full-container freight. Present scale economics as "
            "a curve of unit cost vs volume, not a single number, so "
            "decisions see what each extra thousand units actually buys."
        ),
        "key_points": [
            "Scale cuts unit cost four ways: fixed-cost spreading, learning, volume breaks, and volume-suited processes.",
            "Wright's 80 percent curve: each doubling of output cuts unit labor to 80 percent - 10.0, 8.0, 6.4 hours.",
            "The curve is steepest early: prototypes are brutally expensive, mature products are cheap.",
            "Learning approaches the engineered standard time - it never passes through it.",
            "The dark side: volume-bought low cost demands forecast accuracy, or scale becomes expensive storage.",
        ],
        "requirements": [
            "Early production labor data to fit the learning rate.",
            "The engineered standard time as the learning floor.",
            "Fixed-cost pools and purchasing volume-break schedules.",
            "Volume forecasts with stated confidence, not single-point wishes.",
        ],
        "standards": [
            "Wright TP Factors Affecting the Cost of Airplanes 1936 - the learning curve.",
            "Horngren Datar Rajan Cost Accounting - economies of scale and cost behavior.",
        ],
        "citations": [CIT_WRIGHT, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "abc",
        "name": "Activity-Based Costing",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Traditional costing spreads overhead peanut-butter style - one "
            "rate over labor hours - and it lies whenever products consume "
            "activities unevenly. Activity-based costing, from Cooper and "
            "Kaplan's landmark 1988 work, traces overhead to the activities "
            "that actually cause it, then to the products that consume "
            "those activities. The demonstration is stark: 200,000 dollars "
            "of overhead over 10,000 labor hours gives a 20-dollar rate; "
            "product A with 8,000 hours absorbs 160,000 and product B with "
            "2,000 absorbs 40,000. But setups tell another story - B needs "
            "80 of the 100 setups. Splitting the pool by activity drivers "
            "(800 dollars per setup for the 80,000-dollar setup pool, the "
            "rest by labor hours) reprices A at 112,000 and B at 88,000. "
            "Product B was subsidized by 48,000 dollars under the old math - "
            "the high-variety, low-volume product looked cheap because the "
            "simple high-volume product was carrying its setups. ABC does "
            "not change total cost; it changes who the cost belongs to, and "
            "that changes every pricing decision."
        ),
        "how_it_works": (
            "Identify the activities that consume overhead: setups, "
            "inspections, purchase orders, engineering changes, material "
            "moves. Build a cost pool per activity and choose its driver - "
            "the measurable thing that makes the activity happen. Compute "
            "the driver rate: pool divided by total driver quantity. Charge "
            "each product for the drivers it actually consumes. Products "
            "with many setups, small batches, and frequent engineering "
            "changes absorb far more cost than their labor hours suggest, "
            "which is exactly the distortion ABC exists to fix. Use ABC "
            "for decisions - pricing, mix, outsourcing - while keeping the "
            "traditional system for financial reporting if the auditors "
            "require it."
        ),
        "key_points": [
            "ABC traces overhead to activities, then to products by the drivers they actually consume.",
            "Example: traditional costing priced B at 40,000; ABC reprices it at 88,000 - a 48,000 subsidy exposed.",
            "High-variety, low-volume products are the usual subsidy recipients under peanut-butter allocation.",
            "Driver rates = activity pool divided by total driver quantity; charge products for drivers consumed.",
            "ABC changes cost assignment, not total cost - and that reassignment changes every pricing decision.",
        ],
        "requirements": [
            "Activities identified with their cost pools.",
            "Measurable drivers that plausibly cause each activity.",
            "Driver quantities consumed per product.",
            "A decision process that actually uses the ABC numbers.",
        ],
        "standards": [
            "Cooper R Kaplan RS Measure Costs Right: Make the Right Decisions HBR 1988.",
            "Horngren Datar Rajan Cost Accounting - activity-based costing systems.",
        ],
        "citations": [CIT_COOPER, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "should_cost",
        "name": "Should-Cost Analysis",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Should-cost analysis builds the price a part ought to carry "
            "from raw economics instead of accepting the quote on the "
            "table. Take a steel bracket: 0.5 kilograms of steel at 3.00 "
            "dollars per kilogram is 1.50 of material; half a minute on a "
            "90-dollar-per-hour press is 0.75; labor 0.45 and overhead 0.60 "
            "complete the factory cost at 3.30 dollars, and a 12 percent "
            "supplier margin sets the should-cost at about 3.70 dollars. "
            "Against a 4.10-dollar quote, the gap is 0.40 dollars - nearly "
            "10 percent - and now the negotiation has a map: which chamber "
            "of the cost is the supplier actually charging for? Should-cost "
            "is built from commodity prices, standard machine rates, and "
            "engineered time standards, so it cannot be bluffed by a "
            "confident quote. It does not accuse anyone of overcharging; it "
            "simply shows what the physics and the markets say the part "
            "costs, and invites the supplier to explain the difference."
        ),
        "how_it_works": (
            "Decompose the part into material, process steps, and "
            "secondary operations. Price material from commodity indices "
            "plus a stated scrap and utilization allowance. Time each "
            "process step from standards or measured data and apply "
            "published machine-hour and labor rates for the region. Add "
            "tooling amortization over a stated volume, packaging, and a "
            "reasonable supplier margin - typically 8 to 15 percent for "
            "competitive processes. The result is the should-cost. Compare "
            "it to the quote line by line: the variance in each chamber "
            "becomes a negotiation topic. Refresh should-costs when "
            "commodity prices move, because a should-cost built on last "
            "year's steel price is last year's argument."
        ),
        "key_points": [
            "Should-cost = engineered material + process + tooling + margin, built from markets and standards, not quotes.",
            "Example: 3.30 factory cost plus 12 percent margin = 3.70 should-cost vs 4.10 quote - a 10 percent gap with a map.",
            "Each chamber's variance becomes a negotiation topic instead of a take-it-or-leave-it price.",
            "Commodity indices and published regional rates make the model bluff-proof.",
            "Refresh with commodity prices; a stale should-cost is last year's argument.",
        ],
        "requirements": [
            "Commodity price indices with dates for the material chamber.",
            "Engineered time standards and regional machine and labor rates.",
            "A stated volume for tooling amortization and a stated margin range.",
            "Quote breakdowns detailed enough to compare chamber by chamber.",
        ],
        "standards": [
            "APICS Dictionary - should-cost and cost modeling terminology.",
            "Horngren Datar Rajan Cost Accounting - cost estimation methods.",
        ],
        "citations": [CIT_APICS, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "target_cost",
        "name": "Target Costing and Design-to-Cost",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Target costing works the cost equation backwards: the market "
            "sets the price, the business sets the required margin, and "
            "the product must be designed to fit what is left. A gadget "
            "aimed at a 49.99-dollar retail shelf, where the retailer keeps "
            "50 percent, must wholesale at 25.00 dollars; if the company "
            "needs a 35 percent margin on wholesale, the factory cost "
            "target is 16.25 dollars. That number becomes the design "
            "budget, decomposed to every subsystem and part before the "
            "first sketch is final. Design-to-cost is the engineering "
            "discipline that lives inside the target: cost as a design "
            "requirement with the same standing as weight, power, and "
            "performance. When a feature blows the target, the team "
            "redesigns the feature - it does not renegotiate the target. "
            "Born in Japanese manufacturing and battle-tested across "
            "decades, target costing is how companies sell at market "
            "prices and still make money, instead of costing whatever the "
            "design happens to weigh and hoping the market agrees."
        ),
        "how_it_works": (
            "Start from the researched market price at the expected volume "
            "and channel. Subtract the channel margins - retailer, "
            "distributor - to reach the required wholesale or net revenue. "
            "Subtract the company's required profit margin to reach the "
            "allowable cost: the target. Decompose the target through the "
            "product structure to subsystem and component targets, using "
            "function-cost analysis to protect the features customers "
            "actually value. Track estimated cost against target through "
            "design reviews with the same rigor as the performance spec. "
            "When estimates exceed targets, value engineering removes cost "
            "without removing valued function - the discipline that keeps "
            "the target honest."
        ),
        "key_points": [
            "Target cost = market price minus channel margins minus required profit - the equation runs backwards.",
            "Example: 49.99 retail, 50 percent retail margin, 35 percent company margin = 16.25 factory target.",
            "The target is a design budget, decomposed to subsystems before the design is final.",
            "Cost stands as a requirement equal to weight, power, and performance - features fit the target, not vice versa.",
            "Value engineering protects valued function while removing cost when estimates exceed targets.",
        ],
        "requirements": [
            "A researched market price at a stated volume and channel.",
            "Channel margin structure and the company's required profit margin.",
            "A decomposition method from product target to component targets.",
            "Design reviews that track cost against target like a performance spec.",
        ],
        "standards": [
            "Boothroyd Dewhurst Knight Product Design for Manufacture and Assembly - design-to-cost methods.",
            "Horngren Datar Rajan Cost Accounting - target costing.",
        ],
        "citations": [CIT_BOOTHROYD, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
])

ENTRIES.extend([
    {
        "key": "margin_math",
        "name": "Margin Math: Unit Cost vs Wholesale vs Retail",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Between the factory floor and the customer's hands, the same "
            "product wears three different prices, and each step takes its "
            "cut by its own rule. Trace one unit: factory cost 10.50 "
            "dollars, wholesale price 18.00 dollars, retail price 36.00 "
            "dollars. Markup and margin are not synonyms, and confusing "
            "them is the most expensive arithmetic error in business. "
            "Markup is profit over cost: (18.00 - 10.50) / 10.50 = 71.4 "
            "percent at wholesale. Margin is profit over price: (18.00 - "
            "10.50) / 18.00 = 41.7 percent on the wholesale sale, and "
            "(36.00 - 18.00) / 36.00 = 50.0 percent at retail. The "
            "retailer's 50 percent margin sounds enormous until the rent, "
            "staff, shrinkage, and unsold inventory come out of it. Every "
            "player in the chain needs its margin to survive, which is why "
            "a 10.50-dollar cost becomes a 36-dollar price - and why "
            "cutting out a layer, selling direct, is the oldest margin "
            "strategy in commerce."
        ),
        "how_it_works": (
            "Build the chain rung by rung. Factory cost is the unit "
            "manufacturing cost plus any packaging and inbound freight the "
            "maker absorbs. Wholesale price adds the maker's margin - set "
            "by required return, competition, and channel power. Retail "
            "price adds the retailer's margin, which must cover the store's "
            "operating costs and profit. At each rung compute both markup "
            "(over cost, for pricing decisions) and margin (over price, "
            "for profit reporting), because the two answer different "
            "questions. Convert fluently: a 50 percent margin equals a 100 "
            "percent markup, and the conversion is margin = markup / (1 + "
            "markup). Audit the chain periodically - margin stacked at "
            "every layer is why direct-to-customer models can undercut "
            "traditional retail while earning more per unit."
        ),
        "key_points": [
            "Markup = profit over cost; margin = profit over price - different denominators, different answers.",
            "Example chain: 10.50 cost, 18.00 wholesale (71.4 percent markup, 41.7 percent margin), 36.00 retail (50 percent margin).",
            "A 50 percent margin equals a 100 percent markup: margin = markup / (1 + markup).",
            "Each layer's margin must cover that layer's operating costs - the chain price is survival arithmetic.",
            "Removing a layer (direct sale) is the oldest margin strategy: fewer cuts of the same pie.",
        ],
        "requirements": [
            "True factory cost per unit including packaging and inbound freight.",
            "Each channel layer's required margin and operating cost structure.",
            "Discipline to quote margin on price and markup on cost without mixing them.",
            "Periodic chain audits as costs and channel power shift.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - gross margin and markup analysis.",
            "APICS Dictionary - markup, margin, and channel pricing terminology.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "breakeven",
        "name": "Contribution Margin and Break-Even",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Every unit sold makes two contributions: first it pays its own "
            "variable cost, then whatever is left attacks the fixed costs. "
            "That leftover is the contribution margin, and it is the most "
            "decision-useful number in cost accounting. A product priced at "
            "25.00 dollars with 16.25 dollars of variable cost contributes "
            "8.75 dollars per unit. Against 87,500 dollars of fixed costs - "
            "rent, salaries, the tooling already bought - the break-even "
            "point is 87,500 / 8.75 = 10,000 units. Sell the 10,001st unit "
            "and 8.75 dollars of pure profit appears, because the fixed "
            "costs are already covered. This is why volume discounts, "
            "promotional pricing, and overtime decisions all run through "
            "contribution margin: any price above variable cost helps pay "
            "the fixed nut, and any price below it digs the hole deeper. "
            "Fixed costs are the mountain; contribution margin is the "
            "shovel."
        ),
        "how_it_works": (
            "Separate costs into variable - changing with each unit: "
            "material, piece-rate labor, packaging, sales commission - and "
            "fixed - rent, salaries, insurance, depreciation. Contribution "
            "margin per unit is price minus variable cost per unit; the "
            "contribution margin ratio is that figure divided by price. "
            "Break-even units equal total fixed costs divided by "
            "contribution margin per unit; break-even revenue is fixed "
            "costs divided by the ratio. The margin of safety - actual or "
            "planned sales minus break-even sales - measures how far volume "
            "can fall before losses start. Recompute whenever prices, "
            "variable costs, or fixed costs move, because break-even is a "
            "photograph, not a monument."
        ),
        "key_points": [
            "Contribution margin = price minus variable cost per unit - the amount each sale aims at fixed costs.",
            "Example: 25.00 - 16.25 = 8.75 contribution; 87,500 fixed / 8.75 = 10,000 units to break even.",
            "Past break-even, each unit's full contribution margin becomes profit - the operating leverage effect.",
            "Any price above variable cost helps cover fixed costs; any price below digs deeper.",
            "Margin of safety (sales minus break-even sales) measures how far volume can fall before losses.",
        ],
        "requirements": [
            "A clean variable vs fixed cost split - the classification everything depends on.",
            "Price and variable cost per unit at the decision's volume.",
            "Total fixed costs for the period, stated honestly.",
            "Recomputation whenever price, variable, or fixed inputs move.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - cost-volume-profit analysis.",
            "APICS Dictionary - contribution margin and break-even definitions.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "make_buy_tco",
        "name": "Make vs Buy: Total Cost of Ownership",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The foundations record compared avoidable make cost to buy "
            "price; the advanced version counts everything the decision "
            "truly owns. Total cost of ownership adds the costs the simple "
            "comparison hides: tooling, freight, incoming inspection, "
            "quality failures, inventory carrying, and supply risk. Run the "
            "full comparison at 50,000 units. Make: 5.25 dollars avoidable "
            "cost per unit is 262,500 dollars, plus 40,000 of tooling the "
            "make option requires - 302,500 total. Buy: 5.80 per unit is "
            "290,000, plus 12,500 freight, 5,000 incoming inspection, and "
            "8,000 of priced supply risk - 315,500 total. Making wins by "
            "13,000 dollars, a verdict the headline prices alone would "
            "have reversed. TCO also prices the strategic factors the "
            "spreadsheet cannot: capacity freed or consumed, process "
            "knowledge kept or lost, and the option value of controlling "
            "your own supply. The cheapest quote is rarely the cheapest "
            "decision."
        ),
        "how_it_works": (
            "Build two full cost stacks over the decision horizon - "
            "typically the contract life or the tool life. The make stack: "
            "avoidable unit cost times volume, plus tooling and NRE, plus "
            "any freed-or-consumed capacity effects, plus the cost of "
            "carrying the process knowledge. The buy stack: purchase price "
            "times volume, plus freight and duty, incoming inspection and "
            "quality administration, inventory carrying cost on the longer "
            "pipeline, and a priced risk premium for single-source or "
            "distant supply. Compare totals, then stress-test: what volume "
            "flips the verdict, what quality failure rate flips it, what "
            "lead-time change flips it. Present the crossover points, not "
            "just the winner, so the decision survives contact with "
            "reality."
        ),
        "key_points": [
            "TCO = the full owned cost of each option over the decision horizon, not just unit price vs unit cost.",
            "Example at 50,000 units: make 302,500 total vs buy 315,500 total - making wins by 13,000.",
            "Hidden buy-side costs: freight, duty, inspection, pipeline inventory, and priced supply risk.",
            "Hidden make-side costs: tooling, capacity consumed, and process knowledge that must be maintained.",
            "Report crossover points - the volume, quality, and lead-time values that flip the verdict.",
        ],
        "requirements": [
            "A decision horizon: contract life or tool life, stated.",
            "Complete cost stacks for both options including risk premiums.",
            "Volume forecasts with the crossover volume computed.",
            "Strategic factors - capacity, knowledge, control - priced or explicitly noted.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - relevant cost over the decision horizon.",
            "APICS Dictionary - total cost of ownership.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "parametric",
        "name": "Parametric Cost Estimation",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When no design exists yet, estimators cost the future from the "
            "past: parametric estimation fits cost estimating relationships "
            "- CERs - that tie cost to the physical parameters that drive "
            "it. Weight, power, lines of code, part count, and throughput "
            "are the classic cost drivers. A fitted CER for a family of "
            "enclosures might read: cost = 120 times weight in kilograms "
            "raised to the 0.8 power. A 5-kilogram enclosure then estimates "
            "at 120 times 3.624, about 434.90 dollars. The 0.8 exponent "
            "carries the economics: below 1.0, cost grows slower than "
            "weight - the scale effect baked into the math. CERs are built "
            "by regression on completed projects, so their honesty depends "
            "entirely on the dataset: enough points, similar technology, "
            "costs normalized to today's dollars. A CER is a statistical "
            "promise with a confidence interval, not a quote - but early in "
            "a program, when the design is a sketch and the budget is real, "
            "it is the best promise available."
        ),
        "how_it_works": (
            "Gather historical cost data for completed, comparable items "
            "with their parameter values. Normalize every cost to constant "
            "dollars and comparable scope - development vs production, "
            "prototype vs mature. Regress cost against the parameters, "
            "usually in log-log form so the relationship becomes a power "
            "law, and check the fit: R-squared, residual patterns, and "
            "whether the exponent makes engineering sense. Apply the CER "
            "to the new item's parameters for the point estimate, and "
            "report the prediction interval honestly. Refresh the CER as "
            "new actuals arrive; a CER that never learns is a rumor with "
            "a formula. Never extrapolate far beyond the data range - the "
            "math is confident there precisely because it has no evidence."
        ),
        "key_points": [
            "Parametric estimation fits cost estimating relationships from historical data to cost-driving parameters.",
            "Example CER: cost = 120 x weight^0.8; a 5 kg enclosure estimates at about 434.90 dollars.",
            "Exponents below 1.0 encode scale effects: cost grows slower than the parameter.",
            "CER honesty = dataset quality: enough points, similar technology, costs normalized to constant dollars.",
            "Report the prediction interval; never extrapolate far beyond the data that built the curve.",
        ],
        "requirements": [
            "Historical cost and parameter data for comparable completed items.",
            "Normalization to constant dollars and comparable scope.",
            "Regression diagnostics: fit quality and engineering sense of the exponents.",
            "Prediction intervals reported with every point estimate.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - cost estimation and learning curves.",
            "APICS Dictionary - parametric estimating.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "quality_cost",
        "name": "Cost of Poor Quality",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Poor quality has a price tag, and Juran's framework sorts it "
            "into four buckets: prevention, appraisal, internal failure, "
            "and external failure. A plant spending 20,000 dollars on "
            "prevention (training, mistake-proofing), 35,000 on appraisal "
            "(inspection, testing), 60,000 on internal failure (scrap, "
            "rework found in-house), and 120,000 on external failure "
            "(warranty, returns, field fixes) carries a cost of poor "
            "quality of 235,000 dollars. Against 4,700,000 dollars of "
            "sales, that is 5.0 percent of revenue spent on quality going "
            "wrong - and the industry rule of thumb says most companies "
            "sit between 5 and 15 percent without knowing it. The "
            "economics are asymmetric: external failures cost multiples "
            "of internal ones, because the customer does the discovering "
            "and the brand pays the interest. Every dollar moved from "
            "failure to prevention typically returns several - which is "
            "why the cost-of-quality report is the business case for "
            "quality programs, written in the only language every executive "
            "reads."
        ),
        "how_it_works": (
            "Capture the four buckets from the accounts: prevention from "
            "training, quality engineering, and process-control budgets; "
            "appraisal from inspection and test labor and equipment; "
            "internal failure from scrap and rework records; external "
            "failure from warranty claims, returns processing, field "
            "service, and goodwill concessions. Total them into the cost "
            "of poor quality and express it as a percent of sales - the "
            "headline metric. Trend it quarterly and slice it by product "
            "line and failure mode so improvement teams can aim. The "
            "classic improvement pattern: raise prevention spending "
            "deliberately, watch appraisal and failure fall by multiples, "
            "and report the net as the program's return."
        ),
        "key_points": [
            "Four buckets: prevention, appraisal, internal failure, external failure - total them for the cost of poor quality.",
            "Example: 20,000 + 35,000 + 60,000 + 120,000 = 235,000 dollars, or 5.0 percent of 4,700,000 in sales.",
            "External failures cost multiples of internal ones - the customer discovers them and the brand pays interest.",
            "Most companies sit at 5 to 15 percent of sales in poor-quality cost without measuring it.",
            "Dollars moved from failure to prevention typically return severalfold - the business case for quality.",
        ],
        "requirements": [
            "Scrap, rework, warranty, and returns data captured by cause.",
            "Prevention and appraisal budgets tracked as quality spend.",
            "Sales figures for the percent-of-sales headline metric.",
            "Quarterly trending sliced by product line and failure mode.",
        ],
        "standards": [
            "Juran JM Godfrey AB Juran's Quality Handbook - cost of poor quality framework.",
            "Horngren Datar Rajan Cost Accounting - quality cost reporting.",
        ],
        "citations": [CIT_JURAN, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "lifecycle",
        "name": "Lifecycle Costing",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The purchase price is the cover charge; lifecycle cost is the "
            "whole evening. A machine bought for 85,000 dollars that burns "
            "6,000 dollars of energy, 9,000 of maintenance, and 40,000 of "
            "labor per year costs 55,000 dollars annually to own. Over a "
            "ten-year life that is 550,000 dollars of operating cost, plus "
            "5,000 for end-of-life disposal, minus 8,000 of salvage value - "
            "a lifecycle cost of 632,000 dollars. The 85,000-dollar price "
            "was 13 percent of the real number. Lifecycle costing exists "
            "because the cheapest machine to buy is routinely the most "
            "expensive machine to own: higher energy draw, pricier spares, "
            "shorter life. The same lens prices products for customers - "
            "total cost of ownership is lifecycle costing from the "
            "buyer's side - and it is why energy efficiency, reliability, "
            "and maintainability are cost features, not luxury features."
        ),
        "how_it_works": (
            "Define the life: service years or lifetime units, stated. "
            "List acquisition cost - price plus installation, training, and "
            "commissioning. Estimate annual operating costs: energy at "
            "measured draw, maintenance parts and labor, consumables, "
            "operators, and floor space. Add periodic overhauls and the "
            "end-of-life cost: decommissioning, disposal, or remediation. "
            "Subtract residual or salvage value. Discount future years to "
            "present value if the comparison spans enough time for money "
            "to matter. Compare alternatives on lifecycle total, not "
            "purchase price, and show the crossover year when the "
            "efficient-but-pricey option pulls ahead - decision-makers "
            "remember the year, not the integral."
        ),
        "key_points": [
            "Lifecycle cost = acquisition + lifetime operating + disposal - salvage; the price is usually the smallest part.",
            "Example: 85,000 price + 550,000 operating + 5,000 disposal - 8,000 salvage = 632,000 dollars over ten years.",
            "The cheapest machine to buy is routinely the most expensive to own - energy, spares, and life decide.",
            "Reliability and efficiency are cost features: they move the operating years, not the price tag.",
            "Show the crossover year when the efficient option pulls ahead - it is the number people remember.",
        ],
        "requirements": [
            "A stated service life in years or lifetime units.",
            "Measured or engineered annual operating costs by category.",
            "Overhaul, disposal, and salvage estimates.",
            "Discounting applied when the horizon makes money's time value material.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - life-cycle costing and time value.",
            "APICS Dictionary - life-cycle cost.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "transfer_pricing",
        "name": "Transfer Pricing Between Plants",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "When one plant sells to another inside the same company, the "
            "price they charge each other - the transfer price - decides "
            "where profit appears and who gets credit for it. The workhorse "
            "method is cost-plus: the making plant's cost with an agreed "
            "markup. A component costing 10.50 dollars transferred at cost "
            "plus 15 percent moves at 12.08 dollars. The buying plant sees "
            "12.08 as its material cost; the selling plant books 1.58 of "
            "profit. Set the markup too low and the making plant looks like "
            "a charity; too high and the buying plant cannot compete. Tax "
            "authorities police cross-border transfer prices under the "
            "arm's-length principle - the price must resemble what "
            "unrelated parties would charge - because profit placed in a "
            "low-tax country is tax strategy wearing a cost-accounting "
            "costume. Inside one country, the transfer price is a "
            "management tool: it should motivate the selling plant to be "
            "efficient and let the buying plant make honest make-vs-buy "
            "decisions."
        ),
        "how_it_works": (
            "Choose the method by situation. Cost-plus uses full cost or "
            "variable cost plus a markup - simple, auditable, but it passes "
            "inefficiency downstream. Market-based pricing uses the outside "
            "price when a real market exists - the cleanest answer, "
            "because it is the make-vs-buy price by definition. Negotiated "
            "prices let plant managers bargain within guardrails, "
            "preserving autonomy. Document the method, the cost base, and "
            "the markup with the same rigor as a customer price, because "
            "tax authorities and auditors will read it. Review when costs "
            "move: a transfer price frozen while costs rise quietly taxes "
            "the buying plant for the selling plant's inflation."
        ),
        "key_points": [
            "The transfer price decides where profit appears between plants and who gets credit.",
            "Example: 10.50 cost at cost-plus 15 percent = 12.08 transfer; seller books 1.58 profit per unit.",
            "Methods: cost-plus (simple, passes inefficiency), market-based (cleanest when a market exists), negotiated.",
            "Cross-border prices must satisfy the arm's-length principle - tax authorities read these documents.",
            "Review transfer prices when costs move; a frozen price taxes the buyer for the seller's inflation.",
        ],
        "requirements": [
            "A stated method: cost-plus, market-based, or negotiated, with the cost base defined.",
            "The markup or market reference, documented like a customer price.",
            "Arm's-length support for cross-border transfers.",
            "A review trigger tied to cost movements.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - transfer pricing methods.",
            "APICS Dictionary - transfer price definitions.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "dfm_cost",
        "name": "Design-for-Manufacturing Cost Decisions",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "By the time a design reaches the factory, most of its cost is "
            "already decided - the old rule says 70 to 80 percent of cost "
            "is locked in at the drawing board. Design for manufacturing "
            "attacks cost where it is born. The sharpest lever is part "
            "count: every part carries insertion, fastening, handling, and "
            "quality risk. An assembly with 24 parts at 0.35 dollars of "
            "insertion cost each carries 8.40 dollars of assembly cost; a "
            "redesign integrating functions down to 14 parts cuts it to "
            "4.90 dollars - 3.50 dollars per unit freed without touching "
            "material or labor rates. Boothroyd, Dewhurst, and Knight's "
            "method scores each part on whether it must be separate - must "
            "it move, must it be a different material, must it come apart "
            "- and every part that fails the test is a candidate for "
            "elimination. DFM also standardizes fasteners, loosens "
            "tolerances the function does not need, and designs parts to "
            "be made by the cheapest capable process. Cost reduced in "
            "design stays reduced for the product's whole life."
        ),
        "how_it_works": (
            "Run the Boothroyd-Dewhurst analysis on the assembly: time "
            "each part's handling and insertion, score the three "
            "separateness criteria, and compute the theoretical minimum "
            "part count. The gap between actual and minimum is the design "
            "efficiency - and the cost opportunity. Attack the gap by "
            "combining parts, using snap-fits and molded-in features, and "
            "standardizing fasteners to one or two sizes. Review tolerances "
            "against function: each tolerance tighter than needed is "
            "process cost priced in forever. Re-cost the redesign through "
            "the full stack - material, labor, overhead, tooling - because "
            "part-count reduction sometimes adds tooling cost that volume "
            "must justify."
        ),
        "key_points": [
            "70 to 80 percent of product cost is locked in during design - DFM attacks cost at its birth.",
            "Example: 24 parts at 0.35 insertion = 8.40; 14 parts = 4.90 - 3.50 per unit freed by integration.",
            "The Boothroyd test: a part must move, be a different material, or need separation - else eliminate it.",
            "Standardize fasteners, loosen unneeded tolerances, design for the cheapest capable process.",
            "Re-cost redesigns fully: integration can add tooling that volume must justify.",
        ],
        "requirements": [
            "Handling and insertion time data per part.",
            "The three-criteria separateness scoring done honestly.",
            "Function-based tolerance review with engineering sign-off.",
            "Full re-cost of the redesign including tooling changes.",
        ],
        "standards": [
            "Boothroyd Dewhurst Knight Product Design for Manufacture and Assembly 3rd ed.",
            "Horngren Datar Rajan Cost Accounting - design-stage cost management.",
        ],
        "citations": [CIT_BOOTHROYD, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "disruption_cost",
        "name": "Supply-Chain Disruption Costing",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A supply chain that never breaks is a supply chain whose "
            "breakage cost was never priced. Disruption costing puts the "
            "number on the table: probability times consequence, weighed "
            "against the cost of resilience. A sole-sourced component with "
            "an 8 percent annual disruption probability and a 250,000-"
            "dollar cost per stockout event - idle lines, expedites, lost "
            "sales - carries an expected disruption cost of 20,000 dollars "
            "per year. Qualifying a second source costs 12,000 dollars per "
            "year in audit, quality, and split-volume premiums. The net "
            "benefit of resilience is 8,000 dollars a year, and the "
            "decision makes itself. The consequence side deserves the real "
            "work: line-down cost per hour, expedite freight multiples, "
            "contractual penalties, and the lost-margin math on missed "
            "shipments. Companies that price disruption buy resilience "
            "where it pays and accept risk where it does not; companies "
            "that do not price it buy neither and are surprised by both."
        ),
        "how_it_works": (
            "Map the critical single points: sole sources, single "
            "factories, single ports, single materials. For each, estimate "
            "annual disruption probability from history, geography, and "
            "supplier health. Build the consequence stack: downtime cost "
            "per hour times expected hours, expedite premiums, penalties, "
            "and lost contribution margin on missed sales. Multiply for "
            "expected annual disruption cost. Price the mitigations: dual "
            "sourcing, safety stock carrying cost, buffer capacity, "
            "nearshoring premiums. Fund mitigations where expected loss "
            "exceeds mitigation cost, and document the accepted risks "
            "where it does not - an accepted risk is a decision, an "
            "unpriced risk is an accident waiting for a date."
        ),
        "key_points": [
            "Disruption cost = annual probability times full consequence; compare against resilience cost.",
            "Example: 8 percent x 250,000 = 20,000 expected loss vs 12,000 dual-source cost - resilience nets 8,000.",
            "Consequence stacks downtime, expedites, penalties, and lost margin on missed shipments.",
            "Fund mitigation where expected loss exceeds its cost; document accepted risks as decisions.",
            "Unpriced risk is not risk management - it is an accident waiting for a date.",
        ],
        "requirements": [
            "Single-point-of-failure mapping across sources, sites, and lanes.",
            "Disruption probabilities from history, geography, and supplier health.",
            "Consequence stacks with downtime rates and lost-margin math.",
            "Mitigation costs priced comparably: dual source, stock, capacity, nearshoring.",
        ],
        "standards": [
            "APICS Dictionary - supply chain risk and resilience terminology.",
            "Horngren Datar Rajan Cost Accounting - expected value in cost decisions.",
        ],
        "citations": [CIT_APICS, CIT_HORNGREN],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "compliance_cost",
        "name": "Environmental and Compliance Cost",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Regulations are a cost layer like any other: they must be "
            "measured, allocated, and priced into the product, or they get "
            "paid out of margin by surprise. A mid-size plant's compliance "
            "stack - permits, emissions monitoring, waste handling, safety "
            "training, restricted-substance testing, audit fees - can total "
            "96,000 dollars a year; over 240,000 units that is 0.40 dollars "
            "per unit of compliance cost. The honest treatment separates "
            "three kinds: compliance that prevents harm (proper waste "
            "handling), compliance that documents diligence (testing and "
            "reporting), and non-compliance risk priced as expected "
            "penalties. Design choices move the number enormously: a "
            "material free of restricted substances deletes a whole "
            "testing program, and a process that generates no hazardous "
            "waste deletes a disposal contract. Compliance cost is also "
            "where the cheapest quote often cheats - a supplier thousands "
            "of miles away may simply not be paying it, and that discount "
            "evaporates the day the regulation arrives at your dock."
        ),
        "how_it_works": (
            "Inventory the obligations: environmental permits, emissions "
            "and effluent limits, hazardous waste rules, workplace safety "
            "standards, restricted-substance regulations for the product's "
            "markets, and labeling requirements. Cost each: fees, monitoring "
            "equipment and labor, waste contracts, training hours, testing "
            "per batch or per year, and audit support. Allocate to "
            "products by the driver each obligation follows - waste cost by "
            "waste generated, testing by batches tested, permits by floor "
            "space or revenue. Price design alternatives by their "
            "compliance footprint, because a cleaner design is often a "
            "cheaper design once this layer is visible. Track regulatory "
            "change as a cost forecast input, not as a surprise."
        ),
        "key_points": [
            "Compliance is a cost layer: measure it, allocate it, price it - or pay it from margin by surprise.",
            "Example: 96,000 dollars annual compliance over 240,000 units = 0.40 dollars per unit.",
            "Design moves the number: restricted-substance-free materials delete testing programs.",
            "Allocate by driver: waste by waste generated, testing by batches, permits by space or revenue.",
            "Suspiciously cheap quotes may simply skip compliance - the discount evaporates when regulation arrives.",
        ],
        "requirements": [
            "A complete obligation inventory across environmental, safety, and product regulations.",
            "Annual cost per obligation: fees, labor, contracts, testing, training.",
            "Allocation drivers that follow each obligation honestly.",
            "Regulatory-change tracking as a cost forecast input.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - cost allocation by cost driver.",
            "APICS Dictionary - compliance and regulatory cost terminology.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "twenty_cent",
        "name": "The 20-Cent Lesson: Cost Differentiation at Scale",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This is the lesson the whole database was built to teach: a "
            "product that costs 0.20 dollars to make can sell for 40 "
            "dollars, and the 200-to-1 ratio is not a trick - it is the "
            "value stack made visible. Decompose the 40 dollars: 0.20 of "
            "factory cost, 1.80 of freight, packaging, and duties to move "
            "it around the world, and the rest is the stack of value the "
            "market pays for - design, brand trust, distribution that puts "
            "it in your hand today, warranty that stands behind it, and "
            "the retailer's shelf, staff, and lights. The factory cost is "
            "one line among many, and at scale it becomes almost a "
            "rounding error - which is exactly why manufacturing cost "
            "mastery matters most at scale: a 0.02-dollar saving on a "
            "million units is 20,000 dollars, while the selling price "
            "barely notices. The lesson cuts both ways: cost discipline "
            "without value creation races to the bottom, and value "
            "creation without cost discipline leaks the margin it earned. "
            "Know your 0.20, price your 40, and never confuse the two."
        ),
        "how_it_works": (
            "Build the full value stack for the product: factory cost "
            "from the cost stack in this database's first records, "
            "inbound and outbound logistics, duties, packaging, channel "
            "margins at each layer, marketing and brand investment per "
            "unit, warranty reserves, and retail operating cost. Express "
            "each as dollars and as a share of the selling price. The "
            "factory-cost share is usually the smallest slice - that is "
            "normal, not scandalous. Use the stack two ways: downward, to "
            "find which cost lines scale can crush; upward, to find which "
            "value lines justify the price. Revisit the stack when any "
            "layer's economics shift, because a 200-to-1 ratio built on "
            "yesterday's freight rates is nostalgia, not analysis."
        ),
        "key_points": [
            "A 0.20-dollar factory cost inside a 40-dollar price is a 200-to-1 ratio - the value stack made visible.",
            "The stack: factory cost, logistics, duties, packaging, channel margins, brand, warranty, retail operations.",
            "At scale the factory cost becomes tiny - which is why small unit savings are worth fortunes in volume.",
            "A 0.02 saving at a million units is 20,000 dollars the price never has to move to earn.",
            "Cost discipline without value creation races to the bottom; value without cost discipline leaks margin.",
        ],
        "requirements": [
            "The true factory unit cost from the standard cost stack.",
            "Logistics, duty, and packaging costs per unit at actual volumes.",
            "Each channel layer's margin and operating cost.",
            "Brand, warranty, and retail cost allocations per unit.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - value chain and margin analysis.",
            "APICS Dictionary - value-added cost terminology.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
    {
        "key": "cost_audit",
        "name": "Cost Audit: Verifying What a Thing Really Costs",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A cost audit is the discipline of proving a cost instead of "
            "trusting it - teardown, re-price, and reconcile until the "
            "number confesses. The method: disassemble the product, "
            "identify every component, weigh the materials, time the "
            "assembly, and re-price each line from independent sources. A "
            "teardown of a small device finds 12 components repriced from "
            "distributor data totaling 6.40 dollars against a claimed "
            "material cost of 8.90 dollars - a 2.50-dollar variance, 28 "
            "percent, hiding in the quote. The audit then asks the only "
            "question that matters: is the gap inefficiency, margin, or "
            "error? Each answer leads somewhere different - inefficiency "
            "to process work, margin to negotiation, error to correction. "
            "Cost audits run on suppliers, on internal estimates, and on "
            "your own products before competitors run them for you. The "
            "rule is simple: every important cost gets verified from an "
            "independent source at least once, because costs that are "
            "never checked are never quite true."
        ),
        "how_it_works": (
            "Select the target: the highest-spend parts, the most "
            "suspicious quotes, the products facing price pressure. "
            "Teardown and catalog: every component identified, every "
            "material weighed, every process step timed. Re-price "
            "independently: distributor pricing for components, commodity "
            "indices for materials, standard rates for labor and machine "
            "time. Build the should-cost from the teardown data and "
            "reconcile against the claimed cost line by line. Classify "
            "each variance as inefficiency, margin, or error, and route it: "
            "inefficiency to engineering, margin to procurement's "
            "negotiation file, error to immediate correction. File the "
            "audit so the next quote on the same part starts from "
            "evidence, not from memory."
        ),
        "key_points": [
            "Cost audit = teardown, independent re-pricing, and line-by-line reconciliation until the number confesses.",
            "Example: teardown reprices 12 components at 6.40 vs 8.90 claimed - a 2.50 variance, 28 percent.",
            "Classify every variance: inefficiency goes to engineering, margin to negotiation, error to correction.",
            "Audit suppliers, internal estimates, and your own products - before competitors audit them for you.",
            "Every important cost gets verified from an independent source at least once; unchecked costs drift.",
        ],
        "requirements": [
            "Teardown capability: disassembly, identification, weighing, timing.",
            "Independent price sources: distributors, commodity indices, standard rates.",
            "A should-cost model to reconcile against.",
            "A routing discipline: inefficiency, margin, and error each go somewhere different.",
        ],
        "standards": [
            "Horngren Datar Rajan Cost Accounting - cost verification and variance investigation.",
            "APICS Dictionary - teardown and should-cost terminology.",
        ],
        "citations": [CIT_HORNGREN, CIT_APICS],
        "sig_lens": SIG_LENS,
    },
])
