/* ✳ SIGNATURE — JAH JAH Chain-of-Thought generator. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed + same version always yields the same record.
   Runs in the browser (registered with JAHDB) and in node (self-test below). */
(function(){
'use strict';
var SLUG='cot', PREFIX='JAH-COT-', VERSION='jahdb-cot-1.0';
var MARK='Signature version in the Signature system. Property of Justin Addam Higgins.';
function hashStr(s){var h=2166136261;s=String(s);for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function mulberry(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var CATS=["arithmetic", "algebra", "word-problems", "logic", "code-tracing", "commonsense"];
var ANGLES=["worked example", "strategy spotlight", "error analysis", "speed technique", "verification pass", "difficulty ramp"];
var TOPICS=[{"t": "", "c": "arithmetic", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "algebra", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "word-problems", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "logic", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "code-tracing", "d": "", "f": {}, "s": "signature", "r": null}, {"t": "", "c": "commonsense", "d": "", "f": {}, "s": "signature", "r": null}];
function pickR(rnd,a){return a[(rnd()*a.length)|0];}
function makeId(seed){var n=(typeof seed==='number'?seed:hashStr(String(seed)));return PREFIX+String((n%1000000)+1).padStart(7,'0');}
var COT_STRATS=['step-by-step decomposition','working backwards','unit analysis','elimination of wrong answers','estimate then refine','symbolic manipulation'];
var COT_COMMON=[["How many legs does a spider have?","8","Spiders are arachnids, and arachnids have 8 legs."],["Which planet is known as the Red Planet?","Mars","Mars looks red because of iron oxide dust."],["How many days are in a leap year?","366","A leap year adds February 29."],["How many sides does a hexagon have?","6","Hexa- means six."]];
function compose(seed,rnd,T,cat){
  var A=pickR(rnd,ANGLES);
  var kinds=['arithmetic','algebra','word-problems','logic','code-tracing','commonsense'];
  var want=(T&&T.c)||cat||pickR(rnd,kinds);
  var k=kinds.indexOf(want);if(k<0)k=(rnd()*6)|0;
  var prob,steps,ans,dom,diff,label,cat2=kinds[k];
  if(k===0){var a=12+((rnd()*88)|0),b=12+((rnd()*88)|0),c=2+((rnd()*49)|0);
    prob='What is '+a+' \u00d7 '+b+' + '+c+'?';ans=String(a*b+c);
    steps=['Multiply first: '+a+' \u00d7 '+b+' = '+(a*b)+'.','Then add '+c+': '+(a*b)+' + '+c+' = '+ans+'.','Answer: '+ans+'.'];
    dom='Arithmetic';diff='medium';label='Multi-digit multiplication';}
  else if(k===1){var m=2+((rnd()*8)|0),x=2+((rnd()*19)|0),bb=1+((rnd()*50)|0),cc=m*x+bb;
    prob='Solve for x: '+m+'x + '+bb+' = '+cc;ans='x = '+x;
    steps=['Subtract '+bb+': '+m+'x = '+(cc-bb)+'.','Divide by '+m+': x = '+x+'.','Answer: x = '+x+'.'];
    dom='Algebra';diff='medium';label='Two-step linear equation';}
  else if(k===2){var v=40+((rnd()*81)|0),tt=2+((rnd()*8)|0);
    prob='A train travels at '+v+' km/h for '+tt+' hours. How far does it go?';ans=String(v*tt)+' km';
    steps=['Distance = speed \u00d7 time.',v+' \u00d7 '+tt+' = '+(v*tt)+' km.','Answer: '+(v*tt)+' km.'];
    dom='Word problems';diff='easy';label='Distance word problem';}
  else if(k===3){var s=2+((rnd()*19)|0),d=2+((rnd()*8)|0),nx=s+d*4;
    prob='What comes next: '+s+', '+(s+d)+', '+(s+2*d)+', '+(s+3*d)+', ?';ans=String(nx);
    steps=['Each term grows by '+d+'.','Next = '+(s+3*d)+' + '+d+' = '+nx+'.','Answer: '+nx+'.'];
    dom='Logic';diff='easy';label='Number sequence';}
  else if(k===4){var lo=1+((rnd()*10)|0),hi=lo+5+((rnd()*10)|0),sum=0,i;
    for(i=lo;i<hi;i++)sum+=i;
    prob='What does this print?\ns = 0\nfor i in range('+lo+', '+hi+'):\n    s += i\nprint(s)';ans=String(sum);
    steps=['The loop adds every integer from '+lo+' to '+(hi-1)+'.','That sum is '+sum+'.','Output: '+sum+'.'];
    dom='Code tracing';diff='medium';label='Loop summation trace';}
  else{var q=pickR(rnd,COT_COMMON);prob=q[0];ans=q[1];
    steps=['Consider what is asked: '+q[0],'Reason: '+q[2],'Answer: '+q[1]+'.'];
    dom='Commonsense';diff='easy';label='Commonsense fact';}
  var strat=pickR(rnd,COT_STRATS);
  return {title:label+' \u2014 '+A,
    description:'A '+diff+' '+dom.toLowerCase()+' problem solved with '+strat+' ('+A+').',
    category:cat2,problem:prob,domain:dom,difficulty:diff,strategy:strat,
    thought_steps:steps,final_answer:ans,focus:A};
}
function generate(seed,opts,rnd){
  var r=rnd||mulberry(typeof seed==='number'?seed:hashStr(String(seed)));
  var cat=opts&&opts.category,pool=TOPICS;
  if(cat){var f=TOPICS.filter(function(t){return t.c===cat;});if(f.length)pool=f;}
  var T=pickR(r,pool);
  var rec=compose(seed,r,T,cat);
  if(!rec.id)rec.id=makeId(seed);
  if(!rec.title)rec.title=T.t;
  if(!rec.description)rec.description=T.d;
  if(!rec.category)rec.category=T.c;
  if(!rec.source)rec.source=T.s||'signature';
  if(T.r&&!rec.source_ref)rec.source_ref=T.r;
  rec.signature_mark=MARK;
  return rec;
}
function validate(rec){
  var errs=[],req=["id", "title", "description", "category", "problem", "thought_steps", "final_answer", "source"];
  if(!rec||typeof rec!=='object')return{ok:false,errors:['not an object']};
  req.forEach(function(k){if(rec[k]===undefined||rec[k]===null||rec[k]==='')errs.push('missing '+k);});
  if(rec.id&&!/^[A-Z0-9]+(-[A-Z0-9]+)*-[0-9]{7}$/.test(rec.id))errs.push('bad id format');
  if(rec.source&&['online','signature','fact-checked'].indexOf(rec.source)<0)errs.push('bad source');
  return{ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  var key;try{key=JSON.stringify(rec);}catch(e){return{ok:false,errors:['unstringifiable']};}
  sample=sample||[];
  for(var i=0;i<sample.length;i++){try{if(JSON.stringify(sample[i])===key)return{ok:false,errors:['exact duplicate of archive record']};}catch(e){}}
  return{ok:true,errors:[]};
}
var GEN={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){try{JAHDB.registerGenerator(SLUG,GEN);}catch(e){}}
if(typeof module!=='undefined'){module.exports=GEN;}
function runTests(){
  var pass=0,fail=0;
  function t(name,fn){try{if(fn()){pass++;}else{fail++;console.log('FAIL: '+name);}}catch(e){fail++;console.log('FAIL: '+name+' threw '+e.message);}}
  var i;
  for(i=1;i<=10;i++){(function(s){t('gen+validate seed '+s,function(){return validate(generate(s,{},null)).ok;});})(i);}
  for(i=11;i<=20;i++){(function(s){t('determinism seed '+s,function(){return JSON.stringify(generate(s,{},null))===JSON.stringify(generate(s,{},null));});})(i);}
  for(i=0;i<CATS.length;i++){(function(c){t('category filter '+c,function(){var r=generate(7,{category:c},null);return r.category===c&&validate(r).ok;});})(CATS[i]);}
  t('id format',function(){return /^[A-Z0-9]+(-[A-Z0-9]+)*-[0-9]{7}$/.test(generate(42,{},null).id);});
  t('title non-empty',function(){return String(generate(5,{},null).title).length>3;});
  t('description non-empty',function(){return String(generate(5,{},null).description).length>10;});
  t('source valid',function(){return['online','signature','fact-checked'].indexOf(generate(5,{},null).source)>=0;});
  t('signature mark',function(){return String(generate(5,{},null).signature_mark).indexOf('Signature')>=0;});
  t('reject empty',function(){return !validate({}).ok;});
  t('reject missing title',function(){var r=generate(3,{},null);delete r.title;return !validate(r).ok;});
  t('reject bad id',function(){var r=generate(3,{},null);r.id='nope';return !validate(r).ok;});
  t('driftCheck novel ok',function(){return driftCheck(generate(999,{},null),[]).ok;});
  t('driftCheck dupe caught',function(){var r=generate(999,{},null);return !driftCheck(r,[JSON.parse(JSON.stringify(r))]).ok;});
  t('distinct seeds distinct ids',function(){return generate(1001,{},null).id!==generate(1002,{},null).id;});
  t('json round-trip',function(){var r=generate(77,{},null);return JSON.parse(JSON.stringify(r)).id===r.id;});
  t('extra domain check',function(){var r=generate(9,{},null);return (r.thought_steps.length>=3);});
  t('version string',function(){return GEN.version===VERSION;});
  console.log(pass+'/40 '+(fail===0?'PASS':'FAIL'));
  if(fail>0&&typeof process!=='undefined')process.exitCode=1;
}
if(typeof require!=='undefined'&&require.main===module){runTests();}
})();
