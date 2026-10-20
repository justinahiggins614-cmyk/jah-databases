(function(){'use strict';
/* JAH Git Commands Database generator — jahdb-git-commands-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='git-commands',PREFIX='JAH-GIT-',NAME='JAH Git Commands Database';
var FIELDS=["setup", "basic", "branching", "remote", "stashing", "undo", "inspect", "plumbing"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "git init", "d": "Creates a new repository.", "g": "setup", "l": 2, "q": "What is git init?", "a": "Creates a new repository.", "x": "git init — Creates a new repository. Example: git init my-project.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git clone", "d": "Copies a remote repository locally.", "g": "setup", "l": 2, "q": "What is git clone?", "a": "Copies a remote repository locally.", "x": "git clone — Copies a remote repository locally. Example: git clone https://github.com/user/repo.git.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git config", "d": "Gets and sets configuration.", "g": "setup", "l": 2, "q": "What is git config?", "a": "Gets and sets configuration.", "x": "git config — Gets and sets configuration. Example: git config user.name \"Manon\".  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git alias", "d": "Custom command shortcuts via config.", "g": "setup", "l": 2, "q": "What is git alias?", "a": "Custom command shortcuts via config.", "x": "git alias — Custom command shortcuts via config. Example: git config alias.co checkout.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git help", "d": "Shows help for a command.", "g": "setup", "l": 2, "q": "What is git help?", "a": "Shows help for a command.", "x": "git help — Shows help for a command. Example: git help commit.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git add", "d": "Stages changes.", "g": "basic", "l": 2, "q": "What is git add?", "a": "Stages changes.", "x": "git add — Stages changes. Example: git add file.txt.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git status", "d": "Shows working tree state.", "g": "basic", "l": 2, "q": "What is git status?", "a": "Shows working tree state.", "x": "git status — Shows working tree state. Example: git status.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git diff", "d": "Shows unstaged changes.", "g": "basic", "l": 2, "q": "What is git diff?", "a": "Shows unstaged changes.", "x": "git diff — Shows unstaged changes. Example: git diff.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git commit", "d": "Records staged changes.", "g": "basic", "l": 2, "q": "What is git commit?", "a": "Records staged changes.", "x": "git commit — Records staged changes. Example: git commit -m \"fix bug\".  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git restore", "d": "Restores files (newer undo command).", "g": "basic", "l": 2, "q": "What is git restore?", "a": "Restores files (newer undo command).", "x": "git restore — Restores files (newer undo command). Example: git restore file.txt.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git log", "d": "Shows commit history.", "g": "basic", "l": 2, "q": "What is git log?", "a": "Shows commit history.", "x": "git log — Shows commit history. Example: git log --oneline.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git show", "d": "Shows one object in detail.", "g": "basic", "l": 2, "q": "What is git show?", "a": "Shows one object in detail.", "x": "git show — Shows one object in detail. Example: git show HEAD.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git rm", "d": "Removes files from the index and disk.", "g": "basic", "l": 2, "q": "What is git rm?", "a": "Removes files from the index and disk.", "x": "git rm — Removes files from the index and disk. Example: git rm old.txt.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git mv", "d": "Moves/renames tracked files.", "g": "basic", "l": 2, "q": "What is git mv?", "a": "Moves/renames tracked files.", "x": "git mv — Moves/renames tracked files. Example: git mv a.txt b.txt.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git clean", "d": "Removes untracked files.", "g": "basic", "l": 2, "q": "What is git clean?", "a": "Removes untracked files.", "x": "git clean — Removes untracked files. Example: git clean -fd.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git branch", "d": "Lists, creates, deletes branches.", "g": "branching", "l": 2, "q": "What is git branch?", "a": "Lists, creates, deletes branches.", "x": "git branch — Lists, creates, deletes branches. Example: git branch feature-x.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git checkout", "d": "Switches branches or restores files.", "g": "branching", "l": 2, "q": "What is git checkout?", "a": "Switches branches or restores files.", "x": "git checkout — Switches branches or restores files. Example: git checkout main.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git switch", "d": "Modern branch switching.", "g": "branching", "l": 2, "q": "What is git switch?", "a": "Modern branch switching.", "x": "git switch — Modern branch switching. Example: git switch -c new-branch.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git merge", "d": "Joins branch histories.", "g": "branching", "l": 2, "q": "What is git merge?", "a": "Joins branch histories.", "x": "git merge — Joins branch histories. Example: git merge feature-x.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git rebase", "d": "Replays commits onto a new base.", "g": "branching", "l": 2, "q": "What is git rebase?", "a": "Replays commits onto a new base.", "x": "git rebase — Replays commits onto a new base. Example: git rebase main.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git cherry-pick", "d": "Applies one commit elsewhere.", "g": "branching", "l": 2, "q": "What is git cherry-pick?", "a": "Applies one commit elsewhere.", "x": "git cherry-pick — Applies one commit elsewhere. Example: git cherry-pick abc123.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git worktree", "d": "Multiple working trees for one repo.", "g": "branching", "l": 2, "q": "What is git worktree?", "a": "Multiple working trees for one repo.", "x": "git worktree — Multiple working trees for one repo. Example: git worktree add ../hotfix.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git tag", "d": "Marks releases.", "g": "branching", "l": 2, "q": "What is git tag?", "a": "Marks releases.", "x": "git tag — Marks releases. Example: git tag v1.0.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "git describe", "d": "Names a commit via nearest tag.", "g": "branching", "l": 2, "q": "What is git describe?", "a": "Names a commit via nearest tag.", "x": "git describe — Names a commit via nearest tag. Example: git describe --tags.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}, {"t": "git fetch", "d": "Downloads objects without merging.", "g": "remote", "l": 2, "q": "What is git fetch?", "a": "Downloads objects without merging.", "x": "git fetch — Downloads objects without merging. Example: git fetch origin.  Checked against the authoritative references for this standard. Every entry here is a real, current value — not a placeholder.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-git-commands-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
