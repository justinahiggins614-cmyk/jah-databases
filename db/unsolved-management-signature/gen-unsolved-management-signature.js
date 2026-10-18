(function(){'use strict';
/* JAH The Unsolved Management Signature Database generator — jahdb-unsolved-management-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USMGS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Do Firms Exist (Signature Edition) - Organizations",
  "The Principal-Agent Problem (Signature Edition) - Organizations",
  "What Makes Teams Work (Signature Edition) - Leadership",
  "Leadership Versus Management (Signature Edition) - Leadership",
  "Motivation: What Drives Workers (Signature Edition) - People",
  "The Hawthorne Effect: Real (Signature Edition) - People",
  "Pay for Performance: Does It Work (Signature Edition) - People",
  "Why Mergers Fail (Signature Edition) - Strategy",
  "The Dilemma of the Innovator (Signature Edition) - Strategy",
  "Core Competence: What Is It (Signature Edition) - Strategy",
  "Why Strategies Fail in Execution (Signature Edition) - Strategy"
 ],
 "Compounded": [
  "Organizational Culture: Can It Be Managed (Signature Edition) - Organizations",
  "The Span of Control Problem (Signature Edition) - Organizations",
  "Centralization Versus Decentralization (Signature Edition) - Organizations",
  "Why Organizations Bureaucratize (Signature Edition) - Organizations",
  "The Glass Ceiling: What Sustains It (Signature Edition) - People",
  "Diversity: Does It Improve Performance (Signature Edition) - People",
  "Remote Work: The Productivity Question (Signature Edition) - People",
  "The Gig Economy: Efficient or Exploitative (Signature Edition) - People",
  "Why Change Programs Fail (Signature Edition) - Leadership",
  "Charismatic Leadership: Real or Myth (Signature Edition) - Leadership",
  "Succession: Why CEOs Fail (Signature Edition) - Leadership",
  "Stakeholder Versus Shareholder (Signature Edition) - Strategy"
 ],
 "Advanced": [
  "The Purpose of the Corporation (Signature Edition) - Strategy",
  "ESG: Does It Work (Signature Edition) - Strategy",
  "Platform Power in Markets (Signature Edition) - Strategy",
  "The Attention Economy Firm (Signature Edition) - Strategy",
  "Algorithmic Management: Fair (Signature Edition) - People",
  "Unions: Do They Help Firms (Signature Edition) - People",
  "The Four-Day Week Evidence (Signature Edition) - People",
  "Organizational Learning: How (Signature Edition) - Organizations",
  "The Multinational: How Governed (Signature Edition) - Organizations",
  "Crisis Leadership: What Works (Signature Edition) - Leadership",
  "A Unified Theory of Management (Signature Edition) - Leadership"
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
var gen={version:'jahdb-unsolved-management-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-management-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
