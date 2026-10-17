(function(){'use strict';
/* JAH Muay Boran Combat Signature Database generator — jahdb-combat-muay-boran-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBMBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Muay Boran Fighting Stance (Thaa Yang) (Signature Edition) - Foundations",
  "Muay Boran Footwork (Karn Yang) (Signature Edition) - Foundations",
  "The Nine Weapons of Muay Boran (Naw Arwut) (Signature Edition) - Foundations",
  "Wai Khru Ram Muay (The Teacher-Honoring Dance) (Signature Edition) - Foundations",
  "Mongkon and Prajioud (Sacred Headband and Armbands) (Signature Edition) - Foundations",
  "Card Chuek (Hemp Rope Hand Wraps) (Signature Edition) - Foundations",
  "The Muay Boran Guard (Signature Edition) - Foundations",
  "Muay Boran Body Conditioning (Signature Edition) - Foundations",
  "Triangular Stepping (Sao Chueak) (Signature Edition) - Foundations",
  "Muay Boran Forms Practice (Ram Mai) (Signature Edition) - Foundations",
  "The Five Regional Styles of Muay Boran (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Straight Punch (Mat Trong) (Signature Edition) - Compounded",
  "Hook Punch (Mat Wiang San) (Signature Edition) - Compounded",
  "Uppercut (Mat Soi Dao) (Signature Edition) - Compounded",
  "Horizontal Elbow (Sok Ti) (Signature Edition) - Compounded",
  "Upward Elbow (Sok Ngat) (Signature Edition) - Compounded",
  "Straight Knee (Khao Trong) (Signature Edition) - Compounded",
  "Curved Knee (Khao Khong) (Signature Edition) - Compounded",
  "Low Cutting Kick (Tae Khao) (Signature Edition) - Compounded",
  "Diagonal Roundhouse Kick (Tae Tat) (Signature Edition) - Compounded",
  "Front Push Kick (Thip Trong) (Signature Edition) - Compounded",
  "Clinch Entry and Control (Chap Kho) (Signature Edition) - Compounded",
  "Sweeps (Tad Kha) (Signature Edition) - Compounded",
  "The Ninth Weapon (Headbutt) (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Mae Mai (Master Tricks of Muay Boran) (Signature Edition) - Advanced",
  "Luk Mai (Complementary Tricks of Muay Boran) (Signature Edition) - Advanced",
  "Spinning Back Elbow (Sok Klap) (Signature Edition) - Advanced",
  "Hanuman Tawai Waen (Hanuman Presents the Ring) (Signature Edition) - Advanced",
  "Kwang Liow Lang (The Deer Looks Back) (Signature Edition) - Advanced",
  "Hap Liuk Muay (Grappling and Breaking) (Signature Edition) - Advanced",
  "Clinch Throws and Dumps (Thum) (Signature Edition) - Advanced",
  "Flying Knee (Khao Loi) (Signature Edition) - Advanced",
  "Combination Systems (Chaining the Nine Weapons) (Signature Edition) - Advanced",
  "The Kru (Teaching Lineage of Muay Boran) (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Muay Boran Study — "+safe+"\n"
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
    demo:{kind:"muay-boran-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-muay-boran-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-muay-boran-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
