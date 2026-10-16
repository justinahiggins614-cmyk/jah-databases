(function(){'use strict';
/* JAH The Plane, Jet and Car Crash Investigation Database generator — jahdb-crash-data-databases-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRD-";
var FIELDS=["aviation-investigations","motor-vehicle-crash-data"];
var TOPICS={
 "aviation-investigations": [
  "Tenerife Airport Disaster \u2014 1977 \u2014 aviation-investigations",
  "Japan Air Lines Flight 123 \u2014 1985 \u2014 aviation-investigations",
  "Air France Flight 447 \u2014 2009 \u2014 aviation-investigations",
  "Malaysia Airlines Flight 370 \u2014 2014 \u2014 aviation-investigations",
  "TWA Flight 800 \u2014 1996 \u2014 aviation-investigations",
  "Swissair Flight 111 \u2014 1998 \u2014 aviation-investigations",
  "ValuJet Flight 592 \u2014 1996 \u2014 aviation-investigations",
  "Alaska Airlines Flight 261 \u2014 2000 \u2014 aviation-investigations",
  "American Airlines Flight 587 \u2014 2001 \u2014 aviation-investigations",
  "Colgan Air Flight 3407 \u2014 2009 \u2014 aviation-investigations",
  "Asiana Airlines Flight 214 \u2014 2013 \u2014 aviation-investigations",
  "Lion Air Flight 610 \u2014 2018 \u2014 aviation-investigations",
  "Ethiopian Airlines Flight 302 \u2014 2019 \u2014 aviation-investigations",
  "Germanwings Flight 9525 \u2014 2015 \u2014 aviation-investigations",
  "Indonesia AirAsia Flight 8501 \u2014 2014 \u2014 aviation-investigations",
  "TAM Airlines Flight 3054 \u2014 2007 \u2014 aviation-investigations",
  "Spanair Flight 5022 \u2014 2008 \u2014 aviation-investigations",
  "US Airways Flight 1549 \u2014 2009 \u2014 aviation-investigations",
  "United Airlines Flight 232 \u2014 1989 \u2014 aviation-investigations",
  "Aloha Airlines Flight 243 \u2014 1988 \u2014 aviation-investigations",
  "Eastern Air Lines Flight 401 \u2014 1972 \u2014 aviation-investigations",
  "Delta Air Lines Flight 191 \u2014 1985 \u2014 aviation-investigations",
  "USAir Flight 427 \u2014 1994 \u2014 aviation-investigations",
  "American Eagle Flight 4184 \u2014 1994 \u2014 aviation-investigations",
  "Air France Flight 358 \u2014 2005 \u2014 aviation-investigations",
  "British Airways Flight 38 \u2014 2008 \u2014 aviation-investigations",
  "Qantas Flight 32 \u2014 2010 \u2014 aviation-investigations",
  "PSA Flight 182 \u2014 1978 \u2014 aviation-investigations",
  "Air Canada Flight 797 \u2014 1983 \u2014 aviation-investigations",
  "Southern Airways Flight 242 \u2014 1977 \u2014 aviation-investigations"
 ],
 "motor-vehicle-crash-data": [
  "Ford Pinto Fuel-System Safety Cases \u2014 1970s \u2014 motor-vehicle-crash-data",
  "Takata Airbag Inflator Recalls \u2014 2008\u2013present \u2014 motor-vehicle-crash-data",
  "General Motors Ignition-Switch Cases \u2014 2014 \u2014 motor-vehicle-crash-data",
  "Toyota Unintended-Acceleration Investigations \u2014 2009\u20132011 \u2014 motor-vehicle-crash-data",
  "Tesla Autopilot Fatal Crash, Williston, Florida \u2014 2016 \u2014 motor-vehicle-crash-data",
  "Uber ATG Test Vehicle Crash, Tempe, Arizona \u2014 2018 \u2014 motor-vehicle-crash-data",
  "Firestone Tire / Ford Explorer Cases \u2014 2000 \u2014 motor-vehicle-crash-data",
  "U.S. Roadway Fatality Trends \u2014 FARS Public Data \u2014 motor-vehicle-crash-data",
  "Seat-Belt Effectiveness \u2014 NHTSA Public Findings \u2014 motor-vehicle-crash-data",
  "Alcohol-Impaired Driving Trends \u2014 Public Data \u2014 motor-vehicle-crash-data",
  "Distracted-Driving Research \u2014 Public Findings \u2014 motor-vehicle-crash-data",
  "Motorcycle Helmet Effectiveness \u2014 Public Data \u2014 motor-vehicle-crash-data",
  "Child Passenger Safety \u2014 Public Record \u2014 motor-vehicle-crash-data",
  "Frontal Airbag Effectiveness and Risks \u2014 Public Record \u2014 motor-vehicle-crash-data",
  "Electronic Stability Control Effectiveness \u2014 Public Record \u2014 motor-vehicle-crash-data",
  "Rear Visibility Rule, FMVSS 111 \u2014 2014 \u2014 motor-vehicle-crash-data",
  "School Bus Occupant Safety \u2014 Public Record \u2014 motor-vehicle-crash-data",
  "Large Truck Crash Causation Study \u2014 FMCSA \u2014 motor-vehicle-crash-data",
  "Pedestrian Crash Data \u2014 Public Record \u2014 motor-vehicle-crash-data",
  "New Car Assessment Program \u2014 Public Ratings \u2014 motor-vehicle-crash-data"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Crash Investigation Study — "+safe+"\n"
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
    name:topic+' — crash investigation record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A crash investigation record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-crash-data-databases-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('crash-data-databases',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
