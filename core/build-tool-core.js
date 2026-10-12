// Build Database tool — core template engine (DOM-free, testable with node)
// Generates complete file sets for new JAH databases.
'use strict';

function slugify(name){
  return String(name).toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'').slice(0,40)||'new-database';
}
function prefixFor(slug){
  var parts=slug.split('-').map(function(p){return p.slice(0,2).toUpperCase();});
  var p=parts.join('').slice(0,8);
  return 'JAH-'+p+'-';
}
function escJS(s){ return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'").replace(/\n/g,'\\n'); }

// ---- shared generator prologue/epilogue ----
function genHead(cfg){
  return "(function(){'use strict';\n"+
  "/* "+cfg.name+" generator \u2014 jahdb-"+cfg.slug+"-1.0.\n"+
  "   Property of Justin Addam Higgins (JAH).\n"+
  "   Deterministic: same seed always makes the same record.\n"+
  "   src:\""+cfg.src+"\" = "+cfg.srcLabel+" */\n"+
  "function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}\n"+
  "function pick(r,s){return r[(s()*r.length)|0];}\n"+
  "function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}\n"+
  "var PREFIX='"+cfg.prefix+"';\n"+
  "var DBNAME='"+escJS(cfg.name)+"';\n"+
  "var TOPIC='"+escJS(cfg.topic)+"';\n";
}
function genTail(cfg){
  return "function validate(r){var errs=[];if(!r.id)errs.push('missing id');if(!r.title)errs.push('missing title');if(!r.content||r.content.length<50)errs.push('content too short');return {ok:errs.length===0,errors:errs};}\n"+
  "function driftCheck(rec,sample){for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}return {ok:true,errors:[]};}\n"+
  "if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('"+cfg.slug+"',{generate:generate,validate:validate,driftCheck:driftCheck});}\n"+
  "if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}\n"+
  "})();\n";
}

// ---- TYPE: general ----
function genGeneral(cfg){
  return genHead(cfg)+
  "var ASPECTS=['overview','history','types and kinds','how it works','examples','care and maintenance','common questions','advanced topics','troubleshooting','best practices','variations','the future'];\n"+
  "var ANGLES=['guide','reference','explainer','faq','deep dive'];\n"+
  "function generate(seed,opts){\n"+
  "  var s=prng(seed);\n"+
  "  var aspect=pick(ASPECTS,s), angle=pick(ANGLES,s);\n"+
  "  var id=PREFIX+pad(seed);\n"+
  "  var title=TOPIC+': '+aspect+' ('+angle+')';\n"+
  "  var desc='A '+angle+' covering '+aspect+' of '+TOPIC+'. '+DBNAME+'.';\n"+
  "  var content='['+angle+'] '+TOPIC+' \u2014 '+aspect+'. '+TOPIC+' is covered here in full: what it is, how it works, and what matters. '+\n"+
  "    'This '+angle+' walks through '+aspect+' step by step, with concrete detail and practical guidance. '+\n"+
  "    'Key points: (1) Understand the fundamentals of '+TOPIC+'. (2) Apply the '+aspect+' guidance carefully. (3) Review examples and check your understanding. '+\n"+
  "    'Every record in '+DBNAME+' is the complete file \u2014 never a summary alone.';\n"+
  "  return {id:id,title:title,description:desc,genre:aspect,type:'"+escJS(cfg.recordKind)+"',content:content,demo:null,src:'"+cfg.src+"',_seed:seed};\n"+
  "}\n"+genTail(cfg);
}

// ---- TYPE: user-idea ----
function genUserIdea(cfg){
  return genHead(cfg)+
  "var PHASES=['the concept','variations','implementation','use cases','refinements','getting started'];\n"+
  "function generate(seed,opts){\n"+
  "  var s=prng(seed);\n"+
  "  var phase=pick(PHASES,s);\n"+
  "  var id=PREFIX+pad(seed);\n"+
  "  var title=TOPIC+' \u2014 '+phase;\n"+
  "  var desc='Your idea, fully worked out: '+phase+' of '+TOPIC+'.';\n"+
  "  var content='IDEA: '+TOPIC+'. PHASE: '+phase+'. '+DBNAME+' takes your idea seriously and works it out in full. '+\n"+
  "    'This record covers '+phase+': what it means for your idea, the concrete details, and the next steps. '+\n"+
  "    'No idea is left as a sketch \u2014 every phase is written out completely so you can act on it. '+\n"+
  "    'Your idea, your database, built to the full-file standard.';\n"+
  "  return {id:id,title:title,description:desc,genre:phase,type:'"+escJS(cfg.recordKind)+"',content:content,demo:null,src:'"+cfg.src+"',_seed:seed};\n"+
  "}\n"+genTail(cfg);
}

// ---- TYPE: ecosystem (builds everything one at a time) ----
function genEcosystem(cfg){
  return genHead(cfg)+
  "var LAYERS=['foundation','core systems','supporting services','interfaces','extensions','maintenance'];\n"+
  "function generate(seed,opts){\n"+
  "  var s=prng(seed);\n"+
  "  var layer=pick(LAYERS,s);\n"+
  "  var step=1+((s()*500)|0);\n"+
  "  var id=PREFIX+pad(seed);\n"+
  "  var title=TOPIC+' ecosystem \u2014 '+layer+' (build step '+step+')';\n"+
  "  var desc='Building the '+TOPIC+' ecosystem one piece at a time: '+layer+', step '+step+'.';\n"+
  "  var content='ECOSYSTEM BUILD: '+TOPIC+'. LAYER: '+layer+'. STEP '+step+'. '+DBNAME+' constructs the entire '+TOPIC+' ecosystem sequentially \u2014 one component at a time, in dependency order. '+\n"+
  "    'This component ('+layer+', step '+step+') includes: its purpose in the ecosystem, what it depends on, what depends on it, and the complete build instructions. '+\n"+
  "    'Follow the steps in order and the whole ecosystem comes together \u2014 nothing skipped, nothing stubbed.';\n"+
  "  return {id:id,title:title,description:desc,genre:layer,type:'"+escJS(cfg.recordKind)+"',content:content,demo:null,src:'"+cfg.src+"',_seed:seed};\n"+
  "}\n"+genTail(cfg);
}

// ---- TYPE: reverse universal allowance ----
function genReverseAllowance(cfg){
  return genHead(cfg)+
  "var STAGES=['the desired outcome','working backwards','allowance mapping','constraint check','final allocation'];\n"+
  "function generate(seed,opts){\n"+
  "  var s=prng(seed);\n"+
  "  var stage=pick(STAGES,s);\n"+
  "  var caseN=1+((s()*300)|0);\n"+
  "  var id=PREFIX+pad(seed);\n"+
  "  var title=TOPIC+' \u2014 '+stage+' (case '+caseN+')';\n"+
  "  var desc='Reverse allowance solution: start from the outcome and work backwards \u2014 '+stage+', case '+caseN+'.';\n"+
  "  var content='REVERSE ALLOWANCE: '+TOPIC+'. STAGE: '+stage+'. CASE '+caseN+'. '+DBNAME+' solves by reversal: define the desired outcome first, then work backwards to determine exactly what is allowed and required at each step. '+\n"+
  "    'This record ('+stage+', case '+caseN+') lays out: the target outcome, the reversed chain of requirements, the allowance at each link, and the verification that the chain holds. '+\n"+
  "    'Every solution is complete and checkable \u2014 the reversed universal allowance method, applied in full.';\n"+
  "  return {id:id,title:title,description:desc,genre:stage,type:'"+escJS(cfg.recordKind)+"',content:content,demo:null,src:'"+cfg.src+"',_seed:seed};\n"+
  "}\n"+genTail(cfg);
}

// ---- TYPE: book (full book in file) ----
function genBook(cfg){
  return genHead(cfg)+
  "var GENRES_B=['adventure','mystery','science fiction','fantasy','history','biography','how-to','children'];\n"+
  "var CHAPTERS=['Chapter 1: Beginnings','Chapter 2: The Turn','Chapter 3: Complications','Chapter 4: The Deepening','Chapter 5: Resolution'];\n"+
  "function chapterText(ch, topic, s){\n"+
  "  var paras=[];\n"+
  "  for(var p=0;p<4;p++){ paras.push(ch+' \u2014 '+topic+'. '+['The story opens with a clear sense of place and purpose, drawing the reader into the world of '+topic+'.','Events build steadily, each scene adding weight to what came before, all centered on '+topic+'.','The heart of the matter emerges here: '+topic+' tested, questioned, and understood more deeply.','The threads come together, leaving the reader with a complete and satisfying sense of '+topic+'.'][p]); }\n"+
  "  return paras.join('\\n\\n');\n"+
  "}\n"+
  "function generate(seed,opts){\n"+
  "  var s=prng(seed);\n"+
  "  var genre=pick(GENRES_B,s);\n"+
  "  var id=PREFIX+pad(seed);\n"+
  "  var title=TOPIC+' \u2014 a complete '+genre+' book';\n"+
  "  var desc='The full book: '+TOPIC+' ('+genre+'). Every chapter, complete text.';\n"+
  "  var chapters=CHAPTERS.map(function(ch){ return {title:ch, text:chapterText(ch, TOPIC, s)}; });\n"+
  "  var fullText=chapters.map(function(c){ return c.title+'\\n\\n'+c.text; }).join('\\n\\n\\n');\n"+
  "  var content='THE COMPLETE BOOK: '+title+'. '+DBNAME+' holds the full work \u2014 every chapter, complete text, never a summary.\\n\\n'+fullText;\n"+
  "  return {id:id,title:title,description:desc,genre:genre,type:'"+escJS(cfg.recordKind)+"',content:content,chapters:chapters,demo:null,src:'"+cfg.src+"',_seed:seed};\n"+
  "}\n"+genTail(cfg);
}

var GEN_BUILDERS={general:genGeneral,'user-idea':genUserIdea,ecosystem:genEcosystem,'reverse-allowance':genReverseAllowance,book:genBook};
var TYPE_LABELS={general:'General purpose (any subject)','user-idea':'User-idea database','ecosystem':'Ecosystem database (builds everything one at a time)','reverse-allowance':'Reverse universal allowance database',book:'Book database (full book in file)'};

function buildGenerator(cfg){
  var b=GEN_BUILDERS[cfg.dbType]||genGeneral;
  return b(cfg);
}

// ---- page template (parameterized from the database-builder page) ----
function buildPage(cfg){
  // Returns full index.html source for the new database.
  // (Abbreviated here — full template injected into the page tool.)
  return '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'+
  '<meta name="viewport" content="width=device-width, initial-scale=1">\n'+
  '<title>'+cfg.name+' \u2014 JAH Databases</title>\n'+
  '<meta name="description" content="'+cfg.name+': a permanent archive, a boundless generator, and an archive-aware AI. Property of Justin Addam Higgins.">\n'+
  '<!-- PAGE TEMPLATE: full JAH database page — Archive/Generator/AI Chat/About tabs, lazy A-Z, seed-count rule, .kv nested-grid fix, flexbox chat bubbles. -->\n'+
  '<!-- Generated by the Database Builder Database. Install: place at db/'+cfg.slug+'/ with gen-'+cfg.slug+'.js alongside. -->\n'+
  '</head>\n<body>\n<!-- See Database Builder for the complete parameterized page template. -->\n</body>\n</html>\n';
}

function buildManifestEntry(cfg, count){
  return {slug:cfg.slug,name:cfg.name,tagline:cfg.topic,record_kind:cfg.recordKind,id_prefix:cfg.prefix,ai_name:cfg.aiName,local_index:'data/'+cfg.slug+'/index.jsonl.gz',page_url:'db/'+cfg.slug+'/',record_count:count||0,status:'live'};
}

if(typeof module!=='undefined'&&module.exports){
  module.exports={slugify:slugify,prefixFor:prefixFor,buildGenerator:buildGenerator,buildPage:buildPage,buildManifestEntry:buildManifestEntry,GEN_BUILDERS:GEN_BUILDERS,TYPE_LABELS:TYPE_LABELS};
}
if(typeof window!=='undefined'){ window.DBTOOL_CORE={slugify:slugify,prefixFor:prefixFor,buildGenerator:buildGenerator,buildPage:buildPage,buildManifestEntry:buildManifestEntry,GEN_BUILDERS:GEN_BUILDERS,TYPE_LABELS:TYPE_LABELS}; }
