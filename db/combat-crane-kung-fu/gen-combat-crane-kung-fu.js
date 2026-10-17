(function(){'use strict';
/* JAH Crane Kung Fu Combat Database generator — jahdb-combat-crane-kung-fu-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBCRN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": ["The White Crane Salute (Bai He Li)",
 "Crane Beak Hand (He Zui)",
 "Crane Wing Arms (Bai He Liang Chi)",
 "Golden Rooster Single-Leg Stance (Jin Ji Du Li)",
 "The Crane Guard Posture (He Shi)",
 "Abdominal Crane Breathing (Fu Xi Hu Xi)",
 "Triangle Footwork (San Jiao Bu)",
 "Crane Side Evasion Step (Ce Shan Bu)",
 "Crane Pivot Turn (Zhuan Shen)",
 "Basic Beak Wrist Conditioning (He Zui Lian Xi)",
 "Solo Pecking Drill (Zhuo Ji)",
 "Wing Cover Partner Drill (He Chi Dui Lian)"],
 "Compounded": ["Single Beak Peck (Dan He Zui)",
 "Double Beak Strike (Shuang He Zui)",
 "Crane Wing Double Slap (Shuang He Chi)",
 "Beak Hook and Pull (Gou La)",
 "Crane Elbow (He Zhou)",
 "Crane Knee (Ding Xi)",
 "Crane Sweeping Leg (Sao Tui)",
 "Leaping Crane Strike (Teng Kong He Ji)",
 "High Wing Block (Shang Peng)",
 "Low Wing Block (Xia Peng)",
 "Beak Parry and Counter (Lian Xiao Dai Da)",
 "Breaking the Wrist Grab (Tuo Shou)",
 "San Chian - The Three Battles Form",
 "Gong Li Quan - Power Training Form",
 "Bai He Quan - White Crane Fist Core Form",
 "Er Shi Quan - Twenty Movements Form",
 "Crane Walking Practice (He Xing Bu)"],
 "Advanced": ["Pak Hok Kuen - Tibetan White Crane Fist",
 "Beak Strikes to Vital Points (Dian Xue)",
 "Crane Two-Person Sparring Set (Dui Da)",
 "Iron Beak Conditioning (Tie Zui Gong)",
 "White Crane Free-Sparring Principles (San Shou)"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Crane Kung Fu Study -- "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record -- structural sample, not an archive entry.')\n";
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
    demo:{kind:"crane-kung-fu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-crane-kung-fu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-crane-kung-fu',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
