(function(){'use strict';
/* JAH Medieval Wrestling Combat Database generator — jahdb-combat-medieval-wrestling-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBMW-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Ringen: The Medieval Wrestling Art",
  "The Wrestling Guard (Die Hut)",
  "Grips of the Old Art (Die Griffe)",
  "Closing the Distance (Eingehen)",
  "Balance, Posture, and the Strong Base",
  "Footwork of the Ring (Treten)",
  "Falling Without Harm (Der Fall)",
  "Partner Drilling the Medieval Way (Ueben)",
  "Conditioning: Stone, Rope, and Hill",
  "The Throw, Plainly Told (Der Wurf)",
  "Festival Customs: The Ring, the Judges, the Prize",
  "The Jacket Grip: Wrestling by the Clothes",
 ],
 "Compounded": [
  "Durchgehen: Going Through the Arms",
  "The Hip Throw (Hueftwurf)",
  "The Back Trip (Hintertritt)",
  "The Leg Hook (Beinhaken)",
  "The Waist Lock and Lift (Umfassen)",
  "The Shoulder Throw (Schulterwurf)",
  "The Headlock (Kopfschloss)",
  "The Straight Arm Lock - the Key of Fiore",
  "Breaking the Hold (Durchbruch)",
  "The Cross-Buttock (Kreuzhuefte)",
  "The Thigh Throw (Schenkelwurf)",
  "The Counter Throw (Konterwurf)",
 ],
 "Advanced": [
  "The Great Throw (Der Grosse Wurf)",
  "The Double Arm Lock",
  "The Neck Lever",
  "Wrestling at the Sword (Ringen am Schwert)",
  "The Drop Throw (Opferwurf)",
  "The Knee Lever on the Ground (Kniehebel)",
  "Choke Holds of the Old Books (Wuergen)",
  "The Masters: Fiore, Ott, Talhoffer, Auerswald",
  "The Bout Plan (Kampfplan)",
  "Living Traditions: Schwingen, Glima, Gouren",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Medieval Wrestling Technique Study — "+safe+"\n"
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
    demo:{kind:"medieval-wrestling-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-medieval-wrestling-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-medieval-wrestling',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
