#!/usr/bin/env python3
"""Entries for the Price and Profit Tracking databases (Manon's orders 2026-10-17, #1-2).

Manon's order: "Profit and price marking database so each thing has a price in
a time (time for reference over time)" - "so AI knows what things are worth, or
if make something new it'll have a ballpark."

So this build creates two NEW databases, 34 ladder-ordered records each:

  price-profit-tracking            - The Price and Profit Tracking Database
                                     (public-harvest: real, fact-checked price
                                     and profit data - price anatomy, real
                                     historical series for gold (LBMA), oil
                                     (EIA/FRED), housing (Census/NAR), equities
                                     (S&P 500), the CPI (BLS), depreciation
                                     and appreciation math, the three valuation
                                     approaches, ballpark-estimation heuristics,
                                     and profit-margin benchmarks - organized
                                     in the Signature system)
  price-profit-tracking-signature  - The Price and Profit Tracking Signature Database
                                     (his original Signature Valuation Method:
                                     every price a covenant between maker and
                                     buyer sealed in time, profit the honest
                                     wage of value delivered, the price record
                                     the ledger line of that covenant; src
                                     signature, titles suffixed " (Signature
                                     Edition)", never presented as authentic
                                     public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-PFT- (public) and JAH-PFTS- (signature), verified free in the
manifest id_prefix values (zero hits) and in every shard index file of
jah-databases-data-1 (zero hits on the "id":"JAH-PFT prefix).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the demos
(see demos_price_profit_tracking.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos.

Historical series used (all verified 2026-10-17 against public sources):
  gold: LBMA annual averages via National Mining Association table -
        1920 $20.68, 1934 $34.69, 1970 $36.02, 1980 $615.00 (Jan 1980 intraday
        peak $850), 1990 $383.51, 2000 $279.11, 2010 $1,224.53, 2020 $1,769.64,
        2024 $2,394.86
  oil:  U.S. domestic first purchase (EIA) and WTI spot (FRED/Macrotrends) -
        1970 $3.18, 1980 $21.59, 1990 $20.03, 2000 $26.72 first purchase /
        $30.38 WTI spot, 2008 $99.67 WTI avg (Jul 2008 spike $145.31),
        2016 $43.29, 2020 $39.68 WTI avg (Apr 20, 2020 print -$36.98),
        2024 $76.63, 2025 $65.39
  CPI-U annual average (BLS): 1970 38.8, 1980 82.4, 1990 130.7, 2000 172.2,
        2010 218.056, 2020 258.811, 2023 304.702 (base 1982-84 = 100)
  housing: median new-home sale price (Census): 1975 $39,300, 1980 $64,600,
        1990 $122,900, 2000 $169,000, 2010 $221,800, 2020 $336,900, 2024
        $420,300; median existing-home (NAR) 2024 $407,500
  equities: S&P 500 year-end closes: 2010 1,257.64, 2020 3,756.07, 2023 4,769.83,
        2024 5,881.63; Mar 2000 intraday high 1,552.87; Mar 2009 trough 666
  wages: federal minimum wage 1968 $1.60, 1975 $2.10, 1981 $3.35, 1997 $5.15,
        2009 $7.25 (unchanged since July 24, 2009)

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk.
"""

SIG_TAIL = ("Signature original - his original Signature Valuation Method: "
            "every price a covenant between maker and buyer sealed in time, "
            "profit the honest wage of value delivered, and the price record "
            "the ledger line of that covenant. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_BLS_CPI = ("U.S. Bureau of Labor Statistics. Consumer Price Index, "
               "CPI-U annual averages (base 1982-84=100): 1970 38.8; 1980 "
               "82.4; 1990 130.7; 2000 172.2; 2010 218.056; 2020 258.811; "
               "2023 304.702. Historical CPI-U tables, bls.gov.")
CIT_GOLD = ("LBMA annual average gold prices via National Mining Association "
            "historical table (World Gold Council / Kitco / LBMA sources): "
            "1920 $20.68; 1934 $34.69; 1970 $36.02; 1980 $615.00; 1990 "
            "$383.51; 2000 $279.11; 2010 $1,224.53; 2020 $1,769.64; 2024 "
            "$2,394.86 per troy ounce; January 1980 intraday peak $850.")
CIT_OIL = ("U.S. Energy Information Administration, domestic first purchase "
           "crude prices, and FRED series DCOILWTICO (WTI spot): 1970 $3.18; "
           "1980 $21.59; 1990 $20.03; 2000 $26.72 / $30.38 WTI; 2008 $99.67 "
           "avg with July 2008 spike $145.31; 2016 $43.29; 2020 $39.68 avg "
           "with April 20, 2020 print -$36.98; 2024 $76.63; 2025 $65.39.")
CIT_HOUSING = ("U.S. Census Bureau, median and average sales prices of new "
               "homes sold (annual): 1975 $39,300; 1980 $64,600; 1990 "
               "$122,900; 2000 $169,000; 2010 $221,800; 2020 $336,900; 2024 "
               "$420,300; National Association of Realtors median "
               "existing-home price 2024 $407,500.")
CIT_SP500 = ("S&P 500 year-end closes: 2010 1,257.64; 2020 3,756.07; 2023 "
             "4,769.83; 2024 5,881.63; March 24, 2000 intraday high 1,552.87; "
             "March 6, 2009 trough 666. Historical index data, standard "
             "market records.")
CIT_WAGE = ("U.S. Department of Labor, Fair Labor Standards Act minimum wage "
            "history: 1968 $1.60; 1975 $2.10; 1981 $3.35; 1997 $5.15; July 24, "
            "2009 $7.25, unchanged since.")
CIT_VALUATION = ("Standard valuation practice: the three approaches - "
                 "comparables (market), cost, and income - per the Uniform "
                 "Standards of Professional Appraisal Practice (USPAP) and "
                 "International Valuation Standards (IVS); discounted cash "
                 "flow per standard corporate finance (Brealey, Myers, Allen, "
                 "Principles of Corporate Finance).")
CIT_ACCOUNTING = ("Standard accounting: depreciation methods (straight-line, "
                  "declining-balance, sum-of-the-years-digits) and inventory "
                  "methods (FIFO, LIFO, weighted average) per U.S. GAAP, "
                  "ASC 330 (inventory) and ASC 360 (property, plant, "
                  "equipment).")

