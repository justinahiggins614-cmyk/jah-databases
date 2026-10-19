(function(){'use strict';
/* JAH The Commercial Flying Taxis Future Technology Database — Signature Edition generator — jahdb-futuretech-61-commercial-flying-taxis-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT61-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Commercial Flying Taxis — the Wright Flyer (Signature Edition)", "Commercial Flying Taxis — the First Practical Helicopter (Signature Edition)", "Commercial Flying Taxis — Helicopter Airlines (Signature Edition)", "Commercial Flying Taxis — the Rooftop Era Ends (Signature Edition)", "Commercial Flying Taxis — Light Sport Aircraft Rule (Signature Edition)", "Commercial Flying Taxis — the Transition Flies (Signature Edition)", "Commercial Flying Taxis — the First Electric Multicopter (Signature Edition)", "Commercial Flying Taxis — Ehang Bets on Autonomy (Signature Edition)", "Commercial Flying Taxis — the Passenger Drone Debuts (Signature Edition)", "Commercial Flying Taxis — Uber Elevate - the Business Case (Signature Edition)", "Commercial Flying Taxis — Lilium - the Electric Jet (Signature Edition)"], "Compounded": ["Commercial Flying Taxis — the eVTOL Gold Rush (Signature Edition)", "Commercial Flying Taxis — Joby's S4 Flies (Signature Edition)", "Commercial Flying Taxis — Singapore Sees the Air Taxi (Signature Edition)", "Commercial Flying Taxis — Joby's $6.6B Debut (Signature Edition)", "Commercial Flying Taxis — Archer Goes Public (Signature Edition)", "Commercial Flying Taxis — the Certification Path Opens (Signature Edition)", "Commercial Flying Taxis — Vertiport Rules (Signature Edition)", "Commercial Flying Taxis — Joby Wins Operator Approval (Signature Edition)", "Commercial Flying Taxis — US Vertiport Guidance (Signature Edition)", "Commercial Flying Taxis — Eve - the Incumbent's eVTOL (Signature Edition)", "Commercial Flying Taxis — Dubai Commits (Signature Edition)", "Commercial Flying Taxis — the Gulf Launchpad (Signature Edition)"], "Advanced": ["Commercial Flying Taxis — the Powered-Lift Rulebook (Signature Edition)", "Commercial Flying Taxis — Certification Flight Testing (Signature Edition)", "Commercial Flying Taxis — the First Route Maps (Signature Edition)", "Commercial Flying Taxis — Certified Service Begins (Signature Edition)", "Commercial Flying Taxis — Vertiport Networks (Signature Edition)", "Commercial Flying Taxis — Air Traffic for the Third Dimension (Signature Edition)", "Commercial Flying Taxis — Cost Parity with Ground Taxis (Signature Edition)", "Commercial Flying Taxis — The Noise Problem Solved (Signature Edition)", "Commercial Flying Taxis — Autonomous Air Taxis (Signature Edition)", "Commercial Flying Taxis — Intercity eVTOL (Signature Edition)", "Commercial Flying Taxis — The Everyday Air Taxi - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Commercial Flying Taxis study \u2014 "+safe+"\n"
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
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-61-commercial-flying-taxis-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-61-commercial-flying-taxis-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
