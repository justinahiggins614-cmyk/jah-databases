(function(){'use strict';
/* JAH Public Records Database generator — deterministic, every record validated.
   Signature records are SIMULATED DEMONSTRATION DATASETS — never presented
   as official records. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['statistics','reports','datasets','administrative','links'];
var PREFIX='JAH-PUB-';
var TYPES=['string','number','boolean','date'];
var NOTICE='SIMULATED DEMONSTRATION DATA — simulated for illustration, not official records.';
var SETS=[
 ['Civic library circulation','branch','visits'],
 ['Community garden plots','garden','gardeners'],
 ['Public park maintenance','park','work orders'],
 ['Neighborhood recycling','district','households'],
 ['Transit shelter repairs','route','shelters'],
 ['Farmers market vendors','market','vendors'],
 ['Public pool attendance','pool','swimmers'],
 ['Trail counter readings','trail','hikers'],
 ['Museum weekend visitors','museum','visitors'],
 ['School lunch program','school','meals served'],
 ['Street tree plantings','ward','trees'],
 ['Community center classes','center','enrollments']
];
function cell(r,type){
  if(type==='string')return pick(['North','South','East','West','Central','Riverside'],r);
  if(type==='number')return ri(r,5,5000);
  if(type==='boolean')return r()<0.7;
  return '2024-'+String(ri(r,1,12)).padStart(2,'0')+'-'+String(ri(r,1,28)).padStart(2,'0');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var st=pick(SETS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var cols=[{name:st[1]+'_name',type:'string'},{name:st[2].replace(/ /g,'_'),type:'number'},{name:pick(['recorded_on','verified','notes'],rnd)==='recorded_on'?'recorded_on':pick(['verified','notes'],rnd),type:'date'}];
  if(cols[2].name==='verified')cols[2].type='boolean';
  if(cols[2].name==='notes')cols[2].type='string';
  var nr=3,rows=[],i;
  for(i=0;i<nr;i++)rows.push(cols.map(function(c){return cell(rnd,c.type);}));
  var total=nr+ri(rnd,0,400);
  return {
    id:id,record_id:id,
    title:'Demonstration dataset: '+st[0],
    category:cat,dataset_name:st[0],
    description:'Simulated table modeling '+st[0].toLowerCase()+': '+cols.length+' columns, '+total+' rows ('+nr+'-row sample shown). '+NOTICE,
    columns:cols,rows_sample:rows,row_count_total:total,
    methodology:'Synthesized rows shaped like a real administrative table for practice reading public-style data.',
    published_year:ri(rnd,2020,2026),
    is_real:false,notice:NOTICE,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PUB-\d{7}$/.test(r.id||''))e.push('id');
  if(r.record_id!==r.id)e.push('record_id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='signature'){
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
    if(r.is_real!==false)e.push('is_real');
    if(typeof r.notice!=='string'||r.notice.indexOf('not official records')<0)e.push('notice');
    if(r.title.indexOf('Demonstration dataset:')!==0)e.push('title-prefix');
    if(typeof r.dataset_name!=='string'||!r.dataset_name.length)e.push('dataset_name');
    if(!Array.isArray(r.columns)||r.columns.length<3)e.push('columns');
    else r.columns.forEach(function(c){if(typeof c.name!=='string'||!c.name.length||TYPES.indexOf(c.type)<0)e.push('column');});
    if(!Array.isArray(r.rows_sample)||r.rows_sample.length<3)e.push('rows_sample');
    else r.rows_sample.forEach(function(row){
      if(!Array.isArray(row)||row.length!==r.columns.length)e.push('row-width');
      else row.forEach(function(v,j){
        var t=r.columns[j].type;
        if(t==='number'&&typeof v!=='number')e.push('row-type');
        if(t==='boolean'&&typeof v!=='boolean')e.push('row-type');
        if((t==='string'||t==='date')&&typeof v!=='string')e.push('row-type');
      });
    });
    if(typeof r.row_count_total!=='number'||r.row_count_total<r.rows_sample.length)e.push('row_count_total');
    if(typeof r.methodology!=='string'||!r.methodology.length)e.push('methodology');
    if(typeof r.published_year!=='number'||r.published_year<2020||r.published_year>2026)e.push('published_year');
  }else{
    if(r.is_real!==true)e.push('is_real');
    if(typeof r.source_ref!=='string'||!/^https?:\/\//.test(r.source_ref))e.push('source_ref');
    if(typeof r.topic!=='string'||!r.topic.length)e.push('topic');
    if(typeof r.source_name!=='string'||!r.source_name.length)e.push('source_name');
    if(typeof r.year!=='number'||r.year<1700||r.year>2026)e.push('year');
    if(!Array.isArray(r.key_statistics)||r.key_statistics.length<2)e.push('key_statistics');
    else r.key_statistics.forEach(function(s){if(typeof s.label!=='string'||!s.label.length||typeof s.value!=='string'||!s.value.length)e.push('key_statistic');});
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-public-records-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-records',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
