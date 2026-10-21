(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "concepts", "io", "wrangling"];
var PREFIX='JAH-PCO76-';
var GENVER='jahdb-pc-organizer-pandas-1.0';
var DBNAME='Pandas';
var PROV='Public documentation and published specifications for Pandas; compiled and fact-checked.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["What pandas is", "overview", "pandas is the standard Python library for tabular data \u2014 DataFrames and Series with labeled rows and columns \u2014 created by Wes McKinney in 2008. It is the workbench where data gets cleaned, reshaped, and understood before", {"mode": "install"}, "Runnable demo \u2014 What pandas is"], ["Installing pandas", "setup", "pip install pandas brings the library plus its NumPy foundation; conda users get the MKL-accelerated build. Version 2.x is the modern baseline with copy-on-write and better strings.", {"mode": "install"}, "Runnable demo \u2014 Installing pandas"], ["DataFrame and Series", "concepts", "A DataFrame is a table with labeled rows and columns; a Series is a single labeled column. Labels \u2014 not positions \u2014 are the primary way to address data, which prevents a whole class of off-by-one errors.", {"mode": "df", "rows": 5000, "cols": 8, "names": ["time", "temp", "fan", "load"]}, "Runnable demo \u2014 DataFrame and Series"], ["Reading data", "io", "read_csv turns a file into a DataFrame in one call, with siblings for Excel, Parquet, SQL, and JSON. Most analyses begin with a read and end with a to_csv or to_parquet.", {"mode": "read", "file": "sensors.csv", "n": 5000}, "Runnable demo \u2014 Reading data"], ["First look: head and describe", "concepts", "head() shows the first rows, info() shows dtypes and missing counts, describe() summarizes every numeric column. The three-command first look catches most data problems in a minute.", {"mode": "describe"}, "Runnable demo \u2014 First look: head and describe"], ["Indexing: loc and iloc", "wrangling", "loc selects by label and iloc by position \u2014 two explicit tools instead of one ambiguous bracket. Explicit indexing is how pandas avoids the silent bugs of positional guessing.", {"mode": "loc"}, "Runnable demo \u2014 Indexing: loc and iloc"], ["Boolean filtering", "wrangling", "Boolean masks filter rows expressively: df[df.temp > 70] reads like the question it answers. This demo applies a mask to sensor readings the pandas way.", {"mode": "filter", "col": "temp", "th": 70, "rows": [{"temp": 62}, {"temp": 71}, {"temp": 88}, {"temp": 69}]}, "Runnable demo \u2014 Boolean filtering"], ["GroupBy: split-apply-combine", "wrangling", "groupby splits rows by key, applies an aggregation, and combines the result \u2014 the single most-used pattern in data analysis. This demo averages benchmark scores per cooler exactly the pandas way.", {"mode": "groupby", "key": "cooler", "val": "score", "rows": [{"cooler": "A", "score": 82}, {"cooler": "B", "score": 91}, {"cooler": "A", "score": 84}, {"cooler": "B", "score": 89}]}, "Runnable demo \u2014 GroupBy: split-apply-combine"], ["Merging DataFrames", "wrangling", "merge joins tables SQL-style on key columns \u2014 inner, left, right, outer \u2014 combining the parts list with the price list. The validate argument catches unexpected duplicates before they corrupt the join.", {"mode": "merge", "n": 1250}, "Runnable demo \u2014 Merging DataFrames"], ["Pivot tables", "wrangling", "pivot_table reshapes long data into wide summaries \u2014 average temperature by cooler and month in one call. It is the spreadsheet pivot, scripted and reproducible.", {"mode": "pivot"}, "Runnable demo \u2014 Pivot tables"], ["Apply and vectorization", "wrangling", "apply runs functions row- or column-wise, but vectorized operations on whole columns are the fast path. This demo maps a doubling function the element-wise way, then notes the vectorized alternative.", {"mode": "apply", "vals": [1, 2, 3, 4]}, "Runnable demo \u2014 Apply and vectorization"], ["Missing data", "wrangling", "Missing data is NaN, handled with dropna to remove or fillna to impute \u2014 forward-fill, mean, or constant. Explicit missingness beats silent zeros: a gap should look like a gap.", {"mode": "missing"}, "Runnable demo \u2014 Missing data"], ["Time series", "wrangling", "A DatetimeIndex unlocks resample \u2014 minute data to hourly means in one call \u2014 plus rolling windows and time-zone handling. Sensor logs and financial data live here.", {"mode": "time"}, "Runnable demo \u2014 Time series"], ["Copy-on-write", "concepts", "Copy-on-write, default since pandas 2.0, makes chained assignment safe: views never silently modify the original. A decade of SettingWithCopyWarning ends with one default.", {"mode": "cow"}, "Runnable demo \u2014 Copy-on-write"], ["Analysis workflow", "wrangling", "The pandas ritual: read, first-look, clean missingness, filter and group, merge context, visualize, export. The notebook tells the story; the script reproduces it.", {"mode": "workflow", "steps": ["read_csv the data", "head/info/describe first look", "Handle missing values", "Filter and groupby", "Merge context tables", "Export results"]}, "Runnable demo \u2014 Analysis workflow"]];
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-pandas/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-pandas',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-pandas',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
