(function(){'use strict';
/* JAH The All Accidents Insurance-Proven Documentation Database generator — jahdb-accidents-insurance-proven-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AIP-";
var FIELDS=["official-investigation-records","insurance-documented-records","publicly-reported-records"];
var TOPICS={
 "official-investigation-records": [
  "Charkhi Dadri Mid-Air Collision \u2014 1996 \u2014 official-investigation-records",
  "American Airlines Flight 191 \u2014 1979 \u2014 official-investigation-records",
  "Turkish Airlines Flight 981 \u2014 1974 \u2014 official-investigation-records",
  "Lac-M\u00e9gantic Rail Disaster \u2014 2013 \u2014 official-investigation-records",
  "Amtrak Train 188 Derailment \u2014 2015 \u2014 official-investigation-records",
  "Santiago de Compostela Train Derailment \u2014 2013 \u2014 official-investigation-records",
  "Costa Concordia Grounding \u2014 2012 \u2014 official-investigation-records",
  "Sewol Ferry Sinking \u2014 2014 \u2014 official-investigation-records",
  "Deepwater Horizon Explosion \u2014 2010 \u2014 official-investigation-records",
  "Texas City Refinery Explosion \u2014 2005 \u2014 official-investigation-records",
  "Bhopal Gas Tragedy \u2014 1984 \u2014 official-investigation-records",
  "Herald of Free Enterprise Capsizing \u2014 1987 \u2014 official-investigation-records",
  "Piper Alpha Platform Explosion \u2014 1988 \u2014 official-investigation-records",
  "King's Cross Station Fire \u2014 1987 \u2014 official-investigation-records",
  "Kegworth Air Disaster (British Midland Flight 92) \u2014 1989 \u2014 official-investigation-records",
  "United Airlines Flight 173 \u2014 1978 \u2014 official-investigation-records",
  "Avianca Flight 52 \u2014 1990 \u2014 official-investigation-records",
  "Air Inter Flight 148 \u2014 1992 \u2014 official-investigation-records",
  "San Bruno Pipeline Explosion \u2014 2010 \u2014 official-investigation-records",
  "Air Florida Flight 90 \u2014 1982 \u2014 official-investigation-records",
  "EgyptAir Flight 804 \u2014 2016 \u2014 official-investigation-records",
  "Crossair Flight 3597 \u2014 2001 \u2014 official-investigation-records"
 ],
 "insurance-documented-records": [
  "GM Ignition-Switch Compensation Fund Record \u2014 insurance-documented-records",
  "Takata Airbag Victim Compensation Records \u2014 insurance-documented-records",
  "Grimshaw v. Ford \u2014 Pinto Litigation Record \u2014 insurance-documented-records",
  "Johns-Manville Asbestos Personal Injury Trust \u2014 insurance-documented-records",
  "Exxon Valdez Civil Litigation and Settlement Record \u2014 insurance-documented-records",
  "Gulf Coast Claims Facility \u2014 Deepwater Horizon \u2014 insurance-documented-records",
  "Toyota Unintended-Acceleration Settlement Records \u2014 insurance-documented-records",
  "Ford/Firestone Tire Litigation Settlement Records \u2014 insurance-documented-records",
  "September 11th Victim Compensation Fund \u2014 insurance-documented-records",
  "MGM Grand Fire Litigation Record \u2014 1980 \u2014 insurance-documented-records",
  "Station Nightclub Fire Settlement Records \u2014 2003 \u2014 insurance-documented-records",
  "Imperial Sugar Refinery Explosion Claims \u2014 2008 \u2014 insurance-documented-records",
  "Lac-M\u00e9gantic Victim Compensation Fund \u2014 insurance-documented-records",
  "Aviation Hull and Liability Claims Documentation \u2014 insurance-documented-records"
 ],
 "publicly-reported-records": [
  "Copiap\u00f3 Mining Accident and Rescue \u2014 2010 \u2014 publicly-reported-records",
  "Tham Luang Cave Rescue \u2014 2018 \u2014 publicly-reported-records",
  "Andes Flight Disaster \u2014 1972 \u2014 publicly-reported-records",
  "Hindenburg Disaster \u2014 1937 \u2014 publicly-reported-records",
  "Grand Canyon Mid-Air Collision \u2014 1956 \u2014 publicly-reported-records",
  "Park Slope Mid-Air Collision \u2014 1960 \u2014 publicly-reported-records",
  "Wire-Service Documentation of Breaking Transport Disasters \u2014 publicly-reported-records",
  "Public Statistical Record: Commercial Aviation Accident Rates \u2014 publicly-reported-records",
  "Crowdsourced Video as Accident Documentation \u2014 publicly-reported-records",
  "Historical Newspaper Archives as Accident Documentation \u2014 publicly-reported-records",
  "Aviation Safety Network Public Database \u2014 publicly-reported-records",
  "Bureau of Aircraft Accidents Archives Public Record \u2014 publicly-reported-records",
  "Public-Records Requests and Accident Documentation \u2014 publicly-reported-records",
  "Memorialization and Public Remembrance Records \u2014 publicly-reported-records"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Verified Accident Study — "+safe+"\n"
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
    name:topic+' — verified accident record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A verified accident record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-accidents-insurance-proven-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accidents-insurance-proven',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
