/* ✳ SIGNATURE — JAH Auction Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-AUC-0000001 .. JAH-AUC-1000000). Browser: registers with JAHDB. Node:
   run `node gen-auction.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='auction', PREFIX='JAH-AUC-', VERSION='jahdb-auction-1.0';
var KIND='auction lot', AI='JAH Auction Creator';
var CATEGORIES=["art", "jewelry", "wine", "watches", "cars", "manuscripts", "memorabilia", "estates"];
var MAKERS=["Signature Auction House", "JAH Auctioneers", "Meridian Auctions", "Heritage Auction Gallery", "Apex Auction House", "Continental Auctions", "Paramount Auctioneers", "Golden Gavel Auctions", "Vantage Auction House", "Legacy Auction Gallery", "Copperline Auctions", "Regent Auctioneers"], LINES=["Evening Sale", "Masterpiece Auction", "Heritage Sale", "Curated Session", "Premier Auction", "Collector Sale", "Signature Session", "Centennial Auction", "Gala Sale", "Origin Sale"], WORDS=["a documented provenance chain", "a museum exhibition history", "a signed certificate of authenticity", "a pre-sale estimate range", "a heated multi-bidder contest", "a world-record result", "a single-owner consignment", "a fully illustrated catalog entry"], DESCS=["Evening Lot", "Single-Owner Lot", "Estate Lot", "Curated Lot", "Masterpiece Lot", "Premier Lot", "Heritage Lot", "Gala Lot", "Spotlight Lot", "Collector Lot", "Signature Lot", "Centennial Lot"];
var SPEC_KEYS=["Sale", "Estimate", "Result", "Provenance", "Condition", "Catalog"], SPEC_VALS=[["Evening Sale", "Heritage Sale", "Premier Auction", "Curated Session"], ["$50,000-80,000", "$100,000-150,000", "$200,000-300,000", "$500,000-700,000"], ["sold above estimate", "sold within estimate", "new world record", "sold to a private collector"], ["single owner", "estate consignment", "documented since creation", "gallery provenance"], ["excellent", "museum quality", "very good", "conserved"], ["fully illustrated", "catalogue raisonne listed", "exhibition cataloged", "archived"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Salvator Mundi — Leonardo da Vinci", "mk": "Christie's New York", "yr": "2017", "cat": "art", "blurb": "Sold for $450.3 million in November 2017, the most expensive artwork ever sold at auction.", "spec": {"Work": "Salvator Mundi", "Attributed": "Leonardo da Vinci", "Sale": "Christie's, Nov 2017", "Price": "$450.3M, world record"}, "ref": "Christie's sale record, 15 November 2017."}, {"t": "Les Femmes d'Alger (Version O) — Picasso", "mk": "Christie's New York", "yr": "2015", "cat": "art", "blurb": "Picasso's 1955 canvas sold for $179.4 million in May 2015, then the auction record.", "spec": {"Work": "Les Femmes d'Alger (Version O)", "Artist": "Pablo Picasso", "Sale": "Christie's, May 2015", "Price": "$179.4M"}, "ref": "Christie's sale record, 11 May 2015."}, {"t": "Three Studies of Lucian Freud — Francis Bacon", "mk": "Christie's New York", "yr": "2013", "cat": "art", "blurb": "Bacon's 1969 triptych sold for $142.4 million in 2013, then the record for a living-era work.", "spec": {"Work": "Three Studies of Lucian Freud", "Artist": "Francis Bacon", "Sale": "Christie's, Nov 2013", "Price": "$142.4M"}, "ref": "Christie's sale record, 12 November 2013."}, {"t": "The Scream — Edvard Munch", "mk": "Sotheby's New York", "yr": "2012", "cat": "art", "blurb": "The 1895 pastel version sold for $119.9 million in 2012, then the auction record.", "spec": {"Work": "The Scream (pastel, 1895)", "Artist": "Edvard Munch", "Sale": "Sotheby's, May 2012", "Price": "$119.9M"}, "ref": "Sotheby's sale record, 2 May 2012."}, {"t": "1955 Mercedes-Benz 300 SLR Uhlenhaut Coupe", "mk": "RM Sotheby's", "yr": "2022", "cat": "cars", "blurb": "Sold for $143 million in May 2022, the most expensive car ever sold at auction.", "spec": {"Car": "300 SLR Uhlenhaut Coupe", "Year": "1955", "Sale": "RM Sotheby's, May 2022", "Price": "$143M, world record"}, "ref": "RM Sotheby's sale record, 19 May 2022."}, {"t": "1962 Ferrari 250 GTO", "mk": "RM Sotheby's Monterey", "yr": "2018", "cat": "cars", "blurb": "Sold for $48.4 million in August 2018, then the most expensive car ever auctioned.", "spec": {"Car": "1962 Ferrari 250 GTO", "Sale": "Monterey, Aug 2018", "Price": "$48.4M", "Rarity": "One of 36"}, "ref": "RM Sotheby's Monterey sale, August 2018."}, {"t": "Pink Star Diamond (59.60 ct)", "mk": "Sotheby's Hong Kong", "yr": "2017", "cat": "jewelry", "blurb": "The 59.60-carat oval pink diamond sold for $71.2 million in 2017, the auction record for any jewel.", "spec": {"Stone": "59.60 ct oval pink", "Sale": "Sotheby's Hong Kong, Apr 2017", "Price": "$71.2M, jewel record", "Type": "Fancy vivid pink"}, "ref": "Sotheby's sale record, 4 April 2017."}, {"t": "Oppenheimer Blue Diamond (14.62 ct)", "mk": "Christie's Geneva", "yr": "2016", "cat": "jewelry", "blurb": "The 14.62-carat vivid blue diamond sold for $57.5 million in 2016.", "spec": {"Stone": "14.62 ct vivid blue", "Sale": "Christie's Geneva, May 2016", "Price": "$57.5M", "Name": "Oppenheimer Blue"}, "ref": "Christie's sale record, 18 May 2016."}, {"t": "Patek Philippe Grandmaster Chime 6300A", "mk": "Christie's Geneva", "yr": "2019", "cat": "watches", "blurb": "The steel-only Grandmaster Chime made for Only Watch 2019 sold for $31 million, the record for any wristwatch.", "spec": {"Watch": "Grandmaster Chime 6300A", "Sale": "Only Watch, Nov 2019", "Price": "$31M, watch record", "Unique": "Steel, one of one"}, "ref": "Christie's Only Watch sale, 9 November 2019."}, {"t": "Rolex Daytona \"Paul Newman\" 6239", "mk": "Phillips New York", "yr": "2017", "cat": "watches", "blurb": "Paul Newman's own exotic-dial Daytona sold for $17.8 million in 2017.", "spec": {"Watch": "Daytona 6239, exotic dial", "Owner": "Paul Newman", "Sale": "Phillips, Oct 2017", "Price": "$17.8M"}, "ref": "Phillips New York sale, 26 October 2017."}, {"t": "Macallan 1926 (60 Year Old)", "mk": "Sotheby's London", "yr": "2023", "cat": "wine", "blurb": "A bottle of the 1926 Macallan sold for $2.7 million in 2023, the record for any bottle of spirits or wine.", "spec": {"Bottle": "Macallan 1926, 60 YO", "Sale": "Sotheby's London, Nov 2023", "Price": "$2.7M, bottle record", "Casks": "60 years"}, "ref": "Sotheby's sale record, 18 November 2023."}, {"t": "1945 Romanee-Conti", "mk": "Sotheby's New York", "yr": "2018", "cat": "wine", "blurb": "A single bottle of 1945 Romanee-Conti sold for $558,000 in 2018, then the wine record.", "spec": {"Wine": "1945 Romanee-Conti", "Sale": "Sotheby's NY, Oct 2018", "Price": "$558,000 per bottle", "Vintage": "1945"}, "ref": "Sotheby's sale record, 13 October 2018."}, {"t": "Codex Leicester — Leonardo da Vinci", "mk": "Christie's New York", "yr": "1994", "cat": "manuscripts", "blurb": "Bill Gates bought Leonardo's 72-page scientific manuscript for $30.8 million in 1994.", "spec": {"Work": "Codex Leicester", "Author": "Leonardo da Vinci", "Buyer": "Bill Gates, 1994", "Price": "$30.8M"}, "ref": "Christie's sale record, 11 November 1994."}, {"t": "Bay Psalm Book (1640)", "mk": "Sotheby's New York", "yr": "2013", "cat": "manuscripts", "blurb": "The first book printed in America sold for $14.2 million in 2013, the record for a printed book.", "spec": {"Book": "Bay Psalm Book, 1640", "Note": "First book printed in America", "Sale": "Sotheby's, Nov 2013", "Price": "$14.2M"}, "ref": "Sotheby's sale record, 26 November 2013."}, {"t": "Apollo 11 Lunar Sample Bag", "mk": "Sotheby's New York", "yr": "2017", "cat": "memorabilia", "blurb": "The bag that held the first lunar samples sold for $1.8 million in 2017.", "spec": {"Item": "Lunar sample bag", "Mission": "Apollo 11, 1969", "Sale": "Sotheby's, Jul 2017", "Price": "$1.8M"}, "ref": "Sotheby's sale record, 20 July 2017."}, {"t": "Steve McQueen Heuer Monaco 1133B", "mk": "Phillips New York", "yr": "2020", "cat": "memorabilia", "blurb": "McQueen's Le Mans-worn Heuer Monaco sold for $2.2 million in 2020.", "spec": {"Watch": "Heuer Monaco 1133B", "Worn by": "Steve McQueen, Le Mans", "Sale": "Phillips, Dec 2020", "Price": "$2.2M"}, "ref": "Phillips New York sale, 12 December 2020."}, {"t": "Action Comics #1 (1938)", "mk": "Heritage Auctions", "yr": "2024", "cat": "memorabilia", "blurb": "A high-grade copy of the first Superman appearance sold for $6 million in 2024, the comics record.", "spec": {"Issue": "Action Comics #1, 1938", "Debut": "Superman", "Sale": "Heritage, Apr 2024", "Price": "$6M, comics record"}, "ref": "Heritage Auctions sale record, April 2024."}, {"t": "1952 Topps Mickey Mantle (PSA 9)", "mk": "Heritage Auctions", "yr": "2022", "cat": "memorabilia", "blurb": "The $12.6 million August 2022 sale set the record for any sports card.", "spec": {"Card": "1952 Topps Mantle #311", "Grade": "PSA 9", "Sale": "Heritage, Aug 2022", "Price": "$12.6M, card record"}, "ref": "Heritage Auctions sale record, August 2022."}];
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
