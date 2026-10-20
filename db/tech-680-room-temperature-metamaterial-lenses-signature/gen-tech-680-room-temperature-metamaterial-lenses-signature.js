(function(){'use strict';
/* JAH The Signature Room-Temperature Metamaterial Lenses Database generator — jahdb-tech-680-room-temperature-metamaterial-lenses-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET680S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Room-Temperature Metamaterial Lenses Is","The Current State of Room-Temperature Metamaterial Lenses","Core Principles of Room-Temperature Metamaterial Lenses","Key Vocabulary of Room-Temperature Metamaterial Lenses","Why Room-Temperature Metamaterial Lenses Matters"],"Compounded":["Piece 1 of Room-Temperature Metamaterial Lenses: Precursor Chemistry","Piece 2 of Room-Temperature Metamaterial Lenses: Synthesis Reactor","Piece 3 of Room-Temperature Metamaterial Lenses: Structure Control","Piece 4 of Room-Temperature Metamaterial Lenses: Characterization Suite","Piece 5 of Room-Temperature Metamaterial Lenses: Property Testing","Piece 6 of Room-Temperature Metamaterial Lenses: Scale Manufacturing","Piece 7 of Room-Temperature Metamaterial Lenses: Integration Engineering","Piece 8 of Room-Temperature Metamaterial Lenses: Lifecycle and Safety","How the Pieces of Room-Temperature Metamaterial Lenses Fit Together","Build Plan: Making Room-Temperature Metamaterial Lenses Step by Step"],"Advanced":["The Working Room-Temperature Metamaterial Lens: What a Real Build Looks Like","Simulation Program: Modeling Room-Temperature Metamaterial Lenses in Code","Testing and Verifying Room-Temperature Metamaterial Lenses","Safety, Limits, and Responsible Use of Room-Temperature Metamaterial Lenses","Scaling Room-Temperature Metamaterial Lenses to Production","The Full Teaching Ladder for Room-Temperature Metamaterial Lenses","Open Problems and Next Steps in Room-Temperature Metamaterial Lenses"]};;
var DEMOKIND="signature room-temperature metamaterial lens record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature room-temperature metamaterial lens record planner — "+safe+"\n"
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
    name:topic+' — signature room-temperature metamaterial lens record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature room-temperature metamaterial lens record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-tech-680-room-temperature-metamaterial-lenses-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-680-room-temperature-metamaterial-lenses-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
