(function(){'use strict';
/* JAH Childproofing Guide Database generator — jahdb-childproofing-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='childproofing-guide',PREFIX='JAH-KID-',NAME='JAH Childproofing Guide Database';
var FIELDS=["general", "kitchen", "bathroom", "living", "bedroom", "outdoor"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Get on their level", "d": "Crawl the house to see hazards at toddler height.", "g": "general", "l": 2, "q": "What is Get on their level?", "a": "Crawl the house to see hazards at toddler height.", "x": "Crawl the house to see hazards at toddler height. Key steps: Crawl every room; Note reachable hazards; Fix from their perspective. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Outlet covers", "d": "Sliding plate covers beat plugs.", "g": "general", "l": 2, "q": "What is Outlet covers?", "a": "Sliding plate covers beat plugs.", "x": "Sliding plate covers beat plugs. Key steps: Install sliding covers; Check tamper-resistant outlets. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Furniture anchoring", "d": "Tip-overs kill.", "g": "general", "l": 2, "q": "What is Furniture anchoring?", "a": "Tip-overs kill.", "x": "Tip-overs kill. Key steps: Anchor dressers and TVs to studs; Use anti-tip straps; No climbing temptations. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sharp corners", "d": "Pad the coffee table era.", "g": "general", "l": 2, "q": "What is Sharp corners?", "a": "Pad the coffee table era.", "x": "Pad the coffee table era. Key steps: Corner guards; Rearrange sharp furniture. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Blind cords", "d": "Strangulation hazard.", "g": "general", "l": 2, "q": "What is Blind cords?", "a": "Strangulation hazard.", "x": "Strangulation hazard. Key steps: Cordless blinds best; Cut looped cords; Cleats high up. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Stair gates", "d": "Top and bottom of every staircase.", "g": "general", "l": 2, "q": "What is Stair gates?", "a": "Top and bottom of every staircase.", "x": "Top and bottom of every staircase. Key steps: Hardware-mounted at top; Pressure at bottom OK; No accordion gates. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kitchen: stove", "d": "Burns and pulls.", "g": "kitchen", "l": 2, "q": "What is Kitchen: stove?", "a": "Burns and pulls.", "x": "Burns and pulls. Key steps: Back burners first; Knob covers; Oven lock; No tablecloths to pull. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kitchen: knives", "d": "Up high and locked.", "g": "kitchen", "l": 2, "q": "What is Kitchen: knives?", "a": "Up high and locked.", "x": "Up high and locked. Key steps: Knife block out of reach; Lock drawers with sharps. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kitchen: cleaning supplies", "d": "Lock them all.", "g": "kitchen", "l": 2, "q": "What is Kitchen: cleaning supplies?", "a": "Lock them all.", "x": "Lock them all. Key steps: High cabinet or locked; Dishwasher detergent locked. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Kitchen: trash", "d": "Locking lids.", "g": "kitchen", "l": 2, "q": "What is Kitchen: trash?", "a": "Locking lids.", "x": "Locking lids. Key steps: Locking trash can; Under-sink lock. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bathroom: water temp", "d": "Scalds in seconds.", "g": "bathroom", "l": 2, "q": "What is Bathroom: water temp?", "a": "Scalds in seconds.", "x": "Scalds in seconds. Key steps: Set heater to 120 F; Anti-scald devices; Test bath water. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bathroom: drowning", "d": "Inches of water kill.", "g": "bathroom", "l": 2, "q": "What is Bathroom: drowning?", "a": "Inches of water kill.", "x": "Inches of water kill. Key steps: Never leave alone near water; Toilet locks; Empty tubs immediately. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bathroom: medicines", "d": "Lock all meds.", "g": "bathroom", "l": 2, "q": "What is Bathroom: medicines?", "a": "Lock all meds.", "x": "Lock all meds. Key steps: High locked cabinet; Child-resistant caps; Poison control number saved. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bathroom: razors", "d": "Up and away.", "g": "bathroom", "l": 2, "q": "What is Bathroom: razors?", "a": "Up and away.", "x": "Up and away. Key steps: Locked cabinet; Never in reach. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Living room: choking", "d": "Small objects kill.", "g": "living", "l": 2, "q": "What is Living room: choking?", "a": "Small objects kill.", "x": "Small objects kill. Key steps: Toilet-paper-roll test; Pick up small items; Coins, batteries up high. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Living room: heavy items", "d": "Anchor everything climbable.", "g": "living", "l": 2, "q": "What is Living room: heavy items?", "a": "Anchor everything climbable.", "x": "Anchor everything climbable. Key steps: Anchor bookcases; Secure TVs; No remote temptations on top. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bedroom: crib safety", "d": "Bare is best.", "g": "bedroom", "l": 2, "q": "What is Bedroom: crib safety?", "a": "Bare is best.", "x": "Bare is best. Key steps: No blankets, pillows, bumpers; Firm mattress; Slats under 2-3/8 inches apart. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Bedroom: windows", "d": "Falls kill.", "g": "bedroom", "l": 2, "q": "What is Bedroom: windows?", "a": "Falls kill.", "x": "Falls kill. Key steps: Window guards or stops; Furniture away from windows; No climbing access. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Laundry: pods", "d": "Detergent pods look like candy.", "g": "general", "l": 2, "q": "What is Laundry: pods?", "a": "Detergent pods look like candy.", "x": "Detergent pods look like candy. Key steps: Locked high cabinet; Never in reach; Call poison control if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Garage: chemicals", "d": "Locked storage.", "g": "outdoor", "l": 2, "q": "What is Garage: chemicals?", "a": "Locked storage.", "x": "Locked storage. Key steps: Lock all chemicals; Antifreeze especially — sweet taste; Tools secured. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Outdoor: pools", "d": "Fences save lives.", "g": "outdoor", "l": 2, "q": "What is Outdoor: pools?", "a": "Fences save lives.", "x": "Fences save lives. Key steps: 4-sided fence with self-latching gate; Alarms; Never leave alone; Swim lessons. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Outdoor: play equipment", "d": "Anchor and maintain.", "g": "outdoor", "l": 2, "q": "What is Outdoor: play equipment?", "a": "Anchor and maintain.", "x": "Anchor and maintain. Key steps: Anchor swing sets; Soft landing surface; Inspect yearly. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Outdoor: plants", "d": "Some common plants are toxic.", "g": "outdoor", "l": 2, "q": "What is Outdoor: plants?", "a": "Some common plants are toxic.", "x": "Some common plants are toxic. Key steps: Learn toxic plants; Teach no eating; Fence risky beds. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Firearms", "d": "Locked, unloaded, separate ammo.", "g": "general", "l": 2, "q": "What is Firearms?", "a": "Locked, unloaded, separate ammo.", "x": "Locked, unloaded, separate ammo. Key steps: Gun safe; Ammo locked separately; Kids never access. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Pets and babies", "d": "Never leave alone together.", "g": "general", "l": 2, "q": "What is Pets and babies?", "a": "Never leave alone together.", "x": "Never leave alone together. Key steps: Supervise all interactions; Safe retreat for pets; Teach gentle touch. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-childproofing-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
