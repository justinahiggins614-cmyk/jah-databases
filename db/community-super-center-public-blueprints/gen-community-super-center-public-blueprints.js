(function(){'use strict';
/* JAH The Super Center Community Blueprints Public Database generator — jahdb-community-super-center-public-blueprints-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCCPB-";
var FIELDS=["site-design", "streets", "utilities", "standards"];
var TOPICS={"site-design": ["The Big-Box Site Plan: Standard Elements \u2014 site-design", "Parking Lot Layout and Stall Dimensions \u2014 site-design", "Accessible Parking and ADA Stall Standards \u2014 site-design", "Loading Dock and Truck Court Standards \u2014 site-design", "Pedestrian Walkways Through Parking Areas \u2014 site-design", "Landscape Islands and Shade Tree Requirements \u2014 site-design", "Monument Sign Setbacks and Sight Triangles \u2014 site-design", "Outdoor Display and Garden Center Layouts \u2014 site-design", "Fuel Station Canopy Site Standards \u2014 site-design"], "streets": ["Arterial Street Cross-Sections \u2014 streets", "Collector Street Design Standards \u2014 streets", "Curb Radii for Delivery Trucks \u2014 streets", "Signalized Intersection Spacing on Corridors \u2014 streets", "Driveway Throat Lengths for Retail Sites \u2014 streets", "Transit Stop Placement on Retail Corridors \u2014 streets", "Sidewalk and Crosswalk Standards \u2014 streets", "Bike Lane Design on Commercial Streets \u2014 streets"], "utilities": ["Stormwater Detention for Large Impervious Sites \u2014 utilities", "Fire Apparatus Access Roads \u2014 utilities", "Fire Hydrant Spacing Standards \u2014 utilities", "Water Main Sizing for Commercial Sites \u2014 utilities", "Sanitary Sewer Design for Retail Developments \u2014 utilities", "Electrical Service for Large Commercial Buildings \u2014 utilities", "Lighting Levels for Parking Lots \u2014 utilities", "Grease Interceptors for Food Service Tenants \u2014 utilities"], "standards": ["Zoning Setbacks for Commercial Districts \u2014 standards", "Building Height Limits in Retail Zones \u2014 standards", "Floor Area Ratio in Commercial Development \u2014 standards", "Landscaping Percentage Requirements \u2014 standards", "Noise Ordinance Basics for Commercial Areas \u2014 standards", "Erosion Control During Construction \u2014 standards", "Phased Site Plan Review Process \u2014 standards", "Traffic Impact Study Requirements \u2014 standards", "Americans with Disabilities Act Site Requirements \u2014 standards"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH The Super Center Community Blueprints Public Database \u2014 structural study\n"
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
    description:'SAMPLE RECORD (generated \u2014 structural sample). A structural planning reference record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"community-super-center-public-blueprints-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-community-super-center-public-blueprints-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('community-super-center-public-blueprints',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
