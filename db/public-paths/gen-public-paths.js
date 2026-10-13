(function(){'use strict';
/* JAH Public Paths Database generator — jahdb-public-paths-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PATH-';
var FIELDS=["trade-routes", "historic-roads", "pilgrimage-routes", "american-roads", "european-paths", "asian-paths", "cycling-routes"];
var TOPICS={
 "american-roads":["Route 66","Lincoln Highway"],
 "asian-paths":["Tokaido Road","Ho Chi Minh Trail","Israel National Trail (path sections)","Abraham Path","Transcaucasian Trail"],
 "cycling-routes":["Danube Cycle Path","Loire à Vélo","Rhine Cycle Route"],
 "european-paths":["The Ridgeway","Stevenson Trail (GR70)","St Cuthbert's Way","Offa's Dyke Path","Hadrian's Wall Path","Cotswold Way","South Downs Way","Thames Path","Sultan's Trail","Rob Roy Way","Great Glen Way","Speyside Way","GR34 Sentier des Douaniers","Cleveland Way","Peddars Way & Norfolk Coast Path"],
 "historic-roads":["Qhapaq Ñan (Inca Road System)","Persian Royal Road","Via Appia","Roman Road Network","Via Egnatia","Grand Trunk Road","King's Highway (Via Maris)","Darb Zubaydah","Natchez Trace","Oregon Trail","Santa Fe Trail","Mormon Trail","Pony Express Route","Chisholm Trail","El Camino Real de las Californias","El Camino Real de Tierra Adentro"],
 "pilgrimage-routes":["Via Francigena","Via de la Plata","Camino Portugués","Chemin du Puy (GR65)","St. Olav's Way (Pilegrimsleden)","Pilgrim's Way (Canterbury)","Kumano Kodo (pilgrimage network)","Shikoku 88 (pilgrimage circuit)","Char Dham Yatra","Kailash Kora","Camino del Norte","Camino Primitivo","Via di Francesco (St. Francis Way)","Camino de Invierno","Via Jacobi (Swiss Camino)"],
 "trade-routes":["Silk Road","Amber Road","Incense Route","Tea Horse Road"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Study Lab — "+safe+"\n"
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
    name:topic+' — path study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A path study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'path-chronicle',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-paths-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-paths',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
