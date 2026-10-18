(function(){'use strict';
/* JAH The Everything United Nations Database generator — jahdb-everything-united-nations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVNAT-";
var FIELDS=["Organization","Organs","History","Agencies"];
var TOPICS={
 "Organization": [
  "The Founding of the United Nations \u2014 Organization",
  "Secretaries-General of the UN \u2014 Organization",
  "Multilateral Design (Signature Edition) \u2014 Organization"
 ],
 "Organs": [
  "The Security Council \u2014 Organs",
  "The General Assembly \u2014 Organs",
  "The Signature Assembly (Signature Edition) \u2014 Organs"
 ],
 "History": [
  "UN Peacekeeping \u2014 History",
  "The Universal Declaration of Human Rights \u2014 History",
  "Peacekeeping Doctrine (Signature Edition) \u2014 History"
 ],
 "Agencies": [
  "The Specialized Agencies \u2014 Agencies",
  "The Sustainable Development Goals \u2014 Agencies",
  "Global Governance (Signature Edition) \u2014 Agencies"
 ]
};
/* ============ EXPANSION 2026-10-17 (audit item 42) ============
   International organizations beyond the UN: WHO, WTO, IMF, World Bank,
   regional bodies — mandates, membership, agreements. Opt-in via
   opts.field; existing UN fields untouched. */
FIELDS.push('WHO','WTO','IMF','World Bank','Regional Bodies');
var BASE_FIELDS=['Organization','Organs','History','Agencies'];
var EVNAT_FACTS={"WHO": "The World Health Organization, founded in 1948 and headquartered in Geneva, is the UN specialized agency for international public health, with 194 member states. Its World Health Assembly sets global health policy; its emergency program coordinates outbreak response.", "WTO": "The World Trade Organization, established in 1995 under the Marrakesh Agreement and headquartered in Geneva, administers the multilateral trading system for 166 members. It grew out of the GATT (1948) and settles trade disputes between members.", "IMF": "The International Monetary Fund, created at Bretton Woods in 1944 and headquartered in Washington, DC, promotes global monetary stability for 190 member countries. It lends to countries in balance-of-payments difficulty and issues Special Drawing Rights.", "World Bank": "The World Bank Group, founded at Bretton Woods in 1944 and headquartered in Washington, DC, fights poverty through development lending. Its IBRD arm lends to middle-income governments and its IDA arm supports the poorest countries; 189 states are IBRD members.", "Regional Bodies": "Regional organizations — the African Union (2002, Addis Ababa), European Union (1993 Maastricht Treaty), ASEAN (1967), Organization of American States (1948), and Arab League (1945) — handle collective security, trade, and development for their regions alongside the UN system."};
Object.keys({"WHO": ["WHO Mandate — WHO", "WHO Membership — WHO", "World Health Assembly — WHO", "WHO Emergency Response — WHO", "WHO Regional Offices — WHO"], "WTO": ["WTO Mandate — WTO", "WTO Membership — WTO", "WTO Agreements — WTO", "WTO Dispute Settlement — WTO", "GATT to WTO — WTO"], "IMF": ["IMF Mandate — IMF", "IMF Membership — IMF", "IMF Lending Programs — IMF", "Special Drawing Rights — IMF", "Bretton Woods Origins — IMF"], "World Bank": ["World Bank Mandate — World Bank", "World Bank Membership — World Bank", "IBRD and IDA — World Bank", "World Bank Projects — World Bank", "Bretton Woods Origins — World Bank"], "Regional Bodies": ["African Union — Regional Bodies", "European Union — Regional Bodies", "ASEAN — Regional Bodies", "Organization of American States — Regional Bodies", "Arab League — Regional Bodies"]}).forEach(function(f){TOPICS[f]={"WHO": ["WHO Mandate — WHO", "WHO Membership — WHO", "World Health Assembly — WHO", "WHO Emergency Response — WHO", "WHO Regional Offices — WHO"], "WTO": ["WTO Mandate — WTO", "WTO Membership — WTO", "WTO Agreements — WTO", "WTO Dispute Settlement — WTO", "GATT to WTO — WTO"], "IMF": ["IMF Mandate — IMF", "IMF Membership — IMF", "IMF Lending Programs — IMF", "Special Drawing Rights — IMF", "Bretton Woods Origins — IMF"], "World Bank": ["World Bank Mandate — World Bank", "World Bank Membership — World Bank", "IBRD and IDA — World Bank", "World Bank Projects — World Bank", "Bretton Woods Origins — World Bank"], "Regional Bodies": ["African Union — Regional Bodies", "European Union — Regional Bodies", "ASEAN — Regional Bodies", "Organization of American States — Regional Bodies", "Arab League — Regional Bodies"]}[f];});
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything United Nations — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(BASE_FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=(opts.topic_idx!=null)?pool[opts.topic_idx%pool.length]:pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — united nations record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+(EVNAT_FACTS[field]||('A united nations record of "'+topic+'" in '+field+'.'))+' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-everything-united-nations-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-united-nations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
