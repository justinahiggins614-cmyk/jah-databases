(function(){'use strict';
/* JAH Hanafuda Database generator — jahdb-hanafuda-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HAN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The 48 cards: months as suits", "The four card types: hikari, tane, tanzaku, kasu", "Reading the cards at a glance", "Koi-koi: setup and deal", "Koi-koi: the turn structure", "Koi-koi: capturing and the scoring area", "Koi-koi: making a yaku", "The koi-koi call: risk and reward", "Going out: agari and hand scoring", "Koi-koi yaku: the bright sets", "Koi-koi yaku: tane and tanzaku sets", "Kasu points and chaff strategy"], "Compounded": ["Hana-awase: introduction", "Hana-awase: rules and scoring", "Reading the opponent’s table", "Defensive play in koi-koi", "Month strategy and sequencing", "The rain man card", "Doubling, multipliers, and match scoring", "Hachi-hachi and other hanafuda games", "Card care and handling", "Koi-koi: the dealer’s edge", "Table talk and hanafuda etiquette", "Speed koi-koi and blitz variants"], "Advanced": ["Advanced koi-koi: yaku timing", "Koi-koi probability: counting the pile", "Comeback strategy: playing from behind", "Tournament koi-koi", "Teaching hanafuda", "History of hanafuda", "The art of the cards", "Collecting hanafuda decks", "Koi-koi endgame: the last six cards", "Building a hanafuda study routine"]};
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
    name:topic+" — hanafuda record record",
    title:topic+"",
    description:"SAMPLE RECORD (generated \u2014 structural sample, clearly labeled sample, not an archive record).\n\nA "+field.toLowerCase()+" study of \""+topic+"\" in the hanafuda database. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-hanafuda-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("hanafuda",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
