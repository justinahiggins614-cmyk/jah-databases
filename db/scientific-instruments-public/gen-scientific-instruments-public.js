(function(){'use strict';
/* Scientific Instruments Database generator — jahdb-scientific-instruments-public-1.0.
   Property of Justin Addam Higgins (JAH).
   PUBLIC type: creates blank collection-record TEMPLATES, clearly labeled,
   with NO museum attribution. Never fabricate holdings or museum attributions.
   Deterministic: same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-SCI-PUB-';
var KINDS=["telescope", "microscope", "astrolabe", "chronometer", "orrery", "barometer", "sextant", "calculator", "electrical-apparatus", "surveying-instrument"];
var FIELDS=["astronomy", "navigation", "horology", "optics", "electrical science", "surveying"];
var idRe=/^JAH\-SCI\-PUB\-\d{6}$/;
function normKind(g){
 if(!g) return null;
 var t=String(g).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
 for(var i=0;i<KINDS.length;i++){ if(KINDS[i]===t||KINDS[i].indexOf(t)>=0||t.indexOf(KINDS[i])>=0) return KINDS[i]; }
 return null;
}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function generate(seed,opts,rnd){
 opts=opts||{}; rnd=rnd||prng(seed);
 var topic=(opts.topic||'').toString().trim().slice(0,120);
 var kind=normKind(opts.genre)||pick(KINDS,rnd);
 var field=pick(FIELDS,rnd);
 var id=PREFIX+String(seed).padStart(6,'0');
 var title=topic?('Collection template: '+topic+' ('+kind+')'):('Collection template: '+cap(kind)+' — '+cap(field)+' record');
 var desc='A blank, clearly-labeled collection-record template for a '+kind+' in the field of '+field+(topic?' on the theme "'+topic+'"':'')+'. This template carries NO museum attribution and documents NO real holding: it is a starting form for cataloguers to fill in with verified provenance. Never cite it as belonging to any museum.';
 var content={record_kind:kind,field:field,theme:topic||'(none given)',
  template_fields:['title','creator/maker','date','material','dimensions','holding_museum','city','country','images','historical_context','provenance_note'],
  instructions:'Fill every field from the holding museum\u2019s official collection catalog. Do not invent attributions.'};
 return {id:id,title:title,description:desc,genre:kind,type:'museum collection record',
  museum:null,city:null,country:null,images:[],
  view_3d:null,video:null,audio_guide:null,
  content:content,historical_context:'(template — to be completed with verified historical and cultural context from the holding museum\u2019s published catalog)',
  provenance_note:'TEMPLATE ONLY — no real museum attribution. Not a real holding.',
  attribution:'TEMPLATE — no real museum attribution; not a real holding. Never cite as belonging to any museum.',
  demo:{kind:'museum-label-viewer',program:'function museumLabel(r){var w=window.open(\'\',\'_blank\');var d=w.document;d.write(\'<h1>\'+r.title+\'</h1><p>\'+r.description+\'</p>\');d.close();}\nmuseumLabel(RECORD);',note:'Paste into a browser console with RECORD set to this record JSON to preview a museum label.'},
  src:'public-template',_seed:seed,topic:topic||undefined};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!idRe.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(KINDS.indexOf(r.genre)<0)e.push('genre');
 if(!r.content||typeof r.content!=='object')e.push('content');
 if(r.src!=='public-template')e.push('src must be public-template');
 if(r.museum||r.city||r.country)e.push('templates must carry no museum attribution');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-scientific-instruments-public-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:KINDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-instruments-public',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
