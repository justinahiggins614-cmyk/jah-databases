(function(){'use strict';
/* JAH Tennis Technique Signature Database generator — jahdb-tennis-technique-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TENTECHS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Continental Grip (Signature Edition)", "Eastern Forehand Grip (Signature Edition)", "Ready Position and Split Step (Signature Edition)", "Forehand Groundstroke (Signature Edition)", "Two-Handed Backhand (Signature Edition)", "Serve Toss (Signature Edition)", "Flat Serve (Signature Edition)", "Volley Basics (Signature Edition)", "Overhead Smash Setup (Signature Edition)", "Footwork Patterns (Unit Turn) (Signature Edition)", "Scoring and Court Geometry (Signature Edition)"], "Compounded": ["Topspin Forehand (Windshield Wiper) (Signature Edition)", "Slice Backhand (Signature Edition)", "Kick Serve (Signature Edition)", "Slice Serve (Signature Edition)", "Approach Shot and Net Transition (Signature Edition)", "Drop Shot (Signature Edition)", "Lob (Defensive and Offensive) (Signature Edition)", "Return of Serve Positioning (Signature Edition)", "Passing Shots (Signature Edition)", "Half-Volley (Signature Edition)", "Serve Plus One Patterns (Signature Edition)", "Tiebreak Strategy (Signature Edition)"], "Advanced": ["Inside-Out Forehand (Signature Edition)", "Backhand Down-the-Line Under Pressure (Signature Edition)", "The Tweener (Signature Edition)", "Serve Placement Maps (T / Body / Wide) (Signature Edition)", "Second-Serve Aggression (Signature Edition)", "Returning Big Servers (Signature Edition)", "Playing the Wind and Sun (Signature Edition)", "Five-Set Physical Management (Signature Edition)", "Video and Analytics Scouting (Signature Edition)", "Doubles Formations (I-Formation, Australian) (Signature Edition)", "Mental Reset Rituals (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# tennis-serve-stats-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 tennis technique record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A tennis technique record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tennis-serve-stats-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-tennis-technique-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tennis-technique-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
