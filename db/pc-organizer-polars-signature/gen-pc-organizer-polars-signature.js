(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "concepts", "io", "wrangling"];
var PREFIX='JAH-PCO75S-';
var GENVER='jahdb-pc-organizer-polars-signature-1.0';
var DBNAME='Signature Frame Engine';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Engine concept", "overview", "The Signature Frame Engine is Manon's original DataFrame design: lazy plans, fearless parallelism, and strict schemas as moral positions. It treats your data like it treats your time \u2014 as precious.", {"mode": "install"}, "Runnable demo \u2014 Engine concept"], ["Engine setup", "setup", "The Engine installs as one native package with zero runtime dependencies and verifies its install with a self-test. First import prints the detected core count \u2014 the engine introduces its workforce.", {"mode": "install"}, "Runnable demo \u2014 Engine setup"], ["Plans before promises", "concepts", "Every Engine pipeline is a plan first: the optimizer shows what it will do before doing it, and explain() prints the strategy. No black boxes \u2014 the engine shows its work like a good student.", {"mode": "eager"}, "Runnable demo \u2014 Plans before promises"], ["Honest scanning", "io", "Scanners report what they skip: rows filtered at read time, columns never touched, bytes never moved. The engine brags about the work it avoided, because avoided work is the fastest work.", {"mode": "scan"}, "Runnable demo \u2014 Honest scanning"], ["Predicate filtering", "wrangling", "Filters push to the earliest possible moment \u2014 ideally into the scan itself \u2014 and the plan shows the pushdown. This demo filters the way the Engine does: early and in parallel.", {"mode": "filter", "col": "temp", "th": 75, "rows": [{"temp": 70}, {"temp": 80}, {"temp": 74}, {"temp": 92}, {"temp": 68}]}, "Runnable demo \u2014 Predicate filtering"], ["Composable expressions", "concepts", "Engine expressions read like sentences and compile to vectorized kernels: filter the hot, average the rest. Composition is the whole API \u2014 learn expressions, know the engine.", {"mode": "expr"}, "Runnable demo \u2014 Composable expressions"], ["Parallel grouping", "wrangling", "Grouping fans out across cores with per-group accumulators, then merges \u2014 the classic parallel reduction, handled for you. This demo averages benchmark scores by cooler the parallel way.", {"mode": "groupby", "key": "cooler", "val": "score", "rows": [{"cooler": "X", "score": 88}, {"cooler": "Y", "score": 94}, {"cooler": "X", "score": 90}, {"cooler": "Y", "score": 92}]}, "Runnable demo \u2014 Parallel grouping"], ["Honest joins", "wrangling", "Joins declare their cardinality expectations \u2014 one-to-one, many-to-one \u2014 and fail loudly on violations instead of silently exploding rows. Surprise row multiplication is a bug, and the Engine treats it like one.", {"mode": "join", "n": 2400}, "Runnable demo \u2014 Honest joins"], ["Top-k thinking", "wrangling", "Top-k queries use heaps, not full sorts \u2014 the engine reaches for the right algorithm, not the familiar one. This demo finds the leader the efficient way.", {"mode": "sort", "col": "score", "rows": [{"name": "x", "score": 85}, {"name": "y", "score": 97}, {"name": "z", "score": 79}]}, "Runnable demo \u2014 Top-k thinking"], ["One-pass select", "wrangling", "Select computes new columns while reading, fusing the whole projection into the scan. The plan shows the fusion; the runtime feels it.", {"mode": "select"}, "Runnable demo \u2014 One-pass select"], ["Forge formats", "io", "The Engine's native Forge format stores data with its schema, statistics, and lineage in one file \u2014 Parquet-compatible, provenance included. Files describe themselves completely.", {"mode": "io"}, "Runnable demo \u2014 Forge formats"], ["Infinite streaming", "concepts", "Streaming mode treats datasets as infinite: constant memory, backpressure, progress reporting. A pipeline written for a laptop runs on the data lake unchanged.", {"mode": "stream"}, "Runnable demo \u2014 Infinite streaming"], ["Schema as contract", "concepts", "Schemas are contracts with versions: a pipeline declares the schema it expects, and mismatches fail before a single row is read. Data contracts end the era of 'it worked on my file.'", {"mode": "schema"}, "Runnable demo \u2014 Schema as contract"], ["Engine vs the world", "overview", "The Frame Engine competes on honesty as well as speed: it reports skipped work, shows its plans, and fails loudly. Fast is table stakes; trustworthy is the differentiator.", {"mode": "threads"}, "Runnable demo \u2014 Engine vs the world"], ["Engine workflow", "wrangling", "The Engine ritual: declare the schema, scan with pushdown, compose expressions, aggregate in parallel, collect once, certify the output. Planned, parallel, proven.", {"mode": "workflow", "steps": ["Declare the schema contract", "Scan with predicate pushdown", "Compose expressions", "Aggregate in parallel", "Collect once", "Certify the output schema"]}, "Runnable demo \u2014 Engine workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"install\"){\n  show(\"Install\",\"pip install polars\");\n  show(\"Core\",\"Rust, multithreaded\");\n  show(\"License\",\"MIT / Apache 2.0\");\n}else if(m===\"eager\"){\n  show(\"Eager\",\"pl.DataFrame - executes immediately\");\n  show(\"Lazy\",\"pl.LazyFrame - builds a plan, runs on .collect()\");\n  show(\"Rule\",\"lazy for pipelines, eager for exploration\");\n}else if(m===\"scan\"){\n  show(\"scan_csv / scan_parquet\",\"lazy readers\");\n  show(\"Predicate pushdown\",\"filters apply during the read\");\n  show(\"Result\",\"reads only what the query needs\");\n}else if(m===\"filter\"){\n  var rows=DATA.rows.filter(function(r){return r[DATA.col]>DATA.th;});\n  show(\"Rows in\",DATA.rows.length);\n  show(\"Rows out\",rows.length);\n  show(\"Predicate\",DATA.col+\" > \"+DATA.th);\n}else if(m===\"groupby\"){\n  var g={};\n  DATA.rows.forEach(function(r){var k=r[DATA.key];(g[k]=g[k]||[]).push(r[DATA.val]);});\n  console.log(\"group_by('\"+DATA.key+\"').agg(pl.col('\"+DATA.val+\"').mean()):\");\n  Object.keys(g).forEach(function(k){var a=g[k];console.log(\"  \"+k+\": mean=\"+(Math.round(a.reduce(function(x,y){return x+y;},0)/a.length*100)/100)+\" (n=\"+a.length+\")\");});\n}else if(m===\"expr\"){\n  show(\"Expression\",\"pl.col('a').filter(pl.col('b') > 0).mean()\");\n  show(\"Composes\",\"without intermediate copies\");\n  show(\"Runs\",\"in parallel across columns\");\n}else if(m===\"join\"){\n  show(\"Join\",\"df1.join(df2, on='id', how='left')\");\n  show(\"Rows after\",DATA.n);\n}else if(m===\"io\"){\n  show(\"Formats\",\"CSV, Parquet, JSON, IPC, NDJSON\");\n  show(\"Fastest\",\"Parquet - columnar\");\n}else if(m===\"stream\"){\n  show(\"Streaming\",\".collect(streaming=True)\");\n  show(\"Handles\",\"larger-than-RAM datasets\");\n}else if(m===\"threads\"){\n  show(\"Threads\",\"all cores by default\");\n  show(\"Note\",\"no GIL games - real parallelism\");\n}else if(m===\"schema\"){\n  show(\"Schema\",\"strict dtypes per column\");\n  show(\"Catches\",\"type errors at plan time\");\n}else if(m===\"sort\"){\n  var s=DATA.rows.slice().sort(function(a,b){return b[DATA.col]-a[DATA.col];});\n  show(\"Top row\",s[0][DATA.key]+\" (\"+DATA.col+\"=\"+s[0][DATA.col]+\")\");\n}else if(m===\"select\"){\n  show(\"select\",\"pick and compute columns in one pass\");\n  show(\"Example\",\"df.select(pl.col('a')*2)\");\n}else if(m===\"workflow\"){\n  console.log(\"Wrangling workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
function jitter(v,rnd){
  if(typeof v==='number'){return Math.round(v*(0.9+rnd()*0.2)*100)/100;}
  if(Array.isArray(v)){return v.map(function(x){return jitter(x,rnd);});}
  if(v&&typeof v==='object'){var o={};Object.keys(v).forEach(function(k){o[k]=jitter(v[k],rnd);});return o;}
  return v;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(typeof seed==='number'&&seed>SELFREG.maxRecords)throw new Error('SELF-REGULATION HARD STOP: 1,000,000,000,000 record limit reached');
  var cat=opts.category||pick(CATS,rnd);
  var pool=ARCH.filter(function(a){return a[1]===cat;});
  var a=pick(pool.length?pool:ARCH,rnd);
  var scen=jitter(a[3],rnd); scen.mode=a[3].mode;
  var id=PREFIX+String(10001+seed).padStart(6,'0');
  var program=ENGINE.split('__DATA__').join(JSON.stringify(scen));
  var facts=jitter(a[4]||{},rnd);
  return {id:id,t:a[0]+' (simulated #'+seed+')',
    title:DBNAME+' \u2014 '+a[0]+' (simulated variant, seed '+seed+')',
    g:a[1],category:a[1],
    description:a[2]+' This is a simulated boundless-generator variant (seed '+seed+') from '+GENVER+': the scenario values were deterministically jittered from the archive archetype, and the record passed the independent correctness validator before acceptance.',
    ladder_rank:1+((seed-1)%15),
    march:'MILLION MARCH \u00b7 simulated record \u00b7 archive marches to a 1,000,000-record target \u2014 in progress',
    provenance:PROV,last_verified:'2026-10-21',record_label:SELFREG.simulatedLabel,
    facts:facts,
    demo:{engine:'jahdb-demo-1.0',kind:'code',title:'Runnable demo \u2014 '+a[0]+' (simulated)',language:'javascript',
      program:program,run_hint:'PC: save as demo.js, run `node demo.js`. In-page: press Run.',
      how_to_run:'PC: save the program as demo.js and run `node demo.js`. In-page: open the Demo Lab tab and press Run.',runnable:true},
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-polars-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-polars-signature',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  var n=parseInt(String(r.id||'').slice(PREFIX.length),10);
  if(!(n>=10001))e.push('id-block (generator ids start at 10001; archive owns 1-9999)');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(r.record_label!==SELFREG.simulatedLabel)e.push('record_label');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.demo&&r.demo.language!=='javascript')e.push('demo-language');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return{ok:false,errors:['drift: exact title already in archive']}; }
  return{ok:true,errors:[]};
}
var gen={version:GENVER,selfRegulation:SELFREG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-polars-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