ENTRIES = [
# ================= FOUNDATIONS =================
dict(key="price-anatomy",
     name="What a Price Really Is: The Anatomy of a Price Record",
     group="Foundations", ladder_rank=1, ladder_tier="foundations",
     description=(
        "A price is never just a number. A complete price record carries six "
        "anatomical parts: the amount (how much money), the currency (which "
        "money), the unit (per what - per ounce, per hour, per item), the "
        "time (when the price was quoted, because every price is a "
        "time-stamped fact), the place and market (where the trade could "
        "happen), and the terms (what is included - taxes, shipping, "
        "warranty). Strip any one of these away and the number misleads. A "
        "gallon of milk quoted at $3.89 in Ohio in 2023 and a gallon quoted "
        "at $3.89 in California in 2025 are two different price records even "
        "though the digits match. This record teaches the full anatomy so "
        "that every later record in this database can be read honestly: "
        "amount, currency, unit, time, market, terms - six fields, no "
        "shortcuts."),
     how_it_works=(
        "To dissect any price, write out all six fields. Take the sticker "
        "price of a dozen eggs at $4.50: the amount is 4.50, the currency is "
        "USD, the unit is per dozen, the time is the date you saw it, the "
        "market is the store and city, and the terms are whatever the store "
        "promises. Then normalize: divide amount by unit to get the "
        "per-unit price ($4.50 divided by 12 eggs = $0.375 per egg), which "
        "is the form that lets you compare across package sizes. Two prices "
        "can only be compared when their six fields line up - same currency, "
        "same unit, terms noted, and time close enough that inflation has "
        "not moved the ground under them."),
     key_points=[
        "A price record has six parts: amount, currency, unit, time, market, terms.",
        "Two prices are comparable only when their six fields are aligned.",
        "Per-unit normalization ($0.375 per egg from $4.50 per dozen) is the standard comparison move.",
        "Time is part of the price: every price is a time-stamped fact.",
        "Terms (taxes, shipping, warranty, freshness) change what the number means."],
     requirements=[
        "Every price record must carry a time stamp and a unit.",
        "Comparisons must state which of the six fields were normalized."],
     standards=[
        "Record schema of this database: amount, currency, unit, time, market, terms.",
        "Prices stated per unit before any comparison is drawn."],
     citations=[
        "Record schema standard of The Price and Profit Tracking Database.",
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, a price is a covenant written in numbers: "
        "the maker names the amount, the buyer answers with the purchase, "
        "and the six fields of the record are the witnesses. A covenant "
        "missing its witnesses is not binding - a price missing its time, "
        "its unit, or its terms is not honest. The Signature keeper writes "
        "all six fields every time, because the covenant only holds if "
        "every witness is named.")),

dict(key="nominal-vs-real",
     name="Nominal Versus Real: Money Across Time",
     group="Foundations", ladder_rank=1, ladder_tier="foundations",
     description=(
        "A nominal price is the number on the tag in the money of its own "
        "year. A real price is that same amount restated in the money of a "
        "chosen reference year, so that years can be compared on level "
        "ground. The federal minimum wage was $1.60 in 1968 and $7.25 in "
        "2009. In nominal terms the wage rose; in real terms, converting "
        "1968 dollars to 2023 dollars with the CPI-U (34.8 in 1968, 304.702 "
        "in 2023), the $1.60 wage of 1968 equals about $14.01 in 2023 "
        "dollars - nearly double the 2009 nominal wage of $7.25. That is "
        "the whole point of the distinction: nominal numbers tell you what "
        "people saw, real numbers tell you what they could buy. Every "
        "time series in this database is read in both lights."),
     how_it_works=(
        "Conversion uses a price index, here the CPI-U. The formula is: "
        "real value = nominal value times (index of target year divided by "
        "index of original year). For the 1968 minimum wage into 2023 "
        "dollars: $1.60 x (304.702 / 34.8) = $1.60 x 8.756 = about $14.01. "
        "The ratio of the two index readings, 8.756, is the inflation "
        "multiplier across those 55 years. The same formula runs the other "
        "way: $7.25 in 2009 dollars is worth $7.25 x (304.702 / 214.537) "
        "= about $10.30 in 2023 dollars, using the 2009 CPI-U of 214.537. "
        "Pick one reference year for a whole comparison and hold it fixed, "
        "or the ground shifts under the reader."),
     key_points=[
        "Nominal = the number in its own year's money; real = restated in a reference year's money.",
        "Real value = nominal x (target-year index / original-year index).",
        "$1.60 in 1968 is about $14.01 in 2023 dollars - the real peak of the minimum wage.",
        "The index ratio between two years is the inflation multiplier.",
        "Hold one reference year fixed for an entire comparison."],
     requirements=[
        "State the index, the base years, and the reference year for every conversion.",
        "Never compare nominal prices across decades without the real conversion beside them."],
     standards=[
        "CPI-U annual averages, U.S. Bureau of Labor Statistics.",
        "Conversion formula: nominal x (CPI_target / CPI_original)."],
     citations=[
        CIT_BLS_CPI,
        CIT_WAGE],
     sig_lens=(
        "In the Signature lens, nominal money is the rumor of value and "
        "real money is the value itself. The covenant of a price is written "
        "in nominal ink but sealed in real weight: what matters is not the "
        "digits but what they could command. The Signature keeper therefore "
        "reads every old price twice - once as the people of that year saw "
        "it, once as it weighs today - and lets the real reading judge the "
        "nominal one.")),

dict(key="supply-demand",
     name="Supply and Demand: Why Prices Move",
     group="Foundations", ladder_rank=1, ladder_tier="foundations",
     description=(
        "Prices move because buyers and sellers negotiate through quantity. "
        "When the price is high, sellers want to sell more and buyers want "
        "to buy less; when the price is low, the reverse. The market price "
        "is the one where the quantity buyers want equals the quantity "
        "sellers offer - the equilibrium. If a drought cuts the coffee "
        "harvest, the supply curve shifts left and the equilibrium price "
        "rises: the same buyers now chase fewer bags. If incomes rise, the "
        "demand curve shifts right and the price rises for the opposite "
        "reason. Scarcity, cost, income, taste, and expectation are the "
        "five great shifters. Every price series in this database - gold, "
        "oil, housing - is a diary of these shifts written year by year."),
     how_it_works=(
        "Model demand as quantity = 100 - 2 x price, and supply as quantity "
        "= 20 + 3 x price. Equilibrium is where they meet: 100 - 2P = 20 + "
        "3P, so 80 = 5P and P = 16, with quantity 100 - 32 = 68. Now shift "
        "supply left by 15 (a harvest failure): 100 - 2P = 5 + 3P, so 95 = "
        "5P and P = 19 - the price rises by $3 and quantity falls to 62. "
        "The arithmetic is simple on purpose: it shows that a price is not "
        "a property of the thing but a property of the meeting point "
        "between buyers and sellers, and it moves whenever either side "
        "moves."),
     key_points=[
        "Equilibrium price is where quantity demanded equals quantity supplied.",
        "Supply shifts (costs, harvests, technology) and demand shifts (income, taste) move the price.",
        "Example: demand Q=100-2P, supply Q=20+3P gives P=16, Q=68.",
        "A leftward supply shift of 15 raises the price to 19 and lowers quantity to 62.",
        "Price is a property of the meeting point, not of the thing alone."],
     requirements=[
        "Name which curve shifted and in which direction before explaining any price move.",
        "Keep the demand story and the supply story separate."],
     standards=[
        "Elementary price theory: Marshallian supply and demand.",
        "Linear example kept small and fully worked."],
     citations=[
        "Standard microeconomic price theory (Marshall, Principles of Economics, 1890; modern textbooks).",
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, supply and demand are the two hands of the "
        "covenant: the maker's hand offering, the buyer's hand reaching. "
        "The price is where the hands meet. When one hand pulls back, the "
        "meeting point moves, and the price follows like a shadow. The "
        "Signature keeper watches both hands, never one, because a price "
        "explained by only one hand is half a story.")),

dict(key="cost-types",
     name="The Costs Behind Every Price: Fixed, Variable, and Marginal",
     group="Foundations", ladder_rank=2, ladder_tier="foundations",
     description=(
        "Every price a seller charges stands on a floor built of costs, and "
        "costs come in three kinds. Fixed costs do not change with output: "
        "the rent on the bakery is the same whether it bakes ten loaves or "
        "a thousand. Variable costs move with output: flour, yeast, and "
        "hourly labor rise with every extra loaf. Marginal cost is the cost "
        "of one more unit - the next loaf. A bakery with $5,000 of monthly "
        "fixed cost and $12 of variable cost per loaf spends $9,800 to bake "
        "400 loaves, an average cost of $24.50 per loaf, while the marginal "
        "cost of loaf 401 is just $12. Profit begins where price clears the "
        "relevant cost, and the relevant cost depends on the decision: "
        "average cost for staying in business, marginal cost for the next "
        "unit."),
     how_it_works=(
        "Total cost = fixed cost + (variable cost per unit x quantity). "
        "Average cost = total cost / quantity, and it falls as quantity "
        "rises because the fixed cost spreads thinner - this is the scale "
        "economy every manufacturer chases. Marginal cost = the change in "
        "total cost from one more unit, which for the bakery is the $12 of "
        "flour, yeast, and labor, flat until the ovens run out of room. "
        "Pricing rule of thumb: price must exceed average cost in the long "
        "run or the business dies, but for a one-time extra order, price "
        "need only exceed marginal cost. Confusing the two is the classic "
        "way profitable-looking orders lose money."),
     key_points=[
        "Fixed costs ignore output; variable costs follow it; marginal cost is the next unit's cost.",
        "Example: $5,000 fixed + $12 variable, 400 loaves: total $9,800, average $24.50, marginal $12.",
        "Average cost falls with volume - the engine of scale economies.",
        "Long-run survival needs price above average cost; one-off orders need price above marginal cost.",
        "Most pricing mistakes are average-cost thinking applied to marginal-cost decisions."],
     requirements=[
        "Classify each cost as fixed or variable before any pricing math.",
        "State the quantity the average cost was computed at."],
     standards=[
        "Cost classification per standard managerial accounting.",
        "Average and marginal cost computed from the same cost base."],
     citations=[
        "Standard managerial accounting (Horngren et al., Cost Accounting).",
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, costs are the maker's honest ledger: the "
        "rent that must be paid whether the ovens are hot or cold, the "
        "flour that is spent loaf by loaf, and the price of the next loaf "
        "standing alone. The covenant of a fair price is written over this "
        "ledger - the maker may charge what the market will bear, but must "
        "know, to the dollar, what the bearing costs. Ignorance of the "
        "ledger voids the covenant from the maker's own side.")),

dict(key="markup-vs-margin",
     name="Markup Versus Margin: Two Languages of Profit",
     group="Foundations", ladder_rank=2, ladder_tier="foundations",
     description=(
        "Markup and margin both describe the gap between cost and price, "
        "but they measure it from opposite ends, and mixing them up is one "
        "of the most expensive mistakes in business. Markup is profit as a "
        "fraction of cost: a $60 item sold for $100 carries a markup of $40 "
        "/ $60 = 66.67%. Margin is profit as a fraction of price: the same "
        "item carries a margin of $40 / $100 = 40%. Retailers, "
        "manufacturers, and distributors usually talk markup; investors, "
        "accountants, and income statements talk margin. The translation "
        "is fixed: margin = markup / (1 + markup), and markup = margin / "
        "(1 - margin). A 66.67% markup is a 40% margin, always, and a 50% "
        "margin is a 100% markup - 'double the money' in margin language."),
     how_it_works=(
        "Start with cost C = $60 and price P = $100. Profit = P - C = $40. "
        "Markup = 40/60 = 0.6667 (66.67%), margin = 40/100 = 0.40 (40%). "
        "To convert: margin = 0.6667 / 1.6667 = 0.40, exactly. Going the "
        "other way, a target margin of 25% needs a markup of 0.25 / 0.75 = "
        "33.33%: price = cost x 1.3333. The danger case: a manager told to "
        "'mark up 40%' who prices at cost x 1.40 earns a margin of only "
        "0.40/1.40 = 28.57%, not 40% - an 11.4-point shortfall that has sunk "
        "real product lines. Always ask which language the percentage is "
        "speaking before you price."),
     key_points=[
        "Markup = profit / cost; margin = profit / price. Same gap, different denominator.",
        "$60 cost, $100 price: 66.67% markup, 40% margin.",
        "margin = markup/(1+markup); markup = margin/(1-margin).",
        "A 40% markup yields only a 28.57% margin - the classic shortfall.",
        "Investors speak margin; merchants speak markup; translate before pricing."],
     requirements=[
        "Label every percentage as markup or margin explicitly.",
        "Show the conversion when a target is stated in the other language."],
     standards=[
        "Markup and margin definitions per standard retail accounting.",
        "Conversion identities verified algebraically."],
     citations=[
        "Standard retail and managerial accounting definitions.",
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, markup is the maker's language and margin "
        "is the ledger's language, and the covenant of price must be "
        "legible in both. A maker who confuses the two has miswritten the "
        "covenant and will discover the error only when the ledger refuses "
        "to balance. The Signature keeper translates every percentage into "
        "both tongues before signing, so the promise made at the counter "
        "matches the truth in the books.")),

dict(key="cpi-measure",
     name="The Consumer Price Index: How Inflation Is Measured",
     group="Foundations", ladder_rank=2, ladder_tier="foundations",
     description=(
        "The Consumer Price Index (CPI-U) is the United States' official "
        "thermometer for the cost of living: a weighted basket of tens of "
        "thousands of goods and services, priced monthly by the Bureau of "
        "Labor Statistics, with housing the heaviest weight at roughly a "
        "third of the basket. The index is set so that the 1982-1984 average "
        "equals 100; the 2023 annual average was 304.702, meaning the "
        "basket cost about three times its mid-1980s level. The inflation "
        "rate is the index's growth: from 2020's 258.811 to 2023's 304.702 "
        "the basket rose 17.73% - the post-pandemic surge written in one "
        "number. The CPI is not the price of everything - it misses asset "
        "prices and rural life - but it is the common ruler every "
        "inflation adjustment in this database is measured against."),
     how_it_works=(
        "The BLS prices a fixed basket, weights each item by household "
        "spending shares, and divides the basket's current cost by its "
        "base-period cost, times 100. Inflation between two years is "
        "(later index - earlier index) / earlier index. For 2020 to 2023: "
        "(304.702 - 258.811) / 258.811 = 45.891 / 258.811 = 0.1773, or "
        "17.73%. The basket's composition is updated as spending patterns "
        "change, which is why the CPI is a chained, living measure rather "
        "than a museum piece. Substitution bias - shoppers switching from "
        "expensive beef to cheaper chicken - is the famous imperfection: "
        "the fixed basket can overstate the pain when people adapt, and "
        "the BLS applies hedonic and geometric adjustments to compensate."),
     key_points=[
        "CPI-U: BLS monthly basket, 1982-84 = 100, housing about a third of the weight.",
        "2023 annual average 304.702; 2020 258.811; 1980 82.4; 1970 38.8.",
        "Inflation 2020-2023 = 17.73%, the post-pandemic surge in one number.",
        "Formula: (later index - earlier index) / earlier index.",
        "Known imperfection: substitution bias when shoppers adapt to price changes."],
     requirements=[
        "Cite the index series (CPI-U), the base period, and annual-average versus monthly readings.",
        "Note what the CPI excludes: asset prices, rural households."],
     standards=[
        "U.S. Bureau of Labor Statistics CPI-U methodology.",
        "Annual averages for year-to-year comparisons."],
     citations=[
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, the CPI is the nation's shared ledger of "
        "the covenant of money: one ruler laid across every price in the "
        "land so that no year's digits can lie about their weight. It is "
        "imperfect, as all shared ledgers are, but it is shared - and a "
        "shared imperfection beats a private delusion. The Signature keeper "
        "measures every long price story against this ruler and names the "
        "ruler plainly, so the reader knows whose yardstick judged the "
        "years.")),

dict(key="reading-price-tag",
     name="Reading a Price Tag: Quotes, Units, and Terms",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "A quoted price is an offer, not a fact, and reading it well is a "
        "skill. First find the unit: the $3.29 bag of coffee is 12 ounces, "
        "so its unit price is $0.274 per ounce; the $4.99 bag is 20 ounces, "
        "$0.250 per ounce - the bigger bag is the better buy by 2.4 cents "
        "an ounce, and the unit-price shelf tag does this arithmetic for "
        "you. Then read the terms: is tax included, is that the cash price "
        "or the credit price, does the subscription renew at a higher "
        "rate, is the warranty extra. Then check the time: a quote "
        "expires, and a price seen last month is a rumor, not an offer. "
        "The disciplined reader converts every quote to the same unit, "
        "notes the terms, and stamps the time - the three moves that turn "
        "a tag into a record."),
     how_it_works=(
        "Unit price = quoted amount / quantity in the chosen unit. Coffee "
        "A: $3.29 / 12 oz = $0.2742 per ounce. Coffee B: $4.99 / 20 oz = "
        "$0.2495 per ounce. B wins by $0.0247 per ounce, about 9% cheaper "
        "per cup. The method generalizes: price per pound, per gallon, "
        "per hour, per gigabyte - pick the unit you actually consume and "
        "divide. For terms, list what the price includes and excludes: a "
        "$19.99 monthly subscription that renews at $29.99 after three "
        "months has two prices, and the honest record carries both with "
        "their dates. For time, record the observation date; a quote older "
        "than its stated validity is history, not an offer."),
     key_points=[
        "Unit price = amount / quantity; compare only in the consumed unit.",
        "$3.29/12oz = $0.274/oz vs $4.99/20oz = $0.250/oz: the bigger bag wins.",
        "Terms change the price: tax, renewal rates, warranties, cash vs credit.",
        "A quote has an expiry; an old quote is history, not an offer.",
        "Convert, note terms, stamp time: three moves from tag to record."],
     requirements=[
        "Show the unit-price arithmetic for every comparison.",
        "Record terms and observation date with the quote."],
     standards=[
        "Unit pricing per NIST Handbook 130 guidance on retail unit pricing.",
        "Terms disclosure per standard consumer-protection practice."],
     citations=[
        "NIST Handbook 130, Uniform Laws and Regulations (unit pricing).",
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, the price tag is the maker's spoken "
        "covenant, and reading it is the buyer's sworn duty. The careless "
        "buyer hears only the big digits; the Signature buyer reads the "
        "small print as the covenant's fine clauses, divides by the true "
        "unit, and asks when the promise expires. A covenant read in full "
        "can be trusted; a covenant skimmed is a gamble wearing the "
        "clothes of a promise.")),

