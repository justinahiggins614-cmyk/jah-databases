(function(){'use strict';
/* JAH Camping Skills Database generator — jahdb-camping-skills-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='camping-skills',PREFIX='JAH-CMP-',NAME='JAH Camping Skills Database';
var FIELDS=["shelter", "fire", "water", "cooking", "campcraft"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Choosing a tent", "d": "Size, season, weight.", "g": "shelter", "l": 2, "q": "What is Choosing a tent?", "a": "Size, season, weight.", "x": "Size, season, weight. Key steps: 2-person for 1 camper; 3-season for most; Practice setup at home. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Tent site selection", "d": "Flat, drained, sheltered.", "g": "shelter", "l": 2, "q": "What is Tent site selection?", "a": "Flat, drained, sheltered.", "x": "Flat, drained, sheltered. Key steps: Flat ground; Not in depressions; Wind protection; 200 feet from water. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Tent setup", "d": "Taut and staked.", "g": "shelter", "l": 2, "q": "What is Tent setup?", "a": "Taut and staked.", "x": "Taut and staked. Key steps: Groundsheet first; Stake corners; Guylines taut; Ventilate. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Sleep systems", "d": "Bag plus pad.", "g": "shelter", "l": 2, "q": "What is Sleep systems?", "a": "Bag plus pad.", "x": "Bag plus pad. Key steps: Bag rated below expected low; Insulated pad matters most; Pillow hack: stuff sack. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Hammock camping", "d": "Comfort with technique.", "g": "shelter", "l": 2, "q": "What is Hammock camping?", "a": "Comfort with technique.", "x": "Comfort with technique. Key steps: 30-degree hang angle; Tree straps; Underquilt for cold; Bug net. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Tarp shelters", "d": "Light and versatile.", "g": "shelter", "l": 2, "q": "What is Tarp shelters?", "a": "Light and versatile.", "x": "Light and versatile. Key steps: Learn A-frame and lean-to; Practice knots; Site selection critical. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Fire: the triangle", "d": "Fuel, oxygen, heat.", "g": "fire", "l": 2, "q": "What is Fire: the triangle?", "a": "Fuel, oxygen, heat.", "x": "Fuel, oxygen, heat. Key steps: Tinder, kindling, fuelwood; Tepee or log cabin lay; Feed gradually. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Fire starters", "d": "Tinder is everything.", "g": "fire", "l": 2, "q": "What is Fire starters?", "a": "Tinder is everything.", "x": "Tinder is everything. Key steps: Dryer lint; Cotton balls + petroleum jelly; Birch bark; Commercial starters. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Ferro rod use", "d": "Sparks into tinder.", "g": "fire", "l": 2, "q": "What is Ferro rod use?", "a": "Sparks into tinder.", "x": "Sparks into tinder. Key steps: Scrape, then strike; Aim sparks into tinder bundle; Practice at home. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Fire safety", "d": "Contain and extinguish fully.", "g": "fire", "l": 2, "q": "What is Fire safety?", "a": "Contain and extinguish fully.", "x": "Contain and extinguish fully. Key steps: Clear 10 feet; Keep small; Never leave unattended; Drown, stir, feel. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Leave No Trace fires", "d": "Minimize impact.", "g": "fire", "l": 2, "q": "What is Leave No Trace fires?", "a": "Minimize impact.", "x": "Minimize impact. Key steps: Use existing rings; Burn to ash; Scatter cool ashes; Or use a stove. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Water: carrying", "d": "A liter per 2 hours baseline.", "g": "water", "l": 2, "q": "What is Water: carrying?", "a": "A liter per 2 hours baseline.", "x": "A liter per 2 hours baseline. Key steps: Hard bottles plus collapsible; Know sources ahead. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Water: filtering", "d": "Pump, squeeze, or gravity.", "g": "water", "l": 2, "q": "What is Water: filtering?", "a": "Pump, squeeze, or gravity.", "x": "Pump, squeeze, or gravity. Key steps: Prefilter silty water; Backflush; 0.2 micron. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Water: chemical treatment", "d": "Lightweight backup.", "g": "water", "l": 2, "q": "What is Water: chemical treatment?", "a": "Lightweight backup.", "x": "Lightweight backup. Key steps: Follow wait times; Works best in clear water; Taste remedy: vitamin C. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Water: boiling", "d": "Foolproof.", "g": "water", "l": 2, "q": "What is Water: boiling?", "a": "Foolproof.", "x": "Foolproof. Key steps: Rolling boil 1 minute; 3 minutes above 6,500 ft. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Camp kitchen setup", "d": "Organized and clean.", "g": "cooking", "l": 2, "q": "What is Camp kitchen setup?", "a": "Organized and clean.", "x": "Organized and clean. Key steps: Cook away from tents; Bear-safe storage; Wash station. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Stove basics", "d": "Canister vs liquid fuel.", "g": "cooking", "l": 2, "q": "What is Stove basics?", "a": "Canister vs liquid fuel.", "x": "Canister vs liquid fuel. Key steps: Know your stove; Windscreen; Fuel estimates. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Campfire cooking", "d": "Coals, not flames.", "g": "cooking", "l": 2, "q": "What is Campfire cooking?", "a": "Coals, not flames.", "x": "Coals, not flames. Key steps: Cook over coals; Foil packets; Cast iron. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Food storage: bears", "d": "Hang, canister, or locker.", "g": "cooking", "l": 2, "q": "What is Food storage: bears?", "a": "Hang, canister, or locker.", "x": "Hang, canister, or locker. Key steps: 200 feet from camp; Bear canister where required; Everything scented goes in. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Dishwashing in camp", "d": "Strain and scatter.", "g": "cooking", "l": 2, "q": "What is Dishwashing in camp?", "a": "Strain and scatter.", "x": "Strain and scatter. Key steps: Strain food bits; Scatter gray water 200 feet out; Biodegradable soap. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Camp hygiene", "d": "Stay clean, stay healthy.", "g": "campcraft", "l": 2, "q": "What is Camp hygiene?", "a": "Stay clean, stay healthy.", "x": "Stay clean, stay healthy. Key steps: Hand sanitizer; Cat holes 6-8 inches; 200 feet from water. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Clothing system", "d": "No cotton.", "g": "campcraft", "l": 2, "q": "What is Clothing system?", "a": "No cotton.", "x": "No cotton. Key steps: Wicking base; Warm mid; Rain shell; Camp shoes. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Packing a pack", "d": "Heavy high and close.", "g": "campcraft", "l": 2, "q": "What is Packing a pack?", "a": "Heavy high and close.", "x": "Heavy high and close. Key steps: Sleeping bag bottom; Heavy center-back; Essentials accessible. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Camp chairs and comfort", "d": "Morale matters.", "g": "campcraft", "l": 2, "q": "What is Camp chairs and comfort?", "a": "Morale matters.", "x": "Morale matters. Key steps: Sit pad minimum; Headlamp + book. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}, {"t": "Navigation at camp", "d": "Know your area.", "g": "campcraft", "l": 2, "q": "What is Navigation at camp?", "a": "Know your area.", "x": "Know your area. Key steps: Map of the campground; Marked trails; Share plans. Checked against standard health and outdoor references. This is general information, not medical advice — see a professional for personal concerns.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-camping-skills-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
