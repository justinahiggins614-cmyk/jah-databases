#!/usr/bin/env python3
"""Entries for the Retail Commerce Operations database pair (5,000-target program).

Dedupe gate: all 68 titles checked against the WHOLE system with
code/dedupe_gate.py BEFORE writing. ID prefixes JAH-RTCO- (public) and
JAH-RTCOS- (signature) verified free: zero hits in manifest id_prefix values
(exact + substring) and zero hits in shard record IDs.

34 records per edition, ladder-ordered 1-34 (Foundations 1-12 / Compounded
13-23 / Advanced 24-34).
"""


def R(t, tier, rank, desc, how, kp, req, std, cit, dk, data):
    return {'t': t, 'tier': tier, 'rank': rank, 'desc': desc, 'how': how,
            'kp': kp, 'req': req, 'std': std, 'cit': cit, 'dk': dk, 'data': data}


PUB = [
R("What Retail Commerce Is — Industry Overview", "Foundations", 1,
  "Retail commerce is the industry that moves finished goods from producers to the people who use them, through stores, websites, catalogs, and marketplaces. "
  "It is one of the largest industries in the world, employing tens of millions of people across selling floors, warehouses, buying offices, and corporate headquarters. "
  "Every retail business, from a corner shop to a global chain, runs on the same core loop: buy goods, present them, sell them, and use the proceeds to buy again.",
  "A retailer buys merchandise from suppliers or manufacturers, adds a markup that covers operating costs and profit, and sells each unit to a consumer. "
  "The difference between the selling price and the cost of goods, minus expenses like rent, wages, and shrink, is what keeps the business alive. "
  "Successful retailers tune every part of this loop - assortment, price, availability, and service - so customers return and each square foot of selling space earns its keep.",
  ["Retailers sell finished goods directly to consumers, unlike wholesalers who sell to businesses.",
   "The core retail loop is buy, present, sell, and reinvest the proceeds.",
   "Markup must cover rent, wages, shrink, and still leave a profit.",
   "Retail formats include department stores, supermarkets, specialty shops, discounters, and pure e-commerce.",
   "Customer return visits are the truest measure of a healthy retail operation."],
  ["A clear definition of the customer the store serves.",
   "A merchandise assortment matched to that customer.",
   "Reliable suppliers and a way to pay them.",
   "A place to sell: a storefront, a website, or both."],
  ["Consistent pricing and honest advertising practices.",
   "Accurate sales records for every transaction.",
   "Safe, accessible selling space for customers and staff."],
  ["National Retail Federation industry research on retail formats and employment (public reports).",
   "U.S. Census Bureau Monthly Retail Trade survey methodology (public statistics)."],
  "basket", {"txns": 8500, "items": 22100, "revenue": 187450.0}),

R("Product Catalogs and SKU Systems", "Foundations", 2,
  "A product catalog is the retailer's master list of everything it sells, and the SKU - stock keeping unit - is the unique code that identifies each distinct item in that catalog. "
  "One style of shirt in five sizes and three colors is fifteen SKUs, and each SKU gets its own record with its price, cost, supplier, and stock count. "
  "Without disciplined SKU records, a retailer cannot know what it owns, what is selling, or what to reorder.",
  "When a new product is accepted, the buying team creates a SKU record with a unique number, a plain-language description, the size or variant attributes, the cost, and the selling price. "
  "Every later event - a purchase order, a delivery, a sale, a return, a markdown - references that SKU number, so the system always knows the on-hand count and the sales history per item. "
  "Catalog hygiene means one record per real variant, no duplicates, and retired SKUs archived rather than deleted so history stays intact.",
  ["A SKU identifies one exact variant: style plus size plus color plus pack.",
   "Every inventory and sales event references the SKU number.",
   "Duplicate or sloppy SKU records corrupt counts, reorders, and reports.",
   "Retired SKUs are archived, never deleted, to preserve sales history.",
   "The catalog is the single source of truth for what the retailer sells."],
  ["A numbering scheme with room to grow (never reuse numbers).",
   "A written description standard: same attribute order on every SKU.",
   "Cost and price fields maintained by the buying team.",
   "A process for adding, changing, and retiring SKUs."],
  ["One SKU per distinct sellable variant - no shared numbers.",
   "Descriptions complete enough that a stranger could pick the item.",
   "Cost changes logged with date and reason."],
  ["GS1 General Specifications for product identification numbering (public standard).",
   "Retail industry SKU management best-practice guides (public publications)."],
  "markup", {"cost": 18.50, "price": 42.00}),

R("Barcodes, GTINs, and Product Identification", "Foundations", 3,
  "A barcode is a machine-readable picture of a product number, and the GTIN - Global Trade Item Number - is the worldwide numbering system behind most of them. "
  "The familiar UPC with its twelve digits is one form of GTIN, and scanning it at the register tells the point of sale exactly which SKU just sold and at what price. "
  "Standard numbering lets any retailer's scanner read any supplier's product, which is why a can of soup scans correctly in every store in the country.",
  "A manufacturer or brand owner licenses a company prefix from GS1, assigns item numbers beneath it, and computes the final check digit with the published modulus algorithm. "
  "The full number is printed as a barcode on the package; at the register the scanner decodes the bars, the POS looks up the SKU by that number, and the price on file is charged. "
  "Because the check digit catches mis-scans, the wrong price is almost never charged from a clean scan.",
  ["The GTIN is the global standard number behind UPC and EAN barcodes.",
   "A company prefix from GS1 guarantees the number is unique worldwide.",
   "The check digit is computed, not chosen, and catches scanning errors.",
   "The barcode identifies the item; the retailer's file sets the price."],
  ["A GS1 company prefix for any brand creating its own numbers.",
   "Barcode printing that meets minimum size and contrast rules.",
   "A POS lookup file mapping every scanned number to a SKU and price."],
  ["Printed barcodes must scan on the first pass at normal register speed.",
   "Every GTIN in the store must resolve to exactly one SKU record.",
   "Check digits verified by the modulus algorithm before a number goes live."],
  ["GS1 General Specifications for GTIN structure and check-digit calculation (public standard).",
   "ISO/IEC 15420 for linear barcode print quality (public standard)."],
  "markup", {"cost": 2.10, "price": 4.99}),

R("Retail Pricing Strategy Fundamentals", "Foundations", 4,
  "Pricing strategy is the plan behind the numbers on the tags: how the retailer sets everyday prices, when it discounts, and how it responds to competitors. "
  "Common strategies include everyday low pricing, high-low promotion pricing, premium pricing for luxury goods, and penetration pricing to win a new market. "
  "The strategy must cover costs and deliver the target margin while matching what the customer expects to pay for the retailer's position in the market.",
  "The retailer starts from the item's cost, adds the target margin to reach a candidate price, then adjusts for the strategy: rounding to a psychological price point, aligning with competitor prices, or holding a premium for brand strength. "
  "Promotional prices are planned in a calendar with funding - either margin the retailer gives up or money the supplier contributes - and the everyday price returns when the event ends. "
  "Price changes flow from the pricing file to shelf labels, the POS, and the website together so the customer never sees two prices.",
  ["Everyday price must cover cost plus target margin plus operating reality.",
   "Promotional pricing is planned, funded, and temporary - not accidental.",
   "Psychological price points (9.99) and competitor alignment shape the final number.",
   "One pricing file feeds shelf, register, and website so prices agree everywhere."],
  ["Item cost and target margin for every SKU.",
   "A promotional calendar with funding agreed before the event.",
   "A price-change process that updates shelf, POS, and web together."],
  ["Ticketed shelf price must match the price charged at the register.",
   "Promotional terms (dates, limits) stated plainly to the customer.",
   "Competitor price checks done on comparable items, not mismatched ones."],
  ["Retail pricing strategy literature on EDLP and high-low models (public publications).",
   "State and local pricing-accuracy and scanner laws (public regulations)."],
  "markup", {"cost": 32.00, "price": 79.99}),

R("The Point of Sale (POS) System", "Foundations", 5,
  "The point of sale system is the cash register grown up: the hardware and software that records every sale, takes payment, and updates inventory in real time. "
  "A modern POS includes the terminal, barcode scanner, receipt printer, cash drawer, and card reader, all driven by software holding the price file and the day's transactions. "
  "It is the retailer's nervous system - every unit sold, every dollar taken, and every discount given passes through it.",
  "The cashier scans each item's barcode; the POS looks up the SKU, pulls the current price and any promotion, and builds the ticket line by line. "
  "Tender is accepted as cash, card, gift card, or mobile payment, the drawer or terminal records it, change is computed, and a receipt prints. "
  "At the moment of sale the POS decrements on-hand inventory for each SKU and posts the transaction to the sales journal for the day's close.",
  ["The POS records the sale, takes payment, and updates inventory in one motion.",
   "The price file - not the shelf tag - is what the register charges.",
   "Every transaction posts to a journal used for the daily close and audit.",
   "Modern POS hardware: terminal, scanner, printer, drawer, and payment reader."],
  ["A current price file covering every active SKU.",
   "Payment processing for cash, cards, and gift cards.",
   "A daily close routine: count, reconcile, and post the day's sales.",
   "Trained cashiers who can handle voids, returns, and price checks."],
  ["The charged price must equal the filed price for the scanned SKU.",
   "Voids and no-sales logged with operator ID and reason.",
   "Cash drawers counted and reconciled against the journal every day."],
  ["POS system vendor documentation on transaction journaling (public manuals).",
   "PCI Security Standards for protecting card data at the register (public standard)."],
  "basket", {"txns": 1240, "items": 3720, "revenue": 48620.0}),

R("Cash Handling and Payment Processing", "Foundations", 6,
  "Cash handling is the discipline of receiving, storing, and banking physical money without loss, and payment processing is the parallel discipline for cards and digital payments. "
  "Together they answer the most basic retail question at the end of the day: does the money in hand match the money the system says was taken. "
  "Sloppy cash handling bleeds a store through errors and theft; tight handling makes every dollar traceable.",
  "Each register starts the day with a counted float, and every cash sale, paid-out, and drop is logged against the cashier's ID. "
  "Card payments travel from the reader through the processor to the retailer's bank account, minus a processing fee, usually settling within a day or two. "
  "At close, the drawer is counted, the count is compared to the journal, overages and shortages are investigated, and the cash is secured for bank deposit.",
  ["Every register starts with a counted float and ends with a counted close.",
   "Cashier IDs tie every cash event to a person for accountability.",
   "Card sales settle to the bank minus a processing fee, typically in one to two days.",
   "Overages and shortages are investigated, not ignored."],
  ["A safe or drop box for securing cash during the day.",
   "Card processing with settled-batch reconciliation.",
   "A written cash policy: floats, drops, paid-outs, and deposit routine."],
  ["Two-person counts for large cash movements where practical.",
   "Deposits made on schedule; cash never accumulates past the safe limit.",
   "Card data handled under PCI rules - never written down or stored in the open."],
  ["PCI Data Security Standard for card handling (public standard).",
   "Retail cash-handling procedure guides (public publications)."],
  "breakeven", {"fixed": 18500.0, "price": 24.99, "varcost": 11.20}),

R("Store Layout and Customer Flow", "Foundations", 7,
  "Store layout is the floor plan as a selling tool: where the door, aisles, departments, and registers sit, and how customers move between them. "
  "Good layout pulls shoppers past high-margin departments, keeps staple goods easy to find, and avoids bottlenecks at the entrance, the registers, and the fitting rooms. "
  "The classic patterns are the grid (supermarkets), the loop or racetrack (department stores), and free-flow (boutiques).",
  "The designer maps the selling floor into zones, placing destination departments like groceries at the back so shoppers travel the store, and impulse items near the registers where dwell time is highest. "
  "Aisle width, sightlines, and signage are set so a new customer can orient in seconds, and the decompression zone just inside the entrance is kept open so entering shoppers slow down instead of blowing past displays. "
  "Registers go where queues will not block aisles, with a clear exit path that passes one last display.",
  ["Layout patterns: grid, loop/racetrack, and free-flow, chosen per format.",
   "Destination departments at the back pull traffic through the store.",
   "The decompression zone inside the entrance must stay open and inviting.",
   "Registers placed so queues never block selling aisles."],
  ["A measured floor plan with selling vs. back-of-house space marked.",
   "Signage readable from the main traffic path.",
   "Aisle widths that fit carts, wheelchairs, and two-way traffic."],
  ["Emergency exits and fire aisles kept clear at all times.",
   "Accessible routes meeting disability-access rules.",
   "Maximum occupancy posted and observed."],
  ["Retail store design literature on traffic patterns (public publications).",
   "ADA accessibility guidelines for retail facilities (public regulation)."],
  "sellthru", {"received": 2400, "sold": 1875}),

R("Inventory Basics — Stock Counts", "Foundations", 8,
  "Inventory is the merchandise a retailer owns and has available to sell, and stock counts are how the retailer verifies that the system's numbers match reality. "
  "The system tracks an on-hand quantity per SKU; receiving adds to it, sales subtract from it, and counts confirm it. "
  "Without counts, small errors - a mis-scan here, a damaged item there - compound silently until the system says ten and the shelf holds two.",
  "A cycle count program divides the store into sections and counts a few sections every day on a rotating schedule, so the whole store is verified over weeks without closing for a full physical inventory. "
  "Counters scan or tally each SKU, compare to the system on-hand, investigate variances beyond tolerance, and post adjustments with a reason code. "
  "High-value and high-shrink SKUs are counted most often, because that is where accuracy pays for itself fastest.",
  ["On-hand quantity per SKU is the number every other decision depends on.",
   "Cycle counting verifies sections on rotation instead of shutting down for one big count.",
   "Variances beyond tolerance are investigated before posting, not blindly accepted.",
   "High-value SKUs earn the most frequent counts."],
  ["A counting schedule covering every section on rotation.",
   "Scanners or tally sheets and variance-tolerance rules.",
   "Reason codes for adjustments: damage, theft, mis-receipt, system error."],
  ["Counts performed by someone other than the person who stocks the section, where staffing allows.",
   "Adjustments reviewed by a manager before posting.",
   "A full physical inventory at least annually to reset the baseline."],
  ["Retail inventory accuracy literature on cycle counting (public publications).",
   "Accounting guidance on inventory valuation and physical verification (public standards)."],
  "turnover", {"cogs": 920000.0, "avg_inv": 184000.0}),

R("Receiving and Stocking Goods", "Foundations", 9,
  "Receiving is the controlled intake of merchandise at the back door: verifying what arrived against what was ordered before it ever reaches the shelf. "
  "Stocking is moving verified goods to their selling locations quickly and neatly, so the sales floor is full and shoppable. "
  "A store that receives sloppily will stock wrong counts, pay for goods it never got, and discover shortages only when customers complain.",
  "The receiver checks the delivery against the purchase order - item, quantity, and condition - notes damages and shorts on the delivery receipt, and posts the receipt to inventory. "
  "Goods are then sorted by department, wheeled to the floor, and stocked to the planogram with labels facing forward and like items together. "
  "Overstock goes to the back room in labeled locations so replenishment can find it later.",
  ["Verify item, quantity, and condition against the purchase order at the door.",
   "Note damages and shorts on the delivery receipt before the driver leaves.",
   "Post receipts to inventory the same day goods arrive.",
   "Stock to the planogram: right item, right location, labels forward."],
  ["A purchase order on file for every expected delivery.",
   "A clear back-door routine: check, note, sign, post.",
   "Labeled back-room locations for overstock."],
  ["Damaged goods segregated and claimed, never shelved.",
   "Delivery receipts kept as proof for invoice disputes.",
   "Heavy items stocked with safe lifting practice."],
  ["Retail receiving procedure guides (public publications).",
   "OSHA material-handling guidance for stockrooms (public regulation)."],
  "sellthru", {"received": 5000, "sold": 4350}),

R("Customer Service Fundamentals", "Foundations", 10,
  "Customer service in retail is everything the store does to make buying easy and to fix things when buying goes wrong. "
  "It covers greeting shoppers, answering product questions, handling complaints, processing returns gracefully, and following up on special orders. "
  "Shoppers remember how a store treated them far longer than they remember its prices, and good service is the cheapest form of advertising.",
  "The service standard is simple and repeatable: acknowledge every customer promptly, listen before solving, know the products well enough to advise honestly, and own problems until they are resolved. "
  "Returns are handled under a clear written policy applied consistently, and complaints are logged so patterns - a defective batch, a confusing sign - surface and get fixed. "
  "Staff are empowered to solve common problems on the spot instead of escalating everything to a manager.",
  ["Acknowledge promptly, listen fully, then solve - in that order.",
   "A written return policy, applied the same way by every employee.",
   "Complaints logged so patterns can be found and fixed.",
   "Front-line staff empowered to resolve common problems on the spot."],
  ["A published service standard every employee can recite.",
   "Product knowledge training for each department.",
   "A complaint log reviewed weekly by management."],
  ["Return and refund terms disclosed before the sale where required.",
   "Customer personal data collected only with consent and kept secure.",
   "Accessibility of service for customers with disabilities."],
  ["Retail customer-service training literature (public publications).",
   "FTC guidance on advertising and return disclosures (public regulation)."],
  "basket", {"txns": 3200, "items": 7040, "revenue": 89200.0}),

R("Merchandising Basics", "Foundations", 11,
  "Merchandising is the art and science of presenting products so customers want to buy them: what is displayed, where, in what quantity, and at what price. "
  "It spans assortment decisions, display building, signage, and the timing of when items hit the floor. "
  "Two stores can carry the identical product and sell wildly different quantities purely on the strength of merchandising.",
  "The merchandiser builds displays around a focal item at eye level, groups coordinating products so the customer sees the whole outfit or project, and keeps displays full, faced, and priced. "
  "End caps and window displays carry the current promotion or season, and signage states the price and the offer in words a hurried shopper grasps in three seconds. "
  "Displays are walked daily: restocked, straightened, and refreshed so the store always looks newly opened.",
  ["Present the right product, in the right place, at the right time, at the right price.",
   "Eye level is buy level: prime positions go to priority items.",
   "Group coordinating products so customers see complete solutions.",
   "Walk every display daily: full, faced, priced, and fresh."],
  ["A display calendar tied to promotions and seasons.",
   "Signage standards: price, offer, and dates legible at a glance.",
   "Enough back stock to keep displays full between deliveries."],
  ["Display structures stable and safe for shoppers, including children.",
   "All displayed prices match the POS price file.",
   "Aisles and exits never blocked by displays."],
  ["Visual merchandising trade literature (public publications).",
   "State pricing-accuracy requirements for displayed prices (public regulations)."],
  "markdown", {"orig": 89.99, "pct": 25.0}),

R("Retail Math I — Markup and Margin", "Foundations", 12,
  "Retail math is the arithmetic every buyer and manager uses daily, and its two founding concepts are markup and margin. "
  "Markup is the amount added to cost to reach the selling price, usually expressed as a percentage of cost; margin is the same dollars expressed as a percentage of the selling price. "
  "Confusing the two is the classic beginner error: a 50 percent markup on cost is only a 33 percent margin on price.",
  "Given a cost of 20 and a price of 40, the markup is 20 dollars, which is 100 percent of cost, while the margin is 20 dollars, which is 50 percent of price. "
  "To reach a target margin, the buyer works backward: price equals cost divided by one minus the margin rate. "
  "Every pricing, promotion, and buying decision in retail runs through these two formulas, so fluency with them is non-negotiable.",
  ["Markup percent is figured on cost; margin percent is figured on selling price.",
   "A 50% markup on cost equals a 33.3% margin on price - they are never the same number.",
   "Price = cost / (1 - margin rate) works any target margin backward from cost.",
   "Markdowns are figured on the selling price, like margin."],
  ["Item cost and planned selling price for every SKU.",
   "A target margin by department, set before buying begins.",
   "A calculator - or fluency - at every buying desk."],
  ["Margin figures used in reports defined consistently (gross vs. maintained).",
   "Promotional margin funding agreed in writing before the event.",
   "Rounded prices checked so rounding never pushes margin below target."],
  ["Standard retail mathematics textbooks and buyer training manuals (public publications).",
   "NRF buyer-training materials on markup and margin (public publications)."],
  "markup", {"cost": 45.00, "price": 90.00}),
]

