(function(){'use strict';
/* JAH The 1930s Database generator — jahdb-decades-1930s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1930-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1930s at a Glance: Depression and the Drift to War - Foundations",
  "1931: The Empire State Building Opens - Foundations",
  "1932: Roosevelt Is Elected on a New Deal Promise - Foundations",
  "1933: Hitler Becomes Chancellor of Germany - Foundations",
  "1933: Roosevelt's First Hundred Days - Foundations",
  "1933: Prohibition Ends - Foundations",
  "1933: The Tennessee Valley Authority Is Created - Foundations",
  "1934: The Night of the Long Knives - Foundations",
  "1935: The Social Security Act - Foundations",
  "1935: The Nuremberg Laws - Foundations"
 ],
 "Compounded": [
  "1935: Black Sunday \u2014 the Dust Bowl's Darkest Day - Compounded",
  "1935: Hoover Dam Is Dedicated - Compounded",
  "1935: Nylon Is Invented - Compounded",
  "1936: Jesse Owens Defies Hitler at the Berlin Olympics - Compounded",
  "1936: The Spanish Civil War Begins - Compounded",
  "1936: Gone with the Wind Is Published - Compounded",
  "1937: The Hindenburg Disaster - Compounded",
  "1937: The Golden Gate Bridge Opens - Compounded",
  "1937: Snow White Premieres \u2014 Disney's Impossible Gamble - Compounded",
  "1937: Japan Invades China \u2014 the Road to Nanking - Compounded",
  "1938: The War of the Worlds Broadcast Panics America - Compounded"
 ],
 "Advanced": [
  "1938: Superman Debuts in Action Comics #1 - Advanced",
  "1938: The Munich Agreement \u2014 Appeasement's High-Water Mark - Advanced",
  "1938: Kristallnacht \u2014 the Night of Broken Glass - Advanced",
  "1938: Nuclear Fission Is Discovered - Advanced",
  "1939: The Wizard of Oz Premieres - Advanced",
  "1939: Germany Invades Poland \u2014 World War II Begins - Advanced",
  "1939: The First Helicopter \u2014 Sikorsky's VS-300 - Advanced",
  "1930: Pluto Is Discovered - Advanced",
  "1932: The Neutron Is Discovered - Advanced",
  "1933: The First Drive-In Theater - Advanced",
  "1935: The FBI Gets Its Name - Advanced",
  "1934: Bonnie and Clyde Are Ambushed - Advanced",
  "1939: The World's Fair Promises the World of Tomorrow - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1930S — "+safe+"\n"
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
    name:topic+' — 1930s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1930s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1930s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1930s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1930s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
