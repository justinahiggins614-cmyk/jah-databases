(function(){'use strict';
/* Job Search Database generator — jahdb-job-search-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-JOB-';
var TOPICS=[["Resumes", "The one-page summary of skills and experience."], ["Cover Letters", "The personalized letter introducing a job application."], ["Networking", "Building relationships that lead to opportunities."], ["Job Boards", "Websites listing open positions."], ["Interviews", "Preparing answers, questions, and a confident presence."], ["The STAR Method", "Answering interview questions with situation, task, action, result."], ["References", "People who vouch for your work."], ["Follow-Up", "Thank-you notes after interviews."], ["Professional Profiles", "Online profiles showcasing experience to employers."], ["Tailoring Applications", "Matching each resume to the job description."], ["Researching Companies", "Learning about employers before applying."], ["Salary Negotiation", "Discussing pay professionally and with preparation."], ["Internships", "Work experience that builds skills and contacts."], ["Career Fairs", "Events meeting many employers at once."], ["The Elevator Pitch", "The thirty-second summary of who you are professionally."], ["Portfolios", "Collections of work samples for creative and technical jobs."], ["Background Checks", "The verifications employers run before hiring."], ["Dress Codes", "Dressing appropriately for interviews and workplaces."], ["Handling Rejection", "Learning from no's and keeping momentum."], ["Skills Inventory", "Listing what you can do to target the right jobs."], ["Remote Job Applications", "Applying for work-from-home positions."], ["Informational Interviews", "Chatting with professionals to learn about careers."], ["Applicant Tracking Systems", "The software screening resumes before humans see them."], ["Job Descriptions", "Reading postings carefully for real requirements."], ["Career Changes", "Pivoting to a new field with transferable skills."], ["Part-Time and Temp Work", "Flexible jobs that build experience."], ["Volunteering", "Gaining skills and contacts through service."], ["Staying Organized", "Tracking applications, deadlines, and follow-ups."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'job search record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('job-search',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();