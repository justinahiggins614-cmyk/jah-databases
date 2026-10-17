(function(){'use strict';
/* JAH Wing Chun Combat Database generator — jahdb-combat-wing-chun-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBWC-";
var FIELDS=["Foundations","Hand Techniques","Footwork","Forms","Chi Sao","Wooden Dummy","Weapons"];
var TOPICS={
 "Foundations": [
  "The Centerline Theory (Jung Sin) - Foundations",
  "Yee Jee Kim Yeung Ma: The Basic Stance - Foundations",
  "Man Sau and Wu Sau: The Guard - Foundations"
 ],
 "Hand Techniques": [
  "Yat Jee Chung Kuen: The Vertical Punch - Hand Techniques",
  "Lin Wan Kuen: Chain Punching - Hand Techniques",
  "Tan Sau: The Dispersing Hand - Hand Techniques",
  "Bong Sau: The Wing Arm - Hand Techniques",
  "Fook Sau: The Controlling Hand - Hand Techniques",
  "Pak Sau: The Slapping Hand - Hand Techniques",
  "Lap Sau: The Pulling Hand - Hand Techniques",
  "Jut Sau: The Jerking Hand - Hand Techniques",
  "Kwan Sau: The Rotating Hand - Hand Techniques",
  "Gaun Sau: The Splitting Hand - Hand Techniques",
  "Huen Sau: The Circling Hand - Hand Techniques",
  "Gan Sau: The Low Plowing Hand - Hand Techniques",
  "Biu Sau: The Thrusting Hand - Hand Techniques",
  "Lin Siu Dai Da: Simultaneous Attack and Defense - Hand Techniques",
  "Wing Chun Self-Defense: The Application Framework - Hand Techniques"
 ],
 "Footwork": [
  "Seung Ma and Tui Ma: Advancing and Retreating - Footwork",
  "Juen Ma: Turning the Stance - Footwork",
  "Wing Chun Kicks: Front and Side Kicks - Footwork"
 ],
 "Forms": [
  "Siu Nim Tau: The First Form - Forms",
  "Chum Kiu: The Second Form - Forms",
  "Biu Jee: The Third Form - Forms"
 ],
 "Chi Sao": [
  "Dan Chi Sao: Single-Hand Sticking - Chi Sao",
  "Luk Sao: Double-Hand Rolling - Chi Sao",
  "Lop Sao Drills: Attack and Defense Cycles - Chi Sao",
  "Chi Gerk: Sticky Legs - Chi Sao",
  "Lat Sau Jik Chung: Free Sparring - Chi Sao",
  "Gor Sao: Free Sticking Hands - Chi Sao"
 ],
 "Wooden Dummy": [
  "Mook Yan Jong: The Wooden Dummy Form - Wooden Dummy",
  "Biu Ma: Dummy Footwork and Angles - Wooden Dummy"
 ],
 "Weapons": [
  "Bart Cham Dao: The Eight-Cut Knives - Weapons",
  "Luk Dim Boon Kwan: The Six-and-a-Half-Point Pole - Weapons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Wing Chun Study — "+safe+"\n"
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
    demo:{kind:"wing-chun-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-wing-chun-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-wing-chun',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
