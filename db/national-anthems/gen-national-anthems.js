(function(){'use strict';
/* National Anthems Database generator — jahdb-national-anthems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ANT-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
"Americas": ["United States \u2014 The Star-Spangled Banner", "Canada \u2014 O Canada", "Mexico \u2014 Himno Nacional Mexicano", "Brazil \u2014 Hino Nacional Brasileiro", "Argentina \u2014 Himno Nacional Argentino"],
"Europe": ["United Kingdom \u2014 God Save the King", "France \u2014 La Marseillaise", "Germany \u2014 Deutschlandlied (3rd verse)", "Italy \u2014 Il Canto degli Italiani", "Spain \u2014 Marcha Real", "Ukraine \u2014 Shche ne vmerla Ukraina", "Poland \u2014 Mazurek D\u0105browskiego", "Netherlands \u2014 Wilhelmus", "Belgium \u2014 La Braban\u00e7onne", "Switzerland \u2014 Swiss Psalm", "Austria \u2014 Land der Berge", "Sweden \u2014 Du gamla, du fria"],
"Asia": ["Japan \u2014 Kimigayo", "China \u2014 March of the Volunteers", "India \u2014 Jana Gana Mana", "South Korea \u2014 Aegukga", "Israel \u2014 Hatikvah", "Saudi Arabia \u2014 Aash Al-Maleek", "UAE \u2014 Ishy Bilady", "Pakistan \u2014 Qaumi Taranah", "Bangladesh \u2014 Amar Shonar Bangla", "Indonesia \u2014 Indonesia Raya"],
"Oceania": ["Australia \u2014 Advance Australia Fair", "New Zealand \u2014 God Defend New Zealand"],
"Africa": ["South Africa \u2014 Nkosi Sikelel' iAfrika / Die Stem", "Nigeria \u2014 Arise, O Compatriots", "Egypt \u2014 Bilady, Bilady, Bilady", "Kenya \u2014 Ee Mungu Nguvu Yetu", "Ghana \u2014 God Bless Our Homeland Ghana", "Ethiopia \u2014 Whedefit Gesgeshi"],
"Europe/Asia": ["Russia \u2014 State Anthem of Russia"],
"Asia/Europe": ["Turkey \u2014 \u0130stiklal Mar\u015f\u0131"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# national-anthems-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 chess opening record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A chess opening record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"chess-opening-repertoire-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-national-anthems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('national-anthems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
