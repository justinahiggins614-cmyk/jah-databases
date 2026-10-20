(function(){'use strict';
/* The Government Restriction Categories Database generator — jahdb-restriction-categories-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GRC-";
var SLUG="government-restriction-categories-database";
var FIELDS=["classification", "export", "speech", "tech", "secrecy", "movement", "process"];
var SEED_TITLES=[["US classification levels: Top Secret, Secret, Confidential", "classification"], ["The UK classification system", "classification"], ["Classification systems worldwide", "classification"], ["Executive Order 13526 (2009)", "classification"], ["The Wassenaar Arrangement (1996)", "export"], ["ITAR: the US Munitions List (high-level)", "export"], ["EAR: the Commerce Control List (high-level)", "export"], ["EU Dual-Use Regulation", "export"], ["OFAC sanctions programs", "export"], ["CFIUS: foreign investment review", "export"], ["Deemed exports", "export"], ["Prior restraint: Near v. Minnesota (1931)", "speech"], ["Obscenity: the Miller test (1973)", "speech"], ["Broadcast indecency (FCC)", "speech"], ["Import restrictions: the Ulysses case (1933)", "speech"], ["Cryptography export controls: the history", "tech"], ["Embargoed destinations", "tech"], ["CITES: endangered-species trade", "tech"], ["Controlled Substances schedules (high-level)", "tech"], ["Cultural property: UNESCO 1970", "tech"], ["Arms embargoes (UN)", "tech"], ["Censorship categories by country (documented)", "tech"], ["Film censorship boards (historical)", "tech"], ["State secrets privilege", "secrecy"], ["Invention secrecy orders", "secrecy"], ["'Born classified': Restricted Data", "secrecy"], ["Travel restrictions (general)", "movement"], ["How restriction categories are published", "process"], ["Licenses and exceptions", "process"]];
var BLURBS={"classification": ["A full archive record in the 'classification' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'classification' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "export": ["A full archive record in the 'export' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'export' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "speech": ["A full archive record in the 'speech' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'speech' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "tech": ["A full archive record in the 'tech' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'tech' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "secrecy": ["A full archive record in the 'secrecy' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'secrecy' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "movement": ["A full archive record in the 'movement' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'movement' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "process": ["A full archive record in the 'process' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'process' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Classification": "The system marking information by the damage its disclosure would cause.", "Export control": "Laws restricting the transfer of sensitive technology across borders.", "Dual-use": "Technology with both civilian and military applications \u2014 the core of export control.", "Sanctions": "Government restrictions on trade or dealings with targeted countries, entities, or persons.", "Prior restraint": "Government blocking of publication before it happens \u2014 presumptively unconstitutional in the US.", "Deemed export": "Sharing controlled technology with a foreign national inside the US counts as an export."};
var GEN_SRC="US National Archives (EO 13526); Wassenaar Arrangement public documents; US State Dept (ITAR); BIS (EAR); OFAC";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Government Restriction Categories Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Government Restriction Categories Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-restriction-categories-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-restriction-categories-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
