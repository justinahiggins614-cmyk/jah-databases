(function(){'use strict';
/* JAH The Super Center Communities Public Database generator — jahdb-community-super-center-public-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCCP-";
var FIELDS=["real-places", "planning", "economy", "daily-life"];
var TOPICS={"real-places": ["Bentonville, Arkansas \u2014 the Town That Grew with the Supercenter \u2014 real-places", "Rogers, Arkansas \u2014 Retail Corridor Growth \u2014 real-places", "Springdale, Arkansas \u2014 Working Town Around the Hub \u2014 real-places", "Issaquah, Washington \u2014 Headquarters Town \u2014 real-places", "Minneapolis, Minnesota \u2014 Target's Hometown Footprint \u2014 real-places", "Goodlettsville, Tennessee \u2014 Distribution-Hub Town \u2014 real-places", "Matthews, North Carolina \u2014 Suburb of Two Faces \u2014 real-places", "Tupelo, Mississippi \u2014 Manufacturing and Retail Crossroads \u2014 real-places"], "planning": ["How Commercial Corridors Reshape Small Towns \u2014 planning", "Zoning Around Large-Format Retail Anchors \u2014 planning", "Traffic Planning for Big-Box Corridors \u2014 planning", "Public Transit to Retail Employment Hubs \u2014 planning", "Parking Standards for Large Retail Sites \u2014 planning", "Stormwater Rules for Big Parking Lots \u2014 planning", "Signage Ordinances on Retail Corridors \u2014 planning", "Annexation and Growth Around Commercial Nodes \u2014 planning"], "economy": ["Employment Patterns Around Supercenters \u2014 economy", "Small Businesses Near Big-Box Anchors \u2014 economy", "Property Values Near Retail Corridors \u2014 economy", "Sales Tax Revenue and Municipal Budgets \u2014 economy", "Warehouse and Logistics Jobs Near Retail Hubs \u2014 economy", "The Grocery-Anchor Effect on Nearby Shops \u2014 economy", "Seasonal Hiring Cycles at Large Stores \u2014 economy"], "daily-life": ["The School Commute in Retail-Corridor Towns \u2014 daily-life", "Youth Sports Leagues and Park Funding \u2014 daily-life", "Public Libraries as Community Anchors \u2014 daily-life", "Farmers Markets Alongside Big Retail \u2014 daily-life", "Church and Civic Life in Growing Towns \u2014 daily-life", "Commuting Patterns to Retail Job Centers \u2014 daily-life", "Affordable Housing Near Employment Hubs \u2014 daily-life", "Healthcare Access in Retail Towns \u2014 daily-life", "Senior Services in Suburban Growth Areas \u2014 daily-life", "Community Festivals in Retail Towns \u2014 daily-life", "Neighborhood Identity in Fast-Growing Towns \u2014 daily-life"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH The Super Center Communities Public Database \u2014 structural study\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 structural study record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A structural community reference record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"community-super-center-public-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-community-super-center-public-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-super-center-public',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
