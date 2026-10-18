(function(){'use strict';
/* JAH The Daily Brain Challenge Signature Database generator — jahdb-db-daily-brain-challenge-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DAIBRAICHS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Day 1: How many letters are in the answer to this quest...",
  "Day 2: What number comes next: 2, 4, 8, 16,...",
  "Day 3: Which is heavier: a kilo of feathers or a kilo o...",
  "Day 4: How many months have 28 days...",
  "Day 5: What 3-letter word reads the same forward and ba...",
  "Day 6: If you have 3 apples and take away 2, how many d...",
  "Day 7: What goes around the world but stays in a corner...",
  "Day 8: How many times can you subtract 10 from 100...",
  "Day 9: What has 4 legs in the morning, 2 at noon, 3 in...",
  "Day 10: Which weighs more: your brain or your heart...",
  "Day 11: What 5-letter word has only 1 left when you take..."
 ],
 "Compounded": [
  "Day 12: A bat and ball cost $1.10; the bat costs $1 more...",
  "Day 13: 5 machines make 5 widgets in 5 minutes; 100 mach...",
  "Day 14: A lily patch doubles daily; covers the lake in 4...",
  "Day 15: If 3 cats catch 3 mice in 3 minutes, how long fo...",
  "Day 16: What is the next prime after 7...",
  "Day 17: You have 8 balls, one heavier; minimum weighings...",
  "Day 18: How many squares on a chessboard...",
  "Day 19: A 10-digit number using each digit once, divisib...",
  "Day 20: What is 111,111,111 x 111,111,111...",
  "Day 21: Three boxes labeled wrong; one pull to relabel a...",
  "Day 22: How many moves for the 3-disk Tower of Hanoi...",
  "Day 34: What is the smallest number divisible by 1 throu..."
 ],
 "Advanced": [
  "Day 23: What is the 100th digit of 1/7 = 0.142857142857...",
  "Day 24: How many handshakes if 10 people each shake once...",
  "Day 25: What is the sum 1+2+...+100...",
  "Day 26: A clock strikes 6 times in 5 seconds; how long f...",
  "Day 27: What is the only even prime number...",
  "Day 28: If it takes 6 men 6 days to dig 6 holes, how lon...",
  "Day 29: What number is 1 more than its reversal... (41 v...",
  "Day 30: How many Friday the 13ths can a year have at mos...",
  "Day 31: What is 2^10...",
  "Day 32: A snail climbs 3 ft by day, slips 2 by night, up...",
  "Day 33: What is the 7th Fibonacci number (1,1,2,3,5,...)..."
 ]
};
var DEMOKIND="workout-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Daily Workout — "+safe+"\n"
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
    name:topic+' — daily challenge record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A daily challenge record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-daily-brain-challenge-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-daily-brain-challenge-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