dict(key="break-even",
     name="Break-Even: The Price That Covers the Costs",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "Break-even is the exact point where a price stops losing money: "
        "the quantity at which revenue equals total cost, so every unit "
        "beyond it is profit. A workshop with $12,000 of monthly fixed "
        "costs that sells gadgets at $25 with $13 of variable cost per "
        "gadget earns $12 of contribution per gadget - and $12,000 / $12 = "
        "1,000 gadgets is the break-even quantity, $25,000 of revenue. "
        "Sell 999 and the month loses money; sell 1,001 and the 1,001st "
        "gadget's $12 of contribution is pure operating profit. Break-even "
        "analysis turns the abstract question 'is this price enough' into "
        "a concrete sales target, and it exposes the three levers of "
        "survival: raise price, cut variable cost, or cut fixed cost."),
     how_it_works=(
        "Contribution per unit = price - variable cost per unit = $25 - "
        "$13 = $12. Break-even quantity = fixed costs / contribution = "
        "$12,000 / $12 = 1,000 units. Break-even revenue = 1,000 x $25 = "
        "$25,000. The margin of safety is actual sales minus break-even "
        "sales: at 1,400 units the safety margin is 400 units, or $4,800 of "
        "profit. Sensitivity is immediate from the formula: a $1 price "
        "increase (to $26) drops break-even to $12,000 / $13 = 923 units; "
        "a $1 variable-cost cut does the same. Fixed-cost cuts lower the "
        "numerator directly. Every pricing decision can be auditioned "
        "against this one equation before a dollar is spent."),
     key_points=[
        "Break-even quantity = fixed costs / (price - variable cost).",
        "Example: $12,000 fixed, $25 price, $13 variable: break-even 1,000 units, $25,000 revenue.",
        "Beyond break-even, each unit's contribution is operating profit.",
        "Margin of safety = actual sales minus break-even sales.",
        "Three levers: raise price, cut variable cost, cut fixed cost."],
     requirements=[
        "Separate fixed and variable costs before computing.",
        "State whether break-even is in units or in revenue."],
     standards=[
        "Cost-volume-profit analysis per standard managerial accounting.",
        "Contribution margin computed from the same price and cost base."],
     citations=[
        "Standard cost-volume-profit analysis (Horngren et al., Cost Accounting).",
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, break-even is the covenant's first "
        "milestone: the day the maker's ledger stops bleeding and starts "
        "breathing. Until that day the price is a hope; after it, the "
        "price is a harvest. The Signature keeper counts the units to that "
        "day like a sailor counts rations, because every covenant that "
        "never reaches its milestone was a promise the numbers would not "
        "keep.")),

dict(key="profit-layers",
     name="Gross, Operating, and Net: The Layers of Profit",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "Profit is not one number but a stack of them, each layer answering "
        "a different question. A company with $1,000,000 of revenue and "
        "$620,000 of cost of goods sold earns $380,000 of gross profit - a "
        "38% gross margin - which answers 'does the product itself make "
        "money.' After $230,000 of operating expenses (salaries, rent, "
        "marketing) comes $150,000 of operating profit, a 15% operating "
        "margin - 'does the business run make money.' After $50,000 of "
        "interest and taxes comes $100,000 of net profit, a 10% net margin "
        "- 'what do the owners actually keep.' Each layer strips away a "
        "kind of cost, and the layer where profit vanishes tells you where "
        "the trouble lives: a strong gross margin with a weak net margin "
        "means the product is fine and the overhead is fat."),
     how_it_works=(
        "Gross profit = revenue - cost of goods sold = $1,000,000 - "
        "$620,000 = $380,000; gross margin = 380,000 / 1,000,000 = 38%. "
        "Operating profit = gross profit - operating expenses = $380,000 - "
        "$230,000 = $150,000; operating margin = 15%. Net profit = "
        "operating profit - interest - taxes = $150,000 - $50,000 = "
        "$100,000; net margin = 10%. Margins are always profit divided by "
        "revenue at that layer, never by cost - that is the margin "
        "language, not the markup language. Read the stack top to bottom: "
        "where the margin collapses between layers, there sits the cost "
        "that is eating the business."),
     key_points=[
        "Gross profit = revenue - COGS; operating = gross - opex; net = operating - interest - taxes.",
        "Example: 38% gross, 15% operating, 10% net on $1M revenue.",
        "Margins are profit / revenue at each layer - always the margin language.",
        "The layer where profit vanishes names the problem.",
        "Strong gross with weak net means the product is fine and overhead is fat."],
     requirements=[
        "Show all three layers with their margins, not just net profit.",
        "Classify each expense into COGS, operating, or below-the-line."],
     standards=[
        "Income-statement structure per U.S. GAAP.",
        "Margins computed on revenue at each layer."],
     citations=[
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, the profit stack is the covenant's "
        "accounting: the product's wage, the operation's wage, and the "
        "owner's wage, each honestly separated. A maker who reports only "
        "the top line hides which wage is unpaid. The Signature keeper "
        "lays all three layers open, because the covenant of profit is "
        "only honest when every hand that earned is shown its share.")),

# ================= COMPOUNDED =================
dict(key="gold-series",
     name="Gold Prices Across a Century: A Real Time Series",
     group="Compounded", ladder_rank=4, ladder_tier="compounded",
     description=(
        "Gold is the longest-running price diary in modern finance, and its "
        "LBMA annual averages tell the story of the dollar itself. Under "
        "the gold standard the price barely moved: $20.68 in 1920, $34.69 "
        "in 1934, $36.02 in 1970. When convertibility ended in 1971, the "
        "diary caught fire: $615.00 average in 1980 with a January intraday "
        "peak of $850, then a long sleep - $383.51 in 1990, $279.11 in 2000 "
        "- then the new century's climb: $1,224.53 in 2010, $1,769.64 in "
        "2020, $2,394.86 in 2024. From 1970 to 2024 gold compounded at about "
        "8.1% per year nominal. But read it in real terms: $615 in 1980, "
        "converted with the CPI-U (82.4 to 304.702), is about $2,274 in "
        "2023 dollars - essentially the same purchasing power as gold's "
        "2024 nominal price. The metal preserved; the dollar did the "
        "moving."),
     how_it_works=(
        "A price series is read with two tools: the growth rate and the "
        "real conversion. Compound annual growth rate (CAGR) = "
        "(end/start)^(1/years) - 1. For gold 1970 to 2024: "
        "(2394.86/36.02)^(1/54) - 1 = 66.497^(0.01852) - 1 = about 0.0808, "
        "or 8.1% per year. Real conversion: $615 x (304.702/82.4) = $615 x "
        "3.6976 = about $2,274 in 2023 dollars, versus the 2024 nominal "
        "$2,394.86 - the two readings nearly agree, which is what 'store "
        "of value' means in arithmetic. Note the fixed-price eras: 1934 to "
        "1970 the price was policy, not market - a series must note when "
        "its numbers were decreed rather than discovered."),
     key_points=[
        "LBMA annual averages: 1970 $36.02, 1980 $615.00, 2000 $279.11, 2020 $1,769.64, 2024 $2,394.86.",
        "1970-2024 nominal CAGR about 8.1% per year.",
        "$615 in 1980 is about $2,274 in 2023 dollars - real preservation across 44 years.",
        "January 1980 intraday peak $850; 1934-1970 prices were fixed by policy.",
        "Read every long series twice: nominal growth and real conversion."],
     requirements=[
        "Distinguish annual averages from intraday peaks and policy-fixed prices.",
        "Pair every nominal growth claim with the real-dollar conversion."],
     standards=[
        "LBMA annual averages via National Mining Association historical table.",
        "CAGR and CPI conversion computed from the stated series."],
     citations=[
        CIT_GOLD,
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, gold's century is the covenant of money "
        "kept in metal: when the paper promise wavered, the metal held "
        "its weight and the numbers confessed it. The fixed-price decades "
        "were covenants written by decree; the floating decades are "
        "covenants written by the crowd. The Signature keeper honors both "
        "but never confuses them - a decreed price is a law, a market "
        "price is a testimony, and the ledger must label which is which.")),

dict(key="oil-series",
     name="Oil Prices Since 1970: Boom, Bust, and Negative",
     group="Compounded", ladder_rank=4, ladder_tier="compounded",
     description=(
        "No commodity teaches price volatility like crude oil. The U.S. "
        "domestic first purchase price was $3.18 a barrel in 1970; by 1980 "
        "it was $21.59, and WTI spot averaged $99.67 in 2008 with a July "
        "spike to $145.31. Then the busts: $43.29 in 2016 after the shale "
        "flood, and 2020 - when storage ran out and the April 20 front-month "
        "contract printed negative $36.98, the only negative commodity "
        "price in modern history, sellers paying buyers to take oil away. "
        "The 2020 annual WTI average was $39.68, a 60.2% fall from 2008's "
        "average. By 2024 WTI averaged $76.63 and 2025 $65.39. Oil's diary "
        "proves the first law of price records: the same barrel can be "
        "worth $145 or negative $37 depending on the year, the storage, "
        "and the fear."),
     how_it_works=(
        "Read the series as cycles, not points. The 2008-to-2020 fall: "
        "(99.67 - 39.68) / 99.67 = 59.99 / 99.67 = 0.6018, a 60.2% "
        "decline, driven by the shale supply surge and then COVID demand "
        "destruction. The negative print needs its mechanics: futures "
        "contracts require taking physical delivery, and with storage full "
        "at Cushing, holders paid up to $36.98 a barrel to avoid receiving "
        "oil they could not store - price as the cost of disposal. Annual "
        "averages smooth the violence: the 2020 average of $39.68 hides a "
        "year that touched both $63 and negative territory. For any "
        "volatile series, always quote the average, the high, and the low "
        "together, or the average lies by omission."),
     key_points=[
        "WTI: 2008 avg $99.67 (spike $145.31); 2020 avg $39.68 (print -$36.98); 2024 $76.63.",
        "2008 to 2020 was a 60.2% decline: shale supply then COVID demand collapse.",
        "Negative oil = storage full at Cushing; sellers paid buyers to take delivery.",
        "Annual averages hide violence: always quote average, high, and low.",
        "First law of price records: context (storage, fear) sets the number."],
     requirements=[
        "Quote average, high, and low for volatile series.",
        "Explain the mechanics of any anomalous print (negative, spike)."],
     standards=[
        "EIA domestic first purchase and FRED DCOILWTICO WTI spot series.",
        "Percentage changes computed from annual averages."],
     citations=[
        CIT_OIL],
     sig_lens=(
        "In the Signature lens, oil's diary is the covenant of price "
        "under stress: when the storehouses overflowed, the covenant "
        "inverted and the seller paid the buyer - the market confessing "
        "that a price is not in the barrel but in the circumstance. The "
        "Signature keeper records the negative price without flinching, "
        "because the ledger's duty is to the truth of the year, not to "
        "the comfort of the reader.")),

dict(key="housing-series",
     name="American Home Prices 1975 to 2024: A Real Series",
     group="Compounded", ladder_rank=4, ladder_tier="compounded",
     description=(
        "The median new American home sold for $39,300 in 1975 and $420,300 "
        "in 2024 (Census) - a 10.7-fold rise, compounding at about 5.0% per "
        "year nominal for 49 years. The checkpoints trace the cycles: "
        "$64,600 in 1980, $122,900 in 1990, $169,000 in 2000, $221,800 in "
        "2010, $336,900 in 2020. But the nominal story flatters: $39,300 in "
        "1975, converted with the CPI-U (53.8 to 304.702), is about $222,600 "
        "in 2023 dollars - so roughly half the 10.7-fold rise is inflation "
        "and half is real appreciation, driven by land scarcity, bigger "
        "homes, and cheaper mortgages. The existing-home median (NAR) "
        "reached $407,500 in 2024. Housing teaches the central lesson of "
        "long series: a price that 'always goes up' is usually two stories "
        "- money losing value and the thing gaining it - and only the "
        "real conversion separates them."),
     how_it_works=(
        "Multiple = 420,300 / 39,300 = 10.695 over 49 years. CAGR = "
        "10.695^(1/49) - 1: ln(10.695) = 2.370, divided by 49 = 0.04837, "
        "exponentiated = 1.0496, about 5.0% per year nominal. Real "
        "conversion: $39,300 x (304.702/53.8) = $39,300 x 5.6636 = about "
        "$222,600 in 2023 dollars, versus the 2024 nominal $420,300 - so "
        "about $197,700 of the rise is real. The price-to-income ratio "
        "adds the affordability angle: the existing-home median was 2.9 "
        "times median household income in 1975 and 5.1 times in 2024. A "
        "complete housing price record therefore carries three numbers: "
        "nominal, real, and relative to income."),
     key_points=[
        "Median new home: 1975 $39,300; 2000 $169,000; 2020 $336,900; 2024 $420,300.",
        "10.7-fold nominal rise; CAGR about 5.0% per year over 49 years.",
        "$39,300 in 1975 is about $222,600 in 2023 dollars - half inflation, half real gain.",
        "Price-to-income: 2.9x in 1975, 5.1x in 2024 (existing homes).",
        "Long series need three readings: nominal, real, and relative to income."],
     requirements=[
        "Use median, not average, for home prices (averages skew luxury).",
        "Separate the inflation share from the real share of any long rise."],
     standards=[
        "U.S. Census Bureau new-home medians; NAR existing-home medians.",
        "CAGR and CPI conversion from the stated series."],
     citations=[
        CIT_HOUSING,
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, a home's price is the covenant between a "
        "family and its future, sealed in the largest number most people "
        "ever sign. The Signature keeper reads the 10.7-fold rise without "
        "awe and without despair: half is the dollar's confession, half is "
        "the land's testimony, and the price-to-income ratio is the "
        "judgment - the covenant is only as sound as the years of labor it "
        "asks.")),

