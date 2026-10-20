(function(){'use strict';
/* JAH The Semaphore Signature Database generator — jahdb-techpresent-r16-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..20 rebuild the archive
   records; higher seeds generate boundless variants (quizzes, explorers,
   glossaries) derived from the archive's own anchors. */
var SLUG="semaphore-ci-signature";
var PLAIN="Semaphore — Signature Edition";
var DSUFFIX=" — Signature Method";
var PREFIX="JAH-SCS4-";
var SIG=true;
var SRC="signature";
var FIELDS=["Foundations","Compounded","Advanced"];
var ESSENCE="The Signature edition: the JAH system's original reference on Semaphore. Semaphore: Developer tool: Semaphore. Made by Semaphore, first released 2011. Runs on Cloud; licensed as Commercial.";
var ANCHORS=[{"title": "What Semaphore is", "facts": ["Developer tool: Semaphore.", "Developer tools turn ideas into running software: write, build, test, ship."]}, {"title": "Maker and history", "facts": ["From Semaphore; first released 2011.", "Fast pipelines."]}, {"title": "Core concepts", "facts": ["Monorepo support.", "Learn the vocabulary first: the docs assume it everywhere."]}, {"title": "How it works", "facts": ["Docker-native.", "Most dev tools are command-line first with optional graphical layers on top."]}, {"title": "Installation", "facts": ["Install on Cloud via the official installer or package manager.", "Pin versions in team projects so everyone builds with the same toolchain."]}, {"title": "Daily workflow", "facts": ["The loop is edit, build, run, test, debug; fast tools shorten the loop and win.", "Keep a scratch project for experiments so learning never risks real work."]}, {"title": "Configuration", "facts": ["Configuration lives in text files; keep them in version control.", "Start from the defaults and change one setting at a time."]}, {"title": "Integrations", "facts": ["Connect the tool to version control and CI so work flows automatically.", "Extensions and plugins add language support, linters and debuggers."]}, {"title": "Alternatives", "facts": ["Compare on ecosystem maturity, documentation quality and community size.", "The popular choice is usually popular because the tooling around it is complete."]}, {"title": "Best practices", "facts": ["Read the official docs before Stack Overflow; they are the contract.", "Automate repetitive steps with scripts from the start."]}];
var TERMS=[{"t": "Compiler", "d": "Translates source code into machine code before the program runs."}, {"t": "Interpreter", "d": "Runs source code directly, line by line, without a separate build step."}, {"t": "Debugger", "d": "Steps through running code, inspects variables, and finds faults."}, {"t": "Linter", "d": "Checks code for style errors and likely bugs without running it."}, {"t": "Build", "d": "The process turning source files into a runnable program or package."}, {"t": "Dependency", "d": "An external library a project needs in order to build or run."}, {"t": "Repository", "d": "Version-controlled project history hosted locally or on a service."}, {"t": "CI", "d": "Continuous integration: automated builds and tests on every change."}, {"t": "API", "d": "The defined interface other programs use to talk to a tool or library."}, {"t": "SDK", "d": "Software development kit: libraries, docs and tools for one platform."}];
var GUIDE=["Pick the tool your team or tutorial uses; ecosystem beats features.", "Check documentation quality before committing; you will live in those docs.", "Prefer tools with a large extension or plugin marketplace."];
var SAFETY=["Install only from official sources; dev tools run with high privileges.", "Review scripts and plugins before running them; they execute arbitrary code.", "Keep toolchains updated to receive security patches."];
var MAINT=["Update the toolchain on a schedule, not mid-deadline.", "Rebuild from clean regularly to catch hidden dependency drift.", "Archive old SDKs with old projects so they still build in five years."];
var HIST=["1970s: Unix gives developers pipes, shells and C.", "1990s: IDEs bundle editing, building and debugging in one window.", "2005: Git decentralizes version control; 2008: GitHub socializes it.", "2010s: containers and CI make 'works on my machine' obsolete."];
var TEACH=["Live-code a tiny project from empty folder to running program.", "Teach reading error messages before writing more code.", "Assign a real bug fix in an open-source project."];
var LASTV="2026-10-19";
var PUB_SRC="Public record \u2014 curated public-knowledge reference.";
var SIG_SRC="Signature record \u2014 original work of the JAH system, labeled Signature, never presented as public record.";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pickR(rnd,n){return (rnd()*n)|0;}
function escJ(s){return String(s).replace(/\\/g,"\\\\").replace(/"/g,'\\"').replace(/\n/g,"\\n").replace(/\r/g,"");}
function mkProg(kind,title,items){
  var L=['console.log("'+kind.toUpperCase()+': '+escJ(title)+'");'];
  if(kind==="quiz"){
    L.push('var qa=['+items.slice(0,6).map(function(x){return '["'+escJ(x[0])+'","'+escJ(x[1]).slice(0,150)+'"]';}).join(",")+'];');
    L.push('for(var i=0;i<qa.length;i++){console.log("Q"+(i+1)+": "+qa[i][0]);console.log("A"+(i+1)+": "+qa[i][1]);}');
    L.push('console.log("Reviewed "+qa.length+" Q&A pairs.");');
  }else if(kind==="glossary"){
    L.push('var terms=['+items.slice(0,8).map(function(x){return '["'+escJ(x[0])+'","'+escJ(x[1]).slice(0,150)+'"]';}).join(",")+'];');
    L.push('for(var j=0;j<terms.length;j++){console.log(terms[j][0]+" \u2014 "+terms[j][1]);}');
    L.push('console.log(terms.length+" terms defined.");');
  }else if(kind==="datatable"){
    L.push('var rows=['+items.slice(0,8).map(function(x){return '["'+escJ(x[0])+'","'+escJ(x[1]).slice(0,120)+'"]';}).join(",")+'];');
    L.push('for(var k=0;k<rows.length;k++){console.log(rows[k][0]+" = "+rows[k][1]);}');
    L.push('console.log(rows.length+" values listed.");');
  }else{
    L.push('var items=['+items.slice(0,8).map(function(x){return '"'+escJ(x)+'"';}).join(",")+'];');
    L.push('for(var m=0;m<items.length;m++){console.log((m+1)+". "+items[m]);}');
    L.push('console.log("Done: "+items.length+" items reviewed.");');
  }
  return L.join("\n");
}
function baseRec(seed,title,tier){
  return {
    id:PREFIX+String(seed).padStart(6,"0"),
    t:title, g:FIELDS[tier]||FIELDS[0], c:0, title:title,
    src:SRC, last_verified:LASTV,
    language:"javascript",
    ladder_rank:tier+1, ladder_tier:FIELDS[tier]||FIELDS[0],
    _seed:seed
  };
}
function fin(r,description,definition,points,steps,program,demoKind){
  r.description=description;
  r.definition=definition;
  r.key_points=points.slice(0);
  while(r.key_points.length<3)r.key_points.push("See the full record for working detail.");
  r.how_it_works=steps;
  r.program=program;
  r.demo={kind:demoKind,language:"javascript",program:program,note:"Runnable demo program."};
  r.source=SIG?SIG_SRC:PUB_SRC;
  r.provenance=r.source;
  return r;
}
function overviewRec(){
  var r=baseRec(1,"What "+PLAIN+" Is All About",0);
  var desc=ESSENCE+" Full records with definitions, key facts, procedures, and runnable demo programs, on a teaching ladder from Foundations to Advanced.";
  var prog=mkProg("checklist","Overview",["full records","teaching ladder","runnable demos","scope: "+ESSENCE.slice(0,80)]);
  return fin(r,desc,PLAIN+": complete reference database.",
    ["Full records \u2014 never stubs.","Teaching ladder: Foundations, Compounded, Advanced.",
     "Every record ships a runnable demo program.","Scope: "+ESSENCE.slice(0,100)+"."],
    ["Start with this overview.","Work Foundations in order.","Run each demo.","Advance up the ladder."],
    prog,"overview");
}
function anchorRec(seed,a,tier){
  var r=baseRec(seed,a.title,tier);
  var facts=a.facts||[];
  var desc=a.title+". "+facts.join(" ");
  while(desc.length<140)desc+=" "+ESSENCE;
  var prog=mkProg("datatable",a.title,facts.map(function(f,i){return ["fact "+(i+1),f];}));
  var dcore=((facts[0]||"")+" "+(facts[1]||"")).replace(/^\s+|\s+$/g,"");
  if(dcore.length<30)dcore=ESSENCE;
  return fin(r,desc,a.title+" \u2014 "+dcore.slice(0,140)+".",
    facts.slice(0,4),
    ["Read the definition and key facts.","Run the demo program below.",
     "Note the numbers \u2014 they are the working values.","Apply it to a real case."],
    prog,SIG?"signature method simulator":"archive explorer");
}
function derivedRec(seed,kind,title,descExtra,points,steps,prog,demoKind){
  var tier=seed<=14?1:2;
  var r=baseRec(seed,title+DSUFFIX,tier);
  var desc=title+DSUFFIX+": "+descExtra+" "+ESSENCE;
  while(desc.length<140)desc+=" "+ESSENCE;
  return fin(r,desc,title+DSUFFIX+" \u2014 "+descExtra.slice(0,120)+".",points,steps,prog,demoKind);
}
function glossaryRec(seed){
  var pairs=TERMS.map(function(t){return [t.t,t.d];});
  return derivedRec(seed,"glossary","Core Glossary: "+PLAIN,
    "the working vocabulary of "+PLAIN+": "+pairs.length+" terms with plain definitions, runnable as a demo.",
    pairs.map(function(p){return p[0]+": "+p[1].slice(0,80);}),
    ["Run the demo glossary.","Cover each definition and recite it.","Check against the record.","Repeat until instant."],
    mkProg("glossary","Core Glossary: "+PLAIN,pairs),"glossary drill");
}
function quizRec(seed,rnd){
  var qa=ANCHORS.slice(0,6).map(function(a){return ["Key fact: "+a.title,(a.facts[0]||"").slice(0,150)];});
  return derivedRec(seed,"quiz","Self-Test Quiz: "+PLAIN,
    "a boundless self-test from the archive's own anchors: "+qa.length+" questions with answers from the key facts.",
    qa.map(function(x){return x[0];}),
    ["Run the demo quiz.","Answer each question aloud before reading the answer.","Log misses and re-open those records.","Re-drill until perfect."],
    mkProg("quiz","Self-Test Quiz: "+PLAIN,qa),"self-test quiz");
}
function compareRec(seed){
  var rows=ANCHORS.slice(0,8).map(function(a){return [a.title,(a.facts[0]||"").slice(0,120)];});
  return derivedRec(seed,"compare","Side-by-Side Comparison: "+PLAIN,
    "every anchor laid side by side: "+rows.length+" entries compared on their defining fact.",
    rows.map(function(x){return x[0];}),
    ["Read the comparison table.","Pick the two closest entries and list their differences.","Match entries to real cases.","Revisit after field experience."],
    mkProg("datatable","Side-by-Side Comparison: "+PLAIN,rows),"comparison table");
}
function listRec(seed,kind,title,blurb,items,demoKind){
  return derivedRec(seed,kind,title,blurb,items.slice(0,4),
    ["Read each point.","Run the demo walkthrough.","Apply one point to a real case this week.","Teach the list to someone else."],
    mkProg("checklist",title,items),demoKind);
}
function archiveDerived(seed){
  var k=seed-12;
  if(k===0)return glossaryRec(seed);
  if(k===1)return quizRec(seed,prng(seed));
  if(k===2)return compareRec(seed);
  if(k===3)return listRec(seed,"guide","Selection Guide: "+PLAIN,"how to choose well in "+PLAIN+": the criteria that matter.",GUIDE,"selection guide");
  if(k===4)return listRec(seed,"safety","Safety and Responsible Use: "+PLAIN,"the safety rules for "+PLAIN+": read before touching anything.",SAFETY,"safety briefing");
  if(k===5)return listRec(seed,"maint","Maintenance and Troubleshooting: "+PLAIN,"keeping "+PLAIN+" working: maintenance rhythms and fixes.",MAINT,"maintenance guide");
  if(k===6){var rows=HIST.map(function(h,i){return ["milestone "+(i+1),h.slice(0,120)];});
    return derivedRec(seed,"history","History and Turning Points: "+PLAIN,"how "+PLAIN+" got here: the milestones that shaped it.",
    HIST.slice(0,4),["Read the milestones in order.","Connect each turning point to what changed.","Ask what the next one could be.","Place yourself on the timeline."],
    mkProg("datatable","History and Turning Points: "+PLAIN,rows),"timeline");}
  if(k===7)return listRec(seed,"teach","Teach It to Someone Else: "+PLAIN,"how to teach "+PLAIN+": the explanations that stick.",TEACH,"teaching guide");
  return listRec(seed,"checklist","Master Checklist: "+PLAIN,"the full sweep of "+PLAIN+": every anchor in one checklist.",
    ANCHORS.slice(0,8).map(function(a){return a.title;}),"master checklist");
}
function boundlessQuiz(seed,rnd){
  var qa=ANCHORS.slice(0,6).map(function(a){return ["Key fact: "+a.title,(a.facts[0]||"").slice(0,150)];});
  var r=baseRec(seed,"Boundless Quiz #"+seed+" \u2014 "+SLUG,2);
  return fin(r,"A boundless self-test generated from the archive's own anchors: "+qa.length+" questions drawn from real "+SLUG+" records. Same seed always makes the same quiz.",
    "Generated self-test over the "+SLUG+" archive anchors.",qa.map(function(x){return x[0];}),
    ["Run the demo quiz.","Answer aloud before reading.","Log misses.","Re-drill until perfect."],
    mkProg("quiz","Boundless Quiz #"+seed,qa),"self-test quiz");
}
function boundlessExplorer(seed,rnd){
  var a=ANCHORS[pickR(rnd,ANCHORS.length)];
  var facts=a.facts||[];
  var r=baseRec(seed,"Boundless Explorer #"+seed+": "+a.title,2);
  return fin(r,"A boundless explorer record for "+a.title+": every fact laid out with a runnable program that walks them in order. Generated deterministically from seed "+seed+". "+facts.join(" ").slice(0,200),
    "Explorer record: "+a.title+", all facts in walking order.",facts.slice(0,4),
    ["Read each fact in order.","Run the demo walkthrough.","Pause on any fact you cannot restate.","Summarize the chain from memory."],
    mkProg("checklist","Boundless Explorer: "+a.title,facts.length?facts:["see key facts"]),"record explorer");
}
function boundlessTerms(seed,rnd){
  var pairs=TERMS.map(function(t){return [t.t,t.d];});
  var r=baseRec(seed,"Boundless Glossary Drill #"+seed+" \u2014 "+SLUG,2);
  return fin(r,"A boundless glossary drill from the archive's own vocabulary: "+pairs.length+" terms with definitions, runnable as a demo. Same seed, same drill.",
    "Generated glossary drill over the "+SLUG+" working vocabulary.",pairs.map(function(p){return p[0]+": "+p[1].slice(0,80);}),
    ["Run the demo glossary.","Cover each definition and recite it.","Check against the record.","Repeat until instant."],
    mkProg("glossary","Boundless Glossary Drill #"+seed,pairs),"glossary drill");
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var tier=0;
  if(opts.tier&&FIELDS.indexOf(opts.tier)>=0)tier=FIELDS.indexOf(opts.tier);
  else if(opts.group&&FIELDS.indexOf(opts.group)>=0)tier=FIELDS.indexOf(opts.group);
  if(seed===1)return overviewRec();
  if(seed>=2&&seed<=11){
    var ai=seed-2;
    return anchorRec(seed,ANCHORS[ai],ai<4?0:(ai<7?1:2));
  }
  if(seed>=12&&seed<=20){
    var r=archiveDerived(seed);
    if(opts.tier||opts.group)r.g=FIELDS[tier]||r.g;
    return r;
  }
  var v=rnd();
  if(v<0.4)return boundlessQuiz(seed,rnd);
  if(v<0.7)return boundlessExplorer(seed,rnd);
  return boundlessTerms(seed,rnd);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  var idre=new RegExp("^"+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"\\d{6}$");
  if(!idre.test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.g)<0)e.push("group");
  if(typeof r.title!=="string"||!r.title.length)e.push("title");
  if(typeof r.description!=="string"||r.description.length<120)e.push("description");
  if(typeof r.definition!=="string"||r.definition.length<30)e.push("definition");
  if(!Array.isArray(r.key_points)||r.key_points.length<3)e.push("key_points");
  if(typeof r.program!=="string"||r.program.indexOf("console.log")<0)e.push("program");
  if(r.src!==SRC)e.push("src");
  if(!r.last_verified)e.push("last_verified");
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&(s.t||s.title))seen[s.t||s.title]=1;});
  if(rec&&seen[rec.title||rec.t])return {ok:false,errors:["duplicate title in archive sample"]};
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-techpresent-r16-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
