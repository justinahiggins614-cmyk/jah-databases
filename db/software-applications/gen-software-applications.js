(function(){'use strict';
/* JAH The Software Applications Database generator — jahdb-software-applications-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-APP-";
var FIELDS=["execution"];
var TOPICS={
 "execution": [
  "Native Applications \u2014 execution",
  "Cross-Platform Applications \u2014 execution",
  "Web Applications \u2014 execution",
  "Progressive Web Applications \u2014 execution",
  "Single-Page Applications \u2014 execution",
  "Multi-Page Applications \u2014 execution",
  "Hybrid Applications \u2014 execution",
  "Mobile Applications \u2014 execution",
  "Native Mobile Apps \u2014 execution",
  "Desktop Applications \u2014 execution",
  "Command-Line Applications \u2014 execution",
  "Terminal UI Applications \u2014 execution",
  "Graphical UI Applications \u2014 execution",
  "Headless Applications \u2014 execution",
  "Daemon Services \u2014 execution",
  "Background Services \u2014 execution",
  "System Services \u2014 execution",
  "Windows Services \u2014 execution",
  "Microservices \u2014 execution",
  "Serverless Functions \u2014 execution",
  "Cloud-Native Applications \u2014 execution",
  "Distributed Applications \u2014 execution",
  "Peer-to-Peer Applications \u2014 execution",
  "Decentralized Applications \u2014 execution",
  "Edge Applications \u2014 execution",
  "Embedded Applications \u2014 execution",
  "Real-Time Applications \u2014 execution",
  "Hard Real-Time Applications \u2014 execution",
  "Soft Real-Time Applications \u2014 execution",
  "Batch Applications \u2014 execution",
  "Containerized Applications \u2014 execution",
  "Sandboxed Applications \u2014 execution",
  "Virtualized Applications \u2014 execution",
  "Monolithic Applications \u2014 execution",
  "Event-Driven Applications \u2014 execution",
  "Interactive Applications \u2014 execution",
  "Real-Time Streaming Applications \u2014 execution",
  "Stateless Applications \u2014 execution",
  "Stateful Applications \u2014 execution",
  "WebAssembly Applications \u2014 execution",
  "Legacy Applications \u2014 execution",
  "Kiosk Applications \u2014 execution",
  "Portable Applications \u2014 execution",
  "Single-File Executables \u2014 execution",
  "Multi-Tenant Applications \u2014 execution",
  "Self-Contained Applications \u2014 execution",
  "Console Applications \u2014 execution",
  "Overlay Applications \u2014 execution",
  "System Tray Applications \u2014 execution",
  "Launch Daemons and Agents \u2014 execution",
  "Multi-Platform Applications \u2014 execution",
  "Text-Mode Applications \u2014 execution",
  "Bare-Metal Executables \u2014 execution",
  "Driver Applications \u2014 execution",
  "Distributed Batch Systems \u2014 execution",
  "Batch Processing Systems \u2014 execution",
  "Streaming Media Applications \u2014 execution",
  "Collaboration Applications \u2014 execution",
  "Productivity Suites \u2014 execution",
  "Creative Suites \u2014 execution"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Software Applications — "+safe+"\n"
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
    name:topic+' — software application record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A software application record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-software-applications-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('software-applications',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
