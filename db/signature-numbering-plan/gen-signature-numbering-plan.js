(function(){'use strict';
/* JAH Signature Numbering Plan Database generator — jahdb-signature-numbering-plan-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SNP-";
var FIELDS=["Region codes","Service codes","Exchange codes","Toll & info codes","Offsite relay codes"];
var TOPICS={
 "Region codes": [
  "001 \u2014 Signature Prime Meridian",
  "002 \u2014 Signature Capital Lattice",
  "003 \u2014 Signature Harbor Grid",
  "004 \u2014 Signature Foundry Belt",
  "005 \u2014 Signature Archive Reaches",
  "006 \u2014 Signature Aurora Field",
  "007 \u2014 Signature Meridian Expanse",
  "008 \u2014 Signature Compass Rose",
  "009 \u2014 Signature Beacon Shores",
  "010 \u2014 Signature Keystone Works",
  "011 \u2014 Signature Northlight",
  "012 \u2014 Signature Southgate"
 ],
 "Service codes": [
  "7000 \u2014 Signature Operator",
  "7001 \u2014 Signature Emergency Relay",
  "7002 \u2014 Signature Directory",
  "7003 \u2014 Signature Repair Line",
  "7004 \u2014 Signature Time Signal",
  "7005 \u2014 Signature Weather Wire",
  "7006 \u2014 Signature Archive Desk",
  "7007 \u2014 Signature Maker Line",
  "7008 \u2014 Signature Relay for the Deaf",
  "7009 \u2014 Signature Night Desk",
  "7010 \u2014 Signature Numbering Desk",
  "7011 \u2014 Signature Test Exchange"
 ],
 "Exchange codes": [
  "210 \u2014 Signature Exchange 210 \u2014 Prime Exchange",
  "211 \u2014 Signature Exchange 211 \u2014 Capital Exchange",
  "212 \u2014 Signature Exchange 212 \u2014 Harbor Exchange",
  "213 \u2014 Signature Exchange 213 \u2014 Foundry Exchange",
  "214 \u2014 Signature Exchange 214 \u2014 Archive Exchange",
  "215 \u2014 Signature Exchange 215 \u2014 Aurora Exchange",
  "216 \u2014 Signature Exchange 216 \u2014 Meridian Exchange",
  "217 \u2014 Signature Exchange 217 \u2014 Compass Exchange",
  "218 \u2014 Signature Exchange 218 \u2014 Beacon Exchange",
  "219 \u2014 Signature Exchange 219 \u2014 Keystone Exchange",
  "220 \u2014 Signature Exchange 220 \u2014 Northlight Exchange",
  "221 \u2014 Signature Exchange 221 \u2014 Southgate Exchange"
 ],
 "Toll & info codes": [
  "8000 \u2014 Signature Freefone 8000",
  "8001 \u2014 Signature Info 8001 \u2014 System Status",
  "8002 \u2014 Signature Info 8002 \u2014 Numbering News",
  "8003 \u2014 Signature Info 8003 \u2014 Archive Highlights",
  "8004 \u2014 Signature Info 8004 \u2014 Build Queue",
  "8005 \u2014 Signature Freefone 8005 \u2014 Help Desk",
  "8006 \u2014 Signature Freefone 8006 \u2014 Order Line",
  "8007 \u2014 Signature Info 8007 \u2014 Region Guide",
  "8008 \u2014 Signature Freefone 8008 \u2014 Repair Dispatch",
  "8009 \u2014 Signature Info 8009 \u2014 Trial Codes",
  "8010 \u2014 Signature Freefone 8010 \u2014 Directory Help",
  "8011 \u2014 Signature Info 8011 \u2014 Dialing School"
 ],
 "Offsite relay codes": [
  "9000 \u2014 Signature Offsite Relay 9000",
  "9001 \u2014 Signature Offsite Relay 9001 \u2014 Archive Mirror",
  "9002 \u2014 Signature Offsite Relay 9002 \u2014 AI Relay",
  "9003 \u2014 Signature Offsite Relay 9003 \u2014 Maker Relay",
  "9004 \u2014 Signature Offsite Relay 9004 \u2014 Directory Relay",
  "9005 \u2014 Signature Offsite Relay 9005 \u2014 Emergency Relay",
  "9006 \u2014 Signature Offsite Relay 9006 \u2014 Time Relay",
  "9007 \u2014 Signature Offsite Relay 9007 \u2014 Test Relay",
  "9008 \u2014 Signature Offsite Relay 9008 \u2014 Message Relay",
  "9009 \u2014 Signature Offsite Relay 9009 \u2014 Conference Relay",
  "9010 \u2014 Signature Offsite Relay 9010 \u2014 Data Relay",
  "9011 \u2014 Signature Offsite Relay 9011 \u2014 Night Relay"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature Numbering Study — "+safe+"\n"
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
    name:topic+' — Signature numbering record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A Signature numbering record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"signature-numbering",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-signature-numbering-plan-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-numbering-plan',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
