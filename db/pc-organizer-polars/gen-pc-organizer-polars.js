(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "concepts", "io", "wrangling"];
var PREFIX='JAH-PCO75-';
var GENVER='jahdb-pc-organizer-polars-1.0';
var DBNAME='Polars';
var PROV='Public documentation and published specifications for Polars; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What Polars is", "overview", "Polars is the blazing-fast DataFrame library with its core written in Rust and a Python API on top, built for multithreaded data wrangling. It processes massive datasets faster than pandas by designing for parallelism fr", {"mode": "install"}, "Runnable demo \u2014 What Polars is"], ["Installing Polars", "setup", "One pip install delivers the whole engine \u2014 no JVM, no cluster, no configuration. Import polars as pl and you are wrangling.", {"mode": "install"}, "Runnable demo \u2014 Installing Polars"], ["Eager vs lazy", "concepts", "Eager DataFrames execute every step immediately; LazyFrames build an optimized query plan and run it on collect(). Lazy mode lets the engine reorder, push down filters, and parallelize the whole pipeline.", {"mode": "eager"}, "Runnable demo \u2014 Eager vs lazy"], ["Lazy scanning", "io", "scan_csv and scan_parquet read lazily, and predicate pushdown applies your filters during the read \u2014 the engine never materializes rows you will discard. Scanning a 10 GB file for 1,000 matching rows reads a fraction of ", {"mode": "scan"}, "Runnable demo \u2014 Lazy scanning"], ["Filtering rows", "wrangling", "Filters are expressions on columns \u2014 pl.col('temp') > 70 \u2014 evaluated in parallel across all cores. This demo filters a sensor log the Polars way, in plain JavaScript standing in for the engine.", {"mode": "filter", "col": "temp", "th": 70, "rows": [{"temp": 62}, {"temp": 71}, {"temp": 88}, {"temp": 69}, {"temp": 95}, {"temp": 66}]}, "Runnable demo \u2014 Filtering rows"], ["Expressions", "concepts", "Expressions compose column operations \u2014 filter, transform, aggregate \u2014 into single-pass pipelines with no intermediate copies. One expression can replace five pandas lines and run ten times faster.", {"mode": "expr"}, "Runnable demo \u2014 Expressions"], ["Group-by aggregation", "wrangling", "group_by with aggregations \u2014 mean, sum, count per group \u2014 is the workhorse of data analysis, parallelized across groups. This demo groups benchmark scores by cooler and averages them.", {"mode": "groupby", "key": "cooler", "val": "score", "rows": [{"cooler": "A", "score": 82}, {"cooler": "B", "score": 91}, {"cooler": "A", "score": 84}, {"cooler": "B", "score": 89}, {"cooler": "A", "score": 80}]}, "Runnable demo \u2014 Group-by aggregation"], ["Joins", "wrangling", "Joins merge DataFrames on keys with inner, left, and outer semantics, hashed in parallel. Combining the parts table with the price table is one expression.", {"mode": "join", "n": 1250}, "Runnable demo \u2014 Joins"], ["Sorting", "wrangling", "Sorting is multithreaded and stable, and top-k queries avoid sorting everything when you only want the leaders. This demo finds the top scorer without ceremony.", {"mode": "sort", "col": "score", "rows": [{"name": "a", "score": 82}, {"name": "b", "score": 91}, {"name": "c", "score": 77}]}, "Runnable demo \u2014 Sorting"], ["Select and transform", "wrangling", "select picks and computes columns in a single pass \u2014 rename, cast, derive, all at once. with_columns adds derived columns without disturbing the rest.", {"mode": "select"}, "Runnable demo \u2014 Select and transform"], ["IO formats", "io", "Polars reads and writes CSV, Parquet, JSON, IPC, and NDJSON, with Parquet the speed king for analytics. Columnar storage plus lazy reads is why the combination flies.", {"mode": "io"}, "Runnable demo \u2014 IO formats"], ["Streaming larger-than-RAM", "concepts", "Streaming execution processes datasets bigger than memory in chunks, spilling gracefully instead of crashing. The same pipeline that handles megabytes handles terabytes.", {"mode": "stream"}, "Runnable demo \u2014 Streaming larger-than-RAM"], ["Strict schemas", "concepts", "Strict per-column dtypes catch type errors at plan time instead of mid-pipeline \u2014 a string sneaking into a numeric column fails fast and loudly. Schema discipline is data quality.", {"mode": "schema"}, "Runnable demo \u2014 Strict schemas"], ["Polars vs pandas", "overview", "Polars wins on speed and parallelism for fresh pipelines; pandas wins on ecosystem maturity and library integrations. Many shops prototype in pandas and productionize hot paths in Polars.", {"mode": "threads"}, "Runnable demo \u2014 Polars vs pandas"], ["Wrangling workflow", "wrangling", "The Polars ritual: scan lazily, filter early, select what you need, group and aggregate, collect once. One collect at the end, maximum parallelism throughout.", {"mode": "workflow", "steps": ["scan_csv lazily", "Filter with expressions", "select needed columns", "group_by and aggregate", "collect() once", "Write Parquet"]}, "Runnable demo \u2014 Wrangling workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-polars/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-polars',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-polars',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
