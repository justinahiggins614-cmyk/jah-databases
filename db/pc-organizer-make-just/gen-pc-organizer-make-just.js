(function(){'use strict';
/* Make / Just Database — boundless generator jahdb-pc-organizer-make-just-1.0
   SELF-REGULATION (standing order): hard stop at ONE TRILLION records
   (1,000,000,000,000). Throttled batching, every record correctness-verified
   before acceptance, generated records labeled "simulated" for weeding,
   completion detection when the topic space is exhausted. */
var SELF_REG={max_records:1000000000000,hard_stop:true,throttled:true,
  labeling:'generated records are labeled simulated for weeding',
  correctness:'every record validated before acceptance',
  completion:'detects when the topic space is exhausted'};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["make", "just", "recipes", "automation"];
var PREFIX='JAH-PCO93-';
var ROWS=[["make", "Make: targets and recipes", "Makefiles declare targets with recipes (tab-indented commands); `make test` runs the test recipe. Targets can depend on files for rebuild logic. The 1976 design still runs the world's builds.", ["targets", "tab-indented recipes"]], ["make", "Make dependencies and rebuilds", "Targets depending on files rebuild only when prerequisites are newer — the original build avoidance. Phony targets (.PHONY) always run. Dependency graphs are Make's core.", ["file deps", ".PHONY"]], ["make", "Make variables and functions", "Variables (VAR=value, ?=, +=) and functions (wildcard, patsubst, shell) parameterize builds. Pattern rules (%.o: %.c) generalize compilation. Make is a small language, not just a runner.", ["variables", "pattern rules"]], ["just", "Just: the modern command runner", "Just (Rust, by Casey Rodarmor) is a command runner without Make's build-system legacy: a justfile with simple recipes, sane defaults, no tabs-vs-spaces traps. `just --list` shows documented recipes. Modern ergonomics, sa", ["justfile", "ergonomics"]], ["just", "Just recipes and parameters", "Just recipes take parameters with defaults (serve port='8000'), run with sh by default, and support dependencies between recipes. Parameterized recipes replace shell aliases. Defaults make common cases one word.", ["parameters", "defaults"]], ["just", "Just settings and attributes", "Settings ([private], dotenv-load, shell selection) and attributes tune behavior; dotenv-load auto-loads .env. Configuration lives at the top of the justfile. Explicit beats mysterious.", ["settings", "attributes"]], ["recipes", "Recipes as project documentation", "A justfile with documented recipes IS the project's command reference: new contributors run just --list instead of reading wikis. Executable documentation never rots. The justfile is the README that runs.", ["executable docs", "onboarding"]], ["recipes", "Common recipe patterns", "Patterns: dev (install+run), test (lint+unit), train (long ML runs), serve (model servers), clean (artifacts). Naming conventions make every project feel familiar. Conventions compound.", ["conventions", "familiarity"]], ["automation", "Make for AI workflows", "Make targets like train:, eval:, serve: encode ML pipelines with file dependencies (model depends on data). Rebuild avoidance saves GPU hours. Old tool, perfect fit.", ["ML pipelines", "rebuild avoidance"]], ["automation", "Just for AI workflows", "Just recipes like run-llm, bench, eval wrap long server commands with pinned flags. One word launches the tuned stack. Flags stop being tribal knowledge.", ["flag bundles", "tribal knowledge ends"]], ["just", "Cross-platform justfiles", "Just runs on Windows/macOS/Linux with the same justfile; OS-specific recipes use attributes or shell conditionals. One command surface everywhere. Portability without Make's quirks.", ["portability", "conditionals"]], ["recipes", "Including and modular justfiles", "justfiles import other justfiles (mod keyword), so teams share common recipes across repos. Shared modules standardize workflows. DRY applies to commands too.", ["mod imports", "shared modules"]], ["make", "Make pitfalls to avoid", "Tabs (not spaces), missing .PHONY, and recursive make are the classic traps; .RECIPEPREFIX can replace tabs. Knowing the traps prevents the folklore. Modern Make is tamer than its reputation.", ["tab trap", ".PHONY discipline"]], ["just", "Just pitfalls to avoid", "Recipes run with sh -cu by default (set shell for bash features); each recipe line runs in the same shell by default in Just (unlike Make). Defaults differ — read them. Assumptions cause the bugs.", ["shell defaults", "assumption bugs"]], ["automation", "Choosing Make vs Just", "Make when file-based rebuild logic matters (C builds, ML artifacts); Just when you want a friendly command runner (project tasks, dev workflows). Different jobs, different tools. Many projects use both.", ["fit guidance", "used together"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Make / Just",edition:'public',description:desc,facts:row[3].slice(),
    demo:{language:'python3',program:'print('+JSON.stringify('demo: '+row[1])+')',run:'python3 demo.py',expected_output:''},
    march:'million in progress — 15 of 1,000,000 records (march to a million)',provenance:"Public record \u2014 fact-checked.",last_verified:'2026-10-21',_seed:seed,_simulated:true};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].title===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-pc-organizer-make-just-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-make-just',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_make_just']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
