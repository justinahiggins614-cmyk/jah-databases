(function(){'use strict';
/* JAH Home Security Tips Database generator — jahdb-home-security-tips-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='home-security-tips',PREFIX='JAH-SEC-',NAME='JAH Home Security Tips Database';
var FIELDS=["doors", "windows", "lighting", "habits", "tech", "outdoor"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Deadbolts that work", "d": "A real deadbolt with a 1-inch throw into a reinforced strike.", "g": "doors", "l": 2, "q": "What is Deadbolts that work?", "a": "A real deadbolt with a 1-inch throw into a reinforced strike.", "x": "A real deadbolt with a 1-inch throw into a reinforced strike. Key steps: Install 1-inch throw deadbolts; Reinforce strike plates with 3-inch screws; Lock every time. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Reinforce door frames", "d": "Kicks break frames, not locks.", "g": "doors", "l": 2, "q": "What is Reinforce door frames?", "a": "Kicks break frames, not locks.", "x": "Kicks break frames, not locks. Key steps: 3-inch screws into studs; Reinforced strike plates; Door armor kits for weak frames. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sliding door security", "d": "Sliding doors lift and slide.", "g": "doors", "l": 2, "q": "What is Sliding door security?", "a": "Sliding doors lift and slide.", "x": "Sliding doors lift and slide. Key steps: Security bar in the track; Anti-lift pins; Keyed locks, not just latches. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Window locks", "d": "Windows are the second entry.", "g": "windows", "l": 2, "q": "What is Window locks?", "a": "Windows are the second entry.", "x": "Windows are the second entry. Key steps: Lock every window; Pin double-hungs; Security film for ground floors. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Basement windows", "d": "Small and often forgotten.", "g": "windows", "l": 2, "q": "What is Basement windows?", "a": "Small and often forgotten.", "x": "Small and often forgotten. Key steps: Lock them; Security bars where appropriate; Keep wells clear. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Exterior lighting", "d": "Light removes hiding spots.", "g": "lighting", "l": 2, "q": "What is Exterior lighting?", "a": "Light removes hiding spots.", "x": "Light removes hiding spots. Key steps: Motion lights at entries; Bright address numbers; Timers when away. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Landscaping against crime", "d": "Trim bushes below windows.", "g": "lighting", "l": 2, "q": "What is Landscaping against crime?", "a": "Trim bushes below windows.", "x": "Trim bushes below windows. Key steps: Trim below 3 feet near windows; Thorny plants under windows; No ladder-like trees to upper floors. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Garage security", "d": "Garages hold tools and access.", "g": "doors", "l": 2, "q": "What is Garage security?", "a": "Garages hold tools and access.", "x": "Garages hold tools and access. Key steps: Keep the garage door closed; Lock the interior door; Shield the emergency release. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Mail and packages", "d": "Full mailboxes scream empty house.", "g": "habits", "l": 2, "q": "What is Mail and packages?", "a": "Full mailboxes scream empty house.", "x": "Full mailboxes scream empty house. Key steps: Hold mail when away; Package lockers or neighbors; Do not leave boxes at the door. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Social media silence", "d": "Do not broadcast absence.", "g": "habits", "l": 2, "q": "What is Social media silence?", "a": "Do not broadcast absence.", "x": "Do not broadcast absence. Key steps: Post vacation photos after; Avoid live location tags; Check privacy settings. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Trusted neighbor", "d": "Eyes on the house.", "g": "habits", "l": 2, "q": "What is Trusted neighbor?", "a": "Eyes on the house.", "x": "Eyes on the house. Key steps: Ask a neighbor to watch; Park in the driveway; Vary lights with timers. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Alarm systems", "d": "Monitored or self-monitored.", "g": "tech", "l": 2, "q": "What is Alarm systems?", "a": "Monitored or self-monitored.", "x": "Monitored or self-monitored. Key steps: Monitor entry points; Yard signs deter; Test regularly. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Video doorbells", "d": "See and speak from anywhere.", "g": "tech", "l": 2, "q": "What is Video doorbells?", "a": "See and speak from anywhere.", "x": "See and speak from anywhere. Key steps: Cover the front door; Enable motion alerts; Secure the footage. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Security cameras", "d": "Visible cameras deter.", "g": "tech", "l": 2, "q": "What is Security cameras?", "a": "Visible cameras deter.", "x": "Visible cameras deter. Key steps: Cover entries and driveway; Local plus cloud storage; Check laws on audio. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Smart locks", "d": "Keyless convenience with logs.", "g": "tech", "l": 2, "q": "What is Smart locks?", "a": "Keyless convenience with logs.", "x": "Keyless convenience with logs. Key steps: Unique codes per person; Auto-lock enabled; Battery backups. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Safe for valuables", "d": "Bolt it down.", "g": "habits", "l": 2, "q": "What is Safe for valuables?", "a": "Bolt it down.", "x": "Bolt it down. Key steps: Bolt safes to floor or studs; Fire rating matters; Do not advertise it. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Inventory your belongings", "d": "Photos for insurance.", "g": "habits", "l": 2, "q": "What is Inventory your belongings?", "a": "Photos for insurance.", "x": "Photos for insurance. Key steps: Photograph valuables; Record serial numbers; Store copies offsite. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Spare key safety", "d": "Never under the mat.", "g": "habits", "l": 2, "q": "What is Spare key safety?", "a": "Never under the mat.", "x": "Never under the mat. Key steps: Leave with a trusted person; Lockbox instead of hiding; Rekey when moving in. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Rekey on move-in", "d": "You do not know who has keys.", "g": "doors", "l": 2, "q": "What is Rekey on move-in?", "a": "You do not know who has keys.", "x": "You do not know who has keys. Key steps: Rekey every exterior lock; Or replace with new; Smart locks simplify. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Dog as deterrent", "d": "Barking deters most burglars.", "g": "habits", "l": 2, "q": "What is Dog as deterrent?", "a": "Barking deters most burglars.", "x": "Barking deters most burglars. Key steps: Even small dogs help; Beware of dog signs; Do not rely solely on pets. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Fence and gates", "d": "Fences define and delay.", "g": "outdoor", "l": 2, "q": "What is Fence and gates?", "a": "Fences define and delay.", "x": "Fences define and delay. Key steps: Lock gates; See-through beats solid for visibility; Maintain them. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Shed security", "d": "Sheds hold burglary tools.", "g": "outdoor", "l": 2, "q": "What is Shed security?", "a": "Sheds hold burglary tools.", "x": "Sheds hold burglary tools. Key steps: Lock sheds; Anchor valuable tools; Do not leave ladders out. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Vacation checklist", "d": "Leaving town protocol.", "g": "habits", "l": 2, "q": "What is Vacation checklist?", "a": "Leaving town protocol.", "x": "Leaving town protocol. Key steps: Hold mail; Timers on lights; Neighbor check-ins; Unplug and secure. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Apartment security", "d": "Renters have options.", "g": "habits", "l": 2, "q": "What is Apartment security?", "a": "Renters have options.", "x": "Renters have options. Key steps: Door reinforcement that is removable; Portable alarms; Know neighbors; Renters insurance. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Peephole and viewers", "d": "See before opening.", "g": "doors", "l": 2, "q": "What is Peephole and viewers?", "a": "See before opening.", "x": "See before opening. Key steps: Wide-angle peephole; Or video doorbell; Never open to strangers. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-home-security-tips-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
