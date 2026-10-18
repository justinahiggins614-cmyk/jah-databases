(function(){'use strict';
/* JAH The Personal Motto Database generator — jahdb-gen-personal-motto-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same motto. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function cap(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
var PREFIX="JAH-PMPE-";
var KIND="motto";
var FIELDS=["Foundations","Compounded","Advanced"];
var POOLS={"v": ["Kindness", "Courage", "Curiosity", "Patience", "Joy", "Honesty", "Grit", "Wonder", "Loyalty", "Calm"], "a": ["show up", "begin anyway", "ask better questions", "rest without guilt", "laugh loudly", "help first", "learn one thing", "keep going"], "e": ["every single day.", "especially on hard days.", "and mean it.", "one step at a time.", "with a full heart.", "no exceptions."]};
var STEPS=[{"do": "pick", "bank": "v", "var": "v"}, {"do": "pick", "bank": "a", "var": "a"}, {"do": "pick", "bank": "e", "var": "e"}];
var ARTIFACT="{v}: {a} {e}";
var BLURB="A personal motto: the line you live by, composed from a value and an action.";
var HOW="The generator draws a core value, a daily action, and a closing resolve from three banks, then composes the motto with the seeded PRNG.";
var LABELS={"v": "Core value", "a": "Daily action", "e": "Resolve"};
function resolveArt(V){var art=ARTIFACT,prev=null,n=0;while(art!==prev&&n<4){prev=art;n++;art=art.replace(/\{(\w+)\}/g,function(m,k){return V[k]!=null?V[k]:m;});}return art;}
function buildArtifact(seed){
  var rnd=prng(seed>>>0),V={};
  STEPS.forEach(function(st){
    var v;
    if(st.do==='pick'){v=pick(POOLS[st.bank],rnd);if(st.cap)v=cap(v);if(st.upper)v=v.toUpperCase();if(st.lower)v=v.toLowerCase();V[st.var]=v;}
    else if(st.do==='pickvar'){v=pick(POOLS[V[st.bankvar]],rnd);if(st.cap)v=cap(v);if(st.upper)v=v.toUpperCase();V[st.var]=v;}
    else if(st.do==='int'){v=String(st.min+((rnd()*(st.max-st.min+1))|0));V[st.var]=v;}
    else if(st.do==='lit'){V[st.var]=st.val;}
    else if(st.do==='maybe'){if(rnd()<st.p){v=pick(POOLS[st.bank],rnd);if(st.cap)v=cap(v);V[st.var]=v;}else{V[st.var]=st.other||'';}}
  });
  return {artifact:resolveArt(V),vars:V};
}
function describe(V){
  return STEPS.map(function(st){var lab=LABELS[st.var]||st.var;return lab+': '+(V[st.var]==null?'':V[st.var]);}).join(' | ');
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:FIELDS[s%3];
  var b=buildArtifact(s);
  var id=PREFIX+String(s%1000000).padStart(6,'0');
  return {
    id:id,name:b.artifact,title:b.artifact,
    description:'GENERATED '+KIND.toUpperCase()+' (seed '+s+'). '+BLURB+' Built from \u2014 '+describe(b.vars)+'.',
    field:field,src:'signature',sample:true,kind:KIND,
    recipe:b.vars,seed:s,how_built:HOW,
    disclaimer:'Generated sample \u2014 not an archive record. Seeded generator outputs are labeled samples, never presented as archive records.',
    _seed:s
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.name)e.push('name');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate artifact+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-personal-motto-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,kind:KIND};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-personal-motto',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
