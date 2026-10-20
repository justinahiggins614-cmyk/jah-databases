(function(){'use strict';
/* The CompuServe Signature Database generator — jahdb-internet-history-compuserve-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = fact-checked public record; src:"signature" = Manon's original
   reconstruction, clearly labeled Signature work, never established fact. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX="JAH-INTE-SIG-";
var ITEM={"name": "CompuServe", "era": "1979–2009", "origin": "CompuServe (H&R Block)", "facts": ["1979's commercial online: forums, email, and $12/hour — the professionals' network.", "The CB simulator (1980) was the first online chat; GIF was invented here (1987).", "AOL bought it (1997); the classic service ended 2009."], "specs": {"Rate": "$12/hour (1980s)", "Famous": "CB simulator, GIF"}, "models": ["CompuServe (1979)"], "cat": "Early Internet and Online History"};
var SRC="signature";
var KINDS=["overview", "definition", "history-origins", "how-it-works", "components-anatomy", "specifications", "notable-models", "timeline", "key-figures", "glossary", "cultural-impact", "collecting-preservation", "restoration-guide", "museums-collections", "teaching-simple", "teaching-compounded", "teaching-complex", "code-demo", "related-technologies", "quiz", "specifications-deep", "variants-lineage", "faq", "provenance-methodology"];
function build(kind,seed,topic){
  var r=prng(seed), item=ITEM;
  var f=item.facts[(r()*item.facts.length)|0]||'';
  var m=item.models[(r()*item.models.length)|0]||'';
  var skeys=Object.keys(item.specs), sk=skeys.length?skeys[(r()*skeys.length)|0]:'';
  var spec=sk?(' '+sk+': '+item.specs[sk]+'.'):'';
  var body='';
  if(kind==='overview')body=item.name+' ('+item.era+', '+item.origin+') — '+f+spec+' Notable: '+m+'. Topic angle: '+topic+'.';
  else if(kind==='definition')body='Definition: '+f+' The '+item.name+' is a '+item.cat+' of the '+item.era+' era.';
  else if(kind==='history-origins')body='History: originating with '+item.origin+' in the '+item.era+' era. '+f;
  else if(kind==='how-it-works')body='Working principle of the '+item.name+': '+f+spec;
  else if(kind==='components-anatomy')body='Anatomy of the '+item.name+': '+m+'. Key spec —'+spec;
  else if(kind==='specifications')body='Specifications of the '+item.name+': '+Object.keys(item.specs).map(function(k){return k+': '+item.specs[k];}).join('; ')+'.';
  else if(kind==='notable-models')body='Notable model: '+m+' — '+f;
  else if(kind==='timeline')body='Timeline note: '+item.name+' ('+item.era+') — '+f;
  else if(kind==='key-figures')body='Key figure: '+item.origin+' — '+f;
  else if(kind==='glossary')body='Term in focus: '+sk+'. '+f;
  else if(kind==='cultural-impact')body='Cultural note: '+f;
  else if(kind==='collecting-preservation')body='Collecting the '+item.name+': '+m+'. '+f;
  else if(kind==='restoration-guide')body='Restoring the '+item.name+': document first, stabilize, repair before replacing. '+f;
  else if(kind==='museums-collections')body='See a '+item.name+' in person: '+f;
  else if(kind==='teaching-simple')body='Simply put: '+f;
  else if(kind==='teaching-compounded')body='In context: '+f+spec;
  else if(kind==='teaching-complex')body='Engineering view of the '+item.name+': '+Object.keys(item.specs).map(function(k){return k+': '+item.specs[k];}).join('; ')+'. '+f;
  else if(kind==='code-demo')body='Program demo modeling the '+item.name+'. '+f;
  else if(kind==='related-technologies')body='Related to the '+item.name+': '+m+'. '+f;
  else if(kind==='quiz')body='Quiz — '+f+' Answer: '+spec;
  else if(kind==='specifications-deep')body='Deep specs of the '+item.name+': '+Object.keys(item.specs).map(function(k){return k+': '+item.specs[k];}).join('; ')+'.';
  else if(kind==='variants-lineage')body='Variant: '+m+' of the '+item.name+'. '+f;
  else if(kind==='faq')body='FAQ: '+f;
  else body='Provenance: '+item.name+' ('+item.era+', '+item.origin+'). '+f;
  if(SRC==='signature')body='[Signature reconstruction — Manon\u2019s original take, not established fact.] '+body;
  return body;
}
function generate(seed,opts){
  opts=opts||{};var topic=String(opts.topic||'a new angle');
  var kind=KINDS[((seed-1)%KINDS.length+KINDS.length)%KINDS.length];
  var id=PREFIX+pad(seed);
  var body=build(kind,seed,topic);
  return {id:id,title:ITEM.name+' — '+kind+' #'+seed,description:body.slice(0,220),
    kind:kind,ladder:1,body:body,src:SRC,_seed:seed,
    content_completeness:'full'};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.body||r.body.length<60)errs.push('body too short');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator("internet-history-compuserve-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
