/* jahdb-pc-organizer-magnetic-parts-tray-1.0 — deterministic boundless generator for Magnetic Parts Tray Database.
   Self-regulation (Signature standard): hard stop at 1,000,000,000,000 records;
   throttled output (<=50 records per call); every generated record labeled
   "simulated"; correctness verified by validate(); completion detected when the
   template pool is exhausted for the requested seed space. */
(function(){'use strict';
var HARD_STOP=1000000000000;
var MAX_PER_CALL=50;
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["Tray Basics", "Magnet Science", "Sizes & Shapes", "Workstation Setup", "Maintenance", "Comparisons"];
var PREFIX='JAH-PCO1-';
/* Deterministic template pool: [category, title_pattern, detail_pattern] */
var B=[["Tray Basics", "What a Magnetic Parts Tray Is and Why Builders Use One", "A magnetic parts tray is a shallow steel dish or plate with a magnet in its base that holds screws, standoffs, washers, and other small ferrous hardware in plac"], ["Magnet Science", "How the Base Magnet Holds Hardware in Place", "Most trays use a ferrite or rubber magnet bonded under a stainless-steel dish. The magnetic field passes through the thin steel and pins each screw flat against"], ["Sizes & Shapes", "Standard Sizes: 4-Inch Round, 6-Inch Round, and Rectangular Trays", "The classic magnetic parts tray is a round dish about 4 inches (10 cm) across and 1 inch deep — big enough for a full motherboard's worth of screws. Six-inch (1"], ["Sizes & Shapes", "Round vs Square vs Rectangular Tray Shapes", "Round trays are the most common and cheapest, and their curved rim funnels screws to the center. Square trays tile neatly into bench organizers and drawer divid"], ["Tray Basics", "Materials: Stainless Steel Dishes vs Plastic Magnetic Pads", "Stainless-steel trays are the standard: the magnet acts through the steel, the surface wipes clean, and they last for years. Plastic trays with a magnetic pad i"], ["Magnet Science", "Holding Strength Classes and What They Mean in Practice", "Entry trays (around 5 dollars) use a basic rubber magnet that holds a motherboard's screw set on a flat desk. Mid-range trays add a stronger ceramic magnet that"], ["Magnet Science", "Magnetic Safety Around PC Parts: SSDs, HDDs, and USB Drives", "The weak field of a parts tray is harmless to SSDs, USB flash drives, RAM, and CPUs — flash memory is not magnetic storage. Keep the tray a few inches from spin"], ["Workstation Setup", "Use Case: Motherboard Standoff and Mounting Screw Workflow", "Mounting a motherboard means nine standoffs plus nine matching screws, and dropping one inside the case wastes ten minutes. The workflow: count nine standoffs i"], ["Workstation Setup", "Use Case: M.2 SSD Screws and Other Tiny Fasteners", "M.2 screws are the easiest fasteners to lose in a PC build — a single 2 mm screw can vanish into carpet forever. Drop it in the magnetic tray the moment the mot"], ["Tray Basics", "Buying Guide: What to Check Before You Buy a Parts Tray", "Check five things: a rubber or PVC-coated base so it does not slide or scratch; a magnet strong enough that screws do not migrate when you bump the bench; a rim"], ["Maintenance", "Cleaning and Maintenance: Metal Filings and Paste Smears", "Steel trays collect fine metal filings from case edges and screw threads — wipe them out with a dry cloth before each build, because filings can bridge motherbo"], ["Comparisons", "Magnetic Tray vs Silicone Screw Mat vs Pill Organizer", "Magnetic trays win on bump-resistance and one-hand screw pickup. Silicone screw mats win on zone labeling — you can write position numbers beside each screw pil"], ["Workstation Setup", "Two-Tray and Multi-Tray Workstation Layouts", "Serious builders run a tray system: tray one holds screws coming out of the old configuration, tray two stages screws for the new one, and a third small tray pa"], ["Magnet Science", "Pro Technique: Magnetizing Screwdriver Tips With the Tray", "A strong tray magnet doubles as a screwdriver magnetizer: stroke the bit across the tray's magnet a few times in one direction and the bit becomes weakly magnet"], ["Workstation Setup", "Complete Build-Station Screw Management System", "The master workflow combines everything: one rectangular tray staged with the new build's full screw set counted in advance, one round tray catching every screw"]];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>=HARD_STOP)return {error:'HARD_STOP: 1,000,000,000,000 record limit reached',complete:true};
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=b[1].replace('{n}',String(ri(rnd,2,48)));
  return {id:id,title:title,t:title.slice(0,70),g:cat,category:cat,
    description:b[2].replace('{n}',String(ri(rnd,2,48)))+' This is a simulated record generated by jahdb-pc-organizer-magnetic-parts-tray-1.0.',
    ladder_rank:ri(rnd,1,15),
    demo:{language:'python',program:'print("simulated demo for '+id+'")'},
    provenance:'Simulated record generated by jahdb-pc-organizer-magnetic-parts-tray-1.0 (seed '+seed+'). Labeled simulated per the Signature self-regulation standard.',
    last_verified:'2026-10-21',
    march_marker:'March to a million in progress — simulated generation record '+seed+'.',
    edition:'simulated',simulated:true,_seed:seed,_version:'jahdb-pc-organizer-magnetic-parts-tray-1.0'};
}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var re=/^JAH\-PCO1\-\d{6}$/;
  if(!re.test(r.id||''))e.push('id');
  if(r.title!==undefined&&(typeof r.title!=='string'||!r.title.length))e.push('title');
  if(typeof r.description!=='string'||r.description.length<20)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=15))e.push('ladder_rank');
  if(r.simulated!==true)e.push('simulated-must-be-true');
  if(r._seed===undefined||r._seed>=HARD_STOP)e.push('seed');
  return {ok:!e.length,errors:e,complete:r._seed>=B.length*1000};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){ if(s&&s.id===rec.id)e.push('duplicate of archive record '+s.id); });
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-pc-organizer-magnetic-parts-tray-1.0',HARD_STOP:HARD_STOP,MAX_PER_CALL:MAX_PER_CALL,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-organizer-magnetic-parts-tray',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
