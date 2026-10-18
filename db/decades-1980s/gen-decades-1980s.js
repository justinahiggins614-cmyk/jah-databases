(function(){'use strict';
/* JAH The 1980s Database generator — jahdb-decades-1980s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1980-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1980s at a Glance: Greed, Gadgets, and the Wall Falls - Foundations",
  "1980: Reagan Wins the Presidency - Foundations",
  "1980: CNN Launches \u2014 News Never Sleeps - Foundations",
  "1981: The IBM PC - Foundations",
  "1981: MTV Launches - Foundations",
  "1981: The Space Shuttle Era Begins - Foundations",
  "1981: AIDS Is Identified - Foundations",
  "1982: Thriller \u2014 the Biggest Album Ever - Foundations",
  "1983: The Mobile Phone Is Approved - Foundations",
  "1984: The Macintosh - Foundations"
 ],
 "Compounded": [
  "1980: Pac-Man - Compounded",
  "1981: Reagan Is Shot - Compounded",
  "1982: The Compact Disc - Compounded",
  "1982: The Falklands War - Compounded",
  "1983: The Nintendo Famicom - Compounded",
  "1984: DNA Fingerprinting - Compounded",
  "1985: Live Aid - Compounded",
  "1985: Windows 1.0 Launches the GUI Era - Compounded",
  "1985: The NES Conquers America - Compounded",
  "1986: The Challenger Disaster - Compounded",
  "1986: Chernobyl - Compounded"
 ],
 "Advanced": [
  "1986: Pixar Is Born - Advanced",
  "1987: Prozac \u2014 the Happiness Pill - Advanced",
  "1987: The Montreal Protocol Saves the Ozone - Advanced",
  "1988: The Morris Worm \u2014 the Internet's First Attack - Advanced",
  "1989: The Berlin Wall Falls - Advanced",
  "1989: Tiananmen Square - Advanced",
  "1989: The Exxon Valdez - Advanced",
  "1989: The Game Boy - Advanced",
  "1989: The Simpsons Premieres - Advanced",
  "1984: Tetris - Advanced",
  "1983: The Internet Switches to TCP/IP - Advanced",
  "1980: Post-it Notes - Advanced",
  "1985: The Titanic Wreck Is Found - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1980S — "+safe+"\n"
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
    name:topic+' — 1980s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1980s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1980s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1980s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1980s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
