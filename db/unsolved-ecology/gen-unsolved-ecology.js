(function(){'use strict';
/* JAH The Unsolved Ecology Database generator — jahdb-unsolved-ecology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USCY-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why the Tropics Hold So Many Species - Foundations",
  "What Sets How Many Species a Place Can Hold - Foundations",
  "Why Some Invasions Succeed and Others Fail - Foundations",
  "Why Predator and Prey Numbers Rise and Fall - Foundations",
  "Why Ecosystems Sometimes Collapse All at Once - Foundations",
  "What Decides Which Species Go Extinct - Foundations",
  "How Many Species an Ecosystem Needs to Work - Foundations",
  "What Microbes Actually Do in Ecosystems - Foundations",
  "Why Some Forests Never Come Back After Disturbance - Foundations",
  "What Keeps Food Webs From Unraveling - Foundations",
  "How Far Seeds, Spores, and Larvae Really Travel - Foundations",
  "Why Some Restorations Bloom and Others Fail - Foundations"
 ],
 "Compounded": [
  "How Trophic Cascades Really Work - Compounded",
  "Does the Intermediate Disturbance Hypothesis Hold Up? - Compounded",
  "What Really Controls Ecosystem Productivity - Compounded",
  "Neutral Theory Versus Niche Theory: Who Is Right? - Compounded",
  "The Paradox of the Plankton: Why So Many Coexist - Compounded",
  "Does Biodiversity Dilute Disease? - Compounded",
  "The Forest Carbon Question: Sink or Source in a Warmer World - Compounded",
  "Does Biodiversity Really Make Ecosystems Stable? - Compounded",
  "Dispersal or Local Forces: What Assembles Communities? - Compounded",
  "Do Plant-Soil Feedbacks Explain Forest Diversity? - Compounded",
  "Can We See Ecosystem Collapse Coming? - Compounded",
  "How the Past Haunts Ecosystems - Compounded"
 ],
 "Advanced": [
  "Can We Predict Ecosystem Collapse Quantitatively? - Advanced",
  "Why Are Rainforests Hyperdiverse? - Advanced",
  "The Uncultured Majority: What Unknown Microbes Do - Advanced",
  "Can One Law Scale From Cells to Ecosystems? - Advanced",
  "What Happens in Ecosystems With No Past Analog? - Advanced",
  "May's Paradox: Why Complexity Does Not Always Destabilize - Advanced",
  "Do Rare Species Matter, or Are They Redundant? - Advanced",
  "How Ecosystems Feed Each Other Across Boundaries - Advanced",
  "Can We Truly Measure What Ecosystems Are Worth? - Advanced",
  "What Would a Complete Theory of Ecology Look Like? - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Ecology Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-ecology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-unsolved-ecology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-ecology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
