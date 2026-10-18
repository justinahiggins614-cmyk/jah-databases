(function(){'use strict';
/* JAH The Unsolved Sociology Database generator — jahdb-unsolved-sociology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USSO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Secularization Puzzle - Culture",
  "The Decline of Social Capital - Culture",
  "The Culture of Poverty Debate - Culture",
  "Homophily Versus Influence - Networks",
  "How Do Networks Spread Behaviors - Networks",
  "The Strength of Weak Ties: Limits - Networks",
  "Why Did Crime Fall in the 90s - Deviance",
  "The Marriage Decline - Family",
  "The Bystander Effect: How Real - Behavior",
  "The Fundamental Cause of Health Inequality - Inequality",
  "Social Mobility: How Stuck Are We - Inequality"
 ],
 "Compounded": [
  "The Gender Pay Gap: What Explains It - Inequality",
  "The Racial Wealth Gap - Inequality",
  "Neighborhood Effects: How Much - Inequality",
  "The Cultural Omnivore Thesis - Culture",
  "Emotion Work and Emotional Labor - Culture",
  "The McDonaldization Limits - Institutions",
  "The Iron Law of Oligarchy: Still True - Institutions",
  "Bureaucracy: Can It Be Humane - Institutions",
  "The Credential Society - Institutions",
  "Moral Panics: Why Do They Erupt - Deviance",
  "The Labeling Theory Limits - Deviance",
  "Anomie in the Digital Age - Theory"
 ],
 "Advanced": [
  "The Great Gatsby Curve Mechanism - Inequality",
  "Intersectionality: From Theory to Measurement - Theory",
  "Structuration: Can It Be Tested - Theory",
  "The Social Construction of Reality: Limits - Theory",
  "Collective Memory: How Societies Remember - Culture",
  "The Sociology of Time - Culture",
  "Why Do Social Movements Succeed - Change",
  "The Diffusion of Innovations: What Spreads - Change",
  "Tipping Points in Social Change - Change",
  "The Attention Economy and Social Order - Change",
  "A Unified Theory of the Social - Theory"
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
var gen={version:'jahdb-unsolved-sociology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-sociology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
