(function(){'use strict';
/* JAH Impossible Programs Database generator — jahdb-impossible-programs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IP-";
var FIELDS=["command-line-tools","data-utilities","file-tools","text-tools","developer-tools","system-utilities"];
var TOPICS={
 "command-line-tools": [
  "Wordfreq \u2014 word frequency CLI",
  "Lexcount \u2014 word frequency CLI",
  "Termtally \u2014 word frequency CLI",
  "Vocabscan \u2014 word frequency CLI",
  "Wordrank \u2014 word frequency CLI",
  "Textprobe \u2014 word frequency CLI"
 ],
 "data-utilities": [
  "Csvsum \u2014 CSV column summarizer",
  "Colstat \u2014 CSV column summarizer",
  "Numscan \u2014 CSV column summarizer",
  "Csvprobe \u2014 CSV column summarizer",
  "Fieldavg \u2014 CSV column summarizer",
  "Datasum \u2014 CSV column summarizer",
  "Jsonlfilter \u2014 JSONL record filter (eq)",
  "Jsonlfilter \u2014 JSONL record filter (gt)",
  "Jsonlfilter \u2014 JSONL record filter (contains)",
  "Recfilter \u2014 JSONL record filter (eq)",
  "Recfilter \u2014 JSONL record filter (gt)",
  "Jsonscan \u2014 JSONL record filter (contains)",
  "Waypoint Auditor \u2014 timestamp monotonicity (live archive)",
  "Waypoint Auditor \u2014 coordinate bounds (live archive)",
  "Waypoint Auditor \u2014 segment speed plausibility (live archive)",
  "Waypoint Auditor \u2014 required fields present (live archive)",
  "Waypoint Auditor \u2014 id format and uniqueness (live archive)",
  "Waypoint Auditor \u2014 full audit report (live archive)"
 ],
 "file-tools": [
  "Dedup \u2014 duplicate file remover (keep first)",
  "Dedup \u2014 duplicate file remover (keep last)",
  "Uniquify \u2014 duplicate file remover (keep first)",
  "Uniquify \u2014 duplicate file remover (keep last)",
  "Dupeshave \u2014 duplicate file remover (keep first)",
  "Dupeshave \u2014 duplicate file remover (keep last)",
  "Treereport \u2014 directory tree size reporter",
  "Dirsize \u2014 directory tree size reporter",
  "Sizetree \u2014 directory tree size reporter",
  "Treereport \u2014 directory tree size reporter (2)",
  "Foldstat \u2014 directory tree size reporter",
  "Dirtreemap \u2014 directory tree size reporter"
 ],
 "text-tools": [
  "Tablefmt \u2014 text table formatter",
  "Mdtable \u2014 text table formatter",
  "Colalign \u2014 text table formatter",
  "Textgrid \u2014 text table formatter",
  "Asciitable \u2014 text table formatter",
  "Prettyrows \u2014 text table formatter",
  "Diffstat \u2014 line diff summarizer",
  "Linediff \u2014 line diff summarizer",
  "Changediff \u2014 line diff summarizer",
  "Diffsum \u2014 line diff summarizer",
  "Patchstat \u2014 line diff summarizer",
  "Diffstat \u2014 line diff summarizer (2)"
 ],
 "developer-tools": [
  "Linkcheck \u2014 documentation link checker",
  "Doclinks \u2014 documentation link checker",
  "Mdlinkscan \u2014 documentation link checker",
  "Linkaudit \u2014 documentation link checker",
  "Refcheck \u2014 documentation link checker",
  "Linkhunter \u2014 documentation link checker"
 ],
 "system-utilities": [
  "Passgen \u2014 password generator (16 chars, symbols)",
  "Passgen \u2014 password generator (20 chars, symbols)",
  "Passgen \u2014 password generator (12 chars, no symbols)",
  "Keyforge \u2014 password generator (24 chars, symbols)",
  "Safekey \u2014 password generator (16 chars, no symbols)",
  "Passgen \u2014 password generator (32 chars, symbols)"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Impossible Program — "+safe+"\n"
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
    name:topic+' — program record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A program record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"program-runner",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-impossible-programs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('impossible-programs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
