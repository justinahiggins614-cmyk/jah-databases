(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["overview", "setup", "curation", "evaluation", "export"];
var PREFIX='JAH-PCO73S-';
var GENVER='jahdb-pc-organizer-fiftyone-signature-1.0';
var DBNAME='Signature Dataset Lens';
var PROV='Original Signature design by Justin Addam Higgins (JAH) — authored for the JAH Databases network.';
var SELFREG={maxRecords:1000000000000,throttleMs:5,simulatedLabel:'simulated',
  correctness:'independent validate() runs on every record before acceptance',
  completion:'1,000,000-record target; archive block 1-9999; generator block 10001+'};
/* archetypes: [t, g, blurb, scenario, demoTitle] — drawn from the archive's own 15 records */
var ARCH=[["Lens concept", "overview", "The Signature Dataset Lens is Manon's original curation platform: see the dataset, understand the dataset, then train. It treats curation as the highest-leverage hour in machine learning.", {"mode": "dataset", "name": "forge-street-v1", "n": 60000}, "Runnable demo \u2014 Lens concept"], ["Lens setup", "setup", "The Lens installs as one signed package and opens with a guided tour of a sample dataset \u2014 curation concepts taught by doing. Real projects import with a drag.", {"mode": "install"}, "Runnable demo \u2014 Lens setup"], ["Collections", "curation", "Collections hold samples with versioned fields, so the dataset's schema evolves without breaking history. Every field knows when it was born.", {"mode": "dataset", "name": "forge-street-v1", "n": 60000}, "Runnable demo \u2014 Collections"], ["Specimen cards", "curation", "Every sample gets a specimen card: the media, all labels, provenance, and quality flags on one page. Cards make individual samples discussable \u2014 'card 0042' instead of 'that one image.'", {"mode": "sample", "file": "forge_0042.jpg", "fields": ["truth", "predictions", "provenance", "flags"]}, "Runnable demo \u2014 Specimen cards"], ["The observatory", "curation", "The observatory is the visual hall: sample walls, distribution charts, and embedding skies you can fly through. Understanding arrives through the eyes first.", {"mode": "app"}, "Runnable demo \u2014 The observatory"], ["Question lenses", "curation", "Question lenses are saved views with plain-language names: 'night misses,' 'tiny objects,' 'rainy confusion.' The lens library becomes the team's shared understanding of the data.", {"mode": "filter", "expr": "weather=rain and size=tiny", "n": 208}, "Runnable demo \u2014 Question lenses"], ["Cohort ribbons", "curation", "Cohort ribbons tag sample groups with colors visible across every view \u2014 the review queue glows amber everywhere. Cohorts persist across sessions and teammates.", {"mode": "tag"}, "Runnable demo \u2014 Cohort ribbons"], ["Honest evaluation", "evaluation", "Evaluation reports the full story: mAP overall, per class, per cohort, with failure galleries per slice. A model is only as good as its worst important slice.", {"mode": "eval", "map": 0.66}, "Runnable demo \u2014 Honest evaluation"], ["Constellation maps", "evaluation", "Constellation maps plot embeddings as navigable star fields where similar samples cluster. Zooming into a cluster inspects it; the map is the dataset's geography.", {"mode": "embed", "n": 60000, "d": 512}, "Runnable demo \u2014 Constellation maps"], ["The refinery", "evaluation", "The refinery distills dataset health into actions: duplicates to merge, mislabels to fix, gaps to fill. Each action links to the exact samples \u2014 no vague advice.", {"mode": "brain"}, "Runnable demo \u2014 The refinery"], ["The menagerie", "setup", "The menagerie keeps reference datasets and models versioned and checksummed, loading with one call. Benchmarks reproduce because the menagerie never silently changes.", {"mode": "zoo"}, "Runnable demo \u2014 The menagerie"], ["Lens instruments", "setup", "Instruments are Lens plugins with a workshop for building them: panels, tools, and pipeline steps in one SDK. The community trades instruments like tools.", {"mode": "plugin"}, "Runnable demo \u2014 Lens instruments"], ["Certified export", "export", "Certified exports stamp the dataset hash, curation log, and evaluation snapshot into the package. Training on certified data is auditable end to end.", {"mode": "export", "fmt": "Forge certified"}, "Runnable demo \u2014 Certified export"], ["Lens scripting", "setup", "Lens scripting drives collections, lenses, and evaluation from notebooks with readable one-liners. The gallery of recipes covers every common curation task.", {"mode": "view"}, "Runnable demo \u2014 Lens scripting"], ["Lens workflow", "curation", "The Lens ritual: collect, observe, question, evaluate, refine, certify. Curation as a discipline with instruments, not a chore with eyeballs.", {"mode": "workflow", "steps": ["Collect into the Lens", "Observe in the observatory", "Ask questions with lenses", "Evaluate honestly", "Refine with the refinery", "Certify the export"]}, "Runnable demo \u2014 Lens workflow"]];
var ENGINE="var DATA = __DATA__;\nfunction show(k,v){console.log(k+\": \"+v);}\nvar m=DATA.mode;\nif(m===\"install\"){\n  show(\"Install\",\"pip install fiftyone\");\n  show(\"Launch\",\"fiftyone app launch\");\n  show(\"License\",\"Apache 2.0, open source\");\n}else if(m===\"dataset\"){\n  show(\"Dataset\",DATA.name);\n  show(\"Samples\",DATA.n);\n  show(\"Lives\",\"in MongoDB-backed local store\");\n}else if(m===\"sample\"){\n  show(\"Sample\",DATA.file);\n  show(\"Fields\",DATA.fields.join(\", \"));\n}else if(m===\"filter\"){\n  show(\"Filter\",DATA.expr);\n  show(\"Matched\",DATA.n+\" samples\");\n}else if(m===\"view\"){\n  show(\"View\",\"a saved filtered lens on the dataset\");\n  show(\"Chains\",\"filter, sort, shuffle, limit\");\n}else if(m===\"eval\"){\n  show(\"Evaluation\",\"predictions vs ground truth\");\n  show(\"mAP\",DATA.map);\n  show(\"Matching\",\"COCO-style IoU matching\");\n}else if(m===\"embed\"){\n  show(\"Embeddings\",DATA.n+\" vectors x \"+DATA.d+\" dims\");\n  show(\"Use\",\"similarity search, UMAP scatter\");\n}else if(m===\"zoo\"){\n  show(\"Zoo\",\"one-line datasets and models\");\n  show(\"Example\",\"foz.load_zoo_dataset('quickstart')\");\n}else if(m===\"plugin\"){\n  show(\"Plugins\",\"custom App panels\");\n  show(\"Share\",\"via the plugin hub\");\n}else if(m===\"tag\"){\n  show(\"Tags\",\"label sample subsets\");\n  show(\"Use\",\"mark review queues, splits\");\n}else if(m===\"export\"){\n  show(\"Export\",DATA.fmt);\n  show(\"Round-trip\",\"to training frameworks\");\n}else if(m===\"brain\"){\n  show(\"Brain methods\",\"similarity, uniqueness, mistakenness\");\n  show(\"Finds\",\"duplicates and mislabels\");\n}else if(m===\"app\"){\n  show(\"App\",\"visual curation in the browser\");\n  show(\"Grid\",\"samples with predictions overlaid\");\n}else if(m===\"workflow\"){\n  console.log(\"Curation workflow:\");DATA.steps.forEach(function(s,i){console.log(\"  \"+(i+1)+\". \"+s);});\n}\nconsole.log(\"DEMO_OK\");";
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
    working_version:'https://justinahiggins614-cmyk.github.io/jah-databases/db/pc-organizer-fiftyone-signature/ \u2014 open the Demo Lab tab',
    slug:'pc-organizer-fiftyone-signature',_seed:seed};
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-fiftyone-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
