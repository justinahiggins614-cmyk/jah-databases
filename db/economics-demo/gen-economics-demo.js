(function(){'use strict';
/* JAH Economics Database generator — deterministic, every record validated.
   Signature records are SIMULATED ECONOMIC SCENARIOS — never presented
   as real economic data. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['indicators','markets','demographics','policy','trade'];
var PREFIX='JAH-ECO-';
var NOTICE='SIMULATED ECONOMIC SCENARIO — a teaching model, not real economic data.';
var SCEN=[
 ['a harvest festival boosting a market town','festival spending','vendor income'],
 ['a new bridge cutting freight time','freight cost','delivery speed'],
 ['a skills program lifting wages','training hours','median wage'],
 ['a harbor dredging deepening trade','port fees','cargo volume'],
 ['a drought shifting crop prices','rainfall','grain price'],
 ['a night market extending hours','open hours','stall revenue'],
 ['a rail spur linking two towns','rail freight','local prices'],
 ['a craft fair drawing tourists','visitor count','lodging income'],
 ['a mill upgrading its looms','output per hour','unit cost'],
 ['a fishing quota protecting stocks','catch limit','stock recovery']
];
var VARS=[['household spending','credits'],['vendor income','credits'],['freight cost','credits/ton'],['median wage','credits/week'],['cargo volume','tons'],['stall revenue','credits/day'],['unit cost','credits'],['visitor count','people']];
function fmt(n){return Math.round(n*100)/100;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var sc=pick(SCEN,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var vars=[],used={},i;
  for(i=0;i<2;i++){
    var v=pick(VARS,rnd);if(used[v[0]]){i--;continue;}used[v[0]]=1;
    var base=fmt(50+rnd()*950),pct=fmt((rnd()*24-8));
    vars.push({name:v[0],base_value:base,unit:v[1],change_pct:pct,projected_value:fmt(base*(1+pct/100))});
  }
  return {
    id:id,record_id:id,
    title:'Simulated scenario: '+sc[0],
    category:cat,
    scenario:'What if '+sc[0]+'? This teaching model traces '+sc[1]+' to '+sc[2]+' through two linked variables. '+NOTICE,
    variables:vars,
    assumptions:[pick(['Demand holds steady during the change.','No outside shocks hit the market.','Prices adjust within one season.'],rnd),pick(['Households spend freed income locally.','Suppliers pass half the savings on.'],rnd)],
    outcomes:['If the driver moves as modeled, '+sc[2]+' shifts with it.','Learners recompute the projections when any input changes.'],
    is_real:false,notice:NOTICE,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ECO-\d{7}$/.test(r.id||''))e.push('id');
  if(r.record_id!==r.id)e.push('record_id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.scenario!=='string'||r.scenario.length<40)e.push('scenario');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='signature'){
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
    if(r.is_real!==false)e.push('is_real');
    if(typeof r.notice!=='string'||r.notice.indexOf('not real economic data')<0)e.push('notice');
    if(r.title.indexOf('Simulated scenario:')!==0)e.push('title-prefix');
    if(!Array.isArray(r.variables)||r.variables.length<2)e.push('variables');
    else r.variables.forEach(function(v){
      if(typeof v.name!=='string'||!v.name.length)e.push('var-name');
      if(typeof v.base_value!=='number'||typeof v.change_pct!=='number'||typeof v.projected_value!=='number')e.push('var-numbers');
      else{
        if(v.change_pct<-50||v.change_pct>50)e.push('var-pct-range');
        var exp=v.base_value*(1+v.change_pct/100);
        if(Math.abs(exp-v.projected_value)>Math.max(0.01,Math.abs(exp)*0.005))e.push('var-projected-recompute');
      }
    });
    if(!Array.isArray(r.assumptions)||r.assumptions.length<2)e.push('assumptions');
    if(!Array.isArray(r.outcomes)||!r.outcomes.length)e.push('outcomes');
  }else{
    if(r.is_real!==true)e.push('is_real');
    if(typeof r.source_ref!=='string'||!/^https?:\/\//.test(r.source_ref))e.push('source_ref');
    if(typeof r.indicator!=='string'||!r.indicator.length)e.push('indicator');
    if(typeof r.year!=='number'||r.year<1900||r.year>2026)e.push('year');
    if(typeof r.value_text!=='string'||!r.value_text.length)e.push('value_text');
    if(typeof r.description!=='string'||r.description.length<20)e.push('description');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-economics-demo-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('economics-demo',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
