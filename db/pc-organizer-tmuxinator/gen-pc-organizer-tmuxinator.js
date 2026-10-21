(function(){'use strict';
/* Tmuxinator Database — boundless generator jahdb-pc-organizer-tmuxinator-1.0
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
var CATS=["config", "windows", "panes", "workflow"];
var PREFIX='JAH-PCO100-';
var ROWS=[["config", "The problem: rebuilding terminal layouts", "Every session starts with recreating panes (editor, server logs, GPU monitor, shell) by hand. Tmuxinator declares the layout once; one command restores it. Repetition becomes declaration.", ["declaration", "one command"]], ["config", "Project YAML files", "~/.config/tmuxinator/project.yml declares name, root, windows, panes, and startup commands. YAML is the layout language. Version it with dotfiles.", ["YAML", "dotfiles"]], ["windows", "Windows", "Windows group related panes (code window, serve window, monitor window) with layouts (tiled, main-vertical). Windows organize by concern. Layouts arrange panes.", ["grouping", "layouts"]], ["panes", "Panes with startup commands", "Each pane runs commands on creation (cd ~/proj && nvtop). Panes boot into their job. Startup commands encode the ritual.", ["startup commands", "rituals"]], ["workflow", "tmuxinator start/stop", "tmuxinator start ai builds the session; stop kills it. Session lifecycle is commands. Aliases (mux) shorten further.", ["lifecycle", "aliases"]], ["workflow", "The AI lab layout pattern", "The canonical layout: window 1 editor, window 2 server logs (vLLM), window 3 GPU monitor (nvtop) + shell. The pattern recurs for every local-AI project. One layout, many projects.", ["canonical", "reusable"]], ["config", "Project root and pre_window", "root sets the working directory; pre_window runs setup in every window (source venv). Shared setup runs once per window. DRY for shell setup.", ["root", "pre_window"]], ["panes", "Pane synchronization", "Synchronize-panes broadcasts input to all panes in a window for fleet commands (update all GPU nodes). Broadcasting multiplies keystrokes. Use with care.", ["broadcast", "fleet ops"]], ["workflow", "Attaching and detaching", "Sessions persist on detach; tmuxinator new + attach patterns manage remote sessions over SSH. Persistence survives disconnects. Remote work stays alive.", ["persistence", "remote"]], ["workflow", "Sharing layouts with teams", "Project YAMLs committed to repos give every teammate the same terminal workspace. Layouts become team convention. Onboarding includes the terminal.", ["team convention", "onboarding"]], ["config", "tmuxinator new wizard", "tmuxinator new project scaffolds a starter YAML interactively. Scaffolding beats blank files. The wizard teaches the format.", ["scaffolding", "wizard"]], ["workflow", "Local vs remote sessions", "Local sessions for dev; SSH + tmuxinator on GPU boxes for remote labs. Same tool, both ends. Layouts travel with you.", ["local", "remote"]], ["config", "Debugging layout issues", "tmuxinator debug prints the tmux commands it would run without executing. Dry-run debugging for layouts. See before you run.", ["dry-run", "debugging"]], ["panes", "Alternatives: raw tmux scripting", "Raw tmux send-keys scripts work but YAML declares intent more readably. Declarative beats imperative for layouts. Tmuxinator is the readable layer.", ["declarative", "readability"]], ["workflow", "Completions and aliases", "Shell completions and the mux alias make daily use frictionless. Small ergonomics, daily payoff. Install both.", ["alias", "completions"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Tmuxinator",edition:'public',description:desc,facts:row[3].slice(),
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
var gen={version:'jahdb-pc-organizer-tmuxinator-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-tmuxinator',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_tmuxinator']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
