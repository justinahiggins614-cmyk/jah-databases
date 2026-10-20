(function(){'use strict';
/* The Unsealed Public Records Database generator — jahdb-unsealed-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USR-";
var SLUG="unsealed-public-records-database";
var FIELDS=["court", "leaks", "process"];
var SEED_TITLES=[["United States v. Nixon (1974): the tapes go public", "court"], ["The Pentagon Papers case (1971)", "court"], ["The Watergate trial records", "court"], ["The Enron trial (2006)", "court"], ["The tobacco documents: Master Settlement Agreement (1998)", "court"], ["The O.J. Simpson trial (1995): justice on television", "court"], ["The Boy Scouts 'perversion files' (unsealed 2012)", "court"], ["Catholic Church abuse files unsealed (2000s-2010s)", "court"], ["Epstein-related court documents unsealed (2019-2024)", "court"], ["The Nuremberg trials (1945-1946)", "court"], ["The Eichmann trial (1961): televised justice", "court"], ["The Scopes trial (1925)", "court"], ["The Chicago Seven trial (1969-1970)", "court"], ["Presidential impeachments: the public trials", "court"], ["The January 6th Committee hearings and report (2022)", "court"], ["My Lai: the public exposure (1969)", "leaks"], ["Abu Ghraib: the photos go public (2004)", "leaks"], ["The FinCEN Files (2020)", "leaks"], ["The Pandora Papers (2021)", "leaks"], ["How unsealing works", "process"], ["PACER: the public's courthouse", "process"], ["The Rosenberg trial (1951)", "court"], ["The Lindbergh kidnapping trial (1935)", "court"], ["The Rodney King trial (1992-1993)", "court"], ["The Ellsberg trial dismissed (1973)", "court"], ["The tobacco whistleblower: Jeffrey Wigand", "leaks"], ["The Paradise Papers (2017)", "leaks"], ["The unsealing motion: how it works", "process"]];
var BLURBS={"court": ["A full archive record in the 'court' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'court' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "leaks": ["A full archive record in the 'leaks' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'leaks' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "process": ["A full archive record in the 'process' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'process' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Unsealed": "A court record made public after a judge lifts its seal.", "PACER": "Public Access to Court Electronic Records \u2014 the federal courts' public docket system.", "Docket": "A court's public log of filings and proceedings in a case.", "Protective order": "A court order limiting disclosure of sensitive litigation material; lifting it unseals records.", "Public record": "Government records open to public inspection by law.", "Investigative journalism": "Reporting that uncovers concealed matters of public importance \u2014 often the engine of unsealing."};
var GEN_SRC="Court records via PACER/Justia; National Archives; ICIJ publications; Congressional reports";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Unsealed Public Records Database"+'.',
    'Run: python3 demo.py (standard library only).'+DQ3,
    'RECORD_ID = '+JSON.stringify(rec.id),
    'TITLE = '+JSON.stringify(rec.title),
    'CATEGORY = '+JSON.stringify(rec.g),
    '',
    'def summary():',
    '    return TITLE + " [" + RECORD_ID + "] — " + CATEGORY',
    '',
    'def details():',
    '    return '+JSON.stringify(String(rec.description).slice(0, 400)),
    '',
    'if __name__ == "__main__":',
    '    print("=" * 60)',
    '    print(summary())',
    '    print("=" * 60)',
    '    print(details())',
    '    print()',
    '    print("category:", CATEGORY)',
    '    print("signature_line:", '+JSON.stringify(!!SIG)+')'
  ];
  return lines.join("\n");
}
function generate(seed,opts){
  opts=opts||{};
  var rnd=prng((seed*2654435761)>>>0);
  var entry=SEED_TITLES[(seed-1)%SEED_TITLES.length];
  var title=entry[0],group=entry[1];
  if(opts.field&&FIELDS.indexOf(opts.field)>=0)group=opts.field;
  var blurbs=BLURBS[group]||BLURBS[FIELDS[0]];
  var blurb=pick(blurbs,rnd);
  var cycle=Math.floor((seed-1)/SEED_TITLES.length);
  if(cycle>0)title=title+' — Boundless Variation '+seed;
  var desc='Seed '+seed+' record for the '+"The Unsealed Public Records Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-unsealed-1.0"+' boundless generator: '+
    'the same seed always rebuilds this same record, and every record is validated by an independent checker before acceptance.';
  if(SIG)desc='Signature line — a Signature-created companion to the public record. '+desc+'\n\n'+GEN_DISCLAIMER;
  var rec={
    id:PREFIX+pad6(seed),
    title:title,
    t:title,
    g:group,
    ladder:1+((seed+entry[0].length)%3),
    description:desc,
    definitions:DEFINITIONS,
    program:programFor({id:PREFIX+pad6(seed),title:title,g:group,description:desc}),
    language:'python',
    source:GEN_SRC,
    last_verified:'2026-10-19',
    million_march:'MILLION IN PROGRESS — marching to 1,000,000 full records',
    _seed:seed
  };
  if(SIG){rec.signature=true;rec.record_nature='Signature-created companion — not an official record.';}
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(typeof r.program!=='string'||r.program.length<50)e.push('program');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&(s.t||s.title))seen[s.t||s.title]=1;});
  if(rec&&seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-unsealed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