dict(key="sp500-series",
     name="The S&P 500 as a Price Series",
     group="Compounded", ladder_rank=4, ladder_tier="compounded",
     description=(
        "The S&P 500 is a price series for the American corporate economy "
        "itself: 500 large companies distilled into one number. Its "
        "year-end closes trace the modern era: 1,257.64 in 2010, 3,756.07 "
        "in 2020, 4,769.83 in 2023, 5,881.63 in 2024 - a 4.68-fold rise "
        "from 2010 to 2024, compounding at about 11.6% per year nominal. "
        "The landmarks between the closes tell the emotional story: the "
        "March 2000 intraday high of 1,552.87 before the dot-com bust, the "
        "March 2009 trough of 666 at the financial-crisis bottom - a 57% "
        "fall from the 2007 peak. Unlike gold or oil, this series pays "
        "dividends, so the price alone understates the owner's return; "
        "total-return indexes add roughly two points a year. The S&P diary "
        "is the reference 'risk asset' against which every other long "
        "price series in this database can be judged."),
     how_it_works=(
        "Multiple 2010-2024 = 5,881.63 / 1,257.64 = 4.677 over 14 years. "
        "CAGR = 4.677^(1/14) - 1: ln(4.677) = 1.5426, /14 = 0.11019, "
        "exp = 1.1165, about 11.6% per year nominal - price return only. "
        "Drawdown math: the 2007-2009 fall from the October 2007 high "
        "(about 1,565) to 666 is (1,565-666)/1,565 = 57.4%, the standard "
        "measure of the pain. When comparing to gold's 8.1% or housing's "
        "5.0%, remember the S&P number excludes dividends while the others "
        "are pure price - the honest comparison uses total return, price "
        "plus payouts, for all of them. A price series that pays its "
        "holder is a different animal from one that merely sits there."),
     key_points=[
        "S&P 500 year-end: 2010 1,257.64; 2020 3,756.07; 2023 4,769.83; 2024 5,881.63.",
        "2010-2024: 4.68-fold, about 11.6% per year nominal price return.",
        "Landmarks: Mar 2000 intraday high 1,552.87; Mar 2009 trough 666 (57% drawdown).",
        "Price return understates owner return: dividends add roughly two points a year.",
        "Compare series on total return, not price alone, when payouts exist."],
     requirements=[
        "Label price return versus total return explicitly.",
        "Quote drawdowns from peak to trough, not cherry-picked endpoints."],
     standards=[
        "S&P 500 historical closes, standard market records.",
        "CAGR and drawdown computed from the stated series."],
     citations=[
        CIT_SP500],
     sig_lens=(
        "In the Signature lens, the S&P 500 is the covenant of the "
        "crowd's capital: 500 enterprises bound into one number, rising "
        "and falling on the faith of millions. The Signature keeper reads "
        "it as a parable of patience - the 57% drawdown was the covenant "
        "tested, the recovery the covenant kept - and reminds the reader "
        "that the number on the screen is only the price half of a return "
        "that also pays its keepers in dividends.")),

dict(key="inflation-adjustment",
     name="Time-Traveling Money: Inflation Adjustment",
     group="Compounded", ladder_rank=5, ladder_tier="compounded",
     description=(
        "Inflation adjustment is the time machine of price work: it carries "
        "a price from its own year into any other year's money so the two "
        "can meet honestly. A twenty-dollar bill from 1913, converted with "
        "the CPI-U (9.9 in 1913, 304.702 in 2023), equals about $615.56 in "
        "2023 dollars - the same twenty that bought a week's groceries in "
        "1913 buys a modest dinner out today. The 1968 minimum wage of "
        "$1.60 becomes about $14.01 in 2023 dollars, and the $3.18 barrel "
        "of oil from 1970 becomes about $24.98 in 2023 dollars - cheaper in "
        "real terms than the 2024 barrel at $76.63. The technique is one "
        "formula applied relentlessly: multiply by the ratio of the two "
        "CPI readings. Its limits are honest too: the CPI basket changes, "
        "quality improves, and no index can convert the unbuyable past "
        "perfectly - but an adjusted comparison beats a nominal one every "
        "time."),
     how_it_works=(
        "Adjusted value = original amount x (CPI of target year / CPI of "
        "original year). $20 of 1913 into 2023 dollars: 20 x (304.702/9.9) "
        "= 20 x 30.778 = $615.56. $3.18 of 1970 oil into 2023 dollars: "
        "3.18 x (304.702/38.8) = 3.18 x 7.8537 = about $24.98 - cheaper in "
        "real terms than the 2024 barrel at $76.63, which is the point of "
        "converting. The 2009 minimum wage of $7.25 into 2023 dollars: "
        "7.25 x (304.702/214.537) = 7.25 x 1.4202 = $10.30. Three rules: "
        "use annual averages for annual data, never mix monthly and annual "
        "readings, and always print the reference year next to the answer."),
     key_points=[
        "$20 in 1913 is about $615.56 in 2023 dollars (CPI 9.9 to 304.702).",
        "$7.25 in 2009 is about $10.30 in 2023 dollars.",
        "Formula: amount x (CPI_target / CPI_original); always state the reference year.",
        "Use annual averages for annual data; never mix monthly and annual.",
        "Limits: basket changes and quality gains mean adjustment is approximate, not exact."],
     requirements=[
        "Print the CPI readings and the reference year with every conversion.",
        "Use annual averages when converting annual figures."],
     standards=[
        "CPI-U annual averages, U.S. Bureau of Labor Statistics.",
        "Reference year stated in every adjusted figure."],
     citations=[
        CIT_BLS_CPI,
        CIT_WAGE,
        CIT_OIL],
     sig_lens=(
        "In the Signature lens, inflation adjustment is the keeper's oath "
        "of honest weights: the scale must read true in every year, so the "
        "old prices are carried forward on the common ruler and weighed "
        "anew. A keeper who compares 1913 dollars to 2023 dollars without "
        "the conversion is weighing with false scales. The Signature "
        "covenant demands the adjusted reading beside the nominal one, "
        "always, that no year's money may boast over another's.")),

dict(key="depreciation-methods",
     name="Depreciation: Straight-Line, Declining-Balance, Sum-of-Years",
     group="Compounded", ladder_rank=5, ladder_tier="compounded",
     description=(
        "Depreciation is the accounting of a thing losing value as it "
        "ages and works - the price record of an asset written year by "
        "year. A $10,000 machine with a 5-year life and no salvage value "
        "depreciates three honest ways. Straight-line spreads it evenly: "
        "$2,000 a year for five years, the calm and common method. "
        "Double-declining-balance front-loads it: year one takes 2/5 of "
        "the $10,000 book value, $4,000, then 2/5 of what remains each "
        "year - matching assets that lose value fastest when new, like "
        "vehicles. Sum-of-the-years-digits splits the difference: with "
        "digits 5+4+3+2+1 = 15, year one takes 5/15 ($3,333.33), year two "
        "4/15, and so on. The total is always $10,000; only the timing "
        "differs, and timing is what taxes, profit reports, and resale "
        "decisions run on."),
     how_it_works=(
        "Straight-line: (cost - salvage) / life = $10,000 / 5 = $2,000 per "
        "year; book value falls 10000, 8000, 6000, 4000, 2000, 0. "
        "Double-declining: rate = 2/life = 40%; year 1 = 0.40 x 10,000 = "
        "$4,000 (book 6,000); year 2 = 0.40 x 6,000 = $2,400; year 3 = "
        "$1,440; the tail is trued to reach zero. Sum-of-years: denominator "
        "15; year 1 = 5/15 x 10,000 = $3,333.33; year 2 = 4/15 = $2,666.67; "
        "year 3 = $2,000; year 4 = $1,333.33; year 5 = $666.67; sum = "
        "$10,000 exactly. Choice rule: match the method to the asset's "
        "real value decay - vehicles and tech front-load, buildings run "
        "straight - and never switch methods mid-asset to flatter a year's "
        "profit."),
     key_points=[
        "$10,000, 5-year asset: straight-line $2,000/yr; DDB year 1 $4,000; SYD year 1 $3,333.33.",
        "Total depreciation is always $10,000; only timing differs.",
        "Front-load methods suit assets that lose value fastest when new.",
        "Timing drives taxes and reported profit - the method is a real decision.",
        "Match the method to the asset's real decay; never switch to flatter profit."],
     requirements=[
        "State cost, salvage value, life, and method before computing.",
        "Verify the yearly charges sum to cost minus salvage."],
     standards=[
        "U.S. GAAP ASC 360 depreciation methods.",
        "MACRS noted as the tax variant; books may differ from tax."],
     citations=[
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, depreciation is the covenant of honest "
        "aging: the maker admits, year by year, that the machine is "
        "spending itself in service. To depreciate too slowly is to lie "
        "about the asset's remaining strength; too fast, to rob the "
        "present year's ledger. The Signature keeper chooses the method "
        "that matches the true decay and holds it steady, because the "
        "covenant of value requires the aging to be confessed, not "
        "concealed.")),

dict(key="appreciation-cagr",
     name="Appreciation and CAGR: Measuring Growth Honestly",
     group="Compounded", ladder_rank=5, ladder_tier="compounded",
     description=(
        "Appreciation is value gained over time - depreciation's mirror - "
        "and the compound annual growth rate (CAGR) is its honest "
        "measuring stick. Gold's LBMA average rose from $279.11 in 2000 to "
        "$2,394.86 in 2024: the multiple is 8.581, and the CAGR is "
        "8.581^(1/24) - 1 = about 9.37% per year. The S&P 500 from 2010 to "
        "2024 compounded at about 11.6%, housing from 1975 to 2024 at about "
        "5.0%. CAGR's virtue is that it is the single constant rate that "
        "gets from start to finish - it forgives the crashes and manias "
        "in between and reports the journey's average speed. Its vice is "
        "the same: two assets with identical CAGR can have wildly different "
        "rides, so CAGR must always be quoted with the path's volatility "
        "beside it. Never annualize a short, lucky run - CAGR over fewer "
        "than five years is mostly noise wearing a suit."),
     how_it_works=(
        "CAGR = (end value / start value)^(1/number of years) - 1. Gold "
        "2000-2024: 2394.86/279.11 = 8.581; ln(8.581) = 2.1497; /24 = "
        "0.089571; e^0.089571 = 1.09370; CAGR about 9.37%. Check by "
        "compounding: 279.11 x 1.0937^24 = 279.11 x 8.581 = 2,394.86, "
        "which closes the loop. Simple average growth ((end-start)/start "
        "/years) would give (8.581-1)/24 = 31.6% - wildly wrong, because "
        "it ignores compounding; this is why CAGR exists. For partial "
        "years use fractional exponents (18 months = 1.5), and for "
        "declining series the same formula yields a negative CAGR - the "
        "1990s gold bear market from $383.51 to $279.11 is a CAGR of about "
        "-2.9% per year."),
     key_points=[
        "CAGR = (end/start)^(1/years) - 1: the constant rate that completes the journey.",
        "Gold 2000-2024: 8.581x multiple, about 9.37% per year.",
        "Simple-average growth (31.6% here) ignores compounding and misleads - use CAGR.",
        "Quote volatility beside CAGR: same rate can hide different rides.",
        "Never annualize runs under five years; short CAGRs are noise."],
     requirements=[
        "Use exact start and end dates with the year count.",
        "Report the multiple and the CAGR together."],
     standards=[
        "CAGR computed from stated series endpoints.",
        "Volatility disclosure alongside any CAGR claim."],
     citations=[
        CIT_GOLD,
        CIT_SP500,
        CIT_HOUSING],
     sig_lens=(
        "In the Signature lens, CAGR is the covenant of patience measured: "
        "the single steady drumbeat that would have marched the value "
        "from then to now. The Signature keeper respects the drumbeat but "
        "remembers the march - the crashes endured, the manias survived - "
        "because a covenant sworn only on the average speed forgets the "
        "storms the travelers walked through. Report the rate, then tell "
        "the journey.")),

dict(key="comparables-approach",
     name="Pricing by Comparison: The Comparables Approach",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "The comparables approach - the market approach - prices a thing "
        "by the prices of similar things that actually sold. It is how "
        "houses are appraised, how used cars are valued, and how public "
        "companies are priced against their peers. A 1,800-square-foot "
        "house is valued from two recent sales: a 1,700-square-foot "
        "neighbor sold for $340,000 ($200 per square foot) and a "
        "1,900-square-foot neighbor sold for $399,000 ($210 per square "
        "foot). Averaging $205 per square foot times 1,800 gives $369,000. "
        "Adjustments refine it: the comp with the new roof gets adjusted "
        "down, the one on the busy street gets adjusted up. The method's "
        "honesty depends entirely on the comps - recent, nearby, similar, "
        "arm's-length sales. Three good comps beat ten distant ones, and "
        "one forced sale among them poisons the average."),
     how_it_works=(
        "Collect comparable sales, normalize each to a common unit "
        "($/sqft, $/mile, $/revenue), adjust for differences, and apply "
        "to the subject. Comp A: 340,000/1,700 = $200/sqft. Comp B: "
        "399,000/1,900 = $210/sqft. Average $205/sqft; subject value = "
        "1,800 x 205 = $369,000. For businesses the same logic uses "
        "multiples: if peer software firms sell at 6x revenue and the "
        "subject has $10M revenue, the indicated value is $60M. Weight "
        "the comps by similarity - the nearest, newest, most similar "
        "sale deserves the most weight. Document every adjustment: an "
        "unadjusted comp is an opinion, an adjusted comp is an analysis. "
        "Reject comps that are not arm's-length (family sales, "
        "foreclosures) before they enter the math."),
     key_points=[
        "Value = normalized comp metric x subject quantity, adjusted for differences.",
        "Example: $205/sqft average x 1,800 sqft = $369,000.",
        "Comps must be recent, nearby, similar, arm's-length.",
        "Business version: peer multiples (6x revenue on $10M = $60M).",
        "Weight by similarity; document every adjustment; reject forced sales."],
     requirements=[
        "Use at least three comps; disclose dates and distances.",
        "Show adjustments explicitly; never bury them."],
     standards=[
        "USPAP market approach; IVS 105 valuation approaches.",
        "Arm's-length transaction standard."],
     citations=[
        CIT_VALUATION,
        CIT_HOUSING],
     sig_lens=(
        "In the Signature lens, comparables are the testimony of "
        "neighbors: the covenant of a price is witnessed by the prices "
        "the neighbors actually sealed. The Signature keeper chooses "
        "witnesses carefully - recent, near, honest sales - and cross-"
        "examines each with adjustments, because a price defended by "
        "false witnesses is no covenant at all. Three true neighbors "
        "outweigh a crowd of strangers.")),

