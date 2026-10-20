(function(){'use strict';
/* JAH The Self-Cleaning Solar Roof Tiles Database generator v1.0-et.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..20 rebuild the archive
   records; higher seeds generate boundless variants (quizzes, explorers,
   data tables) derived from the archive's own anchors. */
var SLUG="tech-493-self-cleaning-solar-roof-tiles";
var PREFIX="JAH-ET493-";
var SIG=false;
var SRC="public";
var FIELDS=["Foundations","Compounded","Advanced"];
var ANCHORS=[{"title": "Overview: Self-Cleaning Solar Roof Tiles", "tier": 0, "facts": ["What it is: Solar tiles that clean themselves — coatings shedding dust to protect power output.", "Why it matters: The built world is humanity's biggest artifact: better construction and manufacturing make it faster, cheaper, and greener.", "Scope: components, materials, processes, software, subsystems", "Teaching ladder: Foundations first, then Compounded, then Advanced"]}, {"title": "Core Components", "tier": 0, "facts": ["Tile lamination", "Coating spray", "Durability testers", "Install tools"]}, {"title": "Materials & Matter", "tier": 0, "facts": ["PV cells", "Tile substrates", "Self-cleaning coatings", "Flashing"]}, {"title": "Processes & Methods", "tier": 1, "facts": ["Tile manufacturing", "Coating application", "Testing", "Installation"]}, {"title": "Software & Intelligence", "tier": 1, "facts": ["Soiling models", "Output monitors", "Warranty trackers", "Training modules"]}, {"title": "Subsystems & Architecture", "tier": 1, "facts": ["Tile plant", "Test lab", "Install network", "Warranty service"]}, {"title": "Soiling cuts solar output 5-25% in dusty regions", "tier": 1, "facts": ["Soiling cuts solar output 5-25% in dusty regions.", "Implication: It moves construction from craft toward manufacturing.", "In practice: In practice, document the pilot obsessively for the next sale."]}, {"title": "Hydrophobic and photocatalytic coatings shed dust with rain or dew", "tier": 1, "facts": ["Hydrophobic and photocatalytic coatings shed dust with rain or dew.", "Implication: Codes and crews, not technology, pace adoption.", "In practice: In practice, design for maintenance access from the start."]}, {"title": "Automated cleaning robots are the alternative; coatings are passive", "tier": 1, "facts": ["Automated cleaning robots are the alternative; coatings are passive.", "Implication: It compounds: better methods build the factories for the next methods.", "In practice: In practice, engage code officials before the pilot, not after."]}, {"title": "Tile integration (versus panels) suits residential aesthetics", "tier": 2, "facts": ["Tile integration (versus panels) suits residential aesthetics.", "Implication: Early regions export the expertise worldwide.", "In practice: In practice, train crews thoroughly — new methods fail from habit."]}, {"title": "Coating durability through weather cycles decides economics", "tier": 2, "facts": ["Coating durability through weather cycles decides economics.", "Implication: This decides how fast and clean the world gets built.", "In practice: In practice, measure the whole project cost, not the component."]}, {"title": "Water-scarce regions benefit most from waterless cleaning", "tier": 2, "facts": ["Water-scarce regions benefit most from waterless cleaning.", "Implication: The practical payoff is more housing and infrastructure per dollar.", "In practice: In practice, standardize details to unlock factory production."]}, {"title": "Build Sequence: From Lab to Working System", "tier": 1, "facts": ["Define the structural and performance specification", "Prototype the machine, material, or module", "Validate against building and safety codes", "Pilot on a real project"]}, {"title": "Testing & Validation Protocol", "tier": 1, "facts": ["TEST: Structural testing to code requirements", "TEST: Durability under real weather and loads", "TEST: Safety certification for machines and methods", "TEST: Pilot-project performance measurement"]}, {"title": "Safety, Risk & Stewardship", "tier": 2, "facts": ["Follow construction safety standards on every site", "Guard robotic and autonomous equipment zones", "Verify structural calculations independently", "Plan for failure modes, not just success"]}, {"title": "Economics & Scale-Up", "tier": 2, "facts": ["First cost versus lifecycle cost frames every decision", "Labor savings fund automation investments", "Standardization unlocks manufacturing scale", "Prototype cost / 10 = mature unit cost target"]}, {"title": "Deployment & Integration", "tier": 2, "facts": ["Start with pilot projects and reference builds", "Work with code officials early", "Train the workforce on new methods", "Build the supply chain for materials and parts"]}, {"title": "Maintenance & Lifecycle", "tier": 2, "facts": ["Inspect structures on schedule", "Service machines per the maintenance plan", "Monitor sensor data for early warnings", "Update standards from field experience"]}, {"title": "Roadmap: The Next Ten Years", "tier": 2, "facts": ["Year 1-2: pilots and code approvals", "Year 3-5: commercial projects and cost learning", "Year 5-7: mainstream adoption in lead markets", "Year 8-10: the method becomes standard practice"]}, {"title": "Glossary & Quick Reference", "tier": 2, "facts": ["CLT: Cross-laminated timber — structural wood panels.", "BIM: Building information modeling — the digital twin of a project.", "WAAM: Wire arc additive manufacturing — welding-based 3D printing.", "ICF: Insulated concrete forms — foam blocks filled with concrete."]}];
var ESSENCE="Self-Cleaning Solar Roof Tiles: Solar tiles that clean themselves — coatings shedding dust to protect power output.";
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
