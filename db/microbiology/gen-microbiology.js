(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['bacteria','viruses','fungi','ecology','lab'];
var PREFIX='JAH-MIC-';
var GRAMS=['positive','negative','variable','not applicable'];
var SHAPES=['rod','coccus','spiral','filamentous','pleomorphic','icosahedral'];
var ORGS={
 bacteria:[['Bacillus modelis','rod','positive'],['Coccus rotundus','coccus','positive'],['Spirillum flexa','spiral','negative'],['Filamenta longa','filamentous','variable']],
 viruses:[['Icosavirus model','icosahedral','not applicable'],['Helicovirus model','filamentous','not applicable'],['Envelopovirus model','pleomorphic','not applicable']],
 fungi:[['Mycelium expansum','filamentous','not applicable'],['Yeastia rotunda','coccus','not applicable'],['Sporangia alta','pleomorphic','not applicable']]
};
var HAB=['soil and decaying organic matter','freshwater biofilms','mammalian skin surface','plant root rhizosphere','deep-sea sediment','fermented food matrix'];
var TRAITS=['forms resistant spores under stress','produces extracellular enzymes','forms biofilms on surfaces','tolerates wide pH ranges','exchanges genes by horizontal transfer','grows across a broad temperature range'];
var MEDIA=[['blood agar','general growth of fastidious organisms'],['MacConkey agar','selective for Gram-negative rods'],['Sabouraud agar','fungal cultivation'],['nutrient broth','general liquid culture'],['thioglycollate','oxygen requirement testing']];
var TESTS=[['Gram stain','cell wall classification'],['catalase test','hydrogen peroxide breakdown'],['oxidase test','cytochrome c oxidase presence'],['coagulase test','plasma clotting ability'],['PCR assay','nucleic acid detection']];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var rec={id:id,category:cat,source:'signature',source_ref:'JAH Signature Generator',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
  if(cat==='bacteria'||cat==='viruses'||cat==='fungi'){
    var o=pick(ORGS[cat],rnd),n=ri(rnd,1,60);
    rec.title='Signature microbe model: '+o[0]+' '+n;
    var tr1=pick(TRAITS,rnd),tr2=pick(TRAITS,rnd);
    rec.description='A Signature-generated microbiology study model of '+o[0]+' strain '+n+', a '+o[2]+' '+o[1]+' organism. It '+tr1+' and '+tr2+'. Teaching model; not a verified taxonomic record.';
    rec.organism_name=o[0]+' strain '+n;rec.taxonomy={domain:cat==='bacteria'?'Bacteria':(cat==='viruses'?'Viruses':'Fungi'),model_group:o[0]};
    rec.gram_stain=o[2];rec.shape=o[1];rec.habitat=pick(HAB,rnd);
    rec.traits=[tr1[0].toUpperCase()+tr1.slice(1)+'.',tr2[0].toUpperCase()+tr2.slice(1)+'.'];
    rec.lab_note='Identify with standard '+pick(TESTS,rnd)[0]+' in a teaching laboratory setting.';
  }else if(cat==='ecology'){
    var ec=pick(['biofilm dynamics','nitrogen cycling','gut community balance','soil food web','aquatic bloom control','symbiosis modeling'],rnd);
    rec.title='Microbial ecology study: '+ec;
    rec.description='A teaching record on '+ec+' in microbial communities. Describes drivers, key processes, and measurement approaches in general educational terms.';
    rec.concept=ec;rec.drivers=[pick(HAB,rnd),'nutrient availability','temperature shifts'];
    rec.measurement='Community profiling and process-rate assays in teaching models.';
  }else{
    var m=pick(MEDIA.concat(TESTS),rnd);
    rec.title='Laboratory method: '+m[0];
    rec.description='A teaching record for the '+m[0]+' method, used for '+m[1]+'. Covers principle, basic steps, and interpretation in general educational terms.';
    rec.method=m[0];rec.purpose=m[1];rec.steps=['Prepare the material','Apply the method per teaching protocol','Read and record the result'];
  }
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MIC-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.category==='bacteria'||r.category==='viruses'||r.category==='fungi'){
    if(GRAMS.indexOf(r.gram_stain)<0)e.push('gram_stain');
    if(SHAPES.indexOf(r.shape)<0)e.push('shape');
    if(!r.taxonomy||typeof r.taxonomy!=='object')e.push('taxonomy');
    if(!Array.isArray(r.traits)||!r.traits.length)e.push('traits');
  }
  if(r.category==='ecology'&&typeof r.concept!=='string')e.push('concept');
  if(r.category==='lab'&&(typeof r.method!=='string'||!Array.isArray(r.steps)))e.push('lab');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-microbiology-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('microbiology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
