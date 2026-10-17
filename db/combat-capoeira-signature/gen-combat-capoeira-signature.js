(function(){'use strict';
/* JAH The Capoeira Combat Signature Database generator — jahdb-combat-capoeira-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBCAPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Ginga: Capoeira's Foundational Sway (Signature Edition) - Foundations",
  "The Guard: Arm Position and Protection (Signature Edition) - Foundations",
  "Balanco: Shifting the Weight (Signature Edition) - Foundations",
  "Cocorinha: The Squatting Dodge (Signature Edition) - Foundations",
  "Esquiva Lateral: The Side Dodge (Signature Edition) - Foundations",
  "Esquiva Baixa: The Low Dodge (Signature Edition) - Foundations",
  "Meia-Lua de Frente: The Front Crescent Kick (Signature Edition) - Foundations",
  "Pisao: The Stomping Kick (Signature Edition) - Foundations",
  "Bloqueio Cruzado: The Crossed Block (Signature Edition) - Foundations",
  "Bencao: The Pushing Kick (Signature Edition) - Foundations",
  "Ponteira: The Snapping Front Kick (Signature Edition) - Foundations",
  "Joelhada: The Knee Strike (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Queixada: The Cross-Step Kick (Signature Edition) - Compounded",
  "Armada: The Spinning Inside Crescent Kick (Signature Edition) - Compounded",
  "Martelo: The Hammer Kick (Signature Edition) - Compounded",
  "Rabo de Arraia: The Stingray's Tail Kick (Signature Edition) - Compounded",
  "Au: The Cartwheel (Signature Edition) - Compounded",
  "Role: The Low Ground Spin (Signature Edition) - Compounded",
  "Negativa: The Negative Ground Position (Signature Edition) - Compounded",
  "Cabecada: The Headbutt (Signature Edition) - Compounded",
  "Bananeira: The Handstand (Signature Edition) - Compounded",
  "Vingativa: The Sweeping Takedown (Signature Edition) - Compounded",
  "Chapa: The Side Push Kick (Signature Edition) - Compounded",
  "Macaquinho: The One-Handed Side Flip (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Meia-Lua de Compasso: The Compass Crescent Kick (Signature Edition) - Advanced",
  "S-Dobrado: The Folded S Ground Escape (Signature Edition) - Advanced",
  "Parafuso: The Corkscrew Kick (Signature Edition) - Advanced",
  "Mortal: The Standing Back Flip (Signature Edition) - Advanced",
  "Au sem Mao: The No-Hand Cartwheel (Signature Edition) - Advanced",
  "Chamada: The Call Ritual of the Roda (Signature Edition) - Advanced",
  "Malicia: The Art of Deception (Signature Edition) - Advanced",
  "Jogo de Angola: The Slow Close Game (Signature Edition) - Advanced",
  "Jogo de Regional: The Fast Upright Game (Signature Edition) - Advanced",
  "Sequencia de Bimba: The Eight Teaching Sequences (Signature Edition) - Advanced"
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
var gen={version:'jahdb-combat-capoeira-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-capoeira-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
