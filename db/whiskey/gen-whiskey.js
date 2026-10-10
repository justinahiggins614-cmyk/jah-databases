/* ✳ SIGNATURE — JAH Whiskey Database generator. jahdb-whiskey-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic boundless generator: same seed + version => same record.
   src:"online" = real-world facts with source_ref; src:"fact-checked" = verified claims
   with source_ref and a Signature counterpart; src:"signature" = Signature-authored
   studies, clearly labeled. Every record is a Signature version. */
(function(){
'use strict';
var DBDATA={"meta":{"slug":"whiskey","name":"JAH Whiskey Database","prefix":"JAH-WHISK-","version":"jahdb-whiskey-1.0"},"cats":["scotch","bourbon","irish","japanese","rye","world"],"adj":["Amber","Smoked","Golden","Peated","Honeyed","Oaken","Velvet","Ember","Copper","Malted","Sherry","Bourbon","Highland","Islay","Cask","Single","Double","Triple","Ancient","Noble"],"online":{"scotch":[{"t":"Scotch must age 3 years minimum","d":"Under the Scotch Whisky Regulations 2009, Scotch whisky must be matured in oak casks in Scotland for at least three years.","s":"fact-checked","r":"Scotch Whisky Regulations 2009","sp":{"kind":"scotch","min_age_years":"3","cask":"oak"}},{"t":"The Macallan 1926 — £1.5M","d":"A bottle of The Macallan 1926 60-year-old sold for £1.5 million at Sotheby's London in October 2019, a record for any whisky bottle.","s":"fact-checked","r":"Sotheby's post-sale report, 24 Oct 2019","sp":{"kind":"scotch","distillery":"The Macallan","vintage":"1926","price_gbp":"1,500,000"}},{"t":"Islay — the peat island","d":"Islay's distilleries, including Laphroaig, Lagavulin, and Ardbeg, define heavily peated Scotch, with phenol levels often above 35 ppm.","s":"online","r":"Distillery technical data","sp":{"kind":"scotch","region":"Islay","style":"peated"}}],"bourbon":[{"t":"Bourbon's legal recipe","d":"US federal standards require bourbon to be made in the United States from at least 51% corn and aged in new charred oak containers.","s":"fact-checked","r":"US Standards of Identity for Distilled Spirits (27 CFR 5)","sp":{"kind":"bourbon","corn_min_pct":"51","cask":"new charred oak"}},{"t":"Pappy Van Winkle — the unicorn","d":"Pappy Van Winkle's Family Reserve bourbons, especially the 20- and 23-year-old, routinely trade far above retail on the secondary market.","s":"online","r":"Secondary-market reporting","sp":{"kind":"bourbon","brand":"Pappy Van Winkle"}}],"irish":[{"t":"Irish whiskey's triple distillation","d":"Traditional Irish whiskey is triple-distilled in copper pot stills, giving it a characteristically smooth, light spirit.","s":"online","r":"Irish whiskey technical tradition","sp":{"kind":"irish","distillation":"triple"}},{"t":"Redbreast — single pot still icon","d":"Redbreast, distilled at Midleton, is the benchmark single pot still Irish whiskey, a mash of malted and unmalted barley.","s":"online","r":"Midleton Distillery records","sp":{"kind":"irish","style":"single pot still"}}],"japanese":[{"t":"Yamazaki — Japan's first malt distillery","d":"Yamazaki, founded by Shinjiro Torii in 1923 near Kyoto, was Japan's first malt whisky distillery.","s":"fact-checked","r":"Suntory distillery histories","sp":{"kind":"japanese","founded":"1923"}},{"t":"Japanese whisky sweeps world awards","d":"Yamazaki Sherry Cask 2013 was named the world's best whisky by Jim Murray's Whisky Bible 2015, igniting the Japanese whisky boom.","s":"fact-checked","r":"Whisky Bible 2015","sp":{"kind":"japanese","expression":"Yamazaki Sherry Cask 2013"}}],"rye":[{"t":"Rye's spicy signature","d":"American rye whiskey must be made from at least 51% rye grain, giving it the spicy, peppery profile bartenders prize for classic cocktails.","s":"fact-checked","r":"US Standards of Identity (27 CFR 5)","sp":{"kind":"rye","rye_min_pct":"51"}},{"t":"The Manhattan's whiskey","d":"The classic Manhattan cocktail is built on rye whiskey, sweet vermouth, and bitters — the template for whiskey-forward mixing.","s":"online","r":"Cocktail canon references","sp":{"kind":"rye","cocktail":"Manhattan"}}],"world":[{"t":"Taiwan's Kavalan shocks the world","d":"Kavalan's Solist Vinho Barrique was named world's best single malt at the 2015 World Whiskies Awards, putting Taiwan on the whisky map.","s":"fact-checked","r":"World Whiskies Awards 2015","sp":{"kind":"world","distillery":"Kavalan","country":"Taiwan"}},{"t":"India — the largest whisky market","d":"India is the world's largest whisky-consuming nation by volume, dominated by Indian-made foreign liquor alongside rising single malts like Amrut.","s":"online","r":"Industry volume reporting","sp":{"kind":"world","country":"India"}}]},"sig":{"scotch":{"kind":"tasting study","nouns":["Peat Psalm","Sherry Meridian","Highland Canticle","Malt Ledger","Cask Tide","Spey Engine"],"n1":["the nose opens with heather honey and bonfire smoke over a core of stewed orchard fruit.","the palate is oily and layered, the Signature marker of long, slow distillation.","water opens the dram, lifting citrus oils above the peat."],"n2":["The finish runs long with oak spice and sea salt.","Signature scoring weights cask quality above age statement alone."],"spec":[["region",["Speyside","Islay","Highland","Lowland"]],["age_years",["12","15","18","25"]],["cask",["ex-bourbon","sherry butt","port pipe"]],["abv_pct",["40","43","46","48"]]]},"bourbon":{"kind":"tasting study","nouns":["Corn Psalm","Char Meridian","Barrel Canticle","Mash Ledger","Oak Tide","Kentucky Engine"],"n1":["caramel, vanilla, and toasted oak arrive first, the classic new-char signature.","the high-rye mash bill adds cinnamon and black pepper through the mid-palate.","the chew is rich and coating, built for neat sipping."],"n2":["The finish is warm and lingering with dark cherry.","Small-batch bottlings are graded on barrel-selection consistency."],"spec":[["mash_bill",["high-rye","wheated","traditional"]],["age_years",["6","9","12","15"]],["proof",["90","100","115","125"]],["state",["Kentucky","Tennessee","Texas"]]]},"irish":{"kind":"tasting study","nouns":["Pot Psalm","Triple Meridian","Green Canticle","Barley Ledger","Still Tide","Emerald Engine"],"n1":["triple distillation delivers a silky, fruit-forward spirit with green apple and vanilla.","the pot-still spice builds gently, never harsh, the Irish signature.","sherry-cask finishes add dried fruit depth without weight."],"n2":["The finish is clean and malty with a whisper of spice.","Signature scoring favors distillery character over chill-filtered polish."],"spec":[["style",["single pot still","single malt","blended","single grain"]],["age_years",["10","12","15","21"]],["cask",["ex-bourbon","sherry","rum"]],["abv_pct",["40","43","46","50"]]]},"japanese":{"kind":"tasting study","nouns":["Mizunara Psalm","Kyoto Meridian","Still Canticle","Cedar Ledger","Umami Tide","Nippon Engine"],"n1":["mizunara oak lends incense, sandalwood, and coconut — unmistakably Japanese.","the spirit is precise and elegant, with layers unfolding slowly.","a whisper of smoke frames the fruit rather than covering it."],"n2":["The finish is long, dry, and contemplative.","Mizunara-aged stocks are the scarcest and priced accordingly."],"spec":[["distillery_style",["Yamazaki-style","Yoichi-style","Miyagikyo-style"]],["age_years",["12","18","25","30"]],["cask",["mizunara","sherry","bourbon"]],["abv_pct",["43","45","48","55"]]]},"rye":{"kind":"tasting study","nouns":["Spice Psalm","Pepper Meridian","Grain Canticle","Mash Ledger","Rye Tide","Barrel Engine"],"n1":["cracked pepper, dill, and cinnamon hit first — rye's unmistakable signature.","the mid-palate turns honeyed before the spice returns on the finish.","high-proof bottlings carry the spice without heat."],"n2":["Built for cocktails but complete neat.","The study grades rye content against the 51% legal floor."],"spec":[["rye_pct",["51","75","95","100"]],["age_years",["4","6","10","13"]],["proof",["90","100","110","120"]],["style",["Kentucky rye","Indiana rye","Canadian"]]]},"world":{"kind":"tasting study","nouns":["Tropic Psalm","Highland Meridian","New Canticle","World Ledger","Cask Tide","Global Engine"],"n1":["rapid tropical maturation concentrates flavor fast — angel's share runs high.","the spirit shows maturity beyond its years, the warm-climate signature.","local grain and water give a distinct regional fingerprint."],"n2":["The study adjusts age expectations for climate.","Emerging regions offer the market's best value per flavor unit."],"spec":[["country",["Taiwan","India","Australia","Sweden"]],["age_years",["3","6","10","14"]],["cask",["ex-bourbon","sherry","wine"]],["abv_pct",["40","46","50","57"]]]}}};
var META=DBDATA.meta, CATS=DBDATA.cats;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,arr){return arr[(r()*arr.length)|0];}
var SV='Signature version \u2014 this record is a Signature version in the Signature system.';
function specOf(r,cat,S){var sp={kind:S.kind};(S.spec||[]).forEach(function(f){sp[f[0]]=pick(r,f[1]);});return sp;}
function fromSignature(seed,cat,r){
 var S=DBDATA.sig[cat],adj=pick(r,DBDATA.adj),noun=pick(r,S.nouns);
 var title=adj+' '+noun;
 var desc='A Signature-authored study of '+noun.toLowerCase()+', '+pick(r,S.n1)+' '+pick(r,S.n2)+
 ' Filed as a Signature version in the '+META.name+', '+S.kind+' class.';
 return {id:META.prefix+String(seed).padStart(7,'0'),title:title,description:desc,category:cat,
  src:'signature',signature_version:SV,spec:specOf(r,cat,S),_seed:seed};}
function fromOnline(seed,cat,r,it){
 return {id:META.prefix+String(seed).padStart(7,'0'),title:it.t,description:it.d,category:cat,
  src:it.s,source_ref:it.r,signature_version:SV,spec:it.sp||{kind:cat},_seed:seed};}
function generate(seed,opts,rnd){
 opts=opts||{};seed=seed>>>0;rnd=rnd||prng(seed);
 var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
 var items=DBDATA.online[cat]||[];
 if(items.length&&rnd()<0.35)return fromOnline(seed,cat,rnd,pick(rnd,items));
 return fromSignature(seed,cat,rnd);}
function idOk(id){if(typeof id!=='string')return false;if(id.slice(0,META.prefix.length)!==META.prefix)return false;var d=id.slice(META.prefix.length);if(d.length!==7)return false;for(var i=0;i<7;i++){var ch=d.charCodeAt(i);if(ch<48||ch>57)return false;}return true;}
function validate(rec){
 var e=[];
 if(!rec||typeof rec!=='object')return{ok:false,errors:['not an object']};
 if(!idOk(rec.id))e.push('id format');
 if(typeof rec.title!=='string'||rec.title.length<8)e.push('title');
 if(typeof rec.description!=='string'||rec.description.length<80)e.push('description');
 if(CATS.indexOf(rec.category)<0)e.push('category');
 if(['online','signature','fact-checked'].indexOf(rec.src)<0)e.push('src');
 if(typeof rec.signature_version!=='string'||!rec.signature_version)e.push('signature_version');
 if(rec.src!=='signature'&&typeof rec.source_ref!=='string')e.push('source_ref');
 if(!rec.spec||typeof rec.spec!=='object'||typeof rec.spec.kind!=='string')e.push('spec.kind');
 if(typeof rec._seed!=='number')e.push('_seed');
 return{ok:!e.length,errors:e};}
function driftCheck(rec,sample){
 var e=[];(sample||[]).forEach(function(a){
  var t=a.title||a.t;
  if(t&&String(t).toLowerCase()===String(rec.title).toLowerCase())e.push('duplicate title: '+rec.title);});
 return{ok:!e.length,errors:e};}
var gen={version:META.version,generate:generate,validate:validate,driftCheck:driftCheck,categories:CATS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(META.slug,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
if(typeof require!=='undefined'&&typeof module!=='undefined'&&require.main===module){
 var fails=0,seen={},i,seed,g1,g2,v;
 for(i=0;i<40;i++){seed=1000+i*37;
  g1=generate(seed,{},prng(seed));g2=generate(seed,{},prng(seed));v=validate(g1);
  if(!v.ok){fails++;console.log('FAIL seed '+seed+': '+v.errors.join(','));}
  if(JSON.stringify(g1)!==JSON.stringify(g2)){fails++;console.log('FAIL nondeterministic '+seed);}
  if(g1.src==='signature'){seen[g1.title]=(seen[g1.title]||0)+1;}}
 var dupPairs=0,dupTrip=0;for(var k in seen){if(seen[k]===2)dupPairs++;if(seen[k]>=3)dupTrip++;}
 if(dupPairs>=2||dupTrip>=1){fails++;console.log('FAIL systematic duplicate titles');}
 console.log(fails?('SELF-TEST FAIL '+fails):'SELF-TEST 40/40 PASS');
 process.exit(fails?1:0);}
})();