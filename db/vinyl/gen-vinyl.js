/* ✳ SIGNATURE — JAH Vinyl Record Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-VIN-0000001 .. JAH-VIN-1000000). Browser: registers with JAHDB. Node:
   run `node gen-vinyl.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='vinyl', PREFIX='JAH-VIN-', VERSION='jahdb-vinyl-1.0';
var KIND='vinyl record', AI='JAH Vinyl Creator';
var CATEGORIES=["rock", "jazz", "soul", "hip-hop", "classical", "electronic", "blues", "country"];
var MAKERS=["Signature Wax Works", "JAH Groove Pressing", "Meridian Records", "Velvet Groove Co.", "Analog Atelier", "Northside Vinyl", "Golden Groove Press", "Harborlight Records", "Copperline Audio", "Starling Wax Co.", "Moonphase Records", "Ivory Key Vinyl"], LINES=["First Pressing", "Analog Master", "Studio Session", "Live Archive", "Deep Groove", "Mono Edition", "Half-Speed Master", "Deluxe Reissue", "Night Session", "Origin Cut"], WORDS=["cut from the original analog tapes", "pressed on 180-gram virgin vinyl", "a tip-on gatefold sleeve", "an all-analog mastering chain", "a numbered limited run", "a faithful mono mix", "a half-speed mastered cut", "a heavyweight audiophile pressing"], DESCS=["LP", "Deluxe LP", "Mono LP", "Live LP", "Studio LP", "Reissue", "Box Set", "EP", "Picture Disc", "Audiophile LP", "Session LP", "Demo LP"];
var SPEC_KEYS=["Format", "Speed", "Weight", "Label", "Mastering", "Sleeve"], SPEC_VALS=[["12-inch LP", "12-inch LP", "10-inch LP", "7-inch single"], ["33 1/3 RPM", "33 1/3 RPM", "45 RPM", "33 1/3 RPM"], ["140 g", "180 g", "200 g", "180 g"], ["Signature Wax Works", "Meridian Records", "Velvet Groove Co.", "Analog Atelier"], ["all-analog", "half-speed", "direct metal master", "original master"], ["gatefold", "tip-on single", "deluxe box", "standard sleeve"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Kind of Blue — Miles Davis", "mk": "Miles Davis", "yr": "1959", "cat": "jazz", "blurb": "Recorded in 1959, the best-selling jazz album of all time and a landmark of modal jazz.", "spec": {"Artist": "Miles Davis", "Released": "1959", "Genre": "Modal jazz", "Legacy": "Best-selling jazz album ever"}, "ref": "Kind of Blue session and sales history, Columbia 1959."}, {"t": "Sgt. Pepper's Lonely Hearts Club Band — The Beatles", "mk": "The Beatles", "yr": "1967", "cat": "rock", "blurb": "The 1967 concept album that redefined what a rock LP could be, with its Peter Blake cover.", "spec": {"Artist": "The Beatles", "Released": "1967", "Cover": "Peter Blake collage", "Legacy": "Redefined the album form"}, "ref": "Sgt. Pepper's release history, Parlophone/Capitol 1967."}, {"t": "Thriller — Michael Jackson", "mk": "Michael Jackson", "yr": "1982", "cat": "soul", "blurb": "The 1982 Quincy Jones production, the best-selling album of all time at an estimated 70 million copies.", "spec": {"Artist": "Michael Jackson", "Released": "1982", "Producer": "Quincy Jones", "Sales": "~70 million, best-selling ever"}, "ref": "Thriller sales and production history, Epic 1982."}, {"t": "Nevermind — Nirvana", "mk": "Nirvana", "yr": "1991", "cat": "rock", "blurb": "The 1991 album whose lead single \"Smells Like Teen Spirit\" carried grunge to the top of the charts.", "spec": {"Artist": "Nirvana", "Released": "1991", "Single": "Smells Like Teen Spirit", "Legacy": "Defined grunge's breakthrough"}, "ref": "Nevermind release history, DGC 1991."}, {"t": "What's Going On — Marvin Gaye", "mk": "Marvin Gaye", "yr": "1971", "cat": "soul", "blurb": "Marvin Gaye's 1971 song-cycle on war, ecology, and faith, recorded against Motown's wishes.", "spec": {"Artist": "Marvin Gaye", "Released": "1971", "Theme": "Social song-cycle", "Legacy": "Landmark soul album"}, "ref": "What's Going On recording history, Tamla 1971."}, {"t": "The Dark Side of the Moon — Pink Floyd", "mk": "Pink Floyd", "yr": "1973", "cat": "rock", "blurb": "The 1973 prism-covered album that spent more than 950 weeks on the Billboard 200.", "spec": {"Artist": "Pink Floyd", "Released": "1973", "Chart run": "950+ weeks, Billboard 200", "Cover": "Prism by Hipgnosis"}, "ref": "Dark Side of the Moon chart history."}, {"t": "Abbey Road — The Beatles", "mk": "The Beatles", "yr": "1969", "cat": "rock", "blurb": "The Beatles' 1969 swan song with the famous zebra-crossing cover, home to \"Come Together\" and \"Here Comes the Sun\".", "spec": {"Artist": "The Beatles", "Released": "1969", "Cover": "Zebra crossing, EMI Studios", "Legacy": "Final recorded album"}, "ref": "Abbey Road release history, Apple 1969."}, {"t": "Rumours — Fleetwood Mac", "mk": "Fleetwood Mac", "yr": "1977", "cat": "rock", "blurb": "The 1977 breakup album that became one of the best-selling records ever, with four US top-10 singles.", "spec": {"Artist": "Fleetwood Mac", "Released": "1977", "Singles": "Four US top-10 hits", "Sales": "40+ million"}, "ref": "Rumours sales and chart history, Warner Bros. 1977."}, {"t": "Illmatic — Nas", "mk": "Nas", "yr": "1994", "cat": "hip-hop", "blurb": "Nas's 1994 debut, widely cited as one of the greatest hip-hop albums ever recorded.", "spec": {"Artist": "Nas", "Released": "1994", "Debut": "Studio debut", "Legacy": "Landmark East Coast hip-hop"}, "ref": "Illmatic release history, Columbia 1994."}, {"t": "Blue — Joni Mitchell", "mk": "Joni Mitchell", "yr": "1971", "cat": "rock", "blurb": "Joni Mitchell's 1971 confessional masterpiece, a touchstone of singer-songwriter craft.", "spec": {"Artist": "Joni Mitchell", "Released": "1971", "Style": "Confessional folk", "Legacy": "Singer-songwriter landmark"}, "ref": "Blue release history, Reprise 1971."}, {"t": "Pet Sounds — The Beach Boys", "mk": "The Beach Boys", "yr": "1966", "cat": "rock", "blurb": "Brian Wilson's 1966 studio opus, an influence on the Beatles' own Sgt. Pepper sessions.", "spec": {"Artist": "The Beach Boys", "Released": "1966", "Producer": "Brian Wilson", "Legacy": "Studio-pop landmark"}, "ref": "Pet Sounds recording history, Capitol 1966."}, {"t": "The Velvet Underground & Nico", "mk": "The Velvet Underground", "yr": "1967", "cat": "rock", "blurb": "The 1967 Warhol banana-cover debut that famously sold few copies but started a thousand bands.", "spec": {"Artist": "The Velvet Underground", "Released": "1967", "Cover": "Andy Warhol banana", "Legacy": "Most influential debut ever"}, "ref": "Velvet Underground & Nico history, Verve 1967."}, {"t": "A Love Supreme — John Coltrane", "mk": "John Coltrane", "yr": "1965", "cat": "jazz", "blurb": "Coltrane's 1965 four-part spiritual suite, his self-declared \"humble offering to God\".", "spec": {"Artist": "John Coltrane", "Released": "1965", "Form": "Four-part suite", "Legacy": "Spiritual jazz landmark"}, "ref": "A Love Supreme session history, Impulse! 1965."}, {"t": "Highway 61 Revisited — Bob Dylan", "mk": "Bob Dylan", "yr": "1965", "cat": "rock", "blurb": "The 1965 electric breakthrough opening with \"Like a Rolling Stone\".", "spec": {"Artist": "Bob Dylan", "Released": "1965", "Single": "Like a Rolling Stone", "Legacy": "Electric folk-rock landmark"}, "ref": "Highway 61 Revisited history, Columbia 1965."}, {"t": "Are You Experienced — The Jimi Hendrix Experience", "mk": "Jimi Hendrix", "yr": "1967", "cat": "rock", "blurb": "Hendrix's 1967 debut that rewrote electric guitar vocabulary in a single LP.", "spec": {"Artist": "Jimi Hendrix", "Released": "1967", "Debut": "Studio debut", "Legacy": "Redefined electric guitar"}, "ref": "Are You Experienced history, Track 1967."}, {"t": "Led Zeppelin IV", "mk": "Led Zeppelin", "yr": "1971", "cat": "rock", "blurb": "The untitled 1971 fourth album with \"Stairway to Heaven\", one of the best-selling LPs ever.", "spec": {"Artist": "Led Zeppelin", "Released": "1971", "Title": "Untitled (four symbols)", "Sales": "37+ million"}, "ref": "Led Zeppelin IV history, Atlantic 1971."}, {"t": "Born to Run — Bruce Springsteen", "mk": "Bruce Springsteen", "yr": "1975", "cat": "rock", "blurb": "Springsteen's 1975 breakout, the \"wall of sound\" bid for rock immortality.", "spec": {"Artist": "Bruce Springsteen", "Released": "1975", "Breakout": "Third studio album", "Legacy": "Heartland rock landmark"}, "ref": "Born to Run history, Columbia 1975."}, {"t": "Purple Rain — Prince and the Revolution", "mk": "Prince", "yr": "1984", "cat": "soul", "blurb": "Prince's 1984 film soundtrack, a nine-track run that held number one for 24 weeks.", "spec": {"Artist": "Prince", "Released": "1984", "Film": "Purple Rain", "Chart": "24 weeks at No. 1"}, "ref": "Purple Rain history, Warner Bros. 1984."}, {"t": "Back in Black — AC/DC", "mk": "AC/DC", "yr": "1980", "cat": "rock", "blurb": "The 1980 tribute to Bon Scott and one of the best-selling albums in history.", "spec": {"Artist": "AC/DC", "Released": "1980", "Tribute": "To Bon Scott", "Sales": "50+ million"}, "ref": "Back in Black history, Atlantic 1980."}, {"t": "The Miseducation of Lauryn Hill", "mk": "Lauryn Hill", "yr": "1998", "cat": "hip-hop", "blurb": "The 1998 solo debut that won five Grammys including Album of the Year.", "spec": {"Artist": "Lauryn Hill", "Released": "1998", "Grammys": "Five, incl. Album of the Year", "Legacy": "Neo-soul landmark"}, "ref": "Miseducation Grammy and release history, 1998."}, {"t": "Enter the Wu-Tang (36 Chambers)", "mk": "Wu-Tang Clan", "yr": "1993", "cat": "hip-hop", "blurb": "The 1993 RZA-produced debut that launched the Wu-Tang empire.", "spec": {"Artist": "Wu-Tang Clan", "Released": "1993", "Producer": "RZA", "Legacy": "Hardcore hip-hop landmark"}, "ref": "Enter the Wu-Tang history, Loud 1993."}, {"t": "Time Out — The Dave Brubeck Quartet", "mk": "Dave Brubeck", "yr": "1959", "cat": "jazz", "blurb": "The 1959 odd-time-signature landmark with \"Take Five\", the best-selling jazz single ever.", "spec": {"Artist": "Dave Brubeck Quartet", "Released": "1959", "Single": "Take Five in 5/4", "Legacy": "Odd-meter jazz landmark"}, "ref": "Time Out history, Columbia 1959."}, {"t": "OK Computer — Radiohead", "mk": "Radiohead", "yr": "1997", "cat": "rock", "blurb": "Radiohead's 1997 dystopian song-cycle, a defining album of the decade.", "spec": {"Artist": "Radiohead", "Released": "1997", "Theme": "Technological dread", "Legacy": "Album-of-decade lists"}, "ref": "OK Computer history, XL/Parlophone 1997."}, {"t": "London Calling — The Clash", "mk": "The Clash", "yr": "1979", "cat": "rock", "blurb": "The 1979 double album with the Pennie Smith cover, punk's great expansion.", "spec": {"Artist": "The Clash", "Released": "1979", "Format": "Double LP", "Cover": "Pennie Smith photo"}, "ref": "London Calling history, CBS 1979."}];
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