PUB += [
R("Demand Forecasting", "Compounded", 13,
  "Demand forecasting is the practice of predicting how much of each product customers will want, so the retailer buys enough but not too much. "
  "Forecasts blend sales history, seasonality, trends, promotions, and local events into a forward estimate by SKU, by store, by week. "
  "Good forecasting is the difference between full shelves with fresh stock and a back room drowning in goods nobody wants.",
  "The forecaster starts with historical sales per SKU, adjusts for trend and season using the same weeks last year, then layers in known demand drivers: promotions, holidays, weather, and local events. "
  "Statistical models produce a baseline forecast; buyers and planners review and adjust it with judgment the model cannot see, like a road closure or a viral product moment. "
  "Forecast accuracy is measured afterward - actual versus forecast - and the errors feed back into better models next cycle.",
  ["Forecast by SKU by store by week: the more granular, the more useful.",
   "History plus seasonality plus known events beats gut feel alone.",
   "Human judgment adjusts the statistical baseline for what models cannot see.",
   "Accuracy is measured after the fact and fed back into the process."],
  ["Clean sales history per SKU, ideally two full years.",
   "A calendar of promotions, holidays, and local events.",
   "A defined accuracy metric (e.g., mean absolute percent error) tracked over time."],
  ["Forecasts documented with their assumptions, not presented as certainties.",
   "Promotional lifts estimated from comparable past events.",
   "Safety stock sized from forecast error, not from habit."],
  ["Demand forecasting and inventory planning literature (public publications).",
   "APICS/ASCM materials on forecasting methods (public publications)."],
  "turnover", {"cogs": 2400000.0, "avg_inv": 400000.0}),

R("Purchase Orders and Replenishment", "Compounded", 14,
  "A purchase order is the retailer's formal request to a supplier: send these SKUs, in these quantities, by this date, at these costs. "
  "Replenishment is the ongoing system that decides when to send those orders, keeping shelves stocked without piling up excess. "
  "Together they are the ordering heartbeat of the store: too slow and shelves go empty, too fast and cash gets trapped in stock.",
  "Replenishment watches each SKU's on-hand quantity against its reorder point; when stock falls to the point, the system raises an order for the economic quantity, adjusted for vendor minimums and truck capacity. "
  "The purchase order states SKU, quantity, cost, delivery date, and ship-to location, and becomes the receiving team's checklist when the truck arrives. "
  "Open orders are tracked until fully received, and late or short shipments trigger follow-up with the vendor.",
  ["The purchase order is the contract: SKU, quantity, cost, date, destination.",
   "Reorder points trigger orders automatically before shelves go empty.",
   "Open orders are tracked to completion; shorts and lates get followed up.",
   "Vendor minimums and freight efficiency shape the final order quantity."],
  ["Accurate on-hand counts and lead-time records per SKU and vendor.",
   "Reorder points and order quantities maintained per SKU.",
   "A vendor file with terms, minimums, and contact information."],
  ["Purchase orders authorized before sending - no verbal-only orders of record.",
   "Cost changes confirmed in writing before the order ships.",
   "Receiving matched to the PO before the invoice is approved for payment."],
  ["Retail buying and replenishment procedure guides (public publications).",
   "Uniform Commercial Code provisions on purchase orders (public law)."],
  "eoq", {"D": 5200.0, "S": 85.0, "H": 3.20}),

R("Economic Order Quantity (EOQ)", "Compounded", 15,
  "The economic order quantity is the order size that minimizes the total cost of ordering and holding inventory. "
  "Order too often and ordering costs pile up; order too much and holding costs - the warehouse space, the tied-up cash, the risk of obsolescence - eat the savings. "
  "EOQ finds the sweet spot with a simple square-root formula that buyers have trusted for over a century.",
  "Total cost is the sum of annual ordering cost (orders per year times cost per order) and annual holding cost (average inventory times holding cost per unit). "
  "Because ordering cost falls as order size grows while holding cost rises, the total forms a U-shape, and its minimum sits at EOQ = sqrt(2DS/H), where D is annual demand, S is cost per order, and H is holding cost per unit per year. "
  "Buyers use EOQ as the baseline order quantity, then adjust for vendor minimums, truckloads, and discounts.",
  ["EOQ = sqrt(2 x annual demand x cost per order / holding cost per unit).",
   "Ordering cost falls with bigger orders; holding cost rises - EOQ balances them.",
   "Holding cost includes space, tied-up cash, insurance, and obsolescence risk.",
   "EOQ is the baseline; minimums, trucks, and quantity discounts adjust it."],
  ["Annual demand per SKU, cost per purchase order, and holding cost rate.",
   "A calculator or system that applies the formula per SKU.",
   "Vendor terms: minimums, freight prepaid thresholds, discount breaks."],
  ["Holding cost rate reviewed annually - it drifts with interest rates and rents.",
   "EOQ recomputed when demand, costs, or terms change materially.",
   "Quantity discounts evaluated against EOQ, not blindly accepted."],
  ["F.W. Harris original EOQ model and standard operations texts (public literature).",
   "APICS/ASCM inventory management materials (public publications)."],
  "eoq", {"D": 12000.0, "S": 120.0, "H": 4.50}),

R("Markdowns, Promotions, and Clearance", "Compounded", 16,
  "Markdowns are planned price reductions that move slow or seasonal merchandise; promotions are temporary price events that drive traffic; clearance is the final push to sell remaining stock at any reasonable price. "
  "All three sacrifice margin to gain cash and shelf space, so they must be planned, funded, and measured - never improvised in a panic. "
  "A disciplined markdown cadence (for example 25%, then 50%, then 75% off) trains customers far less than random deep cuts.",
  "The buyer sets a markdown budget for the season as a percentage of sales, then schedules reductions when sell-through lags the plan. "
  "Promotions are calendared with vendor funding, advertised honestly with dates and limits, and executed with full stock and signage. "
  "Clearance gathers remnants in one visible area at final prices; whatever remains after clearance is donated, returned to vendor, or liquidated, and the loss is recorded.",
  ["Markdowns are planned margin investments, not panic price slashing.",
   "A markdown budget, set as a percent of sales, keeps reductions disciplined.",
   "Promotions need funding, advertising, stock, and signage - all four, every time.",
   "Clearance ends the line: sell, donate, return, or liquidate, then record the outcome."],
  ["A markdown budget and an approval level for taking them.",
   "A promotion calendar agreed with vendors and marketing.",
   "Signage and POS updates executed before the event starts."],
  ["Advertised prices honored through the stated dates and limits.",
   "Markdown cadence consistent enough that customers trust everyday prices.",
   "Clearance merchandise clearly marked as final sale where applicable."],
  ["Retail promotion planning literature (public publications).",
   "FTC guides on deceptive pricing and bait advertising (public regulation)."],
  "markdown", {"orig": 120.00, "pct": 40.0}),

R("Planograms and Shelf Space", "Compounded", 17,
  "A planogram is a scale diagram showing exactly which products go on which shelf, in what position and facing count. "
  "It turns shelf space - the most expensive real estate in the store - into a managed asset where every inch earns its keep. "
  "Good planograms put fast sellers at easy reach, give new items a fair trial, and keep the shelf looking abundant without overstocking.",
  "Space planners allocate linear feet by category using sales per foot, then draw each shelf with SKU positions, facings, and capacities derived from days of supply. "
  "The store team sets the shelf to the diagram, reports deviations, and the planogram is re-cut when sales patterns shift or assortments change. "
  "Compliance is audited by walking the aisle with the diagram in hand: the shelf should match the picture.",
  ["A planogram is the shelf's blueprint: SKU, position, facings, capacity.",
   "Space goes to sales per foot - earn the inch or lose it.",
   "Eye level and end caps are premium positions assigned deliberately.",
   "Compliance audits keep the real shelf matched to the diagram."],
  ["Sales-per-foot data by category and SKU.",
   "Planogram software or disciplined manual diagrams.",
   "A reset schedule and a trained set crew."],
  ["Set shelves match the approved planogram within tolerance.",
   "New-item trial space protected for the full trial period.",
   "Safety: no unstable stacking, clear sightlines, accessible reach ranges."],
  ["Retail space-planning literature (public publications).",
   "ADA reach-range guidance for merchandise displays (public regulation)."],
  "sellthru", {"received": 12000, "sold": 9840}),

R("E-commerce Operations", "Compounded", 18,
  "E-commerce operations are everything behind the buy button: the website or app, the product content, the shopping cart, payment, fraud screening, picking, packing, and shipping. "
  "Unlike a store where the customer does the picking, online the retailer does it - which makes fulfillment accuracy and shipping speed the core of the customer experience. "
  "A strong e-commerce operation treats the website as a store that never closes and the warehouse as its back room.",
  "Shoppers browse catalog pages with accurate images, descriptions, and live inventory; the cart and checkout collect payment securely and screen for fraud. "
  "Orders flow to the fulfillment center, where pickers gather items, packers box them to survive transit, and carriers take them for last-mile delivery with tracking the customer can follow. "
  "Customer service handles the where-is-my-order questions with the same tracking the warehouse sees.",
  ["Online, the retailer does the picking - fulfillment accuracy is the experience.",
   "Product content (images, descriptions, live inventory) is the digital shelf.",
   "Checkout must be secure, fast, and fraud-screened.",
   "Tracking from warehouse to doorstep is now a baseline expectation."],
  ["An e-commerce platform with catalog, cart, and secure checkout.",
   "A fulfillment node (warehouse or store) with pick, pack, and ship capability.",
   "Carrier contracts covering the delivery promise made at checkout."],
  ["Charged prices match the website's displayed prices at time of order.",
   "Customer data protected; card data never stored in the clear.",
   "Delivery promises kept or proactively communicated when they slip."],
  ["E-commerce operations literature (public publications).",
   "PCI Data Security Standard for online card processing (public standard)."],
  "basket", {"txns": 5400, "items": 11880, "revenue": 324500.0}),

R("Omnichannel Fulfillment", "Compounded", 19,
  "Omnichannel fulfillment lets the customer buy however they like and receive however they like: buy online pick up in store, buy online ship from store, buy in store ship to home. "
  "It treats every store and warehouse as one shared pool of inventory visible to every selling channel. "
  "Done well, it turns the store fleet into a distributed fulfillment network that beats pure e-commerce on speed.",
  "A single order-management system sees inventory across all nodes and routes each order line to the best source by proximity, stock, and cost. "
  "Store teams pick online orders from shelves with handheld devices, pack at a dedicated station, and hand to carriers or hold for customer pickup with notification. "
  "Service levels are measured per node - pick accuracy, pick time, and on-time handoff - so weak nodes get coaching instead of excuses.",
  ["One inventory pool visible to every channel; the system routes each order line optimally.",
   "Buy online, pick up in store and ship-from-store turn stores into fulfillment nodes.",
   "A single order-management system decides the sourcing per line.",
   "Node-level metrics (accuracy, speed) keep every location honest."],
  ["Real-time inventory visibility across stores and warehouses.",
   "An order-management system with sourcing rules.",
   "In-store pick/pack stations and trained fulfillment staff."],
  ["Pickup orders ready within the promised window, verified by ID at handoff.",
   "Substitutions only with customer consent where offered.",
   "Online prices and promotions honored consistently across fulfillment paths."],
  ["Omnichannel retail operations literature (public publications).",
   "Industry benchmarks for BOPIS and ship-from-store service levels (public reports)."],
  "turnover", {"cogs": 5100000.0, "avg_inv": 720000.0}),

R("Warehousing and Distribution Centers", "Compounded", 20,
  "Warehouses and distribution centers are the retailer's back room at scale: buildings that receive bulk goods from suppliers, store them, and ship store-ready quantities on schedule. "
  "A distribution center serving a chain may move millions of units a week through receiving docks, storage racks, and outbound staging. "
  "Efficiency here - measured in cost per unit handled - flows straight to shelf prices.",
  "Inbound trucks are scheduled to docks, unloaded, and checked against purchase orders; goods are put away into rack locations recorded by the warehouse management system. "
  "Outbound waves pick store orders - by case, by pallet, or by eaches - consolidate them by route, and load trailers on the delivery schedule. "
  "Cross-dock operations skip storage entirely: inbound goods move straight from receiving to outbound trailers for fast-moving items.",
  ["The warehouse management system knows the location of every pallet and case.",
   "Inbound: schedule, unload, verify, put away. Outbound: wave, pick, consolidate, load.",
   "Cross-docking skips storage for fast movers.",
   "Cost per unit handled is the headline efficiency metric."],
  ["A warehouse management system with directed put-away and picking.",
   "Dock scheduling to avoid truck queues.",
   "Material-handling equipment matched to the building and the product."],
  ["OSHA warehouse safety: racking, forklifts, and pedestrian separation.",
   "Food, drug, and hazmat storage per applicable regulations.",
   "Cycle counts in the warehouse as rigorous as in the store."],
  ["Warehouse management literature (public publications).",
   "OSHA standards for powered industrial trucks and storage (public regulation)."],
  "turnover", {"cogs": 12000000.0, "avg_inv": 1500000.0}),

R("Returns and Reverse Logistics", "Compounded", 21,
  "Returns are merchandise flowing backward: from customer to store to a decision - restock, refurbish, return to vendor, donate, or destroy. "
  "Reverse logistics is the system that handles that backward flow efficiently instead of letting it pile up in a back room. "
  "With return rates far higher online than in stores, this is now a profit center or a profit leak depending on discipline.",
  "The return is accepted under the written policy, inspected and graded, and routed by disposition: resalable goods go back to stock, defective goods go to vendor claims, and the rest flows to refurbishment, donation, or liquidation channels. "
  "Each disposition is recorded so the true cost of returns - refunds, handling, and lost margin - is visible by category. "
  "Fraud patterns like wardrobing and empty-box returns are flagged by the system for review.",
  ["Every return gets a disposition: restock, refurbish, vendor claim, donate, or liquidate.",
   "The true cost of returns is tracked by category, not buried in overhead.",
   "A clear written policy, applied consistently, prevents most return disputes.",
   "Return fraud is detected by pattern, not by accusing honest customers."],
  ["A written return policy with time limits and condition rules.",
   "An inspection and grading station for returned goods.",
   "Disposition channels: restock flow, vendor claims, donation, liquidation."],
  ["Refunds issued to the original payment method within the promised time.",
   "Defective-product returns handled under warranty and safety rules.",
   "Customer data from returns kept secure and never resold."],
  ["Reverse-logistics industry literature (public publications).",
   "State retail return and refund disclosure rules (public regulations)."],
  "markdown", {"orig": 65.00, "pct": 50.0}),

R("Loyalty Programs", "Compounded", 22,
  "Loyalty programs reward repeat customers with points, discounts, or perks, and reward the retailer with identified purchase data and steadier visits. "
  "The economics only work if the lift in visits and basket size exceeds the cost of the rewards plus the cost of running the program. "
  "The best programs feel generous to the member and are ruthlessly measured by the finance team.",
  "Members enroll free, earn points or progress per dollar spent, and redeem for discounts, free items, or experiences at defined thresholds. "
  "The program tracks member versus non-member spend, visit frequency, and basket size to prove incremental lift, while unredeemed points are carried as a liability on the books. "
  "Tiers add aspiration: higher spend unlocks better perks, which concentrates the retailer's best customers even further.",
  ["Loyalty economics: visit and basket lift must exceed reward plus operating cost.",
   "Unredeemed points are a real financial liability, tracked and reported.",
   "Member data proves incrementality: member vs. non-member behavior compared.",
   "Tiers concentrate top customers by rewarding higher spend with better perks."],
  ["A member database with secure, consented personal data.",
   "POS and e-commerce integration so earning is automatic.",
   "Finance tracking of point liability and program ROI."],
  ["Terms disclosed at enrollment: earn rates, expiry, and redemption rules.",
   "Points never expire without the notice the terms promise.",
   "Member data used per the stated privacy policy, never sold silently."],
  ["Loyalty marketing literature on program economics (public publications).",
   "State gift-card and rewards expiry regulations (public regulations)."],
  "loyalty", {"members": 42000, "avg_points": 1250, "point_value": 0.008}),

R("Loss Prevention and Shrink", "Compounded", 23,
  "Shrink is the gap between the inventory the books say the store should have and what is actually there - caused by shoplifting, employee theft, paperwork errors, and vendor fraud. "
  "Loss prevention is the program that shrinks the shrink: deterrence, detection, and investigation across all four causes. "
  "Industry shrink often runs one to two percent of sales, which can exceed the entire net profit of a low-margin retailer.",
  "The program starts by measuring shrink per store and category through counts and exception reporting, then attacks the biggest causes first. "
  "Deterrence includes visible security, locked cases for high-risk items, and well-trained staff; detection uses cameras, electronic article surveillance, and point-of-sale exception reports that flag suspicious voids and discounts. "
  "Investigations follow a written protocol with evidence standards, because a false accusation costs more than the theft.",
  ["Shrink = shoplifting + employee theft + paperwork error + vendor fraud.",
   "Measure shrink per store and category, then attack the biggest cause first.",
   "POS exception reporting catches sweethearting, voids, and discount abuse.",
   "Investigations need evidence standards - false accusations are catastrophic."],
  ["Shrink measurement: regular counts plus exception reporting.",
   "A written investigation protocol and trained investigators.",
   "Deterrence hardware: cameras, EAS tags, locked cases for high-risk SKUs."],
  ["Detentions and interviews follow the law - shopkeeper's privilege has strict limits.",
   "Employee investigations respect labor law and documented due process.",
   "Surveillance signage posted where required."],
  ["Loss-prevention industry surveys on shrink causes (public reports).",
   "State shoplifting detention statutes (public law)."],
  "shrink", {"sales": 8500000.0, "shrink_pct": 1.6}),
]

