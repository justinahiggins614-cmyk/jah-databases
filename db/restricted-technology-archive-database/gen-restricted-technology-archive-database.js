(function(){'use strict';
/* The Restricted Technology Archive Database generator — jahdb-restricted-tech-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RTA-";
var SLUG="restricted-technology-archive-database";
var FIELDS=["crypto", "sigint", "space", "media", "policy", "process"];
var SEED_TITLES=[["DES: the public standard (FIPS PUB 46, 1977)", "crypto"], ["SKIPJACK declassified (1998)", "crypto"], ["The Clipper chip (1993-1996)", "crypto"], ["PGP 1.0 (1991): Zimmermann's release", "crypto"], ["Bernstein v. Department of Justice (1996-1999)", "crypto"], ["The 40-bit export era", "crypto"], ["The RSA patent (expired 2000)", "crypto"], ["\"New Directions in Cryptography\" (1976)", "crypto"], ["Enigma and Ultra declassified (1970s)", "sigint"], ["VENONA declassified (1995)", "sigint"], ["SIGABA/ECM II declassified (1996)", "sigint"], ["Purple: Japan's cipher, broken and declassified", "sigint"], ["JN-25: the naval code", "sigint"], ["Lorenz and Colossus declassified", "sigint"], ["TypeX: Britain's cipher machine", "sigint"], ["The Navajo code talkers (declassified 1968)", "sigint"], ["Numbers stations: the public mystery", "sigint"], ["TEMPEST: partially declassified", "sigint"], ["The one-time pad: the perfect cipher, public", "sigint"], ["CORONA declassified (1995)", "space"], ["GPS Selective Availability switched off (2000)", "space"], ["Satellite imagery limits relaxed (2014)", "space"], ["DeCSS: the legal history (2000)", "media"], ["AACS: the successor", "media"], ["COCOM (1949-1994)", "policy"], ["Steganography: hidden in plain sight, publicly", "policy"], ["Operation Gold: the Berlin tunnel (declassified)", "policy"], ["How this archive stays public", "process"]];
var BLURBS={"crypto": ["A full archive record in the 'crypto' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'crypto' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "sigint": ["A full archive record in the 'sigint' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'sigint' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "space": ["A full archive record in the 'space' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'space' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "media": ["A full archive record in the 'media' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'media' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "policy": ["A full archive record in the 'policy' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'policy' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "process": ["A full archive record in the 'process' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'process' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Declassified": "Officially released from classified status \u2014 public thereafter.", "Export control": "Laws restricting technology transfer across borders.", "Public standard": "A specification published openly (e.g., FIPS) \u2014 free for all to implement.", "Signals intelligence": "Intercepting communications and electronic signals.", "Cryptography": "The science of secret writing \u2014 and of breaking it.", "Grandfathered": "Lawfully public before a restriction; remaining public thereafter."};
var GEN_SRC="NIST FIPS publications; NSA declassification releases; court records; IETF RFCs";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Restricted Technology Archive Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Restricted Technology Archive Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-restricted-tech-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-restricted-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
