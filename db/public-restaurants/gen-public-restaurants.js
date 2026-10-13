(function(){'use strict';
/* JAH Public Restaurants Database generator — jahdb-public-restaurants-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-REST-';
var FIELDS=["fast-food", "fast-casual", "casual-dining", "fine-dining"];
var TOPICS={
 "casual-dining":["Olive Garden","Applebee's","Chili's","Red Lobster","Outback Steakhouse","The Cheesecake Factory","Cracker Barrel","Texas Roadhouse","Buffalo Wild Wings","Din Tai Fung","Ippudo","Sushi Samba","Eataly","Dishoom","Gyu-Kaku","Primanti Bros."],
 "fast-casual":["Chipotle","Panda Express","Shake Shack","Five Guys","Panera Bread","Qdoba","Moe's Southwest Grill","Zaxby's","Culver's","El Pollo Loco","Nando's","Wagamama"],
 "fast-food":["McDonald's","Burger King","Wendy's","KFC","Taco Bell","Subway","Chick-fil-A","Pizza Hut","Domino's","Starbucks","Dunkin'","In-N-Out Burger","Whataburger","White Castle","Arby's","Dairy Queen","Sonic Drive-In","Jack in the Box","Carl's Jr. / Hardee's","Popeyes","Little Caesars","Papa John's","Jimmy John's","Jersey Mike's","Firehouse Subs","Bojangles","Del Taco","Jollibee","The Varsity"],
 "fine-dining":["The French Laundry","Eleven Madison Park","Nobu"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/"/g,"'");
  return "# Restaurant Lab — "+safe+"\n"
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
    name:topic+' — restaurant entry study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A restaurant entry study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'menu-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-restaurants-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-restaurants',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
