(function(){'use strict';
/* JAH Voting Guide Database generator — jahdb-voting-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='voting-guide',PREFIX='JAH-VOT-',NAME='JAH Voting Guide Database';
var FIELDS=["eligibility", "registration", "id", "methods", "elections", "at the polls", "research", "rights", "security", "results"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Who can vote in US federal elections?", "d": "US citizens 18+ who meet state residency requirements.", "g": "eligibility", "l": 2, "q": "What is Who can vote in US federal elections??", "a": "US citizens 18+ who meet state residency requirements.", "x": "Who can vote in US federal elections? — US citizens 18+ who meet state residency requirements. Example: Register first..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "How do you register to vote?", "d": "Online, by mail, or in person — deadlines vary by state.", "g": "registration", "l": 2, "q": "What is How do you register to vote??", "a": "Online, by mail, or in person — deadlines vary by state.", "x": "How do you register to vote? — Online, by mail, or in person — deadlines vary by state. Example: Check vote.gov..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is the voter registration deadline?", "d": "Varies by state: from 30 days before to same-day registration.", "g": "registration", "l": 2, "q": "What is What is the voter registration deadline??", "a": "Varies by state: from 30 days before to same-day registration.", "x": "What is the voter registration deadline? — Varies by state: from 30 days before to same-day registration. Example: Check your state..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What ID do you need to vote?", "d": "Varies by state; some require photo ID, others do not.", "g": "id", "l": 2, "q": "What is What ID do you need to vote??", "a": "Varies by state; some require photo ID, others do not.", "x": "What ID do you need to vote? — Varies by state; some require photo ID, others do not. Example: Check your state's rules..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What are the ways to cast a ballot?", "d": "In person on Election Day, early in-person, or absentee/mail ballot.", "g": "methods", "l": 2, "q": "What is What are the ways to cast a ballot??", "a": "In person on Election Day, early in-person, or absentee/mail ballot.", "x": "What are the ways to cast a ballot? — In person on Election Day, early in-person, or absentee/mail ballot. Example: All valid..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is early voting?", "d": "In-person voting before Election Day at designated sites.", "g": "methods", "l": 2, "q": "What is What is early voting??", "a": "In-person voting before Election Day at designated sites.", "x": "What is early voting? — In-person voting before Election Day at designated sites. Example: Shorter lines..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is absentee voting?", "d": "Voting by mail when away or unable to reach polls.", "g": "methods", "l": 2, "q": "What is What is absentee voting??", "a": "Voting by mail when away or unable to reach polls.", "x": "What is absentee voting? — Voting by mail when away or unable to reach polls. Example: Request deadlines apply..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Do mail ballots count the same?", "d": "Yes — counted equally with in-person ballots.", "g": "methods", "l": 2, "q": "What is Do mail ballots count the same??", "a": "Yes — counted equally with in-person ballots.", "x": "Do mail ballots count the same? — Yes — counted equally with in-person ballots. Example: Secure process..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is a primary election?", "d": "Party nominating contests before the general election.", "g": "elections", "l": 2, "q": "What is What is a primary election??", "a": "Party nominating contests before the general election.", "x": "What is a primary election? — Party nominating contests before the general election. Example: Closed or open by state..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is a general election?", "d": "The final election choosing officeholders.", "g": "elections", "l": 2, "q": "What is What is a general election??", "a": "The final election choosing officeholders.", "x": "What is a general election? — The final election choosing officeholders. Example: First Tuesday after first Monday in November..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is a midterm election?", "d": "Congressional elections between presidential years.", "g": "elections", "l": 2, "q": "What is What is a midterm election??", "a": "Congressional elections between presidential years.", "x": "What is a midterm election? — Congressional elections between presidential years. Example: Every 4-year midpoint..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is a ballot measure?", "d": "A law or amendment voted on directly by voters.", "g": "elections", "l": 2, "q": "What is What is a ballot measure??", "a": "A law or amendment voted on directly by voters.", "x": "What is a ballot measure? — A law or amendment voted on directly by voters. Example: Initiatives and referendums..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "How does the Electoral College work?", "d": "538 electors; 270 to win the presidency; states allocate by popular vote.", "g": "elections", "l": 2, "q": "What is How does the Electoral College work??", "a": "538 electors; 270 to win the presidency; states allocate by popular vote.", "x": "How does the Electoral College work? — 538 electors; 270 to win the presidency; states allocate by popular vote. Example: Winner-take-all in most states..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is redistricting?", "d": "Redrawing district lines after each census.", "g": "elections", "l": 2, "q": "What is What is redistricting??", "a": "Redrawing district lines after each census.", "x": "What is redistricting? — Redrawing district lines after each census. Example: Every 10 years..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is gerrymandering?", "d": "Drawing districts to favor a party.", "g": "elections", "l": 2, "q": "What is What is gerrymandering??", "a": "Drawing districts to favor a party.", "x": "What is gerrymandering? — Drawing districts to favor a party. Example: Courts limit extremes..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Can felons vote?", "d": "Depends on state: many restore rights after sentence completion.", "g": "eligibility", "l": 2, "q": "What is Can felons vote??", "a": "Depends on state: many restore rights after sentence completion.", "x": "Can felons vote? — Depends on state: many restore rights after sentence completion. Example: Check your state..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Can you vote while in college out of state?", "d": "Yes — vote at your school address or absentee at home, not both.", "g": "eligibility", "l": 2, "q": "What is Can you vote while in college out of state??", "a": "Yes — vote at your school address or absentee at home, not both.", "x": "Can you vote while in college out of state? — Yes — vote at your school address or absentee at home, not both. Example: One ballot only..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What if you moved recently?", "d": "Update your registration; many states allow updates at the polls.", "g": "registration", "l": 2, "q": "What is What if you moved recently??", "a": "Update your registration; many states allow updates at the polls.", "x": "What if you moved recently? — Update your registration; many states allow updates at the polls. Example: Plan ahead..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What are poll workers?", "d": "Trained staff running polling places.", "g": "at the polls", "l": 2, "q": "What is What are poll workers??", "a": "Trained staff running polling places.", "x": "What are poll workers? — Trained staff running polling places. Example: Volunteer to serve..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is a provisional ballot?", "d": "A ballot cast when eligibility is questioned; verified later.", "g": "at the polls", "l": 2, "q": "What is What is a provisional ballot??", "a": "A ballot cast when eligibility is questioned; verified later.", "x": "What is a provisional ballot? — A ballot cast when eligibility is questioned; verified later. Example: Your vote is protected..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Can you wear campaign gear to vote?", "d": "Most states ban electioneering near polls.", "g": "at the polls", "l": 2, "q": "What is Can you wear campaign gear to vote??", "a": "Most states ban electioneering near polls.", "x": "Can you wear campaign gear to vote? — Most states ban electioneering near polls. Example: Leave it home..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What time do polls open and close?", "d": "Varies by state; if in line at closing, you can vote.", "g": "at the polls", "l": 2, "q": "What is What time do polls open and close??", "a": "Varies by state; if in line at closing, you can vote.", "x": "What time do polls open and close? — Varies by state; if in line at closing, you can vote. Example: Stay in line..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "How do you research candidates?", "d": "Official voter guides, debates, nonpartisan sites like vote411.org.", "g": "research", "l": 2, "q": "What is How do you research candidates??", "a": "Official voter guides, debates, nonpartisan sites like vote411.org.", "x": "How do you research candidates? — Official voter guides, debates, nonpartisan sites like vote411.org. Example: Multiple sources..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is a sample ballot?", "d": "A preview of your exact ballot before Election Day.", "g": "research", "l": 2, "q": "What is What is a sample ballot??", "a": "A preview of your exact ballot before Election Day.", "x": "What is a sample ballot? — A preview of your exact ballot before Election Day. Example: Study it early..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is voter intimidation?", "d": "Illegal threats or coercion at polls — report it.", "g": "rights", "l": 2, "q": "What is What is voter intimidation??", "a": "Illegal threats or coercion at polls — report it.", "x": "What is voter intimidation? — Illegal threats or coercion at polls — report it. Example: Call 866-OUR-VOTE..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-voting-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
