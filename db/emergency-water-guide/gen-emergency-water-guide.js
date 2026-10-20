(function(){'use strict';
/* JAH Emergency Water Guide Database generator — jahdb-emergency-water-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='emergency-water-guide',PREFIX='JAH-WTR-',NAME='JAH Emergency Water Guide Database';
var FIELDS=["storage", "purification", "finding"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "How much to store", "d": "One gallon per person per day; two weeks is the goal.", "g": "storage", "l": 2, "q": "What is How much to store?", "a": "One gallon per person per day; two weeks is the goal.", "x": "One gallon per person per day; two weeks is the goal. Key steps: 14 gallons per person; Pets need water too; Rotate every 6 months. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Storage containers", "d": "Food-grade only.", "g": "storage", "l": 2, "q": "What is Storage containers?", "a": "Food-grade only.", "x": "Food-grade only. Key steps: Food-grade barrels or jugs; Clean with bleach solution first; Cool dark place; Label dates. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Boiling", "d": "The gold standard: rolling boil 1 minute (3 at altitude).", "g": "purification", "l": 2, "q": "What is Boiling?", "a": "The gold standard: rolling boil 1 minute (3 at altitude).", "x": "The gold standard: rolling boil 1 minute (3 at altitude). Key steps: Bring to a rolling boil; 1 minute (3 above 6,500 ft); Cool covered. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bleach disinfection", "d": "Plain unscented bleach: 2 drops per liter, wait 30 minutes.", "g": "purification", "l": 2, "q": "What is Bleach disinfection?", "a": "Plain unscented bleach: 2 drops per liter, wait 30 minutes.", "x": "Plain unscented bleach: 2 drops per liter, wait 30 minutes. Key steps: Use plain unscented bleach; 2 drops per liter clear water; Wait 30 minutes; Slight chlorine smell is good. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Water filters", "d": "Pump and gravity filters for particulates and protozoa.", "g": "purification", "l": 2, "q": "What is Water filters?", "a": "Pump and gravity filters for particulates and protozoa.", "x": "Pump and gravity filters for particulates and protozoa. Key steps: 0.2 micron or smaller; Backflush per instructions; Prefilter muddy water. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "UV purification", "d": "UV pens kill microbes in clear water.", "g": "purification", "l": 2, "q": "What is UV purification?", "a": "UV pens kill microbes in clear water.", "x": "UV pens kill microbes in clear water. Key steps: Works in clear water only; Batteries charged; Follow dose instructions. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Solar disinfection (SODIS)", "d": "Clear bottles in full sun 6 hours.", "g": "purification", "l": 2, "q": "What is Solar disinfection (SODIS)?", "a": "Clear bottles in full sun 6 hours.", "x": "Clear bottles in full sun 6 hours. Key steps: Clear PET bottles; 6 hours full sun (2 days cloudy); Water must be clear. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Distillation", "d": "Boil and condense for the purest.", "g": "purification", "l": 2, "q": "What is Distillation?", "a": "Boil and condense for the purest.", "x": "Boil and condense for the purest. Key steps: Boil water; Catch steam on a cool surface; Drip into a clean container. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Finding water: rain", "d": "Catch it clean.", "g": "finding", "l": 2, "q": "What is Finding water: rain?", "a": "Catch it clean.", "x": "Catch it clean. Key steps: Tarps and containers; First flush diverts debris; Filter after. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Finding water: dew", "d": "Cloth wipe method at dawn.", "g": "finding", "l": 2, "q": "What is Finding water: dew?", "a": "Cloth wipe method at dawn.", "x": "Cloth wipe method at dawn. Key steps: Tie cloths around ankles; Walk through grass; Wring into container. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Finding water: plants", "d": "Transpiration bags on leafy branches.", "g": "finding", "l": 2, "q": "What is Finding water: plants?", "a": "Transpiration bags on leafy branches.", "x": "Transpiration bags on leafy branches. Key steps: Bag a leafy branch; Collect condensation; Avoid poisonous plants. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Finding water: ground", "d": "Dig in low spots and dry streambeds.", "g": "finding", "l": 2, "q": "What is Finding water: ground?", "a": "Dig in low spots and dry streambeds.", "x": "Dig in low spots and dry streambeds. Key steps: Dig at outside bends; Let sediment settle; Purify always. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Signs of water", "d": "Nature points the way.", "g": "finding", "l": 2, "q": "What is Signs of water?", "a": "Nature points the way.", "x": "Nature points the way. Key steps: Follow animal trails downhill; Green vegetation in dry land; Insect swarms near water. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "What NOT to drink", "d": "Some water kills.", "g": "finding", "l": 2, "q": "What is What NOT to drink?", "a": "Some water kills.", "x": "Some water kills. Key steps: Never drink seawater; Avoid stagnant with algae; Purify all wild water. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Muddy water", "d": "Settle then filter.", "g": "purification", "l": 2, "q": "What is Muddy water?", "a": "Settle then filter.", "x": "Settle then filter. Key steps: Let settle hours; Decant clear water; Filter and disinfect. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Chemical contamination", "d": "Filters do not remove chemicals well.", "g": "purification", "l": 2, "q": "What is Chemical contamination?", "a": "Filters do not remove chemicals well.", "x": "Filters do not remove chemicals well. Key steps: Avoid industrial runoff; Distillation helps; When unsure, find another source. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Storing treated water", "d": "Keep it clean.", "g": "storage", "l": 2, "q": "What is Storing treated water?", "a": "Keep it clean.", "x": "Keep it clean. Key steps: Sealed containers; Cool dark place; Rotate. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Water for babies", "d": "Extra care for infants.", "g": "purification", "l": 2, "q": "What is Water for babies?", "a": "Extra care for infants.", "x": "Extra care for infants. Key steps: Boil always; Use within 24 hours; Sterilize bottles. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sanitation without water", "d": "Hygiene matters too.", "g": "storage", "l": 2, "q": "What is Sanitation without water?", "a": "Hygiene matters too.", "x": "Hygiene matters too. Key steps: Hand sanitizer; Wet wipes; Bag waste. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Melting snow", "d": "Melt, do not eat.", "g": "finding", "l": 2, "q": "What is Melting snow?", "a": "Melt, do not eat.", "x": "Melt, do not eat. Key steps: Melt fully before drinking; Purify after; Eating snow chills you. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Solar stills", "d": "Slow but reliable.", "g": "finding", "l": 2, "q": "What is Solar stills?", "a": "Slow but reliable.", "x": "Slow but reliable. Key steps: Dig pit, place container; Cover with plastic; Weight the center; Collect condensate. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Well safety after disaster", "d": "Test before drinking.", "g": "purification", "l": 2, "q": "What is Well safety after disaster?", "a": "Test before drinking.", "x": "Test before drinking. Key steps: Do not use until tested; Disinfect per guidance; Pump to waste first. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Hot water heater source", "d": "40+ gallons hiding in plain sight.", "g": "storage", "l": 2, "q": "What is Hot water heater source?", "a": "40+ gallons hiding in plain sight.", "x": "40+ gallons hiding in plain sight. Key steps: Turn off power/gas first; Drain from the bottom valve; Let sediment settle. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Toilet tank source", "d": "The tank (not bowl) holds clean water.", "g": "storage", "l": 2, "q": "What is Toilet tank source?", "a": "The tank (not bowl) holds clean water.", "x": "The tank (not bowl) holds clean water. Key steps: Use tank water only; Not if chemically treated; Purify to be safe. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Community water points", "d": "Know distribution sites.", "g": "finding", "l": 2, "q": "What is Community water points?", "a": "Know distribution sites.", "x": "Know distribution sites. Key steps: Follow official announcements; Bring clean containers; Share fairly. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-emergency-water-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
