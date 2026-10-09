(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}

var CATS=['bad-tool-call','misunderstanding','timeout','bad-input','api-error'];

var BANK=[
 {type:'bad-tool-call',
  failed:'Assistant called search_weather with argument "cityy" instead of "city"; the tool rejected the call.',
  strategy:'Acknowledge the schema error, re-call the tool with the corrected argument name, and continue the task.',
  recovered:'Retrying with the corrected argument: search_weather(city="Oslo"). The forecast is on its way.'},
 {type:'bad-tool-call',
  failed:'Assistant passed a string where the calculator tool expected a number, causing a type error.',
  strategy:'Convert the input to the expected type, validate it, and re-issue the tool call.',
  recovered:'Converted "42" to the number 42 and re-ran calculate(expression="42*7"). Result: 294.'},
 {type:'misunderstanding',
  failed:'User said "book it" and the assistant booked a flight instead of the hotel the user meant.',
  strategy:'Apologize, clarify which booking was intended, cancel the wrong one, and complete the right one.',
  recovered:'Sorry about that — I canceled the flight hold. Confirming now: you wanted the downtown hotel for two nights, correct?'},
 {type:'misunderstanding',
  failed:'User asked to "make it shorter" meaning the summary, but the assistant shortened the deadline instead.',
  strategy:'State both interpretations, confirm the intended one, and redo only that part.',
  recovered:'To confirm: you want the summary shorter, not the deadline moved. Here is the trimmed summary.'},
 {type:'timeout',
  failed:'The web request timed out after 30 seconds with no data returned.',
  strategy:'Retry once with a narrower scope and a longer timeout; on a second failure, report partial progress honestly.',
  recovered:'The first fetch timed out, so I retried with a smaller page range and got the results. Here they are.'},
 {type:'timeout',
  failed:'The file upload stalled at 90 percent and the connection dropped.',
  strategy:'Resume the upload from the last confirmed chunk instead of restarting from zero.',
  recovered:'Resumed the upload from the 90 percent mark. The file is now fully transferred and verified.'},
 {type:'bad-input',
  failed:'User pasted a CSV where 40 rows are missing headers and delimiters are inconsistent.',
  strategy:'Show exactly which rows fail, accept a corrected upload, and proceed with the valid rows meanwhile.',
  recovered:'Rows 12, 18, and 31-40 are missing headers. I processed the 60 valid rows; send a fixed file for the rest.'},
 {type:'bad-input',
  failed:'User entered a date as "next Friday" but the assistant needs an exact calendar date.',
  strategy:'Resolve the relative date against today\'s date, show the assumption, and ask for confirmation.',
  recovered:'I read "next Friday" as October 16, 2026. If that is right, I will proceed; otherwise give me the exact date.'},
 {type:'api-error',
  failed:'The maps API returned 429 rate-limit errors on every request.',
  strategy:'Back off, switch to cached data, and tell the user the live lookup will resume shortly.',
  recovered:'The maps service is rate-limiting us, so I used cached directions. I will refresh them live in a few minutes.'},
 {type:'api-error',
  failed:'The payment API returned a 500 internal error during checkout.',
  strategy:'Do not retry the charge blindly; verify the transaction state first, then retry once or guide the user.',
  recovered:'The charge did not go through — I checked, and no payment was recorded. It is safe to retry checkout now.'},
 {type:'misunderstanding',
  failed:'User wrote "delete the draft" but there were two drafts, and the assistant deleted the wrong one.',
  strategy:'Restore from the trash or backup, confirm which draft was meant, then delete only that one.',
  recovered:'I restored the deleted draft from trash. Please confirm: delete "Draft v2" and keep "Draft v3"?'},
 {type:'timeout',
  failed:'The database query ran past the 10-second limit and was killed.',
  strategy:'Rewrite the query with tighter filters and pagination, then run it in smaller batches.',
  recovered:'I split the query into paged batches of 500 rows. All 2,300 rows are now loaded without timing out.'}
];

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var pool=BANK;
  if(opts&&opts.category&&CATS.indexOf(opts.category)>=0){
    var f=BANK.filter(function(s){return s.type===opts.category;});
    if(f.length)pool=f;
  }
  var s=pool[ri(rnd,0,pool.length-1)];
  var id='JAH-REPAIR-'+pad6(seed);
  return {id:id,repair_id:id,failed_turn:s.failed,failure_type:s.type,
    recovery_strategy:s.strategy,recovered_turn:s.recovered,
    turns_to_recover:ri(rnd,1,3),title:s.failed.slice(0,80)};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-REPAIR-\d{6}$/.test(r.id))e.push('id');
  if(r.repair_id!==r.id)e.push('repair_id');
  if(typeof r.failed_turn!=='string'||!r.failed_turn.length||r.failed_turn.length>600)e.push('failed_turn');
  if(CATS.indexOf(r.failure_type)<0)e.push('failure_type');
  if(typeof r.recovery_strategy!=='string'||!r.recovery_strategy.length||r.recovery_strategy.length>600)e.push('recovery_strategy');
  if(typeof r.recovered_turn!=='string'||!r.recovered_turn.length||r.recovered_turn.length>600)e.push('recovered_turn');
  if(typeof r.turns_to_recover!=='number'||r.turns_to_recover<1||r.turns_to_recover>3||r.turns_to_recover%1!==0)e.push('turns_to_recover');
  if(r.title!==String(r.failed_turn).slice(0,80))e.push('title');
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-repair-recovery-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('repair-recovery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
