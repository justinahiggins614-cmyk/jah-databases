/* JAH Banking Database generator — jahdb-banking-1.0.
   Deterministic client-side generator. Same seed + same version always makes
   the same record. Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['accounts','lending','payments','cards','regulation','treasury','trade','fintech'];
var PREFIX='JAH-BNK-';
/* Anchors: [name, category, fact1, fact2, example context, example fact]. */
var ANCHORS=[
["FDIC Deposit Insurance","regulation","FDIC insurance covers 250000 dollars per depositor, per insured bank, for each account ownership category, backed by the full faith and credit of the United States government.","Ownership categories include single, joint, certain retirement, trust, employee benefit plan, corporate, and government accounts.","United States","Coverage is automatic, since depositors never apply, and it has protected depositors since 1933."],
["Checking Accounts","accounts","Checking accounts hold transaction balances for daily spending, with debit cards, checks, and electronic payments drawing on them.","The FDIC insures checking balances as deposit products at insured banks.","United States","Direct deposit routes paychecks straight into checking."],
["Savings Accounts","accounts","Savings accounts pay interest on balances held for future needs.","They are FDIC-insured deposit products at insured banks.","United States","High-yield online savings accounts compete on interest rate."],
["Certificates of Deposit","accounts","Certificates of deposit lock funds for a fixed term of months to years, paying higher interest than liquid savings.","Early withdrawal typically triggers a penalty, and the FDIC insures CDs as time deposits.","United States","CD ladders stagger maturities to balance yield and liquidity."],
["Money Market Deposit Accounts","accounts","Money market deposit accounts pay tiered interest on larger balances with limited check-writing.","The FDIC insures money market deposit accounts as deposit products.","United States","They blend savings yield with limited transaction access."],
["ACH Transfers","payments","The Automated Clearing House is a batch network run under Nacha rules, with banks submitting instructions that clear in scheduled windows.","Standard ACH settles in one to three business days, while Same Day ACH settles in same-day windows and is capped at one million dollars per transfer.","United States","Payroll direct deposit and recurring bill pay run on ACH."],
["Fedwire","payments","Fedwire is the Federal Reserve's real-time gross settlement system, in which each wire settles individually and immediately.","Domestic wires usually complete within hours, are effectively final, and cost roughly 25 to 50 dollars.","United States","Real-estate closings and legal settlements use Fedwire for same-day finality."],
["SWIFT Network","payments","SWIFT is the messaging network banks use for international wires, routing payments through correspondent and intermediary banks.","Cross-border wires typically take one to five business days, with fees deducted at each hop.","Global","SWIFT connects more than eleven thousand institutions worldwide."],
["Same-Day ACH","payments","Same Day ACH moves lower-value payments within hours through designated same-day processing windows.","It costs more than standard ACH but far less than a wire.","United States","Nacha expanded same-day windows to speed business payments."],
["Wire Transfer Finality","payments","Once a wire settles, it is effectively irreversible, unlike ACH, which can be returned within set windows.","That finality makes wires a favorite target for fraud, so verification callbacks are standard practice.","United States","Title companies verify wiring instructions by phone before closings."],
["Credit Cards","cards","Credit cards extend revolving credit: borrow up to a limit, pay at least a minimum monthly, and pay interest on carried balances.","Grace periods waive interest when the full statement balance is paid.","Global","Rewards cards return a share of spending as points or cash back."],
["Debit Cards","cards","Debit cards pull directly from a checking balance, so spending is limited to available funds.","They carry no interest charges but may offer fewer purchase protections than credit cards.","Global","PIN and chip verification authorize debit transactions."],
["EMV Chip Cards","cards","EMV chips create a unique transaction code for each payment, defeating simple card cloning.","Chip verification replaced magnetic-stripe swipes across most markets.","Global","The United States completed its EMV liability shift in 2015."],
["Chargebacks","cards","Chargebacks let cardholders dispute transactions through their issuing bank, reversing the payment to the merchant.","Merchants fight friendly fraud with delivery proof and clear descriptors.","Global","Card networks set reason codes and time limits for disputes."],
["Contactless NFC Payments","payments","Near-field communication lets cards and phones pay with a tap, tokenizing the card number so merchants never see it.","Transaction limits for no-PIN taps vary by country.","Global","Transit systems adopted open-loop contactless fare payment."],
["Fixed-Rate Mortgages","lending","Fixed-rate mortgages lock one interest rate for the whole term, commonly thirty or fifteen years in the United States.","Monthly payments stay constant, with principal plus interest amortized over the term.","United States","The thirty-year fixed is the standard American home loan."],
["Adjustable-Rate Mortgages","lending","Adjustable-rate mortgages start with a fixed teaser period, then reset periodically against a benchmark index plus margin.","Rate caps limit how far payments can jump at each reset and over the loan's life.","United States","A 5/1 ARM fixes the rate for five years, then adjusts annually."],
["Amortization","lending","Amortization repays a loan in fixed installments where early payments are mostly interest and later ones mostly principal.","Amortization schedules show the exact split for every payment.","Global","A thirty-year mortgage makes 360 amortized payments."],
["FICO Credit Scores","lending","FICO scores range from 300 to 850, summarizing payment history, utilization, account age, inquiries, and credit mix.","Payment history carries the largest weight in the score.","United States","Lenders tier mortgage rates by score band."],
["Annual Percentage Rate","lending","The annual percentage rate expresses a loan's yearly cost including interest and certain fees, enabling apples-to-apples comparison.","Truth-in-lending rules require APR disclosure on consumer credit.","United States","A lower rate with high fees can mean a higher APR."],
["Home Equity Lines of Credit","lending","Home equity lines let homeowners borrow against equity through a revolving line, usually with variable rates.","Draw periods allow borrowing, while repayment periods amortize the balance.","United States","Interest may be deductible when the funds improve the home."],
["Auto Loans","lending","Auto loans are secured by the vehicle, with terms commonly from 36 to 72 months.","The lender can repossess the car on default.","United States","Dealers and banks compete on auto-loan APRs."],
["Small Business Administration Loans","lending","United States Small Business Administration programs guarantee portions of bank loans to small firms, reducing lender risk.","The 7(a) program is the flagship general-purpose loan.","United States","SBA guarantees have helped millions of small businesses borrow."],
["Microfinance","lending","Microfinance extends tiny loans, often to women entrepreneurs, using group guarantees instead of collateral.","The Grameen Bank model in Bangladesh pioneered the approach in the late twentieth century.","Bangladesh","Grameen-style lending spread across the developing world."],
["Letters of Credit","trade","A letter of credit has the buyer's bank guarantee payment to the seller once shipping documents are presented.","It bridges trust gaps in international trade.","Global","Documentary credits follow the ICC Uniform Customs and Practice."],
["Factoring and Supply-Chain Finance","trade","Factoring sells invoices to a finance company at a discount for immediate cash.","Exporters use forfaiting and export credit insurance for longer terms.","Global","Supply-chain finance programs let suppliers get paid early."],
["Correspondent Banking","payments","Correspondent banks hold accounts for foreign banks, clearing payments where the foreign bank has no branch.","De-risking has shrunk correspondent networks in some regions.","Global","Dollar clearing runs through United States correspondent banks."],
["Foreign Exchange Markets","treasury","Foreign exchange markets trade currency pairs around the clock, with spot settlement typically in two business days.","Corporates hedge currency exposure with forwards, swaps, and options.","Global","The dollar anchors most global foreign-exchange turnover."],
["Repurchase Agreements","treasury","In a repurchase agreement, one party sells securities and agrees to repurchase them later, which is effectively collateralized short-term borrowing.","Overnight repo rates are a key gauge of funding-market stress.","United States","The Federal Reserve conducts repo operations to implement monetary policy."],
["Treasury Securities","treasury","United States Treasury bills, notes, and bonds finance federal borrowing across maturities from weeks to thirty years.","They are considered the global risk-free benchmark.","United States","Treasury auctions set yields the whole market watches."],
["Federal Funds Rate","regulation","The federal funds rate is the target for overnight lending between banks holding reserves at the Federal Reserve.","The Fed moves it to steer employment and price stability.","United States","Mortgage and credit-card rates follow the federal funds path."],
["Reserve Requirements","regulation","Reserve requirements once forced banks to hold a share of deposits at the central bank, until the Fed set the United States requirement to zero in 2020.","Capital requirements, not reserves, are now the binding constraint.","United States","The Federal Reserve eliminated reserve requirements in March 2020."],
["Basel III Capital Rules","regulation","Basel III sets global minimum capital standards, including common equity tier one ratios and liquidity buffers.","Systemically important banks face extra surcharges.","Global","The Basel Committee on Banking Supervision wrote the framework."],
["KYC and AML Compliance","regulation","Know-your-customer rules verify client identity, while anti-money-laundering programs monitor and report suspicious activity.","Banks file suspicious activity reports with financial intelligence units.","Global","The United States Bank Secrecy Act anchors American anti-money-laundering law."],
["SEPA Payments","payments","The Single Euro Payments Area standardizes euro transfers across Europe, making cross-border payments as easy as domestic ones.","SEPA Instant settles euro payments in seconds, around the clock.","Europe","SEPA covers more than thirty-six countries."],
["UPI Instant Payments","payments","India's Unified Payments Interface enables instant bank-to-bank transfers by phone number or QR code, free to users.","UPI processes billions of transactions monthly.","India","UPI launched in 2016 under the National Payments Corporation of India."],
["Peer-to-Peer Payment Apps","fintech","Peer-to-peer apps move money between individuals instantly using bank links or stored balances.","Social feeds and QR codes made splitting bills frictionless.","Global","Venmo, Cash App, and Zelle dominate United States peer-to-peer payments."],
["Neobanks and Digital Banks","fintech","Neobanks operate without branches, competing on slick apps, low fees, and fast onboarding.","Many partner with chartered banks for deposit insurance.","Global","Chime, Revolut, and Nubank scaled to tens of millions of users."],
["Central Bank Digital Currencies","fintech","Central bank digital currencies are digital cash issued directly by central banks, distinct from commercial-bank deposits and crypto assets.","Designs range from retail wallets to wholesale settlement tokens.","Global","China's e-CNY pilots and the Bahamas Sand Dollar led live launches."],
["Escrow Services","lending","Escrow holds funds with a neutral third party until contract conditions are met.","Mortgage escrow accounts collect tax and insurance installments monthly.","United States","Real-estate closings route purchase funds through escrow."],
["Cashier's Checks","payments","A cashier's check is drawn on the bank's own funds, making it effectively guaranteed.","The FDIC lists cashier's checks among insured official items.","United States","Sellers accept cashier's checks for large private sales."],
["Money Orders","payments","Money orders prepay a fixed amount, useful for people without checking accounts.","Caps per money order are typically around one thousand dollars.","United States","Post offices and retailers sell money orders."],
["Direct Deposit","payments","Direct deposit pushes payroll electronically into employee accounts via ACH.","It is faster and cheaper than paper checks.","United States","Most American workers are paid by direct deposit."],
["Mobile Check Deposit","fintech","Remote deposit capture lets customers photograph checks to deposit them by phone.","Banks verify images and usually make funds available within a business day or two.","United States","Check 21 legislation enabled image-based clearing."],
["Overdraft Programs","accounts","Overdraft lets transactions clear beyond the balance for a fee, and opt-in rules govern debit-card overdrafts in the United States.","Regulators have pressed banks to cut overdraft fees.","United States","Many banks now offer grace amounts or no-fee overdraft buffers."],
["Credit Unions","accounts","Credit unions are member-owned cooperatives offering the same core services as banks.","Deposits are insured by the NCUA, not the FDIC, up to the same 250000 dollar standard.","United States","Membership is based on a common bond such as employer or community."],
["Merchant Accounts","fintech","Merchant accounts let businesses accept card payments, with processors settling batches daily.","Interchange fees flow to the cardholder's bank on each sale.","Global","Stripe and Square simplified merchant onboarding."],
["Remittances","payments","Remittances are cross-border transfers from migrant workers to families back home.","The World Bank tracks hundreds of billions in annual flows to developing countries.","Global","Mobile money made remittances cheaper in Africa and Asia."],
["Safe Deposit Boxes","accounts","Safe deposit boxes store valuables in bank vaults under dual-key access.","The FDIC explicitly does not insure box contents.","United States","Boxes range from small document slots to large chests."],
["Islamic Banking","lending","Islamic banking follows Sharia principles, prohibiting interest, called riba, and excessive uncertainty, called gharar.","Instead of interest it uses profit-sharing, leasing, and trade-based contracts such as murabaha and sukuk.","Global","Malaysia and the Gulf states are major hubs for Islamic finance."]
];
var LENSES=[
["Core Overview","online","This overview edition presents {n} as a core {c} concept in modern banking.",null],
["How It Works","online","In practice, {n} works through regulated institutions, standardized networks, and daily settlement cycles.",null],
["Key Mechanics","signature","Its key mechanics include account structures, clearing rules, fee schedules, and reconciliation controls.",null],
["Real-World Use","online","{p} shows it in use: {f}",null],
["Consumer Guide","signature","Consumers should compare fees, read disclosures, and match the product to their actual usage pattern.","Edition {e} updates the comparison checklist."],
["Comparative Analysis","signature","Compared with alternatives in {c}, {n} trades cost and speed against control and finality in predictable ways.",null],
["Historical Development","signature","The instrument matured through twentieth-century banking practice and keeps adapting to digital rails.",null],
["Fees and Costs","signature","Total cost includes stated fees plus less visible spreads, so effective cost must be computed, not assumed.",null],
["Risk Review","signature","A risk review covers credit, operational, fraud, and compliance risk, with controls matched to each.",null],
["Regulatory Notes","online","Regulators set the guardrails for {n}, and compliance programs translate rules into daily controls.","Supervised institutions document every material control."],
["Signature Case Study","signature","This Signature case study walks {n} through a realistic customer scenario, from onboarding to settlement.","All figures here are illustrative scenarios, not financial advice."],
["Fraud and Security","signature","Fraud controls layer verification, monitoring, and customer education, since social engineering defeats technology alone.",null],
["Digital Alternatives","signature","Digital alternatives now replicate {n} with faster onboarding, though they inherit the same underlying rails.",null],
["Business Use","signature","Businesses adopt {n} for predictable cash flow, audit trails, and integration with accounting systems.",null],
["International View","signature","Across borders, {n} must navigate correspondent networks, currency conversion, and divergent regulations.",null],
["Cost Planning","signature","Households and firms plan around {n} by modeling fees under realistic usage, not brochure scenarios.",null],
["Glossary Entry","signature","In plain terms, {n} is a standard {c} tool for moving, storing, or pricing money.",null],
["Eligibility and Access","signature","Access depends on identity verification, account standing, and product-specific eligibility rules.",null],
["Future Outlook","signature","Over the next decade, expect faster settlement, richer data, and tighter fraud controls around {n}.",null],
["Common Misconceptions","signature","A common misconception about {n} is that headline rates tell the whole story, when fees and timing matter as much.",null]
];
var CATDATA={
"accounts":{terms:["Deposit product","Interest accrual","FDIC insurance","Account ownership category"],how:"Funds sit in insured deposit accounts, earning interest according to published tiers, with ownership category determining insurance coverage."},
"lending":{terms:["Principal","Interest rate and APR","Amortization schedule","Collateral"],how:"Lenders underwrite borrowers, disburse principal, and collect amortized payments of principal plus interest over the term."},
"payments":{terms:["Payment rail","Clearing and settlement","Finality","Cutoff time"],how:"Instructions travel a payment rail, clear through network windows, and settle finally into the receiver's account."},
"cards":{terms:["Issuing bank","Acquiring bank","Interchange fee","Authorization"],how:"Cards authorize against a credit line or deposit balance, clear in batches, and settle between issuing and acquiring banks."},
"regulation":{terms:["Supervisory agency","Compliance program","Reporting requirement","Enforcement action"],how:"Agencies write rules, institutions build compliance programs, examiners test controls, and violations draw enforcement."},
"treasury":{terms:["Yield curve","Duration","Liquidity buffer","Counterparty"],how:"Treasury desks manage cash, funding, and rate exposure across money markets and securities portfolios."},
"trade":{terms:["Documentary credit","Bill of lading","Incoterms","Confirming bank"],how:"Trade instruments bridge trust between distant buyers and sellers through bank guarantees tied to shipping documents."},
"fintech":{terms:["API integration","Onboarding and KYC","Custodial account","Interchange revenue"],how:"Fintech firms build software on top of chartered-bank rails, owning the customer experience while partners hold the charter."}
};
function fill(tpl,a,lens,ed){return tpl.replace(/\{n\}/g,a[0]).replace(/\{c\}/g,a[1]).replace(/\{p\}/g,a[4]).replace(/\{f\}/g,a[5]).replace(/\{e\}/g,String(ed));}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var ai=(seed-1)%ANCHORS.length;
  var lix=Math.floor((seed-1)/ANCHORS.length)%LENSES.length;
  var ed=(Math.floor((seed-1)/(ANCHORS.length*LENSES.length))%10)+1;
  if(opts.category){var matches=[];for(var m=0;m<ANCHORS.length;m++)if(ANCHORS[m][1]===opts.category)matches.push(m);if(matches.length)ai=matches[(seed-1)%matches.length];}
  var a=ANCHORS[ai],lens=LENSES[lix];
  var cd=CATDATA[a[1]];
  var desc=a[2]+' '+a[3]+' '+fill(lens[2],a,lens,ed);
  if(lens[3])desc+=' '+fill(lens[3],a,lens,ed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={
    id:id,
    title:a[0]+' — '+lens[0]+' (Edition '+ed+')',
    description:desc,
    category:a[1],
    src:lens[1],
    spec:{
      instrument:a[0],
      category:a[1],
      lens:lens[0],
      edition:ed,
      how_it_works:cd.how,
      key_terms:cd.terms.slice(),
      real_world_use:a[4]+': '+a[5],
      risk_notes:'Standard controls apply: verification, monitoring, reconciliation, and documented compliance procedures.',
      typical_costs:'Costs vary by institution and usage; compare published fee schedules and compute effective cost under realistic volumes.',
      source_note:lens[1]==='online'?'Core facts verified from public sources.':'Signature-generated expansion built on verified anchor facts.'
    },
    _seed:seed
  };
  return rec;
}
function countSentences(s){var t=String(s).replace(/\d+\.\d+/g,'N');var m=t.match(/[^.!?]+[.!?]/g);return m?m.length:0;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not-object']};
  if(!/^JAH-BNK-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>180)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  var ns=countSentences(r.description||'');
  if(ns<2||ns>4)e.push('sentences:'+ns);
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(typeof s.instrument!=='string'||!s.instrument.length)e.push('spec.instrument');
    if(s.category!==r.category)e.push('spec.category');
    if(typeof s.how_it_works!=='string'||!s.how_it_works.length)e.push('spec.how_it_works');
    if(!Array.isArray(s.key_terms)||s.key_terms.length!==4)e.push('spec.key_terms');
    if(typeof s.real_world_use!=='string'||!s.real_world_use.length)e.push('spec.real_world_use');
    if(typeof s.risk_notes!=='string'||!s.risk_notes.length)e.push('spec.risk_notes');
    if(typeof s.edition!=='number'||s.edition<1||s.edition>10)e.push('spec.edition');
  }
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){var ids={};(sample||[]).forEach(function(x){if(x&&x.id)ids[x.id]=1;});return ids[rec.id]?{ok:false,errors:['duplicate-id']}:{ok:true,errors:[]};}
var gen={version:'jahdb-banking-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('banking',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
if(typeof require!=='undefined'&&require.main===module){
  var ok=0,fail=[];
  for(var i=1;i<=40;i++){var v=validate(generate(i,{},prng(i)));if(v.ok)ok++;else fail.push([i,v.errors]);}
  console.log('banking harness: '+ok+'/40 '+(ok===40?'PASS':'FAIL'));
  if(fail.length)console.log(JSON.stringify(fail));
}
})();
