// Boundless generator for documented-probabilities-signature (The Documented Probabilities Signature Database)
// SELF-REGULATION: hard stop at 10^15 records per database, or earlier on genuine completion
// (marked complete with reason). Throttled: at most 1000 records per call.
// Output labeling: built records are "assistant-built"; everything this generator emits is "generated".
// Generator ladder: simple -> most-competitive -> mix-and-match -> unmade -> top-notch-or-better
//                   -> future-grade -> god-mode
const CAP = 10n ** 15n;
const THROTTLE = 1000;
const LADDER = ["simple","most-competitive","mix-and-match","unmade","top-notch-or-better","future-grade","god-mode"];
const SEED_TITLES = ["Birthday Paradox: 23 People, 50.7% \u2014 Signature Edition", "Birthday Paradox: 70 People, 99.92% \u2014 Signature Edition", "Ten Heads in a Row: 1 in 1,024 \u2014 Signature Edition", "Two Dice Sum to Seven: 1 in 6 \u2014 Signature Edition", "6/49 Lottery Jackpot: 1 in 13,983,816 \u2014 Signature Edition", "US Powerball Jackpot: 1 in 292,201,338 \u2014 Signature Edition", "US Mega Millions Jackpot: 1 in 302,575,350 \u2014 Signature Edition", "Struck by Lightning in a Year (US): ~1 in 1,222,000 \u2014 Signature Edition", "NSC Lifetime Odds of Dying: Motor Vehicle 1 in 101 \u2014 Signature Edition", "Monty Hall: Switching Wins 2/3 of the Time \u2014 Signature Edition", "Normal Distribution: 68-95-99.7 Rule \u2014 Signature Edition", "Royal Flush in Poker: 1 in 649,740 \u2014 Signature Edition", "Pocket Aces in Texas Hold'em: 1 in 221 \u2014 Signature Edition", "European Roulette Single Number: 1 in 37 \u2014 Signature Edition", "Craps Pass Line: 49.29% Player Win \u2014 Signature Edition", "Bayes' Theorem: The Mammography Example, 7.8% \u2014 Signature Edition", "At Least One Six in Four Dice Rolls: 51.77% \u2014 Signature Edition", "At Least One Double-Six in 24 Rolls: 49.14% \u2014 Signature Edition", "Two Shuffled Decks Identical: 1 in 52! \u2014 Signature Edition", "Guessing an 8-Letter Lowercase Password: 1 in 208 Billion \u2014 Signature Edition", "Six Sigma: 3.4 Defects Per Million \u2014 Signature Edition", "The 0.05 Significance Threshold (Fisher's Convention) \u2014 Signature Edition", "Benford's Law: Leading Digit 1 Appears 30.1% \u2014 Signature Edition", "Bell State Measurement: 50/50, Never Mixed \u2014 Signature Edition", "Hash Collision at the Birthday Bound: 2^64 Draws, ~50% \u2014 Signature Edition", "USGS: 72% Chance of M\u22656.7 Quake in Bay Area Within 30 Years \u2014 Signature Edition", "Gambler's Fallacy vs. the Hot Hand: Documented Findings \u2014 Signature Edition", "Simpson's Paradox: Documented Reversal Pattern \u2014 Signature Edition", "Laplace's Rule of Succession: The Sunrise Problem \u2014 Signature Edition", "St. Petersburg Paradox: Infinite Expectation, Finite Price \u2014 Signature Edition", "False-Positive Paradox: 1% Prevalence, 95% Accurate Test \u2014 Signature Edition", "Quantum Tunneling: Documented Exponential Sensitivity \u2014 Signature Edition", "Actuarial Present Value: A Life Annuity's Survival Curve \u2014 Signature Edition", "The Friendship Paradox: Your Friends Have More Friends \u2014 Signature Edition", "Inspection Paradox: The Bus You Wait For Is Late \u2014 Signature Edition", "Ellsberg Paradox: Documented Ambiguity Aversion \u2014 Signature Edition", "Future: Documented-Probability Completeness Marker \u2014 Signature Edition"];
const CATEGORIES = ["combinatorics", "distributions", "documented-actuarial", "documented-games", "documented-lottery", "documented-quality", "documented-risk", "documented-statistics", "meta", "paradoxes", "quantum", "theorems"];
let seen = new Set(SEED_TITLES.map(t=>t.toLowerCase()));
let produced = 0n;
let s = 0xC0FFEE;
const rnd = () => { s = (s * 1103515245 + 12345) % 2147483648; return s / 2147483648; };