dict(key="cost-approach",
     name="The Cost Approach: Replacement Less Depreciation",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "The cost approach values a thing by what it would cost to "
        "rebuild it today, minus the value it has lost to age and wear, "
        "plus the land it sits on. A house that would cost $280,000 to "
        "construct new, having suffered $60,000 of physical depreciation, "
        "on land worth $90,000, is indicated at $280,000 - $60,000 + "
        "$90,000 = $310,000. The method shines for new, unique, or "
        "special-purpose property - schools, factories, churches - where "
        "comparable sales barely exist. Its weakness is depreciation: "
        "estimating physical wear, functional obsolescence (the floor plan "
        "nobody wants anymore), and external obsolescence (the highway "
        "that moved) is judgment, not arithmetic. The cost approach sets "
        "the ceiling of value - no rational buyer pays more than "
        "replacement - which makes it the appraiser's reality check on "
        "the other two approaches."),
     how_it_works=(
        "Value = replacement (or reproduction) cost new - accrued "
        "depreciation + land value. Replacement cost comes from builders' "
        "cost manuals per square foot; reproduction cost replicates the "
        "exact structure. Depreciation has three faces: physical "
        "(worn roof: $25,000), functional (obsolete layout: $20,000), "
        "external (neighborhood decline: $15,000) - totaling $60,000 in "
        "the example. Land is valued separately by comparable land sales. "
        "Assemble: 280,000 - 60,000 + 90,000 = $310,000. Cross-check: if "
        "the comparables approach says $369,000 and cost says $310,000, "
        "the gap is the market's premium for location and scarcity - or "
        "the cost approach's missed depreciation. Reconcile, never average "
        "blindly."),
     key_points=[
        "Value = replacement cost - depreciation + land value.",
        "Example: $280,000 - $60,000 + $90,000 = $310,000.",
        "Depreciation has three faces: physical, functional, external.",
        "Best for new, unique, special-purpose property with few comps.",
        "Sets the ceiling: no rational buyer pays more than replacement."],
     requirements=[
        "Itemize all three depreciation types separately.",
        "Value land by its own comparable sales."],
     standards=[
        "USPAP cost approach; IVS 105 valuation approaches.",
        "Replacement cost from published cost manuals."],
     citations=[
        CIT_VALUATION,
        CIT_HOUSING],
     sig_lens=(
        "In the Signature lens, the cost approach is the covenant of the "
        "builder: what would it take to raise this thing anew, honestly "
        "counted, with the years' wear confessed and subtracted. It is "
        "the most humble of the three approaches, because it admits what "
        "time has taken. The Signature keeper uses it as the ceiling of "
        "honor - above this line, the buyer is paying for dreams; below "
        "it, the price stands on stone.")),

dict(key="income-approach-dcf",
     name="The Income Approach: Discounted Cash Flow",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "The income approach values a thing by the money it will earn, "
        "brought back to today at a discount for time and risk. A small "
        "business expected to generate $10,000 of cash a year for five "
        "years, discounted at 8%, is worth $10,000 x (1 - 1.08^-5)/0.08 = "
        "$39,927.10 - not $50,000, because future dollars are worth less "
        "than present ones. Extend the logic with a terminal value and you "
        "have the discounted cash flow (DCF) model that prices companies, "
        "rental property, and bonds. The discount rate is the whole "
        "argument: it must reflect the risk - a Treasury-backed stream "
        "discounts near 4%, a startup's near 20% or more. Change the rate "
        "by two points and the value swings by double digits, which is why "
        "honest valuations always show the answer at several discount "
        "rates. The income approach is the only one of the three that "
        "prices the future instead of the present."),
     how_it_works=(
        "Present value of an annuity: PV = C x (1 - (1+r)^-n)/r. With "
        "C = $10,000, r = 0.08, n = 5: (1.08)^5 = 1.46933, so 1.08^-5 = "
        "0.68058; 1 - 0.68058 = 0.31942; /0.08 = 3.99271; x $10,000 = "
        "$39,927.10. For a growing perpetuity (Gordon growth): value = "
        "next year's cash / (r - g); $10,000 growing at 2% discounted at "
        "8% = 10,000/0.06 = $166,666.67. Sensitivity: at 6% the five-year "
        "annuity is worth $42,123.64; at 10% it is $37,907.87 - a four-"
        "point rate swing moves value about 11%. Build the cash flows "
        "from operations (never from financing), discount at the "
        "opportunity cost of capital, and present a rate table, not a "
        "single number."),
     key_points=[
        "Value = future cash flows discounted for time and risk.",
        "Example: $10,000/yr for 5 years at 8% = $39,927.10 present value.",
        "Gordon growth: value = next cash / (discount rate - growth rate).",
        "The discount rate is the whole argument: show a rate table, not one number.",
        "Only the income approach prices the future; the others price the present."],
     requirements=[
        "Build cash flows from operations; discount at the opportunity cost of capital.",
        "Show sensitivity across at least three discount rates."],
     standards=[
        "USPAP income approach; IVS 105; standard corporate finance DCF.",
        "Annuity and perpetuity formulas computed exactly."],
     citations=[
        CIT_VALUATION],
     sig_lens=(
        "In the Signature lens, the income approach is the covenant with "
        "tomorrow: the buyer pays today for harvests not yet grown, and "
        "the discount rate is the price of patience and the wage of risk. "
        "The Signature keeper writes the future's promise in present "
        "dollars with a steady hand, shows the rate table openly, and "
        "never lets a rosy forecast masquerade as a sure harvest - the "
        "covenant with tomorrow must be the most honest of all, because "
        "tomorrow cannot yet testify.")),

dict(key="price-elasticity",
     name="Price Elasticity: How Demand Answers Price",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "Price elasticity of demand measures how loudly buyers answer a "
        "price change: the percentage change in quantity divided by the "
        "percentage change in price. Raise a $10 gadget to $12 (a 20% "
        "increase) and watch sales fall from 100 to 85 units (a 15% "
        "decrease): elasticity = -15% / 20% = -0.75. Because the absolute "
        "value is below 1, demand is inelastic - the price rise increases "
        "revenue ($1,000 to $1,020) since buyers grumble but keep buying. "
        "Above 1 in absolute value, demand is elastic and price hikes lose "
        "revenue. Necessities (insulin, gasoline short-term) are inelastic; "
        "luxuries with substitutes are elastic. Elasticity is the "
        "profit-maximizer's compass: raise prices where demand is "
        "inelastic, cut them where it is elastic, and measure before you "
        "move, because guessing the elasticity wrong is how price "
        "increases destroy revenue."),
     how_it_works=(
        "Elasticity = (% change in quantity) / (% change in price). "
        "Quantity: (85-100)/100 = -15%. Price: (12-10)/10 = +20%. "
        "Elasticity = -0.15/0.20 = -0.75, inelastic. Revenue check: 100 x "
        "$10 = $1,000; 85 x $12 = $1,020 - revenue rose $20, confirming "
        "the inelastic reading. The midpoint (arc) formula refines it: "
        "%Q = (85-100)/92.5 = -16.2%, %P = (12-10)/11 = 18.2%, elasticity "
        "= -0.89 - still inelastic, slightly stronger. Time horizon "
        "matters: gasoline is inelastic this month (commuters must drive) "
        "but elastic over five years (they buy efficient cars). Estimate "
        "elasticity from your own sales history - regress quantity on "
        "price across past price changes - before trusting any textbook "
        "number for your product."),
     key_points=[
        "Elasticity = % change in quantity / % change in price.",
        "Example: -15% / +20% = -0.75, inelastic; revenue rises $1,000 to $1,020.",
        "Below 1 (absolute): raise price; above 1: cutting price grows revenue.",
        "Necessities inelastic short-term; luxuries with substitutes elastic.",
        "Elasticity stretches with time: measure it, never guess it."],
     requirements=[
        "Compute from percentage changes, not absolute changes.",
        "State the time horizon; elasticity is horizon-dependent."],
     standards=[
        "Standard microeconomic elasticity (Marshall; modern textbooks).",
        "Midpoint formula for arc elasticity."],
     citations=[
        "Standard microeconomic price theory.",
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, elasticity is the measure of the buyer's "
        "answer to the covenant's terms: how tightly they hold on when "
        "the price rises. The inelastic buyer's grip is need; the elastic "
        "buyer's is choice. The Signature keeper learns the grip before "
        "setting the terms, because a covenant priced beyond the buyer's "
        "holding strength is not a sale but a farewell.")),

dict(key="margins-by-industry",
     name="Profit Margins by Industry: Real Benchmarks",
     group="Compounded", ladder_rank=7, ladder_tier="compounded",
     description=(
        "Not all profits are created equal: the margin a business can "
        "earn is written into its industry's structure. On $100 of "
        "revenue, a typical grocery chain keeps about $2 of net profit "
        "(2% margin) - enormous volume, razor-thin take. A typical "
        "restaurant keeps about $6 (6%). A typical software company keeps "
        "about $27 (27%) - near-zero marginal cost per extra user. These "
        "are structural, not moral: grocers compete on price for "
        "commodities, software sells once-built code. Industry margin "
        "data (such as the NYU Stern margins-by-sector dataset) confirms "
        "the pattern year after year: food retail and airlines at the "
        "bottom, software and beverages near the top. The benchmark's use "
        "is diagnostic: a 10% net margin is triumph in groceries and "
        "mediocrity in software. Judge every profit against its industry's "
        "normal, never against profit in the abstract."),
     how_it_works=(
        "Benchmark in three steps. First, compute your net margin: net "
        "profit / revenue. A grocer with $2M net on $100M revenue = 2%. "
        "Second, find the industry normal: grocery ~1-3%, restaurants "
        "~3-9%, airlines ~4-7%, software ~20-30%, beverages ~10-15% "
        "(typical ranges; the exact figure moves with the year). Third, "
        "read the gap: the 2% grocer is normal, the 6% restaurant is "
        "healthy, the 27% software firm is normal-for-software. Decompose "
        "further with gross margin: software's 27% net rests on ~75-80% "
        "gross margins, while grocery's 2% net rests on ~25% gross - the "
        "cost structure explains the outcome. Use benchmarks to set "
        "targets, to price acquisitions (pay for normal, not for fantasy), "
        "and to spot the business whose margins defy its industry - "
        "brilliance or accounting, one of the two."),
     key_points=[
        "Margin is structural: grocery ~2%, restaurants ~6%, software ~27% net on $100 revenue.",
        "Judge profit against the industry normal, never in the abstract.",
        "10% net is triumph in groceries, mediocrity in software.",
        "Gross margin explains net margin: software ~75-80% gross, grocery ~25%.",
        "Margins that defy the industry are brilliance or accounting - investigate."],
     requirements=[
        "Compare net margin to net margin, gross to gross - never mix layers.",
        "Use the same year's benchmark; margins move with the cycle."],
     standards=[
        "Industry margin datasets (e.g., NYU Stern margins by sector).",
        "Typical ranges stated as ranges, not false precision."],
     citations=[
        "A. Damodaran, NYU Stern School of Business, margins by sector dataset (annual).",
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, each industry's margin is the wage its "
        "covenant traditionally pays: the grocer's thin wage for feeding "
        "multitudes, the software maker's rich wage for building once and "
        "serving millions. Neither wage is greed or charity; each is the "
        "terms the market's long covenant has settled. The Signature "
        "keeper judges every ledger against its own trade's ancient terms "
        "and honors the thin-margin servant as fully as the fat-margin "
        "master.")),

