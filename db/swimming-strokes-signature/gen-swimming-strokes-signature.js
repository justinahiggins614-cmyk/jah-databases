(function(){'use strict';
/* JAH Swimming Strokes Signature Database generator — jahdb-swimming-strokes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SWIMSTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Water Comfort and Floating (Signature Edition)", "Streamline Position (Signature Edition)", "Freestyle Arm Cycle (Signature Edition)", "Freestyle Kick (Flutter) (Signature Edition)", "Rhythmic Breathing (Signature Edition)", "Backstroke Basics (Signature Edition)", "Breaststroke Kick (Whip) (Signature Edition)", "Breaststroke Arms (Signature Edition)", "Treading Water (Signature Edition)", "Pool Safety and Lane Etiquette (Signature Edition)", "Gliding and Body Position (Signature Edition)"], "Compounded": ["Freestyle Bilateral Breathing (Signature Edition)", "Freestyle Flip Turn (Signature Edition)", "Backstroke Flip Turn (Signature Edition)", "Breaststroke Pullout (Signature Edition)", "Butterfly Arm Recovery (Signature Edition)", "Butterfly Dolphin Kick (Signature Edition)", "Open Turns (Signature Edition)", "Starts (Track Start) (Signature Edition)", "Drafting in Open Water (Signature Edition)", "Pacing (Negative Split) (Signature Edition)", "IM Transitions (Signature Edition)", "Sidestroke and Rescue Basics (Signature Edition)"], "Advanced": ["Underwater Dolphin Kick (15m Rule) (Signature Edition)", "Freestyle Catch (High Elbow) (Signature Edition)", "Backstroke Rotation Timing (Signature Edition)", "Breaststroke Timing (Pull-Breathe-Kick-Glide) (Signature Edition)", "Butterfly Breathing Rhythm (Signature Edition)", "Sprint vs Distance Stroke Rate (Signature Edition)", "Open-Water Sighting (Signature Edition)", "Relay Exchanges (Signature Edition)", "Race-Pace Stroke Counting (Signature Edition)", "Turn Speed Optimization (Signature Edition)", "Finish Technique (No-Breath Final Strokes) (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# swim-css-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 swimming stroke record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A swimming stroke record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"swim-css-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-swimming-strokes-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('swimming-strokes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
