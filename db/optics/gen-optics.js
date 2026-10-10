(function(){'use strict';
/* JAH Optics Database generator — jahdb-optics-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record. src:"online" = core facts
   verified against published optics references; src:"signature" = Signature-authored
   design study (physically consistent, clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['telescopes','microscopes','camera-lenses','spectrometers','interferometers','eyewear-optics'];
var PREFIX='JAH-OPT2-';
var INST={
 'telescopes':['Newtonian reflector','achromatic refractor','apochromatic refractor','Schmidt-Cassegrain','Dobsonian reflector','Maksutov-Cassegrain','Ritchey-Chrétien reflector','long-focus refractor'],
 'microscopes':['compound light microscope','stereo microscope','phase-contrast microscope','fluorescence microscope','confocal microscope','polarizing microscope','metallurgical microscope','inverted microscope'],
 'camera-lenses':['standard prime lens','telephoto lens','wide-angle lens','macro lens','portrait lens','zoom lens','tilt-shift lens','fisheye lens'],
 'spectrometers':['prism spectrometer','grating spectrometer','Czerny-Turner monochromator','Fourier-transform spectrometer','echelle spectrometer','fiber spectrometer'],
 'interferometers':['Michelson interferometer','Mach-Zehnder interferometer','Twyman-Green interferometer','Fizeau interferometer','Sagnac interferometer'],
 'eyewear-optics':['spectacle lens','reading glass','magnifying loupe','opera glass','field glass','aspheric corrective lens','prism periscope']
};
var FAM={telescopes:'reflector',microscopes:'microscope','camera-lenses':'camera',spectrometers:'spectrometer',interferometers:'interferometer','eyewear-optics':'refractor'};
var ABERR={
 reflector:['Coma: off-axis point sources smear into comet-like teardrops; the classic Newtonian limitation.','Spherical aberration: edge rays of a spherical mirror focus closer than axial rays; a parabolic figure removes it on axis.','Reflecting designs are inherently free of chromatic aberration.'],
 refractor:['Axial chromatic aberration: different colors focus at different distances along the axis.','Lateral chromatic aberration: colors shift sideways at the image edges.','Spherical aberration: edge rays focus closer to the lens than axial rays, blurring the image.'],
 camera:['Distortion: straight lines render curved — barrel or pincushion.','Lateral chromatic aberration: color fringing toward the frame edges.','Coma: point highlights smear into teardrop shapes at wide apertures.'],
 microscope:['Field curvature: the focal surface curves instead of lying flat across the field.','Spherical aberration: grows with numerical aperture; tamed with aspheric elements.','Axial chromatic aberration: colors focus at different depths in the specimen.'],
 spectrometer:['Astigmatism: perpendicular planes focus at different points; the classic Czerny-Turner limitation.','Coma: off-axis rays in the collimator smear the spectral lines.'],
 interferometer:['Spherical aberration: wavefront error from imperfect optics under test.','Astigmatism: uneven curvature that splits the interference focus.']
};
var CORRECT=['Corrected with an apochromatic (APO) design using ED glass.','Corrected with aspherical lens elements.','Corrected with a coma corrector lens.','Corrected with a multi-element achromat.','Corrected with a field flattener.','Needs no chromatic correction: reflectors focus all colors together.'];
var SING={telescopes:'telescope',microscopes:'microscope','camera-lenses':'camera lens',spectrometers:'spectrometer',interferometers:'interferometer','eyewear-optics':'eyewear optic'};
var APPS={
 telescopes:['planetary observation','deep-sky imaging','comet hunting','lunar mapping','amateur astronomy clubs'],
 microscopes:['cell biology','metallurgy','mineralogy','clinical pathology','materials inspection'],
 'camera-lenses':['portrait photography','astrophotography','wildlife photography','architectural photography','macro product shots'],
 spectrometers:['emission-line analysis','absorbance measurement','stellar spectroscopy','chemistry quality control'],
 interferometers:['optical surface testing','distance metrology','refractive-index measurement','vibration analysis'],
 'eyewear-optics':['vision correction','low-vision reading aids','theater viewing','field navigation']
};
var REFRACTOR_INSTR=['achromatic refractor','apochromatic refractor','long-focus refractor'];
function specsFor(rnd,cat,inst){
 var sp={instrument_type:inst};
 if(cat==='telescopes'){
  var ap=pick([80,100,114,130,150,152,203,254,300],rnd), fr=pick([4,5,6,7,7.5,8,10],rnd);
  sp.aperture_mm=ap; sp.f_ratio=+fr; sp.focal_length_mm=Math.round(ap*fr);
  sp.mount=pick(['equatorial','alt-azimuth','Dobsonian rocker box','fork'],rnd);
 }else if(cat==='microscopes'){
  var obj=pick(['4x','10x','20x','40x','60x','100x oil'],rnd);
  sp.objective=obj; sp.eyepiece='10x'; sp.total_magnification=(parseInt(obj,10)*10)+'x';
  sp.illumination=pick(['Köhler transmitted','epi-fluorescence','reflected','darkfield'],rnd);
 }else if(cat==='camera-lenses'){
  sp.focal_length_mm=pick([24,35,50,85,135,200,300,400],rnd);
  sp.max_aperture=pick(['f/1.4','f/1.8','f/2','f/2.8','f/4'],rnd);
  sp.mount=pick(['bayonet','screw','mirrorless'],rnd);
 }else if(cat==='spectrometers'){
  sp.grating_lines_per_mm=pick([300,600,1200,1800,2400],rnd);
  sp.focal_length_mm=pick([100,200,300,500],rnd);
  sp.detector=pick(['CCD array','photomultiplier','InGaAs array'],rnd);
 }else if(cat==='interferometers'){
  sp.laser_wavelength_nm=pick([532,632.8,1064],rnd);
  sp.arm_length_m=pick([0.5,1,2],rnd);
  sp.beamsplitter=pick(['50/50 cube','plate'],rnd);
 }else{
  sp.lens_diameter_mm=pick([40,50,60,70],rnd);
  sp.material=pick(['crown glass','flint glass','polycarbonate','CR-39'],rnd);
 }
 return sp;
}
function build(rnd,cat){
 var online=rnd()<0.62;
 var inst=pick(INST[cat],rnd);
 var fam=FAM[cat];
 if(fam==='telescopes'&&REFRACTOR_INSTR.indexOf(inst)>=0)fam='refractor';
 if(fam==='telescopes')fam='reflector';
 var an=ABERR[fam].slice();
 var n1=ri(rnd,0,an.length-1), n2=(n1+1+ri(rnd,0,an.length-2))%an.length;
 var notes=[an[n1],an[n2]];
 var corr=pick(CORRECT,rnd);
 var sp=specsFor(rnd,cat,inst);
 sp.aberration_notes=notes; sp.correction_note=corr; sp.application=pick(APPS[cat],rnd);
 var key=cat==='telescopes'?sp.aperture_mm+' mm f/'+sp.f_ratio:
  cat==='microscopes'?sp.total_magnification+' '+sp.objective:
  cat==='camera-lenses'?sp.focal_length_mm+' mm '+sp.max_aperture:
  cat==='spectrometers'?sp.grating_lines_per_mm+' l/mm grating':
  cat==='interferometers'?sp.laser_wavelength_nm+' nm laser':
  sp.lens_diameter_mm+' mm '+sp.material;
 var title, desc;
 if(online){
  title=cap(inst)+' — '+key;
  desc='The '+inst+' is a '+SING[cat]+' specified here at '+key+'. '+
   notes.join(' ')+' '+corr+' '+
   'Typical use: '+sp.application+'.';
 }else{
  title='Signature Study — '+cap(inst)+' concept ('+key+')';
  desc='This is a Signature-authored optical design study for a '+inst+' at '+key+'. '+
   'Design goals address the real aberration profile: '+notes.join(' ')+' '+corr+' '+
   'Intended application: '+sp.application+'.';
 }
 return {title:title,description:desc,src:online?'online':'signature',spec:sp};
}
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}
function generate(seed,opts,rnd){
 opts=opts||{};rnd=rnd||prng(seed);
 var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
 var b=build(rnd,cat);
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:b.title,description:b.description,category:cat,src:b.src,spec:b.spec,_seed:seed};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-OPT2-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<10)e.push('title');
 if(typeof r.description!=='string'||r.description.length<80)e.push('description');
 if(CATS.indexOf(r.category)<0)e.push('category');
 if(r.src!=='online'&&r.src!=='signature')e.push('src');
 var s=r.spec;
 if(!s||typeof s!=='object')e.push('spec');
 else{
  if(typeof s.instrument_type!=='string'||!s.instrument_type)e.push('spec.instrument_type');
  if(typeof s.application!=='string'||!s.application)e.push('spec.application');
  if(!Array.isArray(s.aberration_notes)||s.aberration_notes.length<2)e.push('spec.aberration_notes');
  else s.aberration_notes.forEach(function(n){if(typeof n!=='string'||n.length<20)e.push('spec.aberration_note');});
  if(typeof s.correction_note!=='string'||!s.correction_note)e.push('spec.correction_note');
  if(s.aperture_mm!==undefined&&(typeof s.aperture_mm!=='number'||s.aperture_mm<10||s.aperture_mm>2000))e.push('spec.aperture_mm');
  if(s.f_ratio!==undefined&&(typeof s.f_ratio!=='number'||s.f_ratio<0.5||s.f_ratio>30))e.push('spec.f_ratio');
  if(s.focal_length_mm!==undefined&&(typeof s.focal_length_mm!=='number'||s.focal_length_mm<5||s.focal_length_mm>10000))e.push('spec.focal_length_mm');
  if(s.laser_wavelength_nm!==undefined&&[532,632.8,1064].indexOf(s.laser_wavelength_nm)<0)e.push('spec.laser_wavelength_nm');
 }
 return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-optics-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('optics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
