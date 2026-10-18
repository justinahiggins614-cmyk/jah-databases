(function(){'use strict';
/* JAH Signature Waterfowl Database generator — jahdb-waterfowl-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WFS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Mallard (Anas platyrhynchos)", "Signature Study: Canada Goose (Branta canadensis)", "Signature Study: Mute Swan (Cygnus olor)", "Signature Study: Trumpeter Swan (Cygnus buccinator)", "Signature Study: Wood Duck (Aix sponsa)", "Signature Study: Mandarin Duck (Aix galericulata)", "Signature Study: Northern Pintail (Anas acuta)", "Signature Study: American Wigeon (Mareca americana)", "Signature Study: Eurasian Wigeon (Mareca penelope)", "Signature Study: Gadwall (Mareca strepera)", "Signature Study: Northern Shoveler (Spatula clypeata)"], "Compounded": ["Signature Study: Blue-winged Teal (Spatula discors)", "Signature Study: Green-winged Teal (Anas crecca)", "Signature Study: Canvasback (Aythya valisineria)", "Signature Study: Redhead (Aythya americana)", "Signature Study: Greater Scaup (Aythya marila)", "Signature Study: Lesser Scaup (Aythya affinis)", "Signature Study: Common Eider (Somateria mollissima)", "Signature Study: King Eider (Somateria spectabilis)", "Signature Study: Harlequin Duck (Histrionicus histrionicus)", "Signature Study: Long-tailed Duck (Clangula hyemalis)", "Signature Study: Common Goldeneye (Bucephala clangula)", "Signature Study: Bufflehead (Bucephala albeola)"], "Advanced": ["Signature Study: Hooded Merganser (Lophodytes cucullatus)", "Signature Study: Common Merganser (Mergus merganser)", "Signature Study: Red-breasted Merganser (Mergus serrator)", "Signature Study: Ruddy Duck (Oxyura jamaicensis)", "Signature Study: Snow Goose (Anser caerulescens)", "Signature Study: Greater White-fronted Goose (Anser albifrons)", "Signature Study: Greylag Goose (Anser anser)", "Signature Study: Barnacle Goose (Branta leucopsis)", "Signature Study: Brant (Branta bernicla)", "Signature Study: Black Swan (Cygnus atratus)", "Signature Study: Egyptian Goose (Alopochen aegyptiaca)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('Sample record — structural sample, not an archive entry.')\n"
   + "print(record['topic'] + ' [' + record['field'] + ']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic,
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature waterfowl species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-generated",
    sample:true,
    disclaimer:"Generated Signature sample record \u2014 not an archive record. Seeded Signature records are the authoritative entries.",
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-waterfowl-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("waterfowl-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
