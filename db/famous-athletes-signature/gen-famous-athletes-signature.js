(function(){'use strict';
/* JAH Famous Athletes Signature Database generator — jahdb-famous-athletes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FAMATHS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Makes an Athlete Legendary (Signature Edition)", "Jesse Owens (Signature Edition)", "Babe Ruth (Signature Edition)", "Pele (Signature Edition)", "Muhammad Ali (Signature Edition)", "Nadia Comaneci (Signature Edition)", "Mark Spitz (Signature Edition)", "Billie Jean King (Signature Edition)", "Jim Thorpe (Signature Edition)", "Wilma Rudolph (Signature Edition)", "Secretariat (Equine Athlete) (Signature Edition)"], "Compounded": ["Michael Jordan (Signature Edition)", "Serena Williams (Signature Edition)", "Usain Bolt (Signature Edition)", "Tom Brady (Signature Edition)", "Lionel Messi (Signature Edition)", "Simone Biles (Signature Edition)", "Michael Phelps (Signature Edition)", "Wayne Gretzky (Signature Edition)", "Martina Navratilova (Signature Edition)", "Tiger Woods (Signature Edition)", "Roger Federer (Signature Edition)", "Cristiano Ronaldo (Signature Edition)"], "Advanced": ["Kareem Abdul-Jabbar (Signature Edition)", "Jack Nicklaus (Signature Edition)", "Eddy Merckx (Signature Edition)", "Kelly Slater (Signature Edition)", "Tony Hawk (Signature Edition)", "Valentino Rossi (Signature Edition)", "Aleksandr Karelin (Signature Edition)", "Paavo Nurmi (Signature Edition)", "Larisa Latynina (Signature Edition)", "Don Bradman (Signature Edition)", "Jahangir Khan (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# career-line-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 athlete profile record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A athlete profile record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"career-line-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-famous-athletes-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('famous-athletes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
