(function(){'use strict';
/* JAH The Government Agency Directory Signature Database generator — jahdb-government-agency-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GOVAGENCY-SIG-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The United States Department of Agriculture (USDA) (Signature Edition)", "The United States Department of Commerce (Signature Edition)", "The United States Department of Defense (DoD) (Signature Edition)", "The United States Department of Education (Signature Edition)", "The United States Department of Energy (DOE) (Signature Edition)", "The United States Department of Health and Human Services (HHS) (Signature Edition)", "The United States Department of Homeland Security (DHS) (Signature Edition)", "The United States Department of Housing and Urban Development (HUD) (Signature Edition)", "The United States Department of the Interior (Signature Edition)", "The United States Department of Justice (DOJ) (Signature Edition)", "The United States Department of Labor (Signature Edition)", "The United States Department of State (Signature Edition)"], "Compounded": ["The United States Department of Transportation (DOT) (Signature Edition)", "The United States Department of the Treasury (Signature Edition)", "The United States Department of Veterans Affairs (VA) (Signature Edition)", "The United States Environmental Protection Agency (EPA) (Signature Edition)", "The Federal Emergency Management Agency (FEMA) (Signature Edition)", "The Federal Communications Commission (FCC) (Signature Edition)", "The Federal Trade Commission (FTC) (Signature Edition)", "The United States Food and Drug Administration (FDA) (Signature Edition)", "The Internal Revenue Service (IRS) (Signature Edition)", "The National Aeronautics and Space Administration (NASA) (Signature Edition)", "The National Institutes of Health (NIH) (Signature Edition)", "The National Oceanic and Atmospheric Administration (NOAA) (Signature Edition)"], "Advanced": ["The United States Small Business Administration (SBA) (Signature Edition)", "The United States Social Security Administration (SSA) (Signature Edition)", "The United States Agency for International Development (USAID) (Signature Edition)", "The Federal Reserve System (Signature Edition)", "The Library of Congress (Signature Edition)", "The National Archives and Records Administration (NARA) (Signature Edition)", "The Government Accountability Office (GAO) (Signature Edition)", "The Congressional Budget Office (CBO) (Signature Edition)", "The United States Postal Service (USPS) (Signature Edition)", "The United States Census Bureau (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Government Agency Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — government agency record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A government agency record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"agency-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-government-agency-directory-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("government-agency-directory-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