PUB += [
R("Retail Analytics — Sell-Through and GMROI", "Advanced", 24,
  "Retail analytics turns the flood of POS and inventory data into decisions, and its two workhorse metrics are sell-through and GMROI. "
  "Sell-through is the percentage of received units that sold in a period; GMROI - gross margin return on investment - is how many gross-margin dollars each dollar of inventory investment produced. "
  "Together they answer the buyer's two questions: did customers want it, and did it earn its place in the stockroom.",
  "The analyst pulls units received and units sold per SKU to compute sell-through, flagging slow movers for markdown and fast movers for reorder before they stock out. "
  "GMROI is computed as gross margin dollars divided by average inventory cost; a GMROI of 3.0 means three dollars of margin per dollar invested in stock. "
  "Dashboards track both by department, vendor, and store, and buying plans shift open-to-buy dollars from low-GMROI categories to high ones.",
  ["Sell-through = units sold / units received - the demand signal.",
   "GMROI = gross margin dollars / average inventory cost - the efficiency signal.",
   "Low sell-through triggers markdown or exit; high sell-through triggers reorder.",
   "Open-to-buy dollars flow toward high-GMROI categories."],
  ["Clean POS sales and receiving data per SKU.",
   "An analytics cadence: weekly review, monthly deep dive.",
   "Buyers empowered to act on what the numbers say."],
  ["Metrics defined identically across departments and time periods.",
   "Markdown-influenced sell-through flagged so it is not mistaken for full-price demand.",
   "Inventory valued consistently for GMROI comparability."],
  ["Retail analytics literature on sell-through and GMROI (public publications).",
   "NRF buyer analytics training materials (public publications)."],
  "gmroi", {"gross_margin": 385000.0, "avg_inv_cost": 142000.0}),

R("Market Basket Analysis", "Advanced", 25,
  "Market basket analysis studies which products customers buy together in the same transaction, revealing the natural affinities hidden in millions of receipts. "
  "Classic findings - chips with salsa, paint with brushes - drive cross-merchandising, shelf adjacency, and promotion pairing. "
  "It is the quantitative backbone of the old retailer's instinct that certain items belong near each other.",
  "The analyst mines transaction data for association rules: support (how often the pair occurs), confidence (given A, how often B follows), and lift (how much more often than chance). "
  "Strong rules become actions: place the items adjacently, bundle them in a promotion, or recommend B on the product page when A is in the cart. "
  "Rules are re-mined regularly because affinities shift with seasons, trends, and assortment changes.",
  ["Support, confidence, and lift separate real affinities from coincidence.",
   "Strong rules drive adjacency, bundling, and recommendations.",
   "Affinities shift - re-mine regularly, especially across seasons.",
   "Online, basket analysis powers 'frequently bought together' engines."],
  ["Transaction-level basket data with SKU detail.",
   "Analytical tooling for association-rule mining.",
   "A process turning findings into shelf and promotion actions."],
  ["Correlations treated as hypotheses until tested - coincidence is common.",
   "Customer data anonymized for analysis; no individual targeting without consent.",
   "Promoted bundles priced honestly against the separate items."],
  ["Data-mining literature on association rules (public publications).",
   "Retail analytics case studies on basket affinity (public publications)."],
  "basket", {"txns": 9800, "items": 25480, "revenue": 412300.0}),

R("Category Management", "Advanced", 26,
  "Category management runs a group of related products - say, coffee or laundry detergent - as a mini-business with its own sales, margin, and growth targets. "
  "The category manager owns the assortment, shelf space, pricing, and promotions for the category across stores. "
  "It replaced the old brand-by-brand buying with shopper-centric thinking: the category exists to serve a shopping mission, not a vendor.",
  "The manager analyzes category sales, share, and margin, defines the category's role (destination, routine, seasonal, convenience), and sets the assortment breadth and depth accordingly. "
  "Shelf space follows the planogram by role, promotions are calendared to grow the category rather than just shift share between brands, and scorecards track sales, margin, and shopper satisfaction. "
  "Vendor collaboration - sharing data and planning jointly - is encouraged, with the retailer keeping final authority over the shelf.",
  ["A category is managed as a mini-business with its own P&L targets.",
   "Category roles (destination, routine, seasonal) drive space and assortment.",
   "Promotions should grow the category, not merely shift brand share.",
   "Scorecards track sales, margin, and shopper satisfaction together."],
  ["Category definitions and role assignments, reviewed annually.",
   "Shopper and sales data at category granularity.",
   "A category review calendar with vendor collaboration sessions."],
  ["Shelf decisions documented and free of undisclosed vendor payments.",
   "Category performance reported consistently period to period.",
   "Assortment changes communicated to stores before resets."],
  ["Category management industry literature and role frameworks (public publications).",
   "FTC guidance on slotting and trade promotion practices (public regulation)."],
  "gmroi", {"gross_margin": 210000.0, "avg_inv_cost": 68000.0}),

R("Private Label Development", "Advanced", 27,
  "Private label - the retailer's own brand - turns the store from a reseller of national brands into a brand owner, capturing higher margins and customer loyalty that competitors cannot copy. "
  "Development runs from concept and specification through sourcing, quality control, packaging, and launch. "
  "Strong private labels now compete head-to-head with national brands on quality, not just price.",
  "The retailer identifies a category where its brand can win, writes a product specification matching or beating the national brand, and sources manufacturing through competitive bidding with audited factories. "
  "Quality control tests production against the spec, packaging is designed to the retailer's brand standards, and launch is backed by shelf placement and promotion. "
  "Ongoing, the label is managed like any brand: innovation, quality holds, and margin tracking.",
  ["Private label captures higher margin and non-copyable loyalty.",
   "Specification first: match or beat the national brand on quality.",
   "Audited factories and quality testing protect the retailer's name.",
   "The label is managed as a brand: innovate, hold quality, track margin."],
  ["Category analysis showing where own-brand can win.",
   "Sourcing and quality-assurance capability.",
   "Brand standards for packaging and product claims."],
  ["Product claims on pack verified by testing.",
   "Factory audits covering labor and safety standards.",
   "Recalls handled with the speed of a national brand."],
  ["Private-label industry reports on growth and quality (public reports).",
   "FDA/USDA labeling rules for store-brand food and drug products (public regulations)."],
  "markup", {"cost": 8.40, "price": 21.99}),

R("Supply Chain Management", "Advanced", 28,
  "Supply chain management is the end-to-end orchestration of getting goods from raw material to the customer's hands: sourcing, manufacturing, transportation, warehousing, and last-mile delivery. "
  "In retail it determines in-stock rates, landed cost, and speed to shelf - the three levers that decide whether the right product is available at the right price. "
  "Modern chains balance efficiency with resilience, after years of learning that the cheapest chain can also be the most fragile.",
  "Planners forecast demand, source product globally or domestically, and book transportation across ocean, air, rail, and truck legs with tracked milestones. "
  "Distribution centers receive, store, and forward goods to stores on fixed schedules, while control towers monitor the whole flow for disruptions and reroute around them. "
  "Landed cost - product plus freight plus duty plus handling - is tracked per SKU so sourcing decisions compare true costs.",
  ["The chain runs from raw material to the customer's hands as one system.",
   "In-stock rate, landed cost, and speed are the three headline levers.",
   "Landed cost per SKU enables honest sourcing comparisons.",
   "Resilience - backup suppliers and routes - is designed in, not wished for."],
  ["Demand forecasts feeding procurement and transport planning.",
   "A control-tower view of shipments across all legs.",
   "Supplier scorecards: quality, on-time, cost, and compliance."],
  ["Customs and import duties filed accurately and on time.",
   "Supplier labor and safety standards audited, not assumed.",
   "Disruption plans tested before they are needed."],
  ["Supply-chain management literature (public publications).",
   "U.S. Customs import compliance requirements (public regulations)."],
  "eoq", {"D": 48000.0, "S": 450.0, "H": 6.80}),

R("Labor Scheduling and Workforce Management", "Advanced", 29,
  "Labor scheduling puts the right number of trained people in the right place at the right time - enough to serve customers and stock shelves, not so many that payroll devours margin. "
  "Workforce management adds hiring, training, timekeeping, and performance to the scheduling core. "
  "Labor is typically a retailer's largest controllable expense, so scheduling discipline shows up directly in profit.",
  "Traffic counters and sales history forecast customer demand by hour; labor standards translate that demand into required hours by task - registers, floor service, receiving, and stocking. "
  "Schedules are built to the forecast, published in advance, and adjusted for callouts and volume swings, with timekeeping feeding payroll accurately. "
  "Overtime is monitored as the early warning: chronic overtime means the base schedule is understaffed.",
  ["Schedule to forecasted customer demand, not to habit or preference.",
   "Labor standards convert traffic and tasks into required hours.",
   "Published-in-advance schedules plus a fair adjustment process.",
   "Chronic overtime signals an understaffed base schedule."],
  ["Traffic and sales history by hour for forecasting.",
   "Labor standards per task and a scheduling system.",
   "Timekeeping integrated with payroll."],
  ["Wage, hour, break, and overtime law compliance in every schedule.",
   "Minor-work rules observed for young employees.",
   "Schedule-change notice given per applicable predictive-scheduling rules."],
  ["Workforce management literature for retail (public publications).",
   "Department of Labor wage-and-hour rules (public regulations)."],
  "breakeven", {"fixed": 42000.0, "price": 18.50, "varcost": 7.80}),

R("Site Selection and Store Real Estate", "Advanced", 30,
  "Site selection is choosing where stores live: the market, the trade area, the exact corner, and the lease terms. "
  "A great operator in a bad location fights uphill forever, while a good location forgives many mistakes. "
  "Retailers analyze demographics, traffic, competition, and co-tenancy before signing, because a lease is a ten-year bet.",
  "Analysts define the trade area, count rooftops and daytime population, measure traffic counts and visibility, and map competitors and complementary tenants. "
  "Sales forecasting models - gravity models or analog-based - estimate the site's revenue; rent, build-out, and operating costs are weighed against it. "
  "Leases are negotiated on rent structure, term, exclusivity, co-tenancy clauses, and exit options before the bet is placed.",
  ["Location quality compounds: good sites forgive mistakes, bad sites punish excellence.",
   "Trade-area analysis: rooftops, traffic, competition, co-tenancy.",
   "Analog and gravity models forecast site revenue before signing.",
   "The lease is a multi-year bet - negotiate term, rent, and exit carefully."],
  ["Demographic, traffic, and competitor data for candidate markets.",
   "A sales-forecasting model calibrated on existing stores.",
   "Real-estate and legal review of every lease."],
  ["Zoning, signage, and permitting verified before commitment.",
   "Accessibility and parking requirements confirmed.",
   "Environmental checks on the site before build-out."],
  ["Retail real-estate site-selection literature (public publications).",
   "Local zoning and signage ordinances (public regulations)."],
  "breakeven", {"fixed": 310000.0, "price": 42.00, "varcost": 16.50}),

R("RFID and Store Automation", "Advanced", 31,
  "RFID - radio-frequency identification - gives every item a radio-readable tag, letting a store count an entire department in minutes instead of hours. "
  "Store automation extends the idea: electronic shelf labels, self-checkout, automated replenishment alerts, and robots that scan shelves for gaps. "
  "Together they attack retail's oldest costs: counting, pricing labor, and empty shelves.",
  "Each item carries an RFID tag encoded with its EPC number; handheld or fixed readers sweep the floor and reconcile tag reads against the inventory file in near real time. "
  "Electronic shelf labels update prices from the pricing file at the push of a button, and shelf-scanning robots report out-of-stocks and misplaced items for the team to fix. "
  "Accuracy gains feed every other system: replenishment, online availability promises, and shrink detection all improve when the count is right.",
  ["RFID counts whole departments in minutes with near-real-time accuracy.",
   "Electronic shelf labels push price changes instantly from the file.",
   "Shelf robots find out-of-stocks and misplaced items automatically.",
   "Accurate counts lift replenishment, online promises, and shrink control."],
  ["Tagged merchandise (source-tagged by vendors or applied in-house).",
   "Readers, software, and integration with the inventory system.",
   "A change plan: automation shifts labor, it does not simply erase it."],
  ["RFID data used for inventory, not for tracking customers without notice.",
   "Electronic labels match the POS price file at all times.",
   "Automation safety: robots and equipment rated for public spaces."],
  ["GS1 EPC/RFID standards for retail tagging (public standard).",
   "Retail automation case-study literature (public publications)."],
  "shrink", {"sales": 12000000.0, "shrink_pct": 1.1}),

R("Seasonal Planning and Open-to-Buy", "Advanced", 32,
  "Seasonal planning maps the retail year - back-to-school, holiday, spring - into assortments, promotions, and staffing, months before each season arrives. "
  "Open-to-buy is the financial control that keeps seasonal buying honest: the budgeted dollars available to purchase merchandise after accounting for what is already owned or ordered. "
  "Without open-to-buy, seasonal enthusiasm becomes January's clearance disaster.",
  "Planners set seasonal sales, margin, and inventory targets by month, then compute open-to-buy as planned purchases minus goods already received and on order. "
  "Buyers spend only within their open-to-buy, reserving a portion for in-season reorders of proven winners. "
  "Post-season reviews compare plan to actual on sales, margin, and leftover inventory, and the lessons reshape next year's plan.",
  ["Open-to-buy = planned purchases minus on-hand minus on-order: the spending limit.",
   "Seasonal plans set sales, margin, and inventory targets by month.",
   "Reserve part of open-to-buy for in-season chase of winners.",
   "Post-season review turns this year's leftovers into next year's wisdom."],
  ["A seasonal sales and inventory plan by month.",
   "Open-to-buy reporting refreshed as receipts and orders post.",
   "Buyer discipline: no spending beyond open-to-buy without approval."],
  ["Seasonal hiring and layoff plans communicated honestly and legally.",
   "Clearance plans for seasonal remnants set before the season starts.",
   "Vendor dating and return terms negotiated for seasonal risk-sharing."],
  ["Retail seasonal planning literature (public publications).",
   "Open-to-buy methodology in buyer training manuals (public publications)."],
  "markdown", {"orig": 150.00, "pct": 60.0}),

R("Franchise Operations", "Advanced", 33,
  "Franchising lets a retailer expand through owner-operators: the franchisor provides the brand, systems, and support, and the franchisee invests capital and runs the local store. "
  "It is expansion with other people's money and local owner energy, in exchange for sharing control and profit. "
  "The franchise agreement is the constitution of the relationship, and the operations manual is its daily law.",
  "The franchisor documents every process - site criteria, build-out, training, products, pricing guidance, marketing, and quality audits - in an operations manual the franchisee follows. "
  "Franchisees pay an initial fee plus ongoing royalties and marketing contributions, and the franchisor supports them with training, supply chain access, and field consultants. "
  "Compliance is monitored through audits and customer feedback; consistent execution protects the brand every location shares.",
  ["The franchisor supplies brand, systems, and support; the franchisee supplies capital and local operation.",
   "The operations manual standardizes execution across all locations.",
   "Royalties and marketing funds sustain the shared brand.",
   "Audits protect the brand every franchisee shares."],
  ["A proven, documented, replicable store operating system.",
   "Franchise disclosure documents prepared per legal requirements.",
   "Training, supply chain, and field support for franchisees."],
  ["Franchise disclosure and registration per applicable franchise law.",
   "No earnings claims without the substantiation the law requires.",
   "Brand standards enforced evenly - favoritism destroys trust."],
  ["FTC Franchise Rule on disclosure documents (public regulation).",
   "International Franchise Association educational materials (public publications)."],
  "breakeven", {"fixed": 95000.0, "price": 32.00, "varcost": 12.40}),

R("Retail Mastery Review — Running the Whole Operation", "Advanced", 34,
  "The mastery review binds the whole ladder into one operating picture: the retailer as a system where catalog, pricing, inventory, stores, e-commerce, people, and analytics move together. "
  "Each earlier record is a gear; this record is the gearbox, showing how the gears mesh. "
  "A master retailer reads the business the way a pilot reads instruments: every gauge meaningful, every gauge connected.",
  "Start from the customer and work backward: the assortment and price that earn the visit, the inventory that keeps the promise, the staff and systems that deliver it, and the analytics that prove it worked. "
  "Run the weekly rhythm - sales review, inventory actions, price and promotion checks, labor alignment - and the seasonal rhythm - plans, open-to-buy, events, reviews. "
  "Measure what matters: sales growth, margin, GMROI, in-stock, shrink, and customer return rate, and let every decision move at least one of them.",
  ["The retailer is one system: assortment, price, inventory, people, and analytics move together.",
   "Work backward from the customer to every operational decision.",
   "Run the weekly rhythm and the seasonal rhythm without fail.",
   "Six gauges: sales growth, margin, GMROI, in-stock, shrink, return rate."],
  ["Fluency in every record of this database, foundations through advanced.",
   "A weekly operating cadence owned by store and buying leadership.",
   "Honest metrics reviewed together, never in isolation."],
  ["Customer promises - price, availability, returns - kept as stated.",
   "Employee treatment lawful and fair at every level.",
   "Financial reporting accurate and complete."],
  ["Retail management capstone literature (public publications).",
   "National Retail Federation operational benchmarks (public reports)."],
  "gmroi", {"gross_margin": 920000.0, "avg_inv_cost": 265000.0}),
]


