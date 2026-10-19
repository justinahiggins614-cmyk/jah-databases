(function(){'use strict';
/* JAH Financial Fraud Detection Database generator — jahdb-financial-fraud-detection-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FFD-";
var FIELDS=["transaction monitoring", "anomaly detection", "network analysis", "AML", "investigator tools", "adversarial dynamics"];
var TOPICS=[
    {t: "Fraud Types", b: "Card fraud, account takeover, wire fraud, insider abuse, money laundering: the threat taxonomy detection covers."},
    {t: "Transaction Monitoring", b: "Rules plus models scoring payments in milliseconds: the real-time front line."},
    {t: "Anomaly Detection", b: "Unsupervised methods flagging the unusual: essential where labeled fraud is rare and novel."},
    {t: "Supervised Models", b: "Gradient boosting on labeled cases: precision-recall trade-offs tuned to investigator capacity."},
    {t: "Network Analysis", b: "Graph methods exposing mule rings and laundering chains: fraud is organized, so detection must be too."},
    {t: "Behavioral Biometrics", b: "Keystroke, mouse, and device signals distinguishing legitimate users from impostors."},
    {t: "AML Compliance", b: "BSA/AML programs, KYC, SAR filing: the regulatory machinery detection serves."},
    {t: "Sanctions Screening", b: "Real-time list matching against OFAC/UN lists: fuzzy matching at wire speed."},
    {t: "Investigator Workflow", b: "Alert triage, case management, and feedback loops: the human system making models effective."},
    {t: "Adversarial Machine Learning", b: "Evasion, poisoning, and model theft: defending the detectors themselves."},
    {t: "Privacy and Data Sharing", b: "Consortium models and federated learning: catching cross-bank fraud without pooling customer data."},
    {t: "Measuring Effectiveness", b: "Dollars prevented, false-positive rates, investigator efficiency: the metrics proving the system's worth."}
];
var PRINCIPLES=[
    {n: "Fraud adapts to your model", e: "", s: "Static rules die: adversaries probe defenses, so detection must learn continuously."},
    {n: "Precision is operational", e: "", s: "Investigators can only review so many alerts: false-positive rate is the system's real constraint."},
    {n: "Explainability is compliance", e: "", s: "SAR narratives and examiner reviews demand reasons, not just scores."}
];
var USES=["Building transaction monitors", "Tuning alert thresholds", "Mapping fraud networks", "Filing SAR narratives"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Financial Fraud Detection"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fraud Detection Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-financial-fraud-detection-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-financial-fraud-detection-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("financial-fraud-detection",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
