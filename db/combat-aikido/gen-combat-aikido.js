(function(){'use strict';
/* JAH The Aikido Combat Database generator — jahdb-combat-aikido-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBAIK-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Aikido Is: The Way of Harmony - Foundations and History",
  "The Founder: Morihei Ueshiba and the Birth of Aikido - Foundations and History",
  "The Aikido Dojo: Etiquette, Bowing, and Rei - Foundations and History",
  "Shisei and Kamae: Posture and the Hanmi Stance - Movement and Ukemi",
  "Ashi-sabaki: Footwork, Ayumi-ashi and Tsugi-ashi - Movement and Ukemi",
  "Tenkan and Irimi: Turning and Entering Movement - Movement and Ukemi",
  "Ukemi: Mae-ukemi, the Forward Roll - Movement and Ukemi",
  "Ukemi: Ushiro-ukemi and Yoko-ukemi, Back and Side Falls - Movement and Ukemi",
  "Kuzushi: Breaking the Partner's Balance - Core Principles",
  "Awase and Musubi: Blending and Connecting Energy - Core Principles",
  "Ma-ai: Distance, Timing, and Atemi Openings - Core Principles",
  "Grip Fundamentals: Katate-dori and Ryote-dori - Core Principles"
 ],
 "Compounded": [
  "Ikkyo: Ude-osae, the First Teaching - Wrist Controls: Kyo Waza",
  "Nikyo: Kote-mawashi, the Second Teaching - Wrist Controls: Kyo Waza",
  "Sankyo: Kote-hineri, the Third Teaching - Wrist Controls: Kyo Waza",
  "Yonkyo: Tekubi-osae, the Fourth Teaching - Wrist Controls: Kyo Waza",
  "Gokyo: Ude-nobashi, the Fifth Teaching - Wrist Controls: Kyo Waza",
  "Irimi-nage: The Entering Throw - Throws: Nage Waza",
  "Shihonage: The Four-Direction Throw - Throws: Nage Waza",
  "Kotegaeshi: The Wrist Turn-Back Throw - Throws: Nage Waza",
  "Jujinage: The Crossed-Arms Throw - Throws: Nage Waza",
  "Kaiten-nage: The Rotary Throw - Throws: Nage Waza",
  "Sumi-otoshi: The Corner Drop - Throws: Nage Waza",
  "Aiki-otoshi: The Aiki Drop - Throws: Nage Waza"
 ],
 "Advanced": [
  "Koshinage: Hip Throws - Throws: Nage Waza",
  "Udekime-nage: The Straight-Arm Throw - Throws: Nage Waza",
  "Katame-waza: Pins and Immobilizations - Pins and Freestyle",
  "Randori: Freestyle Practice Against Multiple Attackers - Pins and Freestyle",
  "Jiyu-waza: Free Technique Practice - Pins and Freestyle",
  "Tanto-dori: Knife Disarms - Weapons, Disarms, and Advanced Practice",
  "Tachi-dori and Jo-dori: Sword and Staff Disarms - Weapons, Disarms, and Advanced Practice",
  "Kaeshi-waza: Counter Techniques - Weapons, Disarms, and Advanced Practice",
  "Hanmi-handachi and Suwari-waza: Seated and Kneeling Techniques - Weapons, Disarms, and Advanced Practice",
  "Aiki-ken and Aiki-jo: Wooden Sword and Staff Forms - Weapons, Disarms, and Advanced Practice"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Aikido Study — "+safe+"\n"
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
    demo:{kind:"aikido-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-aikido-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-aikido',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
