(function(){'use strict';
/* JAH The Fictional Band Generator Database generator — jahdb-fictional-band-generator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working band generator: every call invents a complete fictional band —
   name, genre, lineup with personalities, origin story, debut album with full
   tracklist, signature sound, and a ready-to-render album-cover SVG.
   Deterministic: same seed, same band. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-FCBGS-";
var FIELDS=["Rock Bands","Electronic Acts","Eclectic Ensembles"];
var BAND_A=["Velvet","Neon","Copper","Midnight","Solar","Paper","Thunder","Glass","Iron","Honey","Static","Crimson","Electric","Wild","Golden","Silent"];
var BAND_B=["Revolver","Parade","Antler","Meridian","Foxglove","Static","Harbor","Comet","Juniper","Anthem","Mirage","Circuit","Lantern","Wolves","Arrow","Choir"];
var GENRES={"Rock Bands":["garage rock","indie rock","post-punk","stoner rock","art rock","heartland rock"],
 "Electronic Acts":["synthwave","techno","downtempo","hyperpop","ambient house","electroclash"],
 "Eclectic Ensembles":["art pop","chamber folk","jazz fusion","worldbeat","baroque pop","experimental"]};
var FIRST=["Mara","Jules","Theo","Priya","Dario","Wren","Kai","Lena","Otis","Suki","Rafe","Nadia","Ellis","June","Milo","Tessa","Idris","Noor","Felix","Ada"];
var LAST=["Vance","Okafor","Lindqvist","Marsh","Delacroix","Kim","Reyes","Novak","Ashby","Quill","Thorne","Ibarra","Sato","Wilder","Frost","Hale"];
var ROLES={"Rock Bands":["lead vocals / rhythm guitar","lead guitar","bass","drums","keyboards"],
 "Electronic Acts":["synth / programming","vocals","drums / pads","bass synth","visuals"],
 "Eclectic Ensembles":["vocals / strings","guitar","keys / accordion","bass","percussion"]};
var TRAITS=["the quiet perfectionist","the wild card","the diplomat","the night owl","the archivist","the prankster","the philosopher","the engine"];
var CITIES=["Portland","Glasgow","Lagos","Melbourne","Austin","Oslo","Mexico City","Seoul","Bristol","Detroit","Lisbon","Toronto"];
var ALBUM_A=["Static","Half-Light","Thunder","Paper","Neon","Low","Golden","Glass","Midnight","Wild","Electric","Silent"];
var ALBUM_B=["Bloom","Reverie","Parade","Mirage","Anthem","Harbor","Circuit","Lantern","Meridian","Choir","Arrow","Foxglove"];
var TRACKS=["Opener","Ignition","City Lights","Halfway Home","Static Bloom","The Long Parade","Glasshouse","Midnight Run","Paper Moons","Anthem for Nobody","Last Train","Reverie","Thunderhead","The Quiet","Neon Harbor","Foxglove","Meridian","Home Signal","Wild Choir","Golden Hour","Low Orbit","The Lantern"];
var PALETTES=[["#FF6B35","#F7C548","#2B2D42"],["#0B4F6C","#20BF9F","#F4F7F5"],["#8A1C7C","#EF476F","#F7C548"],["#1A1A40","#ACE1AF","#D4AF37"],["#C8102E","#F5F0E1","#1A1A1A"],["#005EB8","#FFC72C","#F5F0E1"]];
function coverSVG(initial,cols){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><rect width="300" height="300" fill="'+cols[2]+'"/><circle cx="150" cy="150" r="95" fill="'+cols[0]+'"/><circle cx="150" cy="150" r="62" fill="'+cols[1]+'"/><text x="150" y="172" font-family="Georgia,serif" font-size="72" font-weight="bold" text-anchor="middle" fill="'+cols[2]+'">'+initial+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var name=pick(BAND_A,s)+" "+pick(BAND_B,s);
  var genre=pick(GENRES[field],s);
  var roles=ROLES[field];
  var members=pickN(FIRST,s,5).map(function(fn,i){return {name:fn+" "+pick(LAST,s),role:roles[i],trait:pick(TRAITS,s)};});
  var city=pick(CITIES,s), year=1988+((s()*36)|0);
  var album=pick(ALBUM_A,s)+" "+pick(ALBUM_B,s);
  var tracklist=pickN(TRACKS,s,10);
  var pal=pick(PALETTES,s);
  var svg=coverSVG(name.charAt(0),pal);
  var title=name+" — "+genre+" band";
  var desc='GENERATED BAND — "'+name+'". A '+genre+' '+field.toLowerCase().slice(0,-1)+' from '+city+', formed '+year+'. Lineup: '+members.map(function(m){return m.name+" ("+m.role+")";}).join(", ")+'. Debut album "'+album+'" ('+tracklist.length+' tracks). Signature sound: '+genre+' built on '+members[0].role+' and '+members[1].role+'.';
  var prog="# Band dossier — "+name+"\n"
    +"band = \""+name+"\"\n"+"genre = \""+genre+"\"\n"+"formed = "+year+"\n"+"city = \""+city+"\"\n"
    +"lineup = "+JSON.stringify(members.map(function(m){return m.name+" — "+m.role;}))+"\n"
    +"album = \""+album+"\"\n"+"tracks = "+tracklist.length+"\n"
    +"print(\"Band:\", band)\n"+"print(\"Genre:\", genre)\n"+"print(\"Formed:\", formed, \"in\", city)\n"
    +"print(\"Debut album:\", album, \"(%d tracks)\" % tracks)\n"
    +"print(\"Lineup:\")\n"+"[print(\" -\", m) for m in lineup]\n"
    +"print(\"Cover SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — band record', title:title, description:desc,
    how_it_works:'The generator rolls a band name from evocative word pairs, assigns a genre from the '+field+' pool, builds a five-member lineup with names, roles, and personality traits, sets a formation city and year, titles a debut album, and picks a ten-track tracklist. The album-cover SVG renders the band initial in a generated palette — deterministic per seed.',
    key_points:['Band: '+name+' — '+genre+' ('+field+')','Formed '+year+' in '+city,'Lineup: '+members.map(function(m){return m.name;}).join(', '),'Debut album: "'+album+'" — '+tracklist.join('; '),'Cover palette: '+pal.join(', '),'Deterministic: seed '+seed+' always rebuilds this exact band.'],
    requirements:['A seed number to regenerate this exact band','An HTML file to view the cover SVG'],
    standards:['Band name is original and pronounceable','Lineup covers all five roles','Tracklist has exactly ten titles','Cover SVG renders the band initial'],
    citations:['Band-naming references: evocative compound names.','Album craft references: debut tracklist architecture.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{band:name,genre:genre,formed:year,city:city,members:members,album:album,tracklist:tracklist,palette:pal,svg:svg},
    svg:svg,
    demo:{kind:'band-dossier',language:'python',program:prog,note:'Prints the full band dossier: lineup, album, and tracklist.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.members||r.output.members.length!==5)e.push('members');
  if(!r.output||!r.output.tracklist||r.output.tracklist.length!==10)e.push('tracklist');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate band in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-fictional-band-generator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fictional-band-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();