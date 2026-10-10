(function(){'use strict';
/* JAH Electromagnetism Database generator — jahdb-electromagnetism-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record. src:"online" = core facts
   verified against published EM references; src:"signature" = Signature-authored
   spectrum study (exact c=fλ math, clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['radio','microwave','infrared','visible','ultraviolet','x-ray','gamma'];
var PREFIX='JAH-EM-';
var C=299792458;
var BANDS={
 radio:{wl:'1 mm – 100,000 km',freq:'3 Hz – 300 GHz',uses:'AM/FM radio, television, radar, radio astronomy'},
 microwave:{wl:'1 mm – 1 m',freq:'300 MHz – 300 GHz',uses:'microwave ovens, radar, satellite communication'},
 infrared:{wl:'700 nm – 1 mm',freq:'300 GHz – 430 THz',uses:'thermal imaging, TV remotes, night vision'},
 visible:{wl:'400 – 700 nm',freq:'430 – 750 THz',uses:'human vision, photography, illumination'},
 ultraviolet:{wl:'10 – 400 nm',freq:'750 THz – 30 PHz',uses:'sterilization, fluorescence, tanning'},
 'x-ray':{wl:'0.01 – 10 nm',freq:'30 PHz – 30 EHz',uses:'medical imaging, security screening, materials testing'},
 gamma:{wl:'under 0.01 nm',freq:'above 30 EHz',uses:'cancer radiotherapy, sterilization of medical equipment'}
};
var DEVICES={
 radio:['FM broadcast receiver','shortwave radio set','radio telescope dish','VHF marine radio','AM transmitter tower'],
 microwave:['magnetron radar set','microwave oven (2.45 GHz cavity)','satellite uplink dish','police speed radar','weather radar array'],
 infrared:['thermographic camera','TV infrared remote','night-vision goggles','IR motion sensor','FTIR spectrometer source'],
 visible:['CCD camera','LED panel','fiber-optic link','photographic enlarger','laser pointer (red, 650 nm)'],
 ultraviolet:['mercury-vapor lamp','UV water purifier','fluorescence microscope illuminator','UV lithography stepper','germicidal UVC lamp'],
 'x-ray':['CT scanner','airport baggage scanner','X-ray diffractometer','dental X-ray unit','industrial weld inspector'],
 gamma:['cobalt-60 irradiator','gamma-ray telescope','PET scanner detector ring','industrial radiography source','food irradiation facility']
};
var MAXWELL=[
 'Gauss\u2019s law: the electric flux through any closed surface is proportional to the charge enclosed.',
 'Gauss\u2019s law for magnetism: magnetic field lines always close on themselves — there are no magnetic monopoles.',
 'Faraday\u2019s law: a changing magnetic field induces an electric field.',
 'Amp\u00e8re-Maxwell law: electric currents and changing electric fields generate magnetic fields.'
];
var SPEED='All electromagnetic waves travel at 3.00 × 10⁸ m/s in vacuum.';
var STUDY_F={
 radio:[88e6,100e6,1e9],microwave:[2.45e9,10e9,24e9],infrared:[3e13,3e14],
 visible:[4.3e14,5.5e14,7.5e14],ultraviolet:[1e15,1e16],'x-ray':[1e17,1e18],gamma:[1e20,1e21]
};
function fmtHz(f){
 if(f>=1e18)return (f/1e18)+' EHz';
 if(f>=1e15)return (f/1e15)+' PHz';
 if(f>=1e12)return (f/1e12)+' THz';
 if(f>=1e9)return (f/1e9)+' GHz';
 if(f>=1e6)return (f/1e6)+' MHz';
 return f+' Hz';
}
function fmtM(m){
 if(m>=1)return m.toFixed(2)+' m';
 if(m>=1e-3)return (m*1e3).toFixed(2)+' mm';
 if(m>=1e-6)return (m*1e6).toFixed(1)+' µm';
 if(m>=1e-9)return (m*1e9).toFixed(2)+' nm';
 return (m*1e12).toFixed(2)+' pm';
}
function build(rnd,cat){
 var online=rnd()<0.62;
 var band=BANDS[cat];
 var dev=pick(DEVICES[cat],rnd);
 var mw=pick(MAXWELL,rnd);
 var title,desc,spec;
 if(online){
  title=cap(dev)+' — '+cap(cat)+' band';
  desc='The '+dev.toLowerCase()+' operates in the '+cat+' band: wavelengths '+band.wl+', frequencies '+band.freq+'. '+
   mw+' '+SPEED+' '+
   'Common uses of this band: '+band.uses+'.';
  spec={band:cat,wavelength_range:band.wl,frequency_range:band.freq,device:dev,
   maxwell_principle:mw,propagation_note:SPEED,band_applications:band.uses};
 }else{
  var f=pick(STUDY_F[cat],rnd);
  var lam=C/f;
  title='Signature Study — '+cap(cat)+' at '+fmtHz(f);
  desc='This is a Signature-authored spectrum study: a '+fmtHz(f)+' '+cat+' wave has wavelength λ = c/f = '+fmtM(lam)+'. '+
   'Band reference: '+cat+' spans '+band.wl+' ('+band.freq+'). '+mw+' '+
   'Study device context: '+dev.toLowerCase()+'.';
  spec={band:cat,study_frequency:fmtHz(f),computed_wavelength:fmtM(lam),wavelength_range:band.wl,
   frequency_range:band.freq,device_context:dev,maxwell_principle:mw,propagation_note:SPEED};
 }
 return {title:title,description:desc,src:online?'online':'signature',spec:spec};
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
 if(!/^JAH-EM-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<10)e.push('title');
 if(typeof r.description!=='string'||r.description.length<80)e.push('description');
 if(CATS.indexOf(r.category)<0)e.push('category');
 if(r.src!=='online'&&r.src!=='signature')e.push('src');
 var s=r.spec;
 if(!s||typeof s!=='object')e.push('spec');
 else{
  if(s.band!==r.category)e.push('spec.band');
  if(typeof s.wavelength_range!=='string'||!s.wavelength_range)e.push('spec.wavelength_range');
  if(typeof s.frequency_range!=='string'||!s.frequency_range)e.push('spec.frequency_range');
  if(typeof s.maxwell_principle!=='string'||!/law/i.test(s.maxwell_principle))e.push('spec.maxwell');
  if(typeof s.propagation_note!=='string'||!/10⁸|10\^8|3\.00/.test(s.propagation_note))e.push('spec.propagation');
  if(r.src==='online'&&(typeof s.device!=='string'||!s.device))e.push('spec.device');
 }
 return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-electromagnetism-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('electromagnetism',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
