(function(){'use strict';
/* JAH Famous Rebels and Revolutionaries Database generator — jahdb-famous-rebels-revolutionaries-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-REBEL-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Rebels and Revolutionaries: An Overview", "Spartacus", "Boudica", "Vercingetorix", "The Gracchi", "William Wallace", "Jan Hus", "Martin Luther (Reformer)", "Guy Fawkes", "Oliver Cromwell", "The American Revolutionaries"], "Compounded": ["Robespierre and the Terror", "Toussaint Louverture (Revolutionary)", "Simon Bolivar (Liberator)", "Giuseppe Garibaldi", "John Brown (Militant)", "The 1848 Revolutions", "The Paris Commune (1871)", "Emiliano Zapata", "Vladimir Lenin", "Rosa Luxemburg", "The Russian Revolution (1917)", "Mao Zedong (Revolutionary)"], "Advanced": ["Che Guevara", "Fidel Castro", "Ho Chi Minh (Revolutionary)", "The Cuban Revolution", "The Iranian Revolution (1979)", "1989: The Velvet Revolutions", "The Arab Spring (2011)", "The Color Revolutions", "Nonviolent Revolution", "The Counter-Revolution", "The Revolutionary's Ledger"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — famous-rebels-revolutionaries demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — revolutionary record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A revolutionary record of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"famous-rebels-revolutionaries-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-famous-rebels-revolutionaries-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("famous-rebels-revolutionaries",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
