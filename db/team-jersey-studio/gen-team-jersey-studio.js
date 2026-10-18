(function(){'use strict';
/* JAH The Team Jersey Studio generator — jahdb-team-jersey-studio-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working jersey studio: every call designs an original team jersey —
   fictional club name, kit lane, two-color system with hexes, chest graphic,
   number font, sleeve detail — and renders the jersey front as an SVG.
   Deterministic per seed: same seed, same jersey. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TMJS-";
var FIELDS=["Home Kit","Away Kit","Special Edition"];
var CLUB_A=["Harbor","Iron","Northgate","Copper","Riverside","Juniper","Falcon","Meridian","Onyx","Lantern"];
var CLUB_B=["Wolves","Antlers","FC","Athletic","Rovers","United","Kings","Comets","Forge","Harbor"];
var GRAPHIC=["hooped chest band","vertical sash","tonal pinstripes","shoulder yoke panel","chevron chest","half-and-half split"];
var NUMFONT=["block collegiate","condensed modern","retro varsity","sharp italic"];
var SLEEVE=["contrast cuff band","tonal trim","sponsor-free clean","piped edge"];
var COLORS=[["#C8102E","#F5F0E1"],["#0B4F6C","#F4F7F5"],["#1F3D2B","#DAD7CD"],["#3E2A35","#F7C548"],["#1A3C5E","#C9A227"],["#0A0A0A","#E07A3F"]];
function jerseySVG(cols,graphic,num){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="340" viewBox="0 0 300 340">'
  +'<rect width="300" height="340" fill="#FFFFFF"/>'
  +'<path d="M95 40 L60 60 L40 110 L70 120 L80 100 L80 300 L220 300 L220 100 L230 120 L260 110 L240 60 L205 40 Q150 70 95 40 Z" fill="'+cols[0]+'" stroke="#222222" stroke-width="3"/>'
  +'<rect x="80" y="150" width="140" height="26" fill="'+cols[1]+'" opacity="0.9"/>'
  +'<text x="150" y="235" font-family="Georgia,serif" font-size="72" font-weight="bold" text-anchor="middle" fill="'+cols[1]+'">'+num+'</text>'
  +'<text x="150" y="325" font-family="Georgia,serif" font-size="12" text-anchor="middle" fill="#333333">'+graphic+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var club=pick(CLUB_A,s)+" "+pick(CLUB_B,s);
  var cols=pick(COLORS,s), graphic=pick(GRAPHIC,s), numfont=pick(NUMFONT,s), sleeve=pick(SLEEVE,s);
  var num=1+((s()*98)|0);
  var svg=jerseySVG(cols,graphic,num);
  var title=club+" "+field+" — seed "+seed;
  var desc='GENERATED JERSEY — the '+field.toLowerCase()+' for '+club+'. Colors: '+cols.join(' + ')+'. Chest: '+graphic+'. Numbers in '+numfont+'; sleeves: '+sleeve+'. Star number '+num+'.';
  var prog="# Jersey design — "+club+" (seed "+seed+")\n"
    +"club = \""+club+"\"\n"+"kit = \""+field+"\"\n"+"colors = "+JSON.stringify(cols)+"\n"
    +"graphic = \""+graphic+"\"\n"+"number_font = \""+numfont+"\"\n"+"sleeves = \""+sleeve+"\"\n"+"star_number = "+num+"\n"
    +"print(\"Club:\", club, \"[\"+kit+\"]\")\n"+"print(\"Colors:\", \", \".join(colors))\n"
    +"print(\"Chest:\", graphic, \"| Numbers:\", number_font, \"| Sleeves:\", sleeves)\n"
    +"print(\"Jersey SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — jersey record', title:title, description:desc,
    how_it_works:'The generator names a fictional club from word pairs, assigns the kit lane, picks a two-color system with hexes, a chest graphic, a number font, and a sleeve detail, then renders the jersey front as an SVG with the star number — deterministic per seed.',
    key_points:['Club: '+club,'Kit: '+field,'Colors: '+cols.join(' + '),'Chest: '+graphic,'Numbers: '+numfont,'Sleeves: '+sleeve,'Star number: '+num,'Deterministic: seed '+seed+' always rebuilds this exact jersey.'],
    requirements:['A seed number to regenerate this exact jersey','An HTML file to view the jersey SVG'],
    standards:['Club name is original','Two-color system with hex codes','Chest graphic and number font specified','Jersey SVG renders the star number'],
    citations:['Kit craft references: jersey design systems.','Identity references: fictional club naming.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{club:club,kit:field,colors:cols,graphic:graphic,numberFont:numfont,sleeves:sleeve,starNumber:num,svg:svg},
    svg:svg,
    demo:{kind:'jersey-plan',language:'python',program:prog,note:'Prints the club, kit spec, and design details.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.club||!o.graphic||!o.numberFont)e.push('design');
  if(!o.colors||o.colors.length!==2)e.push('colors');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate jersey in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-team-jersey-studio-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('team-jersey-studio',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();