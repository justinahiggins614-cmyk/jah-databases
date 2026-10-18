(function(){'use strict';
/* JAH Signature Historic Earthquakes Database generator — jahdb-historic-earthquakes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEHI-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Earthquakes Are",
  "The 1960 Valdivia Earthquake",
  "The 1964 Alaska Earthquake",
  "The 2004 Indian Ocean Earthquake",
  "The 2011 Tohoku Earthquake",
  "The 1906 San Francisco Earthquake",
  "The 1976 Tangshan Earthquake",
  "The 2008 Sichuan Earthquake",
  "The 2010 Haiti Earthquake",
  "The 2015 Nepal Earthquake",
  "The 1923 Great Kanto Earthquake"
 ],
 "Compounded": [
  "The 1556 Shaanxi Earthquake",
  "The 1755 Lisbon Earthquake",
  "The 1811-12 New Madrid Earthquakes",
  "The 1868 Arica Earthquake",
  "The 1908 Messina Earthquake",
  "The 1931 Hawke's Bay Earthquake",
  "The 1935 Quetta Earthquake",
  "The 1939 Erzincan Earthquake",
  "The 1960 Agadir Earthquake",
  "The 1970 Ancash Earthquake",
  "The 1985 Mexico City Earthquake",
  "The 1988 Armenia Earthquake"
 ],
 "Advanced": [
  "The 1995 Kobe Earthquake",
  "The 1999 Izmit Earthquake",
  "The 2001 Gujarat Earthquake",
  "The 2003 Bam Earthquake",
  "The 2005 Kashmir Earthquake",
  "The 2010 Maule Earthquake",
  "The 2016 Kaikoura Earthquake",
  "The 2023 Turkiye-Syria Earthquakes",
  "The 2010-2011 Canterbury Earthquakes",
  "Earthquake Early Warning Systems",
  "The Future of Seismic Safety"
 ]
};
var DEMOKIND="quake analyzer";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Magnitude energy calculator — "+safe+"\n"
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
    name:topic+' — earthquake record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A earthquake record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-historic-earthquakes-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('historic-earthquakes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