function ladderFor(n){ // progress through the ladder as output grows
  const f = Number(n) / 1e6;
  if (f < 1) return LADDER[0];
  if (f < 1e3) return LADDER[1];
  if (f < 1e6) return LADDER[2];
  if (f < 1e9) return LADDER[3];
  if (f < 1e12) return LADDER[4];
  if (f < 1e15) return LADDER[5];
  return LADDER[6];
}

function makeOne(i){
  const base = SEED_TITLES[Math.floor(rnd()*SEED_TITLES.length)];
  const cat = CATEGORIES[Math.floor(rnd()*CATEGORIES.length)];
  const variant = ["extended case","edge case","cross-domain mix","stress-test variant","minimal example"][(i%5)];
  const title = base.replace(/ \u2014 Signature Edition$/,"") + " — " + variant + " #" + (i+1);
  const key = title.toLowerCase();
  if (seen.has(key)) return null; // duplicate check: never emit a duplicate
  seen.add(key);
  return { id: "JAH-DPRBSG-" + String(i+1).padStart(6,"0"), slug: "documented-probabilities-signature", src: "generated",
    title, category: cat, generator_ladder_rank: ladderFor(produced),
    description: "Generator-produced " + variant + " in the '" + cat + "' family, derived from: " + base + ".",
    demo_code: "console.log(JSON.stringify({generator:'documented-probabilities-signature', variant:'" + variant + "', seed:'" + base + "'}));",
    provenance: "generated by the documented-probabilities-signature boundless generator", last_verified: "2026-10-21" };
}

// Completion detection: the template space here is finite (seed x category x variant).
function templateSpace(){ return BigInt(SEED_TITLES.length * CATEGORIES.length * 5); }

function generate(n, opts={}){
  n = Math.min(n, THROTTLE);
  const out = [];
  if (produced >= CAP) return { records: out, status: "capped", reason: "10^15 hard cap reached" };
  if (produced >= templateSpace())
    return { records: out, status: "complete", reason: "template space genuinely exhausted (" + templateSpace() + " combinations)" };
  for (let i=0; i<n && produced < CAP && produced < templateSpace(); i++){
    const r = makeOne(Number(produced));
    if (r){ out.push(r); produced++; }
  }
  return { records: out, produced: produced.toString(), cap: CAP.toString(),
           status: produced >= templateSpace() ? "complete" : "running" };
}

// Archive-aware AI: keyword lookup over the seed corpus (built records).
function ask(q){
  const words = q.toLowerCase().split(/[^a-z0-9]+/).filter(w=>w.length>2);
  const scored = SEED_TITLES.map(t=>{
    const tl = t.toLowerCase(); let sc = 0;
    for (const w of words) if (tl.includes(w)) sc++;
    return {title:t, score:sc};
  }).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,5);
  return { query:q, database:"documented-probabilities-signature", matches:scored,
           note: scored.length ? "Top matches from the archive; full records live in data/documented-probabilities-signature/index.jsonl.gz."
                               : "No match in this database's archive." };
}

if (require.main === module){
  const n = parseInt(process.argv[2]||"5",10);
  const res = generate(n);
  console.log(JSON.stringify({status:res.status, produced:res.produced, sample:res.records.slice(0,2).map(r=>r.title)}, null, 1));
}
module.exports = { generate, ask, CAP: CAP.toString(), LADDER, THROTTLE };