SIG = [
R("What Retail Commerce Is — The Signature View", "Foundations", 1,
  "The Signature view of retail commerce starts from a vow: the store is a covenant between the keeper of goods and the people they serve. "
  "Every shelf is a promise kept in public, every price a word that must hold, every return an oath honored without argument. "
  "This edition reframes the full retail ladder as Signature science - the same operations, sworn to a higher standard of keeping faith with the customer.",
  "Where the public edition teaches the mechanics of buying and selling, the Signature edition teaches the discipline behind them: the catalog as a sworn registry, the price as a covenant, the inventory as a trust. "
  "Each record pairs the operational truth with its Signature seal - the practice that makes the operation worthy of the customer's return. "
  "Nothing here is presented as public record; it is his original method, labeled Signature-made throughout.",
  ["The store is a covenant: goods kept faithfully, prices spoken truly.",
   "Every operation in this edition carries a Signature seal - the discipline beneath the mechanics.",
   "The customer's return visit is the signature on the covenant.",
   "Signature-made throughout: an original method, never presented as public record."],
  ["Willingness to hold every price, policy, and promise as sworn.",
   "The public edition alongside for the operational mechanics.",
   "A store or project where the method can be practiced."],
  ["No Signature claim presented as public or official record.",
   "Customer promises kept exactly as stated.",
   "The method taught as his original system, plainly labeled."],
  ["The public edition of this database, for the operational mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "basket", {"txns": 8500, "items": 22100, "revenue": 187450.0}),

R("The Sworn SKU Registry", "Foundations", 2,
  "In the Signature method the SKU is not a number but a sworn identity: each distinct item registered once, described truly, and never duplicated or reused. "
  "The catalog becomes a registry of oaths - one record per real variant, retired with honor when its selling life ends, its history preserved. "
  "A registry kept this way cannot lie about what the store owns.",
  "New items are sworn in with a unique number, a plain true description, cost, and price, witnessed by the buying record. "
  "Every sale, receipt, return, and markdown references the sworn number, so the count is always traceable to events. "
  "Duplicates are merged by ceremony, not silently: the surviving number keeps the history, the retired number is sealed in the archive.",
  ["One sworn number per real variant - identity, not just numbering.",
   "The registry never lies: every count traces to recorded events.",
   "Retired SKUs are sealed with history intact, never deleted.",
   "Duplicates resolved openly, the surviving number keeping the lineage."],
  ["A numbering scheme treated as permanent identity.",
   "Description standards written as registry law.",
   "A retirement rite: archive, do not delete."],
  ["No number ever reused for a different item.",
   "Cost and price changes logged with date and witness.",
   "Registry audits on a fixed rotation."],
  ["The public edition catalog record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "markup", {"cost": 18.50, "price": 42.00}),

R("Seals of Identity — Barcodes in the Signature Method", "Foundations", 3,
  "The Signature method treats the barcode as the item's seal: a machine-readable mark that binds the physical good to its sworn registry identity. "
  "A clean scan is a true reading; a failed scan is the seal refusing to speak, and the method honors the refusal rather than forcing a guess. "
  "Standard numbering is the common tongue that lets every seal be read anywhere.",
  "Numbers are issued under the global standard with computed check digits, printed to scan on the first pass. "
  "At the register the seal is read, the registry answers with the SKU and its filed price, and the sale is recorded against the sworn identity. "
  "Unscannable items are keyed only with verification, and the damaged seal is reported, not hidden.",
  ["The barcode is the item's seal binding it to its registry identity.",
   "A failed scan is information - verify, never guess.",
   "Standard numbers let every seal speak in every store.",
   "The seal identifies; the registry sets the price."],
  ["Standard-issued numbers with computed check digits.",
   "Print quality that scans first pass, every pass.",
   "A verification routine for items whose seals will not read."],
  ["No invented numbers on products bound for other retailers shelves.",
   "Damaged seals reported and reissued, not worked around silently.",
   "Price file accuracy audited against scanned seals."],
  ["GS1 identification standards as the common tongue (public standard).",
   "The public edition barcode record, for the mechanical standard (this system)."],
  "markup", {"cost": 2.10, "price": 4.99}),

R("The Pricing Covenant", "Foundations", 4,
  "In the Signature method a price is a covenant spoken aloud on the tag: this is what the good is worth here, and the word will hold. "
  "Everyday prices are set to sustain the store honestly; promotional prices are temporary vows with stated dates, funded before they are spoken. "
  "A covenant broken - two prices for one item - breaks the customer's trust, which is the store's true capital.",
  "Cost and target margin set the candidate price; the covenant then adjusts it to the market position - honest value, fair premium, or opening offer - and rounds it to a speakable number. "
  "Promotions are calendared with funding secured, advertised with dates and limits, and the everyday price restored on schedule. "
  "Shelf, register, and website speak the same price at all times, because a covenant cannot contradict itself.",
  ["A price is a covenant: spoken on the tag, held at the register.",
   "Promotions are temporary vows - dated, funded, and restored on schedule.",
   "Shelf, register, and web speak one price; contradiction breaks trust.",
   "Margin must sustain the store honestly - no covenant survives a bankrupt keeper."],
  ["Cost and margin truth for every SKU before pricing.",
   "A promotion calendar with funding secured in advance.",
   "One pricing file feeding every customer-facing surface."],
  ["Ticketed price equals charged price, always.",
   "Promotional terms stated plainly and honored fully.",
   "No price spoken that the store cannot sustain."],
  ["The public edition pricing record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "markup", {"cost": 32.00, "price": 79.99}),

R("The Point of Sale as Witness", "Foundations", 5,
  "The Signature method names the POS the witness: it sees every sale, records every tender, and testifies in the daily close. "
  "A witness must be impartial - the same price for every customer, every discount logged, every void explained. "
  "When the witness is trusted, the whole store's numbers can be believed.",
  "Each sale is scanned and ticketed line by line from the filed price; tender is taken by the customer's chosen means and recorded exactly. "
  "The witness decrements the registry counts as goods leave and writes every event to the journal with operator and time. "
  "At close the witness is cross-examined: counted cash against journal, card batches against settlement, discrepancies investigated before rest.",
  ["The POS is the impartial witness to every sale and tender.",
   "Same price for every customer; every exception logged with reason.",
   "The journal is testimony - complete, timestamped, attributable.",
   "The daily close is the cross-examination: verify before rest."],
  ["A current price file the witness reads without improvisation.",
   "Tender capability for every payment the store accepts.",
   "A close routine performed without skipping, every day."],
  ["Voids and discounts carry operator ID and reason.",
   "Cash counts reconciled to the journal daily.",
   "Card data protected under the standing security standard."],
  ["The public edition POS record, for the mechanical standard (this system).",
   "PCI Security Standards for card data (public standard)."],
  "basket", {"txns": 1240, "items": 3720, "revenue": 48620.0}),

R("The Honest Till — Cash in the Signature Method", "Foundations", 6,
  "Cash in the Signature method is handled as a trust held in the hand: counted coming in, counted going out, and every movement attributable to a person. "
  "The till keeper's honor is measured in the close - does the money match the testimony of the witness. "
  "Shortages are confessed and investigated; overages are confessed too, for an unexplained overage is a mystery, not a gift.",
  "Registers open with a counted float witnessed and logged; every cash event during the day carries the operator's mark. "
  "Card settlements are matched batch to bank, fees noted openly as the cost of the convenience. "
  "At close the count is laid against the journal, variances pursued to their cause, and the day's cash secured for the bank run.",
  ["Cash is a trust: counted in, counted out, every movement attributable.",
   "Overages confessed like shortages - mysteries are not gifts.",
   "Card batches matched to bank settlement, fees noted openly.",
   "The close is daily and never skipped."],
  ["A float policy, a drop policy, and a deposit schedule in writing.",
   "Secure storage for cash during and after the day.",
   "Card settlement reconciliation as routine as the cash count."],
  ["Large cash movements counted by two where practical.",
   "Deposits on schedule; accumulation past the safe limit forbidden.",
   "Card data never written down or stored in the open."],
  ["The public edition cash-handling record, for the mechanical standard (this system).",
   "PCI Data Security Standard for card handling (public standard)."],
  "breakeven", {"fixed": 18500.0, "price": 24.99, "varcost": 11.20}),

R("The Pilgrim's Path — Store Layout in the Signature Method", "Foundations", 7,
  "The Signature method lays the store as a pilgrim's path: the customer enters, is welcomed in the open threshold, and is guided past the store's best offerings to the registers without confusion or crush. "
  "Every zone has a purpose, every aisle a readable width, every department a sign that orients the stranger. "
  "The path honors the customer's time - the one thing they cannot get back.",
  "Destination goods rest deep in the store so the journey passes the full offering; impulse goods wait near the registers where the path naturally slows. "
  "The entrance threshold stays open - no barrier greets the pilgrim - and registers sit where their queues trouble no aisle. "
  "The layout is walked as a customer walks it, and whatever confuses the walker is redrawn.",
  ["The store is a path: welcomed entry, guided journey, graceful exit.",
   "The threshold stays open - the customer is a guest, not an intruder.",
   "Destination goods deep, impulse goods where the path slows.",
   "Walk the path as a stranger; redraw whatever confuses."],
  ["A measured plan with selling and service zones marked.",
   "Signage legible from the main path.",
   "Aisles fit carts, wheelchairs, and two-way passage."],
  ["Exits and fire aisles clear at all times.",
   "Accessible routes per the standing access rules.",
   "Occupancy limits posted and honored."],
  ["The public edition layout record, for the mechanical standard (this system).",
   "ADA accessibility guidelines for retail facilities (public regulation)."],
  "sellthru", {"received": 2400, "sold": 1875}),

R("The True Count — Inventory in the Signature Method", "Foundations", 8,
  "The Signature method calls inventory accuracy a matter of truth: the registry says what the store holds, and the count proves it. "
  "Cycle counting is the daily practice of truth-telling - small sections verified in rotation so error never compounds into fiction. "
  "A store that knows its true count can promise availability and keep the promise.",
  "Sections rotate through the count schedule; counters tally each SKU and lay the tally against the registry. "
  "Variances beyond tolerance are investigated to cause - damage, theft, mis-receipt, error - and only then adjusted, with the reason recorded. "
  "High-trust goods - the valuable and the vanishing - are counted most often, for truth matters most where loss hurts most.",
  ["The count is truth-telling: registry against reality, on rotation.",
   "Variances investigated to cause before any adjustment.",
   "Adjustments carry reasons; unexplained changes are forbidden.",
   "Count most often where value and risk are highest."],
  ["A rotation schedule covering the whole store.",
   "Tally tools and written tolerance rules.",
   "Reason codes for every adjustment."],
  ["Counters independent of stockers where staffing allows.",
   "Manager review before adjustments post.",
   "A full physical count annually to re-anchor truth."],
  ["The public edition inventory record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "turnover", {"cogs": 920000.0, "avg_inv": 184000.0}),

R("The Receiving Oath", "Foundations", 9,
  "Receiving in the Signature method is an oath taken at the back door: what was ordered is what arrived, in the quantity and condition promised, or the shortfall is declared on the spot. "
  "The receiver is the store's first guardian - goods pass their inspection before they may be sold. "
  "Nothing unverified reaches the shelf.",
  "Delivery is checked line by line against the purchase order while the driver waits; damages and shorts are written on the receipt before signatures. "
  "Verified goods post to the registry the same day and flow to their planogram homes, labels forward; overstock takes labeled back-room quarters. "
  "Damaged goods are segregated and claimed - never shelved, never hidden.",
  ["The back door is a gate: verify before anything enters the selling floor.",
   "Shorts and damages declared on the receipt, in the driver's presence.",
   "Same-day posting: the registry learns what arrived today.",
   "Damaged goods segregated and claimed, never shelved."],
  ["The purchase order at the door for every delivery.",
   "A written receiving routine: check, declare, sign, post.",
   "Labeled back-room quarters for overstock."],
  ["Delivery receipts kept as evidence for invoice disputes.",
   "Safe lifting practice for heavy goods.",
   "No unverified merchandise on the selling floor."],
  ["The public edition receiving record, for the mechanical standard (this system).",
   "OSHA material-handling guidance (public regulation)."],
  "sellthru", {"received": 5000, "sold": 4350}),

R("The Guest Law — Service in the Signature Method", "Foundations", 10,
  "The Signature method's guest law is simple: every customer is a guest under the store's roof, and guests are acknowledged, heard, and helped. "
  "Complaints are treated as messages from the field - logged, studied, and answered with fixes, not excuses. "
  "Returns are the covenant's test: the store that takes back gracefully is believed the next time it sells.",
  "Staff acknowledge every guest promptly, listen the complaint out before solving, and own the problem to resolution. "
  "The return policy is written plainly and applied evenly; every return is logged with its reason so patterns rise to the surface. "
  "Common problems are solved on the spot by empowered staff - the guest should not have to climb a hierarchy to be made whole.",
  ["Every customer a guest: acknowledged, heard, helped.",
   "Complaints are field messages - log them, fix the cause.",
   "Returns are the covenant's test; handle them gracefully.",
   "Empower the front line to make guests whole on the spot."],
  ["A guest law every employee can recite and practice.",
   "Product knowledge deep enough for honest advice.",
   "A complaint log reviewed weekly, with fixes assigned."],
  ["Return terms disclosed before sale where required.",
   "Guest data taken only with consent and guarded.",
   "Service accessible to guests with disabilities."],
  ["The public edition service record, for the mechanical standard (this system).",
   "FTC guidance on advertising and return disclosures (public regulation)."],
  "basket", {"txns": 3200, "items": 7040, "revenue": 89200.0}),

R("The Art of the Display — Signature Merchandising", "Foundations", 11,
  "Signature merchandising is display as hospitality: the store arranges its goods the way a host sets a table - with care, abundance, and pride. "
  "The focal item takes the honored place at eye level; coordinating goods gather around it like guests at the feast. "
  "A display kept full, faced, and priced tells the customer the keeper cares.",
  "Displays are built around the season's promise, grouped so the customer sees complete solutions, and signed so plainly a hurried stranger understands in three seconds. "
  "End caps and windows carry the current vow - the promotion or the season - and every display is walked daily: restocked, straightened, repriced where the covenant changed. "
  "What is displayed is what is sold; the display never promises what the registry cannot deliver.",
  ["Display is hospitality: arrange goods as a host sets a table.",
   "The honored place - eye level - goes to the season's promise.",
   "Group solutions, not just items: show the whole outfit, the whole project.",
   "Walk every display daily; the store should always look newly opened."],
  ["A display calendar bound to seasons and promotions.",
   "Signage standards: price and offer legible at a glance.",
   "Back stock sufficient to keep displays abundant."],
  ["Structures stable and safe, especially for children.",
   "Displayed prices equal to the price file.",
   "Aisles and exits never blocked."],
  ["The public edition merchandising record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "markdown", {"orig": 89.99, "pct": 25.0}),

R("Signature Retail Math — Markup and Margin", "Foundations", 12,
  "Signature retail math begins where all honest trade begins: knowing exactly what each sale earns. "
  "Markup on cost and margin on price are the two lenses; the method demands fluency in both, for a keeper who confuses them will slowly trade at a loss while believing in profit. "
  "Every covenant price in this method is set with open eyes on both numbers.",
  "From cost and price the keeper derives markup dollars and percent-on-cost, margin dollars and percent-on-price, and checks the margin against the department's sworn target. "
  "To hit a target margin the price is worked backward - cost divided by one minus the margin rate - and rounding is checked so it never dips below the vow. "
  "Markdowns are reckoned on price, like margin, and every promotion's funded margin is known before the first sign is hung.",
  ["Markup is figured on cost; margin on price - never confuse the lenses.",
   "Price = cost / (1 - margin rate) aims any target from cost.",
   "Rounding checked: never below the sworn margin.",
   "Promotion margin funded and known before the event."],
  ["True cost and filed price for every SKU.",
   "A sworn margin target per department.",
   "Fluency - or a calculator - at every pricing hand."],
  ["Margin definitions consistent across all reports.",
   "No price spoken below cost without a planned, funded reason.",
   "Markdown math reckoned on price, documented per event."],
  ["The public edition retail-math record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "markup", {"cost": 45.00, "price": 90.00}),
]

SIG += [
R("Foreseeing Demand — The Signature View", "Compounded", 13,
  "The Signature method treats forecasting as foresight with humility: study the past honestly, weigh the season, name the coming events, and then admit what you cannot know. "
  "The forecast is a sworn estimate, not a prophecy - documented with its reasons, measured afterward, and improved by its errors. "
  "A keeper who studies their misses forecasts better than one who celebrates their hits.",
  "History per SKU is laid out, season and trend marked, and known drivers - promotions, holidays, weather, local happenings - layered in openly. "
  "The statistical baseline is then adjusted by human judgment for what numbers cannot see, and the whole estimate is written down with its assumptions. "
  "After the period, actual is set against forecast, the error studied without blame, and the method sharpened.",
  ["Forecast with humility: a sworn estimate, never a prophecy.",
   "Assumptions written down; errors studied without blame.",
   "Human judgment covers what the model cannot see.",
   "Every miss is tuition for the next forecast."],
  ["Clean history per SKU and a calendar of known drivers.",
   "A written accuracy measure tracked over time.",
   "Judgment reviewers who know the local ground."],
  ["Forecasts presented with their uncertainty, not as certainties.",
   "Safety stock sized from measured error.",
   "No forecast used to punish; used to learn."],
  ["The public edition forecasting record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "turnover", {"cogs": 2400000.0, "avg_inv": 400000.0}),

R("The Ordering Discipline", "Compounded", 14,
  "In the Signature method every purchase order is a sworn request: these goods, this many, by this date, at this cost - written, authorized, and traceable. "
  "Replenishment is the discipline of never letting the registry lie empty while never drowning it in excess. "
  "The ordering hand is steady: triggered by true counts, sized by true demand.",
  "Reorder points stand guard over each SKU; when the count falls to the point, the order rises for the economic quantity, shaped by vendor minimums and honest freight sense. "
  "The purchase order names everything - SKU, quantity, cost, date, destination - and becomes the receiving oath's checklist. "
  "Open orders are watched to completion; the late and the short are pursued, not forgotten.",
  ["Every order written, authorized, and traceable - no verbal ghosts.",
   "Reorder points guard the shelf; the count triggers, not habit.",
   "The PO is the receiving oath's checklist.",
   "Late and short shipments pursued to resolution."],
  ["True counts and honest lead times per SKU and vendor.",
   "Maintained reorder points and order quantities.",
   "A vendor file with terms and contacts."],
  ["No order sent without authorization.",
   "Cost changes confirmed in writing before shipment.",
   "Invoices paid only against matched receipts."],
  ["The public edition purchasing record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "eoq", {"D": 5200.0, "S": 85.0, "H": 3.20}),

R("The Balanced Order — Signature EOQ", "Compounded", 15,
  "The Signature method honors the economic order quantity as the balanced order: the size where the cost of ordering and the cost of holding meet in equilibrium. "
  "To order constantly is to waste motion; to order massively is to bury cash in the back room. "
  "The square root finds the balance point that neither extreme can see.",
  "Annual demand, cost per order, and holding cost per unit are gathered honestly - holding cost counting space, tied cash, insurance, and the risk of decay. "
  "EOQ = sqrt(2DS/H) sets the baseline; the keeper then tempers it with vendor minimums, truck sense, and true discount math. "
  "When demand or costs shift, the balance is recomputed - a stale EOQ is a broken compass.",
  ["The balanced order: ordering cost and holding cost in equilibrium.",
   "Holding cost counted fully - space, cash, insurance, decay.",
   "EOQ is the baseline; minimums and true discounts temper it.",
   "Recompute when the ground shifts; a stale EOQ misleads."],
  ["Honest annual demand, order cost, and holding rate per SKU.",
   "The formula applied per SKU, not guessed.",
   "Vendor terms: minimums, freight thresholds, discount breaks."],
  ["Holding rate reviewed yearly against interest and rents.",
   "Discounts accepted only when they beat the balanced order.",
   "Assumptions documented with each computation."],
  ["The public edition EOQ record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "eoq", {"D": 12000.0, "S": 120.0, "H": 4.50}),

R("The Honorable Reduction — Markdowns in the Signature Method", "Compounded", 16,
  "The Signature method treats markdowns as honorable reductions: the keeper admits the goods did not move as hoped and lowers the covenant openly, by plan, within budget. "
  "Panic slashing trains customers to wait; a disciplined cadence trains them to trust the everyday price. "
  "Clearance is the final honorable act - the goods go to someone who wants them rather than rotting in the back.",
  "A markdown budget is sworn as a percent of sales; reductions follow the cadence when sell-through lags the plan. "
  "Promotions are calendared with funding secured and advertised with honest dates and limits, executed with full stock and true signage. "
  "Clearance gathers the remnants visibly at final prices; the remainder is donated, vendor-returned, or liquidated, and the outcome recorded without shame.",
  ["Reductions by plan and budget, never by panic.",
   "A steady cadence protects trust in the everyday price.",
   "Every promotion: funding, dates, stock, signage - all four.",
   "Clearance completes the line honorably; outcomes recorded."],
  ["A sworn markdown budget and clear approval levels.",
   "A promotion calendar agreed with vendors.",
   "Execution discipline: signs and systems before the doors open."],
  ["Advertised terms honored through their stated dates.",
   "Final-sale terms marked plainly where they apply.",
   "No fake was-prices; the reduction must be real."],
  ["The public edition markdown record, for the mechanical standard (this system).",
   "FTC guides on deceptive pricing (public regulation)."],
  "markdown", {"orig": 120.00, "pct": 40.0}),

R("The Measured Shelf — Signature Planograms", "Compounded", 17,
  "The Signature method measures the shelf as sacred ground: every inch diagrammed, every position earned by sales, every facing a deliberate choice. "
  "The planogram is the shelf's sworn map - and the store keeps its oath by setting the shelf to match the map. "
  "Space is the store's dearest asset; the method refuses to waste it on sentiment.",
  "Feet are allocated by category on sales per foot; each shelf is drawn with SKU, position, facings, and capacity from days of supply. "
  "Fast sellers take the easy reach, new items receive their fair trial ground, and the set crew builds to the diagram. "
  "Audits walk the aisle with map in hand; the shelf must match the picture, or the deviation must have a reason.",
  ["The shelf is sacred ground: diagrammed, earned, deliberate.",
   "Space follows sales per foot - earn the inch or yield it.",
   "Set to the map; audit with map in hand.",
   "New items granted fair trial ground for the full trial."],
  ["Sales-per-foot truth by category and SKU.",
   "Diagramming discipline, by software or by hand.",
   "A reset rhythm and a trained set crew."],
  ["Set shelves match the approved map within tolerance.",
   "No unstable stacking; clear sightlines; reachable ranges.",
   "Changes to the map approved, not improvised."],
  ["The public edition planogram record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "sellthru", {"received": 12000, "sold": 9840}),

R("The Never-Closing Store — Signature E-commerce", "Compounded", 18,
  "The Signature method runs the online store as the never-closing branch: the same covenant of true price, true availability, and kept delivery promises, honored at midnight as at noon. "
  "Where the physical store lends its presence, the online store lends its memory - every order tracked, every promise timestamped. "
  "The buy button is a handshake; the method keeps it firm.",
  "Catalog pages show true images, honest descriptions, and live availability - never selling what the registry does not hold. "
  "Checkout is swift, secure, and fraud-wise; orders flow to fulfillment where pickers gather exactly what was promised, packers armor it for travel, and carriers carry it with tracking the customer can watch. "
  "Where-is-my-order is answered with the same truth the warehouse sees.",
  ["The online store never closes and never breaks covenant.",
   "Never sell what the registry does not hold.",
   "The buy button is a handshake - fulfillment keeps it firm.",
   "Tracking truth shared: customer sees what the warehouse sees."],
  ["A platform with true catalog, cart, and secure checkout.",
   "A fulfillment node with disciplined pick, pack, and ship.",
   "Carrier promises the store can actually keep."],
  ["Charged price equals displayed price at order time.",
   "Customer data guarded; card data never in the clear.",
   "Slipped promises communicated before the customer asks."],
  ["The public edition e-commerce record, for the mechanical standard (this system).",
   "PCI Data Security Standard (public standard)."],
  "basket", {"txns": 5400, "items": 11880, "revenue": 324500.0}),

R("One Inventory, Many Doors — Signature Omnichannel", "Compounded", 19,
  "The Signature method holds one inventory behind many doors: store, website, app, and catalog all draw from the same true pool, and the customer's chosen path is honored whichever door they enter. "
  "Buy online and gather in store, or have the store send it home - the promise is the same because the truth is one. "
  "The method refuses the old lie of separate stocks and separate excuses.",
  "One order system sees every node and routes each line to its best source by nearness, stock truth, and cost. "
  "Store teams pick from their shelves with guided devices, pack at sworn stations, and hold for pickup with prompt word to the customer. "
  "Each node is measured - accuracy, speed, handoff - and coached where it falters, for the chain is only as true as its weakest door.",
  ["One true inventory behind every door the customer may enter.",
   "Each order line routed to its best source by the one system.",
   "Stores as fulfillment kin: picked, packed, and handed off with care.",
   "Every node measured and coached; no weak door excused."],
  ["Live inventory truth across all nodes.",
   "One order system with honest routing rules.",
   "In-store fulfillment stations and trained keepers."],
  ["Pickup promises kept within the stated window, verified handoff.",
   "Substitutions only with the customer's leave.",
   "One price and one promotion across every path."],
  ["The public edition omnichannel record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "turnover", {"cogs": 5100000.0, "avg_inv": 720000.0}),

R("The Great Storehouse — Signature Warehousing", "Compounded", 20,
  "The Signature method keeps the distribution center as the great storehouse: goods received with ceremony, stored with order, and dispatched on rhythm. "
  "The warehouse system knows every pallet's place as the registry knows every SKU - for the storehouse is the registry made physical. "
  "Cost per unit handled is the storehouse's honor price, driven down by discipline, never by corner-cutting.",
  "Trucks are scheduled to docks, unloaded and verified against the purchase order, and goods put away to system-directed homes. "
  "Outbound waves pick by case, pallet, or each, consolidate by route, and load on the delivery rhythm; fast movers cross-dock straight from inbound to outbound. "
  "The building is counted on rotation like the store, for the storehouse's truth feeds every shelf.",
  ["The storehouse is the registry made physical: every pallet placed, every place known.",
   "Inbound verified, outbound waved, fast movers cross-docked.",
   "Cost per unit handled: the honor price, earned by discipline.",
   "Counted on rotation - the storehouse's truth feeds every shelf."],
  ["A warehouse system with directed put-away and picking.",
   "Dock scheduling that honors drivers time.",
   "Equipment matched to building and goods."],
  ["Racking, forklifts, and pedestrian ways per the safety law.",
   "Food, drug, and hazmat stored per their regulations.",
   "No corner cut that risks a worker or a count."],
  ["The public edition warehousing record, for the mechanical standard (this system).",
   "OSHA warehouse safety standards (public regulation)."],
  "turnover", {"cogs": 12000000.0, "avg_inv": 1500000.0}),

R("The Backward Road — Signature Returns", "Compounded", 21,
  "The Signature method walks the backward road with the same care as the forward: a returned good is received, judged honestly, and sent to its rightful next place. "
  "The return is the covenant's second test - the store that welcomes back gracefully is trusted going forward. "
  "Fraud is met with pattern-wise vigilance, never with suspicion cast on honest guests.",
  "Returns arrive under the plain-written policy, are inspected and graded without prejudice, and routed by sworn disposition: restock the resalable, claim the defective from the vendor, refurbish, donate, or liquidate the rest. "
  "Every disposition is recorded, so the true cost of the backward road shows by category. "
  "Wardrobing and empty-box patterns are flagged by the system for quiet review.",
  ["The backward road walked with forward care.",
   "Every return judged and routed to its rightful next place.",
   "True cost of returns visible by category.",
   "Fraud met by pattern, never by accusing honest guests."],
  ["A plain-written return policy with stated limits.",
   "An inspection and grading post for returns.",
   "Disposition roads: restock, vendor claim, refurbish, donate, liquidate."],
  ["Refunds to the original tender within the promised time.",
   "Defective goods handled under warranty and safety law.",
   "Return data guarded, never sold."],
  ["The public edition returns record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "markdown", {"orig": 65.00, "pct": 50.0}),

R("The Circle of Return — Signature Loyalty", "Compounded", 22,
  "The Signature method seals loyalty as a circle of return: the guest comes back, the store gives back, and the bond deepens with every turn. "
  "Rewards are given gladly and accounted honestly - unredeemed promises carried on the books as the liabilities they are. "
  "The program must earn its keep: the lift in visits and baskets must outweigh the rewards and the running cost, measured without flattery.",
  "Members join freely and earn by their spending; thresholds unlock the promised rewards, and tiers honor the most faithful with the finest perks. "
  "Member against non-member is compared honestly to prove the lift is real, and the books carry the outstanding promises truthfully. "
  "Terms are spoken at enrollment - earn, expiry, redemption - and kept to the letter.",
  ["Loyalty is a circle of return, sealed with honest accounting.",
   "Rewards given gladly; outstanding promises booked as liabilities.",
   "Lift proven by honest member-versus-non-member comparison.",
   "Terms spoken at enrollment and kept to the letter."],
  ["A member registry with consented, guarded data.",
   "Earning woven into register and website alike.",
   "Finance eyes on liability and true return."],
  ["Expiry only with the notice the terms promised.",
   "Member data used per the stated policy, never sold in shadow.",
   "No reward promised that the store will not gladly give."],
  ["The public edition loyalty record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "loyalty", {"members": 42000, "avg_points": 1250, "point_value": 0.008}),

R("Guarding the Goods — Signature Loss Prevention", "Compounded", 23,
  "The Signature method guards the goods as a keeper guards a trust: shrink measured honestly, causes faced squarely, and every person treated with dignity - including the accused. "
  "Theft, error, and fraud are real; so is the ruin of a false accusation. "
  "The method pursues the first without ever risking the second.",
  "Shrink is measured per store and category through counts and exception reports; the largest cause is attacked first, whether it is shoplifting, internal theft, paperwork error, or vendor fraud. "
  "Deterrence is open and lawful - visible care, secured high-risk goods, trained staff; detection is systematic - cameras, tags, and register exceptions flagging voids and sweetheart discounts. "
  "Investigations follow written protocol with evidence standards, for the keeper's honor depends on never condemning the innocent.",
  ["Guard the goods; honor the people - including the accused.",
   "Measure shrink by cause and store; strike the largest first.",
   "Detection systematic: cameras, tags, register exceptions.",
   "Evidence standards in every investigation; never condemn the innocent."],
  ["Shrink measurement by count and exception reporting.",
   "A written investigation protocol with evidence standards.",
   "Deterrence proportionate to the measured risk."],
  ["Detentions within the strict limits of the law.",
   "Employee inquiries with documented due process.",
   "Surveillance notice posted where required."],
  ["The public edition loss-prevention record, for the mechanical standard (this system).",
   "State shoplifting detention statutes (public law)."],
  "shrink", {"sales": 8500000.0, "shrink_pct": 1.6}),
]

SIG += [
R("The Two Lenses — Signature Retail Analytics", "Advanced", 24,
  "The Signature method reads the trade through two lenses: did the customers want it, and did it earn its keep. "
  "Sell-through is the wanting, measured in units; GMROI is the earning, measured in margin per dollar of stock. "
  "A keeper fluent in both never confuses motion for progress.",
  "Received against sold yields sell-through per SKU - the slow flagged for honorable reduction, the swift reordered before the shelf empties. "
  "Margin dollars over average inventory cost yields GMROI - three means three dollars of margin per dollar invested. "
  "Open-to-buy flows toward the high earners, and the dashboards tell the truth by department, vendor, and store without flattery.",
  ["Two lenses: the wanting (sell-through) and the earning (GMROI).",
   "Slow movers reduced honorably; swift movers reordered in time.",
   "Investment flows toward what earns; sentiment gets no budget.",
   "Dashboards tell unflattered truth by department and store."],
  ["True sales and receiving data per SKU.",
   "A weekly reading rhythm and a monthly deep study.",
   "Keepers empowered to act on the readings."],
  ["Metrics defined one way, everywhere, always.",
   "Markdown-lifted sell-through marked as such.",
   "Inventory valued consistently for honest comparison."],
  ["The public edition analytics record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "gmroi", {"gross_margin": 385000.0, "avg_inv_cost": 142000.0}),

R("Kindred Goods — Signature Basket Wisdom", "Advanced", 25,
  "The Signature method studies which goods travel together as kindred: the pairs and families that customers naturally gather in one basket. "
  "These affinities are the store's hidden map - honored in adjacency, in bundles, and in honest recommendation. "
  "But the method tests before it trusts, for coincidence wears affinity's clothes.",
  "Transactions are mined for true companionship - how often the pair occurs, how often B follows A, how far above chance the pairing runs. "
  "Proven kindred are set side by side, bundled in fair promotions, and suggested online where the cart already holds the kin. "
  "The map is redrawn with the seasons, for kindred shift as life does.",
  ["Study which goods travel together; honor true kindred.",
   "Test before trusting - coincidence mimics affinity.",
   "Set kindred side by side; bundle them fairly.",
   "Redraw the map with the seasons."],
  ["Basket-level transaction truth with SKU detail.",
   "Tools for honest association study.",
   "A road from finding to shelf action."],
  ["Correlations held as hypotheses until proven.",
   "Analysis anonymized; no targeting without consent.",
   "Bundles priced fairly against the separate goods."],
  ["The public edition basket-analysis record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "basket", {"txns": 9800, "items": 25480, "revenue": 412300.0}),

R("The Stewardship of Kinds — Signature Category Management", "Advanced", 26,
  "The Signature method stewards each category as a small kingdom: coffee, detergent, bread - each with its own health, its own role, its own sworn targets. "
  "The steward thinks in shopping missions, not vendor favors: the category exists to serve the guest's need. "
  "Promotions must grow the kingdom, not merely move its crown from one brand to another.",
  "Each category is given its role - destination drawing journeys, routine serving habits, seasonal marking time - and assortment, space, and promotion follow the role. "
  "Scorecards track the kingdom's true health: sales, margin, and guest satisfaction together. "
  "Vendors are welcomed as counselors with shared data, but the steward keeps the final word over the shelf.",
  ["Each category a small kingdom with sworn targets.",
   "Roles decree space and assortment: destination, routine, seasonal.",
   "Grow the kingdom; do not merely move its crown.",
   "Vendors counsel; the steward decides."],
  ["Category definitions and roles, reviewed yearly.",
   "Sales and shopper truth at category depth.",
   "A review rhythm with vendor counsel sessions."],
  ["Shelf decrees documented and free of hidden payments.",
   "Scorecards consistent across periods.",
   "Assortment changes proclaimed to stores before resets."],
  ["The public edition category record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "gmroi", {"gross_margin": 210000.0, "avg_inv_cost": 68000.0}),

R("The House Brand — Signature Private Label", "Advanced", 27,
  "The Signature method raises the house brand as the store's own banner: goods made to the keeper's specification, carrying the keeper's name, answerable to the keeper's honor. "
  "Where national brands rent the shelf, the house brand owns its loyalty - no competitor can copy it. "
  "It must earn its place by quality first, price second, for a banner that disappoints shames the house.",
  "The keeper finds where the house can win, writes the specification to meet or beat the national brand, and sources through open bidding with audited makers. "
  "Production is tested against the spec, the pack designed to the house standard, and the launch backed with true placement and promotion. "
  "Thereafter the banner is tended like any brand: renewed, quality-held, and margin-watched.",
  ["The house brand is the store's own banner and honor.",
   "Specification first: meet or beat the national brand.",
   "Audited makers, tested production - the name is on the line.",
   "Tended as a brand: renewed, quality-held, margin-watched."],
  ["Category truth showing where the house can win.",
   "Sourcing and quality-keeping capability.",
   "Pack and claim standards of the house."],
  ["Every pack claim proven by testing.",
   "Makers audited for labor and safety.",
   "Recalls executed with national-brand speed."],
  ["The public edition private-label record, for the mechanical standard (this system).",
   "FDA/USDA labeling rules for store-brand goods (public regulations)."],
  "markup", {"cost": 8.40, "price": 21.99}),

R("The Long Road — Signature Supply Chain", "Advanced", 28,
  "The Signature method walks the long road from raw material to the customer's hand as one sworn journey. "
  "In-stock, true landed cost, and speed are its three measures; resilience is its armor, for the cheapest road unguarded is the road that fails in the storm. "
  "Every SKU's true cost - goods, freight, duty, handling - is known, so sourcing choices are honest.",
  "Forecasts feed procurement; transport is booked across sea, air, rail, and road with watched milestones; storehouses receive, keep, and forward on rhythm. "
  "A watchtower view tracks the whole flow, and when disruption strikes, the goods reroute by plan, not panic. "
  "Suppliers are scored on quality, timeliness, cost, and conduct - partners in the journey, not just prices.",
  ["One sworn journey from raw material to the customer's hand.",
   "Three measures: in-stock, true landed cost, speed. Resilience the armor.",
   "True cost per SKU - honest sourcing needs honest numbers.",
   "Disruption met by plan, not panic."],
  ["Forecasts feeding procurement and transport.",
   "A watchtower view across every leg.",
   "Supplier scorecards: quality, time, cost, conduct."],
  ["Duties and customs filed truly and on time.",
   "Supplier labor and safety audited, never assumed.",
   "Contingency roads walked before they are needed."],
  ["The public edition supply-chain record, for the mechanical standard (this system).",
   "U.S. Customs import compliance requirements (public regulations)."],
  "eoq", {"D": 48000.0, "S": 450.0, "H": 6.80}),

R("The Right Hands at the Right Hour — Signature Labor", "Advanced", 29,
  "The Signature method staffs by the honest clock: the right hands, in the right places, at the hours the guests actually come. "
  "Labor is the keeper's largest trust - wages paid for real service - and the schedule is where that trust is either honored or squandered. "
  "Chronic overtime is the confession of a schedule that lies.",
  "Guest traffic by hour is studied; labor standards translate need into hours by task - registers, floor, receiving, stocking. "
  "Schedules are built to the truth, published ahead, adjusted fairly for absence and surge, and timekeeping feeds payroll exactly. "
  "Overtime is watched as the early warning it is.",
  ["Staff to the honest clock of guest traffic.",
   "Standards turn need into hours by task.",
   "Schedules published ahead, adjusted fairly.",
   "Chronic overtime confesses an understaffed base."],
  ["Hourly traffic and sales truth for forecasting.",
   "Labor standards and a scheduling discipline.",
   "Timekeeping true into payroll."],
  ["Wage, hour, break, and overtime law in every schedule.",
   "Youth-work rules honored.",
   "Notice rules for schedule changes obeyed."],
  ["The public edition labor record, for the mechanical standard (this system).",
   "Department of Labor wage-and-hour rules (public regulations)."],
  "breakeven", {"fixed": 42000.0, "price": 18.50, "varcost": 7.80}),

R("Choosing Ground — Signature Site Selection", "Advanced", 30,
  "The Signature method chooses ground as a settler does: study the land, count the rooftops, watch the roads, know the neighbors, and only then raise the roof. "
  "A lease is a years-long vow; the method signs it with open eyes and negotiated terms, never on hope. "
  "Good ground forgives a keeper's mistakes; bad ground punishes their virtues.",
  "The trade area is drawn, its people counted by day and night, its traffic measured, its competitors and companion tenants mapped. "
  "Revenue is forecast by honest models tuned on the keeper's own stores; rent, build-out, and running cost are weighed against it. "
  "Terms are negotiated hard - rent shape, years, protections, exits - before the vow is signed.",
  ["Choose ground like a settler: study first, build after.",
   "The lease is a years-long vow - negotiate it so.",
   "Forecast revenue by honest models, weigh against true cost.",
   "Good ground forgives; bad ground punishes."],
  ["People, traffic, and competitor truth for candidate grounds.",
   "A forecasting model tuned on the keeper's own stores.",
   "Legal eyes on every lease."],
  ["Zoning, signs, and permits proven before commitment.",
   "Access and parking confirmed.",
   "The ground itself checked before building."],
  ["The public edition site-selection record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "breakeven", {"fixed": 310000.0, "price": 42.00, "varcost": 16.50}),

R("The Unseen Counters — Signature RFID and Automation", "Advanced", 31,
  "The Signature method sets unseen counters to watch the shelves: radio tags that let a whole department be counted in minutes, labels that change price at a word, tireless watchers that report the gaps. "
  "Automation in this method does not replace the keeper's care - it multiplies it, freeing hands for guests while machines keep the count. "
  "And the count, being true, lifts every system that drinks from it.",
  "Tagged goods answer the reader's sweep with their sworn numbers, reconciled against the registry in near real time. "
  "Shelf labels take their prices from the one file at a command; roaming watchers report the empty and the misplaced for human hands to mend. "
  "Replenishment, online promises, and shrink-watching all grow sharper on true counts.",
  ["Unseen counters: tags counted in minutes, labels changed at a word.",
   "Automation multiplies care; it does not replace it.",
   "True counts lift replenishment, promises, and shrink-watching.",
   "Hands freed for guests while machines keep the count."],
  ["Tagged goods, by vendor hand or the store's own.",
   "Readers, software, and registry woven together.",
   "A honest plan for how roles shift with the machines."],
  ["Tag data for inventory, not for shadowing guests unawares.",
   "Labels forever equal to the price file.",
   "Machines rated safe for public floors."],
  ["GS1 EPC/RFID standards (public standard).",
   "The public edition automation record, for the mechanical standard (this system)."],
  "shrink", {"sales": 12000000.0, "shrink_pct": 1.1}),

R("The Turning Year — Signature Seasonal Planning", "Advanced", 32,
  "The Signature method keeps the turning year as a keeper keeps a calendar of vows: each season foreseen, stocked, staffed, and reviewed. "
  "Open-to-buy is the year's financial conscience - the sworn remainder that may still be spent, after counting what is owned and what is already coming. "
  "Enthusiasm without the conscience becomes January's clearance pyre.",
  "Sales, margin, and inventory targets are set by month for the season; open-to-buy is computed as planned buying minus owned minus ordered. "
  "Keepers spend within it, holding back a reserve to chase the proven winners mid-season. "
  "When the season turns, plan is set against actual - sales, margin, remnants - and the lessons are written into next year's calendar.",
  ["The year kept as a calendar of vows: foreseen, stocked, reviewed.",
   "Open-to-buy the financial conscience: spend only the sworn remainder.",
   "Hold reserve to chase proven winners mid-season.",
   "Each season's lessons written into the next."],
  ["A monthly plan of sales, margin, and inventory per season.",
   "Open-to-buy reckoned fresh as goods and orders post.",
   "Spending discipline: none beyond the conscience without leave."],
  ["Seasonal staffing proclaimed honestly and lawfully.",
   "Clearance of remnants planned before the season opens.",
   "Vendor terms sharing the seasonal risk, negotiated upfront."],
  ["The public edition seasonal record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "markdown", {"orig": 150.00, "pct": 60.0}),

R("The Shared Banner — Signature Franchising", "Advanced", 33,
  "The Signature method shares its banner through franchising: the keeper's proven way, taught whole to owner-keepers who raise it in new lands. "
  "The franchisor gives the brand, the systems, and the counsel; the franchisee gives capital and local devotion. "
  "One banner, many hands - and the manual is the shared law that keeps every hand true.",
  "Every process is written into the manual - ground-choosing, building, training, goods, pricing counsel, marketing, quality audits - and every franchisee walks by it. "
  "Fees and royalties sustain the shared brand; training, supply roads, and field counsel sustain the franchisee. "
  "Audits and guest voices keep all locations honest, for the banner belongs to all who bear it.",
  ["One banner, many hands; the manual the shared law.",
   "Proven way taught whole - nothing essential withheld.",
   "Royalties sustain the brand all share.",
   "Audits guard the banner every bearer holds."],
  ["A proven, writable, teachable way of running the store.",
   "Disclosure documents per the franchise law.",
   "Training, supply, and field counsel for bearers of the banner."],
  ["Disclosure and registration per the franchise law.",
   "No earnings sung without lawful proof.",
   "Standards enforced evenly - favoritism rots the fellowship."],
  ["FTC Franchise Rule on disclosure (public regulation).",
   "The public edition franchise record, for the mechanical standard (this system)."],
  "breakeven", {"fixed": 95000.0, "price": 32.00, "varcost": 12.40}),

R("The Keeper's Review — Signature Mastery", "Advanced", 34,
  "The keeper's review gathers the whole ladder into one sworn picture: catalog, covenant price, true count, path, hands, and lenses moving as one trade. "
  "Each earlier record was a single art; this is the art of arts - reading the store as the pilot reads the instruments, every gauge true, every gauge joined. "
  "Mastery in the Signature method is not knowing the most, but keeping the whole faithfully.",
  "Begin from the guest and reason backward: the assortment and covenant that earn the visit, the count that keeps the promise, the hands and systems that deliver, the lenses that prove. "
  "Keep the weekly rhythm - sales read, counts acted, prices checked, hands aligned - and the yearly rhythm - seasons planned, conscience kept, events honored, lessons written. "
  "Watch the six gauges - growth, margin, earning-on-stock, in-stock, shrink, return of guests - and let every decision move at least one toward the good.",
  ["The whole trade as one sworn picture: every art joined.",
   "Reason backward from the guest to every decision.",
   "Keep the weekly rhythm and the yearly rhythm without fail.",
   "Mastery is keeping the whole faithfully, not knowing the most."],
  ["The full ladder fluent, foundations through advanced.",
   "A weekly cadence owned without skipping.",
   "Gauges read together, honestly, every cycle."],
  ["Guest promises kept as spoken.",
   "Hands treated lawfully and fairly at every rank.",
   "Books true and complete."],
  ["The public edition mastery record, for the mechanical standard (this system).",
   "Signature system governance on original works (this system)."],
  "gmroi", {"gross_margin": 920000.0, "avg_inv_cost": 265000.0}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + '# '+safe+' -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n'
   + "# EOQ structural sample calculator (retail operations)\\n"
   + "import math\\n"
   + "D, S, H = 1200.0, 50.0, 2.5\\n"
   + "eoq = math.sqrt(2*D*S/H)\\n"
   + "orders = D/eoq\\n"
   + "print('sample annual demand:', D)\\n"
   + "print('sample EOQ:', round(eoq,2))\\n"
   + "print('sample orders per year:', round(orders,2))\\n"
   + "assert eoq > 0 and orders > 0\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""
