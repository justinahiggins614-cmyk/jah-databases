(function(){'use strict';
/* JAH The Who Knows Who Best Database generator — jahdb-gen-who-knows-who-best-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same quiz question. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function cap(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
var PREFIX="JAH-WKWB-";
var KIND="quiz question";
var FIELDS=["Foundations","Compounded","Advanced"];
var POOLS={"cat": ["Favorites", "Memories", "Dreams", "Habits", "Wildcards"], "Favorites": ["What is my all-time favorite movie?", "What food could I eat every single day?", "What is my favorite season and why?", "What is my go-to karaoke song?", "What is my favorite book or comic?", "What is my favorite ice cream flavor?", "What is my favorite holiday?", "What is my favorite board game?"], "Memories": ["What is my funniest childhood memory?", "What was my first pet's name?", "What is the best trip I have ever taken?", "What is my most embarrassing moment I will admit to?", "What was my favorite subject in school?", "What is my earliest memory?", "What concert or show do I brag about?", "What is my proudest moment so far?"], "Dreams": ["What is my dream vacation?", "If I could have any job for a day, what?", "What is one thing on my bucket list?", "Where would I time travel to?", "What is my dream pet?", "What superpower would I pick?", "What would I do with a surprise day off?", "What is my dream house like?"], "Habits": ["What is my morning routine in three words?", "What is my most-used emoji?", "What is my go-to comfort show?", "What snack do I always reach for?", "What is my ideal weekend?", "Am I a morning person or night owl?", "What is my lucky number?", "What is my guilty pleasure song?"], "Wildcards": ["What would my superhero name be?", "What is something I am weirdly good at?", "What is my hottest (kind) food take?", "What would I bring to a desert island?", "What is my most-used phrase?", "What animal am I most like?", "What is my signature dance move?", "What would my autobiography be titled?"]};
var STEPS=[{"do": "pick", "bank": "cat", "var": "cat"}, {"do": "pickvar", "bankvar": "cat", "var": "q"}];
var ARTIFACT="{q}";
var BLURB="A ready-to-ask friendship quiz question with its category and scoring note.";
var HOW="The generator picks a question category, then a question from that category's bank, using the seeded PRNG — the same seed always rebuilds the same question.";
var LABELS={"cat": "Category", "q": "Question"};
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
var gen={version:'jahdb-gen-who-knows-who-best-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,kind:KIND};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-who-knows-who-best',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
