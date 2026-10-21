(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["spatial", "temporal", "performance", "production", "editing"];
var PREFIX='JAH-VCSC-';
var USE="Used by directors, editors, script supervisors, and VFX teams to keep audiences immersed.";
var FLD=[["rule", "Rule"], ["purpose", "Purpose"], ["break_symptom", "Break symptom"]];
var DEMO="# {title} - axis side check (python3)\na={d1}\nb={d2}\ntol={d3}\nsame_side=(a < 180) == (b < 180)\nwithin=abs(a-b) <= tol\nprint(\"shot A: %.0f deg, shot B: %.0f deg\" % (a, b))\nprint(\"AXIS KEPT\" if same_side and within else \"AXIS CROSSED - reshoot or flip\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["spatial", "180-Degree Rule", "Keeps the camera on one side of the action axis so screen direction stays consistent.", "180-Degree Rule", "spatial orientation", "characters appear to swap sides", "45", "50", "30"], ["temporal", "Match on Action", "Cuts mid-gesture so motion carries across the edit, hiding the cut.", "Match on Action", "invisible edits", "jarring jump", "120", "135", "45"], ["performance", "Eyeline Match", "Shows what a character looks at next, aligning gaze direction across the cut.", "Eyeline Match", "subjective clarity", "confused looking", "80", "95", "40"], ["production", "30-Degree Rule", "Requires at least 30 degrees of camera angle change between similar shots.", "30-Degree Rule", "cut motivation", "jump cut feel", "60", "100", "50"], ["editing", "Shot-Reverse-Shot", "Alternates over-shoulder framings in dialogue to preserve spatial logic.", "Shot-Reverse-Shot", "conversation clarity", "disoriented dialogue", "70", "110", "45"], ["spatial", "Establishing Shot", "Opens a scene with a wide that maps the geography before going close.", "Establishing Shot", "orientation", "lost audience", "10", "15", "20"], ["temporal", "Screen Direction", "Keeps moving subjects traveling the same screen direction across cuts.", "Screen Direction", "motion continuity", "reversed travel", "90", "95", "35"], ["performance", "Match Cut", "Joins two shots on a graphic or action similarity for poetic transitions.", "Match Cut", "thematic link", "random cut", "30", "35", "25"], ["production", "Temporal Continuity", "Keeps time flowing consistently; clocks, shadows, and phones agree across coverage.", "Temporal Continuity", "time logic", "impossible timeline", "14", "14", "5"], ["editing", "Prop Continuity", "Tracks every prop's position and state so objects do not teleport between shots.", "Prop Continuity", "object logic", "vanishing props", "3", "3", "2"], ["spatial", "Wardrobe Continuity", "Logs costumes down to buttons so actors match across shooting days.", "Wardrobe Continuity", "character logic", "changed outfit", "2", "2", "1"], ["temporal", "Lighting Continuity", "Matches key direction, color, and ratio so coverage cuts together.", "Lighting Continuity", "visual logic", "shifting shadows", "3200", "3200", "200"], ["performance", "Weather Continuity", "Keeps skies and ground wetness consistent within a scene shot over days.", "Weather Continuity", "world logic", "sun then rain", "1", "1", "0"], ["production", "Sound Bridge", "Carries audio across a visual cut to smooth the transition.", "Sound Bridge", "flow", "abrupt cut", "0", "2", "1"], ["editing", "Graphic Match", "Aligns shapes or colors across the cut for a designed visual rhyme.", "Graphic Match", "style", "clash", "45", "50", "20"], ["spatial", "Axial Cut", "Moves the camera along the lens axis for punch-ins without angle change.", "Axial Cut", "emphasis", "flat cut", "85", "70", "30"], ["temporal", "Cross-cutting Rhythm", "Balances parallel action so tension builds evenly across storylines.", "Cross-cutting Rhythm", "pacing", "lopsided tension", "4", "4", "2"], ["performance", "Point-of-View Consistency", "Keeps POV shots honest: the audience sees only what the character could see.", "Point-of-View Consistency", "subjectivity", "cheating POV", "75", "80", "30"], ["production", "Set Dressing Continuity", "Photographs every set detail so redressing matches after company moves.", "Set Dressing Continuity", "world logic", "moved furniture", "12", "12", "3"], ["editing", "Performance Energy Match", "Matches emotional intensity across takes so the scene arcs correctly.", "Performance Energy Match", "drama", "flat scene", "7", "8", "3"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-video-continuity-and-scene-consistency-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-continuity-and-scene-consistency',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
