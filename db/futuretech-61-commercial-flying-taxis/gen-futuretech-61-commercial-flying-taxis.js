(function(){'use strict';
/* JAH The Commercial Flying Taxis Future Technology Database generator — jahdb-futuretech-61-commercial-flying-taxis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT61-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1903: the Wright Flyer - Foundations",
  "1939: the First Practical Helicopter - Foundations",
  "1950s: Helicopter Airlines - Foundations",
  "1977: the Rooftop Era Ends - Foundations",
  "2004: Light Sport Aircraft Rule - Foundations",
  "2009: the Transition Flies - Foundations",
  "2011: the First Electric Multicopter - Foundations",
  "2014: Ehang Bets on Autonomy - Foundations",
  "2016: the Passenger Drone Debuts - Foundations",
  "2016: Uber Elevate - the Business Case - Foundations",
  "2017: Lilium - the Electric Jet - Foundations"
 ],
 "Compounded": [
  "2018: the eVTOL Gold Rush - Compounded",
  "2019: Joby's S4 Flies - Compounded",
  "2019: Singapore Sees the Air Taxi - Compounded",
  "2020: Joby's $6.6B Debut - Compounded",
  "2021: Archer Goes Public - Compounded",
  "2021: the Certification Path Opens - Compounded",
  "2022: Vertiport Rules - Compounded",
  "2022: Joby Wins Operator Approval - Compounded",
  "2023: US Vertiport Guidance - Compounded",
  "2023: Eve - the Incumbent's eVTOL - Compounded",
  "2024: Dubai Commits - Compounded",
  "2024: the Gulf Launchpad - Compounded"
 ],
 "Advanced": [
  "2024: the Powered-Lift Rulebook - Advanced",
  "2025: Certification Flight Testing - Advanced",
  "2025: the First Route Maps - Advanced",
  "Certified Service Begins - Advanced",
  "Vertiport Networks - Advanced",
  "Air Traffic for the Third Dimension - Advanced",
  "Cost Parity with Ground Taxis - Advanced",
  "The Noise Problem Solved - Advanced",
  "Autonomous Air Taxis - Advanced",
  "Intercity eVTOL - Advanced",
  "The Everyday Air Taxi - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — commercial flying taxi record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A commercial flying taxi record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-61-commercial-flying-taxis-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-61-commercial-flying-taxis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-61-commercial-flying-taxis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
