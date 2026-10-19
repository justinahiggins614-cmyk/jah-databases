(function(){'use strict';
/* JAH Organizations Directory Signature Database generator — jahdb-organizations-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ORG-SIG-";
var FIELDS=["Civil Rights & Advocacy", "Environment", "Faith & Community Charities", "Health", "Humanitarian & Relief", "Service Clubs", "Youth & Education"];
var TOPICS={
 "Civil Rights & Advocacy": [
  "Civil Rights & Advocacy: visiting and contact information",
  "Civil Rights & Advocacy: directory entry deep-dive",
  "Civil Rights & Advocacy: locations and service details",
  "Civil Rights & Advocacy: public records roundup",
  "Civil Rights & Advocacy: community programs index",
  "Civil Rights & Advocacy: finding and reaching listings"
 ],
 "Environment": [
  "Environment: visiting and contact information",
  "Environment: directory entry deep-dive",
  "Environment: locations and service details",
  "Environment: public records roundup",
  "Environment: community programs index",
  "Environment: finding and reaching listings"
 ],
 "Faith & Community Charities": [
  "Faith & Community Charities: visiting and contact information",
  "Faith & Community Charities: directory entry deep-dive",
  "Faith & Community Charities: locations and service details",
  "Faith & Community Charities: public records roundup",
  "Faith & Community Charities: community programs index",
  "Faith & Community Charities: finding and reaching listings"
 ],
 "Health": [
  "Health: visiting and contact information",
  "Health: directory entry deep-dive",
  "Health: locations and service details",
  "Health: public records roundup",
  "Health: community programs index",
  "Health: finding and reaching listings"
 ],
 "Humanitarian & Relief": [
  "Humanitarian & Relief: visiting and contact information",
  "Humanitarian & Relief: directory entry deep-dive",
  "Humanitarian & Relief: locations and service details",
  "Humanitarian & Relief: public records roundup",
  "Humanitarian & Relief: community programs index",
  "Humanitarian & Relief: finding and reaching listings"
 ],
 "Service Clubs": [
  "Service Clubs: visiting and contact information",
  "Service Clubs: directory entry deep-dive",
  "Service Clubs: locations and service details",
  "Service Clubs: public records roundup",
  "Service Clubs: community programs index",
  "Service Clubs: finding and reaching listings"
 ],
 "Youth & Education": [
  "Youth & Education: visiting and contact information",
  "Youth & Education: directory entry deep-dive",
  "Youth & Education: locations and service details",
  "Youth & Education: public records roundup",
  "Youth & Education: community programs index",
  "Youth & Education: finding and reaching listings"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature organizations directory search\n"
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
    name:topic+' — Signature organization record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A Signature organization record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"Signature organization record-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-organizations-directory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('organizations-directory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
