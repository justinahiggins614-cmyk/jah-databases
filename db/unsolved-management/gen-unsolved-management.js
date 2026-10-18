(function(){'use strict';
/* JAH The Unsolved Management Database generator — jahdb-unsolved-management-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USMG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Do Firms Exist - Organizations",
  "The Principal-Agent Problem - Organizations",
  "What Makes Teams Work - Leadership",
  "Leadership Versus Management - Leadership",
  "Motivation: What Drives Workers - People",
  "The Hawthorne Effect: Real - People",
  "Pay for Performance: Does It Work - People",
  "Why Mergers Fail - Strategy",
  "The Dilemma of the Innovator - Strategy",
  "Core Competence: What Is It - Strategy",
  "Why Strategies Fail in Execution - Strategy"
 ],
 "Compounded": [
  "Organizational Culture: Can It Be Managed - Organizations",
  "The Span of Control Problem - Organizations",
  "Centralization Versus Decentralization - Organizations",
  "Why Organizations Bureaucratize - Organizations",
  "The Glass Ceiling: What Sustains It - People",
  "Diversity: Does It Improve Performance - People",
  "Remote Work: The Productivity Question - People",
  "The Gig Economy: Efficient or Exploitative - People",
  "Why Change Programs Fail - Leadership",
  "Charismatic Leadership: Real or Myth - Leadership",
  "Succession: Why CEOs Fail - Leadership",
  "Stakeholder Versus Shareholder - Strategy"
 ],
 "Advanced": [
  "The Purpose of the Corporation - Strategy",
  "ESG: Does It Work - Strategy",
  "Platform Power in Markets - Strategy",
  "The Attention Economy Firm - Strategy",
  "Algorithmic Management: Fair - People",
  "Unions: Do They Help Firms - People",
  "The Four-Day Week Evidence - People",
  "Organizational Learning: How - Organizations",
  "The Multinational: How Governed - Organizations",
  "Crisis Leadership: What Works - Leadership",
  "A Unified Theory of Management - Leadership"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Management Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-management-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-management-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-management',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
