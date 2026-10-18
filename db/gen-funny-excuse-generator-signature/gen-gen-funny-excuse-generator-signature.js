(function(){'use strict';
/* JAH Funny Excuse Generator - jahdb-gen-funny-excuse-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: combinatorial excuse assembly. Same seed, same excuse.
   signature edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX="JAH-HFEGS-";
var FIELDS=["Work", "School", "Social"];
var OPENERS={"Work": ["I was ready for the standup when", "I left early for the office, but", "I had the presentation open when", "I was about to join the call when"], "School": ["I finished the homework, but then", "I was walking to class when", "I had my assignment ready when", "I set three alarms, yet"], "Social": ["I was getting ready to come when", "I had the gift wrapped when", "I was out the door when", "I swear I was coming, but"]};
var CAUSES=["my cat staged a sit-in on my laptop", "a goose claimed my parking spot and defended it", "my GPS developed strong opinions about shortcuts", "the elevator achieved sentience and chose the scenic route", "a flash mob formed in my kitchen", "my coffee achieved independence and fled", "the Wi-Fi unionized and demanded better working conditions", "a squirrel moved into my car and started charging rent", "my alarm clock joined a band and went on tour", "the traffic cones organized a protest", "my shoes went on strike for better laces", "a pigeon stole my keys and flew to another zip code"];
var ESCALATIONS=["and then it brought friends", "which triggered an emergency neighborhood watch meeting", "so now there's a group chat about it with 47 members", "and the HOA has opened an investigation", "which is now local legend - ask anyone", "and I have the blurry photos to prove it"];
var CLOSERS=["I'm seeking counseling. For the goose.", "I've learned nothing, but I've lived.", "I'll be early tomorrow. Probably. Don't hold me to it.", "The cat has been formally reprimanded.", "I'm accepting thoughts, prayers, and snacks.", "This will be in my memoir. Chapter one."];
var SOURCE='signature';
function pick(r,arr){return arr[(r()*arr.length)|0];}
function assemble(seed,field){
  var r=prng(seed>>>0||1);
  var f=(field&&OPENERS[field])?field:pick(r,FIELDS);
  var o=pick(r,OPENERS[f]), c=pick(r,CAUSES), e=pick(r,ESCALATIONS), cl=pick(r,CLOSERS);
  return {field:f,opener:o,cause:c,escalation:e,closer:cl,
          excuse:o+' '+c+', '+e+'. '+cl};
}
function demoProgram(a){
  function q(s){return s.replace(/"/g,"'");}
  return '# Funny Excuse Generator - live excuse\nprint("SITUATION: '+q(a.field)+'")\nprint("OPENER:    '+q(a.opener)+'")\nprint("CAUSE:     '+q(a.cause)+'")\nprint("ESCALATION:'+q(a.escalation)+'")\nprint("CLOSER:    '+q(a.closer)+'")\nprint()\nprint("EXCUSE: '+q(a.excuse)+'")\nprint("OK: excuse assembled from 4 banks")\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var a=assemble(seed>>>0||1,opts.field||null);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  var title='Fresh Excuse: '+a.cause.charAt(0).toUpperCase()+a.cause.slice(1)+(SOURCE==='signature'?' (Signature Edition)':'');
  return {
    id:id,
    name:title+' — '+a.field,
    title:title,
    description:'GENERATED EXCUSE (live generator output - clearly labeled fiction). "'+a.excuse+'"',
    field:a.field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - fictional excuse, not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(a),note:'Live excuse demo program.'},
    _seed:seed>>>0||1, parts:a
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.parts||!r.parts.excuse)e.push('parts');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-funny-excuse-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,assemble:assemble};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-funny-excuse-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
