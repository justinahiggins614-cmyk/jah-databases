(function(){'use strict';
/* JAH Signature Photo Archive Database generator — jahdb-signature-photo-archive-1.0.
   Property of Justin Addam Higgins (JAH).
   Photo archive records: every photo documented with category, caption, and date.
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PHOTO-';
var FIELDS=['screenshot','product-image','photo','diagram','chapter-illustration'];
var CAPTIONS={
 'screenshot':['Database hub status capture','Archive page capture','Generator panel capture','Network statistics capture'],
 'product-image':['Product showcase image','Catalog item image','Featured product capture'],
 'photo':['Archived photograph','Documented photo record','Photo archive entry'],
 'diagram':['System diagram','Architecture diagram','Process flow diagram'],
 'chapter-illustration':['Chapter illustration','Manuscript figure','Illustrated plate']
};
function pad6(n){return String(n).padStart(6,'0');}
function generate(seed,opts){
  opts=opts||{};
  var rnd=prng(seed);
  var cat=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var id=PREFIX+pad6(seed);
  var caption=pick(CAPTIONS[cat],rnd);
  var title=caption+' '+pad6(seed);
  var rec={
    id:id,
    title:title,
    name:title,
    category:cat,
    caption:caption+' — Signature photo archive record '+id+', documented '+cat+'.',
    image_text:'',
    date:'2026-10-12',
    src:'signature-generated',
    type:'signature',
    description:'Signature photo archive: '+cat+'. '+title+'.',
    demo:{kind:'photo-tools',program:'function photoInfo(r){return r.id+" | "+r.category+" | "+r.date;}',note:'Photo record info demo.'},
    _seed:seed
  };
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.category)<0)e.push('category');
  if(!r.title)e.push('title');
  return e.length?{ok:false,errors:e}:{ok:true,errors:[]};
}
function driftCheck(a,b){
  var ka=JSON.stringify(a),kb=JSON.stringify(b);
  return ka===kb?{ok:true,errors:[]}:{ok:false,errors:['drift']};
}
if(typeof module!=='undefined'){module.exports={generate,validate,driftCheck,PREFIX,FIELDS};}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){
  JAHDB.registerGenerator('jahdb-signature-photo-archive-1.0',{generate,validate,driftCheck,fields:FIELDS});
}
})();
