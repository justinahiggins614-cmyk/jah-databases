/* JAH Photography Database generator — jahdb-photography-1.0
   Deterministic (mulberry32). Seed -> full photography entry.
   Sourced records draw every fact from the curated dataset below
   (real camera models, lenses, techniques, and film stocks from public
   photographic knowledge). Signature records are homegrown shoot plans,
   always labeled as such.
   Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-PHO-';
var KIND='photography entry';
var CATS=['camera','lens','technique','composition','lighting','film','genre','accessory','shoot-plan'];
/* [model, maker, year, type, mount, note] */
var CAMERAS=[
["Canon EOS R5","Canon","2020","mirrorless full-frame","RF","45 megapixels with 8K video."],
["Canon EOS R6 Mark II","Canon","2022","mirrorless full-frame","RF","24 megapixels; a hybrid stills and video body."],
["Canon EOS 5D Mark IV","Canon","2016","DSLR full-frame","EF","30 megapixels; a longtime professional workhorse."],
["Nikon Z9","Nikon","2021","mirrorless full-frame","Z","45 megapixels; flagship with no mechanical shutter."],
["Nikon Z8","Nikon","2023","mirrorless full-frame","Z","Flagship Z9 power in a smaller body."],
["Nikon D850","Nikon","2017","DSLR full-frame","F","45 megapixels; a DSLR legend."],
["Sony A7 IV","Sony","2021","mirrorless full-frame","E","33 megapixels; the all-rounder."],
["Sony A7R V","Sony","2022","mirrorless full-frame","E","61 megapixels for maximum resolution."],
["Sony A1","Sony","2021","mirrorless full-frame","E","50 megapixels; the speed flagship."],
["Fujifilm X-T5","Fujifilm","2022","mirrorless APS-C","X","40 megapixels with beloved film simulations."],
["Fujifilm X100V","Fujifilm","2020","compact APS-C, fixed 23mm lens","fixed","A fixed-lens street photography favorite."],
["Fujifilm GFX 100S","Fujifilm","2021","medium format","G","102 megapixels of medium format detail."],
["Panasonic Lumix S5 II","Panasonic","2023","mirrorless full-frame","L","Phase-detect autofocus with video strength."],
["OM System OM-1","OM System","2022","mirrorless Micro Four Thirds","Micro Four Thirds","Stacked sensor with computational shooting modes."],
["Leica Q3","Leica","2023","compact full-frame, fixed 28mm lens","fixed","60 megapixels in a luxury fixed-lens body."],
["Leica M11","Leica","2022","rangefinder full-frame","M","A digital rangefinder with 60 megapixels."],
["Hasselblad X2D 100C","Hasselblad","2022","medium format","XCD","100 megapixels of medium format."],
["Pentax K-3 Mark III","Pentax","2021","DSLR APS-C","K","An optical-viewfinder flagship."],
["Canon EOS Rebel T7","Canon","2018","DSLR APS-C","EF and EF-S","24 megapixels; a beginner DSLR."],
["Nikon D3500","Nikon","2018","DSLR APS-C","F","24 megapixels; a beginner DSLR."],
["Sony ZV-E10","Sony","2021","mirrorless APS-C","E","Built for vlogging."],
["Canon EOS R50","Canon","2023","mirrorless APS-C","RF","A beginner-friendly mirrorless body."],
["Nikon Z fc","Nikon","2021","mirrorless APS-C","Z","Retro styling on a modern Z body."],
["Fujifilm X-S20","Fujifilm","2023","mirrorless APS-C","X","A travel-ready hybrid."],
["Panasonic Lumix GH6","Panasonic","2022","mirrorless Micro Four Thirds","Micro Four Thirds","A video-first Micro Four Thirds body."],
["Sony FX3","Sony","2021","cinema full-frame","E","A compact cinema-line camera."],
["Canon EOS R3","Canon","2021","mirrorless full-frame","RF","A sports flagship with eye-control autofocus."],
["Nikon Z6 III","Nikon","2024","mirrorless full-frame","Z","24 megapixels with a partially stacked sensor."],
["Leica SL3","Leica","2024","mirrorless full-frame","L","60 megapixels on the L mount."],
["Pentax 17","Pentax","2024","35mm half-frame film compact","fixed","A brand-new half-frame film camera."]
];
/* [name, maker, focal, aperture, mount, note] */
var LENSES=[
["RF 24-70mm f/2.8L IS USM","Canon","24-70mm","f/2.8","RF","The professional standard zoom."],
["NIKKOR Z 24-70mm f/2.8 S","Nikon","24-70mm","f/2.8","Z","The professional standard zoom."],
["FE 24-70mm F2.8 GM II","Sony","24-70mm","f/2.8","E","The professional standard zoom."],
["EF 50mm f/1.8 STM","Canon","50mm","f/1.8","EF","The nifty fifty; a budget prime."],
["AF-S 50mm f/1.8G","Nikon","50mm","f/1.8","F","A budget 50mm prime."],
["FE 85mm F1.4 GM","Sony","85mm","f/1.4","E","A classic portrait prime."],
["RF 70-200mm F2.8L IS USM","Canon","70-200mm","f/2.8","RF","The professional telephoto zoom."],
["18-50mm F2.8 DC DN","Sigma","18-50mm","f/2.8","multiple APS-C","A fast APS-C standard zoom."],
["28-75mm F/2.8 Di III VXD G2","Tamron","28-75mm","f/2.8","E and Z","A lightweight standard zoom."],
["XF 35mm f/1.4 R","Fujifilm","35mm","f/1.4","X","A beloved normal prime for X mount."],
["NIKKOR Z 35mm f/1.8 S","Nikon","35mm","f/1.8","Z","A compact wide prime."],
["RF 100-500mm F4.5-7.1L","Canon","100-500mm","f/4.5-7.1","RF","A wildlife super-telephoto zoom."],
["150-600mm F5-6.3 DG DN OS","Sigma","150-600mm","f/5-6.3","multiple","A budget-friendly wildlife zoom."],
["90mm F2.8 Macro G OSS","Sony","90mm","f/2.8","E","A 1:1 macro prime."],
["12-24mm F4 DG HSM Art","Sigma","12-24mm","f/4","multiple","An ultra-wide zoom."],
["70-200mm f/2.8E FL ED VR","Nikon","70-200mm","f/2.8","F","The professional telephoto zoom."]
];
/* [name, note] */
var TECHNIQUES=[
["Rule of thirds","Place key elements along the lines that divide the frame into thirds."],
["Leading lines","Use lines in the scene to pull the eye toward the subject."],
["Golden hour","Shoot in the warm low light just after sunrise or before sunset."],
["Blue hour","Shoot in the deep blue twilight after sunset or before sunrise."],
["Long exposure","Use slow shutter speeds on a tripod to blur motion in water and clouds."],
["Bokeh","Wide apertures turn background points of light into soft circles."],
["HDR","Blend multiple exposures to hold detail in shadows and highlights."],
["Exposure bracketing","Shoot a burst of exposures to merge later."],
["Focus stacking","Combine shots focused at different distances for deep sharpness."],
["Panning","Track a moving subject with a slow shutter, around 1/30s, to blur the background."],
["Depth of field","Aperture, distance, and focal length control how much is sharp."],
["Shutter speed","Controls motion blur and how much light reaches the sensor."],
["Aperture","The lens opening; controls depth of interest and light."],
["ISO","Sensor sensitivity; raise it in low light at the cost of noise."],
["Exposure triangle","Aperture, shutter speed, and ISO trade off against each other."],
["White balance","Set the color temperature so whites look white."],
["Metering modes","Matrix, center-weighted, and spot metering read light differently."],
["Histogram","The graph of tones; keep it off the hard edges."],
["Manual mode","You set aperture, shutter, and ISO yourself."],
["Aperture priority","You set the aperture; the camera picks the shutter speed."],
["Shutter priority","You set the shutter speed; the camera picks the aperture."],
["Zone focusing","Prefocus to a zone and shoot street scenes without refocusing."],
["Hyperfocal distance","Focus at the point that maximizes depth of field."],
["Back-button focus","Move autofocus to a rear button to separate it from the shutter."],
["Burst mode","Hold the shutter for a sequence; pick the sharpest frame."],
["Image stabilization","Lens or sensor stabilization lets you handhold slower speeds."],
["ND filter","A neutral density filter cuts light for long exposures in daylight."],
["Polarizing filter","Cuts reflections and deepens skies; rotate to taste."],
["Double exposure","Layer two images in-camera or in editing for surreal blends."],
["Light painting","Move a light through a long exposure in the dark."],
["Silhouette","Expose for a bright background and let the subject go black."],
["Reflections","Puddles, glass, and water double your composition."],
["Negative space","Empty areas give the subject room to breathe."],
["Framing","Use doorways, arches, or branches to frame the subject."],
["Symmetry","Mirror compositions feel calm and formal."],
["Fill flash","A touch of flash lifts shadows in daylight portraits."],
["Bounce flash","Aim flash at a ceiling or wall for softer light."],
["High key","Bright, low-contrast images with airy whites."],
["Low key","Dark, moody images built on shadow."],
["Black and white","Strip color to emphasize shape, texture, and tone."]
];
var COMPOSITION=[
["Rule of thirds","Divide the frame into thirds and place subjects on the lines."],
["Leading lines","Roads, rivers, and rails guide the eye."],
["Framing","Natural frames add depth and context."],
["Symmetry","Balanced halves feel deliberate and calm."],
["Negative space","Emptiness emphasizes the subject."],
["Foreground interest","Something close adds depth to landscapes."],
["Patterns and texture","Repeating shapes reward a closer look."],
["Viewpoint","Change your height and angle before you shoot."],
["Depth layers","Foreground, middle, and background build dimension."],
["Color contrast","Complementary colors make subjects pop."],
["Simplicity","Remove everything that is not the picture."],
["Golden ratio","A spiral variant of thirds for classical balance."]
];
var LIGHTING=[
["Golden hour","Warm, low, directional sunlight near sunrise and sunset."],
["Blue hour","Cool twilight glow after the sun dips below the horizon."],
["Rembrandt lighting","A triangle of light on the shadowed cheek; classic portraiture."],
["Butterfly lighting","Light from above and front; glamorous and sculpting."],
["Loop lighting","A small nose shadow looping to one side; flattering and easy."],
["Split lighting","Half the face lit, half in shadow; dramatic."],
["Rim lighting","Light from behind outlines the subject."],
["Softbox","A large diffused source for soft, flattering light."],
["Window light","Free, beautiful, directional light for portraits."],
["Overcast light","Clouds are nature's softbox; even and gentle."],
["Backlight","Shoot into the light for glow and silhouette."],
["Harsh midday","Hard overhead sun; seek shade or embrace the contrast."]
];
var FILM=[
["Kodak Portra 400","Kodak","A portrait film with soft, natural color."],
["Kodak Gold 200","Kodak","A warm, affordable consumer color film."],
["Kodak Tri-X 400","Kodak","The classic black-and-white photojournalism film."],
["Fujifilm Velvia 50","Fujifilm","A saturated slide film for landscapes."],
["Ilford HP5 Plus","Ilford","A versatile 400-speed black-and-white film."],
["Ilford Delta 3200","Ilford","An ultra-fast black-and-white film for low light."],
["Cinestill 800T","Cinestill","A tungsten-balanced color film with halation glow."],
["Kodak Ektar 100","Kodak","An ultra-fine-grain color negative film."]
];
var GENRES=[
["Portrait","People photography, from studio to candid."],
["Landscape","Land, sea, and sky at their most dramatic."],
["Street","Unposed life in public places."],
["Macro","Tiny worlds magnified."],
["Wildlife","Animals in their habitat; patience required."],
["Astrophotography","Stars, the Milky Way, and the moon."],
["Wedding","A couple's day, told in moments."],
["Documentary","Truthful storytelling through images."],
["Sports","Peak action frozen in time."],
["Product","Clean, sharp images that sell."]
];
var ACCESSORIES=[
["Tripod","The foundation of sharp long exposures."],
["Monopod","Support with mobility for sports and events."],
["Camera bag","Protection and organization on the move."],
["Memory cards","Fast, reliable cards; carry spares."],
["Spare batteries","Cold and video drain batteries fast."],
["Lens cleaning kit","Blower, brush, and microfiber cloth."],
["External flash","A speedlight opens up portrait and event work."],
["Reflector","Bounce light into shadows for free."]
];
var ANGLES=[
["","", ""],
["beginners"," \u2014 beginners"," Start here if you are new; the basics carry far."],
["quick facts"," \u2014 quick facts",""],
["working pros"," \u2014 working pros"," Professionals squeeze the last drop from this topic."],
["on a budget"," \u2014 on a budget"," Great results do not require the priciest gear."],
["field notes"," \u2014 field notes",""]
];
function comboGen(j,nE,nA,nG){
  var per=nA*nG;
  var e=j%nE, c=Math.floor(j/nE)%per, part=Math.floor(j/(nE*per));
  return {e:e,a:Math.floor(c/nG),g:c%nG,part:part};
}
var SRC="JAH Photography curated dataset v1 \u2014 real cameras, lenses, techniques, and film stocks from public photographic knowledge.";
var SIGSRC="JAH Signature generator \u2014 homegrown shoot plans, clearly labeled as generated.";
function mkRec(seed,cat,title,summary,details,prov,src){
  while(summary.length<80)summary+=" Keep practicing deliberately; the craft rewards steady work.";
  return {id:PREFIX+String(seed).padStart(6,"0"),title:title,category:cat,record_kind:KIND,
    summary:summary,details:details,provenance:prov,source:src,_seed:seed};
}
var CAM_ASPECTS=[
["overview",function(x){return x[0]+" ("+x[1]+", "+x[2]+"): "+x[5];}],
["key specs",function(x){return "Type: "+x[3]+"; mount: "+x[4]+". "+x[5];}],
["best for",function(x){return "Match the body to the work: stills, video, travel, or studio.";}],
["handling",function(x){return "Handling and menus matter as much as specs; try before you buy.";}],
["strengths",function(x){return "Its strengths: "+x[5];}],
["considerations",function(x){return "Weigh price, lens ecosystem, and weight against your needs.";}],
["for beginners",function(x){return "Beginners should master light and composition before chasing bodies.";}],
["quick facts",function(x){return x[1]+" "+x[0]+" ("+x[2]+"), "+x[4]+" mount.";}]
];
var LENS_ASPECTS=[
["overview",function(x){return x[0]+" ("+x[1]+"): "+x[5];}],
["focal length",function(x){return "Focal range "+x[2]+" on "+x[4]+" mount.";}],
["aperture",function(x){return "Maximum aperture "+x[3]+"; wider means more light and blur.";}],
["best for",function(x){return "Pick focal length for the subject first, aperture second.";}],
["handling",function(x){return "Weight and balance on your body matter on long days.";}],
["strengths",function(x){return "Its strengths: "+x[5];}],
["considerations",function(x){return "Check mount compatibility before buying any lens.";}],
["quick facts",function(x){return x[1]+" "+x[0]+", "+x[2]+" "+x[3]+".";}]
];
var TECH_ASPECTS=[
["overview",function(x){return x[0]+": "+x[1]+" Put it into practice on your next shoot and compare results.";}],
["how it works",function(x){return "The mechanics: "+x[1];}],
["when to use",function(x){return "Reach for this technique when the scene calls for it, not by default.";}],
["starting settings",function(x){return "Start with the book's suggestion, then adjust by eye using the histogram.";}],
["common mistakes",function(x){return "Beginners rush; slow down and check the edges of the frame.";}],
["quick tips",function(x){return "Practice deliberately; review on a big screen.";}]
];
var SIMPLE_ASPECTS=[
["overview",function(x){return x[0]+": "+x[1]+" Study the masters, shoot deliberately, and review every frame.";}],
["how it works",function(x){return "In practice: "+x[1];}],
["when to use",function(x){return "Use it when it serves the picture, not as a rule.";}],
["common mistakes",function(x){return "Overuse is the classic mistake; restraint reads as skill.";}],
["quick tips",function(x){return "Study masters of the craft, then shoot a hundred frames.";}],
["field notes",function(x){return "Field note: "+x[1];}]
];
function profRec(seed,j,entries,aspects,cat,detailFn){
  var cb=comboGen(j,entries.length,aspects.length,ANGLES.length);
  var x=entries[cb.e],a=aspects[cb.a],g=ANGLES[cb.g];
  var title=x[0]+" \u2014 "+a[0]+(cb.part>0?" (Part "+(cb.part+1)+")":"")+g[1];
  var summary=a[1](x)+g[2];
  var d=detailFn(x);d.aspect=a[0];d.angle=g[0]||"standard";
  return mkRec(seed,cat,title,summary,d,"sourced",SRC);
}
var PLAN_LOCS=["city streets","a coastline","mountains","a forest","a desert","a small town","a market","a river","a rooftop","a garden"];
var PLAN_TIMES=["dawn","morning","midday","afternoon","golden hour","blue hour"];
function planRec(seed,j){
  var gi=Math.floor(j/(PLAN_LOCS.length*PLAN_TIMES.length))%GENRES.length;
  var li=Math.floor(j/PLAN_TIMES.length)%PLAN_LOCS.length;
  var ti=j%PLAN_TIMES.length;
  var part=Math.floor(j/(GENRES.length*PLAN_LOCS.length*PLAN_TIMES.length));
  var gn=GENRES[gi][0],lc=PLAN_LOCS[li],tm=PLAN_TIMES[ti];
  var title="Shoot plan: "+gn+" at "+lc+" \u2014 "+tm+(part>0?" (v"+(part+1)+")":"");
  var summary="Signature-generated shoot plan \u2014 homegrown material, adapt freely. Genre: "+gn+". Location: "+lc+". Light: "+tm+". "+
    "Shot list: an establishing wide, three detail studies, a human moment, and one experimental frame. Pack water, spare batteries, and patience.";
  return mkRec(seed,"shoot-plan",title,summary,{genre:gn,location:lc,light:tm,variant:part+1,
    shot_list:["establishing wide","three detail studies","a human moment","one experimental frame"]},"signature",SIGSRC);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var s=((seed-1)%10000)+1;
  var explicit=!!opts.category;
  var cat=opts.category;
  if(!cat){
    if(s<=2500)cat="camera";
    else if(s<=3500)cat="lens";
    else if(s<=6500)cat="technique";
    else if(s<=7300)cat="composition";
    else if(s<=8100)cat="lighting";
    else if(s<=8500)cat="film";
    else if(s<=9000)cat="genre";
    else if(s<=9400)cat="accessory";
    else cat="shoot-plan";
  }
  function ord(base){return explicit?(s-1):(s-base);}
  if(cat==="camera")return profRec(seed,ord(1),CAMERAS,CAM_ASPECTS,"camera",function(x){return {model:x[0],maker:x[1],year:x[2],type:x[3],mount:x[4],note:x[5]};});
  if(cat==="lens")return profRec(seed,ord(2501),LENSES,LENS_ASPECTS,"lens",function(x){return {lens:x[0],maker:x[1],focal:x[2],aperture:x[3],mount:x[4],note:x[5]};});
  if(cat==="technique")return profRec(seed,ord(3501),TECHNIQUES,TECH_ASPECTS,"technique",function(x){return {technique:x[0],note:x[1]};});
  if(cat==="composition")return profRec(seed,ord(6501),COMPOSITION,SIMPLE_ASPECTS,"composition",function(x){return {principle:x[0],note:x[1]};});
  if(cat==="lighting")return profRec(seed,ord(7301),LIGHTING,SIMPLE_ASPECTS,"lighting",function(x){return {lighting:x[0],note:x[1]};});
  if(cat==="film")return profRec(seed,ord(8101),FILM,SIMPLE_ASPECTS,"film",function(x){return {stock:x[0],maker:x[1],note:x[2]};});
  if(cat==="genre")return profRec(seed,ord(8501),GENRES,SIMPLE_ASPECTS,"genre",function(x){return {genre:x[0],note:x[1]};});
  if(cat==="accessory")return profRec(seed,ord(9001),ACCESSORIES,SIMPLE_ASPECTS,"accessory",function(x){return {accessory:x[0],note:x[1]};});
  if(cat==="shoot-plan")return planRec(seed,ord(9401));
  return profRec(seed,ord(1),CAMERAS,CAM_ASPECTS,"camera",function(x){return {model:x[0],maker:x[1],year:x[2],type:x[3],mount:x[4],note:x[5]};});
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!/^JAH-PHO-\d{6,7}$/.test(r.id||""))e.push("id");
  if(typeof r.title!=="string"||!r.title.length)e.push("title");
  if(CATS.indexOf(r.category)<0)e.push("category");
  if(r.record_kind!==KIND)e.push("record_kind");
  if(typeof r.summary!=="string"||r.summary.length<80)e.push("summary");
  if(!r.details||typeof r.details!=="object")e.push("details");
  if(r.provenance!=="sourced"&&r.provenance!=="signature")e.push("provenance");
  if(typeof r.source!=="string"||!r.source.length)e.push("source");
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++)if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:["already in archive: "+rec.id]};
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-photography-1.0",generate:generate,validate:validate,driftCheck:driftCheck,categories:CATS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("photography",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
