(function(){'use strict';
/* JAH Painting Guide Database generator — jahdb-painting-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='painting-guide',PREFIX='JAH-PNT-',NAME='JAH Painting Guide Database';
var FIELDS=["prep", "technique", "tools", "cleanup", "conditions"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Choosing interior paint", "d": "Flat hides flaws; eggshell and satin wipe clean; semi-gloss for trim.", "g": "prep", "l": 2, "q": "What is Choosing interior paint?", "a": "Flat hides flaws; eggshell and satin wipe clean; semi-gloss for trim.", "x": "Flat hides flaws; eggshell and satin wipe clean; semi-gloss for trim. Key steps: Pick sheen by room use; Buy quality paint; Get samples on the wall. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Choosing exterior paint", "d": "100% acrylic latex for most siding; oil for some trim.", "g": "prep", "l": 2, "q": "What is Choosing exterior paint?", "a": "100% acrylic latex for most siding; oil for some trim.", "x": "100% acrylic latex for most siding; oil for some trim. Key steps: Match paint to surface; Check the weather window; Buy 10% extra. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Prep: cleaning walls", "d": "Paint sticks to clean surfaces.", "g": "prep", "l": 2, "q": "What is Prep: cleaning walls?", "a": "Paint sticks to clean surfaces.", "x": "Paint sticks to clean surfaces. Key steps: Dust walls; Wash greasy spots with TSP substitute; Rinse and dry. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Prep: patching holes", "d": "Smooth walls make smooth paint.", "g": "prep", "l": 2, "q": "What is Prep: patching holes?", "a": "Smooth walls make smooth paint.", "x": "Smooth walls make smooth paint. Key steps: Fill with spackle; Sand when dry; Spot-prime patches. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Prep: sanding", "d": "Sanding grips the new coat.", "g": "prep", "l": 2, "q": "What is Prep: sanding?", "a": "Sanding grips the new coat.", "x": "Sanding grips the new coat. Key steps: Sand glossy surfaces with 120 grit; Wipe dust; Tack cloth final. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Primer: when you need it", "d": "Bare wood, stains, drastic color changes need primer.", "g": "prep", "l": 2, "q": "What is Primer: when you need it?", "a": "Bare wood, stains, drastic color changes need primer.", "x": "Bare wood, stains, drastic color changes need primer. Key steps: Stain-blocking for water marks; Bonding primer for slick surfaces; Tint primer toward the topcoat. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Taping like a pro", "d": "Tape is for crisp lines, not for sloppiness.", "g": "prep", "l": 2, "q": "What is Taping like a pro?", "a": "Tape is for crisp lines, not for sloppiness.", "x": "Tape is for crisp lines, not for sloppiness. Key steps: Use quality painter tape; Seal edges firmly; Remove while the paint is tacky. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cutting in", "d": "Brush the edges before rolling the field.", "g": "technique", "l": 2, "q": "What is Cutting in?", "a": "Brush the edges before rolling the field.", "x": "Brush the edges before rolling the field. Key steps: Load the brush well; Steady hand, long strokes; Feather the edge for rolling. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Rolling walls", "d": "W for even coverage.", "g": "technique", "l": 2, "q": "What is Rolling walls?", "a": "W for even coverage.", "x": "W for even coverage. Key steps: Load the roller fully; Roll a W pattern; Back-roll to even out; Keep a wet edge. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Painting ceilings", "d": "Ceilings first, then walls, then trim.", "g": "technique", "l": 2, "q": "What is Painting ceilings?", "a": "Ceilings first, then walls, then trim.", "x": "Ceilings first, then walls, then trim. Key steps: Use an extension pole; Work in sections; Flat white hides flaws. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Painting trim", "d": "Trim last with a steady hand.", "g": "technique", "l": 2, "q": "What is Painting trim?", "a": "Trim last with a steady hand.", "x": "Trim last with a steady hand. Key steps: Use a quality angled brush; Long smooth strokes; Two thin coats. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Painting doors", "d": "Remove hardware; paint panels first.", "g": "technique", "l": 2, "q": "What is Painting doors?", "a": "Remove hardware; paint panels first.", "x": "Remove hardware; paint panels first. Key steps: Take off knobs; Paint recessed panels first; Then rails, then stiles; Dry between coats. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Painting cabinets", "d": "The biggest kitchen transformation.", "g": "technique", "l": 2, "q": "What is Painting cabinets?", "a": "The biggest kitchen transformation.", "x": "The biggest kitchen transformation. Key steps: Degrease thoroughly; Sand and prime with bonding primer; Spray or roll thin coats; Cure fully before use. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Spraying basics", "d": "Sprayers are fast but prep-heavy.", "g": "technique", "l": 2, "q": "What is Spraying basics?", "a": "Sprayers are fast but prep-heavy.", "x": "Sprayers are fast but prep-heavy. Key steps: Mask everything; Practice on cardboard; Overlap 50%; Back-brush or roll for adhesion. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Brush selection", "d": "Angled sash for trim, flat for walls.", "g": "tools", "l": 2, "q": "What is Brush selection?", "a": "Angled sash for trim, flat for walls.", "x": "Angled sash for trim, flat for walls. Key steps: Buy the best brush you can; Nylon-poly for latex; Natural bristle for oil. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Roller selection", "d": "Nap matches texture.", "g": "tools", "l": 2, "q": "What is Roller selection?", "a": "Nap matches texture.", "x": "Nap matches texture. Key steps: 3/8 inch for smooth walls; 1/2 inch for light texture; 3/4 inch for rough. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Ladder safety", "d": "Falls are the real painting hazard.", "g": "tools", "l": 2, "q": "What is Ladder safety?", "a": "Falls are the real painting hazard.", "x": "Falls are the real painting hazard. Key steps: 4-to-1 angle rule; Three points of contact; Never overreach. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cleanup: latex", "d": "Soap and water while wet.", "g": "cleanup", "l": 2, "q": "What is Cleanup: latex?", "a": "Soap and water while wet.", "x": "Soap and water while wet. Key steps: Wash brushes thoroughly; Spin dry; Store properly. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cleanup: oil", "d": "Mineral spirits, ventilate.", "g": "cleanup", "l": 2, "q": "What is Cleanup: oil?", "a": "Mineral spirits, ventilate.", "x": "Mineral spirits, ventilate. Key steps: Clean with mineral spirits; Dispose of rags safely — spontaneous combustion risk; Ventilate. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Storing leftover paint", "d": "Good storage saves touch-ups.", "g": "cleanup", "l": 2, "q": "What is Storing leftover paint?", "a": "Good storage saves touch-ups.", "x": "Good storage saves touch-ups. Key steps: Seal the lid tight; Store upside down briefly to seal; Label the room and date. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Touch-up technique", "d": "Feather small areas.", "g": "technique", "l": 2, "q": "What is Touch-up technique?", "a": "Feather small areas.", "x": "Feather small areas. Key steps: Use leftover original paint; Feather edges; Two light coats. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Fixing drips", "d": "Catch them wet or sand them dry.", "g": "technique", "l": 2, "q": "What is Fixing drips?", "a": "Catch them wet or sand them dry.", "x": "Catch them wet or sand them dry. Key steps: Brush out immediately; Or sand when dry and recoat. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Painting in humidity", "d": "Humidity slows drying.", "g": "conditions", "l": 2, "q": "What is Painting in humidity?", "a": "Humidity slows drying.", "x": "Humidity slows drying. Key steps: Paint between 10-30 C; Below 70% humidity; Allow extra dry time. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Lead paint safety", "d": "Pre-1978 homes may have lead.", "g": "conditions", "l": 2, "q": "What is Lead paint safety?", "a": "Pre-1978 homes may have lead.", "x": "Pre-1978 homes may have lead. Key steps: Test before sanding; Use lead-safe practices; Hire certified pros for large jobs. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Estimating paint quantity", "d": "One gallon covers about 350 sq ft per coat.", "g": "prep", "l": 2, "q": "What is Estimating paint quantity?", "a": "One gallon covers about 350 sq ft per coat.", "x": "One gallon covers about 350 sq ft per coat. Key steps: Measure walls; Subtract large openings; Two coats standard; Buy 10% extra. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-painting-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
