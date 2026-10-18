(function(){'use strict';
/* JAH The Personal AI Operating Systems Future Technology Database generator — jahdb-futuretech-86-personal-ai-operating-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT86-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1981: MS-DOS - Foundations",
  "1984: the Mac - Foundations",
  "1985: Windows - Foundations",
  "1997: Clippy - Foundations",
  "2001: OS X - Foundations",
  "2007: the iPhone - Foundations",
  "2008: Android - Foundations",
  "2011: Siri - the Voice Assistant Era - Foundations",
  "2014: Alexa - the Smart Speaker - Foundations",
  "2016: Google Assistant - Foundations",
  "2017: Bixby - Foundations"
 ],
 "Compounded": [
  "2018: Duplex - Compounded",
  "2020: Voice Matures - Compounded",
  "2021: AI-First OS - Compounded",
  "2022: ChatGPT - AI Becomes Conversational - Compounded",
  "2023: Copilot - Compounded",
  "2023: the AI Pin - Compounded",
  "2024: Rabbit R1 - Compounded",
  "2024: Apple Intelligence - Compounded",
  "2025: Agentic OS - Compounded",
  "The AI OS - Compounded",
  "The Ambient Computer - Compounded",
  "Personal Superintelligence - Compounded"
 ],
 "Advanced": [
  "The OS That Knows You - Advanced",
  "The Proactive Assistant - Advanced",
  "The Device Disappears - Advanced",
  "The AI Companion OS - Advanced",
  "The Universal Interface - Advanced",
  "The Trusted OS - Advanced",
  "The Post-Screen Computer - Advanced",
  "The Personal AI Cloud - Advanced",
  "The Sentient Desktop - Advanced",
  "The OS Economy - Advanced",
  "Everyday AI OS - Working Version - Advanced"
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
    name:topic+' — personal AI OS record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A personal AI OS record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-86-personal-ai-operating-systems-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-86-personal-ai-operating-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-86-personal-ai-operating-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
