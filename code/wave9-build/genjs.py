#!/usr/bin/env python3
"""Emit REAL working client-side generator JS for gen-* (GENERATOR class) items.
The JS generator is the single source of truth: node runs it to produce the
34 sample records for the data shard. Deterministic: same seed -> same plan."""
import json
import sys
sys.path.insert(0, '/home/hatch/workspace/jah-databases/code/wave9-build')
import records as R

JS_TPL = r'''(function(){'use strict';
/* JAH __NAME__ — real working generator, jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL generator: deterministic complete plans from the topic bank.
   Same seed -> same plan. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX=__PREFIX__;
var SLUG=__SLUGQ__;
var FIELDS=["Foundations","Compounded","Advanced"];
var STANDARDS=__STANDARDS__;
var CITATIONS=__CITATIONS__;
var BANK=[
__BANK__
];
var TIPS=__TIPS__;
function money(n){return "$"+n.toFixed(2);}
function planDiy(tp,rnd){
  var total=0,i;
  for(i=0;i<tp.mats.length;i++)total+=tp.mats[i][2];
  var tip=pick(TIPS,rnd);
  var L=[];
  L.push("COMPLETE PLAN: "+tp.t);
  L.push("");
  L.push("Overview: "+tp.notes+" Estimated hands-on time "+tp.time+" ("+tp.level+" level). Maker tip: "+tip);
  L.push("");
  L.push("Materials ("+tp.mats.length+" items, about "+money(total)+"):");
  for(i=0;i<tp.mats.length;i++)L.push("  - "+tp.mats[i][0]+" ("+tp.mats[i][1]+") ~"+money(tp.mats[i][2]));
  L.push("");
  L.push("Tools: "+(tp.tools.length?tp.tools.join(", "):"basic hand tools"));
  L.push("");
  L.push("Steps:");
  for(i=0;i<tp.steps.length;i++)L.push("  "+(i+1)+". "+tp.steps[i]);
  L.push("");
  L.push("Timeline: split "+tp.time+" into "+(tp.steps.length>6?"three":"two")+" sessions; never rush the final fitting and finish.");
  L.push("Safety: "+tp.safety);
  var hiw="This plan works because each stage prepares the next: measure and cut before joining, join before finishing. "+
    tp.notes+" Work the steps in order, and when a step resists, re-measure rather than forcing it. Safety is part of the method: "+tp.safety+".";
  var kp=["About "+money(total)+" in materials ("+tp.mats.length+" items).",
    "Roughly "+tp.time+" of hands-on work ("+tp.level+" level).",
    "Key technique: "+tp.notes.split(".")[0]+".",
    "Tools: "+(tp.tools.length?tp.tools.slice(0,6).join(", "):"basic hand tools")+".",
    "Safety: "+tp.safety+".",
    "Maker tip: "+tip];
  var req=["Materials: "+tp.mats.map(function(m){return m[0]+" ("+m[1]+")";}).join("; "),
    "Tools: "+(tp.tools.length?tp.tools.join(", "):"basic hand tools"),
    "Safety gear: "+tp.safety];
  return {description:L.join("\n"),how_it_works:hiw,key_points:kp,requirements:req};
}
function planGm(tp,rnd){
  var tip=pick(TIPS,rnd);
  var L=[];
  L.push("COMPLETE CONCEPT PLAN: "+tp.t);
  L.push("");
  L.push("Concept: "+tp.concept);
  L.push("");
  L.push("Mechanism: "+tp.mechanism);
  L.push("");
  L.push("Parts: "+tp.parts.join(", "));
  L.push("");
  L.push("Validation path: "+tp.build+" Expect about "+tp.time+" of work at "+tp.level+" level. Maker tip: "+tip);
  L.push("Safety: "+tp.safety);
  var hiw="The mechanism is the heart of it: "+tp.mechanism+" Prototype the core interaction first — "+
    "mock up the mechanics in cardboard, breadboard any electronics, and test before enclosing. "+tp.build+" Safety: "+tp.safety+".";
  var kp=["Core mechanism: "+tp.mechanism+".",
    "Key parts: "+tp.parts.slice(0,6).join(", ")+".",
    "About "+tp.time+" of work ("+tp.level+" level).",
    "Prototype the mechanism before the enclosure.",
    "Safety: "+tp.safety+".",
    "Maker tip: "+tip];
  var req=["Parts: "+tp.parts.join(", "),
    "Validation: "+tp.build,
    "Safety: "+tp.safety];
  return {description:L.join("\n"),how_it_works:hiw,key_points:kp,requirements:req};
}
function demoProgram(tp){
  var L=[];
  L.push("#!/usr/bin/env python3");
  L.push('"""'+String(tp.t).replace(/"/g,"'")+' — generated plan demo.');
  L.push("Property of Justin Addam Higgins (JAH).");
  L.push('"""');
  if(tp.kind==="diy"){
    L.push("MATS="+JSON.stringify(tp.mats.map(function(m){return [m[0],m[2]];})));
    L.push("def main():");
    L.push("    total=sum(c for _,c in MATS)");
    L.push('    print("Plan: '+String(tp.t).replace(/"/g,"'")+'")');
    L.push('    for n,c in MATS: print("  %-28s $%6.2f" % (n[:28],c))');
    L.push('    print("  %-28s $%6.2f" % ("TOTAL", total))');
    L.push('    print("OK: plan materials total $%.2f" % total)');
  }else{
    L.push("PARTS="+JSON.stringify(tp.parts));
    L.push("def main():");
    L.push('    print("Concept: '+String(tp.t).replace(/"/g,"'")+'")');
    L.push('    print("Parts (%d):" % len(PARTS))');
    L.push('    for p in PARTS: print("  - "+p)');
    L.push('    print("OK: %d parts listed" % len(PARTS))');
  }
  L.push('if __name__=="__main__": main()');
  return L.join("\n");
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var pool=BANK.filter(function(b){return !opts.field||b.tier===opts.field;});
  if(!pool.length)pool=BANK;
  var tp=(typeof opts.topicIndex==="number"&&BANK[opts.topicIndex])?BANK[opts.topicIndex]:pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,"0");
  var plan=tp.kind==="gm"?planGm(tp,rnd):planDiy(tp,rnd);
  var suf=__EDITION_SUFFIX__;
  return {
    id:id,t:tp.t+suf,g:tp.tier,name:tp.t+suf,title:tp.t+suf,
    description:"SAMPLE RECORD (generated — clearly labeled sample, not an archive record).\n\n"+plan.description,
    how_it_works:plan.how_it_works,
    key_points:plan.key_points,requirements:plan.requirements,
    standards:STANDARDS,citations:CITATIONS,
    src:"signature-generated-sample",sample:true,
    disclaimer:"Generated sample record — not an archive record. Seeded archive records are the authoritative entries.",
    ladder_tier:tp.tier,
    demo:{kind:"python",language:"python",program:demoProgram(tp),note:"Working demonstration program generated with this plan."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.src)e.push("src");
  if(!r.demo||!r.demo.program)e.push("demo");
  var d=String(r.description||"");
  if(d.indexOf("Materials")<0&&d.indexOf("Parts")<0)e.push("plan-materials");
  if(d.indexOf("Steps")<0&&d.indexOf("Validation")<0)e.push("plan-steps");
  if(d.indexOf("Safety")<0)e.push("plan-safety");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.g===record.g;});
  return dups.length?{ok:false,errors:["duplicate title+tier in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-"+SLUG+"-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
/*__NODE_RUNNER__*/
'''

