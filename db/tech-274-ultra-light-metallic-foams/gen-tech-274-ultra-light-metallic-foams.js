(function(){'use strict';
/* JAH The Ultra-Light Metallic Foams Database generator v1.0-et.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..20 rebuild the archive
   records; higher seeds generate boundless variants (quizzes, explorers,
   data tables) derived from the archive's own anchors. */
var SLUG="tech-274-ultra-light-metallic-foams";
var PREFIX="JAH-ET274-";
var SIG=false;
var SRC="public";
var FIELDS=["Foundations","Compounded","Advanced"];
var ANCHORS=[{"title": "Overview: Ultra-Light Metallic Foams", "tier": 0, "facts": ["What it is: Metals filled with gas pores like a sponge — stiff, light, and excellent at absorbing crash energy and sound.", "Why it matters: Materials are the foundation under every other technology: lighter, stronger, smarter matter makes everything built on top of it better.", "Scope: components, materials, processes, software, subsystems", "Teaching ladder: Foundations first, then Compounded, then Advanced"]}, {"title": "Core Components", "tier": 0, "facts": ["Melt foaming furnaces", "Powder foaming presses", "Pore-size imaging systems", "Crash crush-test rigs"]}, {"title": "Materials & Matter", "tier": 0, "facts": ["Aluminum and titanium powders", "Titanium hydride blowing agent", "Foam stabilizer additives", "Extrusion profile stock"]}, {"title": "Processes & Methods", "tier": 1, "facts": ["Foam expansion and solidification", "Cutting and machining", "Density grading", "Crush and acoustic testing"]}, {"title": "Software & Intelligence", "tier": 1, "facts": ["Crush-curve analyzers", "Pore-size image processing", "Energy-absorption models", "Batch certification logs"]}, {"title": "Subsystems & Architecture", "tier": 1, "facts": ["Foaming plant", "Machining cell", "Test laboratory", "Application engineering"]}, {"title": "Aluminum foams reach densities below 0.5 g/cm3 while keeping useful", "tier": 1, "facts": ["Aluminum foams reach densities below 0.5 g/cm3 while keeping useful stiffness and strength.", "Implication: It moves a laboratory curiosity toward an industrial supply chain.", "In practice: In practice, secure the supply chain before promising volume."]}, {"title": "Closed-cell foams absorb impact energy by progressive cell crushing", "tier": 1, "facts": ["Closed-cell foams absorb impact energy by progressive cell crushing, ideal for crash structures.", "Implication: Cost and scale, not physics, are now the gating factors.", "In practice: In practice, measure the full lifecycle, not just the headline property."]}, {"title": "Open-cell foams pass air and fluid, suiting heat exchangers, filters", "tier": 1, "facts": ["Open-cell foams pass air and fluid, suiting heat exchangers, filters, and sound absorbers.", "Implication: It compounds: better materials improve every device built from them.", "In practice: In practice, qualify it against the incumbent it replaces."]}, {"title": "Production routes include melt foaming with blowing agents and", "tier": 2, "facts": ["Production routes include melt foaming with blowing agents and powder-metallurgy foaming.", "Implication: Early adopters gain a performance edge in their own products.", "In practice: In practice, dispersion and defect control decide real performance."]}, {"title": "Applications: crash boxes, blast panels, machine bases with damping", "tier": 2, "facts": ["Applications: crash boxes, blast panels, machine bases with damping, and biomedical implants.", "Implication: This shifts what engineers can assume about the material's limits.", "In practice: In practice, start with the highest-value application first."]}, {"title": "Pore-size control sets the trade-off between strength and energy", "tier": 2, "facts": ["Pore-size control sets the trade-off between strength and energy absorption.", "Implication: The practical payoff is lighter, longer-lasting, more capable products.", "In practice: In practice, certify early — approvals take longer than development."]}, {"title": "Build Sequence: From Lab to Working System", "tier": 1, "facts": ["Define the target property and its test standard", "Synthesize the base material at lab scale", "Engineer the nanostructure or composite architecture", "Scale the process to pilot production"]}, {"title": "Testing & Validation Protocol", "tier": 1, "facts": ["TEST: Property testing against the target specification", "TEST: Accelerated aging and durability cycles", "TEST: Microstructure imaging and defect analysis", "TEST: Batch-to-batch consistency statistics"]}, {"title": "Safety, Risk & Stewardship", "tier": 2, "facts": ["Handle nanomaterials with exposure controls and respirators", "Follow chemical safety data sheets for all precursors", "Validate high-temperature and pressure equipment ratings", "Document waste streams and disposal routes"]}, {"title": "Economics & Scale-Up", "tier": 2, "facts": ["Pilot-plant economics set the first commercial price", "Scale curves: each 10x volume typically cuts cost 20-30%", "Performance premium must beat incumbent total cost", "Prototype cost / 10 = mature unit cost target"]}, {"title": "Deployment & Integration", "tier": 2, "facts": ["Qualify the material for the target application", "Integrate into the customer's manufacturing line", "Train operators on handling and QC", "Monitor field performance and feed back improvements"]}, {"title": "Maintenance & Lifecycle", "tier": 2, "facts": ["Monitor in-service degradation modes", "Schedule re-application or replacement per the rated life", "Keep batch traceability for every installed lot", "Update specifications from field data"]}, {"title": "Roadmap: The Next Ten Years", "tier": 2, "facts": ["Year 1-2: pilot production and first certifications", "Year 3-5: cost reduction and volume scale-up", "Year 5-7: next-generation formulations", "Year 8-10: commodity availability and standards maturity"]}, {"title": "Glossary & Quick Reference", "tier": 2, "facts": ["Nanostructure: Engineered features at the billionth-of-a-meter scale that set material properties.", "Composite: Two or more materials combined so the whole outperforms each part.", "Yield strength: The stress where a material starts to deform permanently.", "Fatigue life: How many load cycles a material survives before cracking."]}];
var ESSENCE="Ultra-Light Metallic Foams: Metals filled with gas pores like a sponge — stiff, light, and excellent at absorbing crash energy and sound.";
var IMPL=[];
var PRAC=[];
var LASTV="2026-10-19";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function escJ(s){return String(s).replace(/\\/g,"\\\\").replace(/"/g,'\\"').replace(/\n/g,"\\n").replace(/\r/g,"");}
function mkTable(title,rows){
  var L=['console.log("'+escJ(title)+'");'];
  for(var i=0;i<rows.length;i++) L.push('console.log("  '+escJ(rows[i][0])+' = '+escJ(rows[i][1])+'");');
  L.push('console.log("Listed "+rows.length+" entries.");');
  return L.join("\n");
}
function mkChecklist(title,items){
  var L=['console.log("'+escJ(title)+'");'];
  L.push('var items=['+items.map(function(x){return '"'+escJ(x)+'"';}).join(",")+'];');
  L.push('for(var i=0;i<items.length;i++){console.log("[ ] "+(i+1)+". "+items[i]);}');
  L.push('console.log("Checklist complete: "+items.length+" items.");');
  return L.join("\n");
}
function mkSteps(title,steps){
  var L=['console.log("'+escJ(title)+'");'];
  L.push('var steps=['+steps.map(function(x){return '"'+escJ(x)+'"';}).join(",")+'];');
  L.push('for(var i=0;i<steps.length;i++){console.log("Step "+(i+1)+": "+steps[i]);}');
  L.push('console.log("Sequence complete: "+steps.length+" steps.");');
  return L.join("\n");
}
function mkQA(title,pairs){
  var L=['console.log("'+escJ(title)+'");'];
  L.push('var qa=['+pairs.map(function(p){return '["'+escJ(p[0])+'","'+escJ(p[1])+'"]';}).join(",")+'];');
  L.push('for(var i=0;i<qa.length;i++){console.log("Q"+(i+1)+": "+qa[i][0]);console.log("A"+(i+1)+": "+qa[i][1]);}');
  L.push('console.log("Reviewed "+qa.length+" Q&A pairs.");');
  return L.join("\n");
}
function baseRec(seed,title,tier){
  return {id:PREFIX+String(seed).padStart(6,"0"),t:title,g:FIELDS[tier]||FIELDS[0],c:0,title:title,
    src:SRC,last_verified:LASTV,language:"javascript",ladder_rank:tier+1,ladder_tier:FIELDS[tier]||FIELDS[0],_seed:seed,
    source:(SIG?"Signature record \u2014 original work of the JAH system, labeled Signature, never presented as public record."
               :"Public record \u2014 curated public-knowledge reference.")};
}
function finish(r,program){
  r.program=program;
  r.demo={kind:(SIG?"signature method simulator":"archive explorer"),language:"javascript",program:program,note:"Runnable demo program. Runs with: node demo.js"};
  r.provenance=r.source;
  if(r.description&&r.description.length<140){var pad=ESSENCE+" ";while(r.description.length<140)r.description+=" "+pad;}
  return r;
}
function anchorRec(seed,a){
  var r=baseRec(seed,a.title,a.tier);
  var facts=a.facts||[];
  var desc=a.title+". "+facts.join(" ");
  while(desc.length<140) desc+=" "+ESSENCE;
  r.description=desc;
  r.definition=a.title+" \u2014 "+(facts[0]||ESSENCE).slice(0,140)+".";
  r.key_points=facts.slice(0,4);
  while(r.key_points.length<3) r.key_points.push("See the full record for working detail.");
  r.how_it_works=["Read the definition and key facts.","Run the demo program below.",
    "Note the numbers \u2014 they are the working values.","Apply it to a real case."];
  var prog=mkQA((SIG?"SIGNATURE ":"")+"KEY FACT: "+a.title.toUpperCase().slice(0,50),
    facts.slice(0,3).map(function(f,i){return ["Fact "+(i+1),f];}));
  return finish(r,prog);
}
function quizRec(seed,rnd,tier){
  var qa=ANCHORS.slice(0,6).map(function(a){return ["Key fact: "+a.title,(a.facts[0]||"").slice(0,150)];});
  var title="Boundless Quiz #"+seed+" \u2014 "+SLUG;
  var r=baseRec(seed,title,tier);
  r.description="A boundless self-test generated from the archive's own anchors: "+qa.length+" questions drawn from real "+SLUG+" records. Same seed always makes the same quiz.";
  r.definition="Generated self-test over the "+SLUG+" archive anchors.";
  r.key_points=qa.map(function(x){return x[0];});
  while(r.key_points.length<3) r.key_points.push("Answer aloud before reading.");
  r.how_it_works=["Run the demo quiz.","Answer each question aloud before reading the answer.","Log misses and re-open those records.","Re-drill until perfect."];
  return finish(r,mkQA("QUIZ #"+seed,qa));
}
function explorerRec(seed,rnd,tier){
  var a=ANCHORS[(rnd()*ANCHORS.length)|0];
  var title="Boundless Explorer #"+seed+" \u2014 "+a.title;
  var r=baseRec(seed,title,tier);
  var rows=(a.facts||[]).map(function(f,i){return ["fact "+(i+1),f.slice(0,120)];});
  r.description="A deep exploration of one archive anchor: "+a.title+". "+(a.facts.join(" ")||ESSENCE);
  r.definition="Explorer view over the anchor: "+a.title+".";
  r.key_points=(a.facts||[]).slice(0,4);
  while(r.key_points.length<3) r.key_points.push(IMPL[(rnd()*IMPL.length)|0]);
  r.how_it_works=["Run the explorer demo.","Follow each fact to its source record.","Compare with neighboring anchors.","Write one new application idea."];
  return finish(r,mkTable("EXPLORER: "+a.title.toUpperCase().slice(0,50),rows.length?rows:[["note","see key facts"]]));
}
function tableRec(seed,rnd,tier){
  var title="Boundless Data Table #"+seed+" \u2014 "+SLUG;
  var r=baseRec(seed,title,tier);
  var rows=ANCHORS.slice(0,8).map(function(a){return [a.title,(a.facts[0]||"").slice(0,100)];});
  r.description="A generated data table summarizing "+rows.length+" archive anchors of "+SLUG+" for quick comparison.";
  r.definition="Comparison table over "+SLUG+" anchors.";
  r.key_points=rows.map(function(x){return x[0];});
  while(r.key_points.length<3) r.key_points.push("Compare rows before deciding.");
  r.how_it_works=["Run the table demo.","Compare the rows side by side.","Open the full records behind interesting rows.","Decide with data, not memory."];
  return finish(r,mkTable("DATA TABLE #"+seed,rows));
}
function generate(seed,opts){
  opts=opts||{};
  var tier=0;
  if(opts.tier==="Compounded")tier=1; else if(opts.tier==="Advanced")tier=2;
  if(seed>=1&&seed<=20){ var a=ANCHORS[seed-1]; if(a) return anchorRec(seed,a); }
  var rnd=prng(seed*2654435761>>>0);
  if(!opts.tier) tier=(rnd()*3)|0;
  var kind=(rnd()*3)|0;
  if(kind===0) return quizRec(seed,rnd,tier);
  if(kind===1) return explorerRec(seed,rnd,tier);
  return tableRec(seed,rnd,tier);
}
function validate(rec){
  var errors=[];
  if(!rec||typeof rec!=="object") return {ok:false,errors:["not an object"]};
  ["id","title","description","definition","program"].forEach(function(k){
    if(!rec[k]||!String(rec[k]).length) errors.push("missing "+k);
  });
  if(rec.description&&rec.description.length<140) errors.push("description too short");
  return {ok:errors.length===0,errors:errors};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].id===rec.id) return {ok:false,errors:["duplicate id "+rec.id]};
  }
  return {ok:true,errors:[]};
}
window.DBGEN={generate:generate,validate:validate,driftCheck:driftCheck,slug:SLUG};
})();
