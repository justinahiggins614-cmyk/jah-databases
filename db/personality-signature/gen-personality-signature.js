(function(){'use strict';
/* JAH The Personality Signature Database generator — jahdb-personality-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRSLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Personality Is (Signature Edition) - Foundations",
  "Traits, States, and Types (Signature Edition) - Foundations",
  "The Big Five at a Glance (Signature Edition) - Foundations",
  "Openness to Experience (Signature Edition) - Foundations",
  "Conscientiousness: The Big Five Discipline Domain (Signature Edition) - Foundations",
  "Extraversion: The Big Five Energy Domain (Signature Edition) - Foundations",
  "Agreeableness: The Big Five Warmth Domain (Signature Edition) - Foundations",
  "Emotional Stability and Neuroticism (Signature Edition) - Foundations",
  "The HEXACO Model (Signature Edition) - Foundations",
  "Honesty-Humility (Signature Edition) - Foundations",
  "Facets: The Six Faces of Every Domain (Signature Edition) - Foundations",
  "Self-Reports, Observer Ratings, and Bias (Signature Edition) - Foundations",
  "Nature, Nurture, and the Sources of Traits (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Sixteen Types of Jung and Myers-Briggs (Signature Edition) - Compounded",
  "Introversion, Extraversion, and Ambiversion in Daily Life (Signature Edition) - Compounded",
  "The Enneagram: Nine Motivational Patterns (Signature Edition) - Compounded",
  "DISC: Four Behavioral Styles (Signature Edition) - Compounded",
  "The Four Temperaments (Signature Edition) - Compounded",
  "The Sixteen Personality Factors (Signature Edition) - Compounded",
  "How Traits Combine: Reading a Full Profile (Signature Edition) - Compounded",
  "Personality at Work (Signature Edition) - Compounded",
  "Personality in Relationships (Signature Edition) - Compounded",
  "Measuring Personality: Reliability and Validity (Signature Edition) - Compounded",
  "The Person-Situation Debate (Signature Edition) - Compounded",
  "Team Chemistry: Traits in Groups (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Trait Stability and Change Across the Lifespan (Signature Edition) - Advanced",
  "Personality Development: The Maturity Principle (Signature Edition) - Advanced",
  "Personality and Decision-Making (Signature Edition) - Advanced",
  "Reading Others Ethically (Signature Edition) - Advanced",
  "Personality and Leadership (Signature Edition) - Advanced",
  "Personality Across Cultures (Signature Edition) - Advanced",
  "Conflict Styles and Personality (Signature Edition) - Advanced",
  "Growing on Purpose: Developing Your Traits (Signature Edition) - Advanced",
  "The Integrated View: One Person, Many Models (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Personality Study — "+safe+"\n"
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
    name:topic+' — personality record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A personality record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"personality-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-personality-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personality-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
