/* ✳ SIGNATURE — JAH Sneaker Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-SNK-0000001 .. JAH-SNK-1000000). Browser: registers with JAHDB. Node:
   run `node gen-sneakers.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='sneakers', PREFIX='JAH-SNK-', VERSION='jahdb-sneakers-1.0';
var KIND='sneaker', AI='JAH Sneaker Creator';
var CATEGORIES=["basketball", "running", "skate", "lifestyle", "tennis", "trail"];
var MAKERS=["Stride Signature", "JAH Footworks", "Velocity Kicks", "Apex Court Co.", "Drift Footwear", "Kinetic Soles", "Paragon Sneaker Atelier", "Flux Footwear", "Summit Stride", "Cipher Kicks", "Nova Tread", "Ember Footworks"], LINES=["Court Legend", "Street Icon", "Runner Prime", "Heritage High", "Velocity Low", "Trail Forge", "Metro Knit", "Retro Wave", "Apex Mid", "Origin"], WORDS=["a responsive foam midsole", "full-grain leather panels", "a breathable engineered knit", "a herringbone traction outsole", "reflective night detailing", "a sculpted heel counter", "premium suede overlays", "a cushioned collar lining"], DESCS=["Runner", "High-Top", "Low-Top", "Court Classic", "Trail", "Skate", "Knit", "Retro", "Mid", "Slip-On", "Trainer", "Hoop"];
var SPEC_KEYS=["Upper", "Midsole", "Outsole", "Closure", "Weight (US 9)", "Best for"], SPEC_VALS=[["full-grain leather", "engineered mesh", "premium suede", "recycled knit"], ["EVA foam", "dual-density foam", "air-cushioned", "gel-infused"], ["rubber herringbone", "gum rubber", "lugged trail rubber", "cupsole rubber"], ["flat laces", "quick-lace", "elastic slip-on", "strap + laces"], ["280 g", "310 g", "340 g", "390 g"], ["daily wear", "court play", "distance running", "skate sessions"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Nike Air Jordan 1 High OG", "mk": "Nike", "yr": "1985", "cat": "basketball", "blurb": "Designed by Peter Moore for Michael Jordan's rookie season, the shoe that launched sneaker culture.", "spec": {"Designer": "Peter Moore", "Debut": "1985", "Athlete": "Michael Jordan", "Legacy": "Origin of sneaker culture"}, "ref": "Nike Air Jordan 1 history, 1985; Peter Moore design."}, {"t": "Nike Air Force 1", "mk": "Nike", "yr": "1982", "cat": "basketball", "blurb": "Bruce Kilgore's 1982 design, the first basketball shoe with Nike Air, later a streetwear staple.", "spec": {"Designer": "Bruce Kilgore", "Debut": "1982", "Innovation": "First Nike Air in basketball", "Legacy": "Streetwear icon"}, "ref": "Nike Air Force 1 history, 1982."}, {"t": "Adidas Superstar", "mk": "Adidas", "yr": "1969", "cat": "basketball", "blurb": "The 1969 shell-toe basketball shoe adopted by Run-DMC in the 1980s, bridging sport and hip-hop.", "spec": {"Debut": "1969", "Signature": "Rubber shell toe", "Culture": "Run-DMC, 1980s hip-hop", "Sport": "Basketball"}, "ref": "Adidas Superstar history, 1969."}, {"t": "Converse Chuck Taylor All Star", "mk": "Converse", "yr": "1917", "cat": "lifestyle", "blurb": "Introduced in 1917 and signed by Chuck Taylor in 1923, the best-selling basketball shoe of all time.", "spec": {"Debut": "1917", "Endorsement": "Chuck Taylor, 1923", "Design": "Canvas high-top", "Legacy": "Best-selling basketball shoe ever"}, "ref": "Converse Chuck Taylor All Star history."}, {"t": "New Balance 990", "mk": "New Balance", "yr": "1982", "cat": "running", "blurb": "Launched in 1982 at $100 — the most expensive running shoe of its day — and made in the USA/UK ever since.", "spec": {"Debut": "1982", "Price then": "$100", "Made in": "USA", "Legacy": "Premium running heritage"}, "ref": "New Balance 990 history, 1982."}, {"t": "Vans Old Skool", "mk": "Vans", "yr": "1977", "cat": "skate", "blurb": "The 1977 debut of the Sidestripe, Vans' first shoe with leather panels, built for skateboarding.", "spec": {"Debut": "1977", "Signature": "Sidestripe", "Sport": "Skateboarding", "Construction": "Canvas and suede"}, "ref": "Vans Old Skool history, 1977."}, {"t": "Puma Suede Classic", "mk": "Puma", "yr": "1968", "cat": "lifestyle", "blurb": "Worn by Tommie Smith on the 1968 Olympic podium, the Suede became a b-boy and hip-hop staple.", "spec": {"Debut": "1968", "Moment": "1968 Olympics podium", "Culture": "B-boy/hip-hop icon", "Upper": "Suede"}, "ref": "Puma Suede history, 1968."}, {"t": "Reebok Classic Leather", "mk": "Reebok", "yr": "1983", "cat": "lifestyle", "blurb": "The 1983 garment-leather classic that defined 1980s casual style on both sides of the Atlantic.", "spec": {"Debut": "1983", "Upper": "Garment leather", "Era": "1980s casual icon", "Origin": "UK/US"}, "ref": "Reebok Classic Leather history, 1983."}, {"t": "Nike Dunk Low", "mk": "Nike", "yr": "1985", "cat": "skate", "blurb": "The 1985 college basketball shoe reborn through skateboarding and streetwear in the 2000s.", "spec": {"Debut": "1985", "Program": "\"Be True To Your School\"", "Rebirth": "SB line, 2002", "Culture": "Skate/streetwear"}, "ref": "Nike Dunk history, 1985."}, {"t": "Nike Air Max 1", "mk": "Nike", "yr": "1987", "cat": "lifestyle", "blurb": "Tinker Hatfield's 1987 design with the first visible Air unit, inspired by the Pompidou Centre.", "spec": {"Designer": "Tinker Hatfield", "Debut": "1987", "Innovation": "Visible Air unit", "Inspiration": "Pompidou Centre"}, "ref": "Nike Air Max 1 history, 1987."}, {"t": "Adidas Stan Smith", "mk": "Adidas", "yr": "1965", "cat": "tennis", "blurb": "The 1965 tennis shoe renamed for Stan Smith in 1971, among the best-selling sneakers ever made.", "spec": {"Debut": "1965", "Namesake": "Stan Smith, 1971", "Sport": "Tennis", "Sales": "Among best-selling ever"}, "ref": "Adidas Stan Smith history."}, {"t": "Adidas Samba", "mk": "Adidas", "yr": "1950", "cat": "lifestyle", "blurb": "Designed in 1950 for icy football pitches, the Samba became a terrace and streetwear classic.", "spec": {"Debut": "1950", "Purpose": "Icy football pitches", "Signature": "T-toe suede overlay", "Culture": "Terrace classic"}, "ref": "Adidas Samba history, 1950."}, {"t": "Nike Cortez", "mk": "Nike", "yr": "1972", "cat": "running", "blurb": "Bill Bowerman's 1972 design, Nike's first track shoe and a West Coast cultural icon.", "spec": {"Designer": "Bill Bowerman", "Debut": "1972", "First": "Nike's first track shoe", "Culture": "West Coast icon"}, "ref": "Nike Cortez history, 1972."}, {"t": "Nike Air Jordan 11", "mk": "Nike", "yr": "1995", "cat": "basketball", "blurb": "Tinker Hatfield's patent-leather 1995 design, worn by Jordan during the 72-10 championship season.", "spec": {"Designer": "Tinker Hatfield", "Debut": "1995", "Signature": "Patent leather", "Season": "72-10 Bulls championship"}, "ref": "Nike Air Jordan 11 history, 1995."}, {"t": "Nike Air Jordan 3", "mk": "Nike", "yr": "1988", "cat": "basketball", "blurb": "The 1988 elephant-print design that kept Jordan at Nike, introducing the Jumpman logo.", "spec": {"Designer": "Tinker Hatfield", "Debut": "1988", "First": "Jumpman logo", "Legacy": "Saved the Jordan line"}, "ref": "Nike Air Jordan 3 history, 1988."}, {"t": "Reebok Pump", "mk": "Reebok", "yr": "1989", "cat": "basketball", "blurb": "The 1989 inflatable-bladder shoe that let wearers \"pump up\" the fit, an icon of early-90s tech.", "spec": {"Debut": "1989", "Innovation": "Inflatable Pump bladder", "Era": "Early-90s tech icon", "Sport": "Basketball"}, "ref": "Reebok Pump history, 1989."}, {"t": "Adidas Yeezy Boost 350", "mk": "Adidas", "yr": "2015", "cat": "lifestyle", "blurb": "Kanye West's 2015 Primeknit and Boost collaboration that reshaped sneaker resale culture.", "spec": {"Debut": "2015", "Designer": "Kanye West", "Tech": "Primeknit, Boost foam", "Impact": "Reshaped resale culture"}, "ref": "Adidas Yeezy Boost 350 history, 2015."}, {"t": "New Balance 550", "mk": "New Balance", "yr": "1989", "cat": "basketball", "blurb": "The 1989 basketball shoe revived in 2020, becoming a retro-court staple.", "spec": {"Debut": "1989", "Revival": "2020", "Sport": "Basketball", "Style": "Retro court"}, "ref": "New Balance 550 history."}, {"t": "Nike Air Max 90", "mk": "Nike", "yr": "1990", "cat": "lifestyle", "blurb": "Tinker Hatfield's 1990 Air Max III, rebranded the Air Max 90, with its unmistakable infrared colorway.", "spec": {"Designer": "Tinker Hatfield", "Debut": "1990", "Colorway": "Infrared", "Line": "Air Max"}, "ref": "Nike Air Max 90 history, 1990."}, {"t": "Asics Gel-Kayano", "mk": "Asics", "yr": "1993", "cat": "running", "blurb": "Toshikazu Kayano's 1993 stability flagship, a reference point in running shoes for three decades.", "spec": {"Designer": "Toshikazu Kayano", "Debut": "1993", "Type": "Stability running", "Legacy": "30+ year lineage"}, "ref": "Asics Gel-Kayano history, 1993."}, {"t": "Saucony Jazz Original", "mk": "Saucony", "yr": "1981", "cat": "running", "blurb": "The 1981 runner whose triangle-wave branding became a retro lifestyle favorite.", "spec": {"Debut": "1981", "Signature": "Triangle wave", "Type": "Running", "Style": "Retro lifestyle"}, "ref": "Saucony Jazz history, 1981."}, {"t": "Nike Blazer Mid", "mk": "Nike", "yr": "1973", "cat": "skate", "blurb": "The 1973 basketball shoe named for the Portland Trail Blazers, later adopted by skateboarders.", "spec": {"Debut": "1973", "Namesake": "Portland Trail Blazers", "Adopted by": "Skateboarding", "Style": "Vulc-soled classic"}, "ref": "Nike Blazer history, 1973."}, {"t": "Ewing 33 Hi", "mk": "Ewing Athletics", "yr": "1989", "cat": "basketball", "blurb": "Patrick Ewing's 1989 signature shoe, the first from an athlete-owned brand.", "spec": {"Debut": "1989", "Athlete": "Patrick Ewing", "First": "Athlete-owned brand shoe", "Sport": "Basketball"}, "ref": "Ewing 33 Hi history, 1989."}, {"t": "Adidas NMD_R1", "mk": "Adidas", "yr": "2015", "cat": "lifestyle", "blurb": "The 2015 \"nomad\" silhouette pairing Boost cushioning with retro runner plugs.", "spec": {"Debut": "2015", "Tech": "Boost midsole", "Signature": "EVA plugs", "Style": "Street nomad"}, "ref": "Adidas NMD history, 2015."}];
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
