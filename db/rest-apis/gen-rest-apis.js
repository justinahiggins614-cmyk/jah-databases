(function(){'use strict';
/* JAH Public REST APIs Database generator — jahdb-rest-apis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RAPI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a REST API",
  "HTTP Methods for APIs",
  "HTTP Status Codes for APIs",
  "REST Resources and URL Design",
  "JSON for APIs",
  "Making API Requests with curl",
  "API Request and Response Anatomy",
  "Query Parameters in APIs",
  "API Headers",
  "Your First API Server",
  "Testing APIs with Tools"
 ],
 "Compounded": [
  "API Pagination",
  "API Filtering and Sorting",
  "API Error Responses",
  "API Authentication Basics",
  "API Rate Limiting",
  "API Versioning",
  "API Documentation",
  "CORS for APIs",
  "API Validation",
  "API Logging and Monitoring",
  "Idempotency in APIs",
  "API Caching Strategies"
 ],
 "Advanced": [
  "OAuth2 and JWT for APIs",
  "API Webhooks",
  "GraphQL vs REST",
  "API Security Best Practices",
  "API Performance Optimization",
  "API Gateway Pattern",
  "API Testing Strategies",
  "API Deprecation Strategies",
  "API Analytics and Monetization",
  "Building a Complete REST API Capstone",
  "The Future of APIs"
 ]
};
var DEMOKIND="rest-apis-demo";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\');
  return 'console.log('+JSON.stringify('Topic: '+safe)+');\n'
       + 'console.log('+JSON.stringify('Field: '+field)+');\n'
       + 'console.log("Sample record - structural sample, not an archive entry.");\n';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — rest api record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A rest api record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'javascript',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-rest-apis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rest-apis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();