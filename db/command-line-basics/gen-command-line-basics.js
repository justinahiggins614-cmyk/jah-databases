(function(){'use strict';
/* JAH Public Command Line Basics Database generator — jahdb-command-line-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CLI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is the Command Line",
  "Opening a Terminal",
  "Command Anatomy",
  "Navigating Directories on the Command Line",
  "Listing Files on the Command Line",
  "Creating and Removing on the Command Line",
  "Copying and Moving on the Command Line",
  "Reading Files on the Command Line",
  "Tab Completion on the Command Line",
  "Command History on the Command Line",
  "Getting Help on the Command Line"
 ],
 "Compounded": [
  "Wildcards and Globbing",
  "Redirection Deep Dive",
  "Pipes Deep Dive",
  "grep in Depth",
  "sed Basics",
  "awk Basics",
  "sort and uniq",
  "wc Counting",
  "find in Depth",
  "xargs",
  "Environment Variables in Depth",
  "Aliases on the Command Line"
 ],
 "Advanced": [
  "Shell Scripting on the Command Line",
  "Shell Variables and Loops",
  "Shell Conditionals",
  "Shell Functions",
  "Exit Codes on the Command Line",
  "Job Control on the Command Line",
  "SSH on the Command Line",
  "curl and wget Downloading",
  "tmux and screen Terminal Multiplexers",
  "Text Processing Pipelines",
  "Regex Mastery on the Command Line"
 ]
};
var DEMOKIND="command-line-basics-demo";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\');
  return 'console.log('+JSON.stringify('Topic: '+safe)+');\n'
       + 'console.log('+JSON.stringify('Field: '+field)+');\n'
       + 'console.log("Sample record - structural sample, not an archive entry.");\n';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — command line record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A command line record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'javascript',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-command-line-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('command-line-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();