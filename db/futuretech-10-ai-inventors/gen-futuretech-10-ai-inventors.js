(function(){'use strict';
/* JAH The AI Inventors Future Technology Database generator — jahdb-"futuretech-10-ai-inventors"-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT10-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The patent system rewards invention",
    "CAD: computers draw the designs",
    "Parametric and generative CAD",
    "Topology optimization: math designs parts",
    "Genetic algorithms evolve designs",
    "The 3D printer: designs become objects",
    "IBM's Watson designs recipes and materials",
    "Deep learning generates images and designs",
    "Autodesk Dreamcatcher: generative design",
    "AI discovers new molecules and drugs",
    "DABUS and the AI-inventor patent debate",
    "AlphaFold designs meet the wet lab"
  ],
  "Compounded": [
    "GNoME: millions of new materials",
    "AI chip design in production",
    "Text-to-3D: words become objects",
    "AI co-inventors in patent filings",
    "Foundation models for engineering",
    "Autonomous invention pipelines",
    "AI-designed products on shelves",
    "AI-designed drugs reach human trials",
    "The AI inventor's first true patent (projection)",
    "AI invents in unfamiliar physics",
    "Invention at machine speed"
  ],
  "Advanced": [
    "AI-designed manufacturing processes",
    "Open invention engines for everyone",
    "AI-architected buildings",
    "Self-improving invention systems",
    "AI invents new science instruments",
    "The patent system redesigned for AI",
    "Invention abundance and its discontents",
    "AI-designed cities and infrastructure",
    "The working AI inventor",
    "The invention singularity",
    "Human-AI invention teams"
  ]
};
function demoProgram(topic,field,seed){
  return "# AI Inventors Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 AI inventor record (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A AI inventor record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-10-ai-inventors",name:"The AI Inventors Future Technology Database"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-10-ai-inventors"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-10-ai-inventors",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
