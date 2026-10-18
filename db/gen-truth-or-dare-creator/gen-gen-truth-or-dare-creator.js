(function(){'use strict';
/* JAH The Truth or Dare Creator generator — jahdb-gen-truth-or-dare-creator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same truth-or-dare card. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function cap(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
var PREFIX="JAH-TODC-";
var KIND="truth-or-dare card";
var FIELDS=["Foundations","Compounded","Advanced"];
var POOLS={"td": ["truth", "dare"], "truth": ["What is the silliest thing you believed as a kid?", "What is your most embarrassing autocorrect fail?", "What is a secret talent nobody here knows about?", "What is the weirdest dream you remember?", "What is your most unpopular (kind) food opinion?", "What is the funniest thing that happened to you this month?", "What is a song you secretly love?", "What is your biggest (silly) fear?", "What is the bravest small thing you have done?", "What is a compliment you have never forgotten?", "What is the strangest food combination you enjoy?", "What is a movie you can quote from start to finish?", "What is the most spontaneous thing you have done?", "What is a skill you wish you had?", "What is your favorite memory from last year?", "What is the best gift you have ever given?", "What is something you are looking forward to?", "What is the funniest joke you know by heart?", "What is a habit you are proud of?", "What is the coolest place you have visited?", "What is your favorite way to spend a rainy day?", "What is something you learned recently?", "What is the best compliment you have given?", "What is a small win from this week?"], "dare": ["Do your best robot dance for 30 seconds.", "Speak in a pirate accent until your next turn.", "Do 10 jumping jacks while naming your favorite foods.", "Draw a portrait of the player to your left in 60 seconds.", "Do an impression of a GPS giving directions.", "Sing the alphabet as an opera singer.", "Do your best superhero landing pose and hold it.", "Tell a joke in slow motion.", "Do a dramatic reading of a snack label.", "Hop on one foot while reciting the alphabet backwards (try!).", "Do your best impression of a nature documentary narrator.", "Balance a book on your head and walk across the room.", "Do 5 push-ups while the group counts in a silly voice.", "Pretend to be a statue and let the group pose you.", "Do a runway walk like a fashion model.", "Sing your favorite song in a whisper.", "Do an impression of your favorite cartoon character.", "Act out a movie scene without words; the group guesses.", "Do a silly walk to the door and back.", "Compliment every player in a different accent.", "Do your best magic trick (real or invented).", "Lead the group in a 30-second dance party.", "Tell a story using only sound effects.", "Do an impression of a sleepy cat waking up."]};
var STEPS=[{"do": "pick", "bank": "td", "var": "td"}, {"do": "pickvar", "bankvar": "td", "var": "text"}];
var ARTIFACT="{td}: {text}";
var BLURB="A clean, opt-in truth question or dare challenge, ready to play.";
var HOW="The generator flips a seeded coin for truth or dare, then draws from that bank. Every card is all-ages, voluntary, and pass-friendly by construction.";
var LABELS={"td": "Card type", "text": "Card text"};
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
var gen={version:'jahdb-gen-truth-or-dare-creator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,kind:KIND};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-truth-or-dare-creator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
