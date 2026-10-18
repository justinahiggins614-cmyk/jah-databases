(function(){'use strict';
/* JAH The Main Character Energy Database generator — jahdb-gen-main-character-energy-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same main-character profile. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function cap(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
var PREFIX="JAH-MCE-";
var KIND="main-character profile";
var FIELDS=["Foundations","Compounded","Advanced"];
var POOLS={"title": ["The Late Bloomer", "Ctrl+Alt+Defy", "Main Street Miracle", "The Comeback Tour", "Neon Horizons", "The Plot Thickens", "Second Act Energy", "The Wild Card", "Golden Hour", "The Underdog Uprising", "Paper Planes", "Static & Stardust", "The Slow Climb", "Electric Daydream", "The Kind Rebellion", "Chasing Daylight", "The Standing Start", "Velvet Revolution", "The Lucky Break", "Analog Heart", "The Great Pivot", "Sunrise Industry", "The Bold Hello", "Miracle on Main Street", "The Encore Kid", "Static Bloom Energy", "The Grand Gesture", "Paper Moon Rising", "The Joyride", "Halftime Hero", "The Plot Armor", "Golden Reel", "The Silver Lining Tour", "Day One Energy", "The Comeback Trail", "Neon Roots"], "scene": ["walking away from an explosion in slow motion (of confetti)", "a montage of small wins set to your favorite song", "the training sequence, but for parallel parking", "a dramatic airport run — for a flight you are early for", "the makeover scene, but it is just a great haircut", "rallying the group chat for a spontaneous adventure"], "song": ["an 80s power ballad", "a lo-fi victory lap", "orchestral swells", "a pop anthem at full volume", "acoustic guitar sunrise", "synthwave at midnight"]};
var STEPS=[{"do": "pick", "bank": "title", "var": "title"}, {"do": "pick", "bank": "scene", "var": "scene"}, {"do": "pick", "bank": "song", "var": "song"}];
var ARTIFACT="{title}";
var BLURB="Your starring-role snapshot: the movie title of your life right now.";
var HOW="The generator draws a movie title, a signature scene, and a soundtrack cue from three banks with the seeded PRNG.";
var LABELS={"title": "Movie title", "scene": "Signature scene", "song": "Soundtrack cue"};
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
var gen={version:'jahdb-gen-main-character-energy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,kind:KIND};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-main-character-energy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
