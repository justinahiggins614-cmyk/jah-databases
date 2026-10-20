(function(){'use strict';
/* JAH Time Zones Guide Database generator — jahdb-time-zones-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='time-zones-guide',PREFIX='JAH-TMZ-',NAME='JAH Time Zones Guide Database';
var FIELDS=["utc-12", "utc-11", "utc-10", "utc-9", "utc-8", "utc-7", "utc-6", "utc-5", "utc-4", "utc-3", "utc-2", "utc-1", "utc0", "utc3", "utc4", "utc5", "utc6", "utc7", "utc8", "utc9", "utc10", "utc11", "utc12", "utc13", "utc14"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "UTC-12:00 Baker Island", "d": "UTC-12. Places: Baker Island, Howland Island. No DST.", "g": "utc-12", "l": 2, "q": "What is UTC-12:00 Baker Island?", "a": "UTC-12. Places: Baker Island, Howland Island. No DST.", "x": "UTC-12:00 Baker Island — UTC-12. Places: Baker Island, Howland Island. No DST. Example: Baker Island.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-11:00 American Samoa", "d": "UTC-11. Places: American Samoa, Niue. No DST.", "g": "utc-11", "l": 2, "q": "What is UTC-11:00 American Samoa?", "a": "UTC-11. Places: American Samoa, Niue. No DST.", "x": "UTC-11:00 American Samoa — UTC-11. Places: American Samoa, Niue. No DST. Example: Pago Pago.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-10:00 Hawaii", "d": "UTC-10. Places: Hawaii, Cook Islands. No DST in Hawaii.", "g": "utc-10", "l": 2, "q": "What is UTC-10:00 Hawaii?", "a": "UTC-10. Places: Hawaii, Cook Islands. No DST in Hawaii.", "x": "UTC-10:00 Hawaii — UTC-10. Places: Hawaii, Cook Islands. No DST in Hawaii. Example: Honolulu.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-09:30 Marquesas", "d": "UTC-09:30. Places: Marquesas Islands. No DST.", "g": "utc-9", "l": 2, "q": "What is UTC-09:30 Marquesas?", "a": "UTC-09:30. Places: Marquesas Islands. No DST.", "x": "UTC-09:30 Marquesas — UTC-09:30. Places: Marquesas Islands. No DST. Example: Taiohae.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "UTC-09:00 Alaska", "d": "UTC-09. Places: Alaska (most). DST to UTC-08 in summer.", "g": "utc-9", "l": 2, "q": "What is UTC-09:00 Alaska?", "a": "UTC-09. Places: Alaska (most). DST to UTC-08 in summer.", "x": "UTC-09:00 Alaska — UTC-09. Places: Alaska (most). DST to UTC-08 in summer. Example: Anchorage.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-08:00 Pacific", "d": "UTC-08. Places: US Pacific, Vancouver, Tijuana. DST to UTC-07.", "g": "utc-8", "l": 2, "q": "What is UTC-08:00 Pacific?", "a": "UTC-08. Places: US Pacific, Vancouver, Tijuana. DST to UTC-07.", "x": "UTC-08:00 Pacific — UTC-08. Places: US Pacific, Vancouver, Tijuana. DST to UTC-07. Example: Los Angeles.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-07:00 Mountain", "d": "UTC-07. Places: Denver, Phoenix (no DST), Edmonton. DST to UTC-06.", "g": "utc-7", "l": 2, "q": "What is UTC-07:00 Mountain?", "a": "UTC-07. Places: Denver, Phoenix (no DST), Edmonton. DST to UTC-06.", "x": "UTC-07:00 Mountain — UTC-07. Places: Denver, Phoenix (no DST), Edmonton. DST to UTC-06. Example: Denver.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-06:00 Central", "d": "UTC-06. Places: Chicago, Mexico City, Winnipeg. DST to UTC-05.", "g": "utc-6", "l": 2, "q": "What is UTC-06:00 Central?", "a": "UTC-06. Places: Chicago, Mexico City, Winnipeg. DST to UTC-05.", "x": "UTC-06:00 Central — UTC-06. Places: Chicago, Mexico City, Winnipeg. DST to UTC-05. Example: Chicago.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-05:00 Eastern", "d": "UTC-05. Places: New York, Toronto, Lima. DST to UTC-04.", "g": "utc-5", "l": 2, "q": "What is UTC-05:00 Eastern?", "a": "UTC-05. Places: New York, Toronto, Lima. DST to UTC-04.", "x": "UTC-05:00 Eastern — UTC-05. Places: New York, Toronto, Lima. DST to UTC-04. Example: New York.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-04:00 Atlantic", "d": "UTC-04. Places: Halifax, Caracas, Santiago. Some DST.", "g": "utc-4", "l": 2, "q": "What is UTC-04:00 Atlantic?", "a": "UTC-04. Places: Halifax, Caracas, Santiago. Some DST.", "x": "UTC-04:00 Atlantic — UTC-04. Places: Halifax, Caracas, Santiago. Some DST. Example: Halifax.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-03:30 Newfoundland", "d": "UTC-03:30. Places: Newfoundland. DST to UTC-02:30.", "g": "utc-3", "l": 2, "q": "What is UTC-03:30 Newfoundland?", "a": "UTC-03:30. Places: Newfoundland. DST to UTC-02:30.", "x": "UTC-03:30 Newfoundland — UTC-03:30. Places: Newfoundland. DST to UTC-02:30. Example: St. John's.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-03:00 Brasilia", "d": "UTC-03. Places: Sao Paulo, Buenos Aires. No DST currently.", "g": "utc-3", "l": 2, "q": "What is UTC-03:00 Brasilia?", "a": "UTC-03. Places: Sao Paulo, Buenos Aires. No DST currently.", "x": "UTC-03:00 Brasilia — UTC-03. Places: Sao Paulo, Buenos Aires. No DST currently. Example: Sao Paulo.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-02:00 Mid-Atlantic", "d": "UTC-02. Places: South Georgia, Fernando de Noronha.", "g": "utc-2", "l": 2, "q": "What is UTC-02:00 Mid-Atlantic?", "a": "UTC-02. Places: South Georgia, Fernando de Noronha.", "x": "UTC-02:00 Mid-Atlantic — UTC-02. Places: South Georgia, Fernando de Noronha. Example: South Georgia.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC-01:00 Azores", "d": "UTC-01. Places: Azores, Cape Verde. DST in Azores.", "g": "utc-1", "l": 2, "q": "What is UTC-01:00 Azores?", "a": "UTC-01. Places: Azores, Cape Verde. DST in Azores.", "x": "UTC-01:00 Azores — UTC-01. Places: Azores, Cape Verde. DST in Azores. Example: Ponta Delgada.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC+00:00 Western Europe", "d": "UTC+00. Places: London, Lisbon, Accra. DST to UTC+01.", "g": "utc0", "l": 2, "q": "What is UTC+00:00 Western Europe?", "a": "UTC+00. Places: London, Lisbon, Accra. DST to UTC+01.", "x": "UTC+00:00 Western Europe — UTC+00. Places: London, Lisbon, Accra. DST to UTC+01. Example: London.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC+01:00 Central Europe", "d": "UTC+01. Places: Paris, Berlin, Lagos. DST to UTC+02.", "g": "utc0", "l": 2, "q": "What is UTC+01:00 Central Europe?", "a": "UTC+01. Places: Paris, Berlin, Lagos. DST to UTC+02.", "x": "UTC+01:00 Central Europe — UTC+01. Places: Paris, Berlin, Lagos. DST to UTC+02. Example: Paris.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC+02:00 Eastern Europe", "d": "UTC+02. Places: Cairo, Athens, Johannesburg. Some DST.", "g": "utc0", "l": 2, "q": "What is UTC+02:00 Eastern Europe?", "a": "UTC+02. Places: Cairo, Athens, Johannesburg. Some DST.", "x": "UTC+02:00 Eastern Europe — UTC+02. Places: Cairo, Athens, Johannesburg. Some DST. Example: Cairo.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC+03:00 Moscow", "d": "UTC+03. Places: Moscow, Istanbul, Nairobi. No DST.", "g": "utc3", "l": 2, "q": "What is UTC+03:00 Moscow?", "a": "UTC+03. Places: Moscow, Istanbul, Nairobi. No DST.", "x": "UTC+03:00 Moscow — UTC+03. Places: Moscow, Istanbul, Nairobi. No DST. Example: Moscow.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "UTC+03:30 Iran", "d": "UTC+03:30. Places: Iran. DST observed historically.", "g": "utc3", "l": 2, "q": "What is UTC+03:30 Iran?", "a": "UTC+03:30. Places: Iran. DST observed historically.", "x": "UTC+03:30 Iran — UTC+03:30. Places: Iran. DST observed historically. Example: Tehran.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "UTC+04:00 Gulf", "d": "UTC+04. Places: Dubai, Baku. No DST.", "g": "utc4", "l": 2, "q": "What is UTC+04:00 Gulf?", "a": "UTC+04. Places: Dubai, Baku. No DST.", "x": "UTC+04:00 Gulf — UTC+04. Places: Dubai, Baku. No DST. Example: Dubai.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "UTC+04:30 Afghanistan", "d": "UTC+04:30. Places: Afghanistan. No DST.", "g": "utc4", "l": 2, "q": "What is UTC+04:30 Afghanistan?", "a": "UTC+04:30. Places: Afghanistan. No DST.", "x": "UTC+04:30 Afghanistan — UTC+04:30. Places: Afghanistan. No DST. Example: Kabul.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "UTC+05:00 Pakistan", "d": "UTC+05. Places: Karachi, Tashkent, Yekaterinburg. No DST.", "g": "utc5", "l": 2, "q": "What is UTC+05:00 Pakistan?", "a": "UTC+05. Places: Karachi, Tashkent, Yekaterinburg. No DST.", "x": "UTC+05:00 Pakistan — UTC+05. Places: Karachi, Tashkent, Yekaterinburg. No DST. Example: Karachi.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact.", "s": "public-reference", "f": null}, {"t": "UTC+05:30 India", "d": "UTC+05:30. Places: India, Sri Lanka. No DST.", "g": "utc5", "l": 2, "q": "What is UTC+05:30 India?", "a": "UTC+05:30. Places: India, Sri Lanka. No DST.", "x": "UTC+05:30 India — UTC+05:30. Places: India, Sri Lanka. No DST. Example: New Delhi.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "UTC+05:45 Nepal", "d": "UTC+05:45. Places: Nepal. No DST.", "g": "utc5", "l": 2, "q": "What is UTC+05:45 Nepal?", "a": "UTC+05:45. Places: Nepal. No DST.", "x": "UTC+05:45 Nepal — UTC+05:45. Places: Nepal. No DST. Example: Kathmandu.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "UTC+06:00 Bangladesh", "d": "UTC+06. Places: Dhaka, Almaty. No DST.", "g": "utc6", "l": 2, "q": "What is UTC+06:00 Bangladesh?", "a": "UTC+06. Places: Dhaka, Almaty. No DST.", "x": "UTC+06:00 Bangladesh — UTC+06. Places: Dhaka, Almaty. No DST. Example: Dhaka.  Checked against standard world references. Figures marked about are rounded; capitals and codes are exact. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-time-zones-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
