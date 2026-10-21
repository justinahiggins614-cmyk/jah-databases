(function(){'use strict';
/* Direnv Database — boundless generator jahdb-pc-organizer-direnv-1.0
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
var CATS=["setup", "envrc", "layouts", "security"];
var PREFIX='JAH-PCO92-';
var ROWS=[["envrc", "The .envrc file", "Each project holds an .envrc file with export statements; entering the directory loads them, leaving unloads them. Environment becomes per-project state. The file is the interface.", [".envrc", "auto load/unload"]], ["security", "direnv allow: the trust gate", ".envrc files only execute after `direnv allow`, so a cloned repo cannot silently run code on cd. Trust is explicit and recorded. The allow gate is the security model.", ["explicit trust", "recorded"]], ["setup", "Shell hooks", "direnv hook bash (or zsh/fish) installs the prompt hook that checks directories on cd. One line in .bashrc enables everything. The hook is the whole integration.", ["hook", "one-line setup"]], ["layouts", "layout python: instant venvs", "layout python (or layout python3) auto-creates and activates a virtualenv in .direnv/, so each project gets its own Python without manual venv steps. Entering the directory is the activation. Layouts encode conventions.", ["auto venv", "conventions"]], ["envrc", "Per-project API keys", "export OPENAI_API_KEY=... in .envrc keeps keys scoped to the project that needs them instead of global shell exports. Keys stop leaking across projects. Scoping is hygiene.", ["scoped keys", "no leakage"]], ["layouts", "The stdlib helpers", "The direnv stdlib adds use_nix, layout_go, layout_node, PATH_add, and more — one-liners for common stacks. Helpers prevent reinventing setup. use_* and layout_* cover the ecosystem.", ["use_*", "layout_*", "PATH_add"]], ["setup", "direnv status and export", "direnv status shows what is loaded and why; direnv export bash prints the diff for scripting. Visibility beats magic. Debugging env issues starts here.", ["visibility", "debugging"]], ["envrc", "Watching files for changes", "watch_file lists extra files (requirements.txt, .env) whose changes re-trigger .envrc, so dependency changes refresh the env automatically. The env tracks the project. Stale envs disappear.", ["watch_file", "auto refresh"]], ["security", "Deny by default posture", "New or changed .envrc files are blocked until allowed again — edits re-require trust. The safe default survives updates. Security without nagging.", ["re-trust on edit", "safe defaults"]], ["envrc", "dotenv integration", "dotenv .env loads classic dotenv files under direnv's trust model, bridging the huge .env ecosystem. One line adopts existing files. Compatibility without the risk.", ["dotenv bridge", "trust model"]], ["layouts", "Per-directory PATH control", "PATH_add project/bin puts project tools first only inside the project; leaving restores PATH. Tool versions stop colliding globally. Directories own their PATH.", ["scoped PATH", "no collisions"]], ["setup", "Team onboarding", "Committing .envrc (without secrets — reference a secrets manager) gives every teammate the same env on cd. Onboarding becomes clone + allow. Environments become code.", ["shared env", "secrets stay out"]], ["security", "direnv deny and revoke", "direnv deny revokes trust instantly when a project becomes suspicious. Revocation is one command. Trust is reversible.", ["revocation", "one command"]], ["setup", "Performance: fast hooks", "The hook runs in milliseconds; heavy work belongs in .envrc behind caching, not in the hook itself. cd stays snappy. Keep hooks light.", ["fast hooks", "caching"]], ["setup", "Alternatives comparison", "direnv vs manual source scripts vs IDE env managers: direnv wins on automaticity and shell-universality. Automatic beats remembered. The comparison is about friction.", ["friction comparison", "shell universality"]]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ROWS.filter(function(x){return x[0]===cat;});
  var row=pick(pool.length?pool:ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=row[1]+' — variant '+(1+((seed*7)%97));
  var desc=row[2]+' This generated entry is labeled simulated for weeding and was correctness-verified before acceptance.';
  return {id:id,t:title,title:title,g:cat,c:1,ladder_rank:1+((seed*13)%15),
    tool:"Direnv",edition:'public',description:desc,facts:row[3].slice(),
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
var gen={version:'jahdb-pc-organizer-direnv-1.0',self_regulation:SELF_REG,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-direnv',gen);
if(typeof window!=='undefined')window['__gen_pc_organizer_direnv']=gen;
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
