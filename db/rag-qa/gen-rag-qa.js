(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['science','history','technology','health','geography','general'];
var PREFIX='JAH-RAG-';
/* rows: [domain, question, span1, span2, [extra sentences], answer] */
var Q=[
 ['science','Why is the sky blue?',
  'Sunlight scatters off air molecules in the atmosphere.',
  'Shorter blue wavelengths scatter most strongly.',
  ['At sunset the light path lengthens and reds dominate.','The effect was explained by Lord Rayleigh in the 1800s.'],
  'The sky is blue because sunlight scatters off air molecules, and the shorter blue wavelengths scatter most strongly.'],
 ['science','How do vaccines train the immune system?',
  'A vaccine introduces a harmless piece of the pathogen.',
  'The immune system builds memory cells against that marker.',
  ['On real exposure, memory cells respond faster and stronger.','Booster shots refresh those memory cells over time.'],
  'Vaccines present a harmless piece of the pathogen so the immune system builds memory cells against it.'],
 ['history','What caused the fall of the Western Roman Empire?',
  'The late empire faced economic strain and political instability.',
  'Pressure from migrating peoples stressed the frontiers.',
  ['By 476 CE the western administration had collapsed.','The eastern half survived another thousand years.'],
  'Economic strain, political instability, and pressure from migrating peoples brought down the Western Roman Empire.'],
 ['history','Why was the printing press revolutionary?',
  'Movable type let books be copied far faster than by hand.',
  'Ideas spread widely and cheaply across Europe as a result.',
  ['Before the press, books were copied slowly by hand.','Gutenberg printed his famous Bible around 1455.'],
  'The press was revolutionary because books could be copied far faster than by hand, so ideas spread widely and cheaply.'],
 ['technology','What does a neural network learn during training?',
  'Training adjusts weights that minimize prediction error.',
  'Over many examples the network captures patterns in the training data.',
  ['Those patterns generalize to new, similar inputs.','Deeper networks can capture more abstract patterns.'],
  'A neural network learns weights that minimize prediction error, capturing patterns in the training data.'],
 ['technology','How does public-key encryption work?',
  'Each user holds a public key that encrypts and a private key that decrypts.',
  'The private key is never shared with anyone.',
  ['Anyone can send a secret message using only the public key.','RSA and elliptic-curve systems both use this principle.'],
  'A public key encrypts messages that only the matching private key can decrypt, and the private key is never shared.'],
 ['health','Why is sleep important for memory?',
  'During sleep the brain replays and consolidates experiences.',
  'Deep sleep strengthens the neural connections behind memories.',
  ['Cutting sleep short measurably weakens next-day recall.','Most adults need seven to nine hours per night.'],
  'Sleep matters because the brain replays and consolidates experiences, and deep sleep strengthens neural connections.'],
 ['health','What makes a diet heart-healthy?',
  'Heart-healthy eating centers on vegetables, whole grains, and lean protein.',
  'It also means limited saturated fat and added sugar.',
  ['Small steady changes beat strict short-term diets.','Olive oil is a staple fat in Mediterranean eating patterns.'],
  'A heart-healthy diet centers on vegetables, whole grains, and lean protein, with limited saturated fat and added sugar.'],
 ['geography','Why does the Amazon matter globally?',
  'The Amazon holds about a tenth of known species on Earth.',
  'Its trees recycle vast amounts of rainfall across the continent.',
  ['Deforestation threatens both that biodiversity and the water cycle.','The river discharges more water than any other on Earth.'],
  'The Amazon matters because it holds about a tenth of known species and its trees recycle vast amounts of rainfall.'],
 ['geography','What causes ocean tides?',
  'Tides come mainly from the moon\u2019s gravity pulling on ocean water.',
  'The sun adds a smaller secondary pull.',
  ['Coasts typically see two high tides per lunar day.','Spring tides occur when sun and moon align.'],
  'Tides are caused by the moon\u2019s gravity pulling on ocean water, with the sun adding a smaller secondary pull.'],
 ['general','How should a beginner start learning a language?',
  'Research shows short daily sessions beat long weekly ones.',
  'Speaking early builds confidence even with mistakes.',
  ['Pair an app for vocabulary with real conversation practice.','Listening to songs helps train the ear for sounds.'],
  'Beginners should favor short daily sessions over long weekly ones, and speaking early builds confidence.'],
 ['general','What is the best way to back up important files?',
  'The rule of thumb is to keep at least two copies in different places.',
  'Automate the backup schedule so it actually happens.',
  ['Test a restore once a year to be sure the copies work.','Cloud plus local drive is a common pairing.'],
  'Keep at least two copies in different places and automate the backup schedule.']
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=Q.filter(function(q){return q[0]===cat;});
  var q=pick(pool.length?pool:Q,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var n=ri(rnd,2,3);
  var ex=q[4];
  var passages=[
    {doc_id:'DOC-'+String(1000+((seed*7)%9000)),text:q[2]+' '+ex[(seed)%ex.length],rank:1},
    {doc_id:'DOC-'+String(1000+((seed*7+131)%9000)),text:q[3]+' '+ex[(seed+1)%ex.length],rank:2}
  ];
  if(n>2)passages.push({doc_id:'DOC-'+String(1000+((seed*7+262)%9000)),text:ex[(seed)%ex.length]+' '+ex[(seed+1)%ex.length],rank:3});
  var spans=n>2?[q[2],q[3]]:[q[2]];
  return {id:id,qa_id:id,title:q[1],question:q[1],passages:passages,answer:q[5],cited_spans:spans,hops:ri(rnd,1,2),domain:cat,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-RAG-\d{6}$/.test(r.id||''))e.push('id');
  if(r.qa_id!==r.id)e.push('qa_id');
  if(r.title!==r.question)e.push('title');
  if(typeof r.question!=='string'||!r.question.length)e.push('question');
  if(!Array.isArray(r.passages)||r.passages.length<2||r.passages.length>3)e.push('passages');
  else r.passages.forEach(function(p,i){
    if(!p||!p.doc_id||typeof p.text!=='string'||!p.text.length)e.push('passage');
    if(p.rank!==i+1)e.push('rank');
  });
  if(typeof r.answer!=='string'||!r.answer.length)e.push('answer');
  if(!Array.isArray(r.cited_spans)||r.cited_spans.length<1||r.cited_spans.length>2)e.push('cited_spans');
  else{var all=r.passages.map(function(p){return p.text;}).join(' ');
    r.cited_spans.forEach(function(s){
      if(typeof s!=='string'||!s.length||all.indexOf(s)<0)e.push('span not verbatim in passages');
    });}
  if(r.hops!==1&&r.hops!==2)e.push('hops');
  if(CATS.indexOf(r.domain)<0)e.push('domain');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-rag-qa-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rag-qa',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
