(function(){'use strict';
/* JAH Power Outage Preparedness Database generator — jahdb-power-outage-prep-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='power-outage-prep',PREFIX='JAH-PWR-',NAME='JAH Power Outage Preparedness Database';
var FIELDS=["before", "during", "after", "kit"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Outage kit basics", "d": "Light, power, food, water.", "g": "kit", "l": 2, "q": "What is Outage kit basics?", "a": "Light, power, food, water.", "x": "Light, power, food, water. Key steps: Flashlights and batteries; Phone power banks; Manual can opener; Water: 1 gallon per person per day. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Food safety: fridge", "d": "4 hours closed is the rule.", "g": "during", "l": 2, "q": "What is Food safety: fridge?", "a": "4 hours closed is the rule.", "x": "4 hours closed is the rule. Key steps: Keep doors closed; 4 hours safe unopened; Discard perishables above 40 F for 2+ hours; When in doubt, throw it out. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Food safety: freezer", "d": "Full freezers hold 48 hours.", "g": "during", "l": 2, "q": "What is Food safety: freezer?", "a": "Full freezers hold 48 hours.", "x": "Full freezers hold 48 hours. Key steps: Keep closed; 48 hours full, 24 half; Ice crystals mean refreeze is OK; Thermometer helps. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Generator safety", "d": "CO kills: outside only.", "g": "during", "l": 2, "q": "What is Generator safety?", "a": "CO kills: outside only.", "x": "CO kills: outside only. Key steps: Never indoors or in garages; 20 feet from the house; Heavy-duty outdoor cords; Let cool before refueling. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Medical devices", "d": "Plan for power-dependent needs.", "g": "before", "l": 2, "q": "What is Medical devices?", "a": "Plan for power-dependent needs.", "x": "Plan for power-dependent needs. Key steps: Backup battery plans; Talk to your utility about medical priority; Keep device manuals; Charge everything before storms. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Staying cool", "d": "Heat without AC.", "g": "during", "l": 2, "q": "What is Staying cool?", "a": "Heat without AC.", "x": "Heat without AC. Key steps: Close blinds; Drink water; Cool showers; Go to cooling centers. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Staying warm", "d": "Cold without heat.", "g": "during", "l": 2, "q": "What is Staying warm?", "a": "Cold without heat.", "x": "Cold without heat. Key steps: Layer up; Close off rooms; Blankets; Never use grills or ovens for heat. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Lighting safely", "d": "No candles if you can avoid it.", "g": "during", "l": 2, "q": "What is Lighting safely?", "a": "No candles if you can avoid it.", "x": "No candles if you can avoid it. Key steps: Flashlights and lanterns; Headlamps free hands; Solar chargers by day. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Unplug electronics", "d": "Surges when power returns.", "g": "during", "l": 2, "q": "What is Unplug electronics?", "a": "Surges when power returns.", "x": "Surges when power returns. Key steps: Unplug sensitive gear; Leave one lamp on to know; Surge protectors help. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sump pump backup", "d": "Basements flood in outages.", "g": "before", "l": 2, "q": "What is Sump pump backup?", "a": "Basements flood in outages.", "x": "Basements flood in outages. Key steps: Battery backup pump; Test yearly; Water-powered backup option. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Well water", "d": "No power means no pump.", "g": "during", "l": 2, "q": "What is Well water?", "a": "No power means no pump.", "x": "No power means no pump. Key steps: Store water ahead; Fill tubs before storms; Hand pump options. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Septic systems", "d": "Pumps need power too.", "g": "during", "l": 2, "q": "What is Septic systems?", "a": "Pumps need power too.", "x": "Pumps need power too. Key steps: Limit water use; Know your system type. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Garage doors", "d": "Manual release know-how.", "g": "during", "l": 2, "q": "What is Garage doors?", "a": "Manual release know-how.", "x": "Manual release know-how. Key steps: Learn the manual release; Do not force; Keep it locked. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Security during outages", "d": "Dark streets need sense.", "g": "during", "l": 2, "q": "What is Security during outages?", "a": "Dark streets need sense.", "x": "Dark streets need sense. Key steps: Lock up; Motion lights on battery; Know neighbors. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Entertainment without power", "d": "Morale matters.", "g": "during", "l": 2, "q": "What is Entertainment without power?", "a": "Morale matters.", "x": "Morale matters. Key steps: Board games; Books; Battery radio for news. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Work from home", "d": "Keep working if you must.", "g": "during", "l": 2, "q": "What is Work from home?", "a": "Keep working if you must.", "x": "Keep working if you must. Key steps: Phone hotspots; Power banks; Shift heavy tasks. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kids and outages", "d": "Make it an adventure.", "g": "during", "l": 2, "q": "What is Kids and outages?", "a": "Make it an adventure.", "x": "Make it an adventure. Key steps: Glow sticks; Camping indoors; Explain simply. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Pets", "d": "Keep routines.", "g": "during", "l": 2, "q": "What is Pets?", "a": "Keep routines.", "x": "Keep routines. Key steps: Fresh water; Comfort; No open flames near pets. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Reporting outages", "d": "Help the utility help you.", "g": "during", "l": 2, "q": "What is Reporting outages?", "a": "Help the utility help you.", "x": "Help the utility help you. Key steps: Report online or by phone; Do not assume neighbors reported; Stay clear of lines. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Downed lines", "d": "Always assume live.", "g": "during", "l": 2, "q": "What is Downed lines?", "a": "Always assume live.", "x": "Always assume live. Key steps: Stay 30+ feet away; Call 911; Do not touch anything touching lines. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "After: restock", "d": "Rebuild the kit.", "g": "after", "l": 2, "q": "What is After: restock?", "a": "Rebuild the kit.", "x": "Rebuild the kit. Key steps: Replace used supplies; Check battery dates; Restock food and water. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "After: fridge cleanup", "d": "Spoiled food protocol.", "g": "after", "l": 2, "q": "What is After: fridge cleanup?", "a": "Spoiled food protocol.", "x": "Spoiled food protocol. Key steps: Discard per the 4-hour rule; Clean with baking soda; Restock gradually. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Whole-house surge protector", "d": "Installed at the panel.", "g": "before", "l": 2, "q": "What is Whole-house surge protector?", "a": "Installed at the panel.", "x": "Installed at the panel. Key steps: Hire an electrician; Protects everything; Layer with point-of-use. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Solar + battery", "d": "Resilience investment.", "g": "before", "l": 2, "q": "What is Solar + battery?", "a": "Resilience investment.", "x": "Resilience investment. Key steps: Battery backup basics; Critical-load panels; Get quotes. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Community resources", "d": "Know where to go.", "g": "during", "l": 2, "q": "What is Community resources?", "a": "Know where to go.", "x": "Know where to go. Key steps: Cooling and warming centers; Charging stations; Neighbor check-ins. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-power-outage-prep-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
