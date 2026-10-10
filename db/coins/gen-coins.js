/* ✳ SIGNATURE — JAH Coin Collecting Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-COIN-0000001 .. JAH-COIN-1000000). Browser: registers with JAHDB. Node:
   run `node gen-coins.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='coins', PREFIX='JAH-COIN-', VERSION='jahdb-coins-1.0';
var KIND='coin', AI='JAH Coin Creator';
var CATEGORIES=["ancient", "medieval", "us-classic", "world", "gold", "silver", "commemorative", "error"];
var MAKERS=["Signature Mint", "JAH Mint Works", "Meridian Mint", "Aurelian Mint Co.", "Sovereign Mint", "Heritage Mint Atelier", "Continental Mint", "Paramount Mint", "Golden State Mint", "Liberty Mint Works", "Copperline Mint", "Regent Mint"], LINES=["Heritage Strike", "Sovereign Issue", "Liberty Series", "Founder Edition", "Centennial Strike", "Eagle Series", "Pioneer Issue", "Meridian Proof", "Golden Age", "Origin Strike"], WORDS=["a deep mirror proof finish", "hand-engraved dies", "a reeded edge", "a limited mintage run", "a cameo contrast finish", "an antique patina", "a high-relief strike", "a numbered certificate"], DESCS=["Medallion", "Proof Strike", "Commemorative", "Pattern", "Restrike", "Piedfort", "Token", "Ingot Round", "Presentation Piece", "Trial Strike", "Collector Coin", "Miniature"];
var SPEC_KEYS=["Denomination", "Metal", "Weight", "Diameter", "Mint", "Finish"], SPEC_VALS=[["1 oz medallion", "half-dollar size", "dollar size", "quarter size"], [".999 fine silver", ".9999 fine gold", "copper-nickel", "bronze"], ["31.1 g", "15.5 g", "26.7 g", "5.67 g"], ["40.6 mm", "32.7 mm", "38.1 mm", "24.3 mm"], ["Signature Mint", "Meridian Mint", "Sovereign Mint", "Heritage Mint"], ["proof", "uncirculated", "antique", "brilliant uncirculated"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "1794 Flowing Hair Silver Dollar", "mk": "US Mint", "yr": "1794", "cat": "us-classic", "blurb": "The first silver dollar struck by the United States; the finest known sold for $10 million in 2013.", "spec": {"Denomination": "$1", "Minted": "1794, Philadelphia", "Designer": "Robert Scot", "Record": "$10M, 2013"}, "ref": "Stack's Bowers sale record, January 2013."}, {"t": "1933 Double Eagle", "mk": "US Mint", "yr": "1933", "cat": "us-classic", "blurb": "The legendary $20 gold piece never officially released; one sold for $18.9 million in 2021, the most expensive coin ever sold.", "spec": {"Denomination": "$20 gold", "Minted": "1933 (recalled)", "Status": "Never officially issued", "Record": "$18.9M, Sotheby's 2021"}, "ref": "Sotheby's sale record, June 2021."}, {"t": "1804 Draped Bust Silver Dollar", "mk": "US Mint", "yr": "1834", "cat": "us-classic", "blurb": "Struck in the 1830s as diplomatic gifts and dated 1804; the \"King of American Coins\" brought $7.68 million in 2021.", "spec": {"Denomination": "$1", "Struck": "1830s, dated 1804", "Known": "15 examples", "Sale": "$7.68M, 2021"}, "ref": "Stack's Bowers sale record, March 2021."}, {"t": "1913 Liberty Head Nickel", "mk": "US Mint", "yr": "1913", "cat": "us-classic", "blurb": "Five struck clandestinely at Philadelphia; the Eliasberg specimen brought $4.56 million.", "spec": {"Denomination": "5c", "Minted": "1913 (unauthorized)", "Known": "5 examples", "Sale": "$4.56M"}, "ref": "Heritage/Stack's Bowers sale history."}, {"t": "1909-S VDB Lincoln Cent", "mk": "US Mint", "yr": "1909", "cat": "us-classic", "blurb": "The first-year Lincoln cent with Victor Brenner's initials; only 484,000 struck at San Francisco.", "spec": {"Denomination": "1c", "Mintage": "484,000", "Mint": "San Francisco", "Designer": "Victor D. Brenner"}, "ref": "US Mint mintage records, 1909."}, {"t": "1916-D Mercury Dime", "mk": "US Mint", "yr": "1916", "cat": "us-classic", "blurb": "The key date of the Mercury dime series with a mintage of just 264,000.", "spec": {"Denomination": "10c", "Mintage": "264,000", "Mint": "Denver", "Designer": "Adolph Weinman"}, "ref": "US Mint mintage records, 1916."}, {"t": "1943 Copper Cent", "mk": "US Mint", "yr": "1943", "cat": "error", "blurb": "A handful struck on copper planchets during the steel-cent year; among the most famous US errors.", "spec": {"Denomination": "1c", "Year": "1943 (steel year)", "Error": "Struck on copper planchet", "Rarity": "Fewer than 20 known"}, "ref": "US Mint error coin studies."}, {"t": "1955 Doubled Die Lincoln Cent", "mk": "US Mint", "yr": "1955", "cat": "error", "blurb": "The dramatic doubled-die obverse visible to the naked eye, the most famous US die variety.", "spec": {"Denomination": "1c", "Variety": "Doubled die obverse", "Visibility": "Naked-eye doubling", "Mint": "Philadelphia"}, "ref": "US Mint variety references."}, {"t": "1907 Saint-Gaudens Double Eagle", "mk": "US Mint", "yr": "1907", "cat": "gold", "blurb": "Augustus Saint-Gaudens' high-relief masterpiece, called the most beautiful US coin ever made.", "spec": {"Denomination": "$20 gold", "Designer": "Augustus Saint-Gaudens", "Relief": "High relief", "Year": "1907"}, "ref": "US Mint Saint-Gaudens history, 1907."}, {"t": "1787 Brasher Doubloon", "mk": "Ephraim Brasher", "yr": "1787", "cat": "us-classic", "blurb": "America's first gold coin, struck by New York goldsmith Ephraim Brasher; one sold for $9.36 million in 2021.", "spec": {"Denomination": "Gold doubloon", "Maker": "Ephraim Brasher", "Year": "1787", "Sale": "$9.36M, 2021"}, "ref": "Heritage Auctions sale record, January 2021."}, {"t": "1822 Capped Head $5 Gold", "mk": "US Mint", "yr": "1822", "cat": "gold", "blurb": "Only three known, all in museums or the Smithsonian; one sold for $8.4 million in 2021.", "spec": {"Denomination": "$5 gold", "Known": "3 examples", "Year": "1822", "Sale": "$8.4M, 2021"}, "ref": "Stack's Bowers sale record, March 2021."}, {"t": "1793 Flowing Hair Cent", "mk": "US Mint", "yr": "1793", "cat": "us-classic", "blurb": "Among the very first cents struck by the young United States Mint.", "spec": {"Denomination": "1c", "Year": "1793", "Mint": "Philadelphia", "Note": "First-year US large cent"}, "ref": "US Mint early copper history."}, {"t": "1877 Indian Head Cent", "mk": "US Mint", "yr": "1877", "cat": "us-classic", "blurb": "The key date of the Indian Head cent series with a mintage of 852,500.", "spec": {"Denomination": "1c", "Mintage": "852,500", "Series": "Indian Head, 1859-1909", "Key date": "Yes"}, "ref": "US Mint mintage records, 1877."}, {"t": "1921 Peace Dollar", "mk": "US Mint", "yr": "1921", "cat": "silver", "blurb": "The high-relief first year of Anthony de Francisci's Peace dollar, a one-year type.", "spec": {"Denomination": "$1 silver", "Designer": "Anthony de Francisci", "Relief": "High relief, 1921 only", "Year": "1921"}, "ref": "US Mint Peace dollar history."}, {"t": "1893-S Morgan Dollar", "mk": "US Mint", "yr": "1893", "cat": "silver", "blurb": "The king of Morgan dollars with a mintage of 100,000, the series key date.", "spec": {"Denomination": "$1 silver", "Mintage": "100,000", "Mint": "San Francisco", "Series": "Morgan, 1878-1921"}, "ref": "US Mint mintage records, 1893."}, {"t": "1916 Standing Liberty Quarter", "mk": "US Mint", "yr": "1916", "cat": "us-classic", "blurb": "The first-year Standing Liberty quarter with Liberty's exposed breast, changed in 1917.", "spec": {"Denomination": "25c", "Year": "1916", "Designer": "Hermon MacNeil", "Note": "Full-breast variety"}, "ref": "US Mint Standing Liberty history."}, {"t": "1932-D Washington Quarter", "mk": "US Mint", "yr": "1932", "cat": "us-classic", "blurb": "The key date of the Washington quarter series, only 436,800 struck at Denver.", "spec": {"Denomination": "25c", "Mintage": "436,800", "Mint": "Denver", "Series": "Washington, 1932-"}, "ref": "US Mint mintage records, 1932."}, {"t": "1787 Fugio Cent", "mk": "US Mint (contract)", "yr": "1787", "cat": "us-classic", "blurb": "The first coin officially circulated by the United States, with Franklin's \"Mind Your Business\" motto.", "spec": {"Denomination": "1c", "Year": "1787", "Motto": "Mind Your Business", "Note": "First US-circulated coin"}, "ref": "US early coinage history."}, {"t": "1864 Two-Cent Piece", "mk": "US Mint", "yr": "1864", "cat": "us-classic", "blurb": "The first US coin to bear \"In God We Trust\", issued during the Civil War.", "spec": {"Denomination": "2c", "Year": "1864", "First": "\"In God We Trust\"", "Era": "Civil War"}, "ref": "US Mint motto history."}, {"t": "1856 Flying Eagle Cent", "mk": "US Mint", "yr": "1856", "cat": "us-classic", "blurb": "The pattern small cent that previewed the end of the large cent era.", "spec": {"Denomination": "1c pattern", "Year": "1856", "Note": "Small-cent prototype", "Rarity": "Pattern issue"}, "ref": "US Mint pattern history."}, {"t": "1933 British Penny", "mk": "Royal Mint", "yr": "1933", "cat": "world", "blurb": "Only six or seven struck for foundation deposits; one of Britain's rarest coins.", "spec": {"Denomination": "1d", "Year": "1933", "Known": "6-7 examples", "Note": "Never circulated"}, "ref": "Royal Mint records; Spink references."}, {"t": "1967 South African Krugerrand", "mk": "SA Mint", "yr": "1967", "cat": "gold", "blurb": "The world's first modern gold bullion coin, launched in 1967 and still the benchmark.", "spec": {"Weight": "1 oz gold", "Launched": "1967", "First": "Modern bullion coin", "Origin": "South Africa"}, "ref": "South African Mint history."}, {"t": "1986 American Gold Eagle", "mk": "US Mint", "yr": "1986", "cat": "gold", "blurb": "America's official gold bullion coin, launched under the Gold Bullion Coin Act of 1985.", "spec": {"Weight": "1 oz gold", "Launched": "1986", "Backing": "US legal tender", "Design": "Saint-Gaudens obverse"}, "ref": "US Mint Gold Eagle history."}, {"t": "1982 Chinese Gold Panda", "mk": "China Mint", "yr": "1982", "cat": "world", "blurb": "China's beloved bullion series with a changing panda design every year since 1982.", "spec": {"Weight": "1 oz gold", "Launched": "1982", "Design": "New panda yearly", "Origin": "China"}, "ref": "China Gold Coin Corporation history."}];
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
