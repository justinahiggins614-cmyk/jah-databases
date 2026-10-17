(function(){'use strict';
/* JAH The Time Basics Signature Database generator — jahdb-time-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TMEBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Time Is (Signature Edition) - Foundations",
  "The Second: The Smallest Common Unit (Signature Edition) - Foundations",
  "Minutes and Hours (Signature Edition) - Foundations",
  "Days, Weeks, and Months (Signature Edition) - Foundations",
  "Years, Decades, Centuries, and Millennia (Signature Edition) - Foundations",
  "Telling Time on an Analog Clock (Signature Edition) - Foundations",
  "Telling Time on a Digital Clock (Signature Edition) - Foundations",
  "AM and PM (Signature Edition) - Foundations",
  "Noon, Midnight, and Relative Time Words (Signature Edition) - Foundations",
  "Smaller Than a Second: Milliseconds, Microseconds, Nanoseconds (Signature Edition) - Foundations",
  "The Ladder of Time Units (Signature Edition) - Foundations",
  "Tools That Measure Time: From Sundials to Stopwatches (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Adding and Subtracting Units of Time (Signature Edition) - Compounded",
  "Elapsed Time: From Start to Finish (Signature Edition) - Compounded",
  "The 24-Hour Clock (Signature Edition) - Compounded",
  "Calendars: How Months and Years Are Organized (Signature Edition) - Compounded",
  "Leap Years: Why February Gains a Day (Signature Edition) - Compounded",
  "Time Zones: Why the Hour Changes Around the World (Signature Edition) - Compounded",
  "Coordinated Universal Time (UTC) (Signature Edition) - Compounded",
  "The International Date Line (Signature Edition) - Compounded",
  "Daylight Saving Time (Signature Edition) - Compounded",
  "The Seven-Day Week: Why Seven (Signature Edition) - Compounded",
  "The Earth in Motion: Rotation, Orbit, and the Seasons (Signature Edition) - Compounded",
  "Reading Schedules and Timetables (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Atomic Time: How the Second Is Defined (Signature Edition) - Advanced",
  "Leap Seconds: Keeping Clocks in Step with the Earth (Signature Edition) - Advanced",
  "Calendars of the World: Gregorian, Julian, Lunar, and Hijri (Signature Edition) - Advanced",
  "The History of Timekeeping: From Water Clocks to Atomic Clocks (Signature Edition) - Advanced",
  "Time Arithmetic Across Days and Time Zones (Signature Edition) - Advanced",
  "Telling Time Around the World: Converting Local Times (Signature Edition) - Advanced",
  "Precision Timing: When Milliseconds Matter (Signature Edition) - Advanced",
  "The Time Number Line: Planning Your Day (Signature Edition) - Advanced",
  "Ages and Eras: Geological and Historical Time (Signature Edition) - Advanced",
  "Time in Science: Frequencies, Periods, and the Speed of Light (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Time Basics Study — "+safe+"\n"
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
    name:topic+' — time basics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A time basics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"time-basics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-time-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('time-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
