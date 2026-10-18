(function(){'use strict';
/* JAH The Artificial Organs Future Technology Database generator — jahdb-"futuretech-35-artificial-organs"-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT35-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The wooden leg: ancient prosthetics",
    "Blood transfusion",
    "The iron lung",
    "Dialysis: the artificial kidney",
    "The heart-lung machine",
    "Jarvik-7: the artificial heart",
    "The first heart transplant",
    "Cyclosporine: transplants take off",
    "LVADs: bridging to transplant",
    "The total artificial heart today",
    "Artificial pancreas",
    "Biohybrid hearts"
  ],
  "Compounded": [
    "Xenotransplantation: pig hearts",
    "Artificial lungs: ECMO advances",
    "The bioartificial kidney",
    "3D-printed hearts (scaffolds)",
    "The organ shortage",
    "Skin grafts: ancient to modern",
    "The first kidney transplant",
    "Heart valves: mechanical and tissue",
    "Lab-grown bladders",
    "HeartMate 3: the levitating pump",
    "The trachea scandal: a warning"
  ],
  "Advanced": [
    "Decellularized scaffolds",
    "Organoids: mini-organs",
    "Beta Bionics: the bionic pancreas",
    "Organ markets: the ethics",
    "Fully implantable artificial heart (projection)",
    "The artificial liver",
    "Biohybrid lungs",
    "The artificial immune system",
    "Whole-body organ replacement",
    "The working artificial organ set",
    "Organs on demand"
  ]
};
function demoProgram(topic,field,seed){
  return "# Artificial Organs Study \u2014 "+topic+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': "+JSON.stringify(topic)+", 'field': "+JSON.stringify(field)+", 'seed': "+seed+"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + '] (seed ' + str(r['seed']) + ')'\n"
   + "print(summarize(record))\n"
   + "print('Generated variant \u2014 not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 artificial organ record (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A artificial organ record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
    field:field,
    src:'signature',
    generated:true,
    disclaimer:'Generated variant \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Generated variant demo.'},
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-35-artificial-organs",name:"The Artificial Organs Future Technology Database"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-35-artificial-organs"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-35-artificial-organs",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
