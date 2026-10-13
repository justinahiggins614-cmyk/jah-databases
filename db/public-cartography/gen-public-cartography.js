(function(){'use strict';
/* JAH Public Cartography Database generator — jahdb-public-cartography-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CART-';
var FIELDS=["historical-maps", "cartographic-techniques", "topographic-survey", "thematic-maps", "digital-maps", "navigation-charts"];
var TOPICS={
 "cartographic-techniques":["Mercator Projection (1569)","Gall–Peters Projection","Robinson Projection","Winkel Tripel Projection","Dymaxion Map","Choropleth Maps","Cartograms","Isoline / Contour Maps","Shaded Relief Maps","Flow Maps"],
 "digital-maps":["Roger Tomlinson GIS (1960s)","OpenStreetMap","Google Maps"],
 "historical-maps":["Tabula Peutingeriana","Ptolemy's Geographia World Map","Hereford Mappa Mundi","Fra Mauro Map","Waldseemüller World Map (1507)","Ortelius Theatrum Orbis Terrarum","Blaeu Atlas Maior","Lewis and Clark Expedition Maps","Eratosthenes' Map of the World","Al-Idrisi's Tabula Rogeriana","Catalan Atlas (1375)","T-O Maps (Isidorean)","Piri Reis Map (1513)","Cantino Planisphere (1502)","Behaim's Erdapfel (1492)","Coronelli Globes","Uranometria Star Atlas (1603)","Hevelius Lunar Map (1647)","Schiaparelli Mars Maps","Marie Tharp Ocean Floor Maps","Ebstorf Mappa Mundi","Saxton's Atlas of England and Wales (1579)","John Speed's Theatre of Great Britaine (1611)"],
 "navigation-charts":["Portolan Charts","Bathymetric Charts","Aeronautical Charts","Nautical Charts","Deep Ocean Floor Maps (modern)"],
 "thematic-maps":["Beck London Tube Map (1931)","Minard's Map of Napoleon's Russian Campaign","John Snow Cholera Map (1854)","Sanborn Fire Insurance Maps","William Smith's Geological Map (1815)","Köppen Climate Maps","Humboldt's Naturgemälde","Census Maps","Electoral Maps","Transit System Maps","Ski Trail Maps","Vegetation and Biome Maps","Population Density Maps"],
 "topographic-survey":["Cassini Carte de France","Ordnance Survey Maps","USGS Topographic Maps","Great Trigonometrical Survey of India","Trail and Hiking Maps","Antarctic Maps"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Study Lab — "+safe+"\n"
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
    name:topic+' — map study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A map study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'map-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-cartography-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-cartography',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
