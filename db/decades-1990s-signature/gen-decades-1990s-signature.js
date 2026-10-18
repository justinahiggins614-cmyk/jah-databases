(function(){'use strict';
/* JAH The 1990s Signature Database generator — jahdb-decades-1990s-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1990S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1990s at a Glance: The End of History and the Web (Signature Edition) - Foundations",
  "1990: Mandela Walks Free (Signature Edition) - Foundations",
  "1990: Hubble Launches \u2014 Blurry Then Brilliant (Signature Edition) - Foundations",
  "1991: The Gulf War \u2014 Desert Storm (Signature Edition) - Foundations",
  "1991: The World Wide Web Goes Public (Signature Edition) - Foundations",
  "1991: The Soviet Union Dissolves (Signature Edition) - Foundations",
  "1992: The LA Riots (Signature Edition) - Foundations",
  "1993: The Waco Siege (Signature Edition) - Foundations",
  "1994: Amazon Is Founded (Signature Edition) - Foundations",
  "1995: The Oklahoma City Bombing (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "1990: The Human Genome Project Launches (Signature Edition) - Compounded",
  "1991: Linux \u2014 a Student's Hobby OS (Signature Edition) - Compounded",
  "1992: The First Text Message (Signature Edition) - Compounded",
  "1993: Mosaic \u2014 the Browser That Lit the Web (Signature Edition) - Compounded",
  "1994: Friends Premieres (Signature Edition) - Compounded",
  "1994: The Channel Tunnel Opens (Signature Edition) - Compounded",
  "1995: Windows 95 (Signature Edition) - Compounded",
  "1995: eBay Is Founded (Signature Edition) - Compounded",
  "1996: Deep Blue Beats Kasparov \u2014 a Game (Signature Edition) - Compounded",
  "1997: Mars Pathfinder Lands (Signature Edition) - Compounded",
  "1997: Titanic \u2014 the King of the Box Office (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "1997: Dolly the Sheep \u2014 the First Cloned Mammal (Signature Edition) - Advanced",
  "1998: Google Is Founded (Signature Edition) - Advanced",
  "1998: The Good Friday Agreement (Signature Edition) - Advanced",
  "1999: The Euro Is Born (Signature Edition) - Advanced",
  "1999: Columbine (Signature Edition) - Advanced",
  "1999: Y2K \u2014 the Bug That Wasn't (Signature Edition) - Advanced",
  "1994: The PlayStation (Signature Edition) - Advanced",
  "1995: The O.J. Simpson Verdict (Signature Edition) - Advanced",
  "1998: Viagra (Signature Edition) - Advanced",
  "1996: The DVD (Signature Edition) - Advanced",
  "1997: Hong Kong Returns to China (Signature Edition) - Advanced",
  "1993: Jurassic Park (Signature Edition) - Advanced",
  "1990: Germany Reunifies (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1990S — "+safe+"\n"
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
    name:topic+' — 1990s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1990s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1990s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1990s-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1990s-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
