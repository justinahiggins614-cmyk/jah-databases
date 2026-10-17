(function(){'use strict';
/* JAH The Green Beret Combatives Combat Database generator — jahdb-combat-green-beret-combatives-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBGB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What the Modern Army Combatives Program Is",
  "The Basic Fighting Stance",
  "The Clinch: Why Close the Distance",
  "Pummeling: Fighting for Inside Position",
  "The Plumb Position: Double Head Control",
  "Rear Breakfall: Falling Safely Backward",
  "Side Breakfall: Falling Safely Sideways",
  "The Guard: Concept and Posture",
  "The Mount: Concept and Posture",
  "Side Control: Concept and Posture",
  "Rear Mount: Concept and Posture",
  "Stand Up in Base: The Technical Stand-Up"
 ],
 "Compounded": [
  "Posture Within the Guard",
  "Pass the Guard: The Standing Pass",
  "Pass the Guard: The Knee Pass",
  "Achieve the Mount from Side Control",
  "Maintain the Mount: Low and High",
  "Escape the Mount: The Upa (Bridge and Roll)",
  "Escape the Mount: The Elbow Escape",
  "Side Control: Achieve and Escape",
  "Escape the Rear Mount",
  "Attack from the Mount: The Straight Armbar",
  "Attack from the Mount: The Bent Armlock (Paintbrush)",
  "The Rear Naked Choke"
 ],
 "Advanced": [
  "The Guillotine Choke from the Clinch",
  "The Double-Leg Takedown",
  "The Single-Leg Takedown",
  "The Foot Sweep",
  "The Hip Throw (O-goshi)",
  "Basic Striking: The Jab and Cross",
  "Basic Striking: Hooks and Uppercuts",
  "Knees and Elbows at Close Range",
  "Head Movement: Slip, Duck, Weave",
  "The Sprawl: Stopping the Takedown"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Combatives Study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"combatives-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-combat-green-beret-combatives-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("combat-green-beret-combatives",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();