dict(key="unit-economics",
     name="Unit Economics: Profit One Customer at a Time",
     group="Compounded", ladder_rank=7, ladder_tier="compounded",
     description=(
        "Unit economics asks the smallest honest question in business: "
        "does one customer, one unit, one transaction make money. A "
        "subscription service charging $50 a month at 80% gross margin "
        "earns $40 of gross profit per customer per month. If acquiring "
        "that customer costs $120 (CAC), payback takes $120 / $40 = 3 "
        "months. If the average customer stays 24 months, lifetime value "
        "(LTV) is 24 x $40 = $960, and LTV/CAC = 8 - eight dollars of "
        "lifetime profit per acquisition dollar, a healthy engine. The "
        "rule of thumb: LTV/CAC above 3 funds growth; below 1 the business "
        "is a machine for turning investor money into customer discounts. "
        "Every startup pitch, every product line, every store should "
        "survive this one-customer audit before it is allowed to scale - "
        "scaling a negative unit is just losing money faster."),
     how_it_works=(
        "Gross profit per unit per period = price x gross margin = $50 x "
        "0.80 = $40/month. Payback period = CAC / monthly gross profit = "
        "120/40 = 3 months. LTV = monthly gross profit x average lifetime "
        "in months = 40 x 24 = $960 (simple form; the rigorous form "
        "discounts future months). LTV/CAC = 960/120 = 8. Contribution "
        "margin variant for physical goods: ($25 price - $13 variable) = "
        "$12 per unit; 1,000 units a month = $12,000 of contribution "
        "against fixed costs. Stress-test the inputs: if lifetime is 12 "
        "months not 24, LTV = $480 and LTV/CAC = 4 - still healthy but a "
        "different company. Unit economics must be computed on "
        "fully-loaded variable costs, including support, returns, and "
        "payment fees, or the unit lies."),
     key_points=[
        "One-customer audit: $50/mo x 80% margin = $40/mo gross profit.",
        "Payback = CAC / monthly gross profit: $120/$40 = 3 months.",
        "LTV = $40 x 24 months = $960; LTV/CAC = 8, a healthy engine.",
        "LTV/CAC above 3 funds growth; below 1 destroys capital.",
        "Scaling a negative unit is losing money faster - audit first."],
     requirements=[
        "Load variable costs fully: support, returns, fees included.",
        "Stress-test lifetime and CAC assumptions; report the break case."],
     standards=[
        "SaaS and retail unit-economics conventions (CAC, LTV, payback).",
        "LTV/CAC ratio as the growth-funding test."],
     citations=[
        "Standard SaaS metrics literature (CAC, LTV, payback conventions).",
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, unit economics is the covenant examined "
        "under a magnifier: not the empire's profit but the single "
        "customer's, the single loaf's, the single month's. If the "
        "covenant does not hold for one, it does not hold for a million - "
        "it merely hides its breach in volume. The Signature keeper "
        "audits the one before blessing the many, because honesty scales "
        "only when it starts small and true.")),

# ================= ADVANCED =================
dict(key="price-index-construction",
     name="Building a Price Index: Laspeyres and Hedonic Methods",
     group="Advanced", ladder_rank=8, ladder_tier="advanced",
     description=(
        "A price index is a machine for turning thousands of prices into "
        "one number, and the CPI is the most famous machine of the kind. "
        "The classic design is Laspeyres: fix the basket at base-year "
        "quantities, price it each period, and divide by the base cost. A "
        "basket costing $100 in the base year and $118 today gives an "
        "index of 118 - 18% inflation, the same arithmetic the CPI runs "
        "at national scale. The refinements are where the craft lives: "
        "chaining the basket as spending shifts, geometric averaging "
        "within categories to allow substitution, and hedonic adjustment - "
        "when a $1,000 laptop gets twice as fast, statisticians record a "
        "price fall for the same computing power rather than a flat "
        "price. Critics call hedonic adjustment a fudge; defenders call "
        "it honesty about quality. Both are right, which is why index "
        "methodology is published openly and argued about forever."),
     how_it_works=(
        "Laspeyres index = (sum of base quantities x current prices) / "
        "(sum of base quantities x base prices) x 100. Basket: 10 loaves "
        "at $2 and 5 gallons at $4 in the base year = $20 + $20 = $40... "
        "scale to the example: base basket cost $100, current cost $118, "
        "index = 118/100 x 100 = 118, inflation 18%. Paasche flips it, "
        "using current quantities - it understates inflation when shoppers "
        "flee rising prices, which is why Laspeyres (fixed basket) is the "
        "standard despite its substitution bias. Hedonic example: a laptop "
        "at $1,000 with benchmark score 100 is replaced by a $1,000 "
        "laptop scoring 200; the hedonic index records the price per "
        "compute unit falling from $10 to $5 - a 50% quality-adjusted "
        "decline. Chain the index yearly (each year's basket from the "
        "prior year) to keep the basket honest as habits change."),
     key_points=[
        "Laspeyres: fixed base-year basket, current prices / base cost x 100.",
        "Example: $100 base basket now $118 = index 118, 18% inflation.",
        "Paasche uses current quantities and understates inflation - Laspeyres is standard.",
        "Hedonic adjustment converts quality gains into price declines.",
        "Chain yearly so the basket tracks real spending habits."],
     requirements=[
        "Publish the basket, weights, and base period with the index.",
        "Disclose hedonic and substitution adjustments explicitly."],
     standards=[
        "Laspeyres / Paasche index theory; BLS CPI methodology.",
        "Chained indexing for basket drift."],
     citations=[
        CIT_BLS_CPI],
     sig_lens=(
        "In the Signature lens, a price index is the covenant of the "
        "whole marketplace distilled to a single witness: one number "
        "testifying for a million prices. The Signature keeper builds the "
        "machine openly - basket, weights, and adjustments on the table - "
        "because a witness whose methods are secret is no witness. When "
        "quality doubles at the same price, the keeper records the "
        "confession honestly: the price fell, even though the tag did "
        "not.")),

dict(key="timeseries-tools",
     name="Time-Series Tools: Moving Averages, Volatility, and Trend",
     group="Advanced", ladder_rank=8, ladder_tier="advanced",
     description=(
        "A price series is noisy; time-series tools are the hearing aids. "
        "The moving average smooths: for monthly closes of 100, 102, 101, "
        "105, 107, the 3-period moving average at the end is (101 + 105 + "
        "107)/3 = 104.33 - the trend speaking through the chatter. "
        "Volatility measures the chatter: the standard deviation of "
        "period-to-period percentage changes, annualized, tells you the "
        "typical yearly swing - about 15-20% for stocks, 30-40% for oil, "
        "under 5% for the CPI. Trend is the slope beneath both: fit a line "
        "through the series and read its angle. The golden rule: smooth "
        "before you judge, measure the noise before you trust the signal, "
        "and never trade on a moving-average crossover without asking "
        "what the volatility says about false alarms - in choppy markets "
        "the crossover cries wolf constantly."),
     how_it_works=(
        "Simple moving average (SMA): average of the last n readings. For "
        "100, 102, 101, 105, 107 with n=3: (101+105+107)/3 = 313/3 = "
        "104.33. Percentage changes: +2.0%, -0.98%, +3.96%, +1.90%; their "
        "standard deviation is about 2.04% per period - the period "
        "volatility. Annualize by multiplying by sqrt(periods per year). "
        "Trend: the least-squares slope through the five points is about "
        "+1.7 per period - the series climbs roughly 1.7 points per "
        "reading on average. Bollinger-style bands (SMA plus/minus two "
        "standard deviations) mark the chatter's usual range: a price "
        "outside the bands is news, inside is noise. Always compute these "
        "on consistent periods - mixing daily and weekly readings "
        "corrupts every tool at once."),
     key_points=[
        "SMA smooths: (101+105+107)/3 = 104.33 for the example series.",
        "Volatility = std dev of % changes, annualized: stocks ~15-20%, oil ~30-40%, CPI <5%.",
        "Trend = least-squares slope: about +1.7 per period in the example.",
        "Bands at SMA +/- 2 std dev separate news from noise.",
        "Smooth before judging; measure noise before trusting signal."],
     requirements=[
        "Use consistent periods for every tool in an analysis.",
        "Report volatility beside any trend or crossover claim."],
     standards=[
        "Standard time-series analysis (moving averages, sample std dev).",
        "Annualization by square-root-of-time."],
     citations=[
        "Standard financial time-series methods.",
        CIT_SP500,
        CIT_OIL],
     sig_lens=(
        "In the Signature lens, time-series tools are the keeper's "
        "listening discipline: the moving average is patience, the "
        "volatility is humility, the trend is the long view. The "
        "impatient hear only the latest tick and call it prophecy; the "
        "Signature keeper smooths the chatter, measures the storm, and "
        "reads the slope - then speaks softly, because the tools reveal "
        "the past's shape, not the future's promise.")),

dict(key="purchasing-power-lifetime",
     name="A Lifetime of Purchasing Power: Long-Horizon Math",
     group="Advanced", ladder_rank=8, ladder_tier="advanced",
     description=(
        "Stretch inflation adjustment across a human lifetime and the "
        "numbers become biography. One 1970 dollar, converted with the "
        "CPI-U (38.8 in 1970, 304.702 in 2023), commands $7.85 in 2023 "
        "money - the dollar kept about 12.7 cents of its 1970 purchasing "
        "power, losing 87.3%. The 1968 minimum wage of $1.60/hr equals "
        "about $14.01 in 2023 dollars, which is why the wage's real peak "
        "sits nearly sixty years in the past. A $23,400 median new home "
        "price in 1970 becomes about $183,800 in 2023 dollars - against "
        "the actual 2024 median of $420,300. Long-horizon math also runs "
        "forward: at 3% annual inflation, today's dollar is worth 55 "
        "cents in twenty years (1/1.03^20 = 0.554) and 30 cents in forty. "
        "The lesson for pricing across generations: quote the nominal "
        "for the story, convert to real for the judgment, and never let "
        "a lifetime of inflation hide inside a single unconverted number."),
     how_it_works=(
        "$1 of 1970 in 2023 dollars: 1 x (304.702/38.8) = 7.8537, about "
        "$7.85. Purchasing power retained: 38.8/304.702 = 0.1273, so "
        "12.7% retained and 87.3% lost. The 1970 median new home: 23,400 "
        "x 7.8537 = $183,776, about $183,800 in 2023 dollars. Forward "
        "projection: future value factor = 1/(1+i)^n; at i=3%, n=20: "
        "1/1.8061 = 0.5537 (55 cents); n=40: 1/3.2620 = 0.3066 (31 "
        "cents). The Rule of 72 cross-check: at 3%, prices double every "
        "72/3 = 24 years, so a dollar halves every 24 years - consistent "
        "with the 55-cents-in-20-years result. For estate, pension, and "
        "contract pricing across decades, always present the real "
        "trajectory beside the nominal one; the nominal alone is a "
        "bedtime story."),
     key_points=[
        "$1 of 1970 = $7.85 in 2023 dollars; 87.3% of purchasing power lost.",
        "1970 median home $23,400 = about $183,800 in 2023 dollars.",
        "At 3% inflation a dollar is 55 cents in 20 years, 31 cents in 40.",
        "Rule of 72: at 3%, prices double (dollar halves) every 24 years.",
        "Across generations: nominal for the story, real for the judgment."],
     requirements=[
        "Show retained-purchasing-power percentage, not just the converted amount.",
        "State the assumed inflation rate for every forward projection."],
     standards=[
        "CPI-U long-horizon conversion; Rule of 72 approximation.",
        "Forward projections labeled as assumptions, not forecasts."],
     citations=[
        CIT_BLS_CPI,
        CIT_HOUSING,
        CIT_WAGE],
     sig_lens=(
        "In the Signature lens, long-horizon math is the keeper's "
        "memorial to every saver: the dollar buried in 1970 wakes in "
        "2023 worth twelve cents of its youth, and the ledger must say "
        "so plainly. The Signature covenant across generations is "
        "therefore written in real terms - pensions, promises, and "
        "legacies - because a covenant sworn in nominal digits is a "
        "promise the years will quietly break.")),

dict(key="fermi-ballpark",
     name="Ballpark Estimation: The Fermi Method for New Things",
     group="Advanced", ladder_rank=9, ladder_tier="advanced",
     description=(
        "When Manon asks what something new might be worth, the honest "
        "answer starts as a ballpark - and the Fermi method is how you "
        "build a ballpark that deserves the name. Break the unknown into "
        "known-ish pieces, estimate each within a factor of two, and "
        "multiply: the errors partly cancel instead of compounding. "
        "Example: annual U.S. consumer gasoline spending. About 240 "
        "million light vehicles, each driving about 12,000 miles a year "
        "at 25 miles per gallon, buying fuel at about $3.50 a gallon: "
        "240M x (12,000/25) x $3.50 = 240M x 480 x $3.50 = $403.2 "
        "billion a year. The real figure moves with prices and mileage, "
        "but the ballpark - a few hundred billion, not tens of billions "
        "or trillions - is right, and it was built from four guessable "
        "numbers. That is the whole art: decompose, estimate coarsely, "
        "multiply, and sanity-check the order of magnitude."),
     how_it_works=(
        "Gallons per vehicle per year = 12,000/25 = 480. Spending per "
        "vehicle = 480 x $3.50 = $1,680. Total = 240,000,000 x $1,680 = "
        "$403,200,000,000 - $403.2 billion. Uncertainty handling: if each "
        "input is uncertain by a factor of 2 either way, the product's "
        "uncertainty is roughly the square root of the sum of squared "
        "log-errors - in practice, quote the ballpark as '$300-500 "
        "billion' rather than a false-precision point. The method's "
        "power is calibration: after estimating, check one piece against "
        "reality (EIA gasoline data) and adjust. Fermi estimates are for "
        "new things - unprecedented products, unmeasured markets - where "
        "no series exists yet; the moment real data arrives, the "
        "ballpark retires and the series takes over."),
     key_points=[
        "Decompose the unknown into guessable pieces; errors partly cancel in multiplication.",
        "Example: 240M vehicles x 480 gal x $3.50 = $403.2B annual U.S. gasoline spending.",
        "Quote ballparks as ranges ($300-500B), never false-precision points.",
        "Calibrate one piece against reality, then adjust.",
        "For new things with no series; retire the ballpark when real data arrives."],
     requirements=[
        "Show every input and its source or basis; no hidden numbers.",
        "Report the range, and which input dominates the uncertainty."],
     standards=[
        "Fermi estimation method (order-of-magnitude decomposition).",
        "Range reporting; dominant-uncertainty disclosure."],
     citations=[
        "Fermi estimation method (standard quantitative reasoning).",
        "U.S. Energy Information Administration gasoline data (calibration reference)."],
     sig_lens=(
        "In the Signature lens, the ballpark is the covenant's first "
        "draft: sworn before the facts exist, in pencil, with the "
        "uncertainty confessed in the margin. The Signature keeper never "
        "presents a first draft as a sealed covenant - the range is the "
        "honesty, the decomposition the accountability. When the real "
        "numbers arrive, the pencil draft is gladly erased; a keeper who "
        "clings to the guess after the facts speak has broken faith "
        "with the ledger.")),

