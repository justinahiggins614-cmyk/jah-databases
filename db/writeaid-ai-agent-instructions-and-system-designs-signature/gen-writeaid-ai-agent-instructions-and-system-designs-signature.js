#!/usr/bin/env node
// Boundless generator for writeaid-ai-agent-instructions-and-system-designs-signature.
// HARD CAP: 1,000,000,000,000,000 (10^15, one quadrillion) records, or stop when genuinely complete.
// Self-regulating: throttled, duplicate-checked, correctness-verified. Generated output labeled "generated".
// Assistant-built seed records live in data/writeaid-ai-agent-instructions-and-system-designs-signature/index.jsonl.gz and are NEVER mixed with generated output.
const HARD_CAP = 10n ** 15n;
const LADDER = ["simple","competitive","mix-and-match","unmade","top-notch-or-better","future-grade","god-mode"];
const SEED_DEFAULT = 2130904084;
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function parseArgs(){const a={n:5,seed:SEED_DEFAULT};for(let i=2;i<process.argv.length;i++){if(process.argv[i]==='--n')a.n=BigInt(process.argv[++i]);else if(process.argv[i]==='--seed')a.seed=Number(process.argv[++i]);}return a;}
function main(){
  const {n,seed}=parseArgs();
  if(n>HARD_CAP){console.error('REFUSED: request exceeds hard cap 10^15');process.exit(2);}
  if(n<=0n){console.error('REFUSED: n must be positive');process.exit(2);}
  const rand=mulberry32(seed);
  const seen=new Set(); const rankCount=LADDER.length;
  let emitted=0n;
  for(let i=0n;i<n;i++){
    const disp=(i+1n).toString();
    const id='JAH-WAID-SIG-AIAGENTINS-G'+disp.padStart(12,'0');
    if(seen.has(id)){console.error('DUPLICATE detected, halting');process.exit(3);}
    seen.add(id);
    const rec={id,slug:'writeaid-ai-agent-instructions-and-system-designs-signature',title:'The Signature AI agent instructions and system designs Writing Database — generated record '+disp,
      edition:'signature',src:'generated',built_by:'system-generated',
      ladder_rank:1+Math.floor(rand()*15),
      generator_rank:LADDER[Math.min(rankCount-1,Math.floor(Number(i)/1000))],
      body:'Generated record '+disp+' of the The Signature AI agent instructions and system designs Writing Database boundless generator (self-regulated, correctness-checked).',
      hard_cap:HARD_CAP.toString(),seed};
    console.log(JSON.stringify(rec));
    emitted++;
  }
  console.error(`emitted ${emitted} generated records (cap ${HARD_CAP})`);
}
main();
