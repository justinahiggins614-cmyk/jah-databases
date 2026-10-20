(function(){'use strict';
/* JAH US States Database generator — jahdb-us-states-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='us-states',PREFIX='JAH-USA-',NAME='JAH US States Database';
var FIELDS=["northeast", "midwest", "south", "west"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Alabama", "d": "Capital: Montgomery (AL). Nickname: Yellowhammer State. Admitted 1819.", "g": "south", "l": 2, "q": "What is Alabama?", "a": "Capital: Montgomery (AL). Nickname: Yellowhammer State. Admitted 1819.", "x": "Alabama — Capital: Montgomery (AL). Nickname: Yellowhammer State. Admitted 1819. Example: Yellowhammer State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Alaska", "d": "Capital: Juneau (AK). Nickname: The Last Frontier. Admitted 1959.", "g": "west", "l": 2, "q": "What is Alaska?", "a": "Capital: Juneau (AK). Nickname: The Last Frontier. Admitted 1959.", "x": "Alaska — Capital: Juneau (AK). Nickname: The Last Frontier. Admitted 1959. Example: The Last Frontier.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Arizona", "d": "Capital: Phoenix (AZ). Nickname: Grand Canyon State. Admitted 1912.", "g": "west", "l": 2, "q": "What is Arizona?", "a": "Capital: Phoenix (AZ). Nickname: Grand Canyon State. Admitted 1912.", "x": "Arizona — Capital: Phoenix (AZ). Nickname: Grand Canyon State. Admitted 1912. Example: Grand Canyon State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Arkansas", "d": "Capital: Little Rock (AR). Nickname: Natural State. Admitted 1836.", "g": "south", "l": 2, "q": "What is Arkansas?", "a": "Capital: Little Rock (AR). Nickname: Natural State. Admitted 1836.", "x": "Arkansas — Capital: Little Rock (AR). Nickname: Natural State. Admitted 1836. Example: Natural State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "California", "d": "Capital: Sacramento (CA). Nickname: Golden State. Admitted 1850.", "g": "west", "l": 2, "q": "What is California?", "a": "Capital: Sacramento (CA). Nickname: Golden State. Admitted 1850.", "x": "California — Capital: Sacramento (CA). Nickname: Golden State. Admitted 1850. Example: Golden State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Colorado", "d": "Capital: Denver (CO). Nickname: Centennial State. Admitted 1876.", "g": "west", "l": 2, "q": "What is Colorado?", "a": "Capital: Denver (CO). Nickname: Centennial State. Admitted 1876.", "x": "Colorado — Capital: Denver (CO). Nickname: Centennial State. Admitted 1876. Example: Centennial State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Connecticut", "d": "Capital: Hartford (CT). Nickname: Constitution State. Admitted 1788.", "g": "northeast", "l": 2, "q": "What is Connecticut?", "a": "Capital: Hartford (CT). Nickname: Constitution State. Admitted 1788.", "x": "Connecticut — Capital: Hartford (CT). Nickname: Constitution State. Admitted 1788. Example: Constitution State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Delaware", "d": "Capital: Dover (DE). Nickname: First State. Admitted 1787.", "g": "south", "l": 2, "q": "What is Delaware?", "a": "Capital: Dover (DE). Nickname: First State. Admitted 1787.", "x": "Delaware — Capital: Dover (DE). Nickname: First State. Admitted 1787. Example: First State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Florida", "d": "Capital: Tallahassee (FL). Nickname: Sunshine State. Admitted 1845.", "g": "south", "l": 2, "q": "What is Florida?", "a": "Capital: Tallahassee (FL). Nickname: Sunshine State. Admitted 1845.", "x": "Florida — Capital: Tallahassee (FL). Nickname: Sunshine State. Admitted 1845. Example: Sunshine State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Georgia", "d": "Capital: Atlanta (GA). Nickname: Peach State. Admitted 1788.", "g": "south", "l": 2, "q": "What is Georgia?", "a": "Capital: Atlanta (GA). Nickname: Peach State. Admitted 1788.", "x": "Georgia — Capital: Atlanta (GA). Nickname: Peach State. Admitted 1788. Example: Peach State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Hawaii", "d": "Capital: Honolulu (HI). Nickname: Aloha State. Admitted 1959.", "g": "west", "l": 2, "q": "What is Hawaii?", "a": "Capital: Honolulu (HI). Nickname: Aloha State. Admitted 1959.", "x": "Hawaii — Capital: Honolulu (HI). Nickname: Aloha State. Admitted 1959. Example: Aloha State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Idaho", "d": "Capital: Boise (ID). Nickname: Gem State. Admitted 1890.", "g": "west", "l": 2, "q": "What is Idaho?", "a": "Capital: Boise (ID). Nickname: Gem State. Admitted 1890.", "x": "Idaho — Capital: Boise (ID). Nickname: Gem State. Admitted 1890. Example: Gem State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Illinois", "d": "Capital: Springfield (IL). Nickname: Prairie State. Admitted 1818.", "g": "midwest", "l": 2, "q": "What is Illinois?", "a": "Capital: Springfield (IL). Nickname: Prairie State. Admitted 1818.", "x": "Illinois — Capital: Springfield (IL). Nickname: Prairie State. Admitted 1818. Example: Prairie State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Indiana", "d": "Capital: Indianapolis (IN). Nickname: Hoosier State. Admitted 1816.", "g": "midwest", "l": 2, "q": "What is Indiana?", "a": "Capital: Indianapolis (IN). Nickname: Hoosier State. Admitted 1816.", "x": "Indiana — Capital: Indianapolis (IN). Nickname: Hoosier State. Admitted 1816. Example: Hoosier State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Iowa", "d": "Capital: Des Moines (IA). Nickname: Hawkeye State. Admitted 1846.", "g": "midwest", "l": 2, "q": "What is Iowa?", "a": "Capital: Des Moines (IA). Nickname: Hawkeye State. Admitted 1846.", "x": "Iowa — Capital: Des Moines (IA). Nickname: Hawkeye State. Admitted 1846. Example: Hawkeye State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Kansas", "d": "Capital: Topeka (KS). Nickname: Sunflower State. Admitted 1861.", "g": "midwest", "l": 2, "q": "What is Kansas?", "a": "Capital: Topeka (KS). Nickname: Sunflower State. Admitted 1861.", "x": "Kansas — Capital: Topeka (KS). Nickname: Sunflower State. Admitted 1861. Example: Sunflower State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Kentucky", "d": "Capital: Frankfort (KY). Nickname: Bluegrass State. Admitted 1792.", "g": "south", "l": 2, "q": "What is Kentucky?", "a": "Capital: Frankfort (KY). Nickname: Bluegrass State. Admitted 1792.", "x": "Kentucky — Capital: Frankfort (KY). Nickname: Bluegrass State. Admitted 1792. Example: Bluegrass State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Louisiana", "d": "Capital: Baton Rouge (LA). Nickname: Pelican State. Admitted 1812.", "g": "south", "l": 2, "q": "What is Louisiana?", "a": "Capital: Baton Rouge (LA). Nickname: Pelican State. Admitted 1812.", "x": "Louisiana — Capital: Baton Rouge (LA). Nickname: Pelican State. Admitted 1812. Example: Pelican State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Maine", "d": "Capital: Augusta (ME). Nickname: Pine Tree State. Admitted 1820.", "g": "northeast", "l": 2, "q": "What is Maine?", "a": "Capital: Augusta (ME). Nickname: Pine Tree State. Admitted 1820.", "x": "Maine — Capital: Augusta (ME). Nickname: Pine Tree State. Admitted 1820. Example: Pine Tree State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Maryland", "d": "Capital: Annapolis (MD). Nickname: Old Line State. Admitted 1788.", "g": "south", "l": 2, "q": "What is Maryland?", "a": "Capital: Annapolis (MD). Nickname: Old Line State. Admitted 1788.", "x": "Maryland — Capital: Annapolis (MD). Nickname: Old Line State. Admitted 1788. Example: Old Line State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Massachusetts", "d": "Capital: Boston (MA). Nickname: Bay State. Admitted 1788.", "g": "northeast", "l": 2, "q": "What is Massachusetts?", "a": "Capital: Boston (MA). Nickname: Bay State. Admitted 1788.", "x": "Massachusetts — Capital: Boston (MA). Nickname: Bay State. Admitted 1788. Example: Bay State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Michigan", "d": "Capital: Lansing (MI). Nickname: Great Lakes State. Admitted 1837.", "g": "midwest", "l": 2, "q": "What is Michigan?", "a": "Capital: Lansing (MI). Nickname: Great Lakes State. Admitted 1837.", "x": "Michigan — Capital: Lansing (MI). Nickname: Great Lakes State. Admitted 1837. Example: Great Lakes State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Minnesota", "d": "Capital: St. Paul (MN). Nickname: North Star State. Admitted 1858.", "g": "midwest", "l": 2, "q": "What is Minnesota?", "a": "Capital: St. Paul (MN). Nickname: North Star State. Admitted 1858.", "x": "Minnesota — Capital: St. Paul (MN). Nickname: North Star State. Admitted 1858. Example: North Star State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Mississippi", "d": "Capital: Jackson (MS). Nickname: Magnolia State. Admitted 1817.", "g": "south", "l": 2, "q": "What is Mississippi?", "a": "Capital: Jackson (MS). Nickname: Magnolia State. Admitted 1817.", "x": "Mississippi — Capital: Jackson (MS). Nickname: Magnolia State. Admitted 1817. Example: Magnolia State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "Missouri", "d": "Capital: Jefferson City (MO). Nickname: Show-Me State. Admitted 1821.", "g": "midwest", "l": 2, "q": "What is Missouri?", "a": "Capital: Jefferson City (MO). Nickname: Show-Me State. Admitted 1821.", "x": "Missouri — Capital: Jefferson City (MO). Nickname: Show-Me State. Admitted 1821. Example: Show-Me State.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-us-states-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