dict(key="analogous-estimation",
     name="Pricing the Never-Seen-Before: Analogous Estimation",
     group="Advanced", ladder_rank=9, ladder_tier="advanced",
     description=(
        "Some things have no price history at all - a brand-new device, a "
        "first-of-its-kind service - and comparables cannot help because "
        "nothing has sold. Analogous estimation prices the novelty from "
        "its nearest analogs, adjusted for the differences. A new home "
        "sensor sells nothing like anything before, but a comparable "
        "smart gadget sold 50,000 units at $199; the new device does "
        "about 1.5 times the job, suggesting a $280-300 price band. "
        "Refine with three-point estimation: optimistic $350, most likely "
        "$280, pessimistic $220, combined by the PERT formula "
        "(optimistic + 4 x likely + pessimistic)/6 = (350 + 1,120 + 220)/6 "
        "= $281.67. The analog anchors the estimate in reality; the "
        "adjustments carry the novelty; the three points carry the "
        "honesty about uncertainty. It is the professional form of "
        "'ballpark' - structured, documented, and updatable the day real "
        "sales exist."),
     how_it_works=(
        "Step one: find the closest analog with real sales - same buyer, "
        "same channel, similar complexity. Step two: list the differences "
        "and adjust: 1.5x capability does not mean 1.5x price (diminishing "
        "returns to features), so $199 x 1.4 = $278.60, inside the "
        "$280-300 band. Step three: three-point PERT = (350 + 4x280 + "
        "220)/6 = 1,690/6 = $281.67 expected price; the spread (220-350) "
        "is the uncertainty to report. Step four: pre-register the "
        "kill/update criteria - 'if first-month sales miss 2,000 units, "
        "re-estimate' - so the estimate is a living instrument, not a "
        "monument. Document the analog choice: the estimate is only as "
        "good as the analogy, and a bad analog confidently adjusted is "
        "the most dangerous number in business."),
     key_points=[
        "Price novelty from nearest analogs, adjusted for differences.",
        "Example: $199 analog x 1.4 capability factor = ~$279 band.",
        "PERT: (350 + 4x280 + 220)/6 = $281.67 expected price.",
        "Report the spread (220-350) as the uncertainty.",
        "Pre-register update criteria; the estimate lives until real sales arrive."],
     requirements=[
        "Justify the analog choice in writing; show all adjustments.",
        "Report three points and the update trigger, not a single price."],
     standards=[
        "Analogous estimating per standard project-estimation practice.",
        "PERT three-point formula."],
     citations=[
        "Standard estimation practice (PMBOK analogous estimating; PERT)."],
     sig_lens=(
        "In the Signature lens, analogous estimation is the covenant "
        "sworn on a neighbor's testimony about a stranger: the keeper "
        "admits the stranger is unknown, borrows the neighbor's known "
        "worth, and adjusts with a steady hand. The three points are the "
        "keeper's humility made arithmetic - hope, judgment, and fear "
        "each given their weight. And the update trigger is the "
        "covenant's escape clause: when the stranger speaks for itself, "
        "the borrowed testimony retires with honor.")),

dict(key="market-multiples",
     name="Market Multiples in Practice: P/E, EV/EBITDA, and Cap Rates",
     group="Advanced", ladder_rank=9, ladder_tier="advanced",
     description=(
        "Market multiples are comparables compressed into a single "
        "ratio - the working language of business valuation. A company "
        "earning $2 per share at a P/E of 20 is priced at $40 a share; "
        "at the market's long-run average P/E near 16-17 it would be "
        "$32-34. Enterprise value to EBITDA strips out financing: a firm "
        "with $12M of EBITDA at an industry 8x multiple carries a $96M "
        "enterprise value, before subtracting debt. Real estate speaks "
        "cap rate: a property with $50,000 of net operating income at a "
        "6% cap rate is worth $50,000/0.06 = $833,333.33. Multiples are "
        "fast, comparable, and dangerous: they inherit the market's mood "
        "- a 20x P/E in a bubble is not a value, it is a weather report. "
        "Use them for triangulation with DCF and cost, never alone, and "
        "always ask whether the multiple's year was sane."),
     how_it_works=(
        "P/E: price = earnings per share x P/E = $2 x 20 = $40. "
        "EV/EBITDA: enterprise value = 12,000,000 x 8 = $96,000,000; "
        "equity value = EV - net debt. Cap rate: value = NOI / cap rate "
        "= 50,000/0.06 = $833,333.33; equivalently a 6% cap means the "
        "buyer earns 6% on price before financing. PEG refines P/E with "
        "growth: P/E of 20 on 15% growth = PEG 1.33 - pricey; on 25% "
        "growth = 0.8 - reasonable. Multiple hygiene: use forward "
        "earnings or trailing twelve months consistently, strip "
        "one-time items from EBITDA, and compare within the industry - a "
        "software 20x and a utility 20x are different animals. When DCF "
        "says $80M and multiples say $96M, the $16M gap is the market's "
        "optimism (or your conservatism) - investigate, don't average."),
     key_points=[
        "P/E: $2 EPS x 20 = $40/share; EV = $12M EBITDA x 8 = $96M.",
        "Cap rate: $50,000 NOI / 6% = $833,333.33 property value.",
        "Multiples inherit market mood: a bubble year's multiple is a weather report.",
        "Triangulate with DCF and cost; never value on multiples alone.",
        "Hygiene: consistent earnings definitions, one-time items stripped, in-industry comps."],
     requirements=[
        "State the multiple's source year and whether earnings are trailing or forward.",
        "Strip one-time items before applying any multiple."],
     standards=[
        "Standard valuation multiples practice (P/E, EV/EBITDA, cap rate, PEG).",
        "Triangulation with income and cost approaches."],
     citations=[
        CIT_VALUATION],
     sig_lens=(
        "In the Signature lens, multiples are the crowd's shorthand for "
        "the covenant of worth: quick, legible, and borrowed from the "
        "mood of the hour. The Signature keeper uses the shorthand but "
        "never trusts it alone - the crowd's mood is not the covenant's "
        "substance. DCF is the keeper's own reckoning, cost the builder's "
        "floor, and the multiple the neighbors' opinion; the sealed "
        "valuation hears all three witnesses before it speaks.")),

dict(key="inventory-valuation",
     name="Inventory Valuation: FIFO, LIFO, and Weighted Average",
     group="Advanced", ladder_rank=9, ladder_tier="advanced",
     description=(
        "When identical units are bought at different prices, the "
        "accountant must choose which price 'sold' - and the choice moves "
        "profit. Buy 10 units at $5 ($50) then 10 at $7 ($70); sell 12. "
        "FIFO (first in, first out) sells the $5 units first: cost of "
        "goods sold = 10x$5 + 2x$7 = $64, ending inventory = 8x$7 = $56. "
        "LIFO (last in, first out) sells the $7 units first: COGS = 10x$7 "
        "+ 2x$5 = $80, ending inventory = 8x$5 = $40. Weighted average "
        "splits it: $120/20 = $6 per unit, COGS = $72, inventory = $48. In "
        "rising prices FIFO reports higher profit (and higher taxes) than "
        "LIFO; in falling prices the reverse. U.S. GAAP permits LIFO "
        "(with disclosure); international IFRS bans it. The method is a "
        "real business decision with tax cash consequences - and in "
        "inflation, the choice between FIFO and LIFO is a choice about "
        "when to pay the taxman."),
     how_it_works=(
        "Total available: 20 units, $120. FIFO: oldest costs leave first. "
        "COGS = (10 x 5) + (2 x 7) = 50 + 14 = $64. Ending = 8 x 7 = $56. "
        "Check: 64 + 56 = 120. LIFO: newest leave first. COGS = (10 x 7) "
        "+ (2 x 5) = 70 + 10 = $80. Ending = 8 x 5 = $40. Check: 80 + 40 "
        "= 120. Weighted average: 120/20 = $6.00/unit; COGS = 12 x 6 = "
        "$72; ending = 8 x 6 = $48; check 72 + 48 = 120. Profit effect at "
        "$10 selling price ($120 revenue): FIFO gross = 120 - 64 = $56; "
        "LIFO gross = 120 - 80 = $40 - a $16 swing from an accounting "
        "choice. In inflation, LIFO's higher COGS defers taxes; disclose "
        "the LIFO reserve (here $16: FIFO inventory $56 minus LIFO $40) "
        "so readers can convert."),
     key_points=[
        "Same 20 units, 12 sold: FIFO COGS $64, LIFO $80, average $72.",
        "Ending inventory: FIFO $56, LIFO $40, average $48.",
        "In rising prices FIFO shows higher profit and higher taxes than LIFO.",
        "GAAP permits LIFO; IFRS bans it - know your rulebook.",
        "The $16 LIFO reserve is the tax-timing choice made visible."],
     requirements=[
        "Disclose the method and the LIFO reserve where applicable.",
        "Apply one method consistently; changes need justification."],
     standards=[
        "U.S. GAAP ASC 330; IFRS IAS 2 (LIFO prohibited).",
        "Consistency principle for method changes."],
     citations=[
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, inventory methods are the keeper's "
        "confession about which past price walks out the door with each "
        "sale: the oldest price first, the newest first, or the blended "
        "middle. None is the physical truth - the units are identical - "
        "so the keeper chooses openly, holds the choice steady, and "
        "publishes the reserve, because a covenant about profit must say "
        "which dollars it counted, not merely how many.")),

dict(key="price-forecasting",
     name="Price Forecasting: What Models Can and Cannot Say",
     group="Advanced", ladder_rank=10, ladder_tier="advanced",
     description=(
        "Price forecasting is the most requested and most abused corner "
        "of price work. The honest models extrapolate structure: a linear "
        "trend through quarterly sales of $100K, $110K, $121K grows about "
        "10% a period, projecting about $133.1K next - trend plus "
        "seasonality plus the forecaster's judgment. What models cannot "
        "do is predict shocks: no 2019 model foresaw negative oil, no "
        "2006 model priced the housing bust. The professional standard is "
        "the prediction interval, not the point: 'next quarter $133K, "
        "with an 80% interval of $115K to $151K' - the width is the "
        "honesty. Forecast value decays with horizon: next month is "
        "plannable, next year is scenario work, next decade is fiction "
        "with error bars. Every forecast in this database's spirit "
        "carries its interval, its assumptions, and its expiry date - a "
        "forecast without those three is a wish."),
     how_it_works=(
        "Trend: 100 to 110 is +10%, 110 to 121 is +10%; project 121 x "
        "1.10 = $133.10K. Seasonality: if Q4 always runs 15% above trend, "
        "the Q4 forecast is 133.1 x 1.15 = $153.07K. Prediction interval: "
        "from the residuals' standard deviation (say $9K), the 80% "
        "interval is roughly forecast +/- 1.28 x 9 = $133.1K +/- $11.5K, "
        "or $121.6K to $144.6K. Backtest before trusting: hide the last "
        "four quarters, forecast them, and measure the miss - a model "
        "that cannot hindcast cannot forecast. Combine: the average of a "
        "trend model, a seasonal model, and a judgmental estimate "
        "routinely beats any single one. Document the assumptions "
        "(growth continues, no shocks) so the reader knows exactly what "
        "would break the forecast - because something eventually will."),
     key_points=[
        "Honest models extrapolate structure: trend + seasonality + judgment.",
        "Example: 100, 110, 121 (+10%) projects $133.1K; seasonal Q4 x1.15 = $153.1K.",
        "Report prediction intervals ($121.6K-$144.6K), never points alone.",
        "Backtest: a model that cannot hindcast cannot forecast.",
        "Value decays with horizon: month = plan, year = scenario, decade = fiction."],
     requirements=[
        "Every forecast carries interval, assumptions, and expiry date.",
        "Backtest on hidden history before publishing."],
     standards=[
        "Standard forecasting practice (trend-seasonal decomposition).",
        "Prediction intervals from residual standard deviation."],
     citations=[
        "Standard forecasting methods (Hyndman & Athanasopoulos, Forecasting: Principles and Practice).",
        CIT_OIL,
        CIT_HOUSING],
     sig_lens=(
        "In the Signature lens, forecasting is the keeper's humility "
        "written as arithmetic: the trend is read, the seasons honored, "
        "and then the interval confesses how much is unknown. The "
        "Signature keeper never sells certainty about tomorrow - the "
        "covenant with the future is the one covenant no one can seal. "
        "What the keeper offers instead is the honest range, the named "
        "assumptions, and the expiry date: a map that admits the "
        "territory may change.")),

