(function(){'use strict';
/* JAH Automobiles History Database generator — "jahdb-automobiles-history-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AUTH-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["Benz Patent-Motorwagen: 1886", "Ford Model T: The Car for the Masses", "The Assembly Line: Manufacturing Revolution", "Volkswagen Beetle: The People's Car", "Chevrolet Corvette: America's Sports Car", "Porsche 911: The Evolution", "Ford Mustang: The Pony Car", "Mini: The Small Wonder", "Toyota Corolla: The Best Seller", "Jeep: The Go-Anywhere", "The Internal Combustion Engine"], "compounded": ["Ferrari vs Lamborghini: The Supercar Duel", "Mercedes 300 SL: The Gullwing", "Jaguar E-Type: The Beauty", "Volkswagen Golf GTI: The Hot Hatch", "Honda Civic and Accord: Japan's Conquest", "BMW 3 Series: The Sports Sedan", "Land Rover and Range Rover", "Ford F-150: America's Best Seller", "Muscle Cars: GTO to Charger", "Safety: From Nader to Airbags", "Emissions: The Catalytic Converter", "Toyota Production System: Lean"], "advanced": ["Bugatti Veyron and Chiron: The 1,000-hp Era", "McLaren F1: The Analog Hypercar", "Audi Quattro: The All-Wheel-Drive Revolution", "Chrysler Minivan: The Family Revolution", "SUV Revolution: Explorer to Escalade", "Tesla Roadster: The Electric Spark", "DeLorean: The Dream and the Fall", "Tucker 48: The What-If", "Edsel: The Failure Lesson", "Racing to Road: Le Mans and F1", "The Automobile Century: Capstone"]};
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
var gen={version:"jahdb-automobiles-history-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("automobiles-history",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
