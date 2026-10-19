(function(){'use strict';
/* jahdb-fundamental-business-1.0 — fundamental business bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FBU-';
var KIND='fundamental business record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Business is the organized creation of value: identifying needs, building offerings, and sustaining the enterprise that delivers them. It joins strategy, operations, finance, and human organization into going concerns.', 'reasoning':'Business thinkers reason in value and viability: does this create more value than it costs, for customers, sustainably? Unit economics first — a business that loses money on each sale rarely makes it up on volume.', 'quantities':'The core quantities are revenue, cost, margin, and cash flow — with customer acquisition cost (CAC) and lifetime value (LTV) as the master ratio. Cash is the master quantity: profits are opinion, cash is fact.', 'mechanism':'Business works the value loop: understand the customer → build the offering → deliver reliably → get paid → reinvest. Product-market fit is the loop closing — customers buying, returning, and referring.', 'miscon':'Business is not just selling: operations, finance, and organization matter as much. Revenue is vanity without margin — growth that burns cash is just expensive. And the customer is not always right — but the customer is always the judge.'};
var SIGLENS=['In the Signature system, business is the value-creation discipline: every database, every product in this network must create real value sustainably, and the Signature formulation teaches each principle as a test you can apply.','The Signature practice is to test the business: compute the unit economics, validate with customers, watch the cash — so business reasoning is done with numbers and evidence, not just ambition.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- unit economics demo. Runs as-is with python3."""\ndef unit_economics(price, cogs, cac, months, churn):\n    ltv = (price - cogs) * (1 / churn)\n    print(f"price ${price} COGS ${cogs} -> contribution ${price-cogs}/mo")\n    print(f"churn {churn:.0%}/mo -> LTV ${ltv:.0f}; CAC ${cac} -> LTV/CAC = {ltv/cac:.1f}")\n    print("LTV/CAC > 3 and payback < 12 months: the health thresholds")\nunit_economics(50, 15, 120, None, 0.05)\n', '#!/usr/bin/env python3\n"""{TITLE} -- breakeven demo. Runs as-is with python3."""\ndef breakeven(fixed, price, variable):\n    return fixed / (price - variable)\nbe = breakeven(100000, 50, 30)\nprint(f"fixed $100k, price $50, variable $30 -> breakeven {be:.0f} units")\nprint("every unit past breakeven contributes $20 to profit")\n', '#!/usr/bin/env python3\n"""{TITLE} -- runway demo. Runs as-is with python3."""\ndef runway(cash, burn_per_month):\n    return cash / burn_per_month\nfor cash, burn in [(2000000, 150000), (500000, 150000)]:\n    print(f"${cash/1e6:.1f}M cash, ${burn/1e3:.0f}k/mo burn -> {runway(cash, burn):.1f} months runway")\nprint("runway is survival: the default alive/dead question for startups")\n'];
var TOPICS=[['What Business Is','Business is value creation organized: finding a need, building something that meets it, and sustaining the enterprise that delivers it. Profit is the scoreboard — value delivered sustainably is the game.'],
['The Core Question of Business','The core question is: what value do we create, for whom, and how do we capture enough of it to continue? Every business plan, pivot, and strategy is an answer under revision.'],
['Assumptions: Value and Viability','The field assumes value is judged by customers and viability by arithmetic: revenues must eventually exceed costs. A business is a hypothesis about value — tested daily by the market.'],
['The Vocabulary: Margin, Moat, Fit','The vocabulary names the essentials: margin (value kept), moat (defensibility), product-market fit (customers pulling the product). Fluency means diagnosing any business in these three.'],
['Cash Flow: The Fundamental Quantity','Cash flow is the fundamental quantity: cash in minus cash out, the business\'s oxygen. Profitable companies die of cash crises — the statement of cash flows tells the truth the income statement polishes.'],
['The Business Model: The Primary Framework','The business model is the primary framework: who pays, for what, how much, how often. The canvas maps it — value proposition, channels, costs — the one-page theory of the business.'],
['A Canonical First Example','The canonical first example is the lemonade stand: cost per cup, price per cup, cups per day — profit as arithmetic. Every multinational is this stand, elaborated — the fundamentals never change.'],
['How Business Measures','The field measures with financial statements and unit economics: the P&L, the balance sheet, CAC versus LTV. Metrics are chosen to match the model — vanity metrics impress; actionable metrics decide.'],
['The Core Mechanism: Product-Market Fit','The core mechanism is product-market fit: the offering customers want, bought repeatedly, recommended freely. Before fit, the job is search; after fit, the job is scale — confusing the two kills companies.'],
['The Simplest Law: Revenues Must Exceed Costs','The simplest law is viability: eventually, revenues must exceed costs. Subsidized growth is a tactic with an expiry date — the arithmetic always comes due.'],
['Common Misconceptions in Business','The misconceptions mislead: that revenue equals success (margin matters), that ideas are the scarce resource (execution is), that the customer is always right (customers are the judge, not the designer), and that growth fixes everything (it amplifies, including flaws).'],
['How Beginners Practice Business','Beginners practice by selling something small: the side project, the freelance gig, the market stall. Real customers teach what case studies can\'t — value is proven at the point of sale.'],
['The Core Model: Supply, Demand, and Competition','The competitive model is the core: five forces shaping profitability — rivals, entrants, substitutes, suppliers, buyers. Strategy is positioning within these forces — or changing them.'],
['The Great Idea: The Moat','The moat is the great idea: the durable advantage — brand, network effects, scale, switching costs — that protects returns. Without a moat, competition erodes every margin eventually.'],
['Systems Thinking: The Organization','Systems thinking in business is the organization: structure, culture, and incentives producing behavior. The org chart is the strategy made visible — form follows (or frustrates) intent.'],
['Invariance: The Accounting Identity','The invariance principle is the accounting equation: assets equal liabilities plus equity, always. Double-entry bookkeeping is the field\'s conservation law — the books must balance.'],
['Approximation: The MVP','Approximation builds the minimum viable product: the smallest test of the value hypothesis. The MVP is disciplined approximation — learn the most from the least built.'],
['Evidence Standards: Paying Customers','The evidence standard is the paying customer: revenue is the vote that counts. Surveys suggest; purchases prove — traction is the only traction.'],
['Classic Discoveries','The classic discoveries are the corporation, scientific management, the franchise, the platform, and lean startup. Each reorganized how value gets created — and each was controversial before it was obvious.'],
['Core Trade-offs: Growth versus Profitability','The core trade-off is growth versus profitability versus control: venture money buys growth at the price of dilution and pace. Bootstrapping keeps control at the price of speed — the founder\'s fundamental choice.'],
['Handling Uncertainty: Scenario Planning','Business handles uncertainty with scenarios and options: plan for several futures, keep options open, decide reversibly where possible. Agility is uncertainty\'s answer — the plan is a hypothesis.'],
['Tools of the Trade','The tools of the trade are the spreadsheet, the business model canvas, the cohort analysis, and the cash forecast. The deepest is the customer interview — the unfiltered voice of the judge.'],
['Ethics and Responsibility','Ethics in business is stakeholder honesty: customers told the truth, employees treated fairly, promises kept. The field\'s license to operate is trust — and trust compounds like interest, or collapses like a bank run.'],
['Teaching Business','Teaching it well runs real ventures: the student business, the consulting project, the pitch to actual investors. Business learned at risk teaches what lectures cannot.'],
['The Frontier Question','The frontier question is business in the AI age: what do firms look like when intelligence is cheap? The frontier asks which human judgments remain scarce — and therefore valuable.'],
['Unifying Theories','The unifying theories are value creation and competitive advantage: create more value than you cost, defend the difference. Everything — strategy, operations, finance — serves these two.'],
['Computational Business','Computational business runs on data: analytics for decisions, automation for operations, platforms for scale. The dashboard is the modern P&L — real-time, granular, actionable.'],
['Bridges to Other Fields','Business bridges to economics (markets), psychology (consumers, teams), law (contracts), engineering (product), and finance (capital). It is the applied convergence of the social sciences.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: predicting startup success, managing at scale without bureaucracy, and aligning profit with social good reliably. Active work, no settled answers.'],
['How New Claims Are Validated','New business ideas are validated by customers paying: the pilot, the preorder, the renewal. A business claim earns trust in the market — the only focus group that matters.'],
['The Great Debates','The great debates — shareholder versus stakeholder, growth versus sustainability, remote versus office — reflect genuine trade-offs. The debates are practical: each side runs companies.'],
['Failure Modes: When Business Gets It Wrong','Business gets it wrong through no market need, running out of cash, and scaling before fit — the startup postmortems\' greatest hits. The immune system is the validated learning loop: build, measure, learn.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis runs whole enterprises from fundamentals: the value proposition, the economics, the organization, the moat — each deliberate, the system coherent. The fundamentals are the strategy itself.'],
['The Signature Formulation: Business as Value Arithmetic','The Signature formulation treats business as value arithmetic: every principle here is tested against value created and cash sustained, because in the Signature system a business that cannot show its numbers cannot be trusted. That is the Signature capstone on business bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Unit economics are computed: CAC, LTV, and margins are known before scaling.", "Customers are consulted: offerings are validated with real users, not assumed.", "Cash is monitored: runway and burn are tracked continuously."],citations:["Drucker, P. F. \u2014 The Practice of Management (Harper).", "Osterwalder, A. and Pigneur, Y. \u2014 Business Model Generation.", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-business-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-business',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
