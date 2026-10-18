(function(){'use strict';
/* JAH The Unsolved Sociology Signature Database generator — jahdb-unsolved-sociology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USSOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Secularization Puzzle (Signature Edition) - Culture",
  "The Decline of Social Capital (Signature Edition) - Culture",
  "The Culture of Poverty Debate (Signature Edition) - Culture",
  "Homophily Versus Influence (Signature Edition) - Networks",
  "How Do Networks Spread Behaviors (Signature Edition) - Networks",
  "The Strength of Weak Ties: Limits (Signature Edition) - Networks",
  "Why Did Crime Fall in the 90s (Signature Edition) - Deviance",
  "The Marriage Decline (Signature Edition) - Family",
  "The Bystander Effect: How Real (Signature Edition) - Behavior",
  "The Fundamental Cause of Health Inequality (Signature Edition) - Inequality",
  "Social Mobility: How Stuck Are We (Signature Edition) - Inequality"
 ],
 "Compounded": [
  "The Gender Pay Gap: What Explains It (Signature Edition) - Inequality",
  "The Racial Wealth Gap (Signature Edition) - Inequality",
  "Neighborhood Effects: How Much (Signature Edition) - Inequality",
  "The Cultural Omnivore Thesis (Signature Edition) - Culture",
  "Emotion Work and Emotional Labor (Signature Edition) - Culture",
  "The McDonaldization Limits (Signature Edition) - Institutions",
  "The Iron Law of Oligarchy: Still True (Signature Edition) - Institutions",
  "Bureaucracy: Can It Be Humane (Signature Edition) - Institutions",
  "The Credential Society (Signature Edition) - Institutions",
  "Moral Panics: Why Do They Erupt (Signature Edition) - Deviance",
  "The Labeling Theory Limits (Signature Edition) - Deviance",
  "Anomie in the Digital Age (Signature Edition) - Theory"
 ],
 "Advanced": [
  "The Great Gatsby Curve Mechanism (Signature Edition) - Inequality",
  "Intersectionality: From Theory to Measurement (Signature Edition) - Theory",
  "Structuration: Can It Be Tested (Signature Edition) - Theory",
  "The Social Construction of Reality: Limits (Signature Edition) - Theory",
  "Collective Memory: How Societies Remember (Signature Edition) - Culture",
  "The Sociology of Time (Signature Edition) - Culture",
  "Why Do Social Movements Succeed (Signature Edition) - Change",
  "The Diffusion of Innovations: What Spreads (Signature Edition) - Change",
  "Tipping Points in Social Change (Signature Edition) - Change",
  "The Attention Economy and Social Order (Signature Edition) - Change",
  "A Unified Theory of the Social (Signature Edition) - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Sociology Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-sociology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-sociology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-sociology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
