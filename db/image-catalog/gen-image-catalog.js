(function(){'use strict';
/* JAH The Image Catalog Database generator — jahdb-image-catalog-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ICAT-";
var FIELDS=["art", "photography", "space", "landmarks", "diagrams", "portraits"];
var TOPICS={"art": ["Renaissance masterpiece", "Impressionist landmark", "Modern art icon"], "photography": ["Defining historical photograph", "Documentary landmark", "Iconic portrait photograph"], "space": ["Great observatory image", "Planetary landmark photo", "Deep-space icon"], "landmarks": ["World wonder view", "Iconic city landmark", "Beloved monument photograph"], "diagrams": ["Essential scientific diagram", "Historic map", "Landmark technical illustration"], "portraits": ["Definitive portrait", "Historic figure portrait", "Iconic portrait study"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "// Catalog entry demo — "+safe+"\n"
   + "// Category: "+field+"\n"
   + "const entry = { title: \""+safe+"\", category: \""+field+"\" };\n"
   + "console.log(entry.title + ' [' + entry.category + ']');\n"
   + "console.log('Sample record — structural sample, not an archive entry.');\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Entry"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — catalog entry (sample)',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A catalog entry for "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. Archive records carry the full verified entry with watch or view links.',
    category:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'catalog-sample',language:'javascript',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.category)<0)e.push('category');
  if(!r.src)e.push('src');
  if(!r.title||String(r.title).length<3)e.push('title');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.category===record.category;});
  return dups.length?{ok:false,errors:['duplicate title+category in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-image-catalog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-catalog',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
