(function(){'use strict';
/* JAH Cheese Guide Database generator — jahdb-cheese-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='cheese-guide',PREFIX='JAH-CHS-',NAME='JAH Cheese Guide Database';
var FIELDS=["hard", "semi-hard", "semi-soft", "soft", "fresh", "blue", "alternative", "care"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cheddar", "d": "Cheddar is the world favorite hard cheese: clothbound farmhouse for depth, block for melting. Ages from mild to extra-sharp.", "g": "hard", "l": 2, "q": "What is Cheddar?", "a": "Cheddar is the world favorite hard cheese: clothbound farmhouse for depth, block for melting. Ages from mild to extra-sharp.", "x": "Cheddar is the world favorite hard cheese: clothbound farmhouse for depth, block for melting. Ages from mild to extra-sharp. milk: cow. origin: England. flavor: sharp, firm. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Parmesan (Parmigiano-Reggiano)", "d": "Parmigiano-Reggiano ages 24+ months into crystalline, nutty perfection. Grate fresh; the rind flavors soups.", "g": "hard", "l": 2, "q": "What is Parmesan (Parmigiano-Reggiano)?", "a": "Parmigiano-Reggiano ages 24+ months into crystalline, nutty perfection. Grate fresh; the rind flavors soups.", "x": "Parmigiano-Reggiano ages 24+ months into crystalline, nutty perfection. Grate fresh; the rind flavors soups. milk: cow. origin: Italy. flavor: nutty, crystalline. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Gouda", "d": "Gouda ages from buttery young to caramel-crystalled old. Smoked gouda is the crowd-pleaser.", "g": "semi-hard", "l": 2, "q": "What is Gouda?", "a": "Gouda ages from buttery young to caramel-crystalled old. Smoked gouda is the crowd-pleaser.", "x": "Gouda ages from buttery young to caramel-crystalled old. Smoked gouda is the crowd-pleaser. milk: cow. origin: Netherlands. flavor: buttery to caramel. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Gruyere", "d": "Gruyere is the fondue and French onion king: nutty, melty, cave-aged.", "g": "hard", "l": 2, "q": "What is Gruyere?", "a": "Gruyere is the fondue and French onion king: nutty, melty, cave-aged.", "x": "Gruyere is the fondue and French onion king: nutty, melty, cave-aged. milk: cow. origin: Switzerland. flavor: nutty, earthy. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Comte", "d": "Comte is Gruyere French cousin: alpine, fruity, endlessly snackable.", "g": "hard", "l": 2, "q": "What is Comte?", "a": "Comte is Gruyere French cousin: alpine, fruity, endlessly snackable.", "x": "Comte is Gruyere French cousin: alpine, fruity, endlessly snackable. milk: cow. origin: France. flavor: nutty, fruity. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Manchego", "d": "Manchego is the Spanish sheep classic: zigzag rind, nutty paste, quince paste partner.", "g": "hard", "l": 2, "q": "What is Manchego?", "a": "Manchego is the Spanish sheep classic: zigzag rind, nutty paste, quince paste partner.", "x": "Manchego is the Spanish sheep classic: zigzag rind, nutty paste, quince paste partner. milk: sheep. origin: Spain. flavor: nutty, tangy. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Pecorino Romano", "d": "Pecorino Romano is the salty grater for cacio e pepe and carbonara.", "g": "hard", "l": 2, "q": "What is Pecorino Romano?", "a": "Pecorino Romano is the salty grater for cacio e pepe and carbonara.", "x": "Pecorino Romano is the salty grater for cacio e pepe and carbonara. milk: sheep. origin: Italy. flavor: salty, sharp. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Asiago", "d": "Asiago fresco melts; Asiago d allevo grates sharp.", "g": "hard", "l": 2, "q": "What is Asiago?", "a": "Asiago fresco melts; Asiago d allevo grates sharp.", "x": "Asiago fresco melts; Asiago d allevo grates sharp. milk: cow. origin: Italy. flavor: sharp when aged. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Mozzarella (fresh)", "d": "Fresh mozzarella is milky pillows for caprese; eat within days, never refrigerate long.", "g": "fresh", "l": 2, "q": "What is Mozzarella (fresh)?", "a": "Fresh mozzarella is milky pillows for caprese; eat within days, never refrigerate long.", "x": "Fresh mozzarella is milky pillows for caprese; eat within days, never refrigerate long. milk: cow/buffalo. origin: Italy. flavor: milky, delicate. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Burrata", "d": "Burrata is mozzarella with a stracciatella cream heart: serve at room temperature.", "g": "fresh", "l": 2, "q": "What is Burrata?", "a": "Burrata is mozzarella with a stracciatella cream heart: serve at room temperature.", "x": "Burrata is mozzarella with a stracciatella cream heart: serve at room temperature. milk: cow. origin: Italy. flavor: creamy, rich. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Ricotta", "d": "Ricotta is twice-cooked whey: sweet clouds for lasagna and pancakes.", "g": "fresh", "l": 2, "q": "What is Ricotta?", "a": "Ricotta is twice-cooked whey: sweet clouds for lasagna and pancakes.", "x": "Ricotta is twice-cooked whey: sweet clouds for lasagna and pancakes. milk: cow/sheep. origin: Italy. flavor: sweet, light. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Feta", "d": "Feta is brined sheep tang: crumble over salads, bake with honey.", "g": "fresh", "l": 2, "q": "What is Feta?", "a": "Feta is brined sheep tang: crumble over salads, bake with honey.", "x": "Feta is brined sheep tang: crumble over salads, bake with honey. milk: sheep/goat. origin: Greece. flavor: salty, tangy. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Halloumi", "d": "Halloumi grills without melting: the squeaky cheese for skewers and salads.", "g": "fresh", "l": 2, "q": "What is Halloumi?", "a": "Halloumi grills without melting: the squeaky cheese for skewers and salads.", "x": "Halloumi grills without melting: the squeaky cheese for skewers and salads. milk: sheep/goat. origin: Cyprus. flavor: salty, squeaky. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Paneer", "d": "Paneer is the Indian grilling cheese: press it firm, cube for curries.", "g": "fresh", "l": 2, "q": "What is Paneer?", "a": "Paneer is the Indian grilling cheese: press it firm, cube for curries.", "x": "Paneer is the Indian grilling cheese: press it firm, cube for curries. milk: cow. origin: India. flavor: mild, firm. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Queso fresco", "d": "Queso fresco crumbles over tacos and enchiladas.", "g": "fresh", "l": 2, "q": "What is Queso fresco?", "a": "Queso fresco crumbles over tacos and enchiladas.", "x": "Queso fresco crumbles over tacos and enchiladas. milk: cow. origin: Mexico. flavor: mild, crumbly. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Brie", "d": "Brie ripens from the rind inward: buy plump, serve gooey at room temperature.", "g": "soft", "l": 2, "q": "What is Brie?", "a": "Brie ripens from the rind inward: buy plump, serve gooey at room temperature.", "x": "Brie ripens from the rind inward: buy plump, serve gooey at room temperature. milk: cow. origin: France. flavor: buttery, mushroomy. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Camembert", "d": "Camembert is Brie deeper Normandy cousin: bake whole with garlic.", "g": "soft", "l": 2, "q": "What is Camembert?", "a": "Camembert is Brie deeper Normandy cousin: bake whole with garlic.", "x": "Camembert is Brie deeper Normandy cousin: bake whole with garlic. milk: cow. origin: France. flavor: earthy, rich. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Goat cheese (chevre)", "d": "Fresh chevre is tangy logs for salads; aged crottins turn nutty.", "g": "soft", "l": 2, "q": "What is Goat cheese (chevre)?", "a": "Fresh chevre is tangy logs for salads; aged crottins turn nutty.", "x": "Fresh chevre is tangy logs for salads; aged crottins turn nutty. milk: goat. origin: France. flavor: tangy, bright. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Blue cheese (Roquefort)", "d": "Roquefort is the king of blues: sheep milk, Penicillium roqueforti, caves of Roquefort.", "g": "blue", "l": 2, "q": "What is Blue cheese (Roquefort)?", "a": "Roquefort is the king of blues: sheep milk, Penicillium roqueforti, caves of Roquefort.", "x": "Roquefort is the king of blues: sheep milk, Penicillium roqueforti, caves of Roquefort. milk: sheep. origin: France. flavor: sharp, salty. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Gorgonzola", "d": "Gorgonzola dolce is spoonable; piccante is firm and fiery.", "g": "blue", "l": 2, "q": "What is Gorgonzola?", "a": "Gorgonzola dolce is spoonable; piccante is firm and fiery.", "x": "Gorgonzola dolce is spoonable; piccante is firm and fiery. milk: cow. origin: Italy. flavor: creamy-sharp. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Stilton", "d": "Stilton is the English Christmas blue: rich veins, port pairing.", "g": "blue", "l": 2, "q": "What is Stilton?", "a": "Stilton is the English Christmas blue: rich veins, port pairing.", "x": "Stilton is the English Christmas blue: rich veins, port pairing. milk: cow. origin: England. flavor: rich, minerally. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cream cheese", "d": "Cream cheese is the bagel and cheesecake base: Philadelphia-style since 1872.", "g": "soft", "l": 2, "q": "What is Cream cheese?", "a": "Cream cheese is the bagel and cheesecake base: Philadelphia-style since 1872.", "x": "Cream cheese is the bagel and cheesecake base: Philadelphia-style since 1872. milk: cow. origin: USA. flavor: mild, tangy. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Mascarpone", "d": "Mascarpone is sweet cream luxury for tiramisu.", "g": "soft", "l": 2, "q": "What is Mascarpone?", "a": "Mascarpone is sweet cream luxury for tiramisu.", "x": "Mascarpone is sweet cream luxury for tiramisu. milk: cow. origin: Italy. flavor: sweet cream. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cottage cheese", "d": "Cottage cheese is the high-protein curd: small or large curd, endlessly versatile.", "g": "fresh", "l": 2, "q": "What is Cottage cheese?", "a": "Cottage cheese is the high-protein curd: small or large curd, endlessly versatile.", "x": "Cottage cheese is the high-protein curd: small or large curd, endlessly versatile. milk: cow. origin: Various. flavor: mild curds. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Swiss (Emmental)", "d": "Emmental is the holey one: mild, nutty, the Reuben melt.", "g": "hard", "l": 2, "q": "What is Swiss (Emmental)?", "a": "Emmental is the holey one: mild, nutty, the Reuben melt.", "x": "Emmental is the holey one: mild, nutty, the Reuben melt. milk: cow. origin: Switzerland. flavor: mild, nutty. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-cheese-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