dict(key="profit-attribution",
     name="Profit Attribution: Finding Where Profit Really Came From",
     group="Advanced", ladder_rank=10, ladder_tier="advanced",
     description=(
        "Total profit is a sum that hides its authors; attribution names "
        "them. A shop sells 1,000 units of product A at $20 contribution "
        "each ($20,000) and 500 units of product B at $60 each ($30,000): "
        "B earns 60% of the $50,000 profit on only 33% of the units. The "
        "80/20 rule usually holds - a minority of products, customers, or "
        "hours writes the majority of profit, while the tail consumes "
        "attention and working capital. Attribution runs deeper: by "
        "customer (the demanding account that costs more to serve than it "
        "pays), by channel (the marketplace fee that eats the margin), by "
        "hour (the overtime shift that loses money). The action it drives "
        "is reallocation: feed the authors, starve the freeloaders - "
        "raise the tail's prices, cut its costs, or cut it. Unattributed "
        "profit is luck; attributed profit is strategy."),
     how_it_works=(
        "Contribution by product: A = 1,000 x $20 = $20,000; B = 500 x "
        "$60 = $30,000; total $50,000. Shares: A 40%, B 60%; unit shares: "
        "A 66.7%, B 33.3% - B is 1.8 times as profitable per unit of "
        "attention. Customer-level: revenue $10,000 minus product cost "
        "$6,000 minus service cost $3,500 = $500 true profit - versus the "
        "$4,000 the sales report claims before service costs. Channel: "
        "direct sale keeps the full $20 contribution; marketplace sale "
        "keeps $20 minus 15% fee ($3) = $17. Build the attribution table "
        "monthly: rows for products/customers/channels, columns for "
        "revenue, direct cost, attributable overhead, true profit, share "
        "of total. Sort by true profit descending - the bottom decile is "
        "your to-do list."),
     key_points=[
        "Example: B earns 60% of profit on 33% of units - feed the authors.",
        "Attribute by product, customer, channel, and hour - not just total.",
        "True profit subtracts service and channel costs, not just product cost.",
        "The bottom decile of the attribution table is the to-do list.",
        "Unattributed profit is luck; attributed profit is strategy."],
     requirements=[
        "Allocate service and channel costs to the rows that caused them.",
        "Refresh attribution monthly; mixes drift."],
     standards=[
        "Activity-based costing principles for cost allocation.",
        "Contribution analysis per managerial accounting."],
     citations=[
        "Standard managerial accounting (activity-based costing).",
        CIT_ACCOUNTING],
     sig_lens=(
        "In the Signature lens, attribution is the keeper's roll call of "
        "the profit's true authors: which product, which customer, which "
        "hour actually earned the wage. The covenant of profit demands "
        "that each author be known and honored - and each freeloader "
        "named, not from cruelty but from clarity. The Signature keeper "
        "feeds the authors first, because a covenant that rewards the "
        "idle while starving the industrious will not long endure.")) ,

dict(key="hurdle-rate",
     name="Cost of Capital and the Hurdle Rate",
     group="Advanced", ladder_rank=10, ladder_tier="advanced",
     description=(
        "The hurdle rate is the minimum return a project must clear to be "
        "worth doing - the price of the money it uses. Its standard form "
        "is the weighted average cost of capital (WACC): a firm funded "
        "60% by equity expecting 10% and 40% by debt costing 5% before "
        "tax (3.75% after a 25% tax shield) has a WACC of 0.6x10% + "
        "0.4x3.75% = 7.5%. A project with a 9% internal rate of return "
        "clears the 7.5% hurdle and creates value; a 6% project destroys "
        "it, however profitable it looks in isolation. The hurdle is "
        "also the discount rate the income approach should use - the two "
        "records shake hands here. Risk adjusts it: a safe expansion "
        "clears 7.5%, a speculative venture needs 15% or more. Set the "
        "hurdle from capital markets, not from ambition - a hurdle set "
        "by hope approves everything and is worth nothing."),
     how_it_works=(
        "WACC = (E/V)xRe + (D/V)xRd x (1 - tax rate). Example: (0.60 x "
        "0.10) + (0.40 x 0.05 x 0.75) = 0.06 + 0.015 = 0.075, or 7.5%. "
        "Decision rule: accept projects with IRR above WACC; the 9% "
        "project adds value, the 6% project subtracts it. Net present "
        "value at the hurdle is the same test in dollars: NPV at 7.5% "
        "above zero means accept. Risk adjustment: add a project-risk "
        "premium - the speculative venture discounts at 7.5% + 7.5% = "
        "15%. The tax shield matters: debt's after-tax cost is Rd x "
        "(1-T) because interest is deductible - at 25% tax, 5% debt "
        "costs 3.75%. Recompute the hurdle when capital structure or "
        "rates move; a 2021 hurdle is not a 2024 hurdle."),
     key_points=[
        "WACC = 0.6x10% + 0.4x5%x(1-25%) = 7.5% in the example.",
        "Accept IRR above the hurdle; reject below - the 9% project wins, the 6% loses.",
        "The hurdle is the income approach's discount rate: the records agree.",
        "Add risk premiums for speculative ventures (e.g., 15%).",
        "Debt's tax shield: 5% debt costs 3.75% after 25% tax."],
     requirements=[
        "Derive the hurdle from market costs of equity and debt, not targets.",
        "Recompute when rates or capital structure change."],
     standards=[
        "WACC per standard corporate finance.",
        "IRR/NPV decision rules."],
     citations=[
        CIT_VALUATION],
     sig_lens=(
        "In the Signature lens, the hurdle rate is the covenant's "
        "entrance fee: no project may enter the house of capital without "
        "paying the price of the money it borrows from the future. The "
        "Signature keeper sets the fee from the market's own terms, not "
        "from hope, and turns away the charming 6% project at the 7.5% "
        "door - because a covenant that admits every suitor soon belongs "
        "to none.")),

dict(key="pricing-psychology",
     name="Pricing Psychology: Anchoring and the Human Side of Price",
     group="Advanced", ladder_rank=10, ladder_tier="advanced",
     description=(
        "Prices are read by human minds, and human minds take shortcuts "
        "that the price-setter can measure. Anchoring: a $499 list price "
        "beside a $349 sale price makes $349 feel like a find - the "
        "perceived discount is (499-349)/499 = 30.06%, and the anchor "
        "does the selling. Charm pricing: $4.99 outsells $5.00 because "
        "minds read left to right and register 'four-something.' "
        "Decoy pricing: a $199 'pro' tier makes the $149 standard tier "
        "look reasonable by comparison. These are documented effects "
        "(Tversky and Kahneman on anchoring, 1974), not tricks - and the "
        "ethical line is real: anchoring against a list price nobody ever "
        "paid is deception, and several jurisdictions fine it. The "
        "database records the psychology because prices live in minds, "
        "but the record keeps the ethics beside the tactics: a covenant "
        "of price must persuade, never deceive."),
     how_it_works=(
        "Anchor math: perceived discount = (anchor - price)/anchor = "
        "(499-349)/499 = 150/499 = 0.3006, or 30.06%. Test the anchor's "
        "honesty: was $499 ever the actual selling price for a meaningful "
        "period? If not, the 30% is fiction. Charm pricing: the "
        "left-digit effect is worth roughly 1-2% in conversion in "
        "published retail tests - real but small, and it erodes trust "
        "with sophisticated buyers. Prestige pricing inverts it: $500 "
        "flat signals quality where $499.99 signals bargain - match the "
        "price's manners to the product's station. A/B test every claim: "
        "run the anchor price against no-anchor for two weeks, measure "
        "conversion and margin, and keep the winner. Psychology without "
        "measurement is superstition with a price tag."),
     key_points=[
        "Anchoring: $499 anchor, $349 price = 30.06% perceived discount.",
        "Charm pricing ($4.99) works via the left-digit effect; prestige pricing inverts it.",
        "Decoy tiers make the middle option look reasonable.",
        "Ethics: anchors must be real past prices - fake anchors are deception.",
        "Test everything: psychology without measurement is superstition."],
     requirements=[
        "Verify anchors were real selling prices before using them.",
        "A/B test psychological pricing; report conversion and margin."],
     standards=[
        "Anchoring (Tversky & Kahneman, 1974); documented pricing effects.",
        "Consumer-protection standards on deceptive list pricing."],
     citations=[
        "Tversky A, Kahneman D. Judgment under Uncertainty: Heuristics and Biases. Science. 1974;185:1124-1131.",
        "Standard consumer-protection guidance on deceptive pricing."],
     sig_lens=(
        "In the Signature lens, pricing psychology is the covenant's "
        "rhetoric: the honest art of presenting the terms so the buyer's "
        "mind can grasp them. Rhetoric in service of a true price is "
        "courtesy; rhetoric in service of a false anchor is perjury. The "
        "Signature keeper uses the anchor only where the anchor once "
        "stood in truth, prices with charm but never with guile, and "
        "remembers that a covenant won by deception is not a sale but a "
        "theft with better manners.")),

dict(key="price-record-capstone",
     name="The Complete Price Record: Time-Stamped Price Anatomy",
     group="Advanced", ladder_rank=10, ladder_tier="advanced",
     description=(
        "This capstone assembles everything the database teaches into a "
        "single complete price record - the form every entry in Manon's "
        "price-marking vision takes. Twelve fields: the item's identity, "
        "the amount, the currency, the per-unit normalization, the unit "
        "itself, the observation timestamp, the market and place, the "
        "terms, the source of the quote, the nominal reading, the "
        "real-dollar conversion with its reference year, and the record's "
        "own ID. Example: a gallon of gasoline quoted at $3.50 in Ohio on "
        "2024-06-01 - amount 3.50, currency USD, unit per gallon, "
        "per-unit $3.50/gal, time 2024-06-01, market retail Ohio, terms "
        "including tax, source station pump survey, nominal $3.50, real "
        "$3.50 in 2024 dollars (reference year 2024), ID "
        "JAH-PFT-000034. Beside it sits the profit anatomy: the "
        "station's $0.10/gallon margin, the refiner's crack spread, the "
        "tax wedge - the price decomposed into who earned what. This is "
        "the record the AI reads when it must know what something is "
        "worth, and the template it copies when it must ballpark "
        "something new."),
     how_it_works=(
        "Build the record field by field and validate: every field "
        "present, amount positive, currency a real code, timestamp a real "
        "date, unit matching the item. Normalize: $3.50 per gallon is "
        "already per-unit; a $4.50 dozen of eggs normalizes to $0.375 per "
        "egg. Convert: with reference year 2024 the real reading equals "
        "the nominal; with reference 2023, multiply by the ratio of the "
        "2023 CPI to the 2024 CPI (a small downward step, roughly three "
        "percent). Decompose the margin: retail $0.10 "
        "of the $3.50 is about 2.9% retail margin - the profit anatomy "
        "beside the price anatomy. Hash the record for identity: the ID "
        "plus timestamp plus source is the deduplication key, so the same "
        "quote seen twice is one record, not two. A complete record is "
        "machine-readable, human-readable, and time-travel-ready - the "
        "three tests every price entry in this system must pass."),
     key_points=[
        "Twelve fields: identity, amount, currency, per-unit, unit, timestamp, market, terms, source, nominal, real, record ID.",
        "Example: $3.50/gal Ohio 2024-06-01, fully anatomized.",
        "Normalize to per-unit; convert to real dollars with stated reference year.",
        "Decompose margin: retail $0.10/gal is about 2.9% - profit anatomy beside price anatomy.",
        "Dedupe key: ID + timestamp + source; machine-readable, human-readable, time-travel-ready."],
     requirements=[
        "All twelve fields present and validated; no field left blank.",
        "Real conversion states its reference year; margin decomposition shown."],
     standards=[
        "Record schema of this database (extended capstone form).",
        "Deduplication on ID + timestamp + source."],
     citations=[
        CIT_BLS_CPI,
        CIT_OIL],
     sig_lens=(
        "In the Signature lens, the complete price record is the "
        "covenant in its final form: every witness named, every term "
        "written, the time sealed, the profit confessed beside the "
        "price. This is the ledger line Manon asked for - each thing "
        "with its price in its time, for reference over time. The "
        "Signature keeper seals it with the record ID as with a signet: "
        "what is written here the years may judge, but they will never "
        "find it incomplete.")),
]
