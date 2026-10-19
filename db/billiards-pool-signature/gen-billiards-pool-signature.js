(function(){'use strict';
/* JAH Billiards Pool Database generator — jahdb-billiards-pool-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-POOL-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The table, balls, and cue", "Stance, bridge, and grip", "Aiming: the ghost ball", "8-ball: the rack and the break", "8-ball: open table and choosing groups", "8-ball: calling shots and winning", "Fouls and ball in hand", "Cue ball basics: stop, follow, draw", "9-ball: rules and the break", "Chalking and the pre-shot routine", "Your first 8-ball game: a walkthrough", "Ball colors and numbers"], "Compounded": ["Position play: thinking three balls ahead", "English: sidespin and its effects", "Banks and kicks", "Safety play", "Pattern play in 8-ball", "The break, refined", "Jump shots: legal and effective", "Common fouls and how to avoid them", "Reading the table", "Stun shots and the tangent line", "Combination shots", "Carom shots"], "Advanced": ["Advanced position routes", "9-ball: the three-foul rule", "Tournament formats and league play", "The mental game of pool", "Advanced banks and kick systems", "Straight pool (14.1): the classic", "One-pocket: the thinking game", "Practice drills library", "Teaching pool", "Building a pool study routine"]};
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
    name:topic+" (Signature Edition)",
    title:topic+" (Signature Edition)",
    description:"SAMPLE RECORD (generated \u2014 structural sample, clearly labeled sample, not an archive record).\n\nA "+field.toLowerCase()+" study of \""+topic+"\" in the billiards pool database. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature",
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
var gen={version:"jahdb-billiards-pool-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("billiards-pool-signature",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
