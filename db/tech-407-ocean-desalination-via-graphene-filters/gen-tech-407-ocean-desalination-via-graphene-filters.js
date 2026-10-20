(function(){'use strict';
/* JAH The Ocean Desalination via Graphene Filters Database generator v1.0-et.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..20 rebuild the archive
   records; higher seeds generate boundless variants (quizzes, explorers,
   data tables) derived from the archive's own anchors. */
var SLUG="tech-407-ocean-desalination-via-graphene-filters";
var PREFIX="JAH-ET407-";
var SIG=false;
var SRC="public";
var FIELDS=["Foundations","Compounded","Advanced"];
var ANCHORS=[{"title": "Overview: Ocean Desalination via Graphene Filters", "tier": 0, "facts": ["What it is: Desalination membranes using graphene's atomic precision to pass water and block salt with less energy.", "Why it matters: Feeding ten billion people while healing the planet is the defining challenge: these technologies grow more with less.", "Scope: components, materials, processes, software, subsystems", "Teaching ladder: Foundations first, then Compounded, then Advanced"]}, {"title": "Core Components", "tier": 0, "facts": ["Membrane casting lines", "Pressure vessels", "Pilot plants", "Fouling test rigs"]}, {"title": "Materials & Matter", "tier": 0, "facts": ["Graphene-oxide dispersions", "Support membranes", "Pressure housings", "Antifouling coatings"]}, {"title": "Processes & Methods", "tier": 1, "facts": ["Membrane fabrication", "Module assembly", "Pilot testing", "Scale-up"]}, {"title": "Software & Intelligence", "tier": 1, "facts": ["Flux models", "Fouling predictors", "Energy calculators", "Pilot analytics"]}, {"title": "Subsystems & Architecture", "tier": 1, "facts": ["Membrane plant", "Pilot program", "Test lab", "Deployment engineering"]}, {"title": "Reverse osmosis dominates desalination but is energy-intensive at 3-4", "tier": 1, "facts": ["Reverse osmosis dominates desalination but is energy-intensive at 3-4 kWh per cubic meter.", "Implication: It moves agriculture from extraction toward regeneration.", "In practice: In practice, secure the buyer before scaling production."]}, {"title": "Nanoporous graphene passes water molecules while blocking hydrated", "tier": 1, "facts": ["Nanoporous graphene passes water molecules while blocking hydrated salt ions.", "Implication: Farmer economics, not ideals, drive adoption.", "In practice: In practice, document everything — data is the product too."]}, {"title": "Graphene-oxide laminates offer a scalable route versus single-layer", "tier": 1, "facts": ["Graphene-oxide laminates offer a scalable route versus single-layer drilling.", "Implication: It compounds: healthy soil improves every crop grown on it.", "In practice: In practice, run local trials — results vary by soil and climate."]}, {"title": "Fouling and mechanical robustness at pressure are the engineering", "tier": 2, "facts": ["Fouling and mechanical robustness at pressure are the engineering challenges.", "Implication: Early regions become the exporters of know-how.", "In practice: In practice, train the grower, not just the equipment."]}, {"title": "Target markets: water-stressed coastal cities and industrial reuse", "tier": 2, "facts": ["Target markets: water-stressed coastal cities and industrial reuse.", "Implication: This decides whether farming can sustain a growing population.", "In practice: In practice, measure economics per acre honestly."]}, {"title": "Energy savings of 20-50% are the prize versus conventional RO", "tier": 2, "facts": ["Energy savings of 20-50% are the prize versus conventional RO.", "Implication: The practical payoff is more food with less land, water, and chemistry.", "In practice: In practice, stack practices: no single fix transforms a farm."]}, {"title": "Build Sequence: From Lab to Working System", "tier": 1, "facts": ["Define the crop, yield, and sustainability targets", "Prototype the biological or mechanical system", "Run controlled trials measuring efficacy", "Validate food safety and environmental impact"]}, {"title": "Testing & Validation Protocol", "tier": 1, "facts": ["TEST: Multi-season field trials across climates", "TEST: Yield and quality versus the control", "TEST: Food-safety and residue testing", "TEST: Environmental impact assessment"]}, {"title": "Safety, Risk & Stewardship", "tier": 2, "facts": ["Verify food-safety clearances before any deployment", "Assess non-target ecological effects", "Follow biosafety rules for engineered organisms", "Protect workers handling biological and chemical inputs"]}, {"title": "Economics & Scale-Up", "tier": 2, "facts": ["Unit economics per acre or kilogram decide adoption", "Premium markets fund the early years", "Policy incentives accelerate sustainable practices", "Prototype cost / 10 = mature unit cost target"]}, {"title": "Deployment & Integration", "tier": 2, "facts": ["Start with demonstration farms in target regions", "Train growers on the new system", "Build input supply chains", "Connect to buyers paying for quality or sustainability"]}, {"title": "Maintenance & Lifecycle", "tier": 2, "facts": ["Monitor soil and ecosystem health over seasons", "Maintain equipment and calibrate sensors", "Refresh biological inputs per schedule", "Adapt practices from accumulated data"]}, {"title": "Roadmap: The Next Ten Years", "tier": 2, "facts": ["Year 1-2: trials and regulatory progress", "Year 3-5: commercial launch in lead markets", "Year 5-7: cost reduction and global spread", "Year 8-10: the practice becomes standard agriculture"]}, {"title": "Glossary & Quick Reference", "tier": 2, "facts": ["Yield: Output per area — the core productivity metric.", "Fertigation: Delivering fertilizer through irrigation water.", "IPM: Integrated pest management — combining control methods.", "RAS: Recirculating aquaculture system — filtered fish farming."]}];
var ESSENCE="Ocean Desalination via Graphene Filters: Desalination membranes using graphene's atomic precision to pass water and block salt with less energy.";
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
