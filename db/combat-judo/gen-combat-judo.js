(function(){'use strict';
/* JAH Judo Combat Database generator — jahdb-combat-judo-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBJ-";
var FIELDS=["Foundations","Nage Waza","Katame Waza","Advanced Study"];
var TOPICS={
 "Foundations": [
  "Judo Reigi: Dojo Etiquette and Respect - Foundations",
  "Shisei: Natural Posture for Judo - Foundations",
  "Mae Ukemi: Forward Breakfall - Foundations",
  "Koho Ukemi: Back Breakfall - Foundations",
  "Yoko Ukemi: Side Breakfall - Foundations",
  "Zenpo Kaiten Ukemi: Forward Rolling Breakfall - Foundations",
  "Kuzushi: The Eight Directions of Balance Breaking - Foundations",
  "Tai Sabaki: Body Movement and Evasion - Foundations",
  "Ayumi Ashi and Tsugi Ashi: Judo Footwork - Foundations",
  "Kumikata: Gripping the Judo Uniform - Foundations"
 ],
 "Nage Waza": [
  "De Ashi Harai: Advancing Foot Sweep - Nage Waza",
  "O Soto Gari: Major Outer Reap - Nage Waza",
  "O Goshi: Major Hip Throw - Nage Waza",
  "Seoi Nage: Shoulder Throw - Nage Waza",
  "O Uchi Gari: Major Inner Reap - Nage Waza",
  "Ko Uchi Gari: Minor Inner Reap - Nage Waza",
  "Hiza Guruma: Knee Wheel - Nage Waza",
  "Tai Otoshi: Body Drop - Nage Waza",
  "Harai Goshi: Sweeping Hip Throw - Nage Waza",
  "Uchi Mata: Inner Thigh Throw - Nage Waza",
  "Tomoe Nage: Circle Throw - Nage Waza",
  "Sumi Gaeshi: Corner Reversal Throw - Nage Waza"
 ],
 "Katame Waza": [
  "Kesa Gatame: Scarf Hold - Katame Waza",
  "Kami Shiho Gatame: Upper Four Corner Hold - Katame Waza",
  "Yoko Shiho Gatame: Side Four Corner Hold - Katame Waza",
  "Nami Juji Jime: Normal Cross Choke - Katame Waza",
  "Hadaka Jime: Rear Naked Strangle - Katame Waza",
  "Juji Gatame: Cross Armlock - Katame Waza",
  "Tate Shiho Gatame: Mounted Four Corner Hold - Katame Waza",
  "Okuri Eri Jime: Sliding Lapel Choke - Katame Waza",
  "Ude Garami: Entangled Armlock - Katame Waza"
 ],
 "Advanced Study": [
  "Renraku Waza: Combination Throwing - Advanced Study",
  "Kaeshi Waza: Counter Techniques - Advanced Study",
  "Randori: Free Practice Method - Advanced Study"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Judo Technique Study — "+safe+"\n"
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
    demo:{kind:"judo-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-judo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-judo',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
