(function(){'use strict';
/* JAH Olympic History Signature Database generator — jahdb-olympic-history-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OLYHISS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Ancient Olympic Games (776 BC) (Signature Edition)", "Pierre de Coubertin and the Revival (Signature Edition)", "Athens 1896: The First Modern Games (Signature Edition)", "The Olympic Rings and Flag (Signature Edition)", "The Olympic Motto (Signature Edition)", "The Torch Relay Origin (Signature Edition)", "The Early Program: Sports of the First Games (Signature Edition)", "Women Enter the Games (1900) (Signature Edition)", "The Marathon Legend (Pheidippides) (Signature Edition)", "Olympic Charter Basics (Signature Edition)", "National Olympic Committees (Signature Edition)"], "Compounded": ["Berlin 1936 and Jesse Owens (Signature Edition)", "London 1948: The Austerity Games (Signature Edition)", "Cold War Rivalries (1952-1988) (Signature Edition)", "The Miracle on Ice (1980) (Signature Edition)", "Munich 1972: Tragedy and Legacy (Signature Edition)", "The Boycotts (1980 and 1984) (Signature Edition)", "Professionals Enter: The Dream Team (1992) (Signature Edition)", "Nadia Comaneci's Perfect 10 (1976) (Signature Edition)", "Mexico City 1968: The Protests (Signature Edition)", "Montreal 1976: The Debt Lesson (Signature Edition)", "Seoul 1988: The Ben Johnson Scandal (Signature Edition)", "Sydney 2000: Best Practices (Signature Edition)"], "Advanced": ["The IOC Session and Host Selection (Signature Edition)", "Agenda 2020 Reforms (Signature Edition)", "New Sports Admission Process (Signature Edition)", "Tokyo 2020: The Postponement (Signature Edition)", "Paris 2024: Gender Parity (Signature Edition)", "LA 2028: The Road Ahead (Signature Edition)", "Olympic Broadcasting Economics (Signature Edition)", "WADA and Anti-Doping Evolution (Signature Edition)", "The Paralympic Story (Signature Edition)", "Olympic Records vs World Records (Signature Edition)", "Venue Legacies: Successes and White Elephants (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# olympic-timeline-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 olympic history record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A olympic history record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"olympic-timeline-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-olympic-history-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('olympic-history-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
