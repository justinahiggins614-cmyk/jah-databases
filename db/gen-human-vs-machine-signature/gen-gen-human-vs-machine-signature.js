(function(){'use strict';
/* JAH The Human vs. Machine Signature Database generator - jahdb-gen-human-vs-machine-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Real generation, not a sample. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX="JAH-HVMS-";
var FIELDS=["Mind Contests", "Body Contests", "Creation Contests"];
var DOMAINS=[
 {d:'Memory recall',h:'Human episodic memory',m:'SSD + database index',  crit:[['Capacity',30,55,98],['Recall speed',25,60,99],['Associative leaps',25,92,40],['Energy use',20,95,55]]},
 {d:'Chess',h:'Grandmaster intuition',m:'Chess engine search',  crit:[['Tactical accuracy',35,80,99],['Strategic creativity',25,90,70],['Endurance',20,60,100],['Learning from one game',20,85,55]]},
 {d:'Image recognition',h:'Human vision + context',m:'Vision neural network',  crit:[['Raw classification speed',30,55,98],['Novel objects',30,88,60],['Context reasoning',25,90,55],['Adversarial robustness',15,80,45]]},
 {d:'Navigation',h:'Human wayfinding',m:'GPS + routing engine',  crit:[['Route precision',30,60,99],['No-signal operation',25,85,20],['Landmark memory',25,88,50],['Traffic adaptation',20,75,95]]},
 {d:'Language translation',h:'Bilingual speaker',m:'Machine translation model',  crit:[['Idiom handling',30,88,65],['Speed (words/min)',25,50,99],['Cultural nuance',25,90,60],['Low-resource languages',20,70,75]]},
 {d:'Medical diagnosis',h:'Physician judgment',m:'Diagnostic AI',  crit:[['Pattern breadth',30,70,92],['Patient context',30,92,55],['Rare-case reasoning',20,85,60],['Accountability',20,95,40]]},
 {d:'Music composition',h:'Human composer',m:'Generative music model',  crit:[['Emotional intent',35,92,55],['Output volume',25,45,99],['Style fusion',20,85,75],['Live improvisation',20,88,50]]},
 {d:'Physical dexterity',h:'Human hand',m:'Robotic gripper',  crit:[['Fine manipulation',35,95,70],['Repeatability',25,60,99],['Tool improvisation',20,90,45],['Fatigue resistance',20,40,99]]}
];
function scoreMatch(dom,rnd){
  var tot=0,hs=0,ms=0,i,c;
  var rows=[];
  for(i=0;i<dom.crit.length;i++){c=dom.crit[i];tot+=c[1];hs+=c[1]*c[2];ms+=c[1]*c[3];
    rows.push({criterion:c[0],weight:c[1],human:c[2],machine:c[3]});}
  hs/=tot;ms/=tot;
  return {rows:rows,human:hs,machine:ms,winner:hs>=ms?'human':'machine',margin:Math.abs(hs-ms)};
}
function demoProgram(topic,field,res){
  var L=['# '+topic,'# Field: '+field,'# transparent-criteria scoring replay',''];
  res.rows.forEach(function(r){
   L.push('criterion = '+JSON.stringify(r.criterion)+'  # weight '+r.weight+'%: human '+r.human+', machine '+r.machine);});
  L.push('');
  L.push('hs = '+res.hs.toFixed(2)+'  # weighted human total');
  L.push('ms = '+res.ms.toFixed(2)+'  # weighted machine total');
  L.push('winner = '+JSON.stringify(res.winner));
  L.push('assert winner == '+JSON.stringify(res.winner));
  L.push('print("human %.1f vs machine %.1f -> %s wins" % (hs, ms, winner))');
  L.push('print("OK: matchup scored transparently")');
  return L.join('\n')+'\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var dom=pick(DOMAINS,rnd);
  var res=scoreMatch(dom,rnd);
  var topic='Human vs Machine: '+dom.d;
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,name:topic+' - generated challenge',title:topic,
   description:'GENERATED CHALLENGE. '+dom.h+' versus '+dom.m+' in '+dom.d+', scored on '
    +res.rows.length+' transparent criteria. Verdict: '+res.winner+' wins '
    +res.human.toFixed(1)+' to '+res.machine.toFixed(1)+' (margin '+res.margin.toFixed(1)+').',
   field:field,domain:dom.d,human:dom.h,machine:dom.m,rows:res.rows,
   human_score:+res.human.toFixed(1),machine_score:+res.machine.toFixed(1),
   winner:res.winner,src:'signature-generated',sample:true,
   disclaimer:'Generated challenge - not an archive record.',
   demo:{kind:'human-vs-machine-demo',language:'python',
    program:demoProgram(topic,field,{h:dom.h,m:dom.m,hs:res.human,ms:res.machine,winner:res.winner,rows:res.rows}),
    note:'Runnable scoring of this exact matchup.'},_seed:seed};
}
function validate(r){var e=[];
 if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
 if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
 if(FIELDS.indexOf(r.field)<0)e.push('field');
 if(!r.winner)e.push('winner');
 if(!r.demo||!r.demo.program)e.push('demo');
 return{ok:!e.length,errors:e};}
function driftCheck(record,sample){var dups=(sample||[]).filter(function(r){return r&&r.domain===record.domain;});
 return dups.length?{ok:false,errors:['domain already in archive sample']}:{ok:true,errors:[]};}
var gen={version:"jahdb-gen-human-vs-machine-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:["Mind Contests", "Body Contests", "Creation Contests"]};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-human-vs-machine-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
