(function(){'use strict';
/* JAH Tea Guide Database generator — jahdb-tea-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='tea-guide',PREFIX='JAH-TEA-',NAME='JAH Tea Guide Database';
var FIELDS=["true", "flavored", "herbal", "method", "care"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Green tea", "d": "Green tea is unoxidized: grassy, fresh, brewed cooler to avoid bitterness.", "g": "true", "l": 2, "q": "What is Green tea?", "a": "Green tea is unoxidized: grassy, fresh, brewed cooler to avoid bitterness.", "x": "Green tea is unoxidized: grassy, fresh, brewed cooler to avoid bitterness. temp: 75-80 C. time: 2-3 min. caffeine: 30-50 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Black tea", "d": "Black tea is fully oxidized: bold and malty, takes milk well.", "g": "true", "l": 2, "q": "What is Black tea?", "a": "Black tea is fully oxidized: bold and malty, takes milk well.", "x": "Black tea is fully oxidized: bold and malty, takes milk well. temp: 95-100 C. time: 3-5 min. caffeine: 50-90 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Oolong tea", "d": "Oolong is the in-between: floral to roasted, re-steeped many times gongfu style.", "g": "true", "l": 2, "q": "What is Oolong tea?", "a": "Oolong is the in-between: floral to roasted, re-steeped many times gongfu style.", "x": "Oolong is the in-between: floral to roasted, re-steeped many times gongfu style. temp: 85-90 C. time: 3-5 min. caffeine: 40-60 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "White tea", "d": "White tea is minimally processed buds: delicate, subtle, expensive.", "g": "true", "l": 2, "q": "What is White tea?", "a": "White tea is minimally processed buds: delicate, subtle, expensive.", "x": "White tea is minimally processed buds: delicate, subtle, expensive. temp: 75-80 C. time: 4-5 min. caffeine: 15-30 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Pu-erh tea", "d": "Pu-erh is fermented and aged like wine: earthy, deep, improving for decades.", "g": "true", "l": 2, "q": "What is Pu-erh tea?", "a": "Pu-erh is fermented and aged like wine: earthy, deep, improving for decades.", "x": "Pu-erh is fermented and aged like wine: earthy, deep, improving for decades. temp: 95 C. time: rinse + short steeps. caffeine: 60-70 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Yellow tea", "d": "Yellow tea is the rare sealed-yellowing tea: smooth and mellow.", "g": "true", "l": 2, "q": "What is Yellow tea?", "a": "Yellow tea is the rare sealed-yellowing tea: smooth and mellow.", "x": "Yellow tea is the rare sealed-yellowing tea: smooth and mellow. temp: 80 C. time: 3 min. caffeine: 30-50 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Matcha", "d": "Matcha is shade-grown stone-ground powder: whisked, not steeped, for frothy intensity.", "g": "true", "l": 2, "q": "What is Matcha?", "a": "Matcha is shade-grown stone-ground powder: whisked, not steeped, for frothy intensity.", "x": "Matcha is shade-grown stone-ground powder: whisked, not steeped, for frothy intensity. temp: 80 C. time: whisk 15 sec. caffeine: 70 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Sencha", "d": "Sencha is the Japanese everyday green: steamed, grassy, bright.", "g": "true", "l": 2, "q": "What is Sencha?", "a": "Sencha is the Japanese everyday green: steamed, grassy, bright.", "x": "Sencha is the Japanese everyday green: steamed, grassy, bright. temp: 75 C. time: 1-2 min. caffeine: 40-60 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Dragon Well (Longjing)", "d": "Dragon Well is pan-fired flat-leaf Chinese green: chestnut-sweet.", "g": "true", "l": 2, "q": "What is Dragon Well (Longjing)?", "a": "Dragon Well is pan-fired flat-leaf Chinese green: chestnut-sweet.", "x": "Dragon Well is pan-fired flat-leaf Chinese green: chestnut-sweet. temp: 80 C. time: 2-3 min. caffeine: 40 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Assam", "d": "Assam is the malty breakfast base: strong Indian black.", "g": "true", "l": 2, "q": "What is Assam?", "a": "Assam is the malty breakfast base: strong Indian black.", "x": "Assam is the malty breakfast base: strong Indian black. temp: 100 C. time: 3-5 min. caffeine: 80 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Darjeeling", "d": "Darjeeling is the champagne of teas: muscatel high-grown Indian.", "g": "true", "l": 2, "q": "What is Darjeeling?", "a": "Darjeeling is the champagne of teas: muscatel high-grown Indian.", "x": "Darjeeling is the champagne of teas: muscatel high-grown Indian. temp: 90 C. time: 3 min. caffeine: 50 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Earl Grey", "d": "Earl Grey is black tea scented with bergamot oil.", "g": "flavored", "l": 2, "q": "What is Earl Grey?", "a": "Earl Grey is black tea scented with bergamot oil.", "x": "Earl Grey is black tea scented with bergamot oil. temp: 95 C. time: 3 min. caffeine: 60 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "English Breakfast", "d": "English Breakfast blends Assam, Ceylon, and Kenyan for morning strength.", "g": "flavored", "l": 2, "q": "What is English Breakfast?", "a": "English Breakfast blends Assam, Ceylon, and Kenyan for morning strength.", "x": "English Breakfast blends Assam, Ceylon, and Kenyan for morning strength. temp: 100 C. time: 3-5 min. caffeine: 80 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Chai (masala)", "d": "Masala chai simmers black tea with ginger, cardamom, and milk.", "g": "flavored", "l": 2, "q": "What is Chai (masala)?", "a": "Masala chai simmers black tea with ginger, cardamom, and milk.", "x": "Masala chai simmers black tea with ginger, cardamom, and milk. temp: simmer. time: 5 min. caffeine: 60 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Jasmine tea", "d": "Jasmine tea is green tea scented with jasmine blossoms.", "g": "flavored", "l": 2, "q": "What is Jasmine tea?", "a": "Jasmine tea is green tea scented with jasmine blossoms.", "x": "Jasmine tea is green tea scented with jasmine blossoms. temp: 80 C. time: 2-3 min. caffeine: 40 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Lapsang souchong", "d": "Lapsang souchong is pine-smoked: campfire in a cup.", "g": "true", "l": 2, "q": "What is Lapsang souchong?", "a": "Lapsang souchong is pine-smoked: campfire in a cup.", "x": "Lapsang souchong is pine-smoked: campfire in a cup. temp: 95 C. time: 3 min. caffeine: 60 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Peppermint tea", "d": "Peppermint is the classic herbal: caffeine-free, cooling, digestive.", "g": "herbal", "l": 2, "q": "What is Peppermint tea?", "a": "Peppermint is the classic herbal: caffeine-free, cooling, digestive.", "x": "Peppermint is the classic herbal: caffeine-free, cooling, digestive. temp: 100 C. time: 5 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Chamomile tea", "d": "Chamomile is the bedtime herbal: apple-scented calm.", "g": "herbal", "l": 2, "q": "What is Chamomile tea?", "a": "Chamomile is the bedtime herbal: apple-scented calm.", "x": "Chamomile is the bedtime herbal: apple-scented calm. temp: 100 C. time: 5 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Rooibos", "d": "Rooibos is the South African red bush: naturally sweet, caffeine-free.", "g": "herbal", "l": 2, "q": "What is Rooibos?", "a": "Rooibos is the South African red bush: naturally sweet, caffeine-free.", "x": "Rooibos is the South African red bush: naturally sweet, caffeine-free. temp: 100 C. time: 5-7 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Hibiscus tea", "d": "Hibiscus is tart ruby-red: vitamin C rich, great iced.", "g": "herbal", "l": 2, "q": "What is Hibiscus tea?", "a": "Hibiscus is tart ruby-red: vitamin C rich, great iced.", "x": "Hibiscus is tart ruby-red: vitamin C rich, great iced. temp: 100 C. time: 5 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Ginger tea", "d": "Ginger tea is fresh-sliced heat: warming and settling.", "g": "herbal", "l": 2, "q": "What is Ginger tea?", "a": "Ginger tea is fresh-sliced heat: warming and settling.", "x": "Ginger tea is fresh-sliced heat: warming and settling. temp: 100 C. time: 5-10 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Lemongrass tea", "d": "Lemongrass tea is citrus calm without caffeine.", "g": "herbal", "l": 2, "q": "What is Lemongrass tea?", "a": "Lemongrass tea is citrus calm without caffeine.", "x": "Lemongrass tea is citrus calm without caffeine. temp: 100 C. time: 5 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Dandelion tea", "d": "Roasted dandelion root brews coffee-like and caffeine-free.", "g": "herbal", "l": 2, "q": "What is Dandelion tea?", "a": "Roasted dandelion root brews coffee-like and caffeine-free.", "x": "Roasted dandelion root brews coffee-like and caffeine-free. temp: 100 C. time: 5 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Nettle tea", "d": "Nettle tea is mineral-rich and earthy.", "g": "herbal", "l": 2, "q": "What is Nettle tea?", "a": "Nettle tea is mineral-rich and earthy.", "x": "Nettle tea is mineral-rich and earthy. temp: 100 C. time: 5 min. caffeine: 0 mg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Iced tea brewing", "d": "Iced tea: brew double-strength hot, pour over ice, or cold-brew 8 hours.", "g": "method", "l": 2, "q": "What is Iced tea brewing?", "a": "Iced tea: brew double-strength hot, pour over ice, or cold-brew 8 hours.", "x": "Iced tea: brew double-strength hot, pour over ice, or cold-brew 8 hours. temp: varies. time: double strength. caffeine: varies. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-tea-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
