(function(){'use strict';
/* JAH The Creative Writing Quest generator — jahdb-db-creative-writing-quest-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CWQS-";
var FIELDS=["Sparks","Craft","Stories"];
var TOPICS={
 "Sparks": [
  "The Daily Writing Habit (Signature Edition) - Sparks",
  "Freewriting: Unlock the Flow (Signature Edition) - Sparks",
  "Prompts That Ignite (Signature Edition) - Sparks",
  "Morning Pages (Signature Edition) - Sparks",
  "Observation: The Writer's Notebook (Signature Edition) - Sparks",
  "What If: The Engine of Fiction (Signature Edition) - Sparks",
  "Dreams as Material (Signature Edition) - Sparks",
  "Constraints That Free (Signature Edition) - Sparks",
  "Reading Like a Writer (Signature Edition) - Sparks",
  "The Idea File (Signature Edition) - Sparks",
  "Jealousy as Compass (Signature Edition) - Sparks",
  "Play: The Serious Work (Signature Edition) - Sparks"
 ],
 "Craft": [
  "Character: Want and Need (Signature Edition) - Craft",
  "Show, Don't Tell (Signature Edition) - Craft",
  "Dialogue That Sounds Real (Signature Edition) - Craft",
  "Setting as Character (Signature Edition) - Craft",
  "Point of View (Signature Edition) - Craft",
  "Tension on Every Page (Signature Edition) - Craft",
  "The First Line (Signature Edition) - Craft",
  "Description Without Drowning (Signature Edition) - Craft",
  "Flashbacks That Work (Signature Edition) - Craft",
  "Voice: Your Fingerprint (Signature Edition) - Craft",
  "Revision: The Real Writing (Signature Edition) - Craft",
  "Subtext: What Isn't Said (Signature Edition) - Craft"
 ],
 "Stories": [
  "Three-Act Structure (Signature Edition) - Stories",
  "The Hero's Journey (Signature Edition) - Stories",
  "Plotting vs Pantsing (Signature Edition) - Stories",
  "The Sagging Middle (Signature Edition) - Stories",
  "Endings That Resonate (Signature Edition) - Stories",
  "Short Stories: Complete Worlds (Signature Edition) - Stories",
  "Novels: The Long Game (Signature Edition) - Stories",
  "Getting Feedback (Signature Edition) - Stories",
  "Publishing Paths (Signature Edition) - Stories",
  "Your Writing Life (Signature Edition) - Stories"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Creative Writing Study — "+safe+"\n"
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
    name:topic+' — writing lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A writing lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"creative-writing-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-creative-writing-quest-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-creative-writing-quest-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
