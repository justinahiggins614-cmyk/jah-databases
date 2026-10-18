(function(){'use strict';
/* JAH The 1920s Signature Database generator — jahdb-decades-1920s-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1920S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Roaring Twenties at a Glance (Signature Edition) - Foundations",
  "1920: American Women Win the Vote (Signature Edition) - Foundations",
  "1920: Prohibition Begins (Signature Edition) - Foundations",
  "1920: KDKA Makes the First Commercial Radio Broadcast (Signature Edition) - Foundations",
  "1920: The Band-Aid Is Invented (Signature Edition) - Foundations",
  "1921: Insulin Is Discovered (Signature Edition) - Foundations",
  "1922: Tutankhamun's Tomb Is Found (Signature Edition) - Foundations",
  "1922: The Soviet Union Is Formed (Signature Edition) - Foundations",
  "1922: Mussolini Marches on Rome (Signature Edition) - Foundations",
  "1923: Yankee Stadium Opens (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "1923: Scandal and Succession \u2014 Harding Dies, Coolidge Takes Over (Signature Edition) - Compounded",
  "1924: The First Winter Olympics Open in Chamonix (Signature Edition) - Compounded",
  "1924: A Parade Launches a Retail Tradition (Signature Edition) - Compounded",
  "1925: The Scopes Trial Puts Evolution on Trial (Signature Edition) - Compounded",
  "1925: The Great Gatsby Defines the Jazz Age (Signature Edition) - Compounded",
  "1925: Quantum Mechanics Is Born (Signature Edition) - Compounded",
  "1925: The Grand Ole Opry Goes on the Air (Signature Edition) - Compounded",
  "1925: The Locarno Treaties Try to Lock In Peace (Signature Edition) - Compounded",
  "1926: Television Is Demonstrated (Signature Edition) - Compounded",
  "1926: Gertrude Ederle Conquers the English Channel (Signature Edition) - Compounded",
  "1926: Route 66 Opens the Mother Road (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "1927: Lindbergh Flies the Atlantic Alone (Signature Edition) - Advanced",
  "1927: The Jazz Singer Ends the Silent Era (Signature Edition) - Advanced",
  "1927: Babe Ruth Hits 60 Home Runs (Signature Edition) - Advanced",
  "1927: The Holland Tunnel Opens (Signature Edition) - Advanced",
  "1928: Penicillin Is Discovered (Signature Edition) - Advanced",
  "1928: Mickey Mouse Debuts (Signature Edition) - Advanced",
  "1928: The Kellogg-Briand Pact Outlaws War (Signature Edition) - Advanced",
  "1928: Amelia Earhart Crosses the Atlantic (Signature Edition) - Advanced",
  "1929: The St. Valentine's Day Massacre (Signature Edition) - Advanced",
  "1929: The Stock Market Crashes (Signature Edition) - Advanced",
  "1929: Hubble Finds the Expanding Universe (Signature Edition) - Advanced",
  "1929: The First Academy Awards (Signature Edition) - Advanced",
  "1926: Winnie-the-Pooh Enters the Hundred Acre Wood (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1920S — "+safe+"\n"
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
    name:topic+' — 1920s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1920s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1920s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1920s-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1920s-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
