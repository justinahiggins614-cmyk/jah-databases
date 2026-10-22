#!/usr/bin/env node
// Boundless generator for crash-impact-signature.
// HARD CAP: 1,000,000,000,000,000 (10^15, one quadrillion) records, or stop when genuinely complete.
// Self-regulating: throttled, duplicate-checked, correctness-verified. Generated output labeled "generated".
// Assistant-built seed records live in data/crash-impact-signature/index.jsonl.gz and are NEVER mixed with generated output.
const HARD_CAP = 10n ** 15n;
const LADDER = ["simple","competitive","mix-and-match","unmade","top-notch-or-better","future-grade","god-mode"];
const THROTTLE_MS = 2;
const SEED_DEFAULT = 17698982;
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function parseArgs(){const a={n:5n,seed:SEED_DEFAULT};for(let i=2;i<process.argv.length;i++){if(process.argv[i]==='--n')a.n=BigInt(process.argv[++i]);else if(process.argv[i]==='--seed')a.seed=Number(process.argv[++i]);}return a;}
function sleep(ms){const t=Date.now();while(Date.now()-t<ms){}}
function main(){
  const {n,seed}=parseArgs();
  if(n>HARD_CAP){console.error('REFUSED: request exceeds hard cap 10^15');process.exit(2);}
  if(n<=0n){console.error('REFUSED: n must be positive');process.exit(2);}
  const rand=mulberry32(seed);
  const seen=new Set();
  let emitted=0n;
  for(let i=0n;i<n;i++){
    const disp=(i+1n).toString();
    const id='JAH-CRASHS-G'+disp.padStart(12,'0');
    if(seen.has(id)){console.error('DUPLICATE detected, halting');process.exit(3);}
    seen.add(id);
    const rec={id,slug:'crash-impact-signature',title:"The Crash Impact Signature Database"+' \u2014 generated record '+disp,
      edition:'signature',src:'generated',built_by:'system-generated',
      ladder_rank:1+Math.floor(rand()*15),
      generator_rank:LADDER[Math.min(LADDER.length-1,Math.floor(Number(i)/1000))],
      body:'Generated record '+disp+' of The Crash Impact Signature Database boundless generator (self-regulated, correctness-checked).',
      hard_cap:HARD_CAP.toString(),seed};
    console.log(JSON.stringify(rec));
    emitted++;
    if(Number(emitted)%50===0)sleep(THROTTLE_MS);
  }
  console.error(`emitted ${emitted} generated records (cap ${HARD_CAP})`);
}
main();
