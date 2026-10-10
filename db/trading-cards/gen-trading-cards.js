/* ✳ SIGNATURE — JAH Trading Card Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-TC-0000001 .. JAH-TC-1000000). Browser: registers with JAHDB. Node:
   run `node gen-trading-cards.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='trading-cards', PREFIX='JAH-TC-', VERSION='jahdb-trading-cards-1.0';
var KIND='trading card', AI='JAH Card Creator';
var CATEGORIES=["baseball", "basketball", "football", "pokemon", "magic", "hockey", "soccer", "comics"];
var MAKERS=["Signature Card Co.", "JAH Card Works", "Meridian Mint", "Heritage Card Atelier", "Apex Card Press", "Golden Era Cards", "Vantage Trading Co.", "Legacy Card House", "Paragon Prints", "Starlight Cards", "Copperfoil Press", "Grandstand Cards"], LINES=["Rookie Series", "Legends Set", "All-Star Edition", "Heritage Collection", "Chrome Parallel", "Autograph Issue", "Showcase Set", "Diamond Parallel", "Centennial Set", "Origin Issue"], WORDS=["a holographic foil finish", "an on-card autograph", "a low-numbered parallel", "a rookie-year issue", "a refractor rainbow finish", "a game-worn memorabilia swatch", "a hand-numbered print run", "a pristine gem-mint grade"], DESCS=["Rookie Card", "Star Card", "Parallel", "Autograph Card", "Relic Card", "Insert", "Base Card", "Showcase Card", "Chrome Card", "Veteran Card", "Prospect Card", "Legend Card"];
var SPEC_KEYS=["Set", "Card no.", "Year", "Print run", "Finish", "Grading"], SPEC_VALS=[["Rookie Series", "Legends Set", "Heritage Collection", "Chrome Parallel"], ["#1", "#7", "#23", "#101"], ["2024", "2025", "2026", "2023"], ["base issue", "numbered to 500", "numbered to 99", "one of one"], ["gloss", "holographic foil", "refractor", "matte"], ["ungraded", "PSA 9", "PSA 10", "BGS 9.5"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "1952 Topps Mickey Mantle #311", "mk": "Topps", "yr": "1952", "cat": "baseball", "blurb": "The post-war hobby's most famous card; a PSA 9 sold for $12.6 million in August 2022, the record for any sports card.", "spec": {"Set": "1952 Topps", "Card": "#311", "Player": "Mickey Mantle", "Record sale": "$12.6M, Heritage, Aug 2022"}, "ref": "Heritage Auctions sale record, August 2022."}, {"t": "1986 Fleer Michael Jordan #57", "mk": "Fleer", "yr": "1986", "cat": "basketball", "blurb": "Jordan's mainstream rookie card from the 1986 Fleer set, the blue-chip of basketball collecting.", "spec": {"Set": "1986 Fleer", "Card": "#57", "Player": "Michael Jordan", "Status": "Definitive rookie card"}, "ref": "1986 Fleer basketball set history."}, {"t": "1979 O-Pee-Chee Wayne Gretzky #18", "mk": "O-Pee-Chee", "yr": "1979", "cat": "hockey", "blurb": "The Great One's rookie card, blue-chip of hockey collecting with its distinctive blue borders.", "spec": {"Set": "1979 O-Pee-Chee", "Card": "#18", "Player": "Wayne Gretzky", "Status": "Definitive rookie card"}, "ref": "1979 O-Pee-Chee hockey set history."}, {"t": "1909-11 T206 Honus Wagner", "mk": "American Tobacco", "yr": "1909", "cat": "baseball", "blurb": "The \"Mona Lisa of cards\" — pulled from production early, with only about 60 known examples.", "spec": {"Set": "T206", "Years": "1909-1911", "Player": "Honus Wagner", "Known": "~60 examples"}, "ref": "T206 Honus Wagner production history."}, {"t": "2000 Playoff Contenders Tom Brady #144", "mk": "Playoff", "yr": "2000", "cat": "football", "blurb": "Brady's championship-ticket rookie autograph; one sold for $3.1 million in 2021.", "spec": {"Set": "2000 Playoff Contenders", "Card": "#144", "Player": "Tom Brady", "Sale": "$3.1M, 2021"}, "ref": "Lelands auction record, June 2021."}, {"t": "1999 Pokemon Base Set 1st Edition Charizard #4", "mk": "Wizards of the Coast", "yr": "1999", "cat": "pokemon", "blurb": "The grail of English Pokemon, the 1st Edition holographic Charizard from the 1999 Base Set.", "spec": {"Set": "Base Set, 1st Edition", "Card": "#4/102", "Pokemon": "Charizard", "Hobby": "English Pokemon grail"}, "ref": "1999 Base Set 1st Edition print history."}, {"t": "1998 Pokemon Japanese Promo Illustrator Pikachu", "mk": "Creatures Inc.", "yr": "1998", "cat": "pokemon", "blurb": "Awarded to illustration contest winners in 1998; one sold for $5.275 million in 2022, the priciest Pokemon card ever.", "spec": {"Issue": "CoroCoro contest prize, 1998", "Pokemon": "Pikachu", "Rarity": "39 awarded", "Record": "$5.275M, 2022"}, "ref": "Guinness World Records sale certification, July 2022."}, {"t": "Alpha Black Lotus — Magic: The Gathering", "mk": "Wizards of the Coast", "yr": "1993", "cat": "magic", "blurb": "The most famous Magic card ever printed, from the 1993 Alpha run of just 1,100 of each rare.", "spec": {"Set": "Alpha, 1993", "Card": "Black Lotus", "Print": "~1,100 rares", "Status": "Most famous MTG card"}, "ref": "Magic: The Gathering Alpha print history, 1993."}, {"t": "1989 Upper Deck Ken Griffey Jr. #1", "mk": "Upper Deck", "yr": "1989", "cat": "baseball", "blurb": "Card #1 of Upper Deck's 1989 debut set, the rookie that defined the premium-card era.", "spec": {"Set": "1989 Upper Deck", "Card": "#1", "Player": "Ken Griffey Jr.", "Era": "Birth of premium cards"}, "ref": "1989 Upper Deck set history."}, {"t": "1933 Goudey Babe Ruth #53", "mk": "Goudey", "yr": "1933", "cat": "baseball", "blurb": "One of four Ruth cards in the 1933 Goudey set, the Depression era's most colorful issue.", "spec": {"Set": "1933 Goudey", "Card": "#53", "Player": "Babe Ruth", "Era": "Depression-era classic"}, "ref": "1933 Goudey set history."}, {"t": "2009 Bowman Chrome Mike Trout Superfractor", "mk": "Bowman", "yr": "2009", "cat": "baseball", "blurb": "Trout's one-of-one Superfractor rookie; sold for $3.9 million in 2020, then the record.", "spec": {"Set": "2009 Bowman Chrome", "Card": "Superfractor 1/1", "Player": "Mike Trout", "Sale": "$3.9M, 2020"}, "ref": "Goldin Auctions sale record, August 2020."}, {"t": "2003-04 Upper Deck Exquisite LeBron James RPA", "mk": "Upper Deck", "yr": "2003", "cat": "basketball", "blurb": "The Exquisite rookie patch autograph numbered to 23; one sold for $5.2 million in 2021.", "spec": {"Set": "2003-04 Exquisite", "Card": "RPA /23", "Player": "LeBron James", "Sale": "$5.2M, 2021"}, "ref": "PWCC sale record, April 2021."}, {"t": "1993 SP Derek Jeter #279", "mk": "Upper Deck", "yr": "1993", "cat": "baseball", "blurb": "The SP foil rookie of Derek Jeter, condition-sensitive and iconic.", "spec": {"Set": "1993 SP", "Card": "#279", "Player": "Derek Jeter", "Note": "Foil, condition-sensitive"}, "ref": "1993 SP baseball set history."}, {"t": "1968 Topps Nolan Ryan #177", "mk": "Topps", "yr": "1968", "cat": "baseball", "blurb": "Ryan's rookie card, shared with Jerry Koosman, from the 1968 Topps set.", "spec": {"Set": "1968 Topps", "Card": "#177", "Player": "Nolan Ryan / Koosman", "Status": "Rookie card"}, "ref": "1968 Topps set history."}, {"t": "1980 Topps Rickey Henderson #482", "mk": "Topps", "yr": "1980", "cat": "baseball", "blurb": "The rookie of baseball's all-time stolen-base king.", "spec": {"Set": "1980 Topps", "Card": "#482", "Player": "Rickey Henderson", "Status": "Rookie card"}, "ref": "1980 Topps set history."}, {"t": "1948 Leaf Jackie Robinson #79", "mk": "Leaf", "yr": "1948", "cat": "baseball", "blurb": "Robinson's rookie card from the 1948 Leaf set, issued one year after he broke the color barrier.", "spec": {"Set": "1948 Leaf", "Card": "#79", "Player": "Jackie Robinson", "Context": "Year after 1947 debut"}, "ref": "1948 Leaf set history."}, {"t": "1961 Fleer Wilt Chamberlain #8", "mk": "Fleer", "yr": "1961", "cat": "basketball", "blurb": "Chamberlain's rookie from the 1961 Fleer set, issued in his 100-point season.", "spec": {"Set": "1961 Fleer", "Card": "#8", "Player": "Wilt Chamberlain", "Season": "100-point season"}, "ref": "1961 Fleer basketball history."}, {"t": "1980 Topps Bird/Erving/Johnson #34", "mk": "Topps", "yr": "1980", "cat": "basketball", "blurb": "The perforated triple-panel rookie of Larry Bird and Magic Johnson — two rookies, one card.", "spec": {"Set": "1980 Topps", "Card": "#34", "Players": "Bird, Erving, Magic", "Format": "Perforated triple panel"}, "ref": "1980 Topps basketball set history."}, {"t": "1955 Topps Roberto Clemente #164", "mk": "Topps", "yr": "1955", "cat": "baseball", "blurb": "Clemente's rookie card from the 1955 Topps set.", "spec": {"Set": "1955 Topps", "Card": "#164", "Player": "Roberto Clemente", "Status": "Rookie card"}, "ref": "1955 Topps set history."}, {"t": "1996 Topps Chrome Kobe Bryant #138", "mk": "Topps", "yr": "1996", "cat": "basketball", "blurb": "Kobe's Topps Chrome rookie from the celebrated 1996 draft class.", "spec": {"Set": "1996 Topps Chrome", "Card": "#138", "Player": "Kobe Bryant", "Class": "1996 draft"}, "ref": "1996 Topps Chrome basketball history."}, {"t": "1957 Topps Bill Russell #77", "mk": "Topps", "yr": "1957", "cat": "basketball", "blurb": "The rookie card of the 11-time champion Bill Russell.", "spec": {"Set": "1957 Topps", "Card": "#77", "Player": "Bill Russell", "Titles": "11 championships"}, "ref": "1957 Topps basketball history."}, {"t": "1972 Topps Julius Erving #195", "mk": "Topps", "yr": "1972", "cat": "basketball", "blurb": "Dr. J's rookie card from the 1972 Topps set.", "spec": {"Set": "1972 Topps", "Card": "#195", "Player": "Julius Erving", "Status": "Rookie card"}, "ref": "1972 Topps basketball history."}, {"t": "1951 Bowman Mickey Mantle #253", "mk": "Bowman", "yr": "1951", "cat": "baseball", "blurb": "Mantle's true rookie card, predating the famous 1952 Topps by a year.", "spec": {"Set": "1951 Bowman", "Card": "#253", "Player": "Mickey Mantle", "Status": "True rookie card"}, "ref": "1951 Bowman set history."}, {"t": "Alifabolaget 1958 Pele #635", "mk": "Alifabolaget", "yr": "1958", "cat": "soccer", "blurb": "The Swedish rookie card of 17-year-old Pele from his 1958 World Cup triumph.", "spec": {"Set": "Alifabolaget 1958", "Card": "#635", "Player": "Pele", "Context": "1958 World Cup winner, age 17"}, "ref": "Alifabolaget 1958 set history."}];
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
