#!/usr/bin/env python3
"""PHASE K — company data: 48 sector companies (new) + 12 enrichment companies.

All financial figures are publicly reported figures, labeled approximate and
reported, with filing citations. Leadership is as publicly reported. Nothing
fabricated: where a figure is uncertain it is omitted or hedged.
"""

SECTORS = [
    # (slug_base, sector label, singular record kind)
    ("technology-companies", "Technology", "technology company record"),
    ("finance-companies", "Finance", "finance company record"),
    ("automotive-companies", "Automotive", "automotive company record"),
    ("healthcare-companies", "Healthcare", "healthcare company record"),
    ("retail-consumer-companies", "Retail and Consumer", "retail and consumer company record"),
    ("energy-industrial-companies", "Energy and Industrial", "energy and industrial company record"),
    ("media-entertainment-companies", "Media and Entertainment", "media and entertainment company record"),
    ("telecom-companies", "Telecom", "telecom company record"),
]

# ---------------------------------------------------------------- technology
TECH = [
    dict(key="tsmc", name="Taiwan Semiconductor Manufacturing Company", short="TSMC",
         group="Semiconductors", industry="Semiconductors — pure-play foundry",
         founded="1987", hq="Hsinchu, Taiwan",
         ceo="C.C. Wei (chairman and CEO, as publicly reported)",
         ticker="2330.TW / TSM", filing="Form 20-F annual report",
         employees="approximately 83,000 (reported)",
         revenue="approximately NT$2.9 trillion (about US$90 billion) in reported 2024 revenue",
         history=("Founded in 1987 in Hsinchu, Taiwan, by Morris Chang, TSMC pioneered the "
                  "pure-play foundry model: manufacturing chips designed by other companies rather "
                  "than selling its own branded chips. Backed in its early years by the Taiwanese "
                  "government and Philips, it grew alongside the fabless semiconductor revolution, "
                  "becoming the indispensable manufacturer for Apple, NVIDIA, AMD, Qualcomm, and "
                  "Broadcom. Its march through process nodes — 7nm, 5nm, 3nm — kept it roughly a "
                  "generation ahead of rivals, and its Arizona fabrication plants mark its first "
                  "major advanced-node manufacturing in the United States."),
         products=("Advanced logic semiconductors on leading process nodes (3nm, 5nm, 7nm and mature "
                   "nodes); wafer manufacturing for smartphones, high-performance computing, AI "
                   "accelerators, automotive, and IoT customers. TSMC does not sell branded chips — "
                   "its product is manufacturing capacity and process technology."),
         model=("TSMC earns revenue by selling wafer manufacturing capacity and advanced process "
                "technology to fabless chip designers. Customers pay per wafer with pricing that "
                "rises steeply at leading nodes. The model depends on enormous, continuous capital "
                "expenditure (tens of billions of US dollars per year as publicly reported) to stay "
                "a node ahead, plus deep co-engineering partnerships in which customers design to "
                "TSMC's process design kits years before volume production."),
         milestones=["1987: founded by Morris Chang in Hsinchu, Taiwan",
                     "Pioneered the pure-play foundry business model",
                     "Volume production of 7nm (2018), 5nm (2020), and 3nm (2022) process nodes",
                     "Arizona fabs announced — first advanced-node TSMC manufacturing in the US"],
         records_note=("Files annual reports on Form 20-F with the US SEC and reports to the Taiwan "
                       "Stock Exchange. Listed in Taipei (2330) and New York (TSM, ADR)."),
         citation=("Company annual report (Form 20-F); Taiwan Stock Exchange filings. "
                   "Figures rounded as reported.")),
    dict(key="amd", name="Advanced Micro Devices, Inc.", short="AMD",
         group="Semiconductors", industry="Semiconductors — processors and GPUs",
         founded="1969", hq="Santa Clara, California, USA",
         ceo="Lisa Su (chair and CEO, as publicly reported)",
         ticker="AMD", filing="Form 10-K annual report",
         employees="approximately 28,000 (reported)",
         revenue="approximately US$25.8 billion in reported 2024 revenue",
         history=("Founded in 1969 in Sunnyvale, California, by Jerry Sanders and seven colleagues "
                  "from Fairchild Semiconductor, AMD spent decades as Intel's scrappy rival in PC "
                  "processors. Near-bankruptcy in the mid-2010s gave way to a turnaround under Lisa "
                  "Su (CEO from 2014): the Zen CPU architecture restored competitiveness, EPYC won "
                  "the data-center market, and the US$49 billion acquisition of Xilinx (completed "
                  "2022) added adaptive computing. AMD is now the leading challenger across CPUs, "
                  "gaming GPUs, and AI accelerators."),
         products=("Ryzen desktop and mobile CPUs, EPYC data-center processors, Radeon graphics, "
                   "Instinct AI accelerators, Xilinx adaptive SoCs and FPGAs, semi-custom chips for "
                   "game consoles (PlayStation, Xbox)."),
         model=("AMD is fabless: it designs processors and accelerators and pays foundries "
                "(chiefly TSMC) to manufacture them. Revenue comes from selling chips into PCs, "
                "data centers, gaming, and embedded markets. The model trades fabrication control "
                "for R&D focus, living or dying on architectural leadership against Intel and "
                "NVIDIA."),
         milestones=["1969: founded by Jerry Sanders and colleagues",
                     "2014: Lisa Su becomes CEO, beginning the turnaround",
                     "2017: Zen architecture launches, restoring CPU competitiveness",
                     "2022: completes US$49 billion Xilinx acquisition (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq (AMD). "
                       "Fabless — manufacturing disclosures center on foundry partners."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="oracle", name="Oracle Corporation", short="Oracle",
         group="Enterprise Software", industry="Enterprise software and cloud",
         founded="1977", hq="Austin, Texas, USA",
         ceo="Safra Catz (CEO, as publicly reported)",
         ticker="ORCL", filing="Form 10-K annual report",
         employees="approximately 164,000 (reported)",
         revenue="approximately US$53 billion in reported fiscal 2024 revenue",
         history=("Founded in 1977 in Santa Clara, California, by Larry Ellison, Bob Miner, and Ed "
                  "Oates as Software Development Laboratories, Oracle built the first commercial "
                  "SQL relational database and rode it to dominance of enterprise data. Aggressive "
                  "acquisitions — PeopleSoft, Siebel, Sun Microsystems (2010, bringing Java and "
                  "SPARC), NetSuite — made it a full-stack enterprise vendor. The 2010s brought a "
                  "pivot to cloud: Oracle Cloud Infrastructure (OCI) and Fusion cloud applications "
                  "now drive growth, and headquarters moved to Austin, Texas, in 2020."),
         products=("Oracle Database, Oracle Cloud Infrastructure (compute, storage, AI infrastructure), "
                   "Fusion Cloud ERP/HCM applications, NetSuite, Java, MySQL."),
         model=("Oracle earns through database licenses and support contracts, cloud subscriptions "
                "(OCI and Fusion applications), and consulting. The shift from upfront licenses to "
                "recurring cloud subscriptions is the core of its modern strategy; large government "
                "and enterprise contracts provide durable, high-margin revenue."),
         milestones=["1977: founded by Ellison, Miner, and Oates",
                     "1979: first commercial SQL relational database",
                     "2010: acquires Sun Microsystems (Java, SPARC)",
                     "2020: headquarters moves to Austin, Texas; cloud pivot accelerates"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (ORCL). "
                       "Founder Larry Ellison remains chairman and CTO as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="salesforce", name="Salesforce, Inc.", short="Salesforce",
         group="Enterprise Software", industry="Enterprise software — CRM and cloud",
         founded="1999", hq="San Francisco, California, USA",
         ceo="Marc Benioff (chair and CEO, as publicly reported)",
         ticker="CRM", filing="Form 10-K annual report",
         employees="approximately 72,000 (reported)",
         revenue="approximately US$34.9 billion in reported fiscal 2024 revenue",
         history=("Founded in 1999 in San Francisco by Marc Benioff, Parker Harris, Dave "
                  "Moellenhoff, and Frank Dominguez, Salesforce pioneered software-as-a-service: "
                  "'No Software' was the founding slogan, replacing installed CRM with a "
                  "subscription web app. It grew into the dominant CRM platform and an acquisition "
                  "machine — Tableau (2019), MuleSoft (2018), and Slack (2021, ~US$27.7 billion as "
                  "reported). The current chapter centers on Agentforce, its AI-agent platform for "
                  "enterprise workflows."),
         products=("Sales Cloud, Service Cloud, Marketing Cloud, Commerce Cloud, Slack, Tableau "
                   "analytics, MuleSoft integration, Agentforce AI agents."),
         model=("Salesforce sells subscriptions to its cloud platforms, priced per user or per "
                "consumption unit, with professional services attached. Growth comes from expanding "
                "seats within existing customers, cross-selling clouds, and large acquisitions "
                "folded into the platform."),
         milestones=["1999: founded; 'No Software' SaaS pioneer",
                     "2004: IPO on NYSE",
                     "2021: completes Slack acquisition (~US$27.7 billion as reported)",
                     "Agentforce launches the AI-agent chapter"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (CRM). "
                       "Fiscal year ends January 31."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="broadcom", name="Broadcom Inc.", short="Broadcom",
         group="Networking & Chips", industry="Semiconductors and infrastructure software",
         founded="2016 (current form)", hq="Palo Alto, California, USA",
         ceo="Hock Tan (president and CEO, as publicly reported)",
         ticker="AVGO", filing="Form 10-K annual report",
         employees="approximately 37,000 (reported)",
         revenue="approximately US$51.6 billion in reported fiscal 2024 revenue",
         history=("Broadcom's lineage traces to the 1961 semiconductor division of Hewlett-Packard "
                  "(via Agilent and Avago Technologies). In 2016 Avago acquired the original "
                  "Broadcom Corporation for ~US$37 billion and took its name. Under Hock Tan, the "
                  "company perfected a disciplined acquisition model — CA Technologies (2018), "
                  "Symantec's enterprise business (2019), and VMware (~US$69 billion, completed "
                  "2023 as reported) — converting mature franchises into cash machines while "
                  "leading in networking and custom AI chips."),
         products=("Networking and broadband semiconductors, custom AI accelerators (TPU-class custom "
                   "silicon with hyperscalers), storage and optical components, VMware virtualization "
                   "and private-cloud software."),
         model=("Broadcom combines high-margin semiconductor franchises with acquired enterprise "
                "software converted to subscription licensing (the VMware playbook). R&D is "
                "concentrated and lean; capital returns to shareholders. The model rewards "
                "pricing power in niches where switching costs are extreme."),
         milestones=["1961 roots: HP semiconductor division; 2016: Avago–Broadcom combination",
                     "2018–2019: CA Technologies and Symantec enterprise acquisitions",
                     "2023: completes VMware acquisition (~US$69 billion as reported)",
                     "Custom AI silicon partnerships with major hyperscalers"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq (AVGO). "
                       "Fiscal year ends in late October/early November."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="cisco", name="Cisco Systems, Inc.", short="Cisco",
         group="Networking & Chips", industry="Networking hardware, software, security",
         founded="1984", hq="San Jose, California, USA",
         ceo="Chuck Robbins (chair and CEO, as publicly reported)",
         ticker="CSCO", filing="Form 10-K annual report",
         employees="approximately 90,000 (reported)",
         revenue="approximately US$53.8 billion in reported fiscal 2024 revenue",
         history=("Founded in 1984 by Stanford computer scientists Leonard Bosack and Sandy Lerner, "
                  "Cisco built the routers that carried the commercial internet's explosive growth "
                  "in the 1990s, briefly becoming the world's most valuable company in 2000. John "
                  "Chambers' acquisition engine (200+ deals) expanded it into switching, voice, "
                  "video, and security. Under Chuck Robbins (CEO from 2015) Cisco pivoted toward "
                  "software subscriptions and security, capped by the ~US$28 billion Splunk "
                  "acquisition (completed 2024 as reported)."),
         products=("Enterprise and service-provider routers and switches, Webex collaboration, "
                   "cybersecurity portfolio, Splunk observability and data platform, Silicon One "
                   "networking chips."),
         model=("Cisco earns from networking hardware plus fast-growing software subscriptions and "
                "services. The strategy is to convert its installed base of enterprise networks "
                "into recurring revenue (networking + security + observability), with acquisitions "
                "filling portfolio gaps."),
         milestones=["1984: founded by Bosack and Lerner at Stanford",
                     "1990: IPO; routers power the 1990s internet boom",
                     "2015: Chuck Robbins becomes CEO; subscription pivot begins",
                     "2024: completes Splunk acquisition (~US$28 billion as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq (CSCO). "
                       "Fiscal year ends the last Saturday in July."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
]

# ------------------------------------------------------------------ finance
FINANCE = [
    dict(key="jpmorgan", name="JPMorgan Chase & Co.", short="JPMorgan Chase",
         group="Banking", industry="Banking and financial services",
         founded="2000 (merger)", hq="New York, New York, USA",
         ceo="Jamie Dimon (chairman and CEO, as publicly reported)",
         ticker="JPM", filing="Form 10-K annual report",
         employees="approximately 317,000 (reported)",
         revenue="approximately US$177 billion in reported 2024 revenue (managed basis)",
         history=("Formed in 2000 by the merger of J.P. Morgan & Co. and Chase Manhattan, with "
                  "roots reaching to the Bank of the Manhattan Company (1799) and J.P. Morgan's "
                  "19th-century banking house. Under Jamie Dimon (CEO from 2005), it absorbed Bear "
                  "Stearns and Washington Mutual during the 2008 crisis and became the largest US "
                  "bank by assets, as well as a dominant investment bank, card issuer, and asset "
                  "manager."),
         products=("Consumer and community banking (Chase branches, cards), corporate and "
                   "investment banking, commercial banking, asset and wealth management."),
         model=("The bank earns net interest income on loans and deposits, plus fees from "
                "investment banking, trading, card interchange, and asset management. Scale across "
                "consumer and wholesale banking diversifies revenue through credit cycles."),
         milestones=["2000: J.P. Morgan–Chase Manhattan merger",
                     "2005: Jamie Dimon becomes CEO",
                     "2008: acquires Bear Stearns and Washington Mutual",
                     "Largest US bank by assets (as publicly reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (JPM). "
                       "Regulated as a global systemically important bank (G-SIB)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="bofa", name="Bank of America Corporation", short="Bank of America",
         group="Banking", industry="Banking and financial services",
         founded="1998 (merger)", hq="Charlotte, North Carolina, USA",
         ceo="Brian Moynihan (chair and CEO, as publicly reported)",
         ticker="BAC", filing="Form 10-K annual report",
         employees="approximately 214,000 (reported)",
         revenue="approximately US$102 billion in reported 2024 revenue",
         history=("Created in 1998 when NationsBank acquired BankAmerica, with roots to Amadeo "
                  "Giannini's Bank of Italy (1904, San Francisco), built to serve immigrants and "
                  "small borrowers. The 2008 acquisition of Merrill Lynch made it a wealth-"
                  "management giant. Under Brian Moynihan (CEO from 2010), it rebuilt capital, "
                  "settled crisis-era litigation, and invested heavily in digital banking."),
         products=("Consumer banking, Merrill wealth management, global corporate and investment "
                   "banking, global markets trading."),
         model=("Net interest income from a vast deposit base plus fees from wealth management "
                "(Merrill), investment banking, and trading. Digital scale — tens of millions of "
                "active digital users as publicly reported — lowers servicing cost per customer."),
         milestones=["1904 roots: Bank of Italy founded by Giannini",
                     "1998: NationsBank–BankAmerica merger creates Bank of America",
                     "2008: acquires Merrill Lynch",
                     "2010: Brian Moynihan becomes CEO"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (BAC). "
                       "Regulated as a G-SIB."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="visa", name="Visa Inc.", short="Visa",
         group="Payments", industry="Payments network",
         founded="1958 (as BankAmericard)", hq="San Francisco, California, USA",
         ceo="Ryan McInerney (CEO, as publicly reported)",
         ticker="V", filing="Form 10-K annual report",
         employees="approximately 31,000 (reported)",
         revenue="approximately US$35.9 billion in reported fiscal 2024 net revenue",
         history=("Began in 1958 as BankAmericard, Bank of America's licensed credit-card program; "
                  "the member-owned Visa network was formed in 1976 and went public in 2008 in what "
                  "was then the largest US IPO. Visa does not issue cards or set cardholder rates — "
                  "it operates the rails: authorizing, clearing, and settling trillions in payments "
                  "volume annually as publicly reported."),
         products=("Global electronic payments network; credit, debit, and prepaid processing; "
                   "value-added services in risk, data, and digital identity."),
         model=("Visa earns primarily from service and data-processing fees tied to payments volume "
                "and cross-border transactions, plus value-added services. It takes no credit risk — "
                "issuing banks do — making it a high-margin toll road on global commerce."),
         milestones=["1958: BankAmericard launches",
                     "1976: Visa network formed",
                     "2008: IPO — then the largest in US history",
                     "Processes trillions in annual payments volume (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (V). "
                       "Fiscal year ends September 30."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="mastercard", name="Mastercard Incorporated", short="Mastercard",
         group="Payments", industry="Payments network",
         founded="1966", hq="Purchase, New York, USA",
         ceo="Michael Miebach (CEO, as publicly reported)",
         ticker="MA", filing="Form 10-K annual report",
         employees="approximately 35,000 (reported)",
         revenue="approximately US$28.2 billion in reported 2024 net revenue",
         history=("Founded in 1966 as the Interbank Card Association by California banks answering "
                  "BankAmericard; the Mastercard brand arrived in 1979 (via Master Charge). It "
                  "converted from a bank association to a public company in 2006. Like Visa, it "
                  "operates the network rather than issuing cards, and has expanded into "
                  "data-analytics and cybersecurity services."),
         products=("Global payments network; credit, debit, and prepaid processing; data and "
                   "analytics, fraud and cyber-intelligence services."),
         model=("Revenue comes from assessments on payments volume and transaction-processing fees, "
                "plus fast-growing services (data, security, consulting). No consumer credit risk; "
                "margins among the highest in financial services as publicly reported."),
         milestones=["1966: Interbank Card Association founded",
                     "1979: Mastercard brand adopted",
                     "2006: IPO after association-to-corporation conversion",
                     "Expansion into data and cyber services"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (MA)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="berkshire", name="Berkshire Hathaway Inc.", short="Berkshire Hathaway",
         group="Diversified Finance", industry="Conglomerate — insurance, rail, energy, holdings",
         founded="1839 (textile mill)", hq="Omaha, Nebraska, USA",
         ceo="Warren Buffett (chairman and CEO, as publicly reported)",
         ticker="BRK.A / BRK.B", filing="Form 10-K annual report",
         employees="approximately 392,000 (reported)",
         revenue="approximately US$371 billion in reported 2024 revenue",
         history=("A Rhode Island textile mill founded in 1839; Warren Buffett began buying control "
                  "in the 1960s and converted it into a holding company. Insurance float from "
                  "GEICO and Berkshire Hathaway Reinsurance funded acquisitions: BNSF Railway "
                  "(2010), Berkshire Hathaway Energy, Precision Castparts, plus a vast equity "
                  "portfolio. Buffett's annual shareholder letters are among the most-read "
                  "documents in business."),
         products=("Insurance (GEICO, reinsurance), BNSF freight rail, Berkshire Hathaway Energy, "
                   "manufacturing and retail subsidiaries, large equity portfolio."),
         model=("Insurance operations generate investable 'float'; wholly owned operating "
                "businesses throw off cash; both fund long-hold equity investments. Decentralized "
                "management with extreme capital allocation discipline at the top."),
         milestones=["1839: textile origins; 1960s: Buffett takes control",
                     "1996: acquires GEICO outright",
                     "2010: acquires BNSF Railway (~US$26 billion as reported)",
                     "Annual shareholder letters — a business canon"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE "
                       "(BRK.A/BRK.B). Never split BRK.A; no dividend as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="amex", name="American Express Company", short="American Express",
         group="Diversified Finance", industry="Payments, cards, travel services",
         founded="1850", hq="New York, New York, USA",
         ceo="Stephen Squeri (chairman and CEO, as publicly reported)",
         ticker="AXP", filing="Form 10-K annual report",
         employees="approximately 75,000 (reported)",
         revenue="approximately US$66 billion in reported 2024 revenue",
         history=("Founded in 1850 in Buffalo, New York, as an express mail company, American "
                  "Express invented the traveler's cheque (1891) and the charge card (1958). Unlike "
                  "Visa and Mastercard, it operates a closed-loop network — issuer, network, and "
                  "acquirer — and lends directly, targeting premium spenders and small businesses."),
         products=("Charge and credit cards (Platinum, Gold, Green), merchant acquiring network, "
                   "travel and lifestyle services, small-business lending."),
         model=("Revenue mixes discount fees from merchants, net interest on card loans, and annual "
                "card fees. The premium customer base spends several times the industry average as "
                "publicly reported, supporting high merchant fees."),
         milestones=["1850: founded as express mail company",
                     "1891: traveler's cheque; 1958: charge card",
                     "Closed-loop network: issuer + network + acquirer",
                     "Premium-spend customer strategy"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (AXP). "
                       "Regulated as a bank holding company."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
]

# ---------------------------------------------------------------- automotive
AUTO = [
    dict(key="volkswagen", name="Volkswagen AG", short="Volkswagen",
         group="German Automakers", industry="Automotive manufacturing",
         founded="1937", hq="Wolfsburg, Germany",
         ceo="Oliver Blume (CEO, as publicly reported)",
         ticker="VOW.DE", filing="Annual report",
         employees="approximately 684,000 (reported)",
         revenue="approximately EUR 322 billion in reported 2024 revenue",
         history=("Founded in 1937 in Germany to build the 'people's car,' Volkswagen grew from "
                  "the Beetle into Europe's largest automaker and one of the world's largest, "
                  "assembling a brand empire: Audi, Porsche, Skoda, SEAT, Bentley, Lamborghini, "
                  "and commercial vehicles (MAN, Scania). The 2015 diesel-emissions scandal cost "
                  "tens of billions as reported and forced a strategic pivot; the group now "
                  "invests heavily in electric platforms (MEB, PPE) while managing the industry's "
                  "hardest transition."),
         products=("Passenger cars across VW, Audi, Porsche, Skoda, SEAT, Bentley, Lamborghini; "
                   "commercial vehicles; electric models on MEB/PPE platforms; financial services."),
         model=("Volume manufacturing across shared platforms and modular architectures, selling "
                "through franchised dealers worldwide. Scale amortizes R&D across 10+ million "
                "annual vehicle deliveries as publicly reported; the EV transition requires "
                "retooling that scale."),
         milestones=["1937: founded; the Beetle becomes a global icon",
                     "1998–2012: Bentley, Bugatti, Lamborghini, Porsche added",
                     "2015: diesel-emissions scandal; strategic reset",
                     "MEB/PPE electric platforms underpin the EV pivot"],
         records_note=("Publishes annual reports under German and IFRS accounting. Listed in "
                       "Frankfurt (VOW). Controlled by Porsche SE as publicly reported."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="mercedes", name="Mercedes-Benz Group AG", short="Mercedes-Benz",
         group="German Automakers", industry="Automotive — premium vehicles",
         founded="1926 (merger)", hq="Stuttgart, Germany",
         ceo="Ola Kaellenius (CEO, as publicly reported)",
         ticker="MBG.DE", filing="Annual report",
         employees="approximately 175,000 (reported)",
         revenue="approximately EUR 146 billion in reported 2024 revenue",
         history=("Its roots reach to 1886, when Carl Benz patented the first automobile; the "
                  "Mercedes-Benz marque was formed by the 1926 merger of Benz and Daimler. The "
                  "three-pointed star became the definitive luxury badge. DaimlerChrysler (1998–"
                  "2007) ended in divorce; the 2021 spin-off of Daimler Truck left a pure "
                  "passenger-car and van company focused on electrified luxury."),
         products=("Mercedes-Benz luxury sedans, SUVs, and AMG performance models; EQ electric "
                   "lineup; Mercedes-Benz Vans; financial services."),
         model=("Premium pricing on engineering prestige and brand equity; high margins per "
                "vehicle versus volume makers. The strategy is 'electric-first luxury' — defending "
                "margins while converting the lineup to electric drivetrains."),
         milestones=["1886: Benz Patent-Motorwagen — the first automobile",
                     "1926: Benz–Daimler merger creates Mercedes-Benz",
                     "1998–2007: DaimlerChrysler era",
                     "2021: Daimler Truck spin-off; pure luxury-car focus"],
         records_note=("Publishes annual reports under IFRS. Listed in Frankfurt (MBG)."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="bmw", name="Bayerische Motoren Werke AG", short="BMW",
         group="German Automakers", industry="Automotive — premium vehicles",
         founded="1916", hq="Munich, Germany",
         ceo="Oliver Zipse (CEO, as publicly reported)",
         ticker="BMW.DE", filing="Annual report",
         employees="approximately 149,000 (reported)",
         revenue="approximately EUR 142 billion in reported 2024 revenue",
         history=("Founded in 1916 in Munich as an aircraft-engine maker, BMW moved to motorcycles "
                  "(1923) and cars (1928). 'The Ultimate Driving Machine' positioning made it the "
                  "sporting alternative to Mercedes. It owns MINI (since 1994) and Rolls-Royce "
                  "Motor Cars (since 1998). BMW's Neue Klasse electric architecture is its bet on "
                  "the next generation of driver-focused EVs."),
         products=("BMW cars and SUVs, MINI, Rolls-Royce Motor Cars, BMW Motorrad motorcycles; "
                   "Neue Klasse electric models; financial services."),
         model=("Premium sport-luxury positioning with engineering-led branding. Multi-brand "
                "strategy spans accessible premium (MINI) to ultra-luxury (Rolls-Royce); "
                "electrification proceeds brand by brand."),
         milestones=["1916: founded as aircraft-engine maker",
                     "1928: enters automobile manufacturing",
                     "1994/1998: MINI and Rolls-Royce added",
                     "Neue Klasse EV architecture launches the electric era"],
         records_note=("Publishes annual reports under IFRS. Listed in Frankfurt (BMW). "
                       "Quandt family is the largest shareholder as publicly reported."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="byd", name="BYD Company Limited", short="BYD",
         group="Asian Automakers", industry="New-energy vehicles and batteries",
         founded="1995", hq="Shenzhen, China",
         ceo="Wang Chuanfu (founder, chairman and president, as publicly reported)",
         ticker="002594.SZ / 1211.HK", filing="Annual report (HKEX/SZSE)",
         employees="approximately 969,000 (reported)",
         revenue="approximately RMB 777.1 billion (about US$107 billion) in reported 2024 revenue",
         history=("Founded in 1995 in Shenzhen by chemist Wang Chuanfu as a rechargeable-battery "
                  "maker, BYD entered autos in 2003 by acquiring a struggling carmaker. It stopped "
                  "making pure gasoline cars in 2022 and scaled plug-in hybrids and battery-"
                  "electrics to 4.27 million vehicles in 2024 as reported — overtaking Tesla in "
                  "annual revenue that year and becoming China's best-selling automaker, built on "
                  "the Blade Battery and extreme vertical integration."),
         products=("New-energy passenger vehicles (Dynasty and Ocean series, Denza, Yangwang, "
                   "Fangchengbao), Blade Battery LFP cells, commercial vehicles, electronics "
                   "assembly, solar and rail transit."),
         model=("Vertical integration from lithium and batteries to semiconductors and finished "
                "cars compresses costs and secures supply. High-volume domestic scale funds "
                "aggressive overseas expansion into Europe, Southeast Asia, and Latin America."),
         milestones=["1995: founded as battery maker by Wang Chuanfu",
                     "2003: enters automobile manufacturing",
                     "2022: ends pure-gasoline car production",
                     "2024: 4.27 million NEVs sold; revenue exceeds Tesla's (as reported)"],
         records_note=("Files annual reports with HKEX and SZSE. Dual-listed (1211.HK, 002594.SZ). "
                       "Wang Chuanfu is founder, chairman, and president as publicly reported."),
         citation=("Company annual report; 2024 results press materials. Figures rounded as reported.")),
    dict(key="honda", name="Honda Motor Co., Ltd.", short="Honda",
         group="Asian Automakers", industry="Automotive and motorcycles",
         founded="1948", hq="Tokyo, Japan",
         ceo="Toshihiro Mibe (president and CEO, as publicly reported)",
         ticker="7267.T / HMC", filing="Form 20-F annual report",
         employees="approximately 194,000 (reported)",
         revenue="approximately JPY 21.7 trillion in reported fiscal 2024 revenue",
         history=("Founded in 1948 by Soichiro Honda and Takeo Fujisawa, Honda grew from motorized "
                  "bicycles into the world's largest motorcycle manufacturer and a top global "
                  "automaker famed for engineering (CVCC, VTEC, HondaJet). It built its US "
                  "manufacturing base early (Ohio, 1982) and cultivated a reputation for "
                  "reliability and efficient engineering over styling excess."),
         products=("Honda and Acura cars and SUVs, motorcycles (world's largest maker as reported), "
                   "power equipment, HondaJet aircraft, marine engines."),
         model=("Engineering-led efficiency: high-reliability products built on flexible global "
                "manufacturing. Motorcycles and power products diversify beyond autos; the "
                "strategy now centers on hybrid strength while developing EVs and hydrogen."),
         milestones=["1948: founded by Soichiro Honda and Takeo Fujisawa",
                     "1963: enters automobile manufacturing",
                     "1982: first Japanese automaker to build cars in the US (Ohio)",
                     "World's largest motorcycle manufacturer (as reported)"],
         records_note=("Files annual reports on Form 20-F with the US SEC. Listed in Tokyo (7267) "
                       "and New York (HMC, ADR)."),
         citation=("Company annual report (Form 20-F). Figures rounded as reported.")),
    dict(key="ford", name="Ford Motor Company", short="Ford",
         group="American Automakers", industry="Automotive manufacturing",
         founded="1903", hq="Dearborn, Michigan, USA",
         ceo="Jim Farley (president and CEO, as publicly reported)",
         ticker="F", filing="Form 10-K annual report",
         employees="approximately 171,000 (reported)",
         revenue="approximately US$185 billion in reported 2024 revenue",
         history=("Founded in 1903 by Henry Ford, Ford's moving assembly line (1913) and Model T "
                  "put the world on wheels. The Ford family retains voting control to this day. "
                  "Ford survived 2008 without a bailout by mortgaging everything in 2006. Under "
                  "Jim Farley (CEO from 2020), Ford split operations into Model e (EVs), Blue "
                  "(gas vehicles), and Pro (commercial) — then slowed EV spending as demand "
                  "cooled, leaning on hybrids and the F-Series, America's best-selling truck line "
                  "for decades as publicly reported."),
         products=("F-Series trucks, Mustang, Bronco, Explorer; commercial vehicles (Ford Pro); "
                   "hybrids and EVs (F-150 Lightning, Mustang Mach-E); Ford Credit financing."),
         model=("Truck and commercial-vehicle profits fund the transition: F-Series and Ford Pro "
                "generate the cash; EVs and software are the growth bet. Family voting control "
                "allows long-horizon decisions."),
         milestones=["1903: founded by Henry Ford; 1913: moving assembly line",
                     "2006: mortgages all assets to fund turnaround — avoids 2008 bailout",
                     "2020: Jim Farley becomes CEO",
                     "F-Series: America's best-selling truck for decades (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (F). "
                       "Ford family holds supervoting shares as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
]

# ---------------------------------------------------------------- healthcare
HEALTH = [
    dict(key="jnj", name="Johnson & Johnson", short="Johnson & Johnson",
         group="Diversified Health", industry="Pharmaceuticals and medical technology",
         founded="1886", hq="New Brunswick, New Jersey, USA",
         ceo="Joaquin Duato (chairman and CEO, as publicly reported)",
         ticker="JNJ", filing="Form 10-K annual report",
         employees="approximately 138,000 (reported)",
         revenue="approximately US$88.8 billion in reported 2024 revenue",
         history=("Founded in 1886 in New Brunswick, New Jersey, by three Johnson brothers, J&J "
                  "built the first commercial first-aid kits and sterile surgical supplies. Its "
                  "decentralized 'credo'-driven structure grew it into the world's largest "
                  "healthcare company by revenue for much of its history. The 2023 separation of "
                  "the consumer business as Kenvue refocused J&J on higher-growth pharmaceuticals "
                  "(Darzalex, Stelara, Tremfya) and MedTech."),
         products=("Pharmaceuticals (oncology, immunology, neuroscience), MedTech (surgical "
                   "devices, orthopaedics, vision care). Consumer health separated as Kenvue "
                   "in 2023."),
         model=("Patent-protected drug franchises plus recurring MedTech device revenue. The "
                "post-Kenvue company is a pure-play pharma/MedTech business investing heavily in "
                "R&D and tuck-in acquisitions."),
         milestones=["1886: founded by the Johnson brothers",
                     "Credo-based decentralized management",
                     "2023: Kenvue consumer separation completed",
                     "Darzalex among the world's top-selling drugs (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (JNJ). "
                       "Dividend Aristocrat with decades of increases as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="roche", name="F. Hoffmann-La Roche Ltd", short="Roche",
         group="Diversified Health", industry="Pharmaceuticals and diagnostics",
         founded="1896", hq="Basel, Switzerland",
         ceo="Thomas Schinecker (CEO, as publicly reported)",
         ticker="ROG.SW", filing="Annual report",
         employees="approximately 103,000 (reported)",
         revenue="approximately CHF 60.9 billion in reported 2024 revenue",
         history=("Founded in 1896 in Basel by Fritz Hoffmann-La Roche, Roche became a pioneer of "
                  "targeted cancer therapy (Herceptin, Avastin, Rituxan via Genenteer, majority-"
                  "owned since 1990). Its diagnostics division — the world's largest in vitro "
                  "diagnostics business as reported — pairs with pharma in a personalized-"
                  "healthcare strategy: test and treat as one system."),
         products=("Oncology and immunology pharmaceuticals, in vitro diagnostics instruments and "
                   "tests, diabetes care, sequencing (Foundation Medicine)."),
         model=("Pharma–diagnostics flywheel: diagnostics identify patients, targeted drugs treat "
                "them. High R&D intensity (among the industry's highest as reported) sustains the "
                "pipeline; Genentech anchors US biotech research."),
         milestones=["1896: founded in Basel by Fritz Hoffmann-La Roche",
                     "1990: majority stake in Genentech",
                     "Herceptin/Avastin define targeted oncology",
                     "World's largest in vitro diagnostics business (as reported)"],
         records_note=("Publishes annual reports under IFRS. Listed on SIX Swiss Exchange (ROG). "
                       "Hoffmann and Oeri families hold voting control as publicly reported."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="pfizer", name="Pfizer Inc.", short="Pfizer",
         group="Pharma", industry="Pharmaceuticals",
         founded="1849", hq="New York, New York, USA",
         ceo="Albert Bourla (chairman and CEO, as publicly reported)",
         ticker="PFE", filing="Form 10-K annual report",
         employees="approximately 88,000 (reported)",
         revenue="approximately US$63.6 billion in reported 2024 revenue",
         history=("Founded in 1849 in Brooklyn by Charles Pfizer and Charles Erhart, Pfizer grew "
                  "through mass-produced penicillin (WWII), blockbusters (Lipitor — once the "
                  "world's best-selling drug), and mega-mergers (Warner-Lambert, Pharmacia, "
                  "Wyeth). The BioNTech partnership delivered Comirnaty, the COVID-19 vaccine that "
                  "made Pfizer a household name; the ~US$43 billion Seagen acquisition (2023) "
                  "rebuilt its oncology pipeline."),
         products=("Comirnaty, Paxlovid, Eliquis, Prevnar, Ibrance; oncology portfolio via Seagen; "
                   "vaccines and rare-disease medicines."),
         model=("Blockbuster-driven pharma economics: patent exclusivity funds R&D and "
                "acquisitions. Post-COVID, the strategy is rebuilding growth through oncology "
                "(Seagen) and next-generation vaccines."),
         milestones=["1849: founded in Brooklyn",
                     "WWII: mass penicillin production",
                     "Lipitor — once the world's top-selling drug",
                     "2020–21: Comirnaty with BioNTech; 2023: Seagen acquisition (~US$43B)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (PFE)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="lilly", name="Eli Lilly and Company", short="Eli Lilly",
         group="Pharma", industry="Pharmaceuticals",
         founded="1876", hq="Indianapolis, Indiana, USA",
         ceo="David Ricks (chair and CEO, as publicly reported)",
         ticker="LLY", filing="Form 10-K annual report",
         employees="approximately 47,000 (reported)",
         revenue="approximately US$45 billion in reported 2024 revenue",
         history=("Founded in 1876 in Indianapolis by Eli Lilly, the company pioneered mass-"
                  "produced insulin (1923) and later Prozac. After patent cliffs in the 2010s, "
                  "Lilly's incretin franchise — Mounjaro and Zepbound (tirzepatide) — made it the "
                  "world's most valuable pharmaceutical company by market capitalization as "
                  "publicly reported, riding the obesity-medicine wave alongside diabetes care."),
         products=("Mounjaro/Zepbound (tirzepatide), Trulicity, Verzenio, Taltz, Jardiance "
                   "(with Boehringer Ingelheim)."),
         model=("Concentrated bets on large therapeutic areas (diabetes/obesity, oncology, "
                "immunology, Alzheimer's) with premium-priced biologics. Manufacturing scale-up "
                "for incretins is the defining operational challenge."),
         milestones=["1876: founded in Indianapolis",
                     "1923: first mass-produced insulin",
                     "1987: Prozac launches",
                     "2022–24: tirzepatide franchise; world's most valuable pharma by market cap (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (LLY)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="unitedhealth", name="UnitedHealth Group Incorporated", short="UnitedHealth",
         group="Payers", industry="Health insurance and health services",
         founded="1977", hq="Minnetonka, Minnesota, USA",
         ceo="Andrew Witty (CEO, as publicly reported)",
         ticker="UNH", filing="Form 10-K annual report",
         employees="approximately 340,000 (reported)",
         revenue="approximately US$400 billion in reported 2024 revenue",
         history=("Founded in 1977 in Minnesota, UnitedHealth grew from a health-plan administrator "
                  "into the largest US health insurer (UnitedHealthcare) fused with the largest "
                  "health-services business (Optum: care delivery, pharmacy benefit management, "
                  "data analytics). The combination — insurer plus provider plus data — is unique "
                  "in scale and the template rivals now imitate."),
         products=("UnitedHealthcare insurance plans, Optum Health care delivery, Optum Rx pharmacy "
                   "benefits, Optum Insight data and analytics."),
         model=("Insurance premiums plus fee-based health services. Owning care delivery and "
                "pharmacy benefits lets the group manage medical costs internally while selling "
                "services to third parties — vertical integration at national scale."),
         milestones=["1977: founded in Minnesota",
                     "UnitedHealthcare + Optum dual-engine structure",
                     "Largest US health insurer by revenue (as reported)",
                     "Optum: one of the largest US physician employers (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (UNH). "
                       "Dow Jones component."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="novartis", name="Novartis AG", short="Novartis",
         group="Payers", industry="Pharmaceuticals — innovative medicines",
         founded="1996 (merger)", hq="Basel, Switzerland",
         ceo="Vas Narasimhan (CEO, as publicly reported)",
         ticker="NOVN.SW / NVS", filing="Annual report (Form 20-F)",
         employees="approximately 76,000 (reported)",
         revenue="approximately US$50.3 billion in reported 2024 revenue (continuing operations)",
         history=("Formed in 1996 by the merger of Ciba-Geigy and Sandoz — Swiss chemical lineages "
                  "reaching to the 1700s. Under Vas Narasimhan (CEO from 2018), Novartis shed "
                  "generics (Sandoz spin-off 2023) and the Alcon eye-care business to become a "
                  "pure innovative-medicines company focused on cardiovascular, immunology, "
                  "neuroscience, and oncology, with bets on radioligand therapy and gene therapy."),
         products=("Entresto, Kisqali, Cosentyx, Kesimpta, Pluvicto (radioligand therapy), "
                   "Zolgensma (gene therapy)."),
         model=("Pure-play innovative pharma: high-margin patented medicines fund deep R&D in "
                "platforms (radioligand, gene therapy, xRNA). Portfolio pruning concentrates "
                "capital on the highest-return therapeutic areas."),
         milestones=["1996: Ciba-Geigy–Sandoz merger",
                     "2018: Vas Narasimhan becomes CEO",
                     "2019/2023: Alcon and Sandoz separations — pure innovative medicines",
                     "Pluvicto pioneers radioligand therapy at scale"],
         records_note=("Files Form 20-F with the US SEC; reports under IFRS. Listed on SIX (NOVN) "
                       "and NYSE (NVS, ADR)."),
         citation=("Company annual report. Figures rounded as reported.")),
]

# ------------------------------------------------------- retail and consumer
RETAIL = [
    dict(key="walmart", name="Walmart Inc.", short="Walmart",
         group="Retail", industry="Retail — discount stores and e-commerce",
         founded="1962", hq="Bentonville, Arkansas, USA",
         ceo="Doug McMillon (president and CEO, as publicly reported)",
         ticker="WMT", filing="Form 10-K annual report",
         employees="approximately 2.1 million (reported)",
         revenue="approximately US$681 billion in reported fiscal 2025 revenue",
         history=("Founded in 1962 in Rogers, Arkansas, by Sam Walton, Walmart perfected everyday-"
                  "low-price discount retail through rural expansion, relentless logistics, and "
                  "supplier leverage. It became the world's largest company by revenue and the "
                  "largest private employer on earth as publicly reported. The modern chapter is "
                  "omnichannel: e-commerce, third-party marketplace, Walmart+ membership, and a "
                  "fast-growing advertising business."),
         products=("Discount supercenters, Sam's Club warehouses, e-commerce and marketplace, "
                   "Walmart+ membership, advertising (Walmart Connect), financial services."),
         model=("High-volume, low-margin retail: buying scale and logistics efficiency fund the "
                "lowest prices, which drive the volume. New profit engines — marketplace "
                "commissions, advertising, memberships — carry far higher margins than the "
                "stores."),
         milestones=["1962: first Walmart opens in Rogers, Arkansas",
                     "World's largest company by revenue; largest private employer (as reported)",
                     "Sam's Club, e-commerce, and Walmart+ membership ecosystem",
                     "Walmart Connect advertising becomes a major profit engine"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (WMT). "
                       "Fiscal year ends January 31. Walton family holds majority voting control "
                       "as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="costco", name="Costco Wholesale Corporation", short="Costco",
         group="Retail", industry="Retail — membership warehouse clubs",
         founded="1983", hq="Issaquah, Washington, USA",
         ceo="Ron Vachris (president and CEO, as publicly reported)",
         ticker="COST", filing="Form 10-K annual report",
         employees="approximately 333,000 (reported)",
         revenue="approximately US$254 billion in reported fiscal 2024 revenue",
         history=("Costco's lineage runs through Sol Price's Price Club (1976); Costco itself was "
                  "founded in 1983 in Seattle by James Sinegal and Jeffrey Brotman, merging with "
                  "Price Club in 1993. The warehouse-club model — limited SKUs, bulk sizes, "
                  "treasure-hunt merchandising, membership fees — produced the most loyal shoppers "
                  "in retail and renewal rates above 90% as publicly reported. Kirkland Signature "
                  "became a powerhouse private brand."),
         products=("Membership warehouse clubs, Kirkland Signature private label, gasoline, "
                   "pharmacy, optical, travel services, e-commerce."),
         model=("Membership fees are the profit engine: merchandise is sold near cost to drive "
                "traffic, and the annual fee drops almost entirely to the bottom line. Limited "
                "assortment (~4,000 SKUs as reported) maximizes turnover per item."),
         milestones=["1976: Price Club pioneers the warehouse club",
                     "1983: Costco founded; 1993: Price Club merger",
                     "Membership renewal rates above 90% (as reported)",
                     "Kirkland Signature — a top private brand by sales (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq "
                       "(COST). Fiscal year ends late August/early September."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="pg", name="The Procter & Gamble Company", short="Procter & Gamble",
         group="Consumer Goods", industry="Consumer packaged goods",
         founded="1837", hq="Cincinnati, Ohio, USA",
         ceo="Jon Moeller (chairman, president and CEO, as publicly reported)",
         ticker="PG", filing="Form 10-K annual report",
         employees="approximately 107,000 (reported)",
         revenue="approximately US$84 billion in reported fiscal 2024 revenue",
         history=("Founded in 1837 in Cincinnati by candlemaker William Procter and soapmaker James "
                  "Gamble, P&G invented modern brand management and consumer research. Tide, "
                  "Pampers, Gillette (acquired 2005 for ~US$57 billion as reported), Crest, and "
                  "Dawn anchor a portfolio of daily-use brands sold in nearly every country. "
                  "David Taylor's and Jon Moeller's streamlining cut underperforming brands to "
                  "focus on 65 core brands as publicly reported."),
         products=("Fabric and home care (Tide, Downy), baby and feminine care (Pampers, Always), "
                   "grooming (Gillette, Braun), health care (Crest, Oral-B, Vicks), beauty (Olay, "
                   "Head & Shoulders)."),
         model=("Brand-led premium pricing on daily necessities: innovation (formulas, packaging) "
                "justifies price premiums over private label; advertising scale builds moats. "
                "Emerging-market premiumization is the long growth lever."),
         milestones=["1837: founded in Cincinnati",
                     "Invented brand management and the soap opera (as advertising)",
                     "2005: Gillette acquisition (~US$57 billion as reported)",
                     "Portfolio focused to core daily-use brands"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (PG). "
                       "Dividend Aristocrat — dividends paid since 1890 as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="loreal", name="L'Oreal S.A.", short="L'Oreal",
         group="Consumer Goods", industry="Cosmetics and beauty",
         founded="1909", hq="Clichy, France",
         ceo="Nicolas Hieronimus (CEO, as publicly reported)",
         ticker="OR.PA", filing="Annual report (Universal Registration Document)",
         employees="approximately 94,000 (reported)",
         revenue="approximately EUR 43.5 billion in reported 2024 revenue",
         history=("Founded in 1909 in Paris by chemist Eugene Schueller, who invented a hair dye "
                  "formula, L'Oreal became the world's largest cosmetics company through brand "
                  "acquisitions (Maybelline, Kiehl's, CeraVe, Aesop) and relentless R&D — it "
                  "files hundreds of beauty-tech patents yearly as reported. Digital and e-"
                  "commerce now drive a large share of sales as publicly reported."),
         products=("L'Oreal Paris, Maybelline, Lancôme, Kiehl's, CeraVe, La Roche-Posay, Redken, "
                   "luxury and dermatological divisions."),
         model=("Multi-division brand ladder from mass (Maybelline) to luxury (Lancôme) to "
                "dermatological (La Roche-Posay). Beauty-tech R&D and influencer-led digital "
                "marketing sustain premium pricing; emerging markets drive volume growth."),
         milestones=["1909: founded by Eugene Schueller in Paris",
                     "World's largest cosmetics company (as reported)",
                     "Maybelline, Kiehl's, CeraVe acquisitions build the portfolio",
                     "Beauty-tech: hundreds of patents filed yearly (as reported)"],
         records_note=("Publishes a Universal Registration Document under French/EU rules. Listed "
                       "on Euronext Paris (OR). Bettencourt Meyers family is the largest "
                       "shareholder as publicly reported."),
         citation=("Company annual report (Universal Registration Document). Figures rounded as reported.")),
    dict(key="cocacola", name="The Coca-Cola Company", short="Coca-Cola",
         group="Beverages & Apparel", industry="Beverages",
         founded="1892", hq="Atlanta, Georgia, USA",
         ceo="James Quincey (chairman and CEO, as publicly reported)",
         ticker="KO", filing="Form 10-K annual report",
         employees="approximately 79,000 (reported)",
         revenue="approximately US$47.1 billion in reported 2024 revenue",
         history=("The drink was created in 1886 by Atlanta pharmacist John Pemberton; Asa Candler "
                  "incorporated the Coca-Cola Company in 1892 and built it through franchised "
                  "bottlers and marketing genius. The secret formula, the contour bottle, and a "
                  "century of advertising made it the world's most recognized brand as widely "
                  "reported. The system now spans 200+ countries with bottling partners like "
                  "Coca-Cola Europacific Partners."),
         products=("Coca-Cola, Sprite, Fanta, Minute Maid, Powerade, Costa Coffee, Topo Chico; "
                   "concentrate sold to franchised bottlers."),
         model=("Concentrate economics: Coca-Cola sells syrup/concentrate to independent bottlers "
                "at high margins while bottlers handle capital-intensive bottling and "
                "distribution. Brand marketing is the central corporate function."),
         milestones=["1886: Pemberton creates Coca-Cola; 1892: company incorporated",
                     "Franchised bottler system scales it to 200+ countries",
                     "Among the world's most recognized brands (as widely reported)",
                     "Costa Coffee acquisition expands beyond sparkling"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (KO). "
                       "Dividend King with 60+ years of increases as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="nike", name="NIKE, Inc.", short="Nike",
         group="Beverages & Apparel", industry="Athletic footwear and apparel",
         founded="1964", hq="Beaverton, Oregon, USA",
         ceo="Elliott Hill (president and CEO, as publicly reported)",
         ticker="NKE", filing="Form 10-K annual report",
         employees="approximately 83,000 (reported)",
         revenue="approximately US$51.4 billion in reported fiscal 2024 revenue",
         history=("Founded in 1964 as Blue Ribbon Sports by runner Phil Knight and coach Bill "
                  "Bowerman, renamed Nike in 1971 for the Greek goddess of victory. The waffle "
                  "sole, the Swoosh, 'Just Do It' (1988), and the Air Jordan line (1984) built the "
                  "world's largest athletic brand. Contract manufacturing in Asia keeps it asset-"
                  "light; the current strategy pushes direct-to-consumer digital sales."),
         products=("Nike footwear and apparel, Jordan Brand, Converse; Nike Direct digital and "
                   "owned retail."),
         model=("Asset-light brand machine: design and marketing in Oregon, manufacturing by "
                "contract partners in Asia. Pricing power comes from athlete endorsements and "
                "cultural cachet; DTC digital sales carry higher margins than wholesale."),
         milestones=["1964: Blue Ribbon Sports founded; 1971: Nike name and Swoosh",
                     "1984: Air Jordan launches; 1988: 'Just Do It'",
                     "World's largest athletic footwear/apparel brand (as reported)",
                     "Digital direct-to-consumer pivot"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (NKE). "
                       "Fiscal year ends May 31."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
]

# ------------------------------------------------------- energy and industrial
ENERGY = [
    dict(key="exxonmobil", name="Exxon Mobil Corporation", short="ExxonMobil",
         group="Oil & Gas", industry="Integrated oil and gas",
         founded="1999 (merger)", hq="Spring, Texas, USA",
         ceo="Darren Woods (chairman and CEO, as publicly reported)",
         ticker="XOM", filing="Form 10-K annual report",
         employees="approximately 62,000 (reported)",
         revenue="approximately US$349 billion in reported 2024 revenue",
         history=("Standard Oil's 1911 breakup created Jersey Standard (Exxon) and Socony (Mobil); "
                  "they recombined in the 1999 Exxon–Mobil merger, then the largest industrial "
                  "merger of its time as widely reported. ExxonMobil is the largest US-based "
                  "international oil major, spanning Permian shale (strengthened by the ~US$60 "
                  "billion Pioneer Natural Resources acquisition, 2024) to Guyana's prolific "
                  "offshore fields."),
         products=("Crude oil and natural gas production, refining, chemicals, lubricants (Mobil "
                   "1), low-carbon solutions (hydrogen, carbon capture)."),
         model=("Integrated value chain: upstream production profits fund refining, chemicals, and "
                "shareholder returns. Scale and low-cost reserves (Permian, Guyana) provide "
                "through-cycle resilience; capital discipline over volume growth."),
         milestones=["1870/1911 roots: Standard Oil to Exxon and Mobil",
                     "1999: Exxon–Mobil merger",
                     "Permian shale + Guyana offshore anchor production",
                     "2024: Pioneer Natural Resources acquisition (~US$60B as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (XOM). "
                       "Dividend Aristocrat with 40+ years of increases as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="chevron", name="Chevron Corporation", short="Chevron",
         group="Oil & Gas", industry="Integrated oil and gas",
         founded="1879", hq="San Ramon, California, USA",
         ceo="Mike Wirth (chairman and CEO, as publicly reported)",
         ticker="CVX", filing="Form 10-K annual report",
         employees="approximately 45,000 (reported)",
         revenue="approximately US$193 billion in reported 2024 revenue",
         history=("Roots to 1879 as Pacific Coast Oil; a Standard Oil descendant, Chevron took its "
                  "modern name after acquiring Gulf Oil in 1984. The Tengiz field (Kazakhstan), "
                  "Permian shale, and Australian LNG underpin production. The ~US$53 billion Hess "
                  "acquisition (announced 2023) targets Guyana's Stabroek block — one of the "
                  "decade's great oil discoveries."),
         products=("Upstream oil and gas, refining and marketing (Chevron, Texaco, Caltex "
                   "stations), chemicals (Chevron Phillips Chemical JV), renewables and offsets."),
         model=("Upstream-led integrated model: advantaged Permian and offshore assets generate "
                "free cash flow through price cycles; downstream and chemicals add stability. "
                "Shareholder returns are the stated priority over production growth."),
         milestones=["1879: Pacific Coast Oil founded",
                     "1984: acquires Gulf Oil; takes Chevron name",
                     "Tengiz, Permian, Australian LNG anchor the portfolio",
                     "Hess acquisition targets Guyana's Stabroek block (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (CVX). "
                       "Dow Jones component."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="shell", name="Shell plc", short="Shell",
         group="Integrated Energy", industry="Integrated energy",
         founded="1907", hq="London, United Kingdom",
         ceo="Wael Sawan (CEO, as publicly reported)",
         ticker="SHEL", filing="Annual report (Form 20-F)",
         employees="approximately 103,000 (reported)",
         revenue="approximately US$289 billion in reported 2024 revenue",
         history=("Formed in 1907 by merging Royal Dutch Petroleum and the Shell Transport and "
                  "Trading Company, Shell became one of the original 'supermajors.' The BG Group "
                  "acquisition (2016, ~US$50 billion as reported) made it a liquefied-natural-gas "
                  "giant. Under Wael Sawan (CEO from 2023), Shell simplified its structure, moved "
                  "its tax residence fully to the UK, and refocused on LNG and advantaged upstream "
                  "while trimming lower-return renewables."),
         products=("LNG (world's largest portfolio trader as reported), upstream oil and gas, "
                   "refining and chemicals, retail fuel stations, EV charging, renewables."),
         model=("LNG-led integrated energy: long-term gas contracts and trading generate durable "
                "cash; upstream funds the dividend and buybacks. The strategy balances "
                "hydrocarbon cash generation with selective low-carbon investment."),
         milestones=["1907: Royal Dutch–Shell merger",
                     "2016: BG Group acquisition (~US$50B as reported) — LNG leadership",
                     "2022: full UK incorporation; simplified share structure",
                     "2023: Wael Sawan becomes CEO; portfolio refocus"],
         records_note=("Files Form 20-F with the US SEC; reports under IFRS. Listed in London, "
                       "New York, and Amsterdam (SHEL)."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="nextera", name="NextEra Energy, Inc.", short="NextEra Energy",
         group="Integrated Energy", industry="Electric utility and renewables",
         founded="1925", hq="Juno Beach, Florida, USA",
         ceo="John Ketchum (chairman, president and CEO, as publicly reported)",
         ticker="NEE", filing="Form 10-K annual report",
         employees="approximately 16,000 (reported)",
         revenue="approximately US$24.8 billion in reported 2024 revenue",
         history=("Roots to 1925 as Florida Power & Light; the NextEra holding structure emerged "
                  "in the 2000s. FPL is one of America's largest regulated utilities, while "
                  "NextEra Energy Resources became the world's largest generator of wind and solar "
                  "power as publicly reported — a bet placed early, when renewables were a "
                  "rounding error, that compounded into market leadership."),
         products=("Regulated electricity (Florida Power & Light), wind/solar/storage development "
                   "(NextEra Energy Resources), nuclear generation, battery storage."),
         model=("Regulated utility earnings (FPL rate base growth) plus competitive renewables "
                "development selling power under long-term contracts. Scale in procurement and "
                "development creates a cost advantage few can match."),
         milestones=["1925: Florida Power & Light origins",
                     "Early large-scale bet on wind and solar",
                     "World's largest wind/solar generator (as reported)",
                     "Among the most valuable US utilities by market cap (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (NEE)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="siemens", name="Siemens AG", short="Siemens",
         group="Industrial", industry="Industrial technology and automation",
         founded="1847", hq="Munich, Germany",
         ceo="Roland Busch (president and CEO, as publicly reported)",
         ticker="SIE.DE", filing="Annual report",
         employees="approximately 312,000 (reported)",
         revenue="approximately EUR 75.9 billion in reported fiscal 2024 revenue",
         history=("Founded in 1847 in Berlin by Werner von Siemens, the company built telegraph "
                  "networks, then electrified industry. The modern Siemens — reshaped by "
                  "divestitures (Siemens Energy, 2020) and the Healthineers listing — is a focused "
                  "industrial-technology company: factory automation, smart buildings, mobility, "
                  "and the Xcelerator digital platform merging the physical and digital factory."),
         products=("Industrial automation and software (Digital Industries), smart infrastructure, "
                   "mobility (trains), Siemens Healthineers (majority-owned), Xcelerator platform."),
         model=("Technology-stack model: automation hardware plus industrial software sold as "
                "subscriptions; services and digital twins deepen lock-in. Portfolio pruning "
                "concentrated capital on the highest-return industrial-tech businesses."),
         milestones=["1847: founded by Werner von Siemens in Berlin",
                     "Electrified industry; built telegraph networks",
                     "2020: Siemens Energy spin-off; Healthineers listed",
                     "Xcelerator: the industrial metaverse platform bet"],
         records_note=("Publishes annual reports under IFRS. Listed in Frankfurt (SIE). Fiscal "
                       "year ends September 30."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="honeywell", name="Honeywell International Inc.", short="Honeywell",
         group="Industrial", industry="Industrial technology — aerospace, automation",
         founded="1885", hq="Charlotte, North Carolina, USA",
         ceo="Vimal Kapur (chairman and CEO, as publicly reported)",
         ticker="HON", filing="Form 10-K annual report",
         employees="approximately 102,000 (reported)",
         revenue="approximately US$38.5 billion in reported 2024 revenue",
         history=("Roots to an 1885 thermostat company; the modern Honeywell was forged by the "
                  "1999 AlliedSignal merger. Under David Cote (2002–2017) it became a disciplined "
                  "industrial compounder; under Vimal Kapur (CEO from 2023) it is simplifying — "
                  "announcing separations of its automation and aerospace-adjacent businesses — to "
                  "focus on aviation, building automation, and industrial software."),
         products=("Aerospace systems and avionics, building automation, industrial automation, "
                   "performance materials, warehouse automation (Intelligrated)."),
         model=("Installed-base economics: aerospace and building systems generate decades of "
                "aftermarket and service revenue. Software and digital overlays (Forge platform) "
                "raise margins on the hardware base."),
         milestones=["1885: thermostat origins; 1999: AlliedSignal merger",
                     "2002–2017: Cote-era compounding",
                     "2023: Vimal Kapur becomes CEO",
                     "Portfolio simplification: automation and aerospace separations announced"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq "
                       "(HON). Dow Jones component (as publicly reported)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
]

# ------------------------------------------------------- media & entertainment
MEDIA = [
    dict(key="disney", name="The Walt Disney Company", short="Disney",
         group="Streaming & Studios", industry="Entertainment — media, parks, streaming",
         founded="1923", hq="Burbank, California, USA",
         ceo="Bob Iger (CEO, as publicly reported)",
         ticker="DIS", filing="Form 10-K annual report",
         employees="approximately 225,000 (reported)",
         revenue="approximately US$94.8 billion in reported fiscal 2024 revenue",
         history=("Founded in 1923 by Walt and Roy Disney, the company grew from Mickey Mouse "
                  "(1928) into the defining entertainment empire: animated classics, Disneyland "
                  "(1955), and acquisitions of Pixar (2006), Marvel (2009), Lucasfilm (2012), and "
                  "21st Century Fox (2019, ~US$71 billion as reported). Disney+ launched in 2019 "
                  "and the streaming business reached profitability as reported; Bob Iger "
                  "returned as CEO in 2022 to steer the turnaround."),
         products=("Disney+, Hulu, ESPN; theme parks and cruises; studios (Disney, Pixar, Marvel, "
                   "Lucasfilm, 20th Century); ABC and linear networks."),
         model=("Franchise flywheel: beloved IP monetized across streaming, parks, merchandise, "
                "and licensing. Parks generate the steadiest cash; streaming is the growth "
                "engine now crossing into profitability as reported."),
         milestones=["1923: founded by Walt and Roy Disney",
                     "1955: Disneyland opens",
                     "2006–2019: Pixar, Marvel, Lucasfilm, Fox acquisitions",
                     "2019: Disney+ launches; streaming turns profitable (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (DIS). "
                       "Fiscal year ends late September/early October."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="netflix", name="Netflix, Inc.", short="Netflix",
         group="Streaming & Studios", industry="Streaming entertainment",
         founded="1997", hq="Los Gatos, California, USA",
         ceo="Ted Sarandos and Greg Peters (co-CEOs, as publicly reported)",
         ticker="NFLX", filing="Form 10-K annual report",
         employees="approximately 14,000 (reported)",
         revenue="approximately US$39 billion in reported 2024 revenue",
         history=("Founded in 1997 by Reed Hastings and Marc Randolph as a DVD-by-mail service, "
                  "Netflix pivoted to streaming in 2007, to originals with House of Cards (2013), "
                  "and to global production — becoming the first streamer profitable at global "
                  "scale as reported. The password-sharing crackdown and ad-supported tier "
                  "re-accelerated subscriber growth past 300 million as publicly reported."),
         products=("Subscription streaming (ad-free and ad-supported tiers), original films and "
                   "series, games, live events."),
         model=("Subscription scale economics: ~US$17 billion in annual content spend as reported "
                "amortized over 300M+ subscribers; recommendation technology reduces churn; "
                "advertising tier adds a second revenue stream per user."),
         milestones=["1997: DVD-by-mail founded",
                     "2007: streaming launches; 2013: originals begin",
                     "First streamer profitable at global scale (as reported)",
                     "300M+ subscribers; ad tier and paid sharing drive growth (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq "
                       "(NFLX)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="wbd", name="Warner Bros. Discovery, Inc.", short="Warner Bros. Discovery",
         group="Studios & Cable", industry="Media — studios, cable, streaming",
         founded="2022 (merger)", hq="New York, New York, USA",
         ceo="David Zaslav (president and CEO, as publicly reported)",
         ticker="WBD", filing="Form 10-K annual report",
         employees="approximately 35,000 (reported)",
         revenue="approximately US$39.3 billion in reported 2024 revenue",
         history=("Formed in 2022 by merging WarnerMedia (AT&T's media arm: Warner Bros., HBO, "
                  "CNN, Turner) with Discovery, reuniting a century of Hollywood history — "
                  "Warner Bros. founded 1923 — with Discovery's unscripted empire. David Zaslav "
                  "took on heavy merger debt and has spent the years since deleveraging, cutting "
                  "costs, and rebuilding the Max streaming service around HBO-quality content."),
         products=("Warner Bros. studios, HBO and Max streaming, CNN, Discovery networks, DC "
                   "Studios, Turner sports rights."),
         model=("Content-library monetization across theatrical, cable affiliate fees, and "
                "streaming. Deleveraging the merger debt is the defining financial task; "
                "franchise IP (DC, Harry Potter, Game of Thrones) is the strategic asset."),
         milestones=["1923: Warner Bros. founded",
                     "2022: WarnerMedia–Discovery merger forms WBD",
                     "HBO/Max as the prestige-streaming anchor",
                     "DC Studios reboot under James Gunn and Peter Safran (as reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq "
                       "(WBD)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="comcast", name="Comcast Corporation", short="Comcast",
         group="Studios & Cable", industry="Telecom, media, theme parks",
         founded="1963", hq="Philadelphia, Pennsylvania, USA",
         ceo="Brian Roberts (chairman and CEO, as publicly reported)",
         ticker="CMCSA", filing="Form 10-K annual report",
         employees="approximately 182,000 (reported)",
         revenue="approximately US$123.7 billion in reported 2024 revenue",
         history=("Founded in 1963 as American Cable Systems by Ralph Roberts, Comcast grew "
                  "through cable consolidation into America's largest cable operator, then bought "
                  "NBCUniversal (2011–2013) and Sky (2018, ~US$39 billion as reported) to become "
                  "a global media-telecom hybrid. Brian Roberts has led it since 2002; the "
                  "current strategy pairs broadband growth with Peacock streaming and theme-park "
                  "expansion."),
         products=("Xfinity broadband and cable, NBCUniversal (NBC, Universal Pictures, Peacock), "
                   "Sky (Europe), Universal theme parks."),
         model=("Broadband subscriptions are the cash engine; content (NBCU, Sky) differentiates "
                "and monetizes across theatrical, streaming, and parks. Theme parks deliver "
                "high-margin experiential revenue."),
         milestones=["1963: American Cable Systems founded",
                     "2011–2013: NBCUniversal acquisition",
                     "2018: Sky acquisition (~US$39B as reported)",
                     "Peacock streaming; Epic Universe theme park expansion"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq "
                       "(CMCSA). Roberts family holds supervoting shares as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="nintendo", name="Nintendo Co., Ltd.", short="Nintendo",
         group="Gaming & Audio", industry="Video games",
         founded="1889", hq="Kyoto, Japan",
         ceo="Shuntaro Furukawa (president, as publicly reported)",
         ticker="7974.T / NTDOY", filing="Annual report (Yuho)",
         employees="approximately 8,000 (reported)",
         revenue="approximately JPY 1.67 trillion in reported fiscal 2024 revenue",
         history=("Founded in 1889 in Kyoto by Fusajiro Yamauchi as a hanafuda playing-card maker, "
                  "Nintendo entered video games in the 1970s and defined the industry twice: the "
                  "NES (1983) revived console gaming, and the Wii (2006) and Switch (2017) proved "
                  "innovation beats raw power. Mario, Zelda, and Pokémon are among the most "
                  "valuable entertainment franchises ever created as widely reported."),
         products=("Nintendo Switch (and successor hardware), Mario, Zelda, Pokémon (via partial "
                   "ownership of The Pokémon Company), mobile games, theme-park partnerships."),
         model=("Integrated hardware–software: consoles sold at accessible prices, profits from "
                "first-party software with extraordinary attach rates and margins. IP is "
                "monetized across games, film (Mario movie), and parks with extreme discipline."),
         milestones=["1889: founded as playing-card maker",
                     "1983: NES revives the game industry",
                     "2017: Switch — hybrid console phenomenon",
                     "Mario/Zelda among the most valuable franchises (as widely reported)"],
         records_note=("Files annual securities reports (Yuho) in Japan. Listed in Tokyo (7974); "
                       "ADR in the US (NTDOY)."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="spotify", name="Spotify Technology S.A.", short="Spotify",
         group="Gaming & Audio", industry="Audio streaming",
         founded="2006", hq="Stockholm, Sweden",
         ceo="Daniel Ek (founder and CEO, as publicly reported)",
         ticker="SPOT", filing="Form 20-F annual report",
         employees="approximately 7,000 (reported)",
         revenue="approximately EUR 15.7 billion in reported 2024 revenue",
         history=("Founded in 2006 in Stockholm by Daniel Ek and Martin Lorentzon as a legal "
                  "answer to piracy, Spotify made on-demand streaming the music industry's "
                  "dominant format and went public via direct listing in 2018. Podcasts and "
                  "audiobooks expanded it beyond music; after years of losses, 2024 brought "
                  "sustained profitability as publicly reported."),
         products=("Music streaming (Premium and ad-supported), podcasts, audiobooks; "
                   "creator tools and advertising platform."),
         model=("Subscription and ad revenue shared with rights holders (~70% of revenue "
                "historically as reported). Scale plus podcast/audiobook diversification and "
                "pricing power drive the path from growth to durable profit."),
         milestones=["2006: founded in Stockholm as the anti-piracy answer",
                     "2018: direct listing on NYSE",
                     "Dominant global music-streaming position (as reported)",
                     "2024: sustained profitability (as reported)"],
         records_note=("Files Form 20-F with the US SEC; domiciled in Luxembourg. Listed on NYSE "
                       "(SPOT)."),
         citation=("Company annual report (Form 20-F). Figures rounded as reported.")),
]

# ------------------------------------------------------------------ telecom
TELECOM = [
    dict(key="verizon", name="Verizon Communications Inc.", short="Verizon",
         group="US Carriers", industry="Telecommunications",
         founded="2000 (merger)", hq="New York, New York, USA",
         ceo="Hans Vestberg (chairman and CEO, as publicly reported)",
         ticker="VZ", filing="Form 10-K annual report",
         employees="approximately 105,000 (reported)",
         revenue="approximately US$134.8 billion in reported 2024 revenue",
         history=("Formed in 2000 by the Bell Atlantic–GTE merger (a Bell System descendant), "
                  "Verizon bought out Vodafone's 45% wireless stake in 2014 for ~US$130 billion as "
                  "reported — then the third-largest corporate deal ever. It built America's most "
                  "awarded wireless network as widely reported and is deploying 5G Ultra "
                  "Wideband and fiber (Fios) while expanding into business services."),
         products=("Wireless service (largest US subscriber base as reported), Fios fiber "
                   "internet, business and enterprise connectivity, 5G private networks."),
         model=("Subscription wireless ARPU plus broadband: high fixed-cost networks monetized "
                "through monthly plans. Network quality supports premium pricing; business "
                "services and fixed wireless add growth."),
         milestones=["2000: Bell Atlantic–GTE merger forms Verizon",
                     "2014: buys Vodafone's wireless stake (~US$130B as reported)",
                     "Most-awarded US wireless network (as widely reported)",
                     "5G Ultra Wideband and Fios fiber expansion"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (VZ). "
                       "Dow Jones component."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="att", name="AT&T Inc.", short="AT&T",
         group="US Carriers", industry="Telecommunications",
         founded="1885", hq="Dallas, Texas, USA",
         ceo="John Stankey (CEO, as publicly reported)",
         ticker="T", filing="Form 10-K annual report",
         employees="approximately 149,000 (reported)",
         revenue="approximately US$122.3 billion in reported 2024 revenue",
         history=("Roots to the 1885 American Telephone and Telegraph Company; the 1984 Bell "
                  "breakup split it, and SBC's 2005 acquisition of AT&T revived the name. A "
                  "decade of media adventure — DirecTV (2015), Time Warner (2018) — ended with "
                  "spin-offs (WarnerMedia into Warner Bros. Discovery, 2022) and a return to "
                  "pure telecom: 5G and fiber under John Stankey (CEO from 2020)."),
         products=("Wireless service, AT&T Fiber internet, business connectivity, FirstNet public-"
                   "safety network."),
         model=("Simplified back to connectivity: wireless and fiber subscriptions. The media "
                "divestitures cut ~US$40 billion+ in debt as reported and refocused capital on "
                "network investment and the dividend."),
         milestones=["1885: AT&T founded; 1984: Bell breakup",
                     "2005: SBC acquires AT&T, takes the name",
                     "2015–2022: media era (DirecTV, Time Warner) then exit",
                     "2020: John Stankey becomes CEO; pure-telecom refocus"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on NYSE (T)."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="tmobile", name="T-Mobile US, Inc.", short="T-Mobile US",
         group="Global Carriers", industry="Telecommunications",
         founded="1994 (as VoiceStream)", hq="Bellevue, Washington, USA",
         ceo="Mike Sievert (CEO, as publicly reported)",
         ticker="TMUS", filing="Form 10-K annual report",
         employees="approximately 70,000 (reported)",
         revenue="approximately US$81.4 billion in reported 2024 revenue",
         history=("Roots to 1994's VoiceStream; Deutsche Telekom bought it in 2001 and rebranded "
                  "it T-Mobile USA. John Legere's 'Un-carrier' disruption (2013–2020) — ending "
                  "contracts, then free international data — stole tens of millions of customers. "
                  "The Sprint merger (2020, ~US$26 billion as reported) delivered the mid-band "
                  "spectrum that made T-Mobile's 5G the US coverage and speed leader as widely "
                  "reported."),
         products=("Wireless service, 5G home internet, business connectivity, wholesale/MVNO "
                   "partnerships."),
         model=("Challenger economics: aggressive pricing and network superiority win "
                "subscribers; merger synergies (tens of billions as reported) fund the 5G build. "
                "Fixed wireless home internet is the newest growth vector."),
         milestones=["2001: Deutsche Telekom acquires VoiceStream",
                     "2013: 'Un-carrier' disruption begins",
                     "2020: Sprint merger (~US$26B as reported); Mike Sievert becomes CEO",
                     "US 5G coverage and speed leader (as widely reported)"],
         records_note=("Files annual reports on Form 10-K with the US SEC. Listed on Nasdaq "
                       "(TMUS). Majority-owned by Deutsche Telekom as publicly reported."),
         citation=("Company annual report (Form 10-K). Figures rounded as reported.")),
    dict(key="dt", name="Deutsche Telekom AG", short="Deutsche Telekom",
         group="Global Carriers", industry="Telecommunications",
         founded="1995", hq="Bonn, Germany",
         ceo="Tim Hoettges (CEO, as publicly reported)",
         ticker="DTE.DE", filing="Annual report",
         employees="approximately 199,000 (reported)",
         revenue="approximately EUR 115.8 billion in reported 2024 revenue",
         history=("Created in 1995 from the privatization of Deutsche Bundespost's telecom arm, "
                  "Deutsche Telekom became Europe's largest telecom operator. Its majority stake "
                  "in T-Mobile US — once nearly sold to AT&T in a blocked 2011 deal — became its "
                  "crown jewel and growth engine. Fiber and 5G buildouts across Germany and "
                  "Europe anchor the domestic business."),
         products=("Mobile and fixed networks (Germany, Europe, US via T-Mobile US), enterprise "
                   "ICT (T-Systems), wholesale."),
         model=("Multi-country operator scale: T-Mobile US contributes the majority of growth as "
                "reported; European operations generate steady cash; fiber/5G investment "
                "sustains the moat."),
         milestones=["1995: privatized from Deutsche Bundespost",
                     "2001: acquires VoiceStream (T-Mobile US)",
                     "2011: blocked AT&T sale — the turning point",
                     "T-Mobile US becomes the growth engine"],
         records_note=("Publishes annual reports under IFRS. Listed in Frankfurt (DTE). German "
                       "state retains a stake as publicly reported."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="ntt", name="Nippon Telegraph and Telephone Corporation", short="NTT",
         group="Asian Carriers", industry="Telecommunications and IT services",
         founded="1985", hq="Tokyo, Japan",
         ceo="Akira Shimada (president and CEO, as publicly reported)",
         ticker="9432.T / NTTYY", filing="Annual report (Yuho / Form 20-F)",
         employees="approximately 338,000 (reported)",
         revenue="approximately JPY 13.5 trillion in reported fiscal 2024 revenue",
         history=("Established in 1985 from the privatization of Japan's telephone public "
                  "corporation, NTT is among the world's largest telecom groups, spanning "
                  "NTT Docomo (mobile), NTT Data (global IT services), and NTT Communications. "
                  "Its IOWN initiative bets on all-photonic networks as the next infrastructure "
                  "leap."),
         products=("Mobile (NTT Docomo), fixed-line and data centers, global IT services "
                   "(NTT Data), enterprise solutions."),
         model=("Domestic telecom cash flows fund global IT-services expansion (NTT Data) and "
                "next-generation network R&D. Scale across telecom and IT is rare among global "
                "carriers."),
         milestones=["1985: privatized from the telephone public corporation",
                     "NTT Docomo pioneered mobile internet (i-mode, 1999)",
                     "NTT Data: global IT-services scale",
                     "IOWN all-photonic network initiative"],
         records_note=("Files annual securities reports in Japan; ADR program in the US. Listed "
                       "in Tokyo (9432). Japanese government retains a stake as publicly "
                       "reported."),
         citation=("Company annual report. Figures rounded as reported.")),
    dict(key="chinamobile", name="China Mobile Limited", short="China Mobile",
         group="Asian Carriers", industry="Telecommunications",
         founded="1997", hq="Hong Kong / Beijing, China",
         ceo="Board-led state-owned enterprise (chairman as publicly disclosed)",
         ticker="941.HK / 600941.SS", filing="Annual report (HKEX/SSE)",
         employees="approximately 450,000 (reported)",
         revenue="approximately RMB 1,040.8 billion (about US$140 billion) in reported 2024 operating revenue",
         history=("Established in 1997 in Hong Kong, China Mobile grew into the world's largest "
                  "mobile operator by subscribers — over 1 billion mobile customers as publicly "
                  "reported. State-controlled via China Mobile Communications Group, it led "
                  "China's 5G buildout (552 million 5G network customers reported for 2024) and "
                  "is expanding into cloud, digital services, and enterprise digitization."),
         products=("Mobile voice and data, 5G services, home broadband (278M+ customers as "
                   "reported), enterprise cloud and digital-transformation services."),
         model=("Unmatched domestic scale amortizes network cost across a billion-plus users; "
                "digital-transformation revenue (cloud, enterprise) is the growth layer atop "
                "mature mobile ARPU."),
         milestones=["1997: established in Hong Kong",
                     "World's largest mobile operator by subscribers (as reported)",
                     "2024: RMB 1,040.8 billion operating revenue; 552M 5G customers (as reported)",
                     "Dual-listed in Hong Kong and Shanghai"],
         records_note=("Files annual reports with HKEX and SSE. State-controlled as publicly "
                       "reported. Leadership disclosures appear in company filings."),
         citation=("Company 2024 annual results (press release and annual report). Figures rounded as reported.")),
]

# ------------------------------------------------- enrichment (12 covered cos)
# slug -> public stub facts used to build complementary financials/leadership/records entries
ENRICH = {
    "company-apple": dict(name="Apple Inc.", short="Apple", industry="Consumer electronics, software, services",
        founded="1976", hq="Cupertino, California, USA", ceo="Tim Cook",
        employees="approximately 164,000 (reported)",
        revenue="approximately US$391 billion in reported fiscal 2024 revenue",
        ticker="AAPL", filing="Form 10-K",
        fin=("Apple reported approximately US$391 billion in fiscal 2024 revenue, with iPhone "
             "the majority of product sales and services the fastest-growing segment as publicly "
             "reported. The company files annual reports on Form 10-K with the US SEC, holds "
             "tens of billions in cash and marketable securities as reported, and returns "
             "capital through dividends and buybacks."),
        lead=("Led by CEO Tim Cook (CEO since 2011, as publicly reported). Founded 1976 by Steve "
              "Jobs, Steve Wozniak, and Ronald Wayne. Governance follows a standard US public-"
              "company board structure with independent directors and committee oversight as "
              "disclosed in proxy filings."),
        recs=("Incorporated in California. Listed on Nasdaq (AAPL); Dow Jones component. "
              "Public records include SEC 10-K/10-Q filings, proxy statements, and patent "
              "assignments. Fiscal year ends the last Saturday in September.")),
    "company-msft": dict(name="Microsoft Corporation", short="Microsoft", industry="Software, cloud, gaming",
        founded="1975", hq="Redmond, Washington, USA", ceo="Satya Nadella",
        employees="approximately 228,000 (reported)",
        revenue="approximately US$245 billion in reported fiscal 2024 revenue",
        ticker="MSFT", filing="Form 10-K",
        fin=("Microsoft reported approximately US$245 billion in fiscal 2024 revenue, led by "
             "server products and cloud services (Azure) plus Office and Windows as publicly "
             "reported. Files Form 10-K with the US SEC; cloud is now the majority of revenue "
             "as reported."),
        lead=("Led by chairman and CEO Satya Nadella (CEO since 2014, as publicly reported). "
              "Founded 1975 by Bill Gates and Paul Allen. Board-led governance with independent "
              "directors as disclosed in proxy filings."),
        recs=("Incorporated in Washington. Listed on Nasdaq (MSFT); Dow Jones component. Public "
              "records include SEC filings and proxy statements. Fiscal year ends June 30.")),
    "company-googl": dict(name="Alphabet Inc.", short="Alphabet (Google)", industry="Internet services, advertising, cloud",
        founded="1998", hq="Mountain View, California, USA", ceo="Sundar Pichai",
        employees="approximately 183,000 (reported)",
        revenue="approximately US$350 billion in reported 2024 revenue",
        ticker="GOOGL / GOOG", filing="Form 10-K",
        fin=("Alphabet reported approximately US$350 billion in 2024 revenue, the large majority "
             "from Google advertising (Search, YouTube) with Google Cloud the growth engine as "
             "publicly reported. Files Form 10-K with the US SEC."),
        lead=("Led by CEO Sundar Pichai (Alphabet CEO since 2019, as publicly reported). Founded "
              "1998 by Larry Page and Sergey Brin; both retain supervoting control as publicly "
              "reported."),
        recs=("Incorporated in Delaware. Dual-class listing on Nasdaq (GOOGL/GOOG). Public "
              "records include SEC filings and proxy statements.")),
    "company-amzn": dict(name="Amazon.com, Inc.", short="Amazon", industry="E-commerce, cloud computing",
        founded="1994", hq="Seattle, Washington, USA", ceo="Andy Jassy",
        employees="approximately 1.5 million (reported)",
        revenue="approximately US$638 billion in reported 2024 revenue",
        ticker="AMZN", filing="Form 10-K",
        fin=("Amazon reported approximately US$638 billion in 2024 revenue; AWS contributes the "
             "majority of operating income despite being a minority of revenue as publicly "
             "reported. Files Form 10-K with the US SEC."),
        lead=("Led by president and CEO Andy Jassy (CEO since 2021, as publicly reported). "
              "Founded 1994 by Jeff Bezos, who remains executive chair as publicly reported."),
        recs=("Incorporated in Delaware. Listed on Nasdaq (AMZN). Public records include SEC "
              "filings and proxy statements.")),
    "company-tsla": dict(name="Tesla, Inc.", short="Tesla", industry="Electric vehicles, energy",
        founded="2003", hq="Austin, Texas, USA", ceo="Elon Musk",
        employees="approximately 125,000 (reported)",
        revenue="approximately US$97.7 billion in reported 2024 revenue",
        ticker="TSLA", filing="Form 10-K",
        fin=("Tesla reported approximately US$97.7 billion in 2024 revenue, majority from "
             "automotive sales with energy generation/storage growing as publicly reported. "
             "Files Form 10-K with the US SEC."),
        lead=("Led by CEO Elon Musk (as publicly reported). Founded 2003 by Martin Eberhard and "
              "Marc Tarpenning; Musk joined in 2004 and led subsequent funding."),
        recs=("Incorporated in Texas (reincorporated 2024 as publicly reported). Listed on Nasdaq "
              "(TSLA). Public records include SEC filings and proxy statements.")),
    "company-meta": dict(name="Meta Platforms, Inc.", short="Meta", industry="Social media, advertising, VR",
        founded="2004", hq="Menlo Park, California, USA", ceo="Mark Zuckerberg",
        employees="approximately 74,000 (reported)",
        revenue="approximately US$164.5 billion in reported 2024 revenue",
        ticker="META", filing="Form 10-K",
        fin=("Meta reported approximately US$164.5 billion in 2024 revenue, nearly all from "
             "advertising across Facebook, Instagram, and WhatsApp as publicly reported; "
             "Reality Labs operates at a reported loss while building VR/AR. Files Form 10-K "
             "with the US SEC."),
        lead=("Led by founder, chairman and CEO Mark Zuckerberg (as publicly reported). Founded "
              "2004 at Harvard. Zuckerberg retains supervoting control as publicly reported."),
        recs=("Incorporated in Delaware. Listed on Nasdaq (META). Public records include SEC "
              "filings and proxy statements. Note: the historical company name 'Facebook' "
              "appears only as fact-checked public history.")),
    "company-ssnlf": dict(name="Samsung Electronics Co., Ltd.", short="Samsung Electronics", industry="Electronics, semiconductors",
        founded="1969", hq="Suwon, South Korea", ceo="Jay Y. Lee (executive chairman, as publicly reported)",
        employees="approximately 267,000 (reported)",
        revenue="approximately KRW 300.9 trillion in reported 2024 revenue",
        ticker="005930.KS", filing="Annual report (DART)",
        fin=("Samsung Electronics reported approximately KRW 300.9 trillion in 2024 revenue, led "
             "by semiconductors (notably memory) and mobile as publicly reported. Files with "
             "Korea's DART system and reports under IFRS."),
        lead=("Executive chairman Jay Y. Lee (as publicly reported). Founded 1969. Part of the "
              "Samsung chaebol; governance disclosures filed under Korean regulations."),
        recs=("Incorporated in South Korea. Listed on KRX (005930). Public records include DART "
              "filings and sustainability reports.")),
    "company-nvda": dict(name="NVIDIA Corporation", short="NVIDIA", industry="Semiconductors — GPUs, AI",
        founded="1993", hq="Santa Clara, California, USA", ceo="Jensen Huang",
        employees="approximately 36,000 (reported)",
        revenue="approximately US$130.5 billion in reported fiscal 2025 revenue",
        ticker="NVDA", filing="Form 10-K",
        fin=("NVIDIA reported approximately US$130.5 billion in fiscal 2025 revenue, the large "
             "majority from data-center GPUs for AI as publicly reported. Files Form 10-K with "
             "the US SEC; fiscal year ends late January."),
        lead=("Led by founder, president and CEO Jensen Huang (as publicly reported). Founded "
              "1993 by Huang, Chris Malachowsky, and Curtis Priem."),
        recs=("Incorporated in Delaware. Listed on Nasdaq (NVDA); Dow Jones component. Public "
              "records include SEC filings and proxy statements.")),
    "company-tm": dict(name="Toyota Motor Corporation", short="Toyota", industry="Automotive manufacturing",
        founded="1937", hq="Toyota City, Japan", ceo="Koji Sato",
        employees="approximately 375,000 (reported)",
        revenue="approximately JPY 37.2 trillion in reported fiscal 2024 revenue",
        ticker="7203.T / TM", filing="Form 20-F",
        fin=("Toyota reported approximately JPY 37.2 trillion in fiscal 2024 revenue and remains "
             "the world's top-selling automaker by volume as publicly reported. Files Form 20-F "
             "with the US SEC."),
        lead=("Led by president and CEO Koji Sato (as publicly reported). Founded 1937 by "
              "Kiichiro Toyoda. Toyota Production System is its management signature."),
        recs=("Incorporated in Japan. Listed in Tokyo (7203) and New York (TM, ADR). Public "
              "records include securities reports and SEC filings.")),
    "company-sony": dict(name="Sony Group Corporation", short="Sony", industry="Electronics, entertainment, financial services",
        founded="1946", hq="Tokyo, Japan", ceo="Kenichiro Yoshida",
        employees="approximately 113,000 (reported)",
        revenue="approximately JPY 13 trillion in reported fiscal 2024 revenue",
        ticker="6758.T / SONY", filing="Form 20-F",
        fin=("Sony reported approximately JPY 13 trillion in fiscal 2024 revenue across game, "
             "music, pictures, imaging sensors, and financial services as publicly reported. "
             "Files Form 20-F with the US SEC."),
        lead=("Led by chairman and CEO Kenichiro Yoshida (as publicly reported). Founded 1946 "
              "by Masaru Ibuka and Akio Morita."),
        recs=("Incorporated in Japan. Listed in Tokyo (6758) and New York (SONY, ADR). Public "
              "records include securities reports and SEC filings.")),
    "company-intc": dict(name="Intel Corporation", short="Intel", industry="Semiconductors",
        founded="1968", hq="Santa Clara, California, USA", ceo="Lip-Bu Tan (as publicly reported)",
        employees="approximately 109,000 (reported)",
        revenue="approximately US$53 billion in reported 2024 revenue",
        ticker="INTC", filing="Form 10-K",
        fin=("Intel reported approximately US$53 billion in 2024 revenue amid its foundry "
             "turnaround as publicly reported. Files Form 10-K with the US SEC."),
        lead=("Led by CEO Lip-Bu Tan (as publicly reported). Founded 1968 by Robert Noyce and "
              "Gordon Moore; Andy Grove built its management legend."),
        recs=("Incorporated in Delaware. Listed on Nasdaq (INTC). Public records include SEC "
              "filings and proxy statements.")),
    "company-ibm": dict(name="International Business Machines Corporation", short="IBM", industry="IT services, software, hardware",
        founded="1911", hq="Armonk, New York, USA", ceo="Arvind Krishna",
        employees="approximately 288,000 (reported)",
        revenue="approximately US$62.8 billion in reported 2024 revenue",
        ticker="IBM", filing="Form 10-K",
        fin=("IBM reported approximately US$62.8 billion in 2024 revenue, led by software and "
             "consulting after the Kyndryl separation as publicly reported. Files Form 10-K "
             "with the US SEC."),
        lead=("Led by chairman and CEO Arvind Krishna (CEO since 2020, as publicly reported). "
              "Founded 1911 as the Computing-Tabulating-Recording Company."),
        recs=("Incorporated in New York. Listed on NYSE (IBM); Dow Jones component. Public "
              "records include SEC filings and proxy statements.")),
}

SECTOR_DATA = {
    "technology-companies": TECH,
    "finance-companies": FINANCE,
    "automotive-companies": AUTO,
    "healthcare-companies": HEALTH,
    "retail-consumer-companies": RETAIL,
    "energy-industrial-companies": ENERGY,
    "media-entertainment-companies": MEDIA,
    "telecom-companies": TELECOM,
}
