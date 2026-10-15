(function(){'use strict';
/* JAH The Software Components Database generator — jahdb-software-components-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CMP-";
var FIELDS=["extension"];
var TOPICS={
 "extension": [
  "Plugins \u2014 extension",
  "Extensions \u2014 extension",
  "Add-ons \u2014 extension",
  "Applets \u2014 extension",
  "Widgets \u2014 extension",
  "Gadgets \u2014 extension",
  "Modules \u2014 extension",
  "Packages \u2014 extension",
  "Bundles \u2014 extension",
  "Components \u2014 extension",
  "Libraries \u2014 extension",
  "Shared Libraries \u2014 extension",
  "Static Libraries \u2014 extension",
  "Dynamic Link Libraries \u2014 extension",
  "Middleware \u2014 extension",
  "Frameworks \u2014 extension",
  "Micro-Frameworks \u2014 extension",
  "Dependencies \u2014 extension",
  "Shims \u2014 extension",
  "Polyfills \u2014 extension",
  "Wrappers \u2014 extension",
  "Device Drivers \u2014 extension",
  "Virtual Drivers \u2014 extension",
  "System Extensions \u2014 extension",
  "Kernel Modules \u2014 extension",
  "Scripts \u2014 extension",
  "Shell Scripts \u2014 extension",
  "Automation Scripts \u2014 extension",
  "Macros \u2014 extension",
  "Helper Applications \u2014 extension",
  "Utilities \u2014 extension",
  "Subroutines \u2014 extension",
  "Functions \u2014 extension",
  "Servlets \u2014 extension",
  "Background Workers \u2014 extension",
  "Sidecars \u2014 extension",
  "Agents \u2014 extension",
  "Telemetry Agents \u2014 extension",
  "Adapters \u2014 extension",
  "Connectors \u2014 extension",
  "Transpiler Plugins \u2014 extension",
  "Linter Rulesets \u2014 extension",
  "Theme Extensions \u2014 extension",
  "Language Packs \u2014 extension",
  "Decorators \u2014 extension",
  "Mixins \u2014 extension",
  "Job Workers \u2014 extension",
  "Monitoring Agents \u2014 extension",
  "API Wrappers \u2014 extension",
  "Helper Utilities \u2014 extension",
  "Font Libraries \u2014 extension",
  "Codec Libraries \u2014 extension",
  "Crypto Libraries \u2014 extension",
  "Math Libraries \u2014 extension",
  "GUI Toolkits \u2014 extension",
  "Testing Libraries \u2014 extension",
  "Serialization Libraries \u2014 extension",
  "HTTP Client Libraries \u2014 extension",
  "Database Drivers \u2014 extension",
  "Logging Libraries \u2014 extension"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Software Components — "+safe+"\n"
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
    name:topic+' — software component record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A software component record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-software-components-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('software-components',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
