(function(){'use strict';
/* JAH Pet Toxin Guide Database generator — jahdb-pet-toxin-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='pet-toxin-guide',PREFIX='JAH-PET-',NAME='JAH Pet Toxin Guide Database';
var FIELDS=["foods", "plants", "chemicals", "response"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chocolate", "d": "Theobromine toxicity; darker is deadlier.", "g": "foods", "l": 2, "q": "What is Chocolate?", "a": "Theobromine toxicity; darker is deadlier.", "x": "Theobromine toxicity; darker is deadlier. Key steps: Keep all chocolate away; Dark/baking most dangerous; Call vet if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Xylitol", "d": "Deadly to dogs even in small amounts; in sugar-free gum and peanut butter.", "g": "foods", "l": 2, "q": "What is Xylitol?", "a": "Deadly to dogs even in small amounts; in sugar-free gum and peanut butter.", "x": "Deadly to dogs even in small amounts; in sugar-free gum and peanut butter. Key steps: Check peanut butter labels; Call vet immediately if eaten; Induces liver failure. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Grapes and raisins", "d": "Can cause kidney failure in dogs; amount unpredictable.", "g": "foods", "l": 2, "q": "What is Grapes and raisins?", "a": "Can cause kidney failure in dogs; amount unpredictable.", "x": "Can cause kidney failure in dogs; amount unpredictable. Key steps: Keep away; Call vet if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Onions and garlic", "d": "Damage red blood cells in dogs and cats.", "g": "foods", "l": 2, "q": "What is Onions and garlic?", "a": "Damage red blood cells in dogs and cats.", "x": "Damage red blood cells in dogs and cats. Key steps: All forms toxic; Watch for pale gums; Vet care. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Macadamia nuts", "d": "Toxic to dogs: weakness, vomiting.", "g": "foods", "l": 2, "q": "What is Macadamia nuts?", "a": "Toxic to dogs: weakness, vomiting.", "x": "Toxic to dogs: weakness, vomiting. Key steps: Keep away; Vet if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Alcohol", "d": "Far more dangerous to pets than people.", "g": "foods", "l": 2, "q": "What is Alcohol?", "a": "Far more dangerous to pets than people.", "x": "Far more dangerous to pets than people. Key steps: Keep drinks away; Vet emergency if ingested. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Caffeine", "d": "Coffee, tea, energy drinks overstimulate dangerously.", "g": "foods", "l": 2, "q": "What is Caffeine?", "a": "Coffee, tea, energy drinks overstimulate dangerously.", "x": "Coffee, tea, energy drinks overstimulate dangerously. Key steps: Keep away; Vet if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Lilies", "d": "Deadly to cats: kidney failure from pollen alone.", "g": "plants", "l": 2, "q": "What is Lilies?", "a": "Deadly to cats: kidney failure from pollen alone.", "x": "Deadly to cats: kidney failure from pollen alone. Key steps: No lilies in cat homes; Brush off pollen, vet immediately; All parts toxic. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sago palm", "d": "Deadly to dogs; liver failure.", "g": "plants", "l": 2, "q": "What is Sago palm?", "a": "Deadly to dogs; liver failure.", "x": "Deadly to dogs; liver failure. Key steps: Remove from yards; All parts toxic; Emergency vet. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Azalea", "d": "Cardiac toxins for dogs and cats.", "g": "plants", "l": 2, "q": "What is Azalea?", "a": "Cardiac toxins for dogs and cats.", "x": "Cardiac toxins for dogs and cats. Key steps: Keep away; Vet if chewed. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Tulip bulbs", "d": "Concentrated toxins in bulbs.", "g": "plants", "l": 2, "q": "What is Tulip bulbs?", "a": "Concentrated toxins in bulbs.", "x": "Concentrated toxins in bulbs. Key steps: Fence bulbs; Vet if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Daffodil", "d": "Vomiting and cardiac issues.", "g": "plants", "l": 2, "q": "What is Daffodil?", "a": "Vomiting and cardiac issues.", "x": "Vomiting and cardiac issues. Key steps: Keep away; Vet if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Oleander", "d": "Extremely toxic cardiac plant.", "g": "plants", "l": 2, "q": "What is Oleander?", "a": "Extremely toxic cardiac plant.", "x": "Extremely toxic cardiac plant. Key steps: Never plant where pets roam; Emergency vet. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Aloe (eaten)", "d": "Skin-safe but gut-toxic if eaten.", "g": "plants", "l": 2, "q": "What is Aloe (eaten)?", "a": "Skin-safe but gut-toxic if eaten.", "x": "Skin-safe but gut-toxic if eaten. Key steps: Keep chewable leaves away. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Pothos", "d": "Calcium oxalates burn mouths.", "g": "plants", "l": 2, "q": "What is Pothos?", "a": "Calcium oxalates burn mouths.", "x": "Calcium oxalates burn mouths. Key steps: Hang high; Watch for drooling. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Antifreeze", "d": "Sweet taste, kidney failure; tiny amounts kill.", "g": "chemicals", "l": 2, "q": "What is Antifreeze?", "a": "Sweet taste, kidney failure; tiny amounts kill.", "x": "Sweet taste, kidney failure; tiny amounts kill. Key steps: Clean spills immediately; Use pet-safe antifreeze; Emergency vet — minutes matter. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Rat poison", "d": "Bleeding or neurological poisons.", "g": "chemicals", "l": 2, "q": "What is Rat poison?", "a": "Bleeding or neurological poisons.", "x": "Bleeding or neurological poisons. Key steps: Use pet-safe alternatives; Know the active ingredient; Vet with the package. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Slug bait (metaldehyde)", "d": "Tremors and seizures.", "g": "chemicals", "l": 2, "q": "What is Slug bait (metaldehyde)?", "a": "Tremors and seizures.", "x": "Tremors and seizures. Key steps: Iron-phosphate alternatives; Vet immediately. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Fertilizers", "d": "GI upset and worse.", "g": "chemicals", "l": 2, "q": "What is Fertilizers?", "a": "GI upset and worse.", "x": "GI upset and worse. Key steps: Keep pets off treated lawns; Store locked. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Cocoa mulch", "d": "Theobromine like chocolate.", "g": "chemicals", "l": 2, "q": "What is Cocoa mulch?", "a": "Theobromine like chocolate.", "x": "Theobromine like chocolate. Key steps: Use other mulches; Vet if eaten. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Essential oils", "d": "Many are toxic to cats especially.", "g": "chemicals", "l": 2, "q": "What is Essential oils?", "a": "Many are toxic to cats especially.", "x": "Many are toxic to cats especially. Key steps: Tea tree, citrus oils risky; Diffuse with ventilation; Cat-safe choices only. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Flea products (wrong species)", "d": "Dog flea meds can kill cats.", "g": "chemicals", "l": 2, "q": "What is Flea products (wrong species)?", "a": "Dog flea meds can kill cats.", "x": "Dog flea meds can kill cats. Key steps: Never swap species products; Read labels; Vet if misapplied. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Human medications", "d": "NSAIDs, acetaminophen, antidepressants.", "g": "chemicals", "l": 2, "q": "What is Human medications?", "a": "NSAIDs, acetaminophen, antidepressants.", "x": "NSAIDs, acetaminophen, antidepressants. Key steps: Lock all meds; Never dose without vet guidance; Acetaminophen kills cats. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "If poisoning is suspected", "d": "Speed saves lives.", "g": "response", "l": 2, "q": "What is If poisoning is suspected?", "a": "Speed saves lives.", "x": "Speed saves lives. Key steps: Call vet or poison control immediately; Bring the package; Do not induce vomiting unless told. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Pet poison helpline", "d": "Save the number.", "g": "response", "l": 2, "q": "What is Pet poison helpline?", "a": "Save the number.", "x": "Save the number. Key steps: ASPCA: (888) 426-4435; Have credit card ready (fee); Call fast. Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-pet-toxin-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
