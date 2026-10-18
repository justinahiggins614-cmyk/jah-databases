(function(){'use strict';
/* JAH Women Suffrage Database generator — jahdb-women-suffrage-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WOMSUF-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Women's Suffrage: An Overview", "Seneca Falls 1848", "Susan B. Anthony", "Elizabeth Cady Stanton", "Sojourner Truth", "The 19th Amendment", "The Pankhursts and the WSPU", "New Zealand 1893: First in the World", "Alice Paul and the NWP", "The Hunger Strikes", "Wyoming 1869: The Equality State"], "Compounded": ["The Anti-Suffrage Opposition", "Suffrage and Race", "Ida B. Wells", "The State-by-State Campaigns", "World War I and the Vote", "The Suffrage Press", "Suffrage Tactics: Parades and Pickets", "The 1913 Washington Parade", "Suffrage and Labor", "Suffrage and Temperance", "The International Wave", "After 1920: The Unfinished Vote"], "Advanced": ["Frances Willard and the WCTU", "Lucy Stone and the AWSA", "Matilda Joslyn Gage", "The Equal Rights Amendment (1923)", "Carrie Chapman Catt", "Suffragette Tactics in Detail", "Suffrage Art and Propaganda", "The Men's Leagues", "The Ratification Battle: Tennessee", "Scandinavian Suffrage", "From Suffrage to Feminism"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — women-suffrage demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — suffrage record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A suffrage record of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"women-suffrage-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-women-suffrage-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("women-suffrage",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
