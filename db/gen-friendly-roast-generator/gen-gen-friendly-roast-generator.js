(function(){'use strict';
/* JAH The Friendly Roast Generator Database generator — jahdb-gen-friendly-roast-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same friendly roast. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function cap(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
var PREFIX="JAH-FRG-";
var KIND="friendly roast";
var FIELDS=["Foundations","Compounded","Advanced"];
var POOLS={"op": ["You are the human version of a warm blanket", "You have the energy of a golden retriever at a tennis ball factory", "You are proof that enthusiasm is a personality trait", "You walk into a room like you own the playlist", "You are the group chat's favorite notification", "You have main-character energy and supporting-character kindness", "You are a walking comfort-food commercial", "You collect hobbies like some people collect stamps", "You are the reason 'one more episode' was invented", "You have the confidence of someone who always finds parking"], "pu": ["and we would not have it any other way.", "and honestly, it is your best feature.", "and the group is better for it.", "and we are all just living in your sitcom.", "and your snack-sharing record proves your heart.", "and your laugh should be bottled and sold.", "and somehow you make Mondays tolerable.", "and your playlist taste is beyond question.", "and your stories deserve their own podcast.", "and being your friend is the real flex."]};
var STEPS=[{"do": "pick", "bank": "op", "var": "op"}, {"do": "pick", "bank": "pu", "var": "pu"}];
var ARTIFACT="{op} {pu}";
var BLURB="An affectionate roast: playful teasing with warmth baked in, safe for any group.";
var HOW="The generator pairs a playful opener with a warm punchline from two banks. Every roast is written to be kind-first — teasing the quirk, celebrating the person.";
var LABELS={"op": "Opener", "pu": "Punchline"};
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
var gen={version:'jahdb-gen-friendly-roast-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,kind:KIND};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-friendly-roast-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
