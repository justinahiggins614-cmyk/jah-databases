(function(){'use strict';
/* JAH The Textile Guide Database generator — jahdb-textile-guide-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TXGD-";
var FIELDS=["Textile Foundations", "The Fabrics", "Textile Mastery"];
var TOPICS={
 "Textile Foundations": [
  "Why Textiles",
  "The Natural Fibers",
  "The Synthetic Fibers",
  "The Cotton Deep",
  "The Wool Deep",
  "The Silk Deep",
  "The Linen Deep",
  "The Weave Types",
  "The Knit Types",
  "The Denim Cloth",
  "The Finishes",
  "The Dye Methods"
 ],
 "The Fabrics": [
  "The Print Methods",
  "The Performance Fabrics",
  "The Sustainable Textiles",
  "The Fabric Weight",
  "The Drape Test",
  "The Hand Feel",
  "The Fabric Store",
  "The Swatch Library",
  "The Care Science",
  "The Textile History",
  "The Velvet Cloth",
  "The Corduroy Cloth",
  "The Chiffon Cloth",
  "The Tweed Cloth",
  "The Canvas Cloth"
 ],
 "Textile Mastery": [
  "The Future Fibers",
  "The Textile Oath",
  "The Textile Legacy",
  "The Jersey Cloth",
  "The Brocade Cloth",
  "The Organza Cloth",
  "The Flannel Cloth"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# textile — "+safe+"\n"
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
    name:topic+' — textile guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A textile guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"textile-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-textile-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('textile-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
