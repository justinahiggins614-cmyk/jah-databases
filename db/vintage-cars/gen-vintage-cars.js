/* ✳ SIGNATURE — JAH Vintage Car Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-VC-0000001 .. JAH-VC-1000000). Browser: registers with JAHDB. Node:
   run `node gen-vintage-cars.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='vintage-cars', PREFIX='JAH-VC-', VERSION='jahdb-vintage-cars-1.0';
var KIND='vintage car', AI='JAH Vintage Car Creator';
var CATEGORIES=["american-classic", "european-sports", "muscle", "pre-war", "luxury", "racing"];
var MAKERS=["Signature Motor Works", "JAH Coachbuilders", "Meridian Motors", "Heritage Auto Atelier", "Apex Motor Co.", "Continental Coachworks", "Paramount Motors", "Golden Era Garage", "Vantage Motor Works", "Legacy Auto House", "Copperline Motors", "Regent Coachbuilders"], LINES=["Heritage Tourer", "Grand Routier", "Speedster", "Continental Coupe", "Pioneer Roadster", "Centennial Sedan", "Rally Special", "Gentleman Racer", "Golden Age", "Origin Model"], WORDS=["a hand-formed aluminum body", "a numbers-matching drivetrain", "a full concours restoration", "its original interior trim", "a documented ownership history", "a freshly rebuilt engine", "factory-correct paint", "a complete tool roll"], DESCS=["Coupe", "Roadster", "Convertible", "Sedan", "Speedster", "Tourer", "Cabriolet", "Spyder", "Grand Tourer", "Phaeton", "Runabout", "Shooting Brake"];
var SPEC_KEYS=["Engine", "Power", "Transmission", "Body", "Production", "Drive"], SPEC_VALS=[["V8", "inline-six", "V12", "flat-four"], ["200 hp", "300 hp", "425 hp", "150 hp"], ["4-speed manual", "3-speed automatic", "5-speed manual", "2-speed automatic"], ["coupe", "convertible", "roadster", "sedan"], ["limited run", "5,000 built", "25,000 built", "one-year only"], ["rear-wheel drive", "rear-wheel drive", "front-wheel drive", "rear-wheel drive"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Ford Model T", "mk": "Ford", "yr": "1908", "cat": "american-classic", "blurb": "The car that put the world on wheels: over 15 million built from 1908 to 1927.", "spec": {"Maker": "Ford", "Years": "1908-1927", "Built": "15+ million", "Legacy": "First affordable automobile"}, "ref": "Ford Motor Company production records."}, {"t": "1957 Chevrolet Bel Air", "mk": "Chevrolet", "yr": "1957", "cat": "american-classic", "blurb": "The Tri-Five icon with its tailfins and chrome, the definitive 1950s American car.", "spec": {"Maker": "Chevrolet", "Year": "1957", "Style": "Tailfin era icon", "Engine": "283 V8"}, "ref": "Chevrolet production history."}, {"t": "1965 Ford Mustang", "mk": "Ford", "yr": "1964", "cat": "american-classic", "blurb": "Launched April 1964 as a 1964 1/2, the Mustang created the pony-car class and sold 22,000 on day one.", "spec": {"Maker": "Ford", "Launch": "April 1964", "First day": "22,000 sold", "Class": "Created the pony car"}, "ref": "Ford Mustang launch records, 1964."}, {"t": "1963 Chevrolet Corvette Sting Ray", "mk": "Chevrolet", "yr": "1963", "cat": "american-classic", "blurb": "The split-window coupe of 1963, Bill Mitchell's masterpiece and a one-year design.", "spec": {"Maker": "Chevrolet", "Year": "1963", "Design": "Split rear window", "Designer": "Bill Mitchell"}, "ref": "Chevrolet Corvette history."}, {"t": "1969 Dodge Charger", "mk": "Dodge", "yr": "1969", "cat": "muscle", "blurb": "The Coke-bottle 1969 Charger, immortalized on screen and the street.", "spec": {"Maker": "Dodge", "Year": "1969", "Engine": "Up to 426 Hemi", "Style": "Coke-bottle coupe"}, "ref": "Dodge Charger production history."}, {"t": "Pontiac GTO", "mk": "Pontiac", "yr": "1964", "cat": "muscle", "blurb": "John DeLorean's 1964 Tempest option package that invented the muscle car.", "spec": {"Maker": "Pontiac", "Year": "1964", "Creator": "John DeLorean", "Note": "First muscle car"}, "ref": "Pontiac GTO history."}, {"t": "1970 Plymouth Hemi 'Cuda", "mk": "Plymouth", "yr": "1970", "cat": "muscle", "blurb": "The 426 Hemi E-body, among the most valuable American muscle cars ever sold.", "spec": {"Maker": "Plymouth", "Year": "1970", "Engine": "426 Hemi V8", "Rarity": "Blue-chip muscle"}, "ref": "Plymouth production records."}, {"t": "1961 Jaguar E-Type", "mk": "Jaguar", "yr": "1961", "cat": "european-sports", "blurb": "Unveiled at Geneva in 1961; Enzo Ferrari called it the most beautiful car ever made.", "spec": {"Maker": "Jaguar", "Debut": "Geneva 1961", "Quote": "\"Most beautiful car ever\" — Enzo Ferrari", "Speed": "150 mph"}, "ref": "Jaguar E-Type launch history."}, {"t": "1955 Mercedes-Benz 300SL Gullwing", "mk": "Mercedes-Benz", "yr": "1955", "cat": "european-sports", "blurb": "The 1955 gullwing-door coupe, the fastest production car of its day.", "spec": {"Maker": "Mercedes-Benz", "Year": "1955", "Doors": "Gullwing", "Note": "Fastest production car of 1955"}, "ref": "Mercedes-Benz 300SL history."}, {"t": "1962 Ferrari 250 GTO", "mk": "Ferrari", "yr": "1962", "cat": "racing", "blurb": "Only 36 built; one sold for $48.4 million in 2018, then the most expensive car ever auctioned.", "spec": {"Maker": "Ferrari", "Built": "36", "Year": "1962-64", "Record": "$48.4M, 2018"}, "ref": "RM Sotheby's Monterey sale, August 2018."}, {"t": "1966 Ford GT40", "mk": "Ford", "yr": "1966", "cat": "racing", "blurb": "The car that ended Ferrari's Le Mans streak with a 1-2-3 finish in 1966.", "spec": {"Maker": "Ford", "Year": "1966", "Win": "Le Mans 1-2-3", "Rival": "Ferrari"}, "ref": "Le Mans records, 1966."}, {"t": "1964 Porsche 911", "mk": "Porsche", "yr": "1964", "cat": "european-sports", "blurb": "The 1964 debut of the rear-engined icon, in production ever since.", "spec": {"Maker": "Porsche", "Debut": "1964", "Layout": "Rear-engined", "Legacy": "In production since 1964"}, "ref": "Porsche 911 history."}, {"t": "1959 Cadillac Eldorado", "mk": "Cadillac", "yr": "1959", "cat": "luxury", "blurb": "The 1959 Eldorado with the tallest tailfins ever fitted to a production car.", "spec": {"Maker": "Cadillac", "Year": "1959", "Fins": "Tallest ever", "Era": "Peak tailfin"}, "ref": "Cadillac production history."}, {"t": "1948 Tucker 48", "mk": "Tucker", "yr": "1948", "cat": "american-classic", "blurb": "Preston Tucker's safety pioneer; only 51 built before the company folded.", "spec": {"Maker": "Tucker", "Year": "1948", "Built": "51", "Note": "Safety pioneer"}, "ref": "Tucker automobile history."}, {"t": "1930 Duesenberg Model J", "mk": "Duesenberg", "yr": "1930", "cat": "pre-war", "blurb": "The straight-eight aristocrat of the classic era, coachbuilt for America's elite.", "spec": {"Maker": "Duesenberg", "Year": "1930", "Engine": "Straight-eight", "Era": "Classic-era flagship"}, "ref": "Duesenberg history."}, {"t": "1932 Ford (Deuce)", "mk": "Ford", "yr": "1932", "cat": "pre-war", "blurb": "The 1932 Ford with the flathead V8, the foundation of hot-rod culture.", "spec": {"Maker": "Ford", "Year": "1932", "Engine": "Flathead V8", "Legacy": "Hot-rod foundation"}, "ref": "Ford production history."}, {"t": "1953 Chevrolet Corvette", "mk": "Chevrolet", "yr": "1953", "cat": "american-classic", "blurb": "The first-year Corvette: 300 Polo White roadsters, hand-built in Flint.", "spec": {"Maker": "Chevrolet", "Year": "1953", "Built": "300", "Note": "First-year Corvette"}, "ref": "Chevrolet Corvette history."}, {"t": "1963 Aston Martin DB5", "mk": "Aston Martin", "yr": "1963", "cat": "european-sports", "blurb": "The 1963 DB5, immortalized as James Bond's car in Goldfinger.", "spec": {"Maker": "Aston Martin", "Year": "1963", "Film": "Goldfinger, 1964", "Engine": "4.0L straight-six"}, "ref": "Aston Martin DB5 history."}, {"t": "1959 Mini", "mk": "BMC", "yr": "1959", "cat": "european-sports", "blurb": "Alec Issigonis's 1959 transverse-engine marvel that democratized clever packaging.", "spec": {"Maker": "BMC", "Year": "1959", "Designer": "Alec Issigonis", "Layout": "Transverse FWD"}, "ref": "Mini history, 1959."}, {"t": "1966 Lamborghini Miura", "mk": "Lamborghini", "yr": "1966", "cat": "european-sports", "blurb": "The 1966 transverse-V12 that invented the supercar.", "spec": {"Maker": "Lamborghini", "Year": "1966", "Layout": "Mid-transverse V12", "Note": "First supercar"}, "ref": "Lamborghini Miura history."}, {"t": "1987 Ferrari F40", "mk": "Ferrari", "yr": "1987", "cat": "european-sports", "blurb": "The last car signed off by Enzo Ferrari, the twin-turbo 1987 flagship.", "spec": {"Maker": "Ferrari", "Year": "1987", "Engine": "Twin-turbo V8", "Note": "Last Enzo-era flagship"}, "ref": "Ferrari F40 history."}, {"t": "1992 McLaren F1", "mk": "McLaren", "yr": "1992", "cat": "european-sports", "blurb": "Gordon Murray's 1992 central-seat V12, still the fastest naturally aspirated production car at 240.1 mph.", "spec": {"Maker": "McLaren", "Year": "1992", "Speed": "240.1 mph", "Seat": "Central driving position"}, "ref": "McLaren F1 records."}, {"t": "1965 Shelby Cobra 427", "mk": "Shelby", "yr": "1965", "cat": "racing", "blurb": "Carroll Shelby's big-block 1965 Cobra, the Anglo-American brute.", "spec": {"Maker": "Shelby", "Year": "1965", "Engine": "427 big-block V8", "Creator": "Carroll Shelby"}, "ref": "Shelby Cobra history."}, {"t": "1938 Volkswagen Beetle lineage", "mk": "Volkswagen", "yr": "1938", "cat": "pre-war", "blurb": "Ferdinand Porsche's people's car; over 21 million Beetles built, the longest-running single design ever.", "spec": {"Maker": "Volkswagen", "Origin": "1938", "Built": "21+ million", "Designer": "Ferdinand Porsche"}, "ref": "Volkswagen production records."}];
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
