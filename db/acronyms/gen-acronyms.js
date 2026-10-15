(function(){'use strict';
/* Acronyms Database generator — jahdb-acronyms-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ACRONYM-';
var TOPICS=[["NASA", "National Aeronautics and Space Administration, the United States civilian space agency."], ["UN", "United Nations, the international organization founded to promote peace and cooperation."], ["UNESCO", "United Nations Educational, Scientific and Cultural Organization."], ["NATO", "North Atlantic Treaty Organization, a military alliance of member countries."], ["EU", "European Union, a political and economic union of European countries."], ["WHO", "World Health Organization, the United Nations agency for global public health."], ["FBI", "Federal Bureau of Investigation, the United States domestic intelligence and security service."], ["CIA", "Central Intelligence Agency, the United States foreign intelligence service."], ["DNA", "Deoxyribonucleic acid, the molecule that carries genetic instructions in living things."], ["CPU", "Central processing unit, the main component of a computer that carries out instructions."], ["RAM", "Random access memory, the short-term working memory of a computer."], ["GPS", "Global Positioning System, satellite-based navigation used worldwide."], ["USB", "Universal Serial Bus, a common standard for connecting devices to computers."], ["HTML", "HyperText Markup Language, the standard language for creating web pages."], ["URL", "Uniform Resource Locator, the address of a resource on the internet."], ["AI", "Artificial intelligence, computer systems that perform tasks requiring human-like intelligence."], ["ASAP", "As soon as possible, a common abbreviation in messages and requests."], ["DIY", "Do it yourself, doing projects yourself rather than hiring someone."], ["RSVP", "From the French phrase meaning please respond; used on invitations."], ["VIP", "Very important person, someone given special treatment or access."], ["ETA", "Estimated time of arrival."], ["FAQ", "Frequently asked questions, a list of common questions and answers."], ["CEO", "Chief executive officer, the highest-ranking executive in a company."], ["ATM", "Automated teller machine, for withdrawing cash and basic banking."], ["PIN", "Personal identification number, a numeric password for cards and accounts."], ["FYI", "For your information, used when sharing something useful."], ["AM and PM", "Ante meridiem (before noon) and post meridiem (after noon) in the 12-hour clock."], ["AD and BC", "Anno Domini and Before Christ, the traditional year-numbering system."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'acronyms record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('acronyms',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();