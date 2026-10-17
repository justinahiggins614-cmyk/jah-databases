(function(){'use strict';
/* JAH The Eskrima Kali Arnis Combat Database generator — jahdb-combat-eskrima-kali-arnis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBEKA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Eskrima, Kali, and Arnis Are - Foundations",
  "The Stick: Baston, Yantok, and Rattan - Foundations",
  "The Grip: Holding the Stick Right - Foundations",
  "Stance and the Ready Position (Handa) - Foundations",
  "The Five Basic Angles (Numerado 1-5) - Foundations",
  "Footwork I: The Forward Triangle (Sulong) - Foundations",
  "Angles Six Through Twelve - Foundations",
  "The Twelve Basic Strikes (Labtik) - Foundations",
  "Footwork II: The Retreat Triangle (Atras) - Foundations",
  "Blocking: The Four Basic Defenses (Defensa) - Foundations",
  "The Abaniko: The Fan Strike - Foundations",
  "Solo Baston Drills: Shadow Striking - Foundations"
 ],
 "Compounded": [
  "Sinawali: The Double-Stick Weave - Compounded",
  "Heaven Six Sinawali - Compounded",
  "Redonda: The Circular Strike - Compounded",
  "Hubud-Lubud: Tie and Untie - Compounded",
  "Sombrada: Counter for Counter - Compounded",
  "Tapi-Tapi: Tapping and Clearing - Compounded",
  "Espada y Daga: Stick and Knife - Compounded",
  "Footwork III: Sidestepping and the Female Triangle - Compounded",
  "Panantukan: Empty-Hand Boxing - Compounded",
  "Gunting: The Scissor Trap - Compounded",
  "Knife Work I: Daga Grips and Angles - Compounded",
  "Disarming I: Snaking the Stick Away (Agaw Sandata) - Compounded",
  "Disarming II: Strips and Punyo Work - Compounded"
 ],
 "Advanced": [
  "Knife Work II: Live-Blade Awareness and Tapping - Advanced",
  "Cadena de Mano: The Chain of Hands - Advanced",
  "Dumog: Filipino Grappling and Wrestling - Advanced",
  "The Live Hand: Kamot as Second Weapon - Advanced",
  "Espada y Daga II: Advanced Live-Hand Control - Advanced",
  "Sparring I: Protected Contact (Laban Laro) - Advanced",
  "Free-Flow Sparring: The Switching Game - Advanced",
  "Multiple Opponents: Moving the Line - Advanced",
  "Mastery: Free-Flow Play - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Eskrima Kali Arnis Study — "+safe+"\n"
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
    name:topic+' — combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"eskrima-kali-arnis-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-eskrima-kali-arnis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-eskrima-kali-arnis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
