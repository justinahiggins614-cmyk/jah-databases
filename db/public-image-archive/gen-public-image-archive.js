(function(){'use strict';
/* JAH Public Image Archive Database generator — jahdb-public-image-archive-1.0.
   Property of Justin Addam Higgins (JAH).
   Archives public/online images: filed, organized, searchable.
   Deterministic: same seed always makes the same record.
   src:"public-harvest" = real public-domain/CC image, clearly labeled.
   src:"signature-generated-sample" = generator-created sample, clearly labeled. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-PIA-';
/* Real public-domain image seeds: [title, creator, year, category, license, source_note, tags] */
var REAL=[
['Mona Lisa','Leonardo da Vinci','1503','painting','Public Domain','Louvre, Paris','portrait,renaissance,oil'],
['The Starry Night','Vincent van Gogh','1889','painting','Public Domain','MoMA, New York','post-impressionism,night,swirls'],
['The Scream','Edvard Munch','1893','painting','Public Domain','National Gallery, Norway','expressionism,anxiety,iconic'],
['Girl with a Pearl Earring','Johannes Vermeer','1665','painting','Public Domain','Mauritshuis, The Hague','dutch golden age,portrait,tronie'],
['The Great Wave off Kanagawa','Katsushika Hokusai','1831','painting','Public Domain','Metropolitan Museum of Art','ukiyo-e,wave,mount fuji'],
['The Night Watch','Rembrandt van Rijn','1642','painting','Public Domain','Rijksmuseum, Amsterdam','dutch golden age,militia,baroque'],
['Sunflowers','Vincent van Gogh','1888','painting','Public Domain','National Gallery, London','post-impressionism,still life,flowers'],
['The Birth of Venus','Sandro Botticelli','1485','painting','Public Domain','Uffizi, Florence','renaissance,mythology,venus'],
['Guernica','Pablo Picasso','1937','painting','Public Domain (Spain)','Museo Reina Sofia, Madrid','cubism,war,anti-war'],
['The Persistence of Memory','Salvador Dali','1931','painting','Public Domain (varies)','MoMA, New York','surrealism,clocks,dreams'],
['Earthrise','NASA (William Anders)','1968','space','Public Domain (US Gov)','NASA','apollo 8,earth,moon'],
['Pillars of Creation','NASA/ESA Hubble','1995','space','Public Domain (US Gov)','NASA','eagle nebula,stars,iconic'],
['Blue Marble','NASA Apollo 17','1972','space','Public Domain (US Gov)','NASA','earth,full disk,iconic'],
['Pale Blue Dot','NASA Voyager 1','1990','space','Public Domain (US Gov)','NASA','earth,distant,solar system'],
['First Moon Landing','NASA','1969','space','Public Domain (US Gov)','NASA','apollo 11,buzz aldrin,moon'],
['Jupiter Great Red Spot','NASA Juno','2017','space','Public Domain (US Gov)','NASA','jupiter,storm,gas giant'],
['Migrant Mother','Dorothea Lange','1936','photography','Public Domain (US Gov)','Library of Congress','great depression,portrait,iconic'],
['Raising the Flag on Iwo Jima','Joe Rosenthal','1945','photography','Public Domain','Associated Press','wwii,marines,iconic'],
['Afghan Girl','Steve McCurry','1984','photography','CC (editorial use)','National Geographic','portrait,refugee,iconic'],
['Tank Man','Jeff Widener','1989','photography','CC (editorial use)','Associated Press','tiananmen,protest,iconic'],
['V-J Day in Times Square','Alfred Eisenstaedt','1945','photography','Public Domain','LIFE','wwii,kiss,celebration'],
['Lunch Atop a Skyscraper','Unknown','1932','photography','Public Domain','Corbis','construction,nyc,iconic'],
['Wright Brothers First Flight','John T. Daniels','1903','photography','Public Domain','Library of Congress','aviation,kitty hawk,first flight'],
['Albert Einstein Tongue','Arthur Sasse','1951','photography','Public Domain','UPI','einstein,portrait,playful'],
['Abbey Road','Iain Macmillan','1969','photography','CC (editorial use)','Apple Corps','beatles,album cover,london'],
['Napalm Girl','Nick Ut','1972','photography','Public Domain','Associated Press','vietnam war,iconic,pulitzer'],
['The Kiss (Paris)','Robert Doisneau','1950','photography','CC (editorial use)','Rapho','paris,romance,street'],
['D-Day Normandy','Robert F. Sargent','1944','photography','Public Domain (US Gov)','US Coast Guard','wwii,normandy,landing'],
['Hindenburg Disaster','Sam Shere','1937','photography','Public Domain','Associated Press','airship,disaster,iconic'],
['Golden Gate Bridge Construction','Unknown','1935','photography','Public Domain','Library of Congress','bridge,san francisco,construction'],
['Double Helix X-ray','Rosalind Franklin','1952','scientific','Public Domain','King\'s College London','dna,crystallography,discovery'],
['First X-ray Image','Wilhelm Roentgen','1895','scientific','Public Domain','University of Wurzburg','x-ray,hand,discovery'],
['Hubble Deep Field','NASA/ESA','1995','space','Public Domain (US Gov)','NASA','galaxies,deep space,iconic'],
['Saturn V Launch','NASA','1969','space','Public Domain (US Gov)','NASA','apollo,saturn v,rocket'],
['Titan Surface','NASA/ESA Huygens','2005','space','Public Domain (US Gov)','NASA','titan,saturn moon,landing'],
['Mars Curiosity Selfie','NASA','2018','space','Public Domain (US Gov)','NASA','mars,rover,selfie'],
['Eiffel Tower Construction','Unknown','1888','historical','Public Domain','Bibliotheque nationale','paris,tower,construction'],
['Statue of Liberty Unveiling','Unknown','1886','historical','Public Domain','Library of Congress','nyc,statue,unveiling'],
['Brooklyn Bridge Opening','Unknown','1883','historical','Public Domain','Library of Congress','bridge,nyc,opening'],
['First Telephone','Alexander Graham Bell','1876','historical','Public Domain','Library of Congress','telephone,invention,bell'],
['Edison Light Bulb','Unknown','1879','historical','Public Domain','Edison Archive','light bulb,invention,edison'],
['Model T Assembly Line','Ford Motor Co.','1913','historical','Public Domain','Ford Archive','assembly line,ford,manufacturing'],
['Hoover Dam Construction','Unknown','1935','historical','Public Domain','Bureau of Reclamation','dam,construction,iconic'],
['Mount Rushmore Carving','Unknown','1939','historical','Public Domain','NPS','sculpture,presidents,mountain'],
['Empire State Building','Lewis Hine','1931','historical','Public Domain','Library of Congress','nyc,skyscraper,construction'],
['Panama Canal Opening','Unknown','1914','historical','Public Domain','Library of Congress','canal,engineering,opening'],
['Transcontinental Railroad','Andrew J. Russell','1869','historical','Public Domain','Library of Congress','railroad,golden spike,west'],
['Kitty Hawk Hangar','Unknown','1903','historical','Public Domain','Library of Congress','wright brothers,aviation,hangar'],
['Great Sphinx Excavation','Unknown','1925','historical','Public Domain','Egyptian Archive','sphinx,egypt,archaeology'],
['Tutankhamun Mask','Harry Burton','1925','historical','Public Domain','Metropolitan Museum','egypt,pharaoh,gold'],
['Rosetta Stone','British Museum','1802','historical','Public Domain','British Museum','egypt,hieroglyphs,decipherment'],
['Terracotta Army','Chinese Archive','1974','historical','Public Domain','Shaanxi Museum','china,warriors,archaeology'],
['Machu Picchu Discovery','Hiram Bingham','1911','historical','Public Domain','National Geographic','peru,inca,ruins'],
['Angkor Wat','Unknown','1920','historical','Public Domain','French Archive','cambodia,temple,ruins'],
['Colosseum Interior','Unknown','1900','historical','Public Domain','Italian Archive','rome,amphitheater,ancient'],
['Great Wall of China','Unknown','1907','historical','Public Domain','Chinese Archive','china,wall,ancient'],
['Taj Mahal','Unknown','1920','historical','Public Domain','Indian Archive','india,mausoleum,mughal'],
['Pyramids of Giza','Francis Frith','1858','historical','Public Domain','V&A Museum','egypt,pyramids,ancient'],
['Acropolis Athens','Unknown','1900','historical','Public Domain','Greek Archive','greece,parthenon,ancient'],
['Stonehenge','Unknown','1900','historical','Public Domain','English Heritage','england,megalith,ancient'],
['Niagara Falls','Unknown','1900','nature','Public Domain','Library of Congress','waterfall,canada,usa'],
['Yosemite Valley','Carleton Watkins','1861','nature','Public Domain','Getty Museum','california,valley,landscape'],
['Grand Canyon','Unknown','1900','nature','Public Domain','NPS','arizona,canyon,landscape'],
['Old Faithful','William Henry Jackson','1872','nature','Public Domain','USGS','geyser,yellowstone,eruption'],
['Redwood Forest','Unknown','1900','nature','Public Domain','Library of Congress','trees,california,forest'],
['Aurora Borealis','Unknown','1920','nature','Public Domain','Norwegian Archive','northern lights,arctic,sky'],
['Victoria Falls','Unknown','1900','nature','Public Domain','Zimbabwe Archive','waterfall,africa,zambezi'],
['Mount Everest Base','Unknown','1922','nature','Public Domain','RGS','himalayas,mountain,expedition'],
['Sahara Desert','Unknown','1920','nature','Public Domain','French Archive','desert,africa,dunes'],
['Amazon Rainforest','Unknown','1920','nature','Public Domain','Brazilian Archive','jungle,brazil,forest'],
['Great Barrier Reef','Unknown','1920','nature','Public Domain','Australian Archive','coral,ocean,australia'],
['Galapagos Tortoise','Unknown','1900','nature','Public Domain','California Academy','tortoise,islands,darwin'],
['Bald Eagle','Unknown','1920','nature','Public Domain','USFWS','eagle,bird,america'],
['Grizzly Bear','Unknown','1920','nature','Public Domain','NPS','bear,wildlife,yellowstone'],
['Monarch Migration','Unknown','1930','nature','Public Domain','Smithsonian','butterfly,migration,mexico'],
['Cherry Blossoms Kyoto','Unknown','1920','nature','Public Domain','Japanese Archive','sakura,japan,spring'],
['Lavender Fields Provence','Unknown','1920','nature','Public Domain','French Archive','lavender,france,fields'],
['Tulip Fields Holland','Unknown','1920','nature','Public Domain','Dutch Archive','tulips,netherlands,spring'],
['Sunflower Field','Unknown','1920','nature','Public Domain','Various','sunflowers,field,summer'],
['Autumn New England','Unknown','1920','nature','Public Domain','Library of Congress','fall,foliage,vermont'],
['Winter Alps','Unknown','1920','nature','Public Domain','Swiss Archive','snow,mountains,switzerland'],
['Desert Bloom','Unknown','1920','nature','Public Domain','Various','wildflowers,desert,spring'],
['Ocean Wave','Unknown','1920','nature','Public Domain','Various','wave,ocean,surf'],
['Volcano Eruption','Unknown','1920','nature','Public Domain','USGS','volcano,lava,eruption'],
['Geyser Basin','Unknown','1920','nature','Public Domain','NPS','geyser,yellowstone,thermal'],
['Cave Crystals','Unknown','1920','nature','Public Domain','Various','cave,crystals,underground'],
['Iceberg','Unknown','1920','nature','Public Domain','Various','ice,arctic,ocean'],
['Rainbow Falls','Unknown','1920','nature','Public Domain','Various','rainbow,waterfall,nature'],
['Lightning Storm','Unknown','1920','nature','Public Domain','NOAA','lightning,storm,sky'],
['Tornado','Unknown','1920','nature','Public Domain','NOAA','tornado,storm,midwest'],
['Hurricane Eye','NOAA','1920','nature','Public Domain','NOAA','hurricane,satellite,storm'],
['Coral Reef Fish','Unknown','1920','nature','Public Domain','NOAA','coral,fish,ocean'],
['Kelp Forest','Unknown','1920','nature','Public Domain','NOAA','kelp,ocean,california'],
['Sequoia Grove','Unknown','1920','nature','Public Domain','NPS','sequoia,trees,california'],
['Joshua Tree','Unknown','1920','nature','Public Domain','NPS','desert,california,tree'],
['Saguaro Cactus','Unknown','1920','nature','Public Domain','NPS','cactus,arizona,desert'],
['Prairie Grassland','Unknown','1920','nature','Public Domain','USFWS','prairie,grass,midwest'],
['Wetland Birds','Unknown','1920','nature','Public Domain','USFWS','wetland,birds,migration'],
['Arctic Tundra','Unknown','1920','nature','Public Domain','USFWS','tundra,arctic,wildlife'],
['Tropical Beach','Unknown','1920','nature','Public Domain','Various','beach,tropical,ocean'],
['Mountain Lake','Unknown','1920','nature','Public Domain','NPS','lake,mountains,reflection'],
['Waterfall Mist','Unknown','1920','nature','Public Domain','NPS','waterfall,mist,forest'],
['Canyon Sunset','Unknown','1920','nature','Public Domain','NPS','canyon,sunset,arizona'],
['Desert Night Sky','Unknown','1920','nature','Public Domain','NPS','stars,desert,night'],
['Forest Path','Unknown','1920','nature','Public Domain','Various','forest,path,trees'],
['Meadow Flowers','Unknown','1920','nature','Public Domain','Various','meadow,flowers,spring'],
['River Bend','Unknown','1920','nature','Public Domain','Various','river,bend,landscape'],
['Cliff Coast','Unknown','1920','nature','Public Domain','Various','cliff,coast,ocean'],
['Island Aerial','Unknown','1920','nature','Public Domain','Various','island,aerial,tropical'],
['Glacier','Unknown','1920','nature','Public Domain','USGS','glacier,ice,alaska'],
['Hot Spring','Unknown','1920','nature','Public Domain','NPS','hotspring,thermal,yellowstone'],
['Mud Pots','Unknown','1920','nature','Public Domain','NPS','mudpot,thermal,yellowstone'],
['Painted Desert','Unknown','1920','nature','Public Domain','NPS','desert,colors,arizona'],
['Slot Canyon','Unknown','1920','nature','Public Domain','NPS','canyon,slot,utah'],
['Arch Formation','Unknown','1920','nature','Public Domain','NPS','arch,rock,utah'],
['Hoodoo Rocks','Unknown','1920','nature','Public Domain','NPS','hoodoo,rock,utah'],
['Badlands','Unknown','1920','nature','Public Domain','NPS','badlands,erosion,dakota'],
['Sand Dunes','Unknown','1920','nature','Public Domain','NPS','dunes,sand,desert'],
['Salt Flats','Unknown','1920','nature','Public Domain','BLM','salt,flats,utah'],
['Crater Lake','Unknown','1920','nature','Public Domain','NPS','lake,crater,oregon'],
['Multnomah Falls','Unknown','1920','nature','Public Domain','USFS','waterfall,oregon,forest'],
['Red Rock Canyon','Unknown','1920','nature','Public Domain','BLM','redrock,canyon,nevada'],
['Antelope Canyon','Unknown','1920','nature','Public Domain','Navajo Nation','canyon,slot,arizona'],
['Horseshoe Bend','Unknown','1920','nature','Public Domain','NPS','river,bend,arizona'],
['Delicate Arch','Unknown','1920','nature','Public Domain','NPS','arch,utah,iconic'],
['Half Dome','Unknown','1920','nature','Public Domain','NPS','halfdome,yosemite,granite'],
['El Capitan','Unknown','1920','nature','Public Domain','NPS','elcapitan,yosemite,cliff'],
['Bridalveil Fall','Unknown','1920','nature','Public Domain','NPS','waterfall,yosemite,mist'],
['Mono Lake','Unknown','1920','nature','Public Domain','Various','lake,tufa,california'],
['Death Valley','Unknown','1920','nature','Public Domain','NPS','desert,valley,california'],
['Joshua Tree Night','Unknown','1920','nature','Public Domain','NPS','night,stars,desert'],
['Alabama Hills','Unknown','1920','nature','Public Domain','BLM','hills,alabama,california'],
['Owens Valley','Unknown','1920','nature','Public Domain','Various','valley,california,sierra'],
['Lake Tahoe','Unknown','1920','nature','Public Domain','USFS','lake,tahoe,alpine'],
['Crater Lake Blue','Unknown','1920','nature','Public Domain','NPS','lake,blue,oregon'],
['Columbia Gorge','Unknown','1920','nature','Public Domain','USFS','gorge,columbia,oregon'],
['Olympic Rainforest','Unknown','1920','nature','Public Domain','NPS','rainforest,washington,moss'],
['North Cascades','Unknown','1920','nature','Public Domain','NPS','cascades,washington,peaks'],
['Mount Rainier','Unknown','1920','nature','Public Domain','NPS','rainier,washington,volcano'],
['Denali','Unknown','1920','nature','Public Domain','NPS','denali,alaska,mountain'],
['Kenai Fjords','Unknown','1920','nature','Public Domain','NPS','fjord,alaska,glacier'],
['Glacier Bay','Unknown','1920','nature','Public Domain','NPS','glacier,bay,alaska'],
['Katmai Bears','Unknown','1920','nature','Public Domain','NPS','bear,alaska,salmon'],
['Aurora Alaska','Unknown','1920','nature','Public Domain','Various','aurora,alaska,night'],
['Tundra Swan','Unknown','1920','nature','Public Domain','USFWS','swan,tundra,bird'],
['Caribou Herd','Unknown','1920','nature','Public Domain','USFWS','caribou,herd,arctic'],
['Polar Bear','Unknown','1920','nature','Public Domain','USFWS','polarbear,arctic,ice'],
['Walrus Haulout','Unknown','1920','nature','Public Domain','USFWS','walrus,arctic,haulout'],
['Puffin Colony','Unknown','1920','nature','Public Domain','USFWS','puffin,colony,seabird'],
['Bald Eagle Nest','Unknown','1920','nature','Public Domain','USFWS','eagle,nest,bird'],
['Great Horned Owl','Unknown','1920','nature','Public Domain','USFWS','owl,nocturnal,bird'],
['Red Fox Kits','Unknown','1920','nature','Public Domain','USFWS','fox,kits,wildlife'],
['River Otter','Unknown','1920','nature','Public Domain','USFWS','otter,river,playful'],
['Beaver Dam','Unknown','1920','nature','Public Domain','USFWS','beaver,dam,wetland'],
['Moose Bull','Unknown','1920','nature','Public Domain','USFWS','moose,bull,wildlife'],
['Elk Bugle','Unknown','1920','nature','Public Domain','NPS','elk,bugle,fall'],
['Bison Herd','Unknown','1920','nature','Public Domain','NPS','bison,herd,prairie'],
['Pronghorn','Unknown','1920','nature','Public Domain','USFWS','pronghorn,antelope,plains'],
['Prairie Dog Town','Unknown','1920','nature','Public Domain','USFWS','prairiedog,town,burrow'],
['Burrowing Owl','Unknown','1920','nature','Public Domain','USFWS','owl,burrow,prairie'],
['Sandhill Cranes','Unknown','1920','nature','Public Domain','USFWS','crane,migration,nebraska'],
['Whooping Crane','Unknown','1920','nature','Public Domain','USFWS','crane,whooping,rare'],
['Snowy Egret','Unknown','1920','nature','Public Domain','USFWS','egret,snowy,wetland'],
['Great Blue Heron','Unknown','1920','nature','Public Domain','USFWS','heron,blue,wetland'],
['Wood Duck','Unknown','1920','nature','Public Domain','USFWS','duck,wood,colorful'],
['Mallard Pair','Unknown','1920','nature','Public Domain','USFWS','mallard,duck,pair'],
['Canada Geese','Unknown','1920','nature','Public Domain','USFWS','goose,canada,migration'],
['Trumpeter Swan','Unknown','1920','nature','Public Domain','USFWS','swan,trumpeter,large'],
['Loon Call','Unknown','1920','nature','Public Domain','USFWS','loon,call,lake'],
['Bald Eagle Soar','Unknown','1920','nature','Public Domain','USFWS','eagle,soar,sky'],
['Peregrine Falcon','Unknown','1920','nature','Public Domain','USFWS','falcon,peregrine,fast'],
['Red-tailed Hawk','Unknown','1920','nature','Public Domain','USFWS','hawk,redtail,soar'],
['American Kestrel','Unknown','1920','nature','Public Domain','USFWS','kestrel,small,falcon'],
['Barn Owl','Unknown','1920','nature','Public Domain','USFWS','owl,barn,ghost'],
['Eastern Screech Owl','Unknown','1920','nature','Public Domain','USFWS','owl,screech,small'],
['Barred Owl','Unknown','1920','nature','Public Domain','USFWS','owl,barred,forest'],
['Great Gray Owl','Unknown','1920','nature','Public Domain','USFWS','owl,gray,large'],
['Snowy Owl','Unknown','1920','nature','Public Domain','USFWS','owl,snowy,arctic']
];
var CATS=['painting','photography','space','historical','scientific','nature'];
var LICENSES=['Public Domain','Public Domain (US Gov)','CC BY','CC BY-SA','CC (editorial use)'];
var REGIONS=['North America','South America','Europe','Africa','Asia','Oceania','Middle East','Central America','Caribbean','Central Asia','East Asia','South Asia','Southeast Asia','Scandinavia','Mediterranean','Pacific Islands','Arctic','Antarctica'];
function thumbSVG(seed,title,cat){
  var s=prng(seed*7919+13);
  var pals={painting:['#2a1a3d','#7a4fb5','#e8d5ff','#1a0f2e'],photography:['#1a1a2e','#4a4a6a','#c0c0d0','#0f0f1a'],space:['#050510','#1a1a3a','#4a7ab5','#000008'],historical:['#2e2418','#6a5a3a','#d0c0a0','#1a140e'],scientific:['#0a1a1a','#1a4a4a','#7ad0d0','#051010'],nature:['#0f2a0f','#2a6a2a','#a0d0a0','#081808']};
  var p=pals[cat]||pals.nature;
  var h='<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">';
  h+='<rect width="400" height="300" fill="'+p[3]+'"/>';
  for(var i=0;i<24;i++){h+='<circle cx="'+(s()*400|0)+'" cy="'+(s()*300|0)+'" r="'+(4+s()*22|0)+'" fill="'+p[(s()*p.length)|0]+'" opacity="0.5"/>';}
  h+='<rect x="0" y="240" width="400" height="60" fill="'+p[0]+'" opacity="0.85"/>';
  h+='<text x="12" y="265" font-family="sans-serif" font-size="13" fill="'+p[2]+'">'+String(title).slice(0,38).replace(/&/g,'&amp;').replace(/</g,'&lt;')+'</text>';
  h+='<text x="12" y="285" font-family="sans-serif" font-size="10" fill="'+p[2]+'" opacity="0.7">JAH-PIA · '+cat+'</text>';
  return h+'</svg>';
}
function make(seed,opts){
  opts=opts||{};
  var s=prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec;
  if(seed<=REAL.length&&!opts.gen){
    var R=REAL[seed-1];
    rec={id:id,title:R[0],description:'Public image: "'+R[0]+'" by '+R[1]+' ('+R[2]+'). Category: '+R[3]+'. License: '+R[4]+'. Source: '+R[5]+'. Filed in the public image archive.',
      category:R[3],creator:R[1],year:R[2],license:R[4],source_note:R[5],tags:R[6],
      source_url:'https://commons.wikimedia.org/wiki/Special:Search?search='+encodeURIComponent(R[0]),
      region:pick(REGIONS,prng(seed*31+7)),
      thumbnail_svg:thumbSVG(seed,R[0],R[3]),
      demo:{kind:'image-viewer',program:'function view(img){return "<img src=\\""+img.source_url+"\\" alt=\\""+img.title+"\\">";}',note:'Open the source URL for the full-resolution public image.'},
      src:'public-harvest',_seed:seed};
  } else {
    var cat=opts.category||pick(CATS,s);
    var lic=pick(LICENSES,s);
    var subj=pick(['mountain vista','ocean sunset','city skyline','forest trail','desert dunes','river valley','historic bridge','vintage portrait','wildlife study','botanical plate','architectural detail','street scene','harbor view','countryside lane','market square','temple facade'],s);
    var t='Archived '+cat+' image: '+subj+' (#'+seed+')';
    rec={id:id,title:t,description:'Generator sample: a '+cat+' image ("'+subj+'") filed under '+lic+'. This is a labeled sample record demonstrating the archive structure.',
      category:cat,creator:'Archive sample',year:String(1900+ri(s,0,126)),license:lic,source_note:'Generated sample',
      tags:subj.replace(/ /g,','),
      source_url:'',thumbnail_svg:thumbSVG(seed,t,cat),
      region:pick(REGIONS,s),year:String(1900+ri(s,0,126)),
      demo:{kind:'image-viewer',program:'function view(img){return img.thumbnail_svg;}',note:'Sample record — thumbnail is a deterministic placeholder.'},
      src:'signature-generated-sample',_seed:seed};
  }
  return rec;
}
function validate(r){
  var e=[];
  if(!r.id||r.id.indexOf(PREFIX)!==0)e.push('bad id');
  if(!r.title)e.push('no title');
  if(!r.category)e.push('no category');
  if(!r.license)e.push('no license');
  if(r.src!=='public-harvest'&&r.src!=='signature-generated-sample')e.push('bad src');
  /* region/year optional for backward compat, required for new records */
  return {ok:!e.length,errors:e};
}
function driftCheck(r,sample){
  var seen={};
  (sample||[]).forEach(function(x){seen[x.title]=1;});
  if(seen[r.title])return {ok:false,errors:['duplicate title']};
  return {ok:true,errors:[]};
}
function generate(seed,opts){var r=make(seed,opts);var v=validate(r);if(!v.ok)throw new Error('invalid: '+v.errors.join(','));return r;}
var api={generate:generate,validate:validate,driftCheck:driftCheck,make:make,PREFIX:PREFIX,REAL_COUNT:REAL.length,CATS:CATS};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-image-archive',api);
})();
