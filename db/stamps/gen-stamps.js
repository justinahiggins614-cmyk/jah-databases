/* ✳ SIGNATURE — JAH Stamp Collecting Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-STAMP-0000001 .. JAH-STAMP-1000000). Browser: registers with JAHDB. Node:
   run `node gen-stamps.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='stamps', PREFIX='JAH-STAMP-', VERSION='jahdb-stamps-1.0';
var KIND='postage stamp', AI='JAH Stamp Creator';
var CATEGORIES=["us-classic", "british", "europe", "asia", "airmail", "commemorative", "first-day", "errors"];
var MAKERS=["Signature Post", "JAH Philatelic Bureau", "Meridian Post", "Heritage Stamp Works", "Aurelian Post", "Continental Philately", "Paramount Post", "Golden Gate Philatelics", "Liberty Stamp Co.", "Regent Post", "Copperline Philately", "Sovereign Post"], LINES=["Heritage Definitive", "Commemorative Issue", "Airmail Series", "Pioneer Post", "Centennial Issue", "Landmark Series", "Expedition Set", "Founder Issue", "Golden Age", "Origin Issue"], WORDS=["an engraved intaglio print", "a perforated souvenir sheet", "a first-day-of-issue cancel", "a full original-gum sheet", "a limited commemorative run", "a color-shift error variety", "a silk-paper printing", "a hand-cancelled cover"], DESCS=["Definitive", "Commemorative", "Airmail", "Souvenir Sheet", "Booklet", "Coil", "Miniature Sheet", "First Day Cover", "Plate Block", "Se-tenant", "Proof", "Gutter Pair"];
var SPEC_KEYS=["Denomination", "Issue year", "Printing", "Perforation", "Paper", "Format"], SPEC_VALS=[["5 cents", "10 cents", "25 cents", "1 dollar"], ["2024", "2025", "2026", "2023"], ["engraved", "lithographed", "photogravure", "embossed"], ["perf 11", "perf 12", "imperforate", "perf 10.5"], ["wove paper", "silk paper", "chalky paper", "self-adhesive"], ["single", "sheet of 20", "souvenir sheet", "booklet pane"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Penny Black", "mk": "Great Britain", "yr": "1840", "cat": "british", "blurb": "The world's first adhesive postage stamp, issued 1 May 1840 after Rowland Hill's postal reforms.", "spec": {"Country": "Great Britain", "Issued": "1 May 1840", "Reformer": "Rowland Hill", "Note": "World's first adhesive stamp"}, "ref": "British Postal Museum archives, 1840."}, {"t": "Two Penny Blue", "mk": "Great Britain", "yr": "1840", "cat": "british", "blurb": "The Penny Black's two-pence companion, issued days later in May 1840.", "spec": {"Country": "Great Britain", "Issued": "May 1840", "Value": "2d", "Note": "Companion to Penny Black"}, "ref": "British Postal Museum archives, 1840."}, {"t": "British Guiana One-Cent Magenta", "mk": "British Guiana", "yr": "1856", "cat": "british", "blurb": "The world's most famous and valuable stamp; the sole survivor sold for $9.48 million in 2021.", "spec": {"Country": "British Guiana", "Year": "1856", "Known": "1 example", "Record": "$9.48M, Sotheby's 2021"}, "ref": "Sotheby's sale record, June 2021."}, {"t": "Treskilling Yellow", "mk": "Sweden", "yr": "1855", "cat": "europe", "blurb": "The Swedish three-skilling stamp misprinted in yellow instead of green; sold for $2.3 million in 2010.", "spec": {"Country": "Sweden", "Year": "1855", "Error": "Color error", "Record": "$2.3M, 2010"}, "ref": "David Feldman sale record, May 2010."}, {"t": "Mauritius \"Post Office\" Issue", "mk": "Mauritius", "yr": "1847", "cat": "british", "blurb": "The legendary 1847 \"Post Office\" one-penny and two-pence, among philately's greatest rarities.", "spec": {"Country": "Mauritius", "Year": "1847", "Inscription": "Post Office", "Rarity": "Fewer than 30 known"}, "ref": "Mauritius postal history, 1847."}, {"t": "Inverted Jenny", "mk": "United States", "yr": "1918", "cat": "errors", "blurb": "The 24-cent Curtiss JN-4 biplane printed upside down; a single sold for $2 million in 2021.", "spec": {"Country": "USA", "Year": "1918", "Error": "Inverted center", "Famous block": "McCoy block of four"}, "ref": "Siegel auction records; Smithsonian holdings."}, {"t": "1847 US First Federal Issue", "mk": "United States", "yr": "1847", "cat": "us-classic", "blurb": "America's first federal stamps: the 5-cent Franklin and 10-cent Washington of 1847.", "spec": {"Country": "USA", "Year": "1847", "Values": "5c Franklin, 10c Washington", "Note": "First US federal issue"}, "ref": "US Postal Service stamp history, 1847."}, {"t": "1869 Pictorial Issue", "mk": "United States", "yr": "1869", "cat": "us-classic", "blurb": "America's first pictorial stamps, showing a locomotive, landing of Columbus, and more.", "spec": {"Country": "USA", "Year": "1869", "First": "US pictorial stamps", "Designs": "Locomotive, Columbus, etc."}, "ref": "US Postal Service stamp history, 1869."}, {"t": "1893 Columbian Exposition Issue", "mk": "United States", "yr": "1893", "cat": "commemorative", "blurb": "The sixteen-stamp 1893 commemorative of Columbus's voyage, America's first commemorative issue.", "spec": {"Country": "USA", "Year": "1893", "Stamps": "16 values to $5", "First": "US commemorative issue"}, "ref": "US Postal Service stamp history, 1893."}, {"t": "1898 Trans-Mississippi Issue", "mk": "United States", "yr": "1898", "cat": "us-classic", "blurb": "The 1898 Omaha exposition issue, prized for its vignettes of Western life.", "spec": {"Country": "USA", "Year": "1898", "Theme": "American West", "Note": "Exposition issue"}, "ref": "US Postal Service stamp history, 1898."}, {"t": "1930 Graf Zeppelin Airmail Set", "mk": "United States", "yr": "1930", "cat": "airmail", "blurb": "The three-stamp 1930 set honoring the Graf Zeppelin's pan-American flight.", "spec": {"Country": "USA", "Year": "1930", "Values": "65c, $1.30, $2.60", "Theme": "Graf Zeppelin flight"}, "ref": "US Postal Service airmail history, 1930."}, {"t": "Hawaiian Missionaries", "mk": "Hawaii", "yr": "1851", "cat": "us-classic", "blurb": "The 1851 Kingdom of Hawaii provisionals, printed on thin pelure paper; among the great Pacific rarities.", "spec": {"Country": "Kingdom of Hawaii", "Year": "1851", "Paper": "Thin pelure", "Rarity": "Great Pacific rarity"}, "ref": "Hawaiian postal history, 1851."}, {"t": "Brazil Bull's Eyes (Olho-de-boi)", "mk": "Brazil", "yr": "1843", "cat": "europe", "blurb": "Brazil's 1843 \"bull's eyes\", the second country in the world to issue adhesive stamps.", "spec": {"Country": "Brazil", "Year": "1843", "Note": "Second stamp-issuing country", "Design": "Numeral in oval"}, "ref": "Brazilian postal history, 1843."}, {"t": "French Ceres 1849", "mk": "France", "yr": "1849", "cat": "europe", "blurb": "France's first stamp, the 1849 Ceres head of the Second Republic.", "spec": {"Country": "France", "Year": "1849", "Design": "Ceres head", "Note": "First French stamp"}, "ref": "French postal history, 1849."}, {"t": "China Red Revenue", "mk": "China", "yr": "1897", "cat": "asia", "blurb": "The 1897 surcharged revenue stamps of Imperial China, among Asia's great rarities.", "spec": {"Country": "Imperial China", "Year": "1897", "Type": "Surcharged revenue", "Rarity": "Asian classic"}, "ref": "Chinese philatelic references, 1897."}, {"t": "\"The Whole Country is Red\"", "mk": "China", "yr": "1968", "cat": "asia", "blurb": "The withdrawn 1968 Cultural Revolution stamp, recalled within half a day of issue.", "spec": {"Country": "China", "Year": "1968", "Status": "Withdrawn same day", "Era": "Cultural Revolution"}, "ref": "Chinese philatelic references, 1968."}, {"t": "Pan-American Inverts", "mk": "United States", "yr": "1901", "cat": "errors", "blurb": "The 1901 Pan-American exposition inverts, America's first famous invert errors.", "spec": {"Country": "USA", "Year": "1901", "Error": "Inverted centers", "Values": "1c, 2c, 4c"}, "ref": "US Postal Service error history, 1901."}, {"t": "First Day Cover — 1840 Penny Black Usage", "mk": "Great Britain", "yr": "1840", "cat": "first-day", "blurb": "Covers bearing the Penny Black from its first days of use are philately's crown jewels.", "spec": {"Country": "Great Britain", "Usage": "May 1840", "Format": "Entire/cover", "Note": "First-day usages"}, "ref": "British Postal Museum usage studies."}];
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
