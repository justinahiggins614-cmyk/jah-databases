(function(){'use strict';
/* JAH Signature Personal Superpower Database generator — jahdb-gen-personal-superpower-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same superpower. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function cap(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
var PREFIX="JAH-PSPES-";
var KIND="superpower";
var FIELDS=["Foundations","Compounded","Advanced"];
var POOLS={"pow": ["Perfect Recall", "Calm Field", "Snack Summoning", "Time Bubble", "Animal Chatter", "Instant Cozy", "Lucky Timing", "Idea Spark", "Mood Lift", "Plant Whisper", "Dream Weaving", "Storm Calm", "Perfect Parallel Parking", "Infinite Phone Battery", "Mosquito Repel", "Always-Find-It", "Speed Read", "Nap Anywhere", "Green Thumb Burst", "Crowd Calm", "Lost & Found Sense", "Recipe Improv", "Traffic Dodge", "Queue Skip (karma-safe)", "Plant Revival", "Baby Soothe", "Dog Whisper", "Perfect Gift Pick", "Spill Immunity", "Alarm Harmony", "Wi-Fi Whisper", "Umbrella Timing", "Sunscreen Memory", "Key Finder", "Name Recall", "Direction Sense", "Echo Location (Social)", "Perfect Pitch (Life)", "Infinite Patience", "Gravity Sass", "Probability Nudge", "Ember Heart"], "dom": ["memory and learning", "rooms and gatherings", "kitchens everywhere", "deadlines and schedules", "pets and wildlife", "blankets and reading nooks", "traffic and queues", "brainstorms", "group chats", "gardens", "sleep and stories", "rainy days", "friendships", "music and rhythm", "long lines", "sports", "dice games", "campfires"], "lim": ["only works when you are genuinely helping someone", "needs a 10-minute nap to recharge", "fails hilariously on Mondays", "only works within 100 feet of snacks", "requires you to narrate what you are doing", "switches off when you brag about it", "only works on days ending in Y", "requires a dramatic entrance", "drains your phone battery instead"]};
var STEPS=[{"do": "pick", "bank": "pow", "var": "pow"}, {"do": "pick", "bank": "dom", "var": "dom"}, {"do": "pick", "bank": "lim", "var": "lim"}];
var ARTIFACT="{pow}";
var BLURB="A personal superpower with its domain and its one keeping-it-interesting limit.";
var HOW="The generator draws a power name, the domain it rules, and one fun limit from three banks using the seeded PRNG.";
var LABELS={"pow": "Power name", "dom": "Domain", "lim": "Limit"};
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
var gen={version:'jahdb-gen-personal-superpower-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,kind:KIND};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-personal-superpower-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
