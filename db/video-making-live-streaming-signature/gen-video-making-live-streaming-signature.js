(function(){'use strict';
/* JAH The Live Streaming Database — Signature Edition generator — 1.0.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VMLSS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "How Live Streaming Works",
  "OBS Studio: The Free Powerhouse",
  "Bitrates and Encoder Settings",
  "Cameras for Streaming",
  "Audio for Streaming",
  "Lighting for Streaming",
  "Scenes and Overlays",
  "Chat and Community",
  "Going Live: The Pre-Stream Ritual",
  "Moderation Tools and Team",
  "Alerts and Engagement",
  "Recording While Streaming"
 ],
 "Compounded": [
  "Multi-Streaming",
  "RTMP, SRT, and Protocols",
  "Internet: Bonding and Backup",
  "Mobile Streaming",
  "Gaming Streams",
  "Event and Wedding Streaming",
  "Corporate and Worship Streams",
  "Shopping and Live Commerce",
  "Latency Modes and Interaction",
  "VOD Strategy and Repurposing",
  "Monetization",
  "Analytics: What to Watch",
  "Scheduling and Promotion"
 ],
 "Advanced": [
  "Backup Plans for Live",
  "Copyright and Music on Streams",
  "Accessibility: Captions on Live",
  "The Streaming Business",
  "Building a Streaming Career",
  "Building a Streaming Studio Facility",
  "Esports Broadcast Production",
  "Multi-Camera Live Direction",
  "The Stream Producer's Playbook"
 ]
};
var DEMOKIND="signature stream planner";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature Stream Planner — "+safe+"\n"
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
    name:topic+' — live streaming record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A live streaming record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'1.0.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-making-live-streaming-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
