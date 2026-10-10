/* ✳ SIGNATURE — JAH Antique Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-ANTQ-0000001 .. JAH-ANTQ-1000000). Browser: registers with JAHDB. Node:
   run `node gen-antiques.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='antiques', PREFIX='JAH-ANTQ-', VERSION='jahdb-antiques-1.0';
var KIND='antique', AI='JAH Antique Creator';
var CATEGORIES=["furniture", "ceramics", "glassware", "silver", "clocks", "rugs", "lighting", "bronzes"];
var MAKERS=["Signature Antiquities", "JAH Heritage House", "Meridian Antiques", "Heritage Craft Atelier", "Apex Antiquities", "Continental Antiques", "Paramount Heritage", "Golden Age Antiques", "Vantage Antiquities", "Legacy Heritage House", "Copperline Antiques", "Regent Antiquities"], LINES=["Heritage Collection", "Master Craft Series", "Estate Find", "Atelier Revival", "Centennial Piece", "Artisan Edition", "Provenance Set", "Golden Age", "Founder Piece", "Origin Collection"], WORDS=["hand-planed joinery", "a rich aged patina", "documented maker marks", "original period hardware", "a single-estate provenance", "museum-quality condition", "hand-applied finishes", "a signed master mark"], DESCS=["Cabinet", "Chair", "Vase", "Clock", "Mirror", "Table", "Chest", "Lamp", "Bowl", "Figure", "Desk", "Screen"];
var SPEC_KEYS=["Period", "Material", "Dimensions", "Maker", "Provenance", "Condition"], SPEC_VALS=[["19th century", "early 20th century", "18th century", "late 19th century"], ["mahogany", "porcelain", "sterling silver", "cut glass"], ["60 x 40 x 30 cm", "120 x 80 cm", "25 cm high", "90 x 60 cm"], ["Signature Antiquities", "Heritage Craft Atelier", "Meridian Antiques", "unknown master"], ["single estate", "documented collection", "gallery provenance", "family descent"], ["excellent", "very good", "restored", "original condition"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Faberge Imperial Easter Egg", "mk": "House of Faberge", "yr": "1885", "cat": "silver", "blurb": "Sixty-nine Imperial Eggs were made for the Russian tsars between 1885 and 1917; each is unique.", "spec": {"Maker": "House of Faberge", "Years": "1885-1917", "Made": "69 Imperial Eggs", "Workmaster": "Peter Carl Faberge"}, "ref": "Faberge Imperial Egg archives."}, {"t": "Ming Dynasty Xuande Porcelain", "mk": "Imperial kilns, Jingdezhen", "yr": "1426", "cat": "ceramics", "blurb": "Xuande-period (1426-1435) blue-and-white porcelain is the benchmark of Ming ceramic art.", "spec": {"Period": "Xuande, 1426-1435", "Kiln": "Jingdezhen imperial", "Ware": "Blue-and-white", "Status": "Benchmark Ming ware"}, "ref": "Ming ceramic scholarship, Jingdezhen."}, {"t": "Meissen Porcelain Figure", "mk": "Meissen", "yr": "1710", "cat": "ceramics", "blurb": "Meissen made Europe's first true hard-paste porcelain from 1710, breaking the Chinese monopoly.", "spec": {"Factory": "Meissen", "From": "1710", "First": "European hard-paste porcelain", "Mark": "Crossed swords"}, "ref": "Meissen factory history, 1710."}, {"t": "Chippendale Secretary Desk", "mk": "Thomas Chippendale style", "yr": "1760", "cat": "furniture", "blurb": "The 1754 \"Director\" pattern book defined English Rococo furniture; originals are museum pieces.", "spec": {"Style": "Chippendale, English Rococo", "Pattern book": "The Director, 1754", "Form": "Secretary desk", "Wood": "Mahogany"}, "ref": "Chippendale Director, 1754."}, {"t": "Tiffany Studios Leaded Glass Lamp", "mk": "Tiffany Studios", "yr": "1899", "cat": "lighting", "blurb": "Louis Comfort Tiffany's leaded Favrile glass shades, made from 1899, are icons of Art Nouveau.", "spec": {"Maker": "Tiffany Studios", "From": "1899", "Glass": "Favrile leaded", "Style": "Art Nouveau"}, "ref": "Tiffany Studios production history."}, {"t": "Rene Lalique Glass Vase", "mk": "Rene Lalique", "yr": "1900", "cat": "glassware", "blurb": "Lalique's molded glass of the Art Nouveau and Deco eras elevated glass to fine art.", "spec": {"Maker": "Rene Lalique", "Era": "Art Nouveau/Deco", "Medium": "Molded glass", "Note": "Signed pieces"}, "ref": "Lalique archives."}, {"t": "Galle Cameo Glass Vase", "mk": "Emile Galle", "yr": "1900", "cat": "glassware", "blurb": "Emile Galle's Nancy cameo glass with botanical motifs, the soul of French Art Nouveau.", "spec": {"Maker": "Emile Galle, Nancy", "Era": "c. 1900", "Technique": "Cameo-carved", "Motif": "Botanical"}, "ref": "Galle glass scholarship."}, {"t": "Paul Storr Georgian Silver", "mk": "Paul Storr", "yr": "1800", "cat": "silver", "blurb": "Paul Storr, the great Regency silversmith, made monumental silver for royalty and the wealthy.", "spec": {"Maker": "Paul Storr", "Era": "Regency, c. 1800", "Mark": "Storr lion marks", "Note": "Royal commissions"}, "ref": "British silver references."}, {"t": "Wedgwood Jasperware", "mk": "Wedgwood", "yr": "1775", "cat": "ceramics", "blurb": "Josiah Wedgwood's blue jasperware with white reliefs, perfected in the 1770s, is still made today.", "spec": {"Maker": "Wedgwood", "Perfected": "1770s", "Ware": "Jasperware", "Relief": "White on blue"}, "ref": "Wedgwood factory history."}, {"t": "Stickley Arts and Crafts Chair", "mk": "Gustav Stickley", "yr": "1900", "cat": "furniture", "blurb": "Gustav Stickley's quarter-sawn oak furniture defined the American Arts and Crafts movement.", "spec": {"Maker": "Gustav Stickley", "Era": "c. 1900", "Wood": "Quarter-sawn oak", "Movement": "Arts and Crafts"}, "ref": "Stickley/Craftsman history."}, {"t": "Shaker Sewing Desk", "mk": "Shaker communities", "yr": "1850", "cat": "furniture", "blurb": "Shaker furniture's honest joinery and utility, made communally in the 19th century.", "spec": {"Maker": "Shaker communities", "Era": "19th century", "Ethos": "Utility, honesty", "Joinery": "Hand-cut"}, "ref": "Shaker furniture scholarship."}, {"t": "Persian Tabriz Carpet", "mk": "Tabriz workshops", "yr": "1880", "cat": "rugs", "blurb": "Tabriz carpets with their medallion designs are the aristocrats of Persian weaving.", "spec": {"Origin": "Tabriz, Persia", "Era": "Late 19th century", "Design": "Medallion", "Knot": "Fine Persian weave"}, "ref": "Persian carpet scholarship."}, {"t": "Sevres Porcelain Vase", "mk": "Manufacture de Sevres", "yr": "1780", "cat": "ceramics", "blurb": "The French royal manufactory's ground-color vases set the standard for 18th-century porcelain.", "spec": {"Factory": "Sevres", "Era": "18th century", "Ground": "Bleu celeste, rose", "Patron": "French crown"}, "ref": "Sevres manufactory history."}, {"t": "Windsor Chair", "mk": "English/American makers", "yr": "1750", "cat": "furniture", "blurb": "The spindled Windsor chair, perfected in the 18th century on both sides of the Atlantic.", "spec": {"Form": "Spindle-back chair", "Era": "18th century", "Wood": "Mixed hardwoods", "Origin": "England/America"}, "ref": "Furniture history references."}, {"t": "Seth Thomas Regulator Clock", "mk": "Seth Thomas", "yr": "1860", "cat": "clocks", "blurb": "Seth Thomas's weight-driven regulators were the timekeepers of American railroads and offices.", "spec": {"Maker": "Seth Thomas", "Era": "Mid-19th century", "Type": "Weight-driven regulator", "Use": "Railroad standard"}, "ref": "Seth Thomas clock history."}, {"t": "Steiff Teddy Bear", "mk": "Steiff", "yr": "1902", "cat": "bronzes", "blurb": "Margarete Steiff's 1902 jointed bear with the button in ear, the original teddy bear.", "spec": {"Maker": "Steiff, Germany", "Year": "1902", "Mark": "Button in ear", "Note": "Original teddy bear"}, "ref": "Steiff company history."}, {"t": "Rookwood Art Pottery Vase", "mk": "Rookwood", "yr": "1900", "cat": "ceramics", "blurb": "Cincinnati's Rookwood Pottery led American art pottery around 1900 with jewel-like glazes.", "spec": {"Maker": "Rookwood, Cincinnati", "Era": "c. 1900", "Glaze": "Jewel-tone art glazes", "Note": "American art pottery"}, "ref": "Rookwood Pottery history."}, {"t": "Waterford Cut Crystal", "mk": "Waterford", "yr": "1783", "cat": "glassware", "blurb": "Waterford's flint glass cutting tradition dates to 1783 in Ireland.", "spec": {"Maker": "Waterford", "From": "1783", "Glass": "Cut flint crystal", "Origin": "Ireland"}, "ref": "Waterford company history."}];
var NOTE_SIG='This is a Signature version in the Signature system: an original creation of the JAH Databases, property of Justin Addam Higgins (JAH).';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(rnd,a){return a[Math.floor(rnd()*a.length)%a.length];}
function pad7(n){return String(n).padStart(7,'0');}
function fmt2(s,a,b){var i=0;return s.replace(/%s/g,function(){return (i++===0)?a:b;});}
function sigRecord(seed,rnd){
  var rid=PREFIX+pad7(seed+1);
  var g=pick(rnd,CATEGORIES);
  var maker=pick(rnd,MAKERS), line=pick(rnd,LINES), desc=pick(rnd,DESCS);
  var num=1+Math.floor(rnd()*899);
  var title=maker+' '+line+' '+desc+' '+num;
  var w1=pick(rnd,WORDS), w2=pick(rnd,WORDS), w3=pick(rnd,WORDS);
  var facts={}, i;
  for(i=0;i<SPEC_KEYS.length;i++){facts[SPEC_KEYS[i]]=pick(rnd,SPEC_VALS[i]);}
  return {
    id:rid, t:title, c:Math.floor(seed/100)+1, g:g,
    title:title, kind:KIND, category:g, maker:maker, series:line,
    description:'A Signature '+KIND+' from '+maker+', in the '+line+' series: '+w1+', finished with '+w2+'.',
    overview:'The '+title+' is an original '+KIND+' created in the Signature system under '+AI+'. It carries '+w1+' and '+w3+', and every example is documented with full provenance in this database. As a Signature version, it is an original work \u2014 never a copy of another maker\u2019s piece \u2014 and it is built to the same full-file standard as every record in the archive.',
    spotlight:'Collectors value the '+line+' for its '+w2+' and the '+line+' series\u2019 reputation for '+w3+'. Each record in this database holds the complete file for its '+KIND+': full description, specifications, and Signature lineage, readable as plain sentences and paragraphs.',
    facts:facts,
    source:'signature',
    source_ref:'Generated by '+AI+' \u2014 Signature version in the Signature system.',
    signature_version:true,
    signature_note:NOTE_SIG
  };
}
function factRecord(seed,rnd){
  var rid=PREFIX+pad7(seed+1);
  var fi=Math.floor(seed/5), f=FACTS[fi%FACTS.length];
  var angle=Math.floor(fi/FACTS.length)%3;
  var open=fmt2(pick(rnd,OPENERS),rid,KIND);
  var overview, spotlight;
  if(angle===0){
    overview=open+' '+f.blurb+' Made by '+f.mk+' in '+f.yr+', it stands as a reference point collectors return to again and again.';
    spotlight='Its place in history is secure: students of '+KIND+' study this piece the way scholars study landmark texts. The facts table below carries the verified particulars.';
  }else if(angle===1){
    overview=open+' '+f.blurb+' On the market it is a blue-chip holding \u2014 the kind of piece that anchors serious collections and headlines landmark sales.';
    spotlight='For the collector, condition and provenance decide everything with a piece like this. Documented examples with clean history command the strongest results, and this database keeps the full file so the facts travel with the '+KIND+'.';
  }else{
    overview=open+' '+f.blurb+' The technical particulars below are the verified reference collectors check first.';
    spotlight='Every detail in the facts table is drawn from published references and maker records. Where this database also holds a Signature version of the same idea, the counterpart link below connects the fact-checked original to its Signature companion.';
  }
  var cs=((seed+1)%5!==0)?seed+1:seed+2;
  return {
    id:rid, t:f.t, c:Math.floor(seed/100)+1, g:f.cat,
    title:f.t, kind:KIND, category:f.cat, maker:f.mk, year:f.yr,
    description:f.blurb, overview:overview, spotlight:spotlight,
    facts:f.spec,
    source:'fact-checked',
    source_ref:f.ref,
    signature_counterpart:PREFIX+pad7(cs+1),
    signature_version:true,
    signature_note:'Fact-checked real-world record. This database is a Signature version in the Signature system; the Signature counterpart linked above is the Signature-system companion to this verified item.'
  };
}
function generate(seed,opts,rnd){
  seed=(typeof seed==='number')?seed:0;
  rnd=rnd||prng(seed);
  var rec=(seed%5===0)?factRecord(seed,rnd):sigRecord(seed,rnd);
  if(opts&&opts.category&&CATEGORIES.indexOf(opts.category)>=0){rec.g=opts.category;rec.category=opts.category;}
  return rec;
}
function validate(rec){
  var errs=[];
  if(!rec||typeof rec!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{7}$').test(String(rec.id)))errs.push('bad id');
  ['t','title','description','overview','spotlight','facts','source','signature_version','g','c'].forEach(function(k){
    if(rec[k]===null||rec[k]===undefined||rec[k]==='')errs.push('missing '+k);
  });
  if(CATEGORIES.indexOf(rec.g)<0)errs.push('bad category');
  if(rec.source!=='fact-checked'&&rec.source!=='signature')errs.push('bad source');
  if(rec.signature_version!==true)errs.push('not marked signature_version');
  if(String(rec.overview||'').length+String(rec.spotlight||'').length<150)errs.push('narrative too short');
  if(JSON.stringify(rec).indexOf('word-break')>=0)errs.push('forbidden word-break');
  if(rec.source==='fact-checked'&&!rec.source_ref)errs.push('fact-checked without source_ref');
  return{ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s.id===rec.id)errs.push('duplicate id '+rec.id);
    else if(s.t===rec.t)errs.push('duplicate title '+rec.t);
  });
  return{ok:errs.length===0,errors:errs};
}
var gen={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'){module.exports=gen;module.exports.SLUG=SLUG;module.exports.PREFIX=PREFIX;module.exports.CATEGORIES=CATEGORIES;}
/* ---------------- 40/40 self-test harness (node) ---------------- */
if(typeof require!=='undefined'&&typeof process!=='undefined'&&require.main===module){runSelfTest();}
function runSelfTest(){
  var pass=0,fail=0;
  function t(name,cond){if(cond){pass++;}else{fail++;console.log('FAIL: '+name);}}
  var seeds=[0,1,7,42,999,2500,123456,999999];
  var i,s;
  for(i=0;i<8;i++){s=seeds[i];t('determinism seed '+s,JSON.stringify(generate(s,{}))===JSON.stringify(generate(s,{})));}
  var vseeds=[0,1,2,3,6,11,42];
  for(i=0;i<7;i++){s=vseeds[i];t('validate seed '+s,validate(generate(s,{})).ok);}
  t('validate rejects empty',!validate({}).ok);
  t('validate rejects bad source',!validate((function(){var r=generate(1,{});r.source='bogus';return r;})()).ok);
  var idre=new RegExp('^'+PREFIX+'\\d{7}$');
  var fseeds=[0,1,7,999];
  for(i=0;i<4;i++){s=fseeds[i];t('id format seed '+s,idre.test(generate(s,{}).id));}
  t('id seed 0 -> 0000001',generate(0,{}).id===PREFIX+'0000001');
  t('id seed 999999 -> 1000000',generate(999999,{}).id===PREFIX+'1000000');
  var seen={},dup=false;
  for(i=0;i<8;i++){s=seeds[i];var id=generate(s,{}).id;if(seen[id])dup=true;seen[id]=1;}
  t('ids unique across 8 seeds',!dup);
  t('id derives from seed',generate(424242,{}).id===PREFIX+'0424243');
  t('id zero-padded 7',generate(5,{}).id.length===PREFIX.length+7);
  var cseeds=[0,1,7,42,999];
  for(i=0;i<5;i++){s=cseeds[i];t('category valid seed '+s,CATEGORIES.indexOf(generate(s,{}).g)>=0);}
  var r0=generate(0,{}),r1=generate(1,{});
  t('field title present',!!r1.title);
  t('field source present',!!r1.source);
  t('narrative >150 chars',String(r1.overview).length+String(r1.spotlight).length>150);
  t('signature_version true',r1.signature_version===true);
  t('fact seed has source_ref',!!r0.source_ref);
  t('fact seed has counterpart',!!r0.signature_counterpart);
  t('sig seed source=signature',r1.source==='signature');
  t('no word-break in record',JSON.stringify(generate(12345,{})).indexOf('word-break')<0);
  t('driftCheck clean',driftCheck(r1,[{id:'X',t:'Y'}]).ok);
  console.log('SELFTEST '+SLUG+': '+pass+'/40 passed'+(fail?' ('+fail+' FAILED)':''));
  process.exitCode=fail?1:0;
}
})();
