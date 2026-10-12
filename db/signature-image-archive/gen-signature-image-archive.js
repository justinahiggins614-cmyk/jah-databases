(function(){'use strict';
/* JAH Signature Image Database generator — jahdb-signature-image-archive-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature versions of public images + all our own original Signature images.
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original, clearly labeled. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-SIA-';
/* Signature original image concepts: [title, style, category, description] */
var ORIGINALS=[
['Neon Meridian','signature-neon','digital art','A sweeping neon meridian line crossing a dark geometric horizon — the Signature mark rendered as pure light.'],
['Chrome Bloom','signature-chrome','digital art','A metallic flower unfolding in chrome petals, reflecting an unseen city — Signature industrial beauty.'],
['Quantum Lattice','signature-quantum','abstract','An infinite lattice of glowing nodes and connections — the Signature vision of connected knowledge.'],
['Obsidian Wave','signature-obsidian','abstract','A frozen obsidian wave caught mid-crash, edges catching silver light — dark Signature elegance.'],
['Solar Forge','signature-solar','digital art','A sun being forged in a cosmic smithy, sparks of plasma shaped by unseen hands — Signature creation myth.'],
['Cipher Garden','signature-cipher','abstract','A garden where every flower is a glyph and every path is an equation — Signature cryptography as nature.'],
['Titan Ascent','signature-titan','digital art','A colossal figure climbing a mountain of light, each step igniting the stone — Signature ambition.'],
['Mirror Deep','signature-mirror','abstract','An endless hall of mirrors reflecting not faces but ideas — Signature introspection.'],
['Pulse City','signature-pulse','digital art','A city at night where every window pulses in rhythm like a heartbeat — Signature urban life.'],
['Void Bloom','signature-void','abstract','A single flower blooming in absolute darkness, lit from within — Signature hope.'],
['Apex Meridian','signature-apex','digital art','The highest point of a geometric mountain range, crowned with Signature light — the peak of the system.'],
['Data Waterfall','signature-data','abstract','A waterfall made of streaming characters and symbols, pooling into a lake of meaning — Signature information.'],
['Iron Petal','signature-iron','digital art','A rose forged from iron plates, delicate and indestructible — Signature resilience.'],
['Ghost Circuit','signature-ghost','abstract','Faint circuit traces glowing through darkness like veins of light — Signature technology as organism.'],
['Crown of Signals','signature-crown','digital art','A crown woven from radio waves and light beams — Signature authority.'],
['Silent Thunder','signature-thunder','abstract','A thundercloud rendered in deep purples, lightning frozen as silver filigree — Signature power held in reserve.'],
['Paper Universe','signature-paper','digital art','An entire galaxy folded from a single sheet of glowing paper — Signature simplicity containing infinity.'],
['Glass Desert','signature-glass','abstract','A desert of glass dunes under twin moons, every grain catching light — Signature clarity.'],
['Ember Atlas','signature-ember','digital art','A world map drawn in embers on dark stone, continents glowing — Signature geography of ideas.'],
['Frozen Signal','signature-frozen','abstract','A radio signal visualized as ice crystals forming in air — Signature communication made visible.'],
['Copper Mind','signature-copper','digital art','A human profile formed from copper wiring and gears, thoughts as electric arcs — Signature intellect.'],
['Velvet Void','signature-velvet','abstract','Deep black velvet texture with a single thread of gold running through — Signature luxury in darkness.'],
['Storm Library','signature-storm','digital art','A library where books fly like birds in a storm, pages as wings — Signature knowledge unleashed.'],
['Crystal Compass','signature-crystal','abstract','A compass rose cut from crystal, each point refracting a different future — Signature direction.'],
['Neon Roots','signature-neon','digital art','A tree with neon roots spreading through dark soil, canopy of stars — Signature growth.'],
['Marble Storm','signature-marble','abstract','White marble veined with storm-gray, polished to mirror — Signature calm within chaos.'],
['Signal Bloom','signature-signal','digital art','A flower whose petals are broadcast waves, blooming across the spectrum — Signature transmission.'],
['Dark Meridian','signature-obsidian','abstract','The meridian line at midnight, a silver thread through black — Signature precision.'],
['Golden Circuit','signature-gold','digital art','A circuit board rendered in gold leaf on black lacquer — Signature value in technology.'],
['Ice Meridian','signature-frozen','abstract','A meridian of ice cracking with light — Signature clarity under pressure.'],
['Phoenix Code','signature-phoenix','digital art','A phoenix rising from lines of code, feathers as syntax — Signature rebirth through creation.'],
['Midnight Atlas','signature-midnight','abstract','A star atlas drawn on midnight blue, constellations as Signature marks — Signature navigation.'],
['Thunder Petal','signature-thunder','digital art','A single petal struck by lightning, glowing from within — Signature fragile power.'],
['Quantum Bloom','signature-quantum','abstract','A flower existing in multiple states at once, petals as probability clouds — Signature possibility.'],
['Chrome Meridian','signature-chrome','digital art','A chrome meridian reflecting an infinite horizon — Signature reflection.'],
['Ember Roots','signature-ember','abstract','Tree roots glowing like embers underground — Signature hidden fire.'],
['Glass Mind','signature-glass','digital art','A transparent head filled with swirling light patterns — Signature transparent thought.'],
['Neon Atlas','signature-neon','abstract','A world map in neon tubes on black — Signature geography of light.'],
['Obsidian Compass','signature-obsidian','digital art','A compass of black glass pointing to an unseen north — Signature true direction.'],
['Solar Roots','signature-solar','abstract','Roots drinking sunlight directly, glowing — Signature direct energy.'],
['Cipher Wave','signature-cipher','digital art','An ocean wave made of encrypted text, crest breaking into plaintext — Signature revelation.'],
['Titan Bloom','signature-titan','abstract','A colossal flower opening over a city, petals as shelter — Signature protection.'],
['Mirror Atlas','signature-mirror','digital art','A world map where every country reflects its opposite — Signature duality.'],
['Pulse Bloom','signature-pulse','abstract','A flower pulsing with heartbeat rhythm, petals opening and closing — Signature life.'],
['Void Compass','signature-void','digital art','A compass floating in darkness, needle pointing to a distant star — Signature guidance.'],
['Apex Bloom','signature-apex','abstract','A flower at the peak of a mountain of light — Signature achievement.'],
['Data Roots','signature-data','digital art','A tree with roots as data streams, branches as interfaces — Signature organic technology.'],
['Iron Wave','signature-iron','abstract','An ocean wave of hammered iron, frozen mid-curl — Signature strength.'],
['Ghost Bloom','signature-ghost','digital art','A translucent flower, barely there, glowing faintly — Signature presence.'],
['Crown Bloom','signature-crown','abstract','A flower wearing a crown of light — Signature royalty of nature.']
];
var SIG_STYLES=['signature-neon','signature-chrome','signature-quantum','signature-obsidian','signature-solar','signature-cipher','signature-titan','signature-mirror','signature-pulse','signature-void','signature-apex','signature-data','signature-iron','signature-ghost','signature-crown','signature-thunder','signature-paper','signature-glass','signature-ember','signature-frozen','signature-copper','signature-velvet','signature-storm','signature-crystal','signature-marble','signature-signal','signature-gold','signature-midnight','signature-phoenix'];
var CATS=['digital art','abstract','portrait','landscape','concept','emblem'];
var REGIONS=['North America','South America','Europe','Africa','Asia','Oceania','Middle East','Central America','Caribbean','Central Asia','East Asia','South Asia','Southeast Asia','Scandinavia','Mediterranean','Pacific Islands','Arctic','Antarctica'];
function sigSVG(seed,title,style){
  var s=prng(seed*104729+7);
  var base='#0a0a14';
  var acc=['#2f7bff','#00e5a0','#7a4fb5','#ffb020','#ff6b6b'][(s()*5)|0];
  var h='<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">';
  h+='<rect width="400" height="300" fill="'+base+'"/>';
  for(var i=0;i<18;i++){
    var x=s()*400|0,y=s()*300|0,r=6+s()*30|0;
    h+='<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="'+acc+'" opacity="0.18"/>';
  }
  h+='<path d="M0,'+(120+s()*60|0)+' Q100,'+(60+s()*40|0)+' 200,'+(140+s()*40|0)+' T400,'+(100+s()*80|0)+'" stroke="'+acc+'" stroke-width="3" fill="none" opacity="0.9"/>';
  h+='<circle cx="'+(80+s()*240|0)+'" cy="'+(60+s()*80|0)+'" r="'+(20+s()*20|0)+'" fill="none" stroke="'+acc+'" stroke-width="2" opacity="0.7"/>';
  for(var j=0;j<5;j++){h+='<line x1="'+(s()*400|0)+'" y1="0" x2="'+(s()*400|0)+'" y2="300" stroke="'+acc+'" stroke-width="1" opacity="0.25"/>';}
  h+='<rect x="0" y="248" width="400" height="52" fill="#000" opacity="0.8"/>';
  h+='<text x="12" y="270" font-family="sans-serif" font-size="13" fill="#e8f1ff">✳ '+String(title).slice(0,34).replace(/&/g,'&amp;').replace(/</g,'&lt;')+'</text>';
  h+='<text x="12" y="290" font-family="sans-serif" font-size="10" fill="'+acc+'">'+style+' · Signature original</text>';
  return h+'</svg>';
}
function make(seed,opts){
  opts=opts||{};
  var s=prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec;
  if(seed<=ORIGINALS.length&&!opts.gen){
    var O=ORIGINALS[seed-1];
    rec={id:id,title:O[0],description:'Signature original image: "'+O[0]+'". '+O[3]+' Style: '+O[1]+'. Category: '+O[2]+'. Created in the Signature system, property of Justin Addam Higgins.',
      category:O[2],style:O[1],based_on:null,creation:'signature-original',
      artwork_svg:sigSVG(seed,O[0],O[1]),
      region:pick(REGIONS,prng(seed*31+7)),year:'2026',
      demo:{kind:'image-viewer',program:'function view(img){return img.artwork_svg;}',note:'Signature original — deterministic artwork, same every render.'},
      src:'signature',_seed:seed};
  } else {
    var style=opts.style||pick(SIG_STYLES,s);
    var cat=opts.category||pick(CATS,s);
    var concept=pick(['meridian','bloom','wave','lattice','compass','crown','roots','signal','atlas','mirror','pulse','forge','garden','storm','crystal'],s);
    var t='Signature '+concept+' study (#'+seed+')';
    var basedOn=(s()<0.4)?('JAH-PIA-'+String(1+((s()*200)|0)).padStart(6,'0')):null;
    rec={id:id,title:t,description:'Signature image: "'+t+'". '+(basedOn?('Signature reimagining of public archive image '+basedOn+', transformed into the '+style+' style.'):'Original Signature composition in the '+style+' style.')+' Property of Justin Addam Higgins.',
      category:cat,style:style,based_on:basedOn,creation:basedOn?'signature-version':'signature-original',
      artwork_svg:sigSVG(seed,t,style),
      region:pick(REGIONS,s),year:'2026',
      demo:{kind:'image-viewer',program:'function view(img){return img.artwork_svg;}',note:'Deterministic Signature artwork.'},
      src:'signature',_seed:seed};
  }
  return rec;
}
function validate(r){
  var e=[];
  if(!r.id||r.id.indexOf(PREFIX)!==0)e.push('bad id');
  if(!r.title)e.push('no title');
  if(!r.style)e.push('no style');
  if(r.src!=='signature')e.push('bad src');
  return {ok:!e.length,errors:e};
}
function driftCheck(r,sample){
  var seen={};
  (sample||[]).forEach(function(x){seen[x.title]=1;});
  if(seen[r.title])return {ok:false,errors:['duplicate title']};
  return {ok:true,errors:[]};
}
function generate(seed,opts){var r=make(seed,opts);var v=validate(r);if(!v.ok)throw new Error('invalid: '+v.errors.join(','));return r;}
var api={generate:generate,validate:validate,driftCheck:driftCheck,make:make,PREFIX:PREFIX,ORIGINAL_COUNT:ORIGINALS.length,STYLES:SIG_STYLES,CATS:CATS};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-image-archive',api);
})();
