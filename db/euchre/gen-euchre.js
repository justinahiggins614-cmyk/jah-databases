(function(){'use strict';
/* JAH Euchre Database generator — jahdb-euchre-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EUCH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Euchre: the 24-card deck and the goal", "Trump and the bowers", "The deal and the kitty", "Round one: ordering it up", "Round two: calling trump", "Going alone: the loner", "Playing the tricks: follow suit", "Scoring the hand", "Rank of cards in trump and non-trump", "Teams, seating, and rotation", "The upcard: reading round one", "Following suit and the renege rule"], "Compounded": ["Calling trump: round one vs round two", "The dealer’s dilemma: pick up or pass", "Leading strategy", "Second-hand play", "Trumping in and sloughing", "Going alone: the decision math", "Defending against a loner", "Counting trump", "Partner signals through play", "Score-based strategy: the endgame", "The eldest hand: first-seat strategy", "Trump management: drawing and holding"], "Advanced": ["Euchres and marches", "Stick the dealer and house rules", "Tournament euchre", "Bid euchre and bidding variants", "Reading the upcard", "Advanced loner hands", "Psychology of the call", "Teaching euchre", "Euchre variants around the world", "Building a euchre study routine"]};
function esc(s){return String(s).replace(/\\/g,"\\\\").replace(/"/g,"'");}
function demoProgram(topic,field,seed){
  var safe=esc(topic);
  var L=[];
  L.push("# "+safe+" — study demo (generated sample)");
  L.push("# Field: "+field+" | Seed: "+seed);
  L.push('TITLE = "'+safe+'"');
  L.push('FIELD = "'+field+'"');
  L.push("SEED = "+seed);
  L.push("def study_prompts(t):");
  L.push('    return [');
  L.push('        "State the single most important rule of " + t + ".",');
  L.push('        "Describe one concrete example of " + t + " in a real game.",');
  L.push('        "Name the most common beginner mistake with " + t + " and its fix.",');
  L.push("    ]");
  L.push("def check_sum(n):");
  L.push("    return n * (n + 1) // 2");
  L.push("def main():");
  L.push('    print("Study card: %s [%s]" % (TITLE, FIELD))');
  L.push("    for i, p in enumerate(study_prompts(TITLE), 1):");
  L.push('        print("  %d. %s" % (i, p))');
  L.push("    n = 10 + (SEED % 40)");
  L.push('    print("Arithmetic check: 1+...+%d = %d" % (n, check_sum(n)))');
  L.push('    print("OK: study demo complete for " + TITLE)');
  L.push('if __name__ == "__main__": main()');
  return L.join("\n")+"\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,"0");
  return {
    id:id,
    name:topic+" — euchre record record",
    title:topic+"",
    description:"SAMPLE RECORD (generated \u2014 structural sample, clearly labeled sample, not an archive record).\n\nA "+field.toLowerCase()+" study of \""+topic+"\" in the euchre database. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
    ladder_tier:field,
    demo:{kind:"study-demo",language:"python",program:demoProgram(topic,field,seed),note:"Study-card demo for the generated sample."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.src)e.push("src");
  if(!r.demo||!r.demo.program)e.push("demo");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:["duplicate title+field in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-euchre-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("euchre",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
