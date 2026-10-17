(function(){'use strict';
/* JAH The Capoeira Combat Database generator — jahdb-combat-capoeira-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBCAP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Ginga: Capoeira's Foundational Sway - Foundations",
  "The Guard: Arm Position and Protection - Foundations",
  "Balanco: Shifting the Weight - Foundations",
  "Cocorinha: The Squatting Dodge - Foundations",
  "Esquiva Lateral: The Side Dodge - Foundations",
  "Esquiva Baixa: The Low Dodge - Foundations",
  "Meia-Lua de Frente: The Front Crescent Kick - Foundations",
  "Pisao: The Stomping Kick - Foundations",
  "Bloqueio Cruzado: The Crossed Block - Foundations",
  "Bencao: The Pushing Kick - Foundations",
  "Ponteira: The Snapping Front Kick - Foundations",
  "Joelhada: The Knee Strike - Foundations"
 ],
 "Compounded": [
  "Queixada: The Cross-Step Kick - Compounded",
  "Armada: The Spinning Inside Crescent Kick - Compounded",
  "Martelo: The Hammer Kick - Compounded",
  "Rabo de Arraia: The Stingray's Tail Kick - Compounded",
  "Au: The Cartwheel - Compounded",
  "Role: The Low Ground Spin - Compounded",
  "Negativa: The Negative Ground Position - Compounded",
  "Cabecada: The Headbutt - Compounded",
  "Bananeira: The Handstand - Compounded",
  "Vingativa: The Sweeping Takedown - Compounded",
  "Chapa: The Side Push Kick - Compounded",
  "Macaquinho: The One-Handed Side Flip - Compounded"
 ],
 "Advanced": [
  "Meia-Lua de Compasso: The Compass Crescent Kick - Advanced",
  "S-Dobrado: The Folded S Ground Escape - Advanced",
  "Parafuso: The Corkscrew Kick - Advanced",
  "Mortal: The Standing Back Flip - Advanced",
  "Au sem Mao: The No-Hand Cartwheel - Advanced",
  "Chamada: The Call Ritual of the Roda - Advanced",
  "Malicia: The Art of Deception - Advanced",
  "Jogo de Angola: The Slow Close Game - Advanced",
  "Jogo de Regional: The Fast Upright Game - Advanced",
  "Sequencia de Bimba: The Eight Teaching Sequences - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Capoeira Technique Study — "+safe+"\n"
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
    name:topic+' — capoeira combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A capoeira combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"capoeira-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-capoeira-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-capoeira',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
