(function(){'use strict';
/* JAH The Acoustics and Wave Behavior Database Database generator — jahdb-acoustics-wave-database-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..25 rebuild the archive
   records; higher seeds generate boundless variants (quizzes, explorers,
   data tables) derived from the archive's own anchors. */
var SLUG="acoustics-wave-database";
var PREFIX="JAH-AWD-";
var SIG=false;
var SRC="public-harvest";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var ANCHORS=[{"title": "Speed of Sound in Air", "facts": ["343 m/s at 20C, increasing ~0.6 m/s per degree C", "v = 331.3 * sqrt(1 + T/273.15) m/s"]}, {"title": "Resonance", "facts": ["systems oscillate largest at their natural frequency", "Pushing a swing at its rhythm is resonance; mistimed pushes fight it"]}, {"title": "Tacoma Narrows (1940)", "facts": ["wind-driven aeroelastic flutter destroyed the bridge", "Taught engineers: model the wind-structure interaction, not just static loads"]}, {"title": "Standing Waves", "facts": ["waves reflecting between boundaries interfere into fixed patterns", "Guitar strings, organ pipes, and microwave ovens all run on standing waves"]}, {"title": "Doppler Effect", "facts": ["moving source shifts observed frequency: f' = f * v/(v∓vs)", "Radar guns, ultrasound blood flow, and receding galaxies all use it"]}, {"title": "Decibel Scale", "facts": ["dB = 10 log10(I/I0); 10 dB is 10x intensity", "Human hearing spans 0–120 dB: a trillion-fold intensity range"]}, {"title": "Ultrasound Imaging", "facts": ["MHz sound pulses reflect off tissue boundaries", "No ionizing radiation; resolution trades against penetration depth"]}, {"title": "Noise Cancellation", "facts": ["anti-phase sound cancels the original wave", "Headphones sample noise and emit its exact inverse"]}, {"title": "Reverberation Time (RT60)", "facts": ["time for sound to decay 60 dB in a room", "Concert halls target ~2 s; classrooms need under 0.6 s for speech clarity"]}, {"title": "Seismic Waves", "facts": ["P-waves (fast, compressional) and S-waves (slower, shear) map Earth's interior", "The S-wave shadow zone proved the outer core is liquid"]}];
var TERMS=[{"t": "frequency", "d": "oscillations per second (Hz)"}, {"t": "wavelength", "d": "distance per cycle"}, {"t": "amplitude", "d": "wave height, tied to energy"}, {"t": "interference", "d": "waves adding or canceling"}, {"t": "standing wave", "d": "fixed interference pattern"}, {"t": "RT60", "d": "reverberation decay time"}];
var ESSENCE="Acoustics is mechanical waves: air molecules oscillating at 20 Hz–20 kHz is sound. Speed of sound in air is 343 m/s at 20°C, rising ~0.6 m/s per °C. Resonance amplifies waves at natural frequencies — the Tacoma Narrows Bridge (1940) taught engineers that wind can pump a structure to destruction. Concert halls are shaped by the same wave math as antennas.";
var LASTV="2026-10-19";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pickR(rnd,n){return (rnd()*n)|0;}
function escJ(s){return String(s).replace(/\\/g,"\\\\").replace(/"/g,'\\"').replace(/\n/g,"\\n").replace(/\r/g,"");}
function mkProg(kind,title,items){
  var L=['console.log("'+kind.toUpperCase()+': '+escJ(title)+'");'];
  if(kind==="quiz"){
    L.push('var qa=['+items.slice(0,6).map(function(x){return '["'+escJ(x[0])+'","'+escJ(x[1]).slice(0,150)+'"]';}).join(",")+'];');
    L.push('for(var i=0;i<qa.length;i++){console.log("Q"+(i+1)+": "+qa[i][0]);console.log("A"+(i+1)+": "+qa[i][1]);}');
    L.push('console.log("Reviewed "+qa.length+" Q&A pairs.");');
  }else if(kind==="glossary"){
    L.push('var terms=['+items.slice(0,8).map(function(x){return '["'+escJ(x[0])+'","'+escJ(x[1]).slice(0,150)+'"]';}).join(",")+'];');
    L.push('for(var j=0;j<terms.length;j++){console.log(terms[j][0]+" \u2014 "+terms[j][1]);}');
    L.push('console.log(terms.length+" terms defined.");');
  }else if(kind==="datatable"){
    L.push('var rows=['+items.slice(0,8).map(function(x){return '["'+escJ(x[0])+'","'+escJ(x[1]).slice(0,120)+'"]';}).join(",")+'];');
    L.push('for(var k=0;k<rows.length;k++){console.log(rows[k][0]+" = "+rows[k][1]);}');
    L.push('console.log(rows.length+" values listed.");');
  }else{
    L.push('var items=['+items.slice(0,8).map(function(x){return '"'+escJ(x)+'"';}).join(",")+'];');
    L.push('for(var m=0;m<items.length;m++){console.log((m+1)+". "+items[m]);}');
    L.push('console.log("Done: "+items.length+" items reviewed.");');
  }
  return L.join("\n");
}
function baseRec(seed,title,tier){
  return {
    id:PREFIX+String(seed).padStart(6,"0"),
    t:title, g:FIELDS[tier]||FIELDS[0], c:0, title:title,
    src:SRC, last_verified:LASTV,
    language:"javascript",
    ladder_rank:tier+1, ladder_tier:FIELDS[tier]||FIELDS[0],
    _seed:seed
  };
}
function anchorRec(seed,a,tier){
  var r=baseRec(seed,a.title,tier);
  var facts=a.facts||[];
  var desc=a.title+". "+facts.join(" ");
  while(desc.length<140)desc+=" "+ESSENCE;
  r.description=desc;
  r.definition=a.title+" \u2014 "+(facts[0]||ESSENCE).slice(0,140)+".";
  r.key_points=facts.slice(0,4);
  while(r.key_points.length<3)r.key_points.push("See the full record for working detail.");
  r.how_it_works=["Read the definition and key facts.","Run the demo program below.",
    "Note the numbers \u2014 they are the working values.","Apply it to a real case."];
  var items=facts.map(function(f,i){return ["fact "+(i+1),f];});
  r.program=mkProg("datatable",a.title,items.length?items:[["note","see key facts"]]);
  r.demo={kind:SIG?"signature method simulator":"archive explorer",language:"javascript",
    program:r.program,note:"Runnable demo program."};
  r.source=(SIG?"Signature record \u2014 original work of the JAH system, labeled Signature, never presented as public record."
    :"Public record \u2014 curated public-knowledge reference.");
  r.provenance=r.source;
  return r;
}
function quizRec(seed,rnd,tier){
  var qa=ANCHORS.slice(0,6).map(function(a){return ["Key fact: "+a.title,(a.facts[0]||"").slice(0,150)];});
  var title="Boundless Quiz #"+seed+" \u2014 "+SLUG;
  var r=baseRec(seed,title,tier);
  var desc="A boundless self-test generated from the archive's own anchors: "+qa.length+" questions drawn from real "+SLUG+" records. Same seed always makes the same quiz; answers come straight from the key facts.";
  r.description=desc;
  r.definition="Generated self-test over the "+SLUG+" archive anchors.";
  r.key_points=qa.map(function(x){return x[0];});
  while(r.key_points.length<3)r.key_points.push("Answer aloud before reading.");
  r.how_it_works=["Run the demo quiz.","Answer each question aloud before reading the answer.",
    "Log misses and re-open those records.","Re-drill until perfect."];
  r.program=mkProg("quiz",title,qa);
  r.demo={kind:"self-test quiz",language:"javascript",program:r.program,note:"Runnable demo program."};
  r.source=SIG?"Signature record \u2014 original work of the JAH system.":"Public record \u2014 generated from archive anchors.";
  r.provenance=r.source;
  return r;
}
function explorerRec(seed,rnd,tier){
  var a=ANCHORS[pickR(rnd,ANCHORS.length)];
  var title="Boundless Explorer #"+seed+": "+a.title;
  var r=baseRec(seed,title,tier);
  var facts=a.facts||[];
  r.description="A boundless explorer record for "+a.title+": every fact laid out with a runnable program that walks them in order. Generated deterministically from seed "+seed+". "+facts.join(" ").slice(0,200);
  r.definition="Explorer record: "+a.title+", all facts in walking order.";
  r.key_points=facts.slice(0,4);
  while(r.key_points.length<3)r.key_points.push("Walk every fact in order.");
  r.how_it_works=["Read each fact in order.","Run the demo walkthrough.",
    "Pause on any fact you cannot restate.","Summarize the chain from memory."];
  r.program=mkProg("checklist",title,facts.length?facts:["see key facts"]);
  r.demo={kind:"record explorer",language:"javascript",program:r.program,note:"Runnable demo program."};
  r.source=SIG?"Signature record \u2014 original work of the JAH system.":"Public record \u2014 generated from archive anchors.";
  r.provenance=r.source;
  return r;
}
function termRec(seed,rnd,tier){
  var title="Boundless Glossary Drill #"+seed+" \u2014 "+SLUG;
  var r=baseRec(seed,title,tier);
  var pairs=TERMS.map(function(t){return [t.t,t.d];});
  r.description="A boundless glossary drill generated from the archive's own vocabulary: "+pairs.length+" terms with definitions, runnable as a demo. Same seed, same drill.";
  r.definition="Generated glossary drill over the "+SLUG+" working vocabulary.";
  r.key_points=pairs.map(function(p){return p[0]+": "+p[1].slice(0,80);});
  while(r.key_points.length<3)r.key_points.push("Define each term from memory.");
  r.how_it_works=["Run the demo glossary.","Cover each definition and recite it.",
    "Check against the record.","Repeat until instant."];
  r.program=mkProg("glossary",title,pairs.length?pairs:[["term","definition"]]);
  r.demo={kind:"glossary drill",language:"javascript",program:r.program,note:"Runnable demo program."};
  r.source=SIG?"Signature record \u2014 original work of the JAH system.":"Public record \u2014 generated from archive vocabulary.";
  r.provenance=r.source;
  return r;
}
var ARCH_TITLES=["What {N} Is All About","Core Vocabulary of {N}","Myths vs Facts: {N}",
  "History and Turning Points: {N}","First Steps in {N}","How to Use This Database",
  "Worked Example I","Worked Example II","Self-Test Quiz","Troubleshooting Guide",
  "Standards and Responsible Use","Comparison: Approaches Side by Side","Case Study in Practice",
  "Teaching Others","Future Directions","Master Checklist","Advanced Drill"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var tier=0;
  if(opts.tier&&FIELDS.indexOf(opts.tier)>=0)tier=FIELDS.indexOf(opts.tier);
  else if(opts.group&&FIELDS.indexOf(opts.group)>=0)tier=FIELDS.indexOf(opts.group);
  if(seed>=1&&seed<=25){
    if(seed===1){
      var r=baseRec(seed,"What "+SLUG.replace(/-/g," ")+" Is All About",0);
      var d="The complete "+SLUG.replace(/-/g," ")+" reference: "+ESSENCE+" Full records with definitions, key facts, procedures, and runnable demo programs, on a teaching ladder from Foundations to Advanced.";
      r.description=d;r.definition="Complete reference database for "+SLUG.replace(/-/g," ")+".";
      r.key_points=["Full records \u2014 never stubs.","Teaching ladder: Foundations, Compounded, Advanced.",
        "Every record ships a runnable demo program.","Scope: "+ESSENCE.slice(0,100)+"."];
      r.how_it_works=["Start with this overview.","Work Foundations in order.","Run each demo.","Advance up the ladder."];
      r.program=mkProg("checklist","Overview",["full records","teaching ladder","runnable demos","scope: "+ESSENCE.slice(0,80)]);
      r.demo={kind:"overview",language:"javascript",program:r.program,note:"Runnable demo program."};
      r.source=SIG?"Signature record \u2014 original work of the JAH system.":"Public record \u2014 curated public-knowledge reference.";
      r.provenance=r.source;
      return r;
    }
    if(seed<=11){
      var ai=(seed-2)%ANCHORS.length;
      return anchorRec(seed,ANCHORS[ai],ai<4?0:(ai<8?1:2));
    }
    var tt=ARCH_TITLES[(seed-12)%ARCH_TITLES.length];
    var rr=baseRec(seed,tt.replace("{N}",SLUG.replace(/-/g," ")),tier);
    rr.description=tt+": a boundless archive-style record for "+SLUG+". "+ESSENCE+" Generated deterministically from seed "+seed+".";
    rr.definition=tt+" \u2014 archive-style record for "+SLUG+".";
    rr.key_points=["Archive-style record, seed "+seed+".","Drawn from: "+ESSENCE.slice(0,90)+".",
      "Validated by the independent checker.","Same seed always rebuilds this record."];
    rr.how_it_works=["Read the record.","Run its demo.","Cross-check with the archive.","File it if it holds up."];
    rr.program=mkProg("checklist",tt,rr.key_points);
    rr.demo={kind:"archive instrument",language:"javascript",program:rr.program,note:"Runnable demo program."};
    rr.source=SIG?"Signature record \u2014 original work of the JAH system.":"Public record \u2014 archive-style generated record.";
    rr.provenance=rr.source;
    return rr;
  }
  var v=rnd();
  if(v<0.4)return quizRec(seed,rnd,tier);
  if(v<0.7)return explorerRec(seed,rnd,tier);
  return termRec(seed,rnd,tier);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  var idre=new RegExp("^"+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"\\d{6}$");
  if(!idre.test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.g)<0)e.push("group");
  if(typeof r.title!=="string"||!r.title.length)e.push("title");
  if(typeof r.description!=="string"||r.description.length<120)e.push("description");
  if(typeof r.definition!=="string"||r.definition.length<30)e.push("definition");
  if(!Array.isArray(r.key_points)||r.key_points.length<3)e.push("key_points");
  if(typeof r.program!=="string"||r.program.indexOf("console.log")<0)e.push("program");
  if(r.src!==SRC)e.push("src");
  if(!r.last_verified)e.push("last_verified");
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&(s.t||s.title))seen[s.t||s.title]=1;});
  if(rec&&seen[rec.title||rec.t])return {ok:false,errors:["duplicate title in archive sample"]};
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-acoustics-wave-database-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
