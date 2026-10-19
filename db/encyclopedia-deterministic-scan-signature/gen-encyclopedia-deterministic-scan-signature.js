(function(){'use strict';
/* JAH The Deterministic X-Scan Encyclopedia Database (Signature Edition) generator — jahdb-encyclopedia-deterministic-scan-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EDXS-";
var FIELDS=["Biochemistry & Molecular Biology", "Cell & Tissue Biophysics", "Anatomy & Physiology", "Digestive System", "Neuroscience", "Ecology & Environment", "Ocean & Atmosphere", "Computer Science", "World History", "Economics, Culture & Society", "Capstone"];
var TOPICS={"Biochemistry & Molecular Biology": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Biochemistry & Molecular Biology", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Biochemistry & Molecular Biology", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Biochemistry & Molecular Biology", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Biochemistry & Molecular Biology", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Biochemistry & Molecular Biology", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Biochemistry & Molecular Biology"], "Cell & Tissue Biophysics": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Cell & Tissue Biophysics", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Cell & Tissue Biophysics", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Cell & Tissue Biophysics", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Cell & Tissue Biophysics", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Cell & Tissue Biophysics", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Cell & Tissue Biophysics"], "Anatomy & Physiology": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Anatomy & Physiology", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Anatomy & Physiology", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Anatomy & Physiology", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Anatomy & Physiology", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Anatomy & Physiology", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Anatomy & Physiology"], "Digestive System": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Digestive System", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Digestive System", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Digestive System", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Digestive System", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Digestive System", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Digestive System"], "Neuroscience": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Neuroscience", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Neuroscience", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Neuroscience", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Neuroscience", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Neuroscience", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Neuroscience"], "Ecology & Environment": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Ecology & Environment", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Ecology & Environment", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Ecology & Environment", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Ecology & Environment", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Ecology & Environment", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Ecology & Environment"], "Ocean & Atmosphere": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Ocean & Atmosphere", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Ocean & Atmosphere", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Ocean & Atmosphere", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Ocean & Atmosphere", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Ocean & Atmosphere", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Ocean & Atmosphere"], "Computer Science": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Computer Science", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Computer Science", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Computer Science", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Computer Science", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Computer Science", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Computer Science"], "World History": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 World History", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 World History", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 World History", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 World History", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 World History", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 World History"], "Economics, Culture & Society": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Economics, Culture & Society", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Economics, Culture & Society", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Economics, Culture & Society", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Economics, Culture & Society", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Economics, Culture & Society", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Economics, Culture & Society"], "Capstone": ["The Deterministic X-Scan Encyclopedia: structural study 1 \u2014 Capstone", "The Deterministic X-Scan Encyclopedia: structural study 2 \u2014 Capstone", "The Deterministic X-Scan Encyclopedia: structural study 3 \u2014 Capstone", "The Deterministic X-Scan Encyclopedia: structural study 4 \u2014 Capstone", "The Deterministic X-Scan Encyclopedia: structural study 5 \u2014 Capstone", "The Deterministic X-Scan Encyclopedia: structural study 6 \u2014 Capstone"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Deterministic X-Scan Encyclopedia — structural study\n"
   + "# Track: "+field+"\n"
   + "record = {'entry': \""+safe+"\", 'track': \""+field+"\"}\n"
   + "print(record['entry'] + ' — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — structural study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
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
var gen={version:'jahdb-encyclopedia-deterministic-scan-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('encyclopedia-deterministic-scan-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