TIPS = {
 'diy': ["Cut everything before you glue anything.", "Dry-fit twice, fasten once.",
         "Sharp tools are safe tools — hone before you start.", "Finish scraps first to test color.",
         "Label your parts as you cut them.", "Take a photo before disassembly for reference."],
 'gadget': ["Prototype the mechanism in cardboard first.", "Test with the cheapest parts that can work.",
            "Measure current draw before choosing a battery.", "Leave 20% headroom in every rating.",
            "Document the wiring before closing the case.", "User-test the interaction early."],
 'machine': ["Build one stage and test it before connecting the next.", "Time the real machine and tune to the math.",
             "Guard every pinch point before demonstrating.", "Level the base before trusting the tower.",
             "Keep a build log with measurements.", "Test to failure on purpose — once."],
}

def bank_entry(theme, title, tier, spec_d):
    tier_name = {'foundations': 'Foundations', 'compounded': 'Compounded', 'advanced': 'Advanced'}[tier]
    if theme == 'money':
        # map knowledge-record fields onto the generator bank shape
        return {'kind': 'gm', 't': title, 'tier': tier_name,
                'concept': spec_d['topic'], 'mechanism': spec_d['knowledge'],
                'parts': spec_d['actions'][:6] or ['study'],
                'build': spec_d['facts'], 'time': spec_d['time'],
                'level': spec_d['level'], 'safety': spec_d['caution'],
                'notes': spec_d['notes']}
    if theme == 'diy':
        return {'kind': 'diy', 't': title, 'tier': tier_name, 'notes': spec_d['notes'],
                'mats': [[n, q, c] for n, q, c in spec_d['materials']],
                'tools': spec_d['tools'], 'steps': spec_d['steps'],
                'time': spec_d['time'], 'level': spec_d['level'], 'safety': spec_d['safety']}
    p = R.parse_gm
    return {'kind': 'gm', 't': title, 'tier': tier_name, 'concept': spec_d['concept'],
            'mechanism': spec_d['mechanism'], 'parts': spec_d['parts'],
            'build': spec_d['build'], 'time': spec_d['time'],
            'level': spec_d['level'], 'safety': spec_d['safety'], 'notes': spec_d['notes']}

def build_gen_js(item, topics, prefix, edition=''):
    theme = item['theme']
    entries = []
    for (title, tier, spec) in topics:
        parse, _ = R.BUILDERS[theme]
        spec_d = parse(spec)
        e = bank_entry(theme, title, tier, spec_d)
        entries.append('  ' + json.dumps(e, ensure_ascii=False))
    bank = ',\n'.join(entries)
    tips = TIPS['diy'] if theme == 'diy' else (TIPS['machine'] if theme == 'machine' else TIPS['gadget'])
    js = JS_TPL
    js = js.replace('__NAME__', item['name'])
    js = js.replace('__SLUG__', item['slug'])
    js = js.replace('__SLUGQ__', json.dumps(item['slug']))
    js = js.replace('__PREFIX__', json.dumps(prefix))
    js = js.replace('__STANDARDS__', json.dumps(R.standards_for(theme, item['slug']), ensure_ascii=False))
    js = js.replace('__CITATIONS__', json.dumps(R.citations_for(theme, item['slug']), ensure_ascii=False))
    js = js.replace('__BANK__', bank)
    js = js.replace('__TIPS__', json.dumps(tips))
    js = js.replace('__EDITION_SUFFIX__', json.dumps(edition))
    js = js.replace('/*__NODE_RUNNER__*/', '')
    return js
