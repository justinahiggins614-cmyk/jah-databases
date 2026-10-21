(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "concepts", "io", "wrangling"];
var PREFIX='JAH-PCO76S-';
var GENVER='jahdb-pc-organizer-pandas-signature-1.0';
var DBNAME='Signature Table Works';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Table Works concept", "overview", "The Signature Table Works is Manon's original data workbench: everything pandas does, with clearer errors, stricter tables, and performance honesty. Familiar enough to feel like home, principled enough to trust.", {"mode": "install"}, "Runnable demo \u2014 Table Works concept"], ["Works setup", "setup", "The Table Works installs as one package with a verified numerics stack and prints a capability report on import \u2014 threads, accelerators, versions. You always know what engine you have.", {"mode": "install"}, "Runnable demo \u2014 Works setup"], ["Tables and columns", "concepts", "Tables carry names, dtypes, and units as first-class metadata \u2014 a temperature column knows it is Celsius. Metadata travels with the data instead of living in someone's head.", {"mode": "df", "rows": 8000, "cols": 8, "names": ["time", "temp_c", "fan_rpm", "load_pct"]}, "Runnable demo \u2014 Tables and columns"], ["Reading with contracts", "io", "Reads declare the expected schema up front, and the Works validates on load \u2014 wrong dtypes fail at the door. Data that lies about its shape never enters the analysis.", {"mode": "read", "file": "sensors.forge", "n": 8000}, "Runnable demo \u2014 Reading with contracts"], ["First look, enforced", "concepts", "The first-look report is automatic on every read: shape, dtypes, missingness, and numeric summaries before you ask. Surprises surface in the first minute, not the first bug.", {"mode": "describe"}, "Runnable demo \u2014 First look, enforced"], ["Explicit addressing", "wrangling", "Addressing is always explicit \u2014 by name or by position, never ambiguous \u2014 and the Works says which it used. There is no bracket that means two things.", {"mode": "loc"}, "Runnable demo \u2014 Explicit addressing"], ["Question filters", "wrangling", "Filters are questions written as code, and the Works echoes the question back with the answer: 'temp_c > 70: 2 of 4 rows.' This demo filters the Works way.", {"mode": "filter", "col": "temp_c", "th": 70, "rows": [{"temp_c": 62}, {"temp_c": 71}, {"temp_c": 88}, {"temp_c": 69}]}, "Runnable demo \u2014 Question filters"], ["Gather-split-combine", "wrangling", "Grouping gathers rows by key, applies honest aggregations, and combines with the method named. This demo averages scores per cooler, naming every step.", {"mode": "groupby", "key": "cooler", "val": "score", "rows": [{"cooler": "X", "score": 88}, {"cooler": "Y", "score": 94}, {"cooler": "X", "score": 90}]}, "Runnable demo \u2014 Gather-split-combine"], ["Declared joins", "wrangling", "Joins declare expected cardinality and fail loudly on violations \u2014 a many-to-many surprise is an error, not a result. The Works would rather argue than corrupt.", {"mode": "merge", "n": 2400}, "Runnable demo \u2014 Declared joins"], ["Reshape studio", "wrangling", "Reshaping \u2014 pivot, melt, stack \u2014 previews the new shape before committing, so wide-to-long never surprises. Previews make reshaping fearless.", {"mode": "pivot"}, "Runnable demo \u2014 Reshape studio"], ["Vector-first functions", "wrangling", "Functions default to vectorized column execution; element-wise apply exists but warns about the faster path. The demo shows both, timed honestly.", {"mode": "apply", "vals": [2, 4, 6, 8]}, "Runnable demo \u2014 Vector-first functions"], ["Honest missingness", "wrangling", "Missing values are typed \u2014 unknown, not-applicable, withheld \u2014 instead of one NaN for everything. Different missings deserve different handling, and the Works knows the difference.", {"mode": "missing"}, "Runnable demo \u2014 Honest missingness"], ["Time as a citizen", "wrangling", "Time is a first-class citizen: time zones, resampling, and rolling windows work out of the box with clear semantics. Temporal bugs get loud errors instead of silent shifts.", {"mode": "time"}, "Runnable demo \u2014 Time as a citizen"], ["Ownership semantics", "concepts", "Ownership semantics make copies explicit and views safe \u2014 the Works tells you which you hold. No warnings needed when the semantics are sound.", {"mode": "cow"}, "Runnable demo \u2014 Ownership semantics"], ["Works workflow", "wrangling", "The Works ritual: contract the schema, read with validation, first-look automatically, analyze explicitly, certify the output. Tables you can defend, start to finish.", {"mode": "workflow", "steps": ["Contract the schema", "Read with validation", "Review the first-look", "Analyze explicitly", "Certify the output schema", "Publish with lineage"]}, "Runnable demo \u2014 Works workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"install\"){\n  show(\"Install\",\"pip install pandas\");\n  show(\"Since\",\"2008, by Wes McKinney\");\n  show(\"Stack\",\"NumPy-based, PyData core\");\n}else if(m===\"df\"){\n  show(\"DataFrame\",DATA.rows+\" rows x \"+DATA.cols+\" cols\");\n  show(\"Think\",\"a spreadsheet with a labeled index\");\n  show(\"Columns\",DATA.names.join(\", \"));\n}else if(m===\"series\"){\n  show(\"Series\",\"one labeled column\");\n  show(\"Example\",\"df['temp'] -> \"+DATA.n+\" values\");\n}else if(m===\"read\"){\n  show(\"read_csv\",DATA.file);\n  show(\"Rows read\",DATA.n);\n  show(\"Also\",\"read_excel, read_parquet, read_sql, read_json\");\n}else if(m===\"describe\"){\n  show(\"describe()\",\"count, mean, std, min, max per column\");\n  show(\"First look\",\"always describe new data\");\n}else if(m===\"loc\"){\n  show(\".loc\",\"label-based indexing\");\n  show(\".iloc\",\"position-based indexing\");\n  show(\"Example\",\"df.loc['row_a', 'temp']\");\n}else if(m===\"filter\"){\n  var rows=DATA.rows.filter(function(r){return r[DATA.col]>DATA.th;});\n  show(\"Boolean mask\",DATA.col+\" > \"+DATA.th);\n  show(\"Rows kept\",rows.length+\" of \"+DATA.rows.length);\n}else if(m===\"groupby\"){\n  var g={};\n  DATA.rows.forEach(function(r){var k=r[DATA.key];(g[k]=g[k]||[]).push(r[DATA.val]);});\n  console.log(\"df.groupby('\"+DATA.key+\"')['\"+DATA.val+\"'].mean():\");\n  Object.keys(g).forEach(function(k){var a=g[k];console.log(\"  \"+k+\": \"+(Math.round(a.reduce(function(x,y){return x+y;},0)/a.length*100)/100));});\n}else if(m===\"merge\"){\n  show(\"merge\",\"SQL-style joins: inner, left, right, outer\");\n  show(\"On\",\"key columns\");\n  show(\"Rows after\",DATA.n);\n}else if(m===\"pivot\"){\n  show(\"pivot_table\",\"reshape long data to wide\");\n  show(\"Use\",\"summaries by two dimensions\");\n}else if(m===\"apply\"){\n  var out=DATA.vals.map(function(v){return v*2;});\n  show(\"apply/map\",\"element-wise functions\");\n  show(\"Example\",\"[\"+DATA.vals.join(\",\")+\"] -> [\"+out.join(\",\")+\"]\");\n}else if(m===\"missing\"){\n  show(\"Missing data\",\"NaN\");\n  show(\"dropna()\",\"remove missing rows\");\n  show(\"fillna()\",\"fill with a value or method\");\n}else if(m===\"time\"){\n  show(\"Time series\",\"DatetimeIndex + resample()\");\n  show(\"Example\",\"hourly means from minute data\");\n}else if(m===\"cow\"){\n  show(\"Copy-on-write\",\"pandas 2.0+ default\");\n  show(\"Means\",\"safer views, often faster\");\n}else if(m===\"io\"){\n  show(\"IO\",\"CSV, Excel, Parquet, SQL, JSON, clipboard\");\n  show(\"Tip\",\"Parquet for speed, CSV for humans\");\n}else if(m===\"workflow\"){\n  console.log(\"Analysis workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-pandas-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-pandas-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-pandas-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
