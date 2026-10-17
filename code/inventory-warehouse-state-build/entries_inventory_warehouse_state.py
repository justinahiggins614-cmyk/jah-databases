#!/usr/bin/env python3
"""Entries for the Inventory and Warehouse State databases (missing-115 Wave 1).

Item 53 of the 115-category missing-database audit: supply, inventory, and
warehouse state - actual stock, reservations, lead times, movement, expiry,
and replenishment. Verified 2026-10-17 against the full manifest (2,390
databases) plus every shard index in jah-databases-data-1: no existing
database is a dedicated inventory/warehouse-state database (keyword
near-hits 'inventory-*' slugs belong to unrelated domains: invisibility,
inventors, investing). BUILD NEW is the verdict.

Two NEW databases, 34 ladder-ordered records each:

  inventory-warehouse-state            - The Inventory and Warehouse State
                                       Database (public-harvest: real,
                                       fact-checked inventory theory and
                                       warehouse management - SKU and
                                       location data models, stock states,
                                       units of measure, FIFO/LIFO/FEFO,
                                       lead time, goods receipt and
                                       putaway, pick-pack-ship, lot and
                                       expiry tracking, cycle counting, ABC
                                       analysis, reorder-point math, EOQ,
                                       safety stock, reservations and
                                       allocation, putaway strategies,
                                       picking strategies, packing records,
                                       movement records, warehouse layout
                                       and slotting, multi-echelon
                                       inventory, MRP, accuracy, perpetual
                                       vs periodic systems, dynamic safety
                                       stock, replenishment systems,
                                       returns and RMAs, serialization,
                                       physical inventory, analytics, and
                                       the inventory health program;
                                       standard references Harris 1913 EOQ;
                                       Wilson 1934 reorder-point methods;
                                       Silver, Pyke, Peterson Inventory
                                       Management; Nahmias Production and
                                       Operations Analysis; Tompkins et al.
                                       Facilities Planning; Bartholdi and
                                       Hackman Warehouse & Distribution
                                       Science; Chopra and Meindl Supply
                                       Chain Management; APICS Dictionary;
                                       IAS 2 Inventories; ASC 330; GS1
                                       General Specifications; Ohno Toyota
                                       Production System; Womack and Jones
                                       Lean Thinking; OSHA 29 CFR 1910.176)
  inventory-warehouse-state-signature  - The Inventory and Warehouse State
                                       Signature Database (his original
                                       Signature Stock Method: every SKU a
                                       stamped note of state, every
                                       location a fixed address in the
                                       system, every movement a witnessed
                                       passage, stock states the truth of
                                       the shelf, safety stock the honor
                                       margin, replenishment the heartbeat;
                                       src signature, titles suffixed
                                       " (Signature Edition)", never
                                       presented as authentic public
                                       record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-INV- (public) and JAH-INVS- (signature), verified free in
the manifest id_prefix values (2,390 databases) and in all 792 shard index
files (zero exact hits; near-hits JAH-INVENT/Inventors, JAH-INVIS/
Invisibility, JAH-INVEST/Investing are unrelated domains).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_inventory_warehouse_state.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Stock Method: every "
            "SKU a stamped note of state, every location a fixed address in "
            "the system, every movement a witnessed passage, stock states "
            "the truth of the shelf, safety stock the honor margin, and "
            "replenishment the heartbeat of the store. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_HARRIS = ("Harris FW. How Many Parts to Make at Once. Factory, The "
              "Magazine of Management; 1913 (the original EOQ model).")
CIT_WILSON = ("Wilson RH. A Scientific Routine for Stock Control. Harvard "
              "Business Review; 1934 (early reorder-point methods).")
CIT_SILVER = ("Silver EA, Pyke DF, Peterson R. Inventory Management and "
              "Production Planning and Scheduling. 3rd ed. Wiley; 1998.")
CIT_NAHMIAS = ("Nahmias S. Production and Operations Analysis. 7th ed. "
               "Waveland Press; 2015.")
CIT_TOMPKINS = ("Tompkins JA et al. Facilities Planning. 4th ed. Wiley; "
                "2010 (warehouse layout, slotting, and material handling).")
CIT_BARTHOLDI = ("Bartholdi JJ, Hackman ST. Warehouse & Distribution "
                 "Science. Supply Chain and Logistics Institute; 2019.")
CIT_CHOPRA = ("Chopra S, Meindl P. Supply Chain Management: Strategy, "
              "Planning, and Operation. 7th ed. Pearson; 2018.")
CIT_APICS = ("APICS Dictionary. Association for Supply Chain Management "
             "(ASCM); 17th ed. (standard supply-chain terminology).")
CIT_IAS2 = ("IAS 2 Inventories. IFRS Foundation; inventories are measured "
            "at the lower of cost and net realisable value.")
CIT_ASC330 = ("ASC 330 Inventory. FASB Accounting Standards Codification; "
              "US GAAP guidance on inventory measurement.")
CIT_GS1 = ("GS1 General Specifications. Global standards for GTIN, SSCC, "
           "and logistics barcode labeling.")
CIT_OHNO = ("Ohno T. Toyota Production System: Beyond Large-Scale "
            "Production. Productivity Press; 1988 (kanban pull systems).")
CIT_WOMACK = ("Womack JP, Jones DT. Lean Thinking. 2nd ed. Free Press; "
              "2003 (waste elimination in operations).")
CIT_OSHA = ("OSHA 29 CFR 1910.176. Handling materials - storage, use and "
            "disposal (US rules for warehouse material handling).")
CIT_GROSS = ("Gross D, Harris CM. Fundamentals of Queueing Theory. Wiley "
             "(stockout and service-level statistics foundations).")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Inventory Is and What a Warehouse Holds",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Inventory is everything a business holds that has value and is "
            "waiting to be used, sold, or transformed. Raw materials wait to "
            "be built into products. Work in process waits between "
            "operations. Finished goods wait for customers. Maintenance and "
            "operating supplies wait for the day a machine needs them. A "
            "warehouse is the building where this waiting happens in an "
            "organized way: goods arrive, are received and checked, are "
            "stored in known locations, are picked and packed when needed, "
            "and ship out. Inventory costs money to hold - the purchase "
            "price, the space, the handling, the insurance, the risk of "
            "obsolescence - and it costs money to run out - lost sales, idle "
            "lines, angry customers. Inventory management is the discipline "
            "of holding the right amount: enough to serve demand and absorb "
            "variability, but no more. This record frames the whole "
            "database. Every later record is one shelf of the discipline: "
            "the atoms of stock data, the math that sets order points and "
            "quantities, the physical records of movement, and the health "
            "measures that keep the whole system honest. Start here and "
            "climb the ladder; every concept ahead assumes this one."
        ),
        "how_it_works": (
            "A warehouse works as a controlled buffer between supply and "
            "demand. Inbound flow begins with a purchase or production order "
            "telling the warehouse what is coming. Goods arrive at the "
            "receiving dock, are counted and inspected against the order, "
            "are labeled with identifiers, and are put away into storage "
            "locations. The system records every step, so the books always "
            "say what the shelves hold. Outbound flow begins with a customer "
            "order or production need. The system reserves stock, directs a "
            "picker to the locations, collects the goods, checks them at a "
            "pack station, and ships them with the right paperwork. Between "
            "the two flows sits the balance of the art: holding enough "
            "stock to keep promises, while the holding cost - typically 20 "
            "to 30 percent of inventory value per year - argues for holding "
            "less. The discipline resolves the tension with records and "
            "math: accurate counts, lead-time measurements, reorder points, "
            "order quantities, and cycle counts. The demo counts the "
            "records a simple warehouse keeps and shows how each category "
            "shares the work."
        ),
        "key_points": [
            "Inventory is value waiting: raw materials, work in process, finished goods, and supplies - and the warehouse is the organized place where the waiting happens.",
            "Holding stock costs 20 to 30 percent of its value per year (space, handling, capital, risk); running out costs lost sales and idle operations.",
            "A warehouse has two flows - inbound (receive, check, put away) and outbound (reserve, pick, pack, ship) - and the system records every step of both.",
            "Inventory management resolves the holding-versus-shortage tension with records and math, not with guessing.",
            "Every later record in this database is one shelf of this discipline: data models, counting, issuing rules, reorder math, movement records, and health measures.",
        ],
        "requirements": [
            "A definition of what counts as inventory in the business, so everyone counts the same thing.",
            "A named warehouse or storage area with receiving and shipping zones, even if it is one room.",
            "A record for every SKU - what it is, where it is, and how many are there.",
            "An inbound record (what arrived) and an outbound record (what left) for every movement.",
            "A working unit of measure for each SKU so counts and orders speak the same language.",
        ],
        "standards": [
            "Inventory terminology follows the APICS Dictionary so that stock states, movements, and records mean the same thing across the industry.",
            "Inventory valuation follows IAS 2 (IFRS) or ASC 330 (US GAAP): the lower of cost and net realisable value.",
            "Warehouse material handling follows OSHA 29 CFR 1910.176 for safe storage and handling practices.",
        ],
        "citations": [CIT_APICS, CIT_IAS2, CIT_ASC330, CIT_OSHA],
        "sig_lens": (
            "The Signature read: inventory is stored promise - every unit on "
            "the shelf a vow the business has made to a customer it has not "
            "met yet. The Signature Stock Method keeps the vow bank honest: "
            "count what is promised, guard it where it sleeps, release it "
            "when it is called, and never let the bank overdraft. The "
            "warehouse is the treasury; the records are the ledger of "
            "promises kept."
        ),
    },
    {
        "key": "sku_atom",
        "name": "The SKU: The Inventory Atom",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The SKU - stock keeping unit - is the atom of inventory data: "
            "the smallest thing the system tracks as a distinct, orderable "
            "item. One SKU is one exact product in one exact form: a 500 ml "
            "bottle of one brand is a different SKU from the 1 liter "
            "bottle, and a blue widget is a different SKU from the red one. "
            "The SKU number is its permanent name in every system, and it "
            "must be unique, stable, and meaningful: unique so two items "
            "never share it, stable so history follows it for years, "
            "meaningful enough that a human can tell at a glance roughly "
            "what it is. Around the SKU gather all the facts the "
            "discipline needs: description, units of measure, dimensions "
            "and weight, shelf life, storage requirements, cost, price, "
            "supplier, lead time, barcode, and the ABC class and reorder "
            "rules the later records compute. Get the SKU model right and "
            "every record downstream - counts, movements, reorder math - "
            "has a clean anchor. Get it wrong, with duplicates and dead "
            "codes and one number for two things, and every report lies a "
            "little."
        ),
        "how_it_works": (
            "A SKU record works as the master key of the inventory system. "
            "When goods arrive, the receiver scans or enters the SKU, and "
            "the system knows exactly what it is, how it is counted, and "
            "where it may go. When a picker picks, the SKU tells the system "
            "what was taken. When finance values the stock, the SKU carries "
            "the cost. The SKU number itself is designed, not accidental: "
            "good designs encode a category prefix, a sequence, and a check "
            "digit so typos get caught; bad designs are free text that "
            "drifts. The record also carries status - active, phase-out, "
            "discontinued - because a SKU is born, lives, and dies, and "
            "dead codes must be retired rather than reused. Aliases map "
            "supplier part numbers and barcodes to the one internal SKU, so "
            "three different labels on three supplier cartons all mean the "
            "same atom. The demo builds a well-formed SKU, validates its "
            "check digit, and maps supplier aliases to the master record."
        ),
        "key_points": [
            "A SKU is one exact item in one exact form - one size, one color, one packaging; change any attribute and you have a new SKU.",
            "The SKU number must be unique, stable, and meaningful: duplicates and reused numbers are the classic source of lying reports.",
            "Every fact the discipline needs hangs on the SKU: description, units, dimensions, cost, supplier, lead time, barcode, and reorder rules.",
            "Supplier aliases and barcodes map many outside names to the one internal SKU number.",
            "A SKU has a lifecycle - active, phase-out, discontinued - and dead codes are retired, never recycled.",
        ],
        "requirements": [
            "A unique SKU number for every distinct item, with a check digit or format rule that catches typos.",
            "A plain-language description and the unit of measure in which the SKU is counted.",
            "Physical facts: dimensions, weight, shelf life, and storage requirements where they matter.",
            "Commercial facts: standard cost, supplier, lead time, and barcode or GTIN.",
            "A status flag and a retirement procedure so dead codes leave the active set.",
        ],
        "standards": [
            "Trade item identification follows GS1 General Specifications: GTIN for the item, SSCC for the shipping unit.",
            "Barcode symbols on products and cartons follow GS1 symbology rules so any scanner reads them.",
            "SKU master data is governed as master data: one owner, one creation process, no shadow numbering.",
        ],
        "citations": [CIT_GS1, CIT_APICS, CIT_SILVER],
        "sig_lens": (
            "The Signature read: the SKU is the stamped note of state - the "
            "smallest sworn statement the system can make. Where public "
            "practice files a product code, the Signature Stock Method "
            "stamps an oath: this number names one thing, and one thing "
            "only, for all time. The atom is the honor of the whole "
            "treasury - corrupt the atom and every sum above it is fiction."
        ),
    },
    {
        "key": "stock_states",
        "name": "Stock States: On Hand, Reserved, and Available to Promise",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "One number is never enough to describe stock. The on-hand "
            "quantity says what physically sits in the warehouse right now. "
            "But some of it may already be promised to customers whose "
            "orders are waiting to ship - that is reserved stock, and it "
            "cannot be promised twice. Subtract the reserved from the "
            "on-hand and you get the available to promise: the quantity the "
            "business may honestly offer to new orders today. There are "
            "more states on the ladder. In-transit is stock bought and "
            "shipped but not yet received. On-order is stock on purchase "
            "orders not yet shipped. Allocated is stock assigned to "
            "production jobs. Quarantine is stock held back for quality "
            "inspection. Damaged is stock that can never ship. Projected "
            "available adds scheduled receipts and subtracts scheduled "
            "issues day by day into the future. A warehouse that confuses "
            "these states oversells, starves production, or counts phantom "
            "stock. The discipline is simple: every unit is always in "
            "exactly one state, every state change is a recorded movement, "
            "and available to promise is computed, never guessed."
        ),
        "how_it_works": (
            "Stock states work as a conserved ledger. Receiving adds to "
            "on-hand and takes from in-transit. Reserving moves units from "
            "available to reserved without touching on-hand - nothing "
            "physical moves, but the promise is now spoken for. Picking "
            "moves reserved units out of on-hand entirely. Adjustments move "
            "units between states when counts disagree with the books. The "
            "fundamental identities are: on-hand minus reserved equals "
            "available to promise; and the sum of all states equals total "
            "inventory position. When an order arrives, the system checks "
            "available to promise, not on-hand - promising from on-hand is "
            "how double-promises happen. When a receipt is scheduled, "
            "projected available rises on that future date, letting sales "
            "promise stock that is not here yet with eyes open. Quarantine "
            "and damaged states keep bad stock out of every promise. The "
            "demo builds a full stock-state ledger for one SKU and "
            "computes available to promise, then processes an order and "
            "shows the states rebalancing."
        ),
        "key_points": [
            "On-hand is physical presence; reserved is promises already made; available to promise is what may honestly be offered to new orders.",
            "Every unit is always in exactly one state, and every state change is a recorded movement - the ledger is conserved.",
            "In-transit and on-order extend the picture into the future; projected available shows what can be promised each coming day.",
            "Quarantine and damaged states keep suspect stock out of every promise and every count of sellable goods.",
            "Promising from on-hand instead of available to promise is the classic double-promise failure.",
        ],
        "requirements": [
            "A defined list of stock states the system recognizes, with rules for every legal transition between them.",
            "A reservation record tying each reserved unit to the order or job that holds it, released on shipment or cancellation.",
            "An available-to-promise calculation refreshed on every reservation, receipt, and adjustment.",
            "Quarantine and damage states with inspection and disposition records before stock re-enters sellable states.",
            "A reconciliation routine that proves the states sum to the physical count.",
        ],
        "standards": [
            "Stock-state definitions follow the APICS Dictionary (on-hand, reserved, available to promise, allocated, projected available).",
            "Inventory is carried on the books in these states consistently with IAS 2 / ASC 330 measurement rules.",
            "State changes are audit-trailed: who moved what, when, from which state to which, and why.",
        ],
        "citations": [CIT_APICS, CIT_SILVER, CIT_IAS2],
        "sig_lens": (
            "The Signature read: stock states are the truth of the shelf - "
            "not what the business hopes is there, but what is there and "
            "what is already spoken for. The Signature Stock Method counts "
            "promises before it counts boxes: a unit that is reserved has "
            "already left the treasury in spirit. Available to promise is "
            "the honest remainder, and honesty about the remainder is the "
            "whole of the discipline."
        ),
    },
    {
        "key": "location_address",
        "name": "The Location Address: Aisles, Bays, and Bins",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A warehouse location is a street address for stock: a "
            "structured name that tells a person or a machine exactly "
            "where to find one SKU. The classic address has levels - "
            "aisle, bay, level, and bin - like A-12-03-B: aisle A, bay 12, "
            "third level, bin B. Every location has a type: forward pick "
            "faces where daily picking happens, bulk reserve where full "
            "pallets wait, quarantine where inspected goods are held, and "
            "staging where outbound shipments are assembled. Fixed "
            "slotting gives each SKU its own permanent home - easy to find, "
            "easy to memorize, wasteful of space. Random or dynamic "
            "slotting puts each pallet wherever space fits when it "
            "arrives - dense and flexible, but totally dependent on the "
            "system knowing where everything is. Zone storage groups "
            "families together - all the fasteners in one zone, all the "
            "flammables in the fire-rated zone. The location record carries "
            "the address, the type, the dimensions and weight capacity, "
            "what is in it now, and what it is allowed to hold. A "
            "warehouse without trusted addresses is a building full of "
            "hiding places."
        ),
        "how_it_works": (
            "Location addressing works as a coordinate system layered on "
            "the building. The address encodes the path: the aisle "
            "chooses the corridor, the bay chooses the rack section, the "
            "level chooses the height, the bin chooses the slot. Warehouse "
            "management software keeps a map of every address with its "
            "type, capacity, and current contents, and directs putaway "
            "and picking as routing problems on that map. When goods "
            "arrive, the system suggests locations that fit the unit's "
            "size, match its storage needs, and keep it near where it "
            "will be picked. When an order needs picking, the system "
            "sorts the picks into a walking sequence so the picker "
            "travels the shortest sensible route. Barcodes or RFID tags "
            "on each location let the picker confirm arrival - scanning "
            "the location and the item closes the loop that prevents "
            "picking the right SKU from the wrong address. The demo "
            "builds a small location map, encodes and decodes addresses, "
            "and validates that a putaway suggestion fits the location "
            "type and capacity."
        ),
        "key_points": [
            "A location address is a structured coordinate - aisle, bay, level, bin - that names exactly one storage slot.",
            "Locations have types: forward pick, bulk reserve, quarantine, staging - and goods go only where the type allows.",
            "Fixed slotting gives every SKU a permanent home (simple, space-hungry); dynamic slotting uses any fitting space (dense, system-dependent).",
            "The system keeps a map of every address with capacity and contents, and routes putaway and picking on that map.",
            "Scanning the location barcode together with the item barcode closes the loop against picking from the wrong address.",
        ],
        "requirements": [
            "A location naming scheme applied to every storage slot, with no two addresses alike and no address unused-and-unknown.",
            "A location master: type, dimensions, weight capacity, allowed products, and current contents for every address.",
            "A putaway rule that suggests a fitting address for every arriving unit.",
            "A pick sequence that orders picks into a sensible travel path.",
            "Location labels - barcode or RFID - on the rack so confirmation scans are possible.",
        ],
        "standards": [
            "Location identification may follow GS1 SSCC/GLN practices for logistics units and locations in automated systems.",
            "Rack storage heights and clearances respect local fire and building codes (sprinklered high-pile rules where they apply).",
            "Aisle widths and pedestrian routes follow OSHA 29 CFR 1910.176 handling and storage rules.",
        ],
        "citations": [CIT_TOMPKINS, CIT_BARTHOLDI, CIT_GS1],
        "sig_lens": (
            "The Signature read: the location is the fixed address in the "
            "system - the sworn home of the stock. The Signature Stock "
            "Method gives every unit a true address and keeps the map "
            "honest, because a treasure whose map lies is already lost. "
            "Fixed or dynamic, the principle is the same: the system must "
            "be able to lay its hand on any unit, any hour, without "
            "searching."
        ),
    },
    {
        "key": "uom_hierarchy",
        "name": "Units of Measure and the Pack Hierarchy",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "One SKU can be counted in several units at once: the "
            "manufacturer ships pallets, the warehouse stores cases, the "
            "customer orders eaches. The unit of measure hierarchy ties "
            "these together with fixed conversion factors: 1 pallet equals "
            "40 cases, 1 case equals 24 eaches, so 1 pallet equals 960 "
            "eaches. The base unit - usually the each, the smallest "
            "sellable unit - is the currency every quantity converts to "
            "before the math happens; the other units are just convenient "
            "packaging for humans and machines. The hierarchy also "
            "carries the physical facts: a case has dimensions and weight, "
            "a pallet has a stacking limit, and the GTIN on the case "
            "barcode differs from the GTIN on the each. Mistakes here are "
            "expensive and classic: ordering 100 when you meant 100 cases "
            "of 24, receiving 40 pallets as 40 eaches, or pricing per case "
            "while costing per each. The discipline keeps one base unit "
            "per SKU, publishes the conversions, and makes the system "
            "convert automatically - humans should name the unit, and the "
            "system should do the arithmetic."
        ),
        "how_it_works": (
            "The unit hierarchy works as a conversion ladder. Every SKU "
            "names its base unit, and every alternate unit carries a "
            "factor: how many base units it contains. Any quantity "
            "enters the system as a number plus a unit, and the system "
            "immediately converts to base units for storage, costing, "
            "and math, converting back only for display and paperwork. "
            "Receiving 40 cases of a 24-each case stores 960 eaches and "
            "prints 960 eaches on the bin label, while the receipt "
            "record remembers it arrived as 40 cases. Picking 2 pallets "
            "of a 40-case pallet releases 80 cases. Rounding rules are "
            "set per unit - you cannot pick half a sealed case if the "
            "SKU ships whole cases only. The GTIN hierarchy mirrors "
            "the pack hierarchy: each packaging level carries its own "
            "barcode so a scanner always knows which level it read. The "
            "demo defines a three-level pack hierarchy, converts "
            "quantities between levels, and shows what happens when a "
            "unit is misread."
        ),
        "key_points": [
            "Every SKU has one base unit - usually the each - and every other unit converts to it by a fixed factor.",
            "Humans name the unit; the system does the arithmetic: convert on entry to base units, convert back only for display.",
            "The pack hierarchy carries physical facts: case dimensions and weight, pallet stacking limits, per-level barcodes.",
            "Unit mistakes are classic and expensive: ordering 100 meaning cases while the system heard eaches.",
            "Rounding rules per unit stop impossible quantities like half a sealed case.",
        ],
        "requirements": [
            "One declared base unit per SKU and a published conversion factor for every alternate unit.",
            "Automatic conversion on every transaction: receipts, picks, adjustments, and orders.",
            "Physical data per pack level: dimensions, weight, stacking limits.",
            "Distinct barcodes (GTINs) per packaging level so scans identify the level.",
            "Rounding and whole-pack rules that forbid fractional sealed units where they are not allowed.",
        ],
        "standards": [
            "Trade-item and packaging-level identification follows GS1 General Specifications (distinct GTIN per level).",
            "Quantities are recorded with their unit stated; conversions are system-computed, never mental math at the dock.",
            "Cost and price are always tied to a named unit - per each, per case, per pallet - on every document.",
        ],
        "citations": [CIT_GS1, CIT_APICS, CIT_SILVER],
        "sig_lens": (
            "The Signature read: the unit is the measure of the oath - the "
            "agreed yardstick by which the treasury counts. The Signature "
            "Stock Method keeps one true measure per SKU and lets every "
            "other measure bow to it, because a promise counted in two "
            "different yards is two different promises. Convert honestly, "
            "name the unit always, and the ledger never lies about size."
        ),
    },
    {
        "key": "valuation_simple",
        "name": "Inventory Valuation Basics: FIFO and LIFO",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "When the same SKU arrives at different prices over time, which "
            "units did you sell and what did they cost? The issuing rule "
            "answers that question. FIFO - first in, first out - says the "
            "oldest units leave first, so cost of goods sold uses the "
            "oldest purchase prices and the stock on the shelf is valued "
            "at the newest prices. LIFO - last in, first out - says the "
            "newest units leave first, so cost of goods sold uses the "
            "newest prices and the shelf carries the old ones. When prices "
            "rise, FIFO shows higher profit (cheap old costs against "
            "current revenue) and a balance sheet close to replacement "
            "cost; LIFO shows lower profit and an aging balance sheet. "
            "Weighted average cost blends all purchases into one moving "
            "average. The choice is not free: tax law and accounting "
            "standards constrain it - IFRS forbids LIFO entirely, while "
            "US GAAP permits it - and once chosen it must be applied "
            "consistently. Physically, the rule should match reality: "
            "perishables must flow FIFO or FEFO by expiry, while a gravel "
            "pile naturally flows LIFO. The money follows the flow, so "
            "the flow must be honest."
        ),
        "how_it_works": (
            "An issuing rule works as a cost layer stack. Each receipt "
            "adds a layer: quantity at its purchase price. Each issue "
            "peels layers off in the rule's order. Under FIFO the peel "
            "starts at the oldest layer; under LIFO it starts at the "
            "newest; under weighted average there are no layers, just one "
            "average cost recomputed at each receipt. Consider three "
            "receipts - 100 units at 10, 100 at 12, 100 at 14 - and a sale "
            "of 150. FIFO costs the sale at 100 times 10 plus 50 times 12, "
            "which is 1,600, and values the remaining 150 at 50 times 12 "
            "plus 100 times 14, which is 2,000. LIFO costs the sale at 100 "
            "times 14 plus 50 times 12, which is 2,000, and values the "
            "remainder at 1,600. Same physical sale, 400 of reported "
            "profit difference. The warehouse system enforces the physical "
            "side - which pallet the forklift takes - while the books "
            "enforce the cost side, and the two must agree. The demo runs "
            "the same receipts and sale through FIFO, LIFO, and weighted "
            "average and prints the three profit and valuation answers."
        ),
        "key_points": [
            "The issuing rule decides which purchase price attaches to each unit sold: FIFO takes the oldest, LIFO the newest, average blends them.",
            "When prices rise, FIFO reports higher profit and a fresher balance sheet; LIFO reports lower profit and an aging one.",
            "The choice is constrained by law and standards: IFRS (IAS 2) forbids LIFO; US GAAP (ASC 330) permits it; consistency is mandatory.",
            "The physical flow should match the cost flow: perishables flow FIFO or by expiry; bulk piles naturally flow LIFO.",
            "The warehouse enforces which units move; the books enforce which costs attach - and the two must agree.",
        ],
        "requirements": [
            "A declared cost-flow assumption per SKU or site, documented and applied consistently period to period.",
            "Receipt layers recording quantity and unit cost for every inbound lot.",
            "Issue transactions that peel layers in the declared order and post the cost to the sale.",
            "A physical issuing discipline that matches the cost rule where product nature demands it.",
            "A tax and audit review of the chosen method before it is adopted.",
        ],
        "standards": [
            "IAS 2 Inventories (IFRS) permits FIFO and weighted average only; LIFO is prohibited.",
            "ASC 330 (US GAAP) permits FIFO, LIFO, and average, with disclosure of the method used.",
            "Cost-flow assumptions are disclosed in the financial statements and applied consistently.",
        ],
        "citations": [CIT_IAS2, CIT_ASC330, CIT_SILVER, CIT_NAHMIAS],
        "sig_lens": (
            "The Signature read: the issuing rule is the order of "
            "departure - which vow leaves the treasury first. The "
            "Signature Stock Method issues the eldest promise first, "
            "because the oldest vow has waited longest and deserves its "
            "turn. Money follows the flow, so the flow is sacred: take "
            "the old stock first, count its true cost, and let the "
            "balance sheet show the shelf as it truly stands."
        ),
    },
    {
        "key": "lead_time",
        "name": "Lead Time: The Clock That Drives Everything",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Lead time is the delay between deciding you need stock and "
            "having it usable on the shelf. It has pieces: the "
            "administrative time to raise and send the order, the "
            "supplier's time to make or pick the goods, the transit time "
            "to move them to you, and your own receiving and inspection "
            "time before the stock is available. Every piece varies - "
            "suppliers run late, trucks break down, ports congest - so "
            "lead time is really a distribution with an average and a "
            "spread, not a single number. Almost every inventory formula "
            "ahead depends on lead time: the reorder point covers demand "
            "during lead time plus safety stock against its variability; "
            "the economic order quantity balances against it; multi-echelon "
            "planning compounds it across tiers. A business that treats "
            "lead time as a fixed promise gets stockouts whenever reality "
            "disagrees. The discipline measures lead time per supplier per "
            "SKU from real history - order date to available date - tracks "
            "the average and the variability, and feeds both into the "
            "math. Shorten the lead time and you can hold less stock for "
            "the same service; that is why lead-time reduction is one of "
            "the highest-leverage projects in operations."
        ),
        "how_it_works": (
            "Lead time works as the exposure window of inventory control. "
            "From the moment you order, you are exposed to demand you "
            "cannot serve from incoming stock until the lead time elapses "
            "and the goods are available. If average daily demand is 20 "
            "units and average lead time is 10 days, you will consume "
            "about 200 units while waiting - so you must order when 200 "
            "plus a safety margin remain. The safety margin covers the "
            "variability: if lead time sometimes stretches to 14 days, "
            "those extra 4 days of demand must be on the shelf too. The "
            "warehouse measures each leg separately so improvement has "
            "a target: cut the supplier leg with better scheduling, the "
            "transit leg with nearer sourcing, the receiving leg with "
            "faster inspection. Supplier scorecards track on-time "
            "delivery against promised dates, and the spread of lateness "
            "feeds the safety-stock formula directly. The demo splits a "
            "lead time into its legs, computes demand during lead time, "
            "and shows how a 4-day stretch changes the stock needed."
        ),
        "key_points": [
            "Lead time is order-to-available time in legs: administrative, supplier, transit, and receiving - each with its own variability.",
            "It is a distribution, not a number: the average sets the base coverage, the spread sets the safety stock.",
            "The reorder point, safety stock, and order quantity formulas all depend on lead time - it is the master clock.",
            "Measure lead time from real history per supplier per SKU, not from the promise on the quote.",
            "Shortening lead time lets you hold less stock for the same service - it is among the highest-leverage improvements.",
        ],
        "requirements": [
            "A lead-time measurement per supplier per SKU: order date to available-on-shelf date, from system history.",
            "The average and the variability (standard deviation) of that history, refreshed regularly.",
            "A split of lead time into legs so each can be attacked separately.",
            "Supplier on-time-delivery scorecards tied to the measured, not promised, lead time.",
            "Every reorder formula fed with the measured lead time, never a wish.",
        ],
        "standards": [
            "Lead-time measurement uses system timestamps (order sent, goods received, stock available) - the same timestamps finance can audit.",
            "Service-level and lateness definitions follow APICS Dictionary usage.",
            "Supplier agreements state lead time as a committed distribution or percentile, not a single-day promise.",
        ],
        "citations": [CIT_SILVER, CIT_NAHMIAS, CIT_APICS, CIT_CHOPRA],
        "sig_lens": (
            "The Signature read: lead time is the wait the treasury "
            "endures between the call and the answer. The Signature Stock "
            "Method measures the wait honestly and stocks the bridge "
            "across it, because a promise that arrives late is a promise "
            "half broken. Shorten the wait and the treasury can run lean "
            "without fear - the swiftest supply needs the smallest guard."
        ),
    },
    {
        "key": "goods_receipt",
        "name": "Goods Receipt: Receiving and Putaway Records",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Goods receipt is the moment outside stock becomes your "
            "stock: the dock door where the truck's promise meets your "
            "count. The receiving record captures what the purchase order "
            "said should arrive, what actually arrived, when, in what "
            "condition, and who checked it. Variances are the heart of "
            "the record: short shipments, over shipments, damaged "
            "cartons, wrong items, and late arrivals each get their own "
            "disposition - accept, reject, hold for credit, or quarantine "
            "for inspection. Blind receiving, where the checker sees the "
            "order quantities, invites rubber-stamping; many warehouses "
            "hide the expected count so the check is real. After receipt "
            "comes putaway: each unit is directed to a storage location, "
            "and the putaway record ties the SKU, quantity, lot, and "
            "destination address together. Until putaway is confirmed, "
            "received stock sits in a staging state - visible to the "
            "system but not yet pickable. Receipt without records is how "
            "warehouses fill with mystery stock; receipt with records is "
            "how the books stay true to the shelves."
        ),
        "how_it_works": (
            "Receiving works as a three-way match: purchase order, "
            "delivery note, and physical count must agree within "
            "tolerance. The receiver identifies the inbound shipment, "
            "pulls up its expected lines, counts and inspects each "
            "line, and records the actuals. A tolerance rule decides "
            "the small variances - a 2 percent short on a bulk line "
            "may be accepted with a note, while any variance on a "
            "high-value serialized line is rejected. Damaged goods "
            "are photographed, segregated, and moved to a damage or "
            "quarantine state, never into sellable stock. Accepted "
            "goods are labeled with the SKU, quantity, lot, and a "
            "license-plate barcode for the pallet or carton, then the "
            "system directs putaway: the location is suggested by the "
            "putaway rule, and the operator confirms arrival with a "
            "scan. The demo runs a receipt with three variance cases - "
            "short, over, damaged - applies tolerance rules, and "
            "prints the resulting putaway tasks."
        ),
        "key_points": [
            "Receiving is a three-way match: purchase order, delivery note, and physical count must agree within tolerance.",
            "Every variance gets a disposition: accept, reject, hold for credit, or quarantine - never silent acceptance.",
            "Damaged goods are segregated and photographed, never mixed into sellable stock.",
            "Putaway is a separate recorded step: SKU, quantity, lot, and destination address tied together and scan-confirmed.",
            "Stock is not pickable until putaway is confirmed; staging holds it honestly in between.",
        ],
        "requirements": [
            "A receiving record per shipment line: expected, actual, condition, timestamp, and checker.",
            "Published tolerance rules per SKU class deciding which variances auto-accept and which escalate.",
            "A quarantine and damage process with inspection records and disposition decisions.",
            "License-plate labeling of received pallets and cartons with SKU, quantity, and lot.",
            "A putaway task per accepted unit with system-suggested, scan-confirmed destination.",
        ],
        "standards": [
            "Receiving inspection follows the sampling logic of the quality plan; critical defects trigger full inspection.",
            "Damaged-goods handling follows the carrier claims process and the site safety rules.",
            "Putaway into rack storage respects load ratings and the fire-code clearances of the location type.",
        ],
        "citations": [CIT_BARTHOLDI, CIT_TOMPKINS, CIT_APICS],
        "sig_lens": (
            "The Signature read: receiving is the gate of the treasury - "
            "the sworn inspection where outside goods become the "
            "system's own. The Signature Stock Method counts at the "
            "gate with open eyes and no trust on credit: what the truck "
            "says and what the hand counts must agree before the oath "
            "is accepted. Mystery stock at the gate becomes mystery "
            "shortage at the shelf; the gate keeps the ledger clean."
        ),
    },
    {
        "key": "pick_pack_ship",
        "name": "The Pick-Pack-Ship Flow",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Pick-pack-ship is the outbound heartbeat: turn a customer "
            "order into boxes on a truck. Picking is the labor heart of "
            "the warehouse - often half or more of its operating cost - "
            "because it is travel: walking the aisles to collect each "
            "line of the order. The pick record says which order, which "
            "SKU, how many, from which location, and the picker confirms "
            "each with a scan so the wrong item in the right quantity "
            "never starts its journey. Packing turns picked goods into "
            "shippable parcels: the right carton, protective material, "
            "the packing slip, and a final verification scan that the "
            "carton contents match the order. Shipping closes the loop: "
            "the carton is weighed, labeled with the carrier label, "
            "manifested onto the load, and the stock leaves the books. "
            "Every step has a failure mode the records exist to catch: "
            "mis-picks caught by scan confirmation, short picks caught "
            "at pack verification, wrong addresses caught at manifest. "
            "The discipline is unforgiving arithmetic - the customer "
            "receives exactly what was ordered, or the record says why "
            "not - and it is where the warehouse's promise-keeping is "
            "measured most directly."
        ),
        "how_it_works": (
            "The flow works as a staged pipeline with a check at every "
            "handoff. Order release waves a set of orders to the floor. "
            "Pick tasks direct operators along a travel sequence; each "
            "pick is confirmed by scanning the location and the item, "
            "and the system compares the scan to the task - a mismatch "
            "stops the picker before the error travels. Picked goods "
            "move to pack stations, where the operator scans each item "
            "into the carton; the pack screen shows the order lines "
            "filling up, and it will not close the carton while a line "
            "is short. The carton is weighed against its expected "
            "weight band - a classic cheap catch for missing or extra "
            "items. Shipping prints the carrier label, assigns the "
            "carton to a load, and posts the issue transaction that "
            "removes the stock from the books and books the cost of "
            "goods sold. The demo releases a three-line order, confirms "
            "picks with scans, verifies the pack by weight band, and "
            "manifests the shipment."
        ),
        "key_points": [
            "Picking is the cost heart of the warehouse - mostly travel - and scan confirmation at each pick stops errors before they travel.",
            "Pack verification matches carton contents to the order line by line, with a weight-band check as a cheap second net.",
            "Shipping manifests the carton onto a load and posts the issue: stock leaves the books and cost of goods sold is booked.",
            "Every handoff has its check: pick scan, pack scan, weight band, manifest - the pipeline catches what each stage misses.",
            "The customer receives exactly what was ordered, or the record says why not - that is the promise measured here.",
        ],
        "requirements": [
            "Order release that waves pickable orders to the floor in a controlled flow.",
            "Pick tasks with location sequence, item, and quantity, confirmed by location-plus-item scans.",
            "Pack stations that verify contents against the order and weigh each carton against its band.",
            "Carrier labels, load assignment, and a manifest record per shipment.",
            "Issue transactions that remove shipped stock from the books at the correct cost.",
        ],
        "standards": [
            "Carrier labeling and manifests follow the carrier's shipping-system rules and the GS1 SSCC for logistics units.",
            "Pack stations follow ergonomic and safety practice for repetitive handling work.",
            "Proof of shipment and delivery records are retained per the site's commercial and tax policy.",
        ],
        "citations": [CIT_BARTHOLDI, CIT_TOMPKINS, CIT_GS1],
        "sig_lens": (
            "The Signature read: pick-pack-ship is the departure of the "
            "vow - the moment the treasury hands the promise to the "
            "customer. The Signature Stock Method treats every order as "
            "a sacred delivery: the picker walks the map, the packer "
            "seals the oath, the shipper witnesses it leave. A wrong "
            "item shipped is a broken vow; the checks at every handoff "
            "are the honor guard of the promise."
        ),
    },
    {
        "key": "expiry_lot_basics",
        "name": "Lots, Batches, and Expiry: The Basics",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "A lot - or batch - is one production run's worth of a "
            "product: every unit made together under the same conditions "
            "at the same time. The lot number ties units to their "
            "origin: which raw materials went in, which machines and "
            "operators made them, and which quality tests they passed. "
            "For anything perishable - food, medicine, chemicals, "
            "cosmetics - each lot also carries an expiry date, after "
            "which the product may not be sold or used. The warehouse "
            "tracks stock by lot, not just by SKU: the same SKU can "
            "have three lots on the shelf with three different expiry "
            "dates, and the issuing rule must pick the right one. "
            "Expiry management is calendar work the system does "
            "relentlessly: days-until-expiry computed for every lot, "
            "alerts as dates approach, blocked picks of expired stock, "
            "and disposition records for what must be destroyed or "
            "returned. Traceability is the lot's deeper purpose: when a "
            "defect is found, the lot number reaches forward to every "
            "customer who received it and backward to every ingredient "
            "that made it. Without lot discipline, a recall is a guess; "
            "with it, a recall is a list."
        ),
        "how_it_works": (
            "Lot tracking works as a second dimension of the stock "
            "ledger: every quantity is recorded as SKU plus lot plus "
            "expiry. Receiving creates the lot record from the "
            "supplier's lot number and certificate, stamps the "
            "expiry from the product master or the supplier document, "
            "and labels the physical units. Every movement - putaway, "
            "pick, transfer, adjustment - names the lot, so the "
            "system always knows which lots sit where. A nightly job "
            "recomputes days-until-expiry; lots inside the alert "
            "window appear on the expiry watch list, and lots past "
            "expiry are automatically blocked from picking and "
            "moved to a hold state for disposition. When a quality "
            "issue hits a lot, the genealogy runs both ways: forward "
            "to shipments and customers, backward to component lots "
            "and suppliers. The demo builds three lots of one SKU "
            "with different expiries, computes days remaining, blocks "
            "the expired lot, and traces one lot forward to its "
            "shipments."
        ),
        "key_points": [
            "A lot is one production run: same time, same conditions, one number tying units to their origin and tests.",
            "Stock is tracked as SKU plus lot plus expiry - the same SKU can hold several lots with different dates.",
            "The system recomputes days-until-expiry relentlessly, alerts on approaching dates, and blocks expired picks automatically.",
            "Traceability runs both ways from the lot: forward to customers and shipments, backward to ingredients and suppliers.",
            "Without lot discipline a recall is a guess; with it, a recall is a list.",
        ],
        "requirements": [
            "A lot record created at receiving: supplier lot number, quantity, expiry, and certificates.",
            "Lot identity carried on every movement: putaway, pick, transfer, and adjustment.",
            "A nightly expiry computation with alert windows and automatic pick-blocking at expiry.",
            "Disposition records for expired or recalled stock: destroy, return, or rework - with witnesses.",
            "Forward and backward traceability from any lot within the time the regulations demand.",
        ],
        "standards": [
            "Food traceability follows the applicable food-safety rules of the market (lot-level one-up-one-down traceability at minimum).",
            "Pharmaceutical lots follow good distribution practice for the market, with full chain traceability.",
            "Expiry dates are printed and barcoded in GS1 application-identifier format where GS1 labeling is used.",
        ],
        "citations": [CIT_GS1, CIT_APICS, CIT_SILVER],
        "sig_lens": (
            "The Signature read: the lot is the family of the stock - "
            "units born together, sharing one fate. The Signature Stock "
            "Method honors the family: it knows each lot's birthday and "
            "its last day, never sells the dead, and can name every "
            "child of a troubled birth. Expiry is the natural law of "
            "perishables; the method bows to it and plans around it."
        ),
    },
    {
        "key": "cycle_counting",
        "name": "Cycle Counting: Counting Without Stopping",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A full wall-to-wall physical inventory shuts the warehouse "
            "down; cycle counting counts a little every day and never "
            "stops the operation. The method is simple: count a scheduled "
            "slice of SKUs or locations each day, compare to the books, "
            "investigate the differences, and correct them. Done "
            "relentlessly, the whole warehouse is counted several times "
            "a year - the important SKUs far more often - and accuracy "
            "stays high because errors are found days after they happen, "
            "not months. The schedule is usually ABC-driven: A items "
            "counted monthly or weekly, B items quarterly, C items "
            "once or twice a year. There are flavors: control-group "
            "counting, where one small representative set is counted "
            "daily to measure the process itself; location-based, where "
            "whole aisles are swept; and exception-based, where counts "
            "are triggered by events like a zero on-hand with open "
            "orders. The count is blind - the counter does not see the "
            "book quantity first - so the count is evidence, not "
            "confirmation. Cycle counting is not just counting; the "
            "investigation of each variance finds the broken process "
            "that created it, and fixing the process is the real prize."
        ),
        "how_it_works": (
            "A cycle-count program works as a daily drumbeat. Each "
            "morning the system generates the day's count tasks from "
            "the schedule: which SKUs or locations, prioritized by "
            "ABC class and by triggers like recent variances or "
            "zero-stock anomalies. The counter goes to the location, "
            "counts blind, and enters the quantity. The system compares "
            "to the book: matches close the task silently, and "
            "variances open an investigation. Small variances may "
            "recount once and adjust; large or repeated variances "
            "escalate to a root-cause review - was it a mis-pick, a "
            "unit-of-measure error, a receipt posted to the wrong "
            "lot, a location label fallen off? The adjustment posts "
            "with a reason code, so the history shows not just what "
            "changed but why. Metrics close the loop: count accuracy "
            "by ABC class, variances per hundred counts, and repeat "
            "variance rate. The demo builds an ABC-driven yearly "
            "schedule, runs a day of blind counts against a small "
            "warehouse, and investigates the variances it finds."
        ),
        "key_points": [
            "Cycle counting counts a scheduled slice every day instead of shutting down for a wall-to-wall count - accuracy stays high because errors are found in days, not months.",
            "The schedule is ABC-driven: A items counted often, C items rarely, plus event triggers like zero-stock anomalies.",
            "Counts are blind: the counter never sees the book quantity first, so the count is evidence, not confirmation.",
            "Every variance is investigated with a reason code - the broken process behind the variance is the real find.",
            "Metrics close the loop: accuracy by ABC class, variances per hundred counts, repeat-variance rate.",
        ],
        "requirements": [
            "A published count schedule by ABC class covering every SKU at least once a year, A items far more often.",
            "Daily blind count tasks generated by the system, with recount and escalation rules for variances.",
            "Reason-coded adjustments so the history explains why each correction happened.",
            "Root-cause review for large or repeated variances, with process fixes tracked to closure.",
            "Accuracy metrics by class reported regularly, with targets the operation is held to.",
        ],
        "standards": [
            "Count procedures follow the site's inventory-accuracy policy, aligned with the financial audit requirements for stock.",
            "Blind-count discipline: book quantities are hidden from counters until the count is entered.",
            "Adjustments above the materiality threshold require a second approval before posting.",
        ],
        "citations": [CIT_SILVER, CIT_NAHMIAS, CIT_APICS, CIT_BARTHOLDI],
        "sig_lens": (
            "The Signature read: cycle counting is the daily inspection "
            "of the treasury - the sworn habit of verifying the vow "
            "bank a little every day. The Signature Stock Method never "
            "lets the ledger drift far from the shelf, because drift "
            "compounds and lies grow comfortable. Count blind, question "
            "every variance, fix the process that made it - that is how "
            "a treasury stays honest for decades."
        ),
    },
    {
        "key": "abc_analysis",
        "name": "ABC Analysis: Ranking Stock by Value and Motion",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Not all SKUs deserve equal attention. ABC analysis ranks "
            "every SKU by annual usage value - yearly demand times unit "
            "cost - and splits the ranking into classes: A items are "
            "the vital few, roughly 10 to 20 percent of SKUs carrying "
            "70 to 80 percent of the value; B items are the middle "
            "third; C items are the trivial many, half or more of the "
            "SKUs carrying a few percent of the value. The classes "
            "drive different policies: A items get tight control, "
            "frequent counts, careful forecasting, and low safety "
            "stock relative to their scrutiny; C items get simple "
            "rules, big order quantities, and infrequent counts - "
            "because counting a two-dollar SKU weekly costs more than "
            "the SKU. The analysis extends naturally: ABC by pick "
            "frequency drives slotting, ABC by margin drives service "
            "levels, and XYZ analysis classifies by demand variability "
            "to sit beside ABC's value view. The ranking is "
            "recomputed regularly because demand moves - today's C "
            "can be next quarter's A. ABC is the discipline of "
            "proportion: spend control effort where the money is, and "
            "spend simplicity where it is not."
        ),
        "how_it_works": (
            "ABC analysis works as a sorted cumulative curve. For "
            "each SKU, compute annual usage value: annual demand in "
            "base units times standard unit cost. Sort descending, "
            "walk down the list accumulating value, and cut the "
            "classes at the chosen value thresholds - commonly 80 "
            "percent of value for A, the next 15 for B, the last 5 "
            "for C. The class then sets policy: cycle-count "
            "frequency, forecast method effort, safety-stock "
            "service level, and order-quantity review cadence. A "
            "SKU that is A by value but C by pick frequency teaches "
            "a useful lesson - the two rankings answer different "
            "questions, and slotting listens to motion while "
            "control listens to money. Reclassification runs on a "
            "schedule, typically quarterly, with hysteresis rules "
            "so borderline SKUs do not flip classes every month. "
            "The demo ranks twelve SKUs by annual usage value, cuts "
            "the ABC classes, and assigns each class its control "
            "policy."
        ),
        "key_points": [
            "ABC ranks SKUs by annual usage value: A is the vital few carrying most of the value, C is the trivial many carrying little.",
            "The class sets the policy: tight control and frequent counts for A, simple rules and big quantities for C.",
            "Different rankings answer different questions: ABC by value drives control, ABC by pick frequency drives slotting, XYZ by variability drives safety stock.",
            "Recompute on a schedule - demand moves, and today's C can be next quarter's A - with hysteresis against class-flipping.",
            "ABC is the discipline of proportion: control effort follows the money; simplicity covers the rest.",
        ],
        "requirements": [
            "Annual demand and standard cost per SKU so annual usage value can be computed honestly.",
            "Published class thresholds (commonly 80/15/5 of value) applied the same way every cycle.",
            "A policy table per class: count frequency, forecast effort, service level, review cadence.",
            "A quarterly reclassification run with hysteresis rules for borderline SKUs.",
            "Separate motion-based ranking for slotting decisions, kept beside the value ranking.",
        ],
        "standards": [
            "Annual usage value uses standard cost and a full twelve months of demand history (or forecast where history is thin).",
            "Class definitions and policy tables are documented in the inventory-control procedure.",
            "Reclassification is system-run and audit-trailed, not spreadsheet folklore.",
        ],
        "citations": [CIT_SILVER, CIT_NAHMIAS, CIT_APICS, CIT_CHOPRA],
        "sig_lens": (
            "The Signature read: ABC is the order of honor in the "
            "treasury - the vital few guarded closely, the many "
            "trusted to simple rules. The Signature Stock Method gives "
            "its attention where the value sleeps and its simplicity "
            "where the pennies rest, because guarding everything "
            "equally guards nothing well. Know which vows are heavy "
            "and watch them; let the light ones walk on plain rules."
        ),
    },
    {
        "key": "reorder_point",
        "name": "Reorder Point Math",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The reorder point is the stock level that triggers a new "
            "order: when available inventory falls to this number, buy "
            "more now or run out during the lead time. The classic "
            "formula is disarmingly simple: reorder point equals "
            "average demand during average lead time, plus safety "
            "stock. If you sell 20 units a day and replenishment takes "
            "10 days, you will sell about 200 while waiting - so order "
            "when 200 plus your safety buffer remain. The safety stock "
            "covers the variability of demand and lead time; the base "
            "200 covers the averages. The formula assumes demand and "
            "lead time are reasonably stable and independent - good "
            "enough for thousands of SKUs, dangerous for the wild "
            "ones. Reorder points are living numbers: demand shifts, "
            "lead times stretch, and the point must be recomputed on "
            "a schedule, not carved in stone. The system watches "
            "inventory position - on-hand plus on-order minus "
            "backorders - and fires the order the moment it touches "
            "the point. Set it too high and cash sleeps on the shelf; "
            "set it too low and customers meet empty shelves. The "
            "math exists to set it just right."
        ),
        "how_it_works": (
            "The reorder point works as a tripwire on the inventory "
            "position. Each day - or each transaction - the system "
            "computes position: on-hand plus scheduled receipts minus "
            "reservations and backorders. When position falls to or "
            "below the reorder point R, the system raises an order for "
            "the order quantity Q. The point itself is R = d * L + "
            "SS, where d is average demand per day, L is average lead "
            "time in days, and SS is the safety stock. The product d "
            "* L is the expected consumption during the wait; SS is "
            "the buffer against the wait being longer or hungrier "
            "than expected. Continuous review - checking after every "
            "transaction - fires orders the moment the tripwire is "
            "touched; periodic review checks once per cycle and must "
            "cover the review period too. The demo computes R for a "
            "SKU from measured demand and lead time, then simulates "
            "daily demand and fires the order exactly when position "
            "crosses the point."
        ),
        "key_points": [
            "Reorder point R = average demand during average lead time + safety stock: order when inventory position touches R.",
            "The base term covers the expected wait; the safety stock covers the wait being longer or hungrier than expected.",
            "The tripwire watches inventory position - on-hand plus on-order minus commitments - not on-hand alone.",
            "Continuous review fires after every transaction; periodic review must also cover the review interval.",
            "Reorder points are living numbers: recompute on a schedule as demand and lead times move.",
        ],
        "requirements": [
            "Measured average daily demand per SKU from real history or forecast.",
            "Measured average lead time per supplier per SKU, with its variability.",
            "A computed safety stock matched to the target service level.",
            "Continuous position monitoring that raises the order the moment the tripwire is touched.",
            "A recomputation schedule so the points track moving demand and lead times.",
        ],
        "standards": [
            "Demand and lead-time inputs come from system history, refreshed on the planning cycle.",
            "The reorder-point formula and its inputs are documented per SKU in the planning parameters.",
            "Order triggering is system-automated with planner review, not dependent on memory.",
        ],
        "citations": [CIT_WILSON, CIT_SILVER, CIT_NAHMIAS, CIT_APICS],
        "sig_lens": (
            "The Signature read: the reorder point is the watchman's "
            "cry - the exact shelf level at which the treasury calls "
            "for reinforcement. The Signature Stock Method sets the "
            "cry by honest measurement, not by fear: cover the "
            "expected march of demand, hold a guard for the uncertain "
            "days, and call at the true moment. Too early and gold "
            "sleeps; too late and the gate stands empty."
        ),
    },
    {
        "key": "eoq",
        "name": "The Economic Order Quantity",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Every order costs two opposing things. Ordering costs - "
            "the paperwork, the receiving labor, the freight, the "
            "setup - punish small frequent orders. Holding costs - "
            "capital tied up, space, insurance, risk - punish large "
            "infrequent ones. The economic order quantity, EOQ, is the "
            "order size where the two punishments balance: Q = "
            "sqrt(2DS/H), where D is annual demand, S is the cost of "
            "placing one order, and H is the annual holding cost of "
            "one unit. Order the EOQ and total cost - ordering plus "
            "holding - is at its minimum for the model's "
            "assumptions: steady demand, fixed order cost, and holding "
            "cost proportional to inventory. The model, born in a 1913 "
            "factory magazine article, is the most famous formula in "
            "inventory theory - and the most misapplied. Real life adds "
            "quantity discounts, perishability, truckload rounding, "
            "and lumpy demand, and each bends the answer. The wise use "
            "of EOQ is as a starting point and a sanity check: compute "
            "it, then adjust for the real constraints, and never let "
            "the formula overrule a pallet that will not fit through "
            "the door."
        ),
        "how_it_works": (
            "EOQ works by minimizing the sum of two cost curves. Annual "
            "ordering cost is (D/Q) * S: more, smaller orders cost more "
            "to place. Annual holding cost is (Q/2) * H: average "
            "inventory is half the order quantity, each unit costing H "
            "per year to hold. Add the curves and the total is a "
            "U-shape; calculus puts the bottom at Q = sqrt(2DS/H). "
            "Take D = 10,000 units a year, S = 50 per order, H = 2 per "
            "unit per year: EOQ = sqrt(2 * 10000 * 50 / 2) = sqrt(500000) "
            "which is about 707 units, ordered about 14 times a year. "
            "The total cost curve is flat near the bottom - being 20 "
            "percent off the EOQ costs only about 2 percent extra - "
            "which is why rounding to truckloads and pack sizes is "
            "harmless. Quantity discounts shift the answer: compare "
            "total cost at the EOQ against total cost at each discount "
            "break and take the cheapest honest total. The demo "
            "computes EOQ for a SKU, shows the flat-bottomed total "
            "cost curve, and tests a discount break."
        ),
        "key_points": [
            "EOQ = sqrt(2DS/H) balances ordering cost against holding cost at the minimum total cost.",
            "The total cost curve is flat near the bottom: rounding to truckloads and pack sizes costs almost nothing.",
            "The model assumes steady demand, fixed order cost, and proportional holding cost - real constraints bend the answer.",
            "Quantity discounts are tested by comparing honest total cost at the EOQ against each price break.",
            "Use EOQ as a starting point and sanity check, then adjust for pallets, perishability, and lumpy demand.",
        ],
        "requirements": [
            "Annual demand D per SKU from history or forecast, in base units.",
            "A measured order cost S: the true cost of placing and receiving one order.",
            "A holding-cost rate H per unit per year, including capital, space, and risk.",
            "A discount-break comparison wherever suppliers offer tiered pricing.",
            "Practical rounding to pack sizes, pallet quantities, and truckloads.",
        ],
        "standards": [
            "Holding cost includes the cost of capital, warehousing, insurance, and obsolescence risk - commonly 20 to 30 percent of unit value per year.",
            "Order cost is measured from the site's own process, not copied from a textbook.",
            "EOQ parameters are reviewed on the planning cycle as demand and costs move.",
        ],
        "citations": [CIT_HARRIS, CIT_SILVER, CIT_NAHMIAS, CIT_APICS],
        "sig_lens": (
            "The Signature read: the economic order quantity is the "
            "measured stride of the treasury - neither the nervous "
            "shuffle of tiny orders nor the lumbering march of "
            "mountains. The Signature Stock Method walks the middle "
            "path the numbers mark: count the true cost of ordering, "
            "count the true cost of holding, and step where the two "
            "balance. The stride is a guide, not a chain - the door "
            "and the pallet have their vote too."
        ),
    },
    {
        "key": "safety_stock",
        "name": "Safety Stock Math",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Safety stock is the buffer between the plan and the "
            "world: extra units held so that when demand runs hot or "
            "the supplier runs late, the shelf still serves. The "
            "classic formula is safety stock = z * sigma * sqrt(L), "
            "where sigma is the standard deviation of demand per "
            "period, L is the lead time in periods, and z is the "
            "service factor from the normal distribution for the "
            "target service level - 1.65 for 95 percent, 2.33 for 99 "
            "percent. The square root is the key insight: variability "
            "grows with the square root of time, so doubling the lead "
            "time only multiplies the needed buffer by about 1.4. "
            "Service level is a business choice with a price: each "
            "extra nine of service costs disproportionately more "
            "stock, so 99 percent service can cost far more than 95. "
            "The formula assumes demand is roughly normal and "
            "independent period to period - check the assumption for "
            "lumpy, seasonal, or promotional demand, where the "
            "textbook buffer misleads. Safety stock is insurance: "
            "priced by statistics, bought with shelf space, and "
            "claimed whenever reality beats the forecast."
        ),
        "how_it_works": (
            "Safety stock works as a statistical cushion sized by two "
            "inputs: how much demand varies, and how sure you want to "
            "be. Measure daily demand's standard deviation sigma from "
            "history. Choose the service level - the fraction of "
            "replenishment cycles that must not stock out - and read "
            "z: 1.28 for 90 percent, 1.65 for 95, 2.05 for 98, 2.33 "
            "for 99. Multiply: SS = z * sigma_d * sqrt(L). With sigma "
            "of 8 units a day, lead time 9 days, and 95 percent "
            "service: SS = 1.65 * 8 * 3 = 39.6, about 40 units. Lead "
            "time variability gets its own term when suppliers are "
            "unreliable: the full form combines demand variance over "
            "average lead time with average demand squared times lead "
            "time variance. The buffer then joins the reorder point: "
            "R = d*L + SS. Recompute as demand patterns move, and "
            "watch the fill rate - the fraction of demand actually "
            "served from stock - because cycle service and fill rate "
            "are different promises. The demo computes safety stock "
            "at three service levels and prices each in units and "
            "dollars."
        ),
        "key_points": [
            "Safety stock = z * sigma * sqrt(L): variability times the service factor times the square root of lead time.",
            "Service level is a priced choice: 95 percent is 1.65 sigma, 99 percent is 2.33 - each extra nine costs disproportionately more.",
            "Variability grows with the square root of time: doubling lead time multiplies the buffer by only about 1.4.",
            "Unreliable suppliers add a lead-time-variance term to the formula - measure lateness, not just averages.",
            "Safety stock joins the reorder point as R = d*L + SS, and is recomputed as demand patterns move.",
        ],
        "requirements": [
            "Measured demand variability (standard deviation) per SKU from real history.",
            "A chosen service level per ABC class, priced and approved as a business decision.",
            "Lead-time variability measured per supplier, added to the formula where it matters.",
            "A recomputation schedule tied to the demand-review cycle.",
            "Fill-rate monitoring to verify the promised service is actually delivered.",
        ],
        "standards": [
            "Service-level definitions (cycle service vs fill rate) follow APICS Dictionary usage.",
            "Statistical inputs come from system history with outliers reviewed, not blindly included.",
            "Safety-stock parameters are documented per SKU and approved at the level the inventory policy names.",
        ],
        "citations": [CIT_SILVER, CIT_NAHMIAS, CIT_GROSS, CIT_APICS],
        "sig_lens": (
            "The Signature read: safety stock is the honor margin of "
            "the treasury - the guard held back so the vow never "
            "breaks on a bad day. The Signature Stock Method sizes "
            "the guard by honest measurement of the world's "
            "unruliness, not by fear and not by hope. A guard too "
            "small abandons the promise; a guard too large starves "
            "the treasury of its gold. Measure, price the nines, and "
            "hold the line."
        ),
    },
    {
        "key": "fefo",
        "name": "FEFO: Issuing by Expiry",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "FEFO - first expired, first out - is the issuing rule for "
            "anything with a date on it: pick the lot with the nearest "
            "expiry first, regardless of when it arrived. A late "
            "delivery of short-dated product must jump the queue ahead "
            "of older, longer-dated stock, or it will die on the "
            "shelf. FEFO generalizes FIFO: when lots arrive in expiry "
            "order the two agree, and when they do not, FEFO is the "
            "one that saves product. The warehouse enforces it "
            "physically and systematically: flow racks that present "
            "the oldest dates first, pick tasks that name the lot to "
            "take, and system blocks that refuse picks from the wrong "
            "lot. Exceptions exist and are managed openly: a customer "
            "contract demanding minimum remaining shelf life may "
            "require skipping the nearest-expiry lot for a fresher "
            "one - a documented override, not a quiet cheat. The "
            "discipline also watches the horizon: lots approaching "
            "expiry are flagged for markdown, donation, or return "
            "before they become waste. FEFO is FIFO with a conscience "
            "about time: the product's clock, not the receiving "
            "clock, decides who leaves first."
        ),
        "how_it_works": (
            "FEFO works as an expiry-sorted pick queue. Every lot "
            "carries its expiry date; the pick engine sorts candidate "
            "lots by expiry ascending and consumes the nearest-expiry "
            "lot first, moving to the next only when the first is "
            "exhausted. The pick task names the exact lot and "
            "location, and the scan confirmation enforces it - "
            "picking a different lot is a variance, not a shortcut. "
            "Minimum-remaining-life rules sit on top: if the order "
            "or the customer requires 60 days of life remaining, "
            "lots below the threshold are skipped with the override "
            "logged. A watch list ranks lots by days remaining; "
            "planners work the list top-down with markdowns, "
            "transfers to faster-moving sites, or returns to the "
            "supplier. Expired lots are blocked from every pick and "
            "moved to hold for disposition. The demo stocks three "
            "lots with scrambled arrival and expiry order, runs a "
            "FEFO pick, and shows FIFO picking the wrong lot for "
            "comparison."
        ),
        "key_points": [
            "FEFO picks the nearest-expiry lot first, regardless of arrival order - the product's clock decides.",
            "When lots arrive in expiry order, FEFO and FIFO agree; when they do not, FEFO is the one that prevents waste.",
            "Pick tasks name the exact lot and scans enforce it; picking another lot is a variance.",
            "Minimum-remaining-life rules for demanding customers are documented overrides, never quiet cheats.",
            "An expiry watch list worked top-down - markdown, transfer, return - keeps waste from happening by surprise.",
        ],
        "requirements": [
            "Expiry dates captured at receiving for every lot of every dated SKU.",
            "A pick engine that sorts by expiry and names the lot on every pick task.",
            "Scan enforcement of the named lot at the pick face.",
            "Documented minimum-life rules per customer or channel with logged overrides.",
            "A watch list by days-remaining with assigned dispositions before expiry.",
        ],
        "standards": [
            "Expiry capture and labeling follow GS1 application-identifier date formats where GS1 labeling is used.",
            "Dated-product handling follows the food, pharma, or chemical regulations of the market.",
            "Expired-stock disposition is witnessed and recorded per the site's quality procedure.",
        ],
        "citations": [CIT_GS1, CIT_SILVER, CIT_APICS],
        "sig_lens": (
            "The Signature read: FEFO is the law of the dying - the "
            "nearest end goes first, whatever the order of arrival. "
            "The Signature Stock Method bows to the natural law of "
            "perishables: it sends the eldest-dated vow out first and "
            "never lets good product die of neglect. Waste is the "
            "treasury's shame; the watch list is its conscience."
        ),
    },
    {
        "key": "reservation_logic",
        "name": "Reservations and Allocation Logic",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A reservation is a promise pinned to specific stock: this "
            "order owns these 50 units, and no other order may take "
            "them. Allocation is the rulebook for deciding which orders "
            "get pinned when stock is short: priority customers first, "
            "oldest orders first, biggest margin first - the business "
            "chooses, but it must choose openly and apply the rule "
            "every time. Soft reservations earmark quantity against "
            "expected receipts; hard reservations pin actual on-hand "
            "units, sometimes down to the lot and location. The logic "
            "matters most in shortage: without allocation rules, the "
            "loudest salesperson wins and the strategic customer "
            "waits. Reservations have a lifecycle - created at order "
            "entry or release, adjusted as quantities change, consumed "
            "by picking, released on cancellation or shipment - and "
            "stale reservations are a classic disease: dead orders "
            "holding live stock hostage. The discipline sweeps for "
            "them, expires reservations on a policy, and reports "
            "reserved-but-unshipped aging like an unpaid bill. "
            "Allocation also faces fairness questions the system "
            "should answer with data: partial shipments or all-or-"
            "nothing, and who gets told what, when. Promise only what "
            "the reservation backs, and back every promise with a "
            "reservation."
        ),
        "how_it_works": (
            "Reservation logic works as a claim registry on available "
            "stock. When an order is promised, the system checks "
            "available to promise; if the quantity is there, it "
            "creates a reservation record tying order, SKU, quantity, "
            "and optionally lot and location. The reserved quantity "
            "leaves available to promise immediately, so the next "
            "order sees the honest remainder. When stock is short, "
            "the allocation rule ranks the competing orders - by "
            "customer priority class, then order age is the common "
            "pattern - and reserves top-down until stock runs out; "
            "the rest wait or split per policy. Picking consumes "
            "reservations line by line; cancellation or shipment "
            "releases them. A nightly sweep flags reservations older "
            "than the policy threshold and reservations against "
            "cancelled orders, releasing the stale ones after "
            "review. The demo takes three orders against short "
            "stock, applies priority-then-age allocation, and shows "
            "the claim registry before and after a cancellation."
        ),
        "key_points": [
            "A reservation pins a promise to specific stock; allocation is the open rulebook for who gets pinned when stock is short.",
            "Soft reservations earmark expected receipts; hard reservations pin actual on-hand units down to lot and location.",
            "Without allocation rules the loudest voice wins shortages; with them, priority then age decides - openly and every time.",
            "Reservations have a lifecycle: created, adjusted, consumed by picking, released on shipment or cancellation.",
            "Stale reservations are a classic disease: sweep for dead orders holding live stock and expire them on policy.",
        ],
        "requirements": [
            "A reservation record per claim: order, SKU, quantity, lot/location where hard, timestamp.",
            "A published allocation rule for shortages, applied automatically and identically every time.",
            "Immediate deduction from available to promise on every reservation and release.",
            "A stale-reservation sweep with aging reports and a release policy.",
            "Partial-shipment and all-or-nothing policies decided in advance, not at the crisis.",
        ],
        "standards": [
            "Reservation and allocation rules are documented in the order-promising procedure and visible to sales.",
            "Promise dates given to customers derive from reserved or projected stock, never from hope.",
            "Reservation changes are audit-trailed with the order change that caused them.",
        ],
        "citations": [CIT_APICS, CIT_SILVER, CIT_CHOPRA],
        "sig_lens": (
            "The Signature read: a reservation is a spoken vow with a "
            "name on it - this stock belongs to this customer until "
            "the promise is kept or honorably released. The Signature "
            "Stock Method pins every promise to real units and rations "
            "shortage by open rank, never by noise. Stale vows are "
            "released so the living may be served; the registry is "
            "the honor roll of the treasury."
        ),
    },
    {
        "key": "putaway_strategies",
        "name": "Putaway Strategies",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Putaway is the decision of where each arriving unit sleeps, "
            "and the strategy shapes the warehouse's whole travel map. "
            "Fixed putaway returns every SKU to its permanent home - "
            "simple to learn, simple to audit, and wasteful whenever "
            "the home stands half empty. Dynamic putaway places each "
            "unit in any fitting empty location - dense and flexible, "
            "but the system must remember everything because no human "
            "can. Zone putaway restricts SKUs to their family zones - "
            "fasteners with fasteners, flammables in the fire-rated "
            "zone - trading some density for findability and safety. "
            "Forward-fill putaway tops up the pick faces from bulk "
            "reserve, keeping the fast movers at arm's reach. The "
            "strategy also answers the cube question: heavy low, light "
            "high, fast near the dock, slow in the back. Good putaway "
            "rules consider the unit's size against the location's "
            "capacity, its velocity against the zone map, its "
            "hazards against the restrictions, and its lot against "
            "the neighbors - because mixing lots in one bin is how "
            "FEFO dies. Putaway done well makes picking cheap; "
            "putaway done lazily - everything in the nearest empty "
            "hole - makes every future pick expensive."
        ),
        "how_it_works": (
            "A putaway strategy works as a scored search over open "
            "locations. When goods are received and labeled, the "
            "system filters locations by fit: capacity and dimensions "
            "for the unit, allowed product families, hazard "
            "compatibility, and temperature or security needs. The "
            "survivors are scored: proximity to the SKU's pick face, "
            "proximity to the dock for fast movers, consolidation "
            "with the same lot already stored, and travel distance "
            "from receiving. The top scorer wins and becomes the "
            "putaway task; the operator confirms with a location "
            "scan. Forward-fill runs as a separate wave: when a pick "
            "face falls below its trigger, the system tasks a "
            "replenishment move from bulk to forward. Exceptions - "
            "no fitting location, oversized units, quarantine holds - "
            "route to staging with a reason, never to a random hole. "
            "The demo scores five open locations for an arriving "
            "pallet under zone-plus-velocity rules and tasks the "
            "winner."
        ),
        "key_points": [
            "Fixed, dynamic, zone, and forward-fill putaway trade simplicity, density, findability, and pick-face readiness against each other.",
            "The system filters open locations by fit - size, family, hazard, temperature - then scores the survivors by travel and consolidation.",
            "Heavy low, light high, fast near the dock, slow in the back: the cube and velocity rules of good placement.",
            "Mixing lots in one bin kills FEFO; the putaway rule keeps lots separable where dates matter.",
            "Lazy putaway - nearest empty hole - taxes every future pick; disciplined putaway pays for itself in travel saved.",
        ],
        "requirements": [
            "A declared putaway strategy per zone with its scoring rules written down.",
            "A location master with capacity, allowed families, and restrictions current and trusted.",
            "System-suggested destinations on every putaway task, scan-confirmed at arrival.",
            "A forward-fill trigger per pick face with replenishment tasks from bulk.",
            "An exception path to staging with reasons, never silent random placement.",
        ],
        "standards": [
            "Hazardous or regulated goods are stored per their material safety and local fire-code requirements.",
            "Rack load ratings are respected in every putaway suggestion the system makes.",
            "Putaway confirmations are timestamped and tied to the operator for traceability.",
        ],
        "citations": [CIT_BARTHOLDI, CIT_TOMPKINS, CIT_APICS],
        "sig_lens": (
            "The Signature read: putaway is the settling of the "
            "treasury - each new arrival given its rightful chamber. "
            "The Signature Stock Method seats every unit where it "
            "belongs by size, speed, and nature, because a treasury "
            "that shelves at random is a maze, and a maze loses "
            "things. Heavy low, swift near the door, kin with kin - "
            "order at the settling saves a hundred searches later."
        ),
    },
    {
        "key": "picking_strategies",
        "name": "Picking Strategies: Wave, Zone, Batch, Discrete",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Picking is how orders become collections of goods, and "
            "the strategy decides how pickers spend their walking. "
            "Discrete picking is one picker, one order, start to "
            "finish - simple and traceable, but the picker walks "
            "the whole warehouse for every small order. Batch "
            "picking lets one picker collect the same SKU for many "
            "orders in one pass - brilliant when many orders share "
            "few SKUs, but it needs a sort afterward. Zone picking "
            "divides the warehouse into territories: each picker "
            "owns a zone, orders flow zone to zone on conveyors or "
            "carts, and nobody walks the whole building - at the "
            "cost of coordination. Wave picking releases groups of "
            "orders together on a schedule tuned to the shipping "
            "departures, so the day's trucks leave full and on "
            "time. The choice depends on the order profile: few "
            "lines per order favors batching, many lines favors "
            "discrete or zone, tight ship windows favor waves. "
            "Most real warehouses blend them - zones for the "
            "building, batches within the fast zone, waves for the "
            "carriers. The strategy is reviewed as the order mix "
            "changes, because the profile that chose it will not "
            "last forever."
        ),
        "how_it_works": (
            "A picking strategy works by grouping the day's order "
            "lines into efficient tours. The system takes released "
            "orders and clusters them: by zone for zone picking, by "
            "shared SKUs for batch picking, by ship window for wave "
            "picking. Each cluster becomes pick tasks sequenced for "
            "short travel - typically a serpentine path through the "
            "aisles that visits every needed location once. The "
            "picker follows the task list on a handheld or voice "
            "system, confirming each pick by scanning location and "
            "item. In zone picking, totes travel between zones and "
            "each zone adds its lines; in batch picking, the picker "
            "sorts at a pack station or into a put wall afterward. "
            "Waves are timed backward from carrier pickup: the wave "
            "plan says which orders must be picked by when, and "
            "the floor is staffed to the plan. The demo builds ten "
            "orders, clusters them three ways - discrete, batch, "
            "and zone - and compares the total travel distance of "
            "each."
        ),
        "key_points": [
            "Discrete is one picker per order (simple, much walking); batch groups shared SKUs across orders (less walking, needs sorting).",
            "Zone picking gives each picker a territory and flows orders between zones - nobody walks the whole building.",
            "Wave picking releases order groups on a schedule tuned to carrier departures so trucks leave full and on time.",
            "The order profile chooses the strategy: lines per order, shared SKUs, and ship windows decide.",
            "Real warehouses blend strategies and re-review them as the order mix changes.",
        ],
        "requirements": [
            "An order profile analysis - lines per order, SKU overlap, ship windows - before choosing the strategy.",
            "Released orders clustered by the strategy into sequenced pick tasks.",
            "Travel-sequenced task lists with scan confirmation at every pick.",
            "Sort capacity - put walls or pack stations - wherever batching is used.",
            "Wave plans timed backward from carrier pickups, staffed to the plan.",
        ],
        "standards": [
            "Pick accuracy is measured per strategy (mis-picks per thousand lines) and targeted explicitly.",
            "Voice and handheld picking systems follow the site's ergonomic and safety practice.",
            "Wave cut-off times are published to sales so promise times match floor reality.",
        ],
        "citations": [CIT_BARTHOLDI, CIT_TOMPKINS, CIT_APICS],
        "sig_lens": (
            "The Signature read: picking is the gathering of the "
            "vow - walking the map to collect what was promised. The "
            "Signature Stock Method walks wisely: it groups the "
            "gathering so no step is wasted and no order waits on a "
            "wandering picker. The strategy is the marching order of "
            "the treasury - discrete, batched, zoned, or waved - and "
            "the wise commander matches the march to the battle."
        ),
    },
    {
        "key": "packing_records",
        "name": "Packing Records and Shipment Integrity",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Packing is where the warehouse's accuracy becomes the "
            "customer's experience: the right items, protected, in "
            "the right box, with the right papers. The packing "
            "record ties the order to its cartons: which lines went "
            "into which carton, the carton's weight and dimensions, "
            "its tracking number, and who packed it. Cartonization - "
            "choosing the box - balances protection against freight: "
            "too big a box wastes dimensional-weight money and lets "
            "goods rattle; too small crushes them. Verification is "
            "the discipline's spine: scan each item into the carton "
            "against the order, weigh the sealed carton against its "
            "expected band, and count the cartons against the "
            "manifest. Hazardous, fragile, and temperature-sensitive "
            "goods get their labeled packaging and documentation as "
            "the regulations demand, not as an afterthought. A "
            "shipment with integrity is one the warehouse could "
            "defend line by line: every carton accounted for, every "
            "line verified, every exception documented. When the "
            "customer opens the box, the packing record is the "
            "silent witness that it left right."
        ),
        "how_it_works": (
            "Packing works as a verified assembly line per order. "
            "The pack station screen shows the order's lines; the "
            "operator scans each item as it enters the carton, and "
            "the line fills on screen - the station refuses to close "
            "a carton with lines still open or items unscanned. "
            "Carton selection is system-suggested from the items' "
            "dimensions and fragility, and the operator confirms or "
            "overrides with a reason. Void fill and protection go in "
            "per the packaging standard for the goods class. The "
            "sealed carton is weighed: if the weight falls outside "
            "the expected band for its contents, the carton is "
            "reopened and rechecked - the cheapest mis-pack detector "
            "ever built. Labels print with the carrier tracking "
            "number and the SSCC for the logistics unit; the carton "
            "joins the manifest for its load. The demo packs a "
            "three-line order, catches a short line at verification, "
            "and flags an overweight carton at the weight check."
        ),
        "key_points": [
            "The packing record ties the order to its cartons: lines per carton, weight, dimensions, tracking number, packer.",
            "Scan-into-carton verification refuses to close a carton with open lines - the spine of packing discipline.",
            "The weight band on the sealed carton is the cheapest mis-pack detector in the warehouse.",
            "Cartonization balances protection against dimensional-weight freight: right box, right fill, right papers.",
            "Hazardous, fragile, and temperature-sensitive goods get their regulated packaging as a requirement, not an afterthought.",
        ],
        "requirements": [
            "Pack stations that display order lines and verify each scanned item into the carton.",
            "System-suggested carton sizes from item dimensions, with override reasons logged.",
            "A weight band per carton checked automatically before the label prints.",
            "Carrier labels and SSCCs printed per carton, tied to the load manifest.",
            "Packaging standards per goods class: protection, labeling, and documentation.",
        ],
        "standards": [
            "Logistics-unit identification follows GS1 SSCC practice on every carton.",
            "Dangerous-goods packaging and documentation follow the applicable transport regulations of the mode.",
            "Weight-band tolerances are set from measured pack data, not guessed.",
        ],
        "citations": [CIT_GS1, CIT_BARTHOLDI, CIT_TOMPKINS],
        "sig_lens": (
            "The Signature read: packing is the sealing of the vow - "
            "the treasury's promise wrapped, weighed, and witnessed. "
            "The Signature Stock Method seals nothing unverified: "
            "every line scanned, every carton weighed, every box "
            "fit for its journey. What leaves the gate in honor "
            "arrives in honor; the packing record is the seal's "
            "testimony."
        ),
    },
    {
        "key": "movement_records",
        "name": "Movement Records: Transfers, Adjustments, and Audits",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Not every stock change is a receipt or a shipment. "
            "Transfers move stock between locations, zones, or sites - "
            "forward-fill from bulk to pick face, balancing between "
            "warehouses, quarantine to sellable after inspection. "
            "Adjustments correct the books when the count disagrees "
            "with reality: found stock, lost stock, damaged write-offs, "
            "unit-of-measure corrections. Each adjustment needs a "
            "reason code, because an adjustment without a reason is a "
            "confession without a story. Reclassifications change a "
            "unit's state - sellable to quarantine, quarantine to "
            "sellable, sellable to scrap - without moving it. The "
            "movement record is the same shape every time: what, how "
            "many, from where to where, from which state to which, "
            "when, who, and why. The audit trail is the sum of these "
            "records: given any unit, the trail shows every state it "
            "ever occupied; given any discrepancy, the trail shows "
            "every hand that touched it. Warehouses that treat "
            "adjustments as casual corrections breed casual "
            "inaccuracy; warehouses that investigate every "
            "adjustment breed accuracy."
        ),
        "how_it_works": (
            "Movement records work as double-entry postings on the "
            "stock ledger. A transfer posts a minus at the source "
            "location and a plus at the destination in one atomic "
            "transaction - the two legs never separate, so stock "
            "cannot vanish between them. An adjustment posts a plus "
            "or minus against the location with a reason code and, "
            "above the materiality threshold, a second approval. "
            "A reclassification posts a minus in the old state and a "
            "plus in the new state at the same location. The ledger "
            "is conserved: the sum of all locations and states for "
            "a SKU always equals its total, and any posting that "
            "would break conservation is rejected. Cycle counts, "
            "receiving, picking, and shipping all post through the "
            "same movement engine, so the audit trail is complete "
            "by construction. Investigators query the trail by SKU, "
            "by location, by operator, or by reason code. The demo "
            "runs a forward-fill transfer, a damage adjustment with "
            "reason code, and a quarantine release, then proves "
            "the ledger still balances."
        ),
        "key_points": [
            "Transfers, adjustments, and reclassifications are all postings on one conserved stock ledger.",
            "Every posting is atomic: source minus and destination plus in one transaction, so stock never vanishes between legs.",
            "Adjustments carry reason codes and need second approval above the materiality threshold.",
            "The ledger is conserved: all locations and states always sum to the SKU total, and breakers are rejected.",
            "The audit trail answers two questions: where has this unit been, and whose hands touched this discrepancy.",
        ],
        "requirements": [
            "One movement engine that all transactions post through: receipts, picks, transfers, adjustments.",
            "Reason codes on every adjustment, with second approval above the threshold.",
            "Atomic postings: both legs of every movement in one transaction.",
            "A conservation check that rejects any posting breaking the SKU total.",
            "Trail queries by SKU, location, operator, and reason code for investigators.",
        ],
        "standards": [
            "Adjustment thresholds and approval levels are set in the inventory-control policy and enforced by the system.",
            "Movement records are retained per the financial audit and tax requirements of the jurisdiction.",
            "Segregation of duties: the person counting is not the person approving the adjustment.",
        ],
        "citations": [CIT_APICS, CIT_SILVER, CIT_IAS2],
        "sig_lens": (
            "The Signature read: every movement is a witnessed "
            "passage - the treasury's log of where each unit has "
            "walked. The Signature Stock Method writes every step "
            "in the book with its reason, because unwritten steps "
            "are where stock goes to disappear. The ledger is "
            "sacred and conserved; the trail is the memory of the "
            "treasury, and a treasury that remembers cannot be robbed "
            "by confusion."
        ),
    },
    {
        "key": "layout_slotting",
        "name": "Warehouse Layout and Slotting Basics",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Warehouse layout is the floor plan of the operation: "
            "where receiving, storage, picking, packing, and shipping "
            "live, and how goods flow between them. The classic "
            "shapes are flow-through - receiving at one end, shipping "
            "at the other, goods moving one way - and U-flow, where "
            "both docks share one wall and the building wraps around. "
            "Slotting is the finer art inside the plan: which SKU "
            "sleeps in which location. The golden rules are simple: "
            "fast movers near the dock and at waist height, slow "
            "movers far and high, heavy low, families together, and "
            "hazards segregated. Slotting by velocity - the ABC of "
            "pick frequency - puts the most-visited SKUs on the "
            "shortest travel paths, which is where picking labor, "
            "the biggest cost, is won or lost. The layout also "
            "reserves the unglamorous space: staging for inbound and "
            "outbound, quarantine for inspection, returns processing, "
            "battery charging, offices. A good layout is drawn around "
            "the flow of goods, not around the building's columns; "
            "the building is the constraint, the flow is the design. "
            "Re-slot on a schedule, because velocity changes and "
            "yesterday's perfect slot is today's long walk."
        ),
        "how_it_works": (
            "Layout and slotting work as a travel-minimization "
            "problem. The designer maps the building: dock doors, "
            "aisles, rack rows, pick faces, pack stations, with "
            "distances between every pair that matters. SKUs are "
            "ranked by pick velocity, and the fastest are assigned "
            "to the locations with the shortest round trips from "
            "the pack stations - the golden zone at waist-to-shoulder "
            "height near the dock end of the aisles. Families are "
            "kept adjacent so multi-line orders pick compactly; "
            "hazards and temperature-controlled goods take their "
            "mandated zones regardless of velocity. The test of a "
            "layout is simulated picks: run a representative week of "
            "orders through the slot map and total the travel "
            "distance, then try the alternative arrangement. "
            "Re-slotting moves SKUs between locations as velocity "
            "ranks change, scheduled in quiet hours with full "
            "system-directed moves. The demo maps a small "
            "warehouse, slots ten SKUs by velocity, and compares "
            "total pick travel against an unslotted arrangement."
        ),
        "key_points": [
            "Layout places the functions - receiving, storage, picking, packing, shipping - around the flow of goods, not the building's columns.",
            "Slotting assigns SKUs to locations by velocity: fast movers near the dock at waist height, slow movers far and high.",
            "Families pick adjacently, hazards sit in their mandated zones, heavy goods stay low.",
            "The test of a layout is simulated picks: run a real order week through the slot map and total the travel.",
            "Re-slot on a schedule - velocity changes, and yesterday's perfect slot becomes today's long walk.",
        ],
        "requirements": [
            "A measured building map with distances between docks, aisles, pick faces, and pack stations.",
            "Pick-velocity ranking per SKU from real order history.",
            "A slot plan assigning every active SKU, honoring family, hazard, and ergonomic rules.",
            "A travel simulation comparing the plan against alternatives before moves are made.",
            "A re-slotting schedule with system-directed moves in quiet hours.",
        ],
        "standards": [
            "Rack and storage design follows the fire and building codes for the occupancy and commodity class.",
            "Ergonomic practice keeps the fastest picks in the golden zone and respects manual-handling limits.",
            "Pedestrian and equipment routes are separated per OSHA 29 CFR 1910.176 practice.",
        ],
        "citations": [CIT_TOMPKINS, CIT_BARTHOLDI, CIT_OSHA],
        "sig_lens": (
            "The Signature read: layout is the architecture of the "
            "treasury and slotting the seating of its court - the "
            "swiftest vows nearest the gate, the heavy low, the kin "
            "together. The Signature Stock Method seats every SKU "
            "by its worth and its speed, because a court seated "
            "wisely serves swiftly. Draw the plan around the flow "
            "of promises, and the walking - the treasury's dearest "
            "expense - falls away."
        ),
    },
    {
        "key": "multi_echelon",
        "name": "Multi-Echelon Inventory",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "One warehouse is simple; a network is where the real "
            "money hides. Multi-echelon inventory manages stock across "
            "tiers: central distribution centers feeding regional "
            "warehouses feeding stores or customers. Each tier holds "
            "stock for its own demand plus the demand of the tiers "
            "below it, and the classic mistake is managing each "
            "location alone - every site carrying full safety stock "
            "against its own variability, the network drowning in "
            "buffer. The key concept is echelon stock: a location's "
            "own inventory plus everything downstream of it. Planned "
            "on echelon position, the network holds safety stock "
            "where variability pools - usually upstream, where one "
            "buffer can cover many downstream sites through risk "
            "pooling. The square-root law captures the intuition: "
            "consolidating n identical locations into one cuts the "
            "safety stock by roughly the square root of n. Network "
            "design then trades the inventory savings of "
            "centralization against the transport cost and service "
            "time of distance. Transshipments - lateral moves between "
            "same-tier sites - are the network's pressure valve when "
            "one site stocks out and its neighbor overflows. The "
            "discipline thinks in networks, not buildings: where "
            "should each unit of buffer live so the whole system "
            "serves at the lowest total cost."
        ),
        "how_it_works": (
            "Multi-echelon planning works on echelon inventory "
            "position: at each site, on-hand plus on-order plus all "
            "downstream inventory, minus backorders. Reorder logic "
            "runs per echelon with echelon lead times - the time to "
            "move stock from the upstream echelon - rather than "
            "supplier lead times. Safety stock is sized on the "
            "pooled variability: downstream demand variations that "
            "are independent partially cancel, so the upstream "
            "buffer grows slower than the sum of local buffers. "
            "Take four regional sites each needing 100 units of "
            "safety stock alone: pooled at one central site, the "
            "need falls toward 100 times sqrt(4), about 200, not "
            "400 - the square-root law in action. Allocation "
            "rules then ration upstream stock among downstream "
            "sites in shortage, and transshipment rules let sites "
            "rebalance laterally within cost limits. The demo "
            "builds a two-echelon network, sizes safety stock "
            "per-site versus pooled, and shows the savings of the "
            "echelon view."
        ),
        "key_points": [
            "Echelon stock is a site's own inventory plus everything downstream - planning on echelon position prevents buffer duplication.",
            "Risk pooling: independent downstream variations partially cancel, so upstream safety stock grows slower than the sum of local buffers.",
            "The square-root law: consolidating n identical sites cuts safety stock by roughly sqrt(n).",
            "Network design trades inventory savings of centralization against transport cost and service time.",
            "Transshipments between same-tier sites are the network's pressure valve in local shortages.",
        ],
        "requirements": [
            "A network map: tiers, sites, lanes, lead times, and which sites each site serves.",
            "Echelon inventory positions computed per site per SKU from system data.",
            "Pooled safety-stock sizing on echelon demand variability, not per-site silos.",
            "Allocation rules for rationing upstream stock among downstream sites in shortage.",
            "Transshipment rules with cost limits for lateral rebalancing.",
        ],
        "standards": [
            "Network inventory parameters follow the same APICS terminology as single-site planning, extended to echelons.",
            "Inter-site transfers are recorded as movements with the same audit discipline as receipts and shipments.",
            "Service-level promises account for the echelon lead time the customer actually experiences.",
        ],
        "citations": [CIT_CHOPRA, CIT_SILVER, CIT_NAHMIAS, CIT_APICS],
        "sig_lens": (
            "The Signature read: the network is the treasury with "
            "many vaults - and the Signature Stock Method guards the "
            "whole, not each door separately. Buffer pooled upstream "
            "covers many vaults at once; buffer scattered at every "
            "door is gold sleeping in a dozen beds. Think in "
            "echelons: where should each unit of guard live so the "
            "entire realm serves at the least cost."
        ),
    },
    {
        "key": "mrp_logic",
        "name": "MRP: Materials Requirements Planning",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Reorder points work for independent demand - customers "
            "buying finished goods. MRP - materials requirements "
            "planning - works for dependent demand: the components "
            "needed to build those goods, where demand for parts is "
            "computed from the production plan, not forecasted. The "
            "engine takes the master production schedule (what "
            "finished goods, when), explodes it through the bill of "
            "materials (what components each needs), and nets "
            "against inventory (what is already on hand or on "
            "order) to produce planned orders timed by lead time. "
            "The logic is time-phased: gross requirements land on "
            "the dates production needs them, scheduled receipts "
            "cover what is coming, and net requirements become "
            "planned order releases offset backward by the lead "
            "time. MRP's famous weakness is nervousness: small "
            "schedule changes ripple into flurries of rescheduled "
            "orders, so real systems freeze near-term plans and "
            "dampen the churn. Its famous strength is coordination: "
            "thousands of components arriving in the right "
            "quantities on the right days for the build. MRP does "
            "not replace the reorder point - it precedes it, turning "
            "the production plan into the component demand the "
            "reorder math then serves."
        ),
        "how_it_works": (
            "MRP works as a backward-scheduled netting calculation "
            "per component. Start with gross requirements by week "
            "from the exploded master schedule. Subtract scheduled "
            "receipts (open purchase and production orders arriving "
            "in each week) and the on-hand balance carried forward. "
            "The remainder is net requirements - what must be "
            "ordered. Planned order receipts cover the net "
            "requirements, and planned order releases are offset "
            "earlier by the component's lead time: need 500 in week "
            "6 with a 2-week lead time, release the order in week 4. "
            "Lot-sizing rules shape the releases: lot-for-lot "
            "orders exactly the net need, fixed quantities round to "
            "the EOQ or pack size, period-order-quantity covers whole "
            "weeks. Pegging traces every planned order back to the "
            "parent demand that created it, so a schedule change can "
            "be explained. The demo explodes a two-level bill of "
            "materials, nets against on-hand and scheduled "
            "receipts, and releases lead-time-offset planned orders."
        ),
        "key_points": [
            "MRP serves dependent demand: component needs computed from the production plan through the bill of materials, not forecasted.",
            "The logic nets: gross requirements minus scheduled receipts minus on-hand equals net requirements, released backward by lead time.",
            "Time-phasing puts every requirement and receipt on its week; lot-sizing rules shape the planned releases.",
            "Pegging traces each planned order to the parent demand that created it - explanations survive schedule changes.",
            "MRP's weakness is nervousness: freeze near-term plans and dampen churn, or small changes ripple into order flurries.",
        ],
        "requirements": [
            "A master production schedule with quantities by date for finished goods.",
            "An accurate bill of materials per product, maintained as engineering changes land.",
            "Current on-hand balances, scheduled receipts, and lead times per component.",
            "Lot-sizing rules per component: lot-for-lot, fixed quantity, or period coverage.",
            "A frozen near-term horizon and change-dampening rules against nervousness.",
        ],
        "standards": [
            "MRP terminology and time-bucket conventions follow APICS Dictionary usage.",
            "Bills of materials are engineering-controlled documents with revision history.",
            "Planned orders are planner-reviewed before release; the system proposes, the planner disposes.",
        ],
        "citations": [CIT_SILVER, CIT_NAHMIAS, CIT_APICS, CIT_CHOPRA],
        "sig_lens": (
            "The Signature read: MRP is the muster of the treasury - "
            "the production plan calling every component to its post "
            "on its day. The Signature Stock Method musters by "
            "lineage: each planned order knows the parent demand "
            "that summoned it, each release is timed by the true "
            "march of the lead time. Muster steadily and freeze the "
            "near ranks - a nervous muster scatters the host."
        ),
    },
    {
        "key": "inventory_accuracy",
        "name": "Inventory Accuracy: Causes and Cures",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Inventory accuracy is the fraction of records that match "
            "reality - and it is the foundation every formula stands "
            "on. A reorder point computed from a wrong on-hand is a "
            "precise way to be wrong; an MRP exploded from phantom "
            "stock builds phantom plans. Accuracy is measured two "
            "ways: count accuracy (records matching within tolerance) "
            "and dollar accuracy (value matching), because a "
            "warehouse can be 98 percent right by count and badly "
            "wrong by dollars if the misses are the expensive SKUs. "
            "The causes are a familiar rogue's gallery: mis-picks "
            "and mis-puts, unit-of-measure confusion, receipts "
            "posted to the wrong lot, unrecorded damage and "
            "shrinkage, location labels fallen or faded, and "
            "transactions posted late or twice. The cures are "
            "process, not heroics: scan confirmation at every "
            "handoff, blind cycle counts on an ABC schedule, "
            "reason-coded adjustments with investigation, location "
            "audits, and transaction discipline - post it when it "
            "happens, where it happens. World-class operations hold "
            "95 percent-plus count accuracy on A items; below 90, "
            "the planning system is decoration. Accuracy is not a "
            "project with an end date. It is a vital sign, taken "
            "daily, treated immediately."
        ),
        "how_it_works": (
            "Accuracy work runs as a measurement-and-cure loop. "
            "Measure: cycle counts and control groups produce "
            "accuracy by ABC class, variance dollars, and repeat-"
            "variance rates. Diagnose: each variance is traced "
            "through the movement trail to its cause - the trail "
            "shows the mis-posted receipt, the unconfirmed pick, "
            "the double-posted transfer. Cure: fix the process "
            "that created the cause - relabel the faded location, "
            "retrain the unit-of-measure step, add the scan that "
            "was skipped - and verify the cure with targeted "
            "recounts. The Pareto of causes gets the attention: "
            "typically a handful of failure modes create most "
            "variances, and killing the top two moves the metric "
            "more than a hundred spot corrections. Dollar "
            "accuracy gets its own watch because finance values "
            "the balance sheet on these numbers. The demo "
            "measures accuracy across a counted sample, traces "
            "three variances to their causes through the trail, "
            "and prices the fixes against the variance dollars."
        ),
        "key_points": [
            "Accuracy is the foundation every formula stands on: wrong on-hand makes precise reorder points precisely wrong.",
            "Measure two ways: count accuracy (records matching) and dollar accuracy (value matching) - the misses may be the expensive SKUs.",
            "The causes are a rogue's gallery: mis-picks, UOM confusion, wrong-lot receipts, unrecorded damage, faded labels, late postings.",
            "Cure the process, not the variance: trace each cause through the movement trail and fix the step that created it.",
            "The Pareto of causes rules: a handful of failure modes create most variances - kill the top two first.",
        ],
        "requirements": [
            "Accuracy metrics by ABC class: count accuracy, dollar accuracy, variance rates, reported on a cadence.",
            "Variance investigation through the movement trail to a named cause for every significant miss.",
            "Process fixes tracked to closure with verification recounts.",
            "Scan confirmation and blind counts as the standing prevention, not one-time projects.",
            "A published accuracy target per class that planning is allowed to assume.",
        ],
        "standards": [
            "Accuracy measurement methods are consistent period to period so trends are real.",
            "Financial reporting on inventory values follows IAS 2 / ASC 330 on the corrected balances.",
            "Segregation of duties between counting, investigating, and approving adjustments.",
        ],
        "citations": [CIT_SILVER, CIT_NAHMIAS, CIT_APICS, CIT_IAS2],
        "sig_lens": (
            "The Signature read: accuracy is the honesty of the "
            "treasury - the daily proof that the ledger and the "
            "shelf tell one story. The Signature Stock Method "
            "treats every variance as a wound to be healed at its "
            "source, not bandaged at the count. Measure daily, "
            "trace ruthlessly, cure the process - for a treasury "
            "that lies to itself cannot keep a single promise."
        ),
    },
    {
        "key": "perpetual_periodic",
        "name": "Perpetual and Periodic Inventory Systems",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A perpetual system updates the books on every "
            "transaction: each receipt adds, each pick subtracts, "
            "and the system always claims to know the balance. A "
            "periodic system updates on a schedule: the books rest "
            "between counts, and the true balance is known only "
            "when someone counts. Perpetual is the modern "
            "standard wherever transactions are system-recorded - "
            "it enables reorder points, available-to-promise, and "
            "daily accuracy work - but it is only as true as its "
            "transaction discipline; unrecorded moves make the "
            "perpetual balance a confident fiction. Periodic "
            "survives where transactions are impractical to record "
            "- small shops, bulk commodities - and where the "
            "cost of the system exceeds the cost of occasional "
            "surprise. The two also drive different review "
            "rhythms: perpetual pairs naturally with continuous "
            "review (order when the tripwire is touched), while "
            "periodic pairs with periodic review (order up to the "
            "target each cycle). Many operations run a hybrid: "
            "perpetual for the A items that fund the business, "
            "periodic for the C items where simplicity wins. The "
            "choice is economic: perpetual costs discipline and "
            "systems; periodic costs surprise. Know which you are "
            "paying."
        ),
        "how_it_works": (
            "A perpetual system works as a live ledger: every "
            "movement posts immediately, the balance is always "
            "current, and cycle counts verify it in slices. "
            "Shrinkage and error appear as variances to "
            "investigate, and the books are trued by "
            "reason-coded adjustments. A periodic system works "
            "as a reset: between counts the books hold the last "
            "known balance, issues are estimated or simply "
            "unknown, and the physical count re-establishes "
            "truth - with cost of goods sold computed as "
            "beginning inventory plus purchases minus ending "
            "inventory. The drift between the two is "
            "instructive: simulate a month of unrecorded "
            "shrinkage under perpetual-with-lazy-posting and "
            "watch the balance climb away from reality, then "
            "watch the periodic count snap it back with one "
            "large adjustment. The lesson is that perpetual "
            "without discipline is periodic with delusions. "
            "The demo runs both systems over thirty days of "
            "transactions with realistic error rates and "
            "compares the month-end truth each one reports."
        ),
        "key_points": [
            "Perpetual updates on every transaction and always claims a balance; periodic updates on schedule and knows truth only at the count.",
            "Perpetual enables reorder points, ATP, and daily accuracy work - but only with transaction discipline.",
            "Periodic survives where recording every move costs more than the occasional surprise.",
            "Perpetual pairs with continuous review; periodic pairs with order-up-to periodic review.",
            "Perpetual without discipline is periodic with delusions: unrecorded moves make a confident fiction.",
        ],
        "requirements": [
            "A declared system per SKU class: perpetual or periodic, chosen economically and documented.",
            "For perpetual: every movement posted when and where it happens, with scan confirmation.",
            "For periodic: a count schedule the business can actually keep, and COGS computed from the resets.",
            "Cycle counts or control counts verifying perpetual balances on rotation.",
            "A drift watch: variance trends that reveal when perpetual discipline is slipping.",
        ],
        "standards": [
            "The inventory system choice and its review rhythm are documented in the inventory-control policy.",
            "Cost of goods sold under either system reconciles to the financial records per IAS 2 / ASC 330.",
            "Physical counts follow consistent procedures so period comparisons are valid.",
        ],
        "citations": [CIT_APICS, CIT_SILVER, CIT_IAS2, CIT_ASC330],
        "sig_lens": (
            "The Signature read: perpetual is the treasury that "
            "writes every step; periodic the treasury that "
            "remembers in seasons. The Signature Stock Method "
            "writes every step for the vows that matter and counts "
            "the seasons honestly for the rest - but it never "
            "pretends a neglected ledger is a living one. Know "
            "which treasury you keep, pay its price, and take its "
            "truth on its own terms."
        ),
    },
    {
        "key": "advanced_slotting",
        "name": "Advanced Slotting: Cube, Velocity, and the Golden Zone",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Basic slotting puts fast movers near the dock. Advanced "
            "slotting optimizes the warehouse as a three-dimensional "
            "travel problem. The cube-per-order index - COI - ranks "
            "each SKU by its storage cube divided by its order "
            "frequency: the smallest COI (tiny, often-ordered) earns "
            "the closest slots, the largest COI (bulky, rarely "
            "ordered) goes deep. The golden zone - roughly knee to "
            "shoulder height - holds the fastest picks because "
            "bending and reaching cost time and backs; the math of "
            "ergonomics joins the math of travel. Correlated "
            "slotting places SKUs that appear together on orders "
            "side by side, so multi-line picks walk compact loops "
            "instead of zigzagging the building. Forward-reserve "
            "configuration splits each fast SKU between a small "
            "forward pick face and bulk reserve, with the face size "
            "tuned to the replenishment economics. Congestion "
            "modeling keeps the most popular SKUs from sharing one "
            "aisle at one time - the fastest slot in the building "
            "is worthless if three pickers queue for it. Re-slotting "
            "is scheduled, simulated before moves, and measured "
            "after: travel per order line before and after is the "
            "scoreboard. Advanced slotting turns the warehouse from "
            "a building that holds stock into a machine that picks "
            "it."
        ),
        "how_it_works": (
            "Advanced slotting works as a scored assignment. For "
            "each SKU compute the COI: storage cube in cubic feet "
            "divided by picks per period. Sort ascending - small, "
            "frequent first. For each SKU in order, score the open "
            "locations: travel distance from the pack stations, "
            "height band (golden zone preferred for fast picks), "
            "adjacency to correlated SKUs from order-history "
            "affinity, family and hazard fit, and congestion "
            "penalty if the aisle already hosts hot SKUs. Assign "
            "the best scorer, continue down the list. Forward "
            "faces are sized from the SKU's daily pick volume and "
            "the replenishment trip cost: too small a face means "
            "constant refills, too large wastes golden-zone space. "
            "The whole plan is simulated against a representative "
            "order set before any physical move, and the "
            "before-and-after travel per line is reported. The "
            "demo computes COI for eight SKUs, assigns them to a "
            "location grid with golden-zone scoring, and reports "
            "the travel saved versus naive slotting."
        ),
        "key_points": [
            "The cube-per-order index (cube divided by order frequency) ranks who earns the closest slots: small and frequent wins.",
            "The golden zone - knee to shoulder height - holds the fastest picks: ergonomics joins travel in the math.",
            "Correlated slotting seats order-mates side by side so multi-line picks walk compact loops.",
            "Forward faces are sized from pick volume versus replenishment cost; congestion modeling keeps hot SKUs out of shared queues.",
            "Simulate before moving, measure after: travel per order line before and after is the scoreboard.",
        ],
        "requirements": [
            "COI or equivalent velocity-cube ranking per SKU from real pick history and measured cube.",
            "Order-line affinity analysis for correlated placement of frequent companions.",
            "A scored location assignment honoring travel, height, family, hazard, and congestion.",
            "Forward-face sizing per fast SKU from pick volume and refill economics.",
            "Simulation before moves and travel-per-line measurement after.",
        ],
        "standards": [
            "Slotting plans respect rack ratings, fire-code clearances, and hazard segregation regardless of velocity.",
            "Ergonomic placement follows manual-handling guidance for the golden zone and weight limits.",
            "Re-slotting moves are system-directed with full movement records.",
        ],
        "citations": [CIT_TOMPKINS, CIT_BARTHOLDI, CIT_APICS],
        "sig_lens": (
            "The Signature read: advanced slotting is the seating "
            "of the court by merit and measure - the swiftest and "
            "smallest nearest the throne, companions beside "
            "companions, none crowded at the gate. The Signature "
            "Stock Method measures each SKU's worth in cube and "
            "speed and seats it accordingly, for a treasury "
            "arranged as a machine serves its promises at the "
            "speed of thought."
        ),
    },
    {
        "key": "dynamic_safety_stock",
        "name": "Dynamic Safety Stock and Service Levels",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Static safety stock is a number set once and aging "
            "quietly wrong. Dynamic safety stock recomputes the "
            "buffer as demand variability, lead times, and "
            "service targets move - seasonal SKUs get fat buffers "
            "in peak season and lean ones off-season, automatically. "
            "The service level itself deserves engineering, not "
            "habit: cycle service (fraction of cycles without "
            "stockout) and fill rate (fraction of demand served "
            "from stock) are different promises, and customers "
            "feel fill rate. The economics are explicit: each "
            "point of service has a stock cost and a stockout "
            "cost, and the optimal service level balances them - "
            "expensive stockouts justify high service, cheap and "
            "substitutable goods do not. Differentiated service "
            "by ABC class is the standard practice: 99 percent "
            "for the A items that fund the business, lower for "
            "the C items where the buffer would cost more than "
            "the occasional miss. Forecast-error-based buffers go "
            "further than demand-variability ones where "
            "forecasts drive ordering: size the buffer on the "
            "forecast error distribution, which is the "
            "variability that actually surprises you. Dynamic "
            "safety stock is the buffer growing up: measured, "
            "priced, differentiated, and always current."
        ),
        "how_it_works": (
            "Dynamic safety stock works as a recomputed policy, "
            "not a stored number. Each planning cycle, the system "
            "refreshes per-SKU inputs: demand variability (or "
            "forecast error) over recent history, current lead "
            "time and its variability per supplier, and the "
            "service target from the ABC-class policy table. It "
            "recomputes SS = z * sigma * sqrt(L) with the fresh "
            "inputs - plus the lead-time-variance term where "
            "suppliers wobble - and updates the reorder point. "
            "Seasonality enters through time-varying sigma: the "
            "peak season's wider swings automatically fatten the "
            "buffer, and the quiet season thins it. The economics "
            "check runs alongside: marginal stock cost of the "
            "next service point versus marginal stockout cost, "
            "flagging SKUs where the policy target looks "
            "uneconomic. Fill rate is monitored against the "
            "promise, and persistent gaps trigger a review of "
            "the inputs, not just a bigger number. The demo "
            "recomputes safety stock across a seasonal swing and "
            "prices three service levels against their stockout "
            "costs."
        ),
        "key_points": [
            "Dynamic safety stock recomputes the buffer each cycle from fresh variability, lead times, and service targets.",
            "Cycle service and fill rate are different promises: customers feel fill rate - engineer to the one that matters.",
            "Optimal service balances marginal stock cost against marginal stockout cost; differentiate by ABC class.",
            "Forecast-error-based buffers beat demand-variability ones where forecasts drive the ordering.",
            "Seasonality enters through time-varying variability: fat buffers in peak, lean off-season, automatically.",
        ],
        "requirements": [
            "Per-SKU variability inputs refreshed each planning cycle: demand sigma or forecast-error sigma.",
            "Current lead times with variability per supplier per SKU.",
            "A service-target table by ABC class, priced and approved.",
            "Automatic recomputation of safety stock and reorder points on the cycle.",
            "Fill-rate monitoring against the promise with input reviews on persistent gaps.",
        ],
        "standards": [
            "Service-level definitions follow APICS Dictionary (cycle service vs fill rate).",
            "Statistical inputs use cleaned history with documented outlier treatment.",
            "Policy changes to service targets are approved at the level the inventory policy names.",
        ],
        "citations": [CIT_SILVER, CIT_NAHMIAS, CIT_GROSS, CIT_APICS],
        "sig_lens": (
            "The Signature read: the dynamic guard watches the "
            "seasons - swelling when the storms come, thinning "
            "when the skies clear, always measured and never "
            "habitual. The Signature Stock Method prices each "
            "degree of certainty and buys exactly what the vow "
            "requires: the heavy vows guarded to the nines, the "
            "light ones trusted to leaner watch. A guard that "
            "never changes is a guard asleep."
        ),
    },
    {
        "key": "replenishment_systems",
        "name": "Replenishment Systems: Kanban, Min-Max, and DRP",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Replenishment is the standing order to keep the shelf "
            "full, and the systems differ in how they decide when "
            "and how much. Kanban is the pull system: a fixed number "
            "of cards or containers circulates, each card authorizing "
            "one container of stock, and an empty container returning "
            "upstream is the order signal - no card, no production, "
            "no overstock possible by construction. The number of "
            "kanbans is the math: demand during lead time times one "
            "plus the safety factor, divided by container size. "
            "Min-max is the simple visual sibling: when the bin "
            "falls to the min, order up to the max - the two-bin "
            "system on the factory floor is min-max made physical. "
            "DRP - distribution requirements planning - is MRP's "
            "downstream mirror: it time-phases demand across the "
            "distribution network and generates planned shipments "
            "between sites. The choice follows the demand pattern: "
            "kanban for stable, repeating consumption; min-max for "
            "simple, low-value supervision; DRP for networks with "
            "lumpy, planned distribution. All three share the "
            "discipline's soul: the replenishment signal is "
            "automatic, visible, and tied to real consumption - "
            "never to somebody's feeling about the shelf."
        ),
        "how_it_works": (
            "Kanban works as a closed loop of authorizations. "
            "Containers of fixed size circulate between the "
            "supplying process and the consuming point; each "
            "container carries a kanban card. When the consumer "
            "empties a container, the card returns upstream as the "
            "order for exactly one container - production or "
            "replenishment happens only on a returned card. The "
            "card count sets the maximum inventory in the loop: "
            "cards = D * L * (1 + S) / C, where D is demand rate, "
            "L lead time, S the safety factor, and C the container "
            "quantity. Min-max works as a visual trigger: the bin "
            "has a marked min line; crossing it orders the "
            "difference to max. DRP works as time-phased netting "
            "per site: gross requirements by week from forecasts "
            "and orders, minus on-hand and in-transit, yielding "
            "planned receipts that become planned shipments from "
            "upstream. The demo sizes a kanban loop for a "
            "production cell, runs a min-max bin through a week, "
            "and nets a two-site DRP plan."
        ),
        "key_points": [
            "Kanban is pull by construction: fixed cards circulate, an empty container returning is the order, no card means no stock.",
            "Kanban sizing: cards = demand * lead time * (1 + safety factor) / container quantity.",
            "Min-max is the visual sibling: cross the min line, order up to the max - the two-bin system made physical.",
            "DRP is MRP's downstream mirror: time-phased netting across the network generating planned inter-site shipments.",
            "Match the system to the pattern: kanban for stable repeating consumption, min-max for simple supervision, DRP for planned networks.",
        ],
        "requirements": [
            "For kanban: fixed container quantities, a card per container, and the discipline that no card means no production.",
            "A kanban sizing computation per loop, reviewed as demand rates move.",
            "For min-max: marked min and max per bin and a standing order-up-to process.",
            "For DRP: time-phased demand per site, on-hand and in-transit visibility, and planned shipment logic.",
            "In all three: the signal is automatic and tied to consumption, never to feeling.",
        ],
        "standards": [
            "Kanban practice follows the pull-system principles of the Toyota Production System literature.",
            "Container quantities respect ergonomic handling limits and the point-of-use space.",
            "DRP planned shipments respect lane capacities and lead times in the network model.",
        ],
        "citations": [CIT_OHNO, CIT_WOMACK, CIT_SILVER, CIT_APICS],
        "sig_lens": (
            "The Signature read: replenishment is the heartbeat of "
            "the treasury - the steady pulse that keeps every shelf "
            "alive. The Signature Stock Method beats in pull rhythm: "
            "each empty vessel returning upstream is a call, each "
            "card an authorization, and the heart never races ahead "
            "of need nor lags behind it. Count the cards, size them "
            "honestly, and the pulse steadies the whole body."
        ),
    },
    {
        "key": "returns_rma",
        "name": "Returns, RMAs, and Reverse Logistics",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Goods come back: wrong items, damaged arrivals, "
            "warranty failures, recalls, and customers who changed "
            "their minds. The RMA - return merchandise authorization - "
            "is the gate: no return enters without a number tying it "
            "to the original order, the reason, and the promised "
            "disposition. The returns dock inspects and grades every "
            "unit: restockable as new, refurbishable, parts "
            "harvest, or scrap - and the grade decides the "
            "financial fate, from full credit to zero. Reverse "
            "logistics is the whole backward pipeline: return "
            "transport, receipt, inspection, disposition, and the "
            "credit or replacement flowing back to the customer. "
            "It is expensive and getting more so with e-commerce "
            "return rates, which is why the discipline measures "
            "it: return rate by SKU and reason, cost per return, "
            "recovery rate of returned value. The data is gold: "
            "returns by reason are the quality department's "
            "cheapest field intelligence, and a spike in one "
            "reason code is an early warning no survey will give. "
            "Handle returns well and they become a loyalty "
            "engine; handle them badly and they become a "
            "reputation fire."
        ),
        "how_it_works": (
            "Returns work as a mirrored inbound flow with "
            "inspection at its heart. The customer requests an "
            "RMA with the order number and reason; the system "
            "issues the authorization with return instructions "
            "and the promised disposition policy. At the returns "
            "dock, each unit is received against its RMA, "
            "inspected, and graded: A (restock as new), B "
            "(refurbish), C (parts harvest), D (scrap). The "
            "grade posts the stock to the right state - A to "
            "sellable, B to a refurb queue, C to teardown, D to "
            "scrap - and triggers the financial leg: credit "
            "memo, replacement shipment, or repair order. Reason "
            "codes accumulate into the returns dashboard: rate "
            "by SKU, by reason, by customer, with cost per return "
            "and value recovery rate. Recalls ride the same rails "
            "with urgency flags and customer-notification records. "
            "The demo processes five returns through grading, "
            "posts each to its disposition state, and computes "
            "the recovery rate."
        ),
        "key_points": [
            "The RMA is the gate: no return enters without a number tying it to the order, the reason, and the promised disposition.",
            "Grading decides the financial fate: restock as new, refurbish, parts harvest, or scrap - each with its own stock state.",
            "Reverse logistics is the full backward pipeline: transport, receipt, inspection, disposition, and the credit flowing back.",
            "Returns data is quality intelligence: spikes by reason code are early warnings no survey provides.",
            "Measure it: return rate by SKU and reason, cost per return, recovery rate of returned value.",
        ],
        "requirements": [
            "An RMA process with authorization numbers, return instructions, and disposition promises.",
            "A returns inspection station with grading rules and trained graders.",
            "Disposition states in the system: sellable, refurb queue, teardown, scrap - with postings per grade.",
            "Credit and replacement processing tied to the RMA, not to memory.",
            "A returns dashboard: rates, reasons, costs, and recovery, reviewed with quality.",
        ],
        "standards": [
            "Returned goods are quarantined on receipt until inspection and grading are complete.",
            "Warranty and recall handling follow the product's warranty terms and the market's consumer-protection rules.",
            "Scrap disposition of regulated goods follows environmental disposal rules.",
        ],
        "citations": [CIT_APICS, CIT_CHOPRA, CIT_BARTHOLDI],
        "sig_lens": (
            "The Signature read: returns are the vows that came "
            "home - promises the world sent back, each carrying a "
            "lesson. The Signature Stock Method receives them at "
            "a proper gate, grades them honestly, and learns from "
            "every reason code, for the returned vow is the "
            "treasury's truest teacher. Recover what honor allows, "
            "credit what honor demands, and let the reasons teach."
        ),
    },
    {
        "key": "serialization",
        "name": "Serialized Inventory and Traceability",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Lot tracking knows families; serialization knows "
            "individuals. A serialized item carries a unique serial "
            "number from birth to retirement: one phone, one "
            "engine, one medical device - each with its own identity, "
            "its own history, its own warranty. The warehouse "
            "tracks serialized stock unit by unit: which serial "
            "numbers are in which locations, which shipped to which "
            "customer on which date, which came back on which RMA. "
            "The discipline is strict because the stakes are: "
            "recalls of medical devices or automotive parts must "
            "reach the exact affected units, warranty claims must "
            "verify the exact unit's age and history, and theft or "
            "diversion shows as a serial in the wrong hands. "
            "Serialization pairs with aggregation: the serials in "
            "a case are children of the case SSCC, the cases "
            "children of the pallet - so scanning the pallet "
            "identifies every unit without opening it. The data "
            "model is heavier than lot tracking - millions of "
            "individuals, not thousands of lots - and the "
            "processes must capture every serial at receipt, at "
            "pick, and at ship without exception. Where the law "
            "demands it, as in pharmaceuticals, serialization is "
            "not best practice but license to operate."
        ),
        "how_it_works": (
            "Serialization works as an individual registry "
            "alongside the quantity ledger. At receipt, each "
            "unit's serial is captured - by scan, by supplier "
            "file, or by range - and registered to the lot, "
            "the location, and the receipt. Every movement "
            "names serials: the pick task lists the exact "
            "serials to take, the pack scan confirms them, "
            "the shipment records which serials left to which "
            "customer. Aggregation builds the hierarchy: case "
            "SSCC parents its serials, pallet SSCC parents its "
            "cases, and a single pallet scan explodes to the "
            "full unit list. The registry enforces uniqueness - "
            "a duplicate serial is rejected at capture - and "
            "state: a serial is exactly one of in-stock, "
            "shipped, returned, scrapped, or in-service. "
            "Recalls query by lot or date range and return the "
            "exact serials and their customer addresses. The "
            "demo registers twenty serials across two cases, "
            "aggregates them to a pallet, ships three units, "
            "and traces one serial's full history."
        ),
        "key_points": [
            "Serialization tracks individuals, not families: each unit's own identity, history, and warranty from birth to retirement.",
            "Every movement names serials: receipt captures them, picks list them, shipments record which went where.",
            "Aggregation builds parent-child hierarchy: pallet parents cases, cases parent serials - one scan explodes to the unit list.",
            "The registry enforces uniqueness and state: a serial is exactly one of in-stock, shipped, returned, scrapped, or in-service.",
            "Recalls become exact: query by lot or date, get the precise serials and their customer addresses.",
        ],
        "requirements": [
            "Serial capture at receipt for every serialized SKU: scan, supplier file, or verified range.",
            "Serial identity on every movement: putaway, pick, pack, ship, return.",
            "Aggregation records: case-to-serial and pallet-to-case parentage maintained automatically.",
            "Uniqueness enforcement at capture and a state machine per serial.",
            "Recall query capability returning exact serials and ship-to addresses on demand.",
        ],
        "standards": [
            "Pharmaceutical serialization follows the market's track-and-trace regulations (unit-level identification and verification).",
            "Serial formats follow GS1 SGTIN practice where GS1 identification is used.",
            "Serialized records are retained per the product's regulatory and warranty retention periods.",
        ],
        "citations": [CIT_GS1, CIT_APICS, CIT_BARTHOLDI],
        "sig_lens": (
            "The Signature read: the serial is the true name of "
            "the unit - spoken once at birth and never shared. "
            "The Signature Stock Method knows its charges by name: "
            "where each was born, where it sleeps, whom it serves, "
            "and when it returns. A treasury that names its "
            "greatest pieces individually can summon any one of "
            "them, anywhere, in an hour - and that is the highest "
            "form of the keeper's art."
        ),
    },
    {
        "key": "physical_inventory",
        "name": "The Full Physical Inventory",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The full physical inventory - the wall-to-wall count - "
            "is the discipline's day of reckoning: every SKU, every "
            "location, counted and reconciled, usually once a year "
            "for the financial audit. It shuts down or sharply "
            "curtails operations, which is why cycle counting exists "
            "to make it almost unnecessary - almost, because "
            "auditors and the tax authorities still want the "
            "annual proof. Preparation is most of the work: "
            "transactions cut off and posted, in-transit settled, "
            "locations labeled and swept, count teams trained, and "
            "the warehouse frozen - nothing moves during the count "
            "except by the count team's rules. Counting is blind "
            "and double: two independent counts per location, "
            "reconciled where they disagree, with recounts for "
            "the differences that matter. Reconciliation is the "
            "judgment phase: every variance investigated, "
            "adjustments posted with reason codes, and the "
            "financial inventory revalued on the corrected "
            "balances. The count's deeper product is the "
            "accuracy report: where the books were wrong and why, "
            "feeding next year's cycle-count priorities. A clean "
            "physical inventory - small adjustments, known causes - "
            "is the certificate that the year's daily discipline "
            "worked."
        ),
        "how_it_works": (
            "The physical inventory works as a controlled freeze "
            "and sweep. Cutoff: all receipts, picks, and "
            "transfers are posted, open transactions closed, and "
            "the system balance is snapshotted as the book "
            "record. Freeze: the warehouse stops moving stock; "
            "any emergency move is logged by the count team. "
            "Teams sweep location by location with blind count "
            "sheets - no book quantities shown - and each "
            "location is counted twice by different teams; "
            "matches post, mismatches trigger a third count. "
            "Stratified sampling may cover the C items where "
            "full double counts are uneconomic, with the method "
            "documented for the auditors. Reconciliation "
            "compares the frozen counts to the snapshot: "
            "variances are investigated, adjustments posted with "
            "reason codes and approvals, and the inventory is "
            "revalued. The demo freezes a small warehouse, runs "
            "double blind counts with one planted discrepancy, "
            "reconciles against the snapshot, and posts the "
            "adjustment."
        ),
        "key_points": [
            "The wall-to-wall count is the annual reckoning: every SKU, every location, counted and reconciled for the audit.",
            "Preparation is most of the work: cutoff posted, in-transit settled, locations labeled, the warehouse frozen.",
            "Counting is blind and double: two independent counts per location, reconciled where they disagree.",
            "Reconciliation is judgment: investigate every variance, post adjustments with reason codes and approvals.",
            "The count's deeper product is the accuracy report feeding next year's cycle-count priorities.",
        ],
        "requirements": [
            "A count plan: teams, territories, schedule, blind sheets, and the freeze rules.",
            "Transaction cutoff with all movements posted and the book balance snapshotted.",
            "Double blind counts per location with a defined mismatch-recount rule.",
            "Variance investigation and reason-coded adjustments with approvals.",
            "An accuracy report to the auditors and to next year's count program.",
        ],
        "standards": [
            "The count procedure satisfies the external auditors' requirements for observing inventory.",
            "Inventory is valued on the reconciled balances per IAS 2 / ASC 330.",
            "Count teams are independent of the custodians of the stock they count.",
        ],
        "citations": [CIT_IAS2, CIT_ASC330, CIT_APICS, CIT_SILVER],
        "sig_lens": (
            "The Signature read: the full count is the treasury's "
            "day of judgment - every chamber opened, every vow "
            "verified, the ledger weighed against the gold. The "
            "Signature Stock Method meets the day without fear, "
            "for the daily inspection has kept the books near "
            "true all year. Count blind, count twice, judge every "
            "variance - and let the certificate of the count be "
            "the honor of the house."
        ),
    },
    {
        "key": "inventory_analytics",
        "name": "Inventory Analytics: Turns, Days of Supply, and Stockouts",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Analytics turns the ledger into judgment: is this "
            "inventory healthy? Inventory turns - cost of goods sold "
            "divided by average inventory value - says how many times "
            "the stock cycles per year; higher turns mean leaner "
            "capital, but turns too high mean stockouts. Days of "
            "supply inverts it: average inventory divided by daily "
            "usage, the number of days the shelf could serve at "
            "current pace. Fill rate - the fraction of demand served "
            "immediately from stock - measures the customer's "
            "experience; stockout rate and backorder aging measure "
            "its failures. Excess and obsolete reporting names the "
            "dead: stock above the maximum, stock with no movement "
            "in a year, stock past its market life - each with a "
            "disposition and an owner. GMROI - gross margin return "
            "on inventory investment - joins profit and turns for "
            "retail judgment: margin times turns, the return on "
            "every dollar sleeping on the shelf. The analytics "
            "run on rhythm - weekly for operations, monthly for "
            "management - and every metric has an owner and a "
            "target. Numbers without owners are wallpaper; the "
            "discipline assigns both."
        ),
        "how_it_works": (
            "Inventory analytics work as a computed dashboard over "
            "the ledger. Turns: annual cost of goods sold divided by "
            "average inventory value (beginning plus ending over "
            "two, or monthly average for seasonality). Days of "
            "supply: on-hand value divided by average daily usage "
            "value. Fill rate: order lines shipped complete from "
            "stock divided by lines ordered. Stockout tracking "
            "logs every zero-available event with its duration and "
            "lost or backordered demand. Excess logic flags SKUs "
            "above their max or with days of supply beyond policy; "
            "obsolete logic flags no-movement and expired-market "
            "SKUs for disposition review. GMROI: gross margin "
            "dollars divided by average inventory cost. Targets "
            "are set by ABC class and channel, and the dashboard "
            "shows trend arrows, not just snapshots - direction "
            "matters more than position. The demo computes turns, "
            "days of supply, fill rate, and GMROI for a SKU set "
            "and flags the excess and obsolete."
        ),
        "key_points": [
            "Turns (COGS over average inventory) measure capital leanness; days of supply measures the shelf's endurance at current pace.",
            "Fill rate measures the customer's experience; stockout logs with duration and lost demand measure its failures.",
            "Excess and obsolete reporting names the dead stock with dispositions and owners - no anonymous corpses.",
            "GMROI (margin times turns) judges the return on every dollar sleeping on the shelf.",
            "Every metric runs on rhythm with an owner and a target; trend arrows matter more than snapshots.",
        ],
        "requirements": [
            "A metric dictionary: turns, days of supply, fill rate, stockout rate, excess, obsolete, GMROI - defined once, used everywhere.",
            "Targets by ABC class and channel, approved and published.",
            "Weekly operational and monthly management rhythms with named owners per metric.",
            "Excess and obsolete reviews with dispositions, owners, and deadlines.",
            "Trend views, not snapshots: direction matters more than position.",
        ],
        "standards": [
            "Turns and valuation inputs reconcile to the financial records per IAS 2 / ASC 330.",
            "Metric definitions follow APICS Dictionary usage so benchmarks compare honestly.",
            "Dashboard data comes from the system ledger, not from manual spreadsheets.",
        ],
        "citations": [CIT_APICS, CIT_SILVER, CIT_NAHMIAS, CIT_IAS2],
        "sig_lens": (
            "The Signature read: analytics are the treasury's "
            "mirror - showing the keeper the true face of the "
            "stock: how fast the gold turns, how long the shelf "
            "endures, how often the vow was kept. The Signature "
            "Stock Method looks in the mirror on rhythm and acts "
            "on what it sees, for a keeper who will not look will "
            "not know, and a keeper who will not act has no "
            "business keeping."
        ),
    },
    {
        "key": "health_program",
        "name": "The Inventory Health Program",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The health program is everything in this database "
            "running as one routine: the capstone record. It "
            "binds the data models (SKU, location, lot), the "
            "counting (cycle counts, the annual physical), the "
            "issuing rules (FIFO, FEFO), the math (reorder "
            "points, EOQ, safety stock, kanban), the movement "
            "records (receipts, transfers, adjustments with "
            "reasons), and the analytics (turns, fill rate, "
            "excess) into a single operating cadence with owners, "
            "rhythms, and targets. The program scores overall "
            "health as a weighted composite: accuracy, fill "
            "rate, turns, excess and obsolete, count compliance, "
            "and on-time replenishment - one number the business "
            "can watch, with drill-down to the failing part. "
            "Governance is explicit: an inventory policy document "
            "names the rules, the planners own the parameters, "
            "operations owns the execution, finance owns the "
            "valuation, and a monthly review owns the truth. "
            "Continuous improvement closes the loop: every "
            "variance, stockout, and excess event feeds a "
            "corrective action, and the program measures whether "
            "the actions worked. A warehouse can run every "
            "technique in this database and still be unhealthy "
            "if they run as disconnected chores; the health "
            "program makes them one organism with one pulse."
        ),
        "how_it_works": (
            "The health program works as a governed composite. "
            "Each pillar reports its metric on rhythm: accuracy "
            "from cycle counts, fill rate from order promises, "
            "turns and days of supply from the ledger, excess "
            "and obsolete from the analytics, count compliance "
            "from the schedule, on-time replenishment from the "
            "purchase and transfer orders. Weights set by "
            "management combine them into a health score from 0 "
            "to 100; thresholds set the colors - green, amber, "
            "red - and red pillars get corrective actions with "
            "owners and dates. The monthly review walks the "
            "scorecard top-down: red first, then amber trends, "
            "then the improvement backlog. Parameter governance "
            "keeps the math honest: reorder points, safety "
            "stocks, and ABC classes are recomputed on schedule "
            "by named planners, never left to age. The annual "
            "physical inventory certifies the year. The demo "
            "scores a warehouse across six pillars, weights them "
            "into one health number, and raises corrective "
            "actions for the red pillars."
        ),
        "key_points": [
            "The health program binds every technique in this database into one governed routine with owners, rhythms, and targets.",
            "A weighted composite score - accuracy, fill rate, turns, excess, count compliance, on-time replenishment - gives the business one number to watch.",
            "Governance is explicit: policy names the rules, planners own parameters, operations owns execution, finance owns valuation.",
            "Red pillars get corrective actions with owners and dates; the monthly review walks the scorecard top-down.",
            "Disconnected techniques are chores; the program makes them one organism with one pulse.",
        ],
        "requirements": [
            "An inventory policy document naming the rules, owners, rhythms, and targets for every pillar.",
            "A weighted health score computed on rhythm with drill-down to failing pillars.",
            "Monthly scorecard reviews with corrective actions tracked to closure.",
            "Parameter governance: recomputation schedules and named owners for reorder points, safety stock, and ABC classes.",
            "An annual physical inventory certifying the year's discipline.",
        ],
        "standards": [
            "The inventory policy is a controlled document, reviewed annually and approved at the level it names.",
            "Health metrics reconcile to the financial inventory records per IAS 2 / ASC 330.",
            "Corrective actions follow the site's quality-system practice to verified closure.",
        ],
        "citations": [CIT_APICS, CIT_SILVER, CIT_CHOPRA, CIT_IAS2],
        "sig_lens": (
            "The Signature read: the health program is the oath "
            "of the whole house - every technique a sworn "
            "officer, every metric a watch kept, every review a "
            "council of the treasury. The Signature Stock Method "
            "in full is not a set of tricks but a way of keeping: "
            "count honestly, promise carefully, move visibly, "
            "measure relentlessly, and improve without end. This "
            "is the capstone - the treasury kept as a living "
            "thing, healthy by routine and honest by design."
        ),
    },
]
