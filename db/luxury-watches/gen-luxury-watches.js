/* ✳ SIGNATURE — JAH Luxury Watch Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-LW-0000001 .. JAH-LW-1000000). Browser: registers with JAHDB. Node:
   run `node gen-luxury-watches.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='luxury-watches', PREFIX='JAH-LW-', VERSION='jahdb-luxury-watches-1.0';
var KIND='luxury watch', AI='JAH Watch Creator';
var CATEGORIES=["dress", "dive", "pilot", "racing", "field", "luxury-sport", "chronograph", "moonphase"];
var MAKERS=["Meridian Chrono Works", "JAH Time Atelier", "Signature Horology", "Aurelian Watch Co.", "Vantage Timepieces", "Halcyon Horology", "Obsidian Watch Atelier", "Celestine Time Co.", "Regent Chronometry", "Northstar Watch Works", "Ivory Tower Time", "Sovereign Horology"], LINES=["Heritage", "Sovereign", "Meridian", "Voyager", "Regatta", "Eclipse", "Paramount", "Continental", "Apex", "Legacy"], WORDS=["hand-finished bridges", "a column-wheel chronograph", "a silicon escapement", "72-hour power reserve", "a domed sapphire crystal", "hand-applied indices", "a guilloche dial", "a transparent caseback"], DESCS=["Automatic", "Chronometer", "GMT", "Moonphase", "Tourbillon", "Diver", "Pilot", "Dress", "Skeleton", "Worldtimer", "Perpetual", "Regulator"];
var SPEC_KEYS=["Movement", "Case", "Diameter", "Water resistance", "Strap", "Functions"], SPEC_VALS=[["Cal. SIG-101 automatic", "Cal. SIG-202 manual", "Cal. SIG-303 GMT", "Cal. SIG-404 chrono"], ["brushed steel", "18k rose gold", "titanium", "platinum"], ["38 mm", "40 mm", "41 mm", "42 mm"], ["50 m", "100 m", "200 m", "300 m"], ["alligator leather", "steel bracelet", "rubber strap", "woven textile"], ["hours, minutes, seconds", "hours, minutes, small seconds, date", "chronograph, tachymeter", "dual time, day-night"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Rolex Submariner Date 126610LN", "mk": "Rolex", "yr": "2020", "cat": "dive", "blurb": "The 41 mm successor to the 116610LN, powered by the calibre 3235 with a 70-hour power reserve.", "spec": {"Movement": "Calibre 3235, automatic", "Case": "41 mm Oystersteel", "Water resistance": "300 m", "Bezel": "Cerachrom, unidirectional"}, "ref": "Rolex official specifications for the Submariner Date 126610LN."}, {"t": "Omega Speedmaster Moonwatch 310.30.42.50.01.001", "mk": "Omega", "yr": "2021", "cat": "chronograph", "blurb": "The direct descendant of the watch worn on the Moon during Apollo 11 in 1969, now with the Master Chronometer calibre 3861.", "spec": {"Movement": "Calibre 3861, manual", "Case": "42 mm stainless steel", "Heritage": "Worn on the lunar surface, 1969", "Crystal": "Hesalite"}, "ref": "Omega official Speedmaster Moonwatch specifications; NASA flight-qualified history."}, {"t": "Patek Philippe Nautilus 5711/1A-010", "mk": "Patek Philippe", "yr": "2006", "cat": "luxury-sport", "blurb": "The steel Nautilus with blue-black gradient dial, discontinued in 2021 after a fifteen-year run as the most coveted steel sports watch in the world.", "spec": {"Movement": "Calibre 26-330 S C", "Case": "40 mm steel", "Dial": "Blue-black gradient", "Status": "Discontinued 2021"}, "ref": "Patek Philippe Nautilus reference history, 2006-2021."}, {"t": "Audemars Piguet Royal Oak 15510ST", "mk": "Audemars Piguet", "yr": "2022", "cat": "luxury-sport", "blurb": "The current 41 mm Royal Oak automatic, carrying Gerald Genta's 1972 integrated-bracelet design into its sixth decade.", "spec": {"Movement": "Calibre 4302", "Case": "41 mm steel", "Design": "Gerald Genta, 1972", "Dial": "Grande Tapisserie"}, "ref": "Audemars Piguet Royal Oak collection specifications."}, {"t": "Cartier Tank Louis", "mk": "Cartier", "yr": "1917", "cat": "dress", "blurb": "Louis Cartier's 1917 rectangular design, worn by figures from Princess Diana to Andy Warhol, and still in production.", "spec": {"Origin": "Designed 1917", "Case": "Rectangular, gold", "Movement": "Manual manufacture", "Legacy": "Over a century in production"}, "ref": "Cartier Tank history, maison archives."}, {"t": "Jaeger-LeCoultre Reverso Classic", "mk": "Jaeger-LeCoultre", "yr": "1931", "cat": "dress", "blurb": "Born in 1931 for polo players who needed to protect the dial, the swivelling Reverso remains an Art Deco icon.", "spec": {"Origin": "1931, polo players", "Case": "Reversible rectangular", "Movement": "Calibre 822, manual", "Design": "Art Deco"}, "ref": "Jaeger-LeCoultre Reverso history, 1931."}, {"t": "Blancpain Fifty Fathoms", "mk": "Blancpain", "yr": "1953", "cat": "dive", "blurb": "Introduced in 1953 and adopted by French combat divers, it is widely regarded as the first true modern dive watch.", "spec": {"Origin": "1953", "Water resistance": "300 m class", "Bezel": "Unidirectional dive bezel", "Heritage": "French Navy combat divers"}, "ref": "Blancpain Fifty Fathoms history, 1953."}, {"t": "Breitling Navitimer B01", "mk": "Breitling", "yr": "1952", "cat": "pilot", "blurb": "The 1952 pilot's chronograph with its circular slide rule, developed for the Aircraft Owners and Pilots Association.", "spec": {"Origin": "1952, AOPA", "Movement": "In-house B01 chronograph", "Bezel": "Circular slide rule", "Case": "43 mm steel"}, "ref": "Breitling Navitimer history and B01 specifications."}, {"t": "TAG Heuer Carrera", "mk": "TAG Heuer", "yr": "1963", "cat": "racing", "blurb": "Jack Heuer's 1963 design named for the Carrera Panamericana road race, with a clean dial built for legibility at speed.", "spec": {"Origin": "1963, Jack Heuer", "Named for": "Carrera Panamericana", "Case": "42 mm steel", "Style": "Racing chronograph"}, "ref": "TAG Heuer Carrera history, 1963."}, {"t": "Grand Seiko Snowflake SBGA211", "mk": "Grand Seiko", "yr": "2005", "cat": "dress", "blurb": "The Spring Drive classic with a snow-textured dial inspired by the Hotaka mountains, accurate to one second per day.", "spec": {"Movement": "Spring Drive 9R65", "Accuracy": "±1 second per day", "Reserve": "72 hours", "Case": "41 mm titanium"}, "ref": "Grand Seiko SBGA211 official specifications."}, {"t": "Tudor Black Bay 58", "mk": "Tudor", "yr": "2018", "cat": "dive", "blurb": "A 39 mm neo-vintage diver sized like the 1958 original, with the manufacture calibre MT5402.", "spec": {"Movement": "MT5402, 70 h reserve", "Case": "39 mm steel", "Water resistance": "200 m", "Heritage": "1958 Big Crown proportions"}, "ref": "Tudor Black Bay 58 official specifications."}, {"t": "Rolex GMT-Master II 126710BLRO", "mk": "Rolex", "yr": "2018", "cat": "pilot", "blurb": "The red-and-blue \"Pepsi\" GMT on a Jubilee bracelet, with the calibre 3285 and a 70-hour reserve.", "spec": {"Movement": "Calibre 3285", "Case": "40 mm Oystersteel", "Bezel": "Cerachrom red/blue, 24 h", "Bracelet": "Jubilee"}, "ref": "Rolex GMT-Master II 126710BLRO specifications."}, {"t": "A. Lange & Sohne Lange 1", "mk": "A. Lange & Sohne", "yr": "1994", "cat": "dress", "blurb": "The 1994 relaunch icon with its off-centre dial and outsize date, the watch that re-established Glashutte watchmaking.", "spec": {"Origin": "1994 relaunch", "Movement": "Calibre L121.1, manual", "Signature": "Outsize date, off-centre dial", "Case": "38.5 mm gold"}, "ref": "A. Lange & Sohne Lange 1 history, 1994."}, {"t": "Omega Seamaster Diver 300M 210.30.42.20.03.001", "mk": "Omega", "yr": "2018", "cat": "dive", "blurb": "The 2018 generation with wave dial, Master Chronometer calibre 8800, and helium escape valve.", "spec": {"Movement": "Calibre 8800, Master Chronometer", "Case": "42 mm steel", "Water resistance": "300 m", "Bezel": "Ceramic"}, "ref": "Omega Seamaster Diver 300M specifications."}, {"t": "Zenith El Primero", "mk": "Zenith", "yr": "1969", "cat": "chronograph", "blurb": "One of the first automatic chronographs, beating at 36,000 vibrations per hour since 1969.", "spec": {"Origin": "1969", "Movement": "El Primero, 36,000 vph", "Type": "Automatic chronograph", "Legacy": "In production since 1969"}, "ref": "Zenith El Primero history, 1969."}, {"t": "IWC Portugieser Chronograph IW3716", "mk": "IWC", "yr": "1998", "cat": "dress", "blurb": "The modern Portugieser chronograph with recessed subdials and feuille hands, a direct line to the 1939 original.", "spec": {"Origin": "Lineage to 1939", "Case": "41 mm steel", "Movement": "Calibre 69355", "Style": "Dress chronograph"}, "ref": "IWC Portugieser Chronograph specifications."}, {"t": "Vacheron Constantin Overseas 4500V", "mk": "Vacheron Constantin", "yr": "2016", "cat": "luxury-sport", "blurb": "The third-generation Overseas with quick-change bracelet system and the calibre 5100.", "spec": {"Movement": "Calibre 5100", "Case": "41 mm steel", "Bracelet": "Interchangeable system", "Heritage": "Overseas line since 1996"}, "ref": "Vacheron Constantin Overseas specifications."}, {"t": "Casio G-Shock DW-5600", "mk": "Casio", "yr": "1983", "cat": "field", "blurb": "Kikuo Ibe's 1983 \"triple 10\" tough watch — 10-metre drop, 10-bar water resistance, 10-year battery — still the G-Shock archetype.", "spec": {"Origin": "1983, Kikuo Ibe", "Shock resistance": "Triple-10 concept", "Water resistance": "200 m", "Battery": "~10 years"}, "ref": "Casio G-Shock DW-5600 history, 1983."}, {"t": "Seiko SKX007", "mk": "Seiko", "yr": "1996", "cat": "dive", "blurb": "The beloved automatic diver with the 7S26 movement, discontinued in 2019 and since a cult collectible.", "spec": {"Movement": "7S26 automatic", "Case": "42 mm steel", "Water resistance": "200 m", "Status": "Discontinued 2019"}, "ref": "Seiko SKX007 specifications and discontinuation, 2019."}, {"t": "Hamilton Khaki Field Mechanical", "mk": "Hamilton", "yr": "2018", "cat": "field", "blurb": "The modern descendant of the Vietnam-era MIL-W-46374 field watch, hand-wound and true to the original proportions.", "spec": {"Movement": "H-50, 80 h reserve", "Case": "38 mm steel", "Heritage": "US military field watches", "Style": "Military field"}, "ref": "Hamilton Khaki Field specifications; MIL-W-46374 lineage."}, {"t": "Nomos Tangente", "mk": "Nomos Glashutte", "yr": "1992", "cat": "dress", "blurb": "The Bauhaus-minimalist Glashutte original that put Nomos on the map, with the in-house Alpha calibre.", "spec": {"Origin": "1992", "Movement": "Alpha, manual, in-house", "Case": "35-38 mm steel", "Design": "Bauhaus"}, "ref": "Nomos Glashutte Tangente specifications."}, {"t": "Bulova Lunar Pilot", "mk": "Bulova", "yr": "1971", "cat": "chronograph", "blurb": "The chronograph worn on the Moon during Apollo 15 in 1971, reissued in faithful high-precision quartz form.", "spec": {"Heritage": "Worn on the Moon, Apollo 15, 1971", "Case": "43.5 mm steel", "Movement": "High-precision quartz", "Reissue": "Faithful archive reissue"}, "ref": "Bulova Lunar Pilot history, Apollo 15."}, {"t": "Tissot PRX Powermatic 80", "mk": "Tissot", "yr": "2021", "cat": "luxury-sport", "blurb": "The 2021 revival of the 1978 integrated-bracelet design, with an 80-hour Powermatic movement at an accessible price.", "spec": {"Origin": "1978 design, revived 2021", "Movement": "Powermatic 80, 80 h", "Case": "40 mm steel", "Bracelet": "Integrated"}, "ref": "Tissot PRX history and specifications."}, {"t": "Longines Master Collection Moonphase", "mk": "Longines", "yr": "2005", "cat": "moonphase", "blurb": "The elegant moonphase of the Master Collection line, carrying Longines' long complication heritage.", "spec": {"Complication": "Moonphase, date", "Case": "40-42 mm steel", "Movement": "Automatic L899", "Style": "Classic dress"}, "ref": "Longines Master Collection specifications."}];
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
