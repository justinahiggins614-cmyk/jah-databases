(function(){'use strict';
/* JAH Commercial Airliners History Database generator — "jahdb-commercial-airliners-history-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AIRLN-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["The First Scheduled Airline: St. Petersburg–Tampa Airboat Line", "Ford Trimotor: The Tin Goose", "Junkers Ju 52: Corrugated Workhorse", "Douglas DC-3: The Airliner That Paid", "Boeing 307 Stratoliner: First Pressurized Cabin", "Lockheed Constellation: Triple-Tail Icon", "de Havilland Comet: First Jet Airliner", "Tupolev Tu-104: Soviet Jet Pioneer", "Sud Aviation Caravelle: Rear-Engine Revolution", "Boeing 707: The Jet Age Begins", "Douglas DC-8: The 707's Rival"], "compounded": ["Boeing 727: The Trijet Workhorse", "Boeing 737: Best-Selling Jetliner", "Boeing 747: Queen of the Skies", "McDonnell Douglas DC-10: Trijet Wide-Body", "Lockheed L-1011 TriStar: The Advanced Trijet", "Concorde: Supersonic Transport", "Airbus A300: Europe's Twin-Aisle", "McDonnell Douglas MD-80: Stretched Workhorse", "Boeing 757: Narrow-Body Muscle", "Boeing 767: ETOPS Pioneer", "Fokker 100: Regional Jet Era", "Airbus A320: Fly-by-Wire Pioneer"], "advanced": ["Airbus A330: Long-Range Twin", "Boeing 777: Digitally Designed Twin", "Airbus A340: Four-Engine Long-Haul", "Airbus A380: Largest Passenger Airliner", "Boeing 787 Dreamliner: Composite Era", "Boeing 747-8: Stretched Jumbo", "Airbus A350 XWB: Composite Long-Haul", "Airbus A320neo: New Engine Option", "Boeing 737 MAX: Latest 737", "Embraer E-Jets E2: Modern Regionals", "The Modern Airliner: Systems That Fly Today"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+" — structural sample demo\n"
    + "RECORD = "+JSON.stringify({topic:safe,field:field})+"\n"
    + "def main():\n"
    + "    print('Record:', RECORD['topic'])\n"
    + "    print('Field:', RECORD['field'])\n"
    + "    vals = [3, 7, 11]\n"
    + "    print('Sample values:', vals)\n"
    + "    print('Total:', sum(vals))\n"
    + "    print('Demo complete.')\n"
    + "if __name__ == '__main__':\n"
    + "    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — structural sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A '+field+' sample on "'+topic+'". Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sample-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-commercial-airliners-history-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("commercial-airliners-history",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
