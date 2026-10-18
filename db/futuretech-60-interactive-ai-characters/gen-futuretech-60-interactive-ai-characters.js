(function(){'use strict';
/* JAH The Interactive AI Characters Future Technology Database generator — jahdb-futuretech-60-interactive-ai-characters-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT60-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Ancient: the Told-Again Character - Foundations",
  "1887: Sherlock Holmes - the Persistent Character - Foundations",
  "1974: D&D - You Become the Character - Foundations",
  "1980: Zork - Characters You Can Talk To - Foundations",
  "1980: MUDs - Characters Live Online - Foundations",
  "1996: Tamagotchi - the Character Needs You - Foundations",
  "1996: Creatures - Pets That Learn - Foundations",
  "2001: Black & White - the Creature You Raise - Foundations",
  "2005: Nintendogs - Pocket Companions - Foundations",
  "2011: Siri - the Phone Gets Personality - Foundations",
  "2015: Undertale - Characters Who Remember You - Foundations"
 ],
 "Compounded": [
  "2016: Westworld - Drama of the Hosts - Compounded",
  "2018: Detroit - Branching Persons - Compounded",
  "2020: the Model Becomes a Cast - Compounded",
  "2022: Character.AI - Fictional Friends - Compounded",
  "2023: Companions Go Mainstream - Compounded",
  "2023: Meta's AI Characters - Compounded",
  "2024: Story-Living Apps - Compounded",
  "2024: Persistent Story Worlds - Compounded",
  "2025: Games Ship Living NPCs - Compounded",
  "Characters with Lifelong Arcs - Compounded",
  "Characters That Age - Compounded",
  "Relationships That Deepen - Compounded"
 ],
 "Advanced": [
  "Characters Crossing Stories - Advanced",
  "Reader-Shaped Growth - Advanced",
  "Characters with Jobs and Lives - Advanced",
  "Graceful Farewells - Advanced",
  "Shared Character Canon - Advanced",
  "Characters Who Teach - Advanced",
  "Gentle Companions - Advanced",
  "Character Rights Frameworks - Advanced",
  "Persistent Ensemble Casts - Advanced",
  "The Living Library - Advanced",
  "Living Fictional Friends - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — interactive AI character record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A interactive AI character record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-60-interactive-ai-characters-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-60-interactive-ai-characters-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-60-interactive-ai-characters',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
