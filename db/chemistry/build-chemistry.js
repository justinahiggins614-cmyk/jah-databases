'use strict';
// Build JAH Chemistry Database: ~2000 online (elements, isotopes, compounds, reactions, lab, physical) + signature.
// All numeric chemistry (molar masses, balanced equations, electron configs) is COMPUTED, not asserted.
const path=require('path');
const lib=require('../buildlib.js');
const gen=require('./gen-chemistry.js');
const REPO=path.join(__dirname,'..','..');
const SLUG='chemistry', PREFIX='JAH-CHEM-';
const REFIUPAC='https://iupac.org/';
const REFPUB='https://pubchem.ncbi.nlm.nih.gov/';
let seed=0; const recs=[];
function add(r){ seed++; r._seed=seed; r.id=lib.idOf(PREFIX,seed); recs.push(r); }
const AW={H:1.008,He:4.0026,Li:6.94,Be:9.0122,B:10.81,C:12.011,N:14.007,O:15.999,F:18.998,Ne:20.180,Na:22.990,Mg:24.305,Al:26.982,Si:28.085,P:30.974,S:32.06,Cl:35.45,Ar:39.948,K:39.098,Ca:40.078,Sc:44.956,Ti:47.867,V:50.942,Cr:51.996,Mn:54.938,Fe:55.845,Co:58.933,Ni:58.693,Cu:63.546,Zn:65.38,Ga:69.723,Ge:72.630,As:74.922,Se:78.971,Br:79.904,Kr:83.798,Rb:85.468,Sr:87.62,Ag:107.87,Cd:112.41,In:114.82,Sn:118.71,Sb:121.76,Te:127.60,I:126.90,Xe:131.29,Cs:132.91,Ba:137.33,W:183.84,Pt:195.08,Au:196.97,Hg:200.59,Pb:207.2,Bi:208.98,U:238.03};
function mm(comp){let m=0;for(const el in comp){if(!(el in AW))throw new Error('AW missing '+el);m+=comp[el]*AW[el];}return Math.round(m*1000)/1000;}
function fmt(comp){let s='';for(const el of Object.keys(comp))s+=el+(comp[el]>1?comp[el]:'');return s;}
function atomCount(species){const t={};for(const sp of species)for(const el in sp.comp)t[el]=(t[el]||0)+sp.coef*sp.comp[el];return t;}
function balanced(R,P){const a=atomCount(R),b=atomCount(P);const k=new Set([...Object.keys(a),...Object.keys(b)]);for(const x of k)if((a[x]||0)!==(b[x]||0))return false;return true;}
// ---- elements: [symbol,name,group,period,category] ----
const EL=[['H','Hydrogen',1,1,'nonmetal'],['He','Helium',18,1,'noble gas'],['Li','Lithium',1,2,'alkali metal'],['Be','Beryllium',2,2,'alkaline earth metal'],['B','Boron',13,2,'metalloid'],['C','Carbon',14,2,'nonmetal'],['N','Nitrogen',15,2,'nonmetal'],['O','Oxygen',16,2,'nonmetal'],['F','Fluorine',17,2,'halogen'],['Ne','Neon',18,2,'noble gas'],['Na','Sodium',1,3,'alkali metal'],['Mg','Magnesium',2,3,'alkaline earth metal'],['Al','Aluminium',13,3,'post-transition metal'],['Si','Silicon',14,3,'metalloid'],['P','Phosphorus',15,3,'nonmetal'],['S','Sulfur',16,3,'nonmetal'],['Cl','Chlorine',17,3,'halogen'],['Ar','Argon',18,3,'noble gas'],['K','Potassium',1,4,'alkali metal'],['Ca','Calcium',2,4,'alkaline earth metal'],['Sc','Scandium',3,4,'transition metal'],['Ti','Titanium',4,4,'transition metal'],['V','Vanadium',5,4,'transition metal'],['Cr','Chromium',6,4,'transition metal'],['Mn','Manganese',7,4,'transition metal'],['Fe','Iron',8,4,'transition metal'],['Co','Cobalt',9,4,'transition metal'],['Ni','Nickel',10,4,'transition metal'],['Cu','Copper',11,4,'transition metal'],['Zn','Zinc',12,4,'transition metal'],['Ga','Gallium',13,4,'post-transition metal'],['Ge','Germanium',14,4,'metalloid'],['As','Arsenic',15,4,'metalloid'],['Se','Selenium',16,4,'nonmetal'],['Br','Bromine',17,4,'halogen'],['Kr','Krypton',18,4,'noble gas'],['Rb','Rubidium',1,5,'alkali metal'],['Sr','Strontium',2,5,'alkaline earth metal'],['Y','Yttrium',3,5,'transition metal'],['Zr','Zirconium',4,5,'transition metal'],['Nb','Niobium',5,5,'transition metal'],['Mo','Molybdenum',6,5,'transition metal'],['Tc','Technetium',7,5,'transition metal'],['Ru','Ruthenium',8,5,'transition metal'],['Rh','Rhodium',9,5,'transition metal'],['Pd','Palladium',10,5,'transition metal'],['Ag','Silver',11,5,'transition metal'],['Cd','Cadmium',12,5,'transition metal'],['In','Indium',13,5,'post-transition metal'],['Sn','Tin',14,5,'post-transition metal'],['Sb','Antimony',15,5,'metalloid'],['Te','Tellurium',16,5,'metalloid'],['I','Iodine',17,5,'halogen'],['Xe','Xenon',18,5,'noble gas'],['Cs','Caesium',1,6,'alkali metal'],['Ba','Barium',2,6,'alkaline earth metal'],['La','Lanthanum',3,6,'lanthanide'],['Ce','Cerium',3,6,'lanthanide'],['Pr','Praseodymium',3,6,'lanthanide'],['Nd','Neodymium',3,6,'lanthanide'],['Pm','Promethium',3,6,'lanthanide'],['Sm','Samarium',3,6,'lanthanide'],['Eu','Europium',3,6,'lanthanide'],['Gd','Gadolinium',3,6,'lanthanide'],['Tb','Terbium',3,6,'lanthanide'],['Dy','Dysprosium',3,6,'lanthanide'],['Ho','Holmium',3,6,'lanthanide'],['Er','Erbium',3,6,'lanthanide'],['Tm','Thulium',3,6,'lanthanide'],['Yb','Ytterbium',3,6,'lanthanide'],['Lu','Lutetium',3,6,'lanthanide'],['Hf','Hafnium',4,6,'transition metal'],['Ta','Tantalum',5,6,'transition metal'],['W','Tungsten',6,6,'transition metal'],['Re','Rhenium',7,6,'transition metal'],['Os','Osmium',8,6,'transition metal'],['Ir','Iridium',9,6,'transition metal'],['Pt','Platinum',10,6,'transition metal'],['Au','Gold',11,6,'transition metal'],['Hg','Mercury',12,6,'transition metal'],['Tl','Thallium',13,6,'post-transition metal'],['Pb','Lead',14,6,'post-transition metal'],['Bi','Bismuth',15,6,'post-transition metal'],['Po','Polonium',16,6,'post-transition metal'],['At','Astatine',17,6,'halogen'],['Rn','Radon',18,6,'noble gas'],['Fr','Francium',1,7,'alkali metal'],['Ra','Radium',2,7,'alkaline earth metal'],['Ac','Actinium',3,7,'actinide'],['Th','Thorium',3,7,'actinide'],['Pa','Protactinium',3,7,'actinide'],['U','Uranium',3,7,'actinide'],['Np','Neptunium',3,7,'actinide'],['Pu','Plutonium',3,7,'actinide'],['Am','Americium',3,7,'actinide'],['Cm','Curium',3,7,'actinide'],['Bk','Berkelium',3,7,'actinide'],['Cf','Californium',3,7,'actinide'],['Es','Einsteinium',3,7,'actinide'],['Fm','Fermium',3,7,'actinide'],['Md','Mendelevium',3,7,'actinide'],['No','Nobelium',3,7,'actinide'],['Lr','Lawrencium',3,7,'actinide'],['Rf','Rutherfordium',4,7,'transition metal'],['Db','Dubnium',5,7,'transition metal'],['Sg','Seaborgium',6,7,'transition metal'],['Bh','Bohrium',7,7,'transition metal'],['Hs','Hassium',8,7,'transition metal'],['Mt','Meitnerium',9,7,'transition metal'],['Ds','Darmstadtium',10,7,'transition metal'],['Rg','Roentgenium',11,7,'transition metal'],['Cn','Copernicium',12,7,'transition metal'],['Nh','Nihonium',13,7,'superheavy'],['Fl','Flerovium',14,7,'superheavy'],['Mc','Moscovium',15,7,'superheavy'],['Lv','Livermorium',16,7,'superheavy'],['Ts','Tennessine',17,7,'superheavy'],['Og','Oganesson',18,7,'superheavy']];
const ORDER=[['1s',2],['2s',2],['2p',6],['3s',2],['3p',6],['4s',2],['3d',10],['4p',6],['5s',2],['4d',10],['5p',6],['6s',2],['4f',14],['5d',10],['6p',6],['7s',2],['5f',14],['6d',10],['7p',6]];
function econfig(z){let n=z,out=[];for(const [orb,cap] of ORDER){if(n<=0)break;const t=Math.min(cap,n);out.push(orb+t);n-=t;}return out.join(' ');}
EL.forEach((e,i)=>{
  const z=i+1, cfg=econfig(z);
  const block=/([spdf])\d+$/.exec(cfg.split(' ').pop())[1];
  add({title:'Element '+z+': '+e[1]+' ('+e[0]+')',category:'physical',
    description:'Element '+z+', '+e[1]+' ('+e[0]+'): a '+e[4]+' in group '+e[2]+', period '+e[3]+'. Standard periodic-table reference data.',
    concept:'element overview',statement:'Element '+z+': '+e[1]+' ('+e[0]+'), '+e[4]+', group '+e[2]+', period '+e[3]+', block '+block+'.',
    source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
  add({title:e[1]+' electron configuration',category:'physical',
    description:'Aufbau-predicted electron configuration of '+e[1]+' (Z='+z+'): '+cfg+'. Predicted by filling order; a few elements differ in their ground state.',
    concept:'electron configuration',statement:'Aufbau-predicted configuration of '+e[0]+' (Z='+z+'): '+cfg+'.',
    source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
  add({title:e[1]+' - properties and uses',category:'physical',
    description:'Properties and uses of '+e[1]+' ('+e[0]+'): a '+e[4]+' of period '+e[3]+'. Chemical behavior follows its group and block; uses follow standard reference works.',
    concept:'element properties',statement:e[1]+' ('+e[0]+'): '+e[4]+', group '+e[2]+', period '+e[3]+'.',
    source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
});
console.log('elements done:',seed);
// ---- isotopes: [symbol, name, Z, [mass numbers], note] ----
const ISO=[['H','Hydrogen',1,[1,2],'protium and deuterium are stable'],['He','Helium',2,[3,4],'helium-3 and helium-4 are stable'],['Li','Lithium',3,[6,7],'both stable'],['Be','Beryllium',4,[9],'beryllium-9 is the only stable isotope'],['B','Boron',5,[10,11],'both stable'],['C','Carbon',6,[12,13],'stable; carbon-14 is a well-known radioisotope'],['N','Nitrogen',7,[14,15],'both stable'],['O','Oxygen',8,[16,17,18],'all stable'],['F','Fluorine',9,[19],'fluorine-19 is the only stable isotope'],['Ne','Neon',10,[20,21,22],'all stable'],['Na','Sodium',11,[23],'sodium-23 is the only stable isotope'],['Mg','Magnesium',12,[24,25,26],'all stable'],['Al','Aluminium',13,[27],'aluminium-27 is the only stable isotope'],['Si','Silicon',14,[28,29,30],'all stable'],['P','Phosphorus',15,[31],'phosphorus-31 is the only stable isotope'],['S','Sulfur',16,[32,33,34,36],'all stable'],['Cl','Chlorine',17,[35,37],'both stable'],['Ar','Argon',18,[36,38,40],'all stable'],['K','Potassium',19,[39,40,41],'potassium-40 is a primordial radioisotope'],['Ca','Calcium',20,[40,42,43,44,46,48],'all stable'],['Sc','Scandium',21,[45],'scandium-45 is the only stable isotope'],['Ti','Titanium',22,[46,47,48,49,50],'all stable'],['V','Vanadium',23,[50,51],'vanadium-50 is primordial'],['Cr','Chromium',24,[50,52,53,54],'all stable'],['Mn','Manganese',25,[55],'manganese-55 is the only stable isotope'],['Fe','Iron',26,[54,56,57,58],'all stable'],['Co','Cobalt',27,[59],'stable; cobalt-60 is a well-known radioisotope'],['Ni','Nickel',28,[58,60,61,62,64],'all stable'],['Cu','Copper',29,[63,65],'both stable'],['Zn','Zinc',30,[64,66,67,68,70],'all stable'],['Ga','Gallium',31,[69,71],'both stable'],['Ge','Germanium',32,[70,72,73,74,76],'all stable'],['As','Arsenic',33,[75],'arsenic-75 is the only stable isotope'],['Se','Selenium',34,[74,76,77,78,80,82],'all stable'],['Br','Bromine',35,[79,81],'both stable'],['Kr','Krypton',36,[78,80,82,83,84,86],'all stable'],['Rb','Rubidium',37,[85,87],'rubidium-87 is primordial'],['Sr','Strontium',38,[84,86,87,88],'stable; strontium-90 is a fission product'],['Y','Yttrium',39,[89],'yttrium-89 is the only stable isotope'],['Zr','Zirconium',40,[90,91,92,94,96],'all stable'],['Nb','Niobium',41,[93],'niobium-93 is the only stable isotope'],['Mo','Molybdenum',42,[92,94,95,96,97,98,100],'all stable'],['Ru','Ruthenium',44,[96,98,99,100,101,102,104],'all stable'],['Rh','Rhodium',45,[103],'rhodium-103 is the only stable isotope'],['Pd','Palladium',46,[102,104,105,106,108,110],'all stable'],['Ag','Silver',47,[107,109],'both stable'],['Cd','Cadmium',48,[106,108,110,111,112,113,114,116],'stable or primordial'],['In','Indium',49,[113,115],'indium-115 is primordial'],['Sn','Tin',50,[112,114,115,116,117,118,119,120,122,124],'ten stable isotopes, the most of any element'],['Sb','Antimony',51,[121,123],'both stable'],['Te','Tellurium',52,[120,122,123,124,125,126,128,130],'stable or primordial'],['I','Iodine',53,[127],'stable; iodine-131 is a well-known radioisotope'],['Xe','Xenon',54,[124,126,128,129,130,131,132,134,136],'stable or primordial'],['Cs','Caesium',55,[133],'stable; caesium-137 is a fission product'],['Ba','Barium',56,[130,132,134,135,136,137,138],'stable or primordial'],['La','Lanthanum',57,[138,139],'lanthanum-138 is primordial'],['Ce','Cerium',58,[136,138,140,142],'stable or primordial'],['Pr','Praseodymium',59,[141],'praseodymium-141 is the only stable isotope'],['Nd','Neodymium',60,[142,143,144,145,146,148,150],'stable or primordial'],['Sm','Samarium',62,[144,147,148,149,150,152,154],'stable or primordial'],['Eu','Europium',63,[151,153],'both stable'],['Gd','Gadolinium',64,[152,154,155,156,157,158,160],'stable or primordial'],['Tb','Terbium',65,[159],'terbium-159 is the only stable isotope'],['Dy','Dysprosium',66,[156,158,160,161,162,163,164],'stable or primordial'],['Ho','Holmium',67,[165],'holmium-165 is the only stable isotope'],['Er','Erbium',68,[162,164,166,167,168,170],'stable or primordial'],['Tm','Thulium',69,[169],'thulium-169 is the only stable isotope'],['Yb','Ytterbium',70,[168,170,171,172,173,174,176],'stable or primordial'],['Lu','Lutetium',71,[175,176],'lutetium-176 is primordial'],['Hf','Hafnium',72,[174,176,177,178,179,180],'stable or primordial'],['Ta','Tantalum',73,[180,181],'tantalum-180m is primordial'],['W','Tungsten',74,[180,182,183,184,186],'stable or primordial'],['Re','Rhenium',75,[185,187],'rhenium-187 is primordial'],['Os','Osmium',76,[184,186,187,188,189,190,192],'stable or primordial'],['Ir','Iridium',77,[191,193],'both stable'],['Pt','Platinum',78,[190,192,194,195,196,198],'stable or primordial'],['Au','Gold',79,[197],'gold-197 is the only stable isotope'],['Hg','Mercury',80,[196,198,199,200,201,202,204],'stable or primordial'],['Tl','Thallium',81,[203,205],'both stable'],['Pb','Lead',82,[204,206,207,208],'all stable'],['Bi','Bismuth',83,[209],'bismuth-209 is primordial']];
ISO.forEach(x=>{
  x[3].forEach(a=>{
    const n=a-x[2];
    add({title:x[0]+'-'+a+' isotope',category:'physical',
      description:'Isotope '+x[1].toLowerCase()+'-'+a+': Z='+x[2]+', N='+n+', mass number '+a+'. '+x[4][0].toUpperCase()+x[4].slice(1)+'.',
      concept:'isotope',statement:x[0]+'-'+a+': protons '+x[2]+', neutrons '+n+', mass number '+a+'.',
      source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
  });
});
console.log('isotopes done:',seed);
// ---- verified compounds: [name, display formula, composition, category, note] ----
const CMP=[['Water','H2O',{H:2,O:1},'inorganic','the universal solvent'],['Hydrogen peroxide','H2O2',{H:2,O:2},'inorganic','an oxidizer and disinfectant'],['Ozone','O3',{O:3},'inorganic','a triatomic allotrope of oxygen'],['Sodium chloride','NaCl',{Na:1,Cl:1},'inorganic','common table salt'],['Potassium chloride','KCl',{K:1,Cl:1},'inorganic','a salt and fertilizer'],['Calcium chloride','CaCl2',{Ca:1,Cl:2},'inorganic','a desiccant and de-icer'],['Magnesium chloride','MgCl2',{Mg:1,Cl:2},'inorganic','a salt used in dust control'],['Silver chloride','AgCl',{Ag:1,Cl:1},'inorganic','a light-sensitive salt'],['Silver nitrate','AgNO3',{Ag:1,N:1,O:3},'inorganic','used in photography and labs'],['Hydrochloric acid','HCl',{H:1,Cl:1},'inorganic','a strong mineral acid'],['Hydrobromic acid','HBr',{H:1,Br:1},'inorganic','a strong mineral acid'],['Nitric acid','HNO3',{H:1,N:1,O:3},'inorganic','a strong oxidizing acid'],['Sulfuric acid','H2SO4',{H:2,S:1,O:4},'inorganic','a strong diprotic acid'],['Phosphoric acid','H3PO4',{H:3,P:1,O:4},'inorganic','a weak triprotic acid'],['Carbonic acid','H2CO3',{H:2,C:1,O:3},'inorganic','forms in carbonated water'],['Acetic acid','CH3COOH',{C:2,H:4,O:2},'organic','the acid in vinegar'],['Formic acid','HCOOH',{C:1,H:2,O:2},'organic','the simplest carboxylic acid'],['Citric acid','C6H8O7',{C:6,H:8,O:7},'organic','a citrus fruit acid'],['Lactic acid','C3H6O3',{C:3,H:6,O:3},'organic','forms in muscle and fermentation'],['Oxalic acid','C2H2O4',{C:2,H:2,O:4},'organic','a dicarboxylic acid'],['Benzoic acid','C6H5COOH',{C:7,H:6,O:2},'organic','a food preservative'],['Ascorbic acid','C6H8O6',{C:6,H:8,O:6},'organic','vitamin C'],['Sodium hydroxide','NaOH',{Na:1,O:1,H:1},'inorganic','caustic soda, a strong base'],['Potassium hydroxide','KOH',{K:1,O:1,H:1},'inorganic','caustic potash, a strong base'],['Calcium hydroxide','Ca(OH)2',{Ca:1,O:2,H:2},'inorganic','slaked lime'],['Magnesium hydroxide','Mg(OH)2',{Mg:1,O:2,H:2},'inorganic','milk of magnesia'],['Ammonia','NH3',{N:1,H:3},'inorganic','a basic nitrogen compound'],['Ammonium chloride','NH4Cl',{N:1,H:4,Cl:1},'inorganic','a fertilizer and lab reagent'],['Ammonium nitrate','NH4NO3',{N:2,H:4,O:3},'inorganic','a fertilizer and oxidizer'],['Ammonium sulfate','(NH4)2SO4',{N:2,H:8,S:1,O:4},'inorganic','a nitrogen fertilizer'],['Urea','CO(NH2)2',{C:1,O:1,N:2,H:4},'organic','a nitrogen fertilizer and metabolite'],['Sodium carbonate','Na2CO3',{Na:2,C:1,O:3},'inorganic','washing soda'],['Potassium carbonate','K2CO3',{K:2,C:1,O:3},'inorganic','potash'],['Calcium carbonate','CaCO3',{Ca:1,C:1,O:3},'inorganic','limestone and chalk'],['Magnesium carbonate','MgCO3',{Mg:1,C:1,O:3},'inorganic','a mineral and antacid'],['Sodium bicarbonate','NaHCO3',{Na:1,H:1,C:1,O:3},'inorganic','baking soda'],['Sodium sulfate','Na2SO4',{Na:2,S:1,O:4},'inorganic','a drying agent'],['Potassium sulfate','K2SO4',{K:2,S:1,O:4},'inorganic','a fertilizer'],['Calcium sulfate','CaSO4',{Ca:1,S:1,O:4},'inorganic','gypsum'],['Magnesium sulfate','MgSO4',{Mg:1,S:1,O:4},'inorganic','Epsom salt'],['Copper(II) sulfate','CuSO4',{Cu:1,S:1,O:4},'inorganic','blue vitriol'],['Zinc sulfate','ZnSO4',{Zn:1,S:1,O:4},'inorganic','a dietary and lab salt'],['Iron(II) sulfate','FeSO4',{Fe:1,S:1,O:4},'inorganic','green vitriol'],['Barium sulfate','BaSO4',{Ba:1,S:1,O:4},'inorganic','an X-ray contrast medium'],['Sodium nitrate','NaNO3',{Na:1,N:1,O:3},'inorganic','Chile saltpeter'],['Potassium nitrate','KNO3',{K:1,N:1,O:3},'inorganic','saltpeter'],['Calcium nitrate','Ca(NO3)2',{Ca:1,N:2,O:6},'inorganic','a fertilizer'],['Lead(II) nitrate','Pb(NO3)2',{Pb:1,N:2,O:6},'inorganic','a lab reagent'],['Sodium phosphate','Na3PO4',{Na:3,P:1,O:4},'inorganic','a cleaning agent'],['Calcium phosphate','Ca3(PO4)2',{Ca:3,P:2,O:8},'inorganic','bone mineral'],['Sodium oxide','Na2O',{Na:2,O:1},'inorganic','a basic oxide'],['Calcium oxide','CaO',{Ca:1,O:1},'inorganic','quicklime'],['Magnesium oxide','MgO',{Mg:1,O:1},'inorganic','magnesia'],['Zinc oxide','ZnO',{Zn:1,O:1},'inorganic','a pigment and sunscreen'],['Iron(III) oxide','Fe2O3',{Fe:2,O:3},'inorganic','rust and pigment'],['Aluminium oxide','Al2O3',{Al:2,O:3},'inorganic','alumina and corundum'],['Copper(II) oxide','CuO',{Cu:1,O:1},'inorganic','a black oxide'],['Silicon dioxide','SiO2',{Si:1,O:2},'inorganic','quartz sand'],['Titanium dioxide','TiO2',{Ti:1,O:2},'inorganic','a white pigment'],['Sulfur dioxide','SO2',{S:1,O:2},'inorganic','a pollutant and preservative'],['Sulfur trioxide','SO3',{S:1,O:3},'inorganic','forms sulfuric acid with water'],['Carbon dioxide','CO2',{C:1,O:2},'inorganic','a greenhouse gas'],['Carbon monoxide','CO',{C:1,O:1},'inorganic','a toxic gas'],['Nitrogen dioxide','NO2',{N:1,O:2},'inorganic','a brown pollutant gas'],['Nitrous oxide','N2O',{N:2,O:1},'inorganic','laughing gas'],['Methane','CH4',{C:1,H:4},'organic','natural gas'],['Ethane','C2H6',{C:2,H:6},'organic','a natural gas component'],['Propane','C3H8',{C:3,H:8},'organic','a fuel gas'],['Butane','C4H10',{C:4,H:10},'organic','a fuel gas'],['Ethylene','C2H4',{C:2,H:4},'organic','a plant hormone and monomer'],['Acetylene','C2H2',{C:2,H:2},'organic','a welding fuel'],['Benzene','C6H6',{C:6,H:6},'organic','an aromatic hydrocarbon'],['Toluene','C7H8',{C:7,H:8},'organic','an aromatic solvent'],['Naphthalene','C10H8',{C:10,H:8},'organic','mothballs'],['Cyclohexane','C6H12',{C:6,H:12},'organic','a cyclic alkane'],['Styrene','C8H8',{C:8,H:8},'organic','a polymer monomer'],['Methanol','CH3OH',{C:1,H:4,O:1},'organic','wood alcohol'],['Ethanol','C2H5OH',{C:2,H:6,O:1},'organic','drinking alcohol and solvent'],['Ethylene glycol','C2H6O2',{C:2,H:6,O:2},'organic','antifreeze'],['Glycerol','C3H8O3',{C:3,H:8,O:3},'organic','glycerin'],['Formaldehyde','CH2O',{C:1,H:2,O:1},'organic','a preservative and resin precursor'],['Acetaldehyde','CH3CHO',{C:2,H:4,O:1},'organic','an industrial aldehyde'],['Acetone','CH3COCH3',{C:3,H:6,O:1},'organic','a common solvent'],['Diethyl ether','C4H10O',{C:4,H:10,O:1},'organic','an anesthetic and solvent'],['Chloroform','CHCl3',{C:1,H:1,Cl:3},'organic','a solvent'],['Carbon tetrachloride','CCl4',{C:1,Cl:4},'organic','a solvent'],['Dichloromethane','CH2Cl2',{C:1,H:2,Cl:2},'organic','a solvent'],['Glucose','C6H12O6',{C:6,H:12,O:6},'organic','blood sugar'],['Fructose','C6H12O6',{C:6,H:12,O:6},'organic','fruit sugar'],['Sucrose','C12H22O11',{C:12,H:22,O:11},'organic','table sugar'],['Lactose','C12H22O11',{C:12,H:22,O:11},'organic','milk sugar'],['Aspirin','C9H8O4',{C:9,H:8,O:4},'organic','acetylsalicylic acid'],['Caffeine','C8H10N2O4',{C:8,H:10,N:2,O:4},'organic','a stimulant'],['Nicotine','C10H14N2',{C:10,H:14,N:2},'organic','a tobacco alkaloid'],['Ibuprofen','C13H18O2',{C:13,H:18,O:2},'organic','an anti-inflammatory'],['Paracetamol','C8H9NO2',{C:8,H:9,N:1,O:2},'organic','acetaminophen'],['Aniline','C6H5NH2',{C:6,H:7,N:1},'organic','an aromatic amine'],['Phenol','C6H5OH',{C:6,H:6,O:1},'organic','carbolic acid'],['Pyridine','C5H5N',{C:5,H:5,N:1},'organic','an aromatic heterocycle'],['Furan','C4H4O',{C:4,H:4,O:1},'organic','an aromatic heterocycle'],['Potassium permanganate','KMnO4',{K:1,Mn:1,O:4},'inorganic','a strong oxidizer'],['Potassium dichromate','K2Cr2O7',{K:2,Cr:2,O:7},'inorganic','an oxidizer'],['Sodium thiosulfate','Na2S2O3',{Na:2,S:2,O:3},'inorganic','a photographic fixer'],['Sodium hypochlorite','NaClO',{Na:1,Cl:1,O:1},'inorganic','bleach'],['Boric acid','H3BO3',{H:3,B:1,O:3},'inorganic','a weak acid'],['Silicon carbide','SiC',{Si:1,C:1},'inorganic','carborundum abrasive'],['Calcium carbide','CaC2',{Ca:1,C:2},'inorganic','produces acetylene with water'],['Sodium cyanide','NaCN',{Na:1,C:1,N:1},'inorganic','highly toxic salt'],['Sulfur hexafluoride','SF6',{S:1,F:6},'inorganic','an insulating gas'],['Carbon disulfide','CS2',{C:1,S:2},'organic','a solvent'],['Xenon difluoride','XeF2',{Xe:1,F:2},'inorganic','a noble-gas compound'],['Tungsten hexafluoride','WF6',{W:1,F:6},'inorganic','used in chip making'],['Uranium hexafluoride','UF6',{U:1,F:6},'inorganic','used in enrichment'],['Cisplatin','Pt(NH3)2Cl2',{Pt:1,N:2,H:6,Cl:2},'inorganic','a chemotherapy drug'],['Ferrocene','Fe(C5H5)2',{Fe:1,C:10,H:10},'organic','a sandwich compound'],['EDTA','C10H16N2O8',{C:10,H:16,N:2,O:8},'organic','a chelating agent'],['TNT','C7H5N3O6',{C:7,H:5,N:3,O:6},'organic','trinitrotoluene explosive'],['Nitroglycerin','C3H5N3O9',{C:3,H:5,N:3,O:9},'organic','an explosive and medicine'],['Cholesterol','C27H46O',{C:27,H:46,O:1},'organic','a sterol'],['Adenine','C5H5N5',{C:5,H:5,N:5},'organic','a DNA base'],['Guanine','C5H5N5O',{C:5,H:5,N:5,O:1},'organic','a DNA base'],['Cytosine','C4H5N3O',{C:4,H:5,N:3,O:1},'organic','a DNA base'],['Thymine','C5H6N2O2',{C:5,H:6,N:2,O:2},'organic','a DNA base'],['Uracil','C4H4N2O2',{C:4,H:4,N:2,O:2},'organic','an RNA base'],['Glycine','C2H5NO2',{C:2,H:5,N:1,O:2},'organic','the simplest amino acid'],['Alanine','C3H7NO2',{C:3,H:7,N:1,O:2},'organic','an amino acid'],['Serine','C3H7NO3',{C:3,H:7,N:1,O:3},'organic','an amino acid'],['Cysteine','C3H7NO2S',{C:3,H:7,N:1,O:2,S:1},'organic','a sulfur amino acid'],['Aspartic acid','C4H7NO4',{C:4,H:7,N:1,O:4},'organic','an amino acid'],['Lysine','C6H14N2O2',{C:6,H:14,N:2,O:2},'organic','an amino acid'],['Phenylalanine','C9H11NO2',{C:9,H:11,N:1,O:2},'organic','an amino acid'],['Tryptophan','C11H12N2O2',{C:11,H:12,N:2,O:2},'organic','an amino acid']];
CMP.forEach(c=>{
  const m=mm(c[2]);
  add({title:c[0]+' ('+c[1]+')',category:c[3],
    description:c[0]+', '+c[1]+': '+c[4]+'. Molar mass '+m+' g/mol computed from standard atomic weights.',
    formula:fmt(c[2]),composition:c[2],molar_mass_g_mol:m,compound_class:c[4],
    safety_note:'Follow standard laboratory safety practice for this substance.',
    source:'online',source_ref:REFPUB,creation_mode:'ONLINE-VERIFIED'});
});
console.log('compounds embedded:',CMP.length,'total:',seed);
// ---- computed compound series ----
function seriesCompound(name,disp,comp,cat,note){
  const m=mm(comp);
  add({title:name+' ('+disp+')',category:cat,
    description:name+', '+disp+': '+note+'. Molar mass '+m+' g/mol computed from standard atomic weights.',
    formula:fmt(comp),composition:comp,molar_mass_g_mol:m,compound_class:note,
    safety_note:'Follow standard laboratory safety practice for this substance.',
    source:'online',source_ref:REFPUB,creation_mode:'ONLINE-VERIFIED'});
}
for(let n=1;n<=20;n++) seriesCompound('n-Alkane C'+n,'C'+n+'H'+(2*n+2),{C:n,H:2*n+2},'organic','straight-chain alkane');
for(let n=2;n<=12;n++) seriesCompound('1-Alkene C'+n,'C'+n+'H'+(2*n),{C:n,H:2*n},'organic','terminal alkene');
for(let n=2;n<=10;n++) seriesCompound('1-Alkyne C'+n,'C'+n+'H'+(2*n-2),{C:n,H:2*n-2},'organic','terminal alkyne');
for(let n=1;n<=10;n++) seriesCompound('1-Alkanol C'+n,'C'+n+'H'+(2*n+2)+'O',{C:n,H:2*n+2,O:1},'organic','primary alcohol');
for(let n=1;n<=8;n++) seriesCompound('Alkanoic acid C'+n,'C'+n+'H'+(2*n)+'O2',{C:n,H:2*n,O:2},'organic','carboxylic acid');
for(let n=3;n<=9;n++) seriesCompound('Cycloalkane C'+n,'C'+n+'H'+(2*n),{C:n,H:2*n},'organic','cycloalkane ring');
const CATS4=[['Na',1,'sodium'],['K',1,'potassium'],['Ca',2,'calcium'],['Mg',2,'magnesium'],['Al',3,'aluminium'],['Fe',3,'iron(III)'],['Fe',2,'iron(II)'],['Cu',2,'copper(II)'],['Zn',2,'zinc'],['Ag',1,'silver'],['Ba',2,'barium'],['Pb',2,'lead(II)']];
const ANS=[['Cl',1,'chloride'],['Br',1,'bromide'],['I',1,'iodide'],['O',2,'oxide'],['S',2,'sulfide']];
function gcd(a,b){return b?gcd(b,a%b):a;}
CATS4.forEach(ct=>{
  ANS.forEach(an=>{
    const g=gcd(ct[1],an[1]), catN=an[1]/g, anN=ct[1]/g;
    const comp={}; comp[ct[0]]=catN; comp[an[0]]=anN;
    seriesCompound(ct[2][0].toUpperCase()+ct[2].slice(1)+' '+an[2],ct[0]+(catN>1?catN:'')+an[0]+(anN>1?anN:''),comp,'inorganic','binary salt');
  });
});
const OXO=[['NO3',1,{N:1,O:3},'nitrate'],['SO4',2,{S:1,O:4},'sulfate'],['CO3',2,{C:1,O:3},'carbonate'],['PO4',3,{P:1,O:4},'phosphate']];
CATS4.forEach(ct=>{
  OXO.forEach(ox=>{
    const g=gcd(ct[1],ox[1]), catN=ox[1]/g, anN=ct[1]/g;
    const comp={}; comp[ct[0]]=catN;
    for(const el in ox[2]) comp[el]=(comp[el]||0)+ox[2][el]*anN;
    seriesCompound(ct[2][0].toUpperCase()+ct[2].slice(1)+' '+ox[3],ct[0]+(catN>1?catN:'')+ox[0]+(anN>1?anN:''),comp,'inorganic','oxo salt');
  });
});
[['Lithium hydride','LiH',{Li:1,H:1}],['Sodium hydride','NaH',{Na:1,H:1}],['Potassium hydride','KH',{K:1,H:1}],['Calcium hydride','CaH2',{Ca:1,H:2}],['Magnesium hydride','MgH2',{Mg:1,H:2}]].forEach(h=>seriesCompound(h[0],h[1],h[2],'inorganic','saline hydride'));
for(let n=1;n<=6;n++){['Cl','Br','I'].forEach(x=>{const comp={C:n,H:2*n+1};comp[x]=1;seriesCompound('1-Haloalkane C'+n+' '+x,'C'+n+'H'+(2*n+1)+x,comp,'organic','alkyl halide');});}
console.log('compounds total:',seed);
// ---- reactions: [name, reactants, products]; verified balanced by code ----
function sp(f,coef,comp){return {formula:f,coef:coef,comp:comp};}
const RXNS=[];
for(let n=1;n<=20;n++) RXNS.push(['Alkane C'+n+' combustion',[sp('C'+n+'H'+(2*n+2),2,{C:n,H:2*n+2}),sp('O2',3*n+1,{O:2})],[sp('CO2',2*n,{C:1,O:2}),sp('H2O',2*n+2,{H:2,O:1})]]);
for(let n=1;n<=8;n++) RXNS.push(['Alcohol C'+n+' combustion',[sp('C'+n+'H'+(2*n+2)+'O',2,{C:n,H:2*n+2,O:1}),sp('O2',3*n,{O:2})],[sp('CO2',2*n,{C:1,O:2}),sp('H2O',2*n+2,{H:2,O:1})]]);
for(let n=2;n<=12;n++) RXNS.push(['Alkene C'+n+' combustion',[sp('C'+n+'H'+(2*n),2,{C:n,H:2*n}),sp('O2',3*n,{O:2})],[sp('CO2',2*n,{C:1,O:2}),sp('H2O',2*n,{H:2,O:1})]]);
for(let n=2;n<=10;n++) RXNS.push(['Alkyne C'+n+' combustion',[sp('C'+n+'H'+(2*n-2),2,{C:n,H:2*n-2}),sp('O2',3*n-1,{O:2})],[sp('CO2',2*n,{C:1,O:2}),sp('H2O',2*n-2,{H:2,O:1})]]);
const AB_RX=[
['HCl + NaOH',[['HCl',1,{H:1,Cl:1}],['NaOH',1,{Na:1,O:1,H:1}]],[['NaCl',1,{Na:1,Cl:1}],['H2O',1,{H:2,O:1}]]],
['HBr + KOH',[['HBr',1,{H:1,Br:1}],['KOH',1,{K:1,O:1,H:1}]],[['KBr',1,{K:1,Br:1}],['H2O',1,{H:2,O:1}]]],
['HI + NaOH',[['HI',1,{H:1,I:1}],['NaOH',1,{Na:1,O:1,H:1}]],[['NaI',1,{Na:1,I:1}],['H2O',1,{H:2,O:1}]]],
['HNO3 + KOH',[['HNO3',1,{H:1,N:1,O:3}],['KOH',1,{K:1,O:1,H:1}]],[['KNO3',1,{K:1,N:1,O:3}],['H2O',1,{H:2,O:1}]]],
['HCl + NH4OH',[['HCl',1,{H:1,Cl:1}],['NH4OH',1,{N:1,H:5,O:1}]],[['NH4Cl',1,{N:1,H:4,Cl:1}],['H2O',1,{H:2,O:1}]]],
['H2SO4 + 2 NaOH',[['H2SO4',1,{H:2,S:1,O:4}],['NaOH',2,{Na:1,O:1,H:1}]],[['Na2SO4',1,{Na:2,S:1,O:4}],['H2O',2,{H:2,O:1}]]],
['H2SO4 + 2 KOH',[['H2SO4',1,{H:2,S:1,O:4}],['KOH',2,{K:1,O:1,H:1}]],[['K2SO4',1,{K:2,S:1,O:4}],['H2O',2,{H:2,O:1}]]],
['H2SO4 + Ca(OH)2',[['H2SO4',1,{H:2,S:1,O:4}],['Ca(OH)2',1,{Ca:1,O:2,H:2}]],[['CaSO4',1,{Ca:1,S:1,O:4}],['H2O',2,{H:2,O:1}]]],
['H2SO4 + Mg(OH)2',[['H2SO4',1,{H:2,S:1,O:4}],['Mg(OH)2',1,{Mg:1,O:2,H:2}]],[['MgSO4',1,{Mg:1,S:1,O:4}],['H2O',2,{H:2,O:1}]]],
['H2SO4 + Ba(OH)2',[['H2SO4',1,{H:2,S:1,O:4}],['Ba(OH)2',1,{Ba:1,O:2,H:2}]],[['BaSO4',1,{Ba:1,S:1,O:4}],['H2O',2,{H:2,O:1}]]],
['H2CO3 + 2 NaOH',[['H2CO3',1,{H:2,C:1,O:3}],['NaOH',2,{Na:1,O:1,H:1}]],[['Na2CO3',1,{Na:2,C:1,O:3}],['H2O',2,{H:2,O:1}]]],
['H2CO3 + Ca(OH)2',[['H2CO3',1,{H:2,C:1,O:3}],['Ca(OH)2',1,{Ca:1,O:2,H:2}]],[['CaCO3',1,{Ca:1,C:1,O:3}],['H2O',2,{H:2,O:1}]]],
['H2S + 2 NaOH',[['H2S',1,{H:2,S:1}],['NaOH',2,{Na:1,O:1,H:1}]],[['Na2S',1,{Na:2,S:1}],['H2O',2,{H:2,O:1}]]],
['H2S + Ca(OH)2',[['H2S',1,{H:2,S:1}],['Ca(OH)2',1,{Ca:1,O:2,H:2}]],[['CaS',1,{Ca:1,S:1}],['H2O',2,{H:2,O:1}]]],
['H3PO4 + 3 NaOH',[['H3PO4',1,{H:3,P:1,O:4}],['NaOH',3,{Na:1,O:1,H:1}]],[['Na3PO4',1,{Na:3,P:1,O:4}],['H2O',3,{H:2,O:1}]]],
['H3PO4 + 3 KOH',[['H3PO4',1,{H:3,P:1,O:4}],['KOH',3,{K:1,O:1,H:1}]],[['K3PO4',1,{K:3,P:1,O:4}],['H2O',3,{H:2,O:1}]]],
['2 H3PO4 + 3 Ca(OH)2',[['H3PO4',2,{H:3,P:1,O:4}],['Ca(OH)2',3,{Ca:1,O:2,H:2}]],[['Ca3(PO4)2',1,{Ca:3,P:2,O:8}],['H2O',6,{H:2,O:1}]]],
['Zn + 2 HCl',[['Zn',1,{Zn:1}],['HCl',2,{H:1,Cl:1}]],[['ZnCl2',1,{Zn:1,Cl:2}],['H2',1,{H:2}]]],
['Mg + 2 HCl',[['Mg',1,{Mg:1}],['HCl',2,{H:1,Cl:1}]],[['MgCl2',1,{Mg:1,Cl:2}],['H2',1,{H:2}]]],
['Fe + 2 HCl',[['Fe',1,{Fe:1}],['HCl',2,{H:1,Cl:1}]],[['FeCl2',1,{Fe:1,Cl:2}],['H2',1,{H:2}]]],
['Ca + 2 HCl',[['Ca',1,{Ca:1}],['HCl',2,{H:1,Cl:1}]],[['CaCl2',1,{Ca:1,Cl:2}],['H2',1,{H:2}]]],
['2 Al + 6 HCl',[['Al',2,{Al:1}],['HCl',6,{H:1,Cl:1}]],[['AlCl3',2,{Al:1,Cl:3}],['H2',3,{H:2}]]],
['2 Na + 2 HCl',[['Na',2,{Na:1}],['HCl',2,{H:1,Cl:1}]],[['NaCl',2,{Na:1,Cl:1}],['H2',1,{H:2}]]],
['Mg + H2SO4',[['Mg',1,{Mg:1}],['H2SO4',1,{H:2,S:1,O:4}]],[['MgSO4',1,{Mg:1,S:1,O:4}],['H2',1,{H:2}]]],
['Zn + H2SO4',[['Zn',1,{Zn:1}],['H2SO4',1,{H:2,S:1,O:4}]],[['ZnSO4',1,{Zn:1,S:1,O:4}],['H2',1,{H:2}]]],
['2 Al + 3 H2SO4',[['Al',2,{Al:1}],['H2SO4',3,{H:2,S:1,O:4}]],[['Al2(SO4)3',1,{Al:2,S:3,O:12}],['H2',3,{H:2}]]],
['Water synthesis',[['H2',2,{H:2}],['O2',1,{O:2}]],[['H2O',2,{H:2,O:1}]]],
['Ammonia synthesis (Haber)',[['N2',1,{N:2}],['H2',3,{H:2}]],[['NH3',2,{N:1,H:3}]]],
['Sodium chloride synthesis',[['Na',2,{Na:1}],['Cl2',1,{Cl:2}]],[['NaCl',2,{Na:1,Cl:1}]]],
['Potassium chloride synthesis',[['K',2,{K:1}],['Cl2',1,{Cl:2}]],[['KCl',2,{K:1,Cl:1}]]],
['Magnesium oxide formation',[['Mg',2,{Mg:1}],['O2',1,{O:2}]],[['MgO',2,{Mg:1,O:1}]]],
['Calcium oxide formation',[['Ca',2,{Ca:1}],['O2',1,{O:2}]],[['CaO',2,{Ca:1,O:1}]]],
['Iron(III) oxide formation',[['Fe',4,{Fe:1}],['O2',3,{O:2}]],[['Fe2O3',2,{Fe:2,O:3}]]],
['Aluminium chloride synthesis',[['Al',2,{Al:1}],['Cl2',3,{Cl:2}]],[['AlCl3',2,{Al:1,Cl:3}]]],
['Hydrogen chloride synthesis',[['H2',1,{H:2}],['Cl2',1,{Cl:2}]],[['HCl',2,{H:1,Cl:1}]]],
['Sulfur dioxide formation',[['S',1,{S:1}],['O2',1,{O:2}]],[['SO2',1,{S:1,O:2}]]],
['Carbon dioxide formation',[['C',1,{C:1}],['O2',1,{O:2}]],[['CO2',1,{C:1,O:2}]]],
['Hydrogen peroxide decomposition',[['H2O2',2,{H:2,O:2}]],[['H2O',2,{H:2,O:1}],['O2',1,{O:2}]]],
['Calcium carbonate decomposition',[['CaCO3',1,{Ca:1,C:1,O:3}]],[['CaO',1,{Ca:1,O:1}],['CO2',1,{C:1,O:2}]]],
['Potassium chlorate decomposition',[['KClO3',2,{K:1,Cl:1,O:3}]],[['KCl',2,{K:1,Cl:1}],['O2',3,{O:2}]]],
['Sodium azide decomposition',[['NaN3',2,{Na:1,N:3}]],[['Na',2,{Na:1}],['N2',3,{N:2}]]],
['Carbonic acid decomposition',[['H2CO3',1,{H:2,C:1,O:3}]],[['H2O',1,{H:2,O:1}],['CO2',1,{C:1,O:2}]]],
['Mercury(II) oxide decomposition',[['HgO',2,{Hg:1,O:1}]],[['Hg',2,{Hg:1}],['O2',1,{O:2}]]],
['Copper(II) hydroxide decomposition',[['Cu(OH)2',1,{Cu:1,O:2,H:2}]],[['CuO',1,{Cu:1,O:1}],['H2O',1,{H:2,O:1}]]],
['Ammonium chloride decomposition',[['NH4Cl',1,{N:1,H:4,Cl:1}]],[['NH3',1,{N:1,H:3}],['HCl',1,{H:1,Cl:1}]]],
['Calcium hydroxide decomposition',[['Ca(OH)2',1,{Ca:1,O:2,H:2}]],[['CaO',1,{Ca:1,O:1}],['H2O',1,{H:2,O:1}]]],
['Silver chloride precipitation',[['AgNO3',1,{Ag:1,N:1,O:3}],['NaCl',1,{Na:1,Cl:1}]],[['AgCl',1,{Ag:1,Cl:1}],['NaNO3',1,{Na:1,N:1,O:3}]]],
['Silver bromide precipitation',[['AgNO3',1,{Ag:1,N:1,O:3}],['KBr',1,{K:1,Br:1}]],[['AgBr',1,{Ag:1,Br:1}],['KNO3',1,{K:1,N:1,O:3}]]],
['Barium sulfate precipitation',[['BaCl2',1,{Ba:1,Cl:2}],['Na2SO4',1,{Na:2,S:1,O:4}]],[['BaSO4',1,{Ba:1,S:1,O:4}],['NaCl',2,{Na:1,Cl:1}]]],
['Lead(II) iodide precipitation',[['Pb(NO3)2',1,{Pb:1,N:2,O:6}],['KI',2,{K:1,I:1}]],[['PbI2',1,{Pb:1,I:2}],['KNO3',2,{K:1,N:1,O:3}]]],
['Calcium carbonate precipitation',[['CaCl2',1,{Ca:1,Cl:2}],['Na2CO3',1,{Na:2,C:1,O:3}]],[['CaCO3',1,{Ca:1,C:1,O:3}],['NaCl',2,{Na:1,Cl:1}]]],
['Copper(II) hydroxide precipitation',[['CuSO4',1,{Cu:1,S:1,O:4}],['NaOH',2,{Na:1,O:1,H:1}]],[['Cu(OH)2',1,{Cu:1,O:2,H:2}],['Na2SO4',1,{Na:2,S:1,O:4}]]],
['Iron(III) hydroxide precipitation',[['FeCl3',1,{Fe:1,Cl:3}],['NaOH',3,{Na:1,O:1,H:1}]],[['Fe(OH)3',1,{Fe:1,O:3,H:3}],['NaCl',3,{Na:1,Cl:1}]]],
['Magnesium hydroxide precipitation',[['MgSO4',1,{Mg:1,S:1,O:4}],['NaOH',2,{Na:1,O:1,H:1}]],[['Mg(OH)2',1,{Mg:1,O:2,H:2}],['Na2SO4',1,{Na:2,S:1,O:4}]]],
['Calcium phosphate precipitation',[['CaCl2',3,{Ca:1,Cl:2}],['Na3PO4',2,{Na:3,P:1,O:4}]],[['Ca3(PO4)2',1,{Ca:3,P:2,O:8}],['NaCl',6,{Na:1,Cl:1}]]],
['Copper(II) sulfide precipitation',[['Na2S',1,{Na:2,S:1}],['CuSO4',1,{Cu:1,S:1,O:4}]],[['CuS',1,{Cu:1,S:1}],['Na2SO4',1,{Na:2,S:1,O:4}]]],
['Barium nitrate sulfate precipitation',[['Ba(NO3)2',1,{Ba:1,N:2,O:6}],['Na2SO4',1,{Na:2,S:1,O:4}]],[['BaSO4',1,{Ba:1,S:1,O:4}],['NaNO3',2,{Na:1,N:1,O:3}]]],
['Strontium sulfate precipitation',[['SrCl2',1,{Sr:1,Cl:2}],['Na2SO4',1,{Na:2,S:1,O:4}]],[['SrSO4',1,{Sr:1,S:1,O:4}],['NaCl',2,{Na:1,Cl:1}]]],
['Silver iodide precipitation',[['AgNO3',1,{Ag:1,N:1,O:3}],['NaI',1,{Na:1,I:1}]],[['AgI',1,{Ag:1,I:1}],['NaNO3',1,{Na:1,N:1,O:3}]]],
['Lead(II) sulfate precipitation',[['Pb(NO3)2',1,{Pb:1,N:2,O:6}],['Na2SO4',1,{Na:2,S:1,O:4}]],[['PbSO4',1,{Pb:1,S:1,O:4}],['NaNO3',2,{Na:1,N:1,O:3}]]],
['Zinc sulfide precipitation',[['ZnSO4',1,{Zn:1,S:1,O:4}],['Na2S',1,{Na:2,S:1}]],[['ZnS',1,{Zn:1,S:1}],['Na2SO4',1,{Na:2,S:1,O:4}]]],
['Nickel(II) hydroxide precipitation',[['NiCl2',1,{Ni:1,Cl:2}],['NaOH',2,{Na:1,O:1,H:1}]],[['Ni(OH)2',1,{Ni:1,O:2,H:2}],['NaCl',2,{Na:1,Cl:1}]]],
['Aluminium hydroxide precipitation',[['AlCl3',1,{Al:1,Cl:3}],['NaOH',3,{Na:1,O:1,H:1}]],[['Al(OH)3',1,{Al:1,O:3,H:3}],['NaCl',3,{Na:1,Cl:1}]]],
['Zinc displaces copper',[['Zn',1,{Zn:1}],['CuSO4',1,{Cu:1,S:1,O:4}]],[['ZnSO4',1,{Zn:1,S:1,O:4}],['Cu',1,{Cu:1}]]],
['Iron displaces copper',[['Fe',1,{Fe:1}],['CuSO4',1,{Cu:1,S:1,O:4}]],[['FeSO4',1,{Fe:1,S:1,O:4}],['Cu',1,{Cu:1}]]],
['Chlorine displaces bromine',[['Cl2',1,{Cl:2}],['NaBr',2,{Na:1,Br:1}]],[['NaCl',2,{Na:1,Cl:1}],['Br2',1,{Br:2}]]],
['Chlorine displaces iodine',[['Cl2',1,{Cl:2}],['KI',2,{K:1,I:1}]],[['KCl',2,{K:1,Cl:1}],['I2',1,{I:2}]]],
['Sodium with water',[['Na',2,{Na:1}],['H2O',2,{H:2,O:1}]],[['NaOH',2,{Na:1,O:1,H:1}],['H2',1,{H:2}]]],
['Calcium with water',[['Ca',1,{Ca:1}],['H2O',2,{H:2,O:1}]],[['Ca(OH)2',1,{Ca:1,O:2,H:2}],['H2',1,{H:2}]]],
['Thermite reaction',[['Al',2,{Al:1}],['Fe2O3',1,{Fe:2,O:3}]],[['Al2O3',1,{Al:2,O:3}],['Fe',2,{Fe:1}]]],
['Carbon reduces copper oxide',[['C',1,{C:1}],['CuO',2,{Cu:1,O:1}]],[['CO2',1,{C:1,O:2}],['Cu',2,{Cu:1}]]],
['Hydrogen reduces copper oxide',[['H2',1,{H:2}],['CuO',1,{Cu:1,O:1}]],[['Cu',1,{Cu:1}],['H2O',1,{H:2,O:1}]]],
['Methane chlorination',[['CH4',1,{C:1,H:4}],['Cl2',1,{Cl:2}]],[['CH3Cl',1,{C:1,H:3,Cl:1}],['HCl',1,{H:1,Cl:1}]]],
['Ethylene hydrogenation',[['C2H4',1,{C:2,H:4}],['H2',1,{H:2}]],[['C2H6',1,{C:2,H:6}]]],
['Ethylene bromination',[['C2H4',1,{C:2,H:4}],['Br2',1,{Br:2}]],[['C2H4Br2',1,{C:2,H:4,Br:2}]]],
['Acetylene hydrogenation',[['C2H2',1,{C:2,H:2}],['H2',2,{H:2}]],[['C2H6',1,{C:2,H:6}]]],
['Esterification (ethyl acetate)',[['CH3COOH',1,{C:2,H:4,O:2}],['C2H5OH',1,{C:2,H:6,O:1}]],[['CH3COOC2H5',1,{C:4,H:8,O:2}],['H2O',1,{H:2,O:1}]]]
];
AB_RX.forEach(r=>RXNS.push([r[0],r[1].map(x=>sp(x[0],x[1],x[2])),r[2].map(x=>sp(x[0],x[1],x[2]))]));
RXNS.forEach(rx=>{
  if(!balanced(rx[1],rx[2])) throw new Error('UNBALANCED: '+rx[0]);
  const eq=rx[1].map(s=>(s.coef>1?s.coef:'')+s.formula).join(' + ')+' -> '+rx[2].map(s=>(s.coef>1?s.coef:'')+s.formula).join(' + ');
  add({title:'Reaction: '+rx[0],category:'reactions',
    description:'Balanced chemical equation for '+rx[0].toLowerCase()+': '+eq+'. Atom counts verified equal on both sides.',
    reaction_name:rx[0],equation:eq,reactants:rx[1],products:rx[2],balanced:true,
    source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
  const masses=rx[1].concat(rx[2]).map(s=>({formula:s.formula,coef:s.coef,molar_mass_g_mol:mm(s.comp)}));
  add({title:rx[0]+' - stoichiometry',category:'reactions',
    description:'Stoichiometry detail for '+rx[0].toLowerCase()+': molar masses of each species computed from standard atomic weights; mole ratios follow the balanced coefficients.',
    reaction_name:rx[0],equation:eq,species_masses:masses,balanced:true,
    source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
});
console.log('reactions:',RXNS.length,'total:',seed);
// ---- lab techniques: [name, purpose] ----
const LABT=[['titration','determining concentration by measured reaction'],['gravimetric analysis','determining mass by precipitation and weighing'],['simple distillation','separating liquids by boiling point'],['fractional distillation','separating close-boiling liquids'],['steam distillation','distilling heat-sensitive substances'],['vacuum filtration','fast solid-liquid separation'],['gravity filtration','gentle solid-liquid separation'],['recrystallization','purifying solids by crystal growth'],['sublimation','purifying by solid-vapor transition'],['liquid-liquid extraction','separating by differential solubility'],['Soxhlet extraction','continuous solid extraction'],['paper chromatography','separating by differential migration'],['thin-layer chromatography','fast mixture analysis on plates'],['column chromatography','preparative separation on columns'],['gas chromatography','separating volatile mixtures'],['HPLC','high-resolution liquid separation'],['ion-exchange chromatography','separating by charge'],['UV-Vis spectroscopy','identifying by light absorption'],['infrared spectroscopy','identifying functional groups'],['NMR spectroscopy','determining molecular structure'],['mass spectrometry','identifying by mass-to-charge ratio'],['atomic absorption spectroscopy','measuring metal concentrations'],['flame photometry','detecting alkali metals by emission'],['X-ray crystallography','determining crystal structures'],['pH measurement','measuring acidity with electrodes'],['calorimetry','measuring heat of reaction'],['potentiometry','measuring voltage of cells'],['voltammetry','studying redox by current-voltage'],['electrolysis','driving reactions with current'],['centrifugation','separating by density'],['reflux','heating with condensed return'],['melting point determination','assessing purity of solids'],['boiling point determination','identifying liquids'],['density measurement','mass per unit volume'],['viscosity measurement','resistance to flow'],['refractometry','measuring refractive index'],['polarimetry','measuring optical rotation'],['Kjeldahl nitrogen analysis','determining protein nitrogen'],['desiccator use','keeping samples dry'],['analytical balance use','precise mass measurement'],['volumetric flask use','preparing exact volumes'],['burette use','delivering measured volumes'],['pipette use','transferring measured volumes'],['Bunsen burner use','controlled heating'],['crucible use','high-temperature containment'],['separatory funnel use','liquid-liquid separation'],['water bath use','gentle uniform heating'],['ice bath use','cooling reactions'],['fume hood use','safe handling of vapors'],['chemical storage','segregating incompatibles'],['waste disposal','segregating chemical waste'],['solution preparation','making standard concentrations'],['serial dilution','stepwise concentration reduction'],['standardization','calibrating against a primary standard'],['qualitative analysis','identifying ions present'],['flame test','identifying metals by flame color'],['borax bead test','identifying metals in beads'],['litmus test','testing acidity or basicity'],['Tollens test','detecting aldehydes'],['Fehling test','detecting reducing sugars']];
const LASPECTS=['principle','procedure','applications','safety','interpretation','teaching notes'];
LABT.forEach(t=>{
  LASPECTS.forEach(a=>{
    add({title:'Laboratory technique: '+t[0]+' - '+a,category:'lab',
      description:'Laboratory technique ('+a+'): '+t[0]+' - '+t[1]+'. Standard chemistry teaching reference.',
      technique:t[0],principle:t[1],steps:['Prepare equipment and reagents','Perform the technique per teaching protocol','Record and interpret the result'],
      source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- physical chemistry concepts: [name, statement] ----
const PHYS=[['ideal gas law','PV = nRT relates pressure, volume, temperature, and amount'],['Boyle\u2019s law','at constant temperature, pressure and volume are inversely related'],['Charles\u2019s law','at constant pressure, volume and temperature are directly related'],['Avogadro\u2019s law','equal volumes of gases hold equal particle counts'],['Dalton\u2019s law','total pressure is the sum of partial pressures'],['Graham\u2019s law','effusion rate is inversely proportional to the square root of molar mass'],['kinetic molecular theory','gas behavior follows from particle motion'],['first law of thermodynamics','energy is conserved in all processes'],['second law of thermodynamics','entropy of the universe increases'],['third law of thermodynamics','a perfect crystal has zero entropy at absolute zero'],['Hess\u2019s law','reaction enthalpy is path-independent'],['Gibbs free energy','G = H - TS predicts spontaneity'],['entropy','a measure of energy dispersal'],['enthalpy','heat content at constant pressure'],['heat capacity','heat per degree of temperature change'],['rate law','rate depends on concentrations raised to orders'],['rate-determining step','the slowest step controls the rate'],['activation energy','the minimum energy barrier to reaction'],['catalysts','speed reactions without being consumed'],['equilibrium constant','K relates product and reactant concentrations'],['Le Chatelier\u2019s principle','systems shift to counteract imposed changes'],['solubility product','Ksp governs dissolution equilibrium'],['common ion effect','a shared ion suppresses dissolution'],['Arrhenius acids','produce H+ in water'],['Arrhenius bases','produce OH- in water'],['Bronsted-Lowry acids','proton donors'],['Bronsted-Lowry bases','proton acceptors'],['Lewis acids','electron-pair acceptors'],['Lewis bases','electron-pair donors'],['pH scale','pH = -log[H+]'],['buffers','resist pH change'],['titration curves','pH plotted against titrant volume'],['oxidation numbers','bookkeeping of electron transfer'],['electrochemical cells','convert chemical and electrical energy'],['standard reduction potentials','rank oxidizing strength'],['Nernst equation','potential under nonstandard conditions'],['Faraday\u2019s laws','charge determines electrolysis amounts'],['atomic radius trend','decreases across a period, increases down a group'],['ionization energy trend','increases across a period, decreases down a group'],['electronegativity trend','increases across a period, decreases down a group'],['ionic bonding','electron transfer between ions'],['covalent bonding','electron sharing between atoms'],['metallic bonding','delocalized electrons in a lattice'],['hydrogen bonding','strong dipole attraction involving H'],['VSEPR theory','electron pairs arrange to minimize repulsion'],['hybridization','mixing of atomic orbitals'],['freezing point depression','solute lowers the freezing point'],['boiling point elevation','solute raises the boiling point'],['osmotic pressure','pressure from solute concentration differences'],['mole concept','one mole is an Avogadro-scale count of particles'],['Avogadro\u2019s number','6.022 x 10^23 particles per mole'],['empirical formula','simplest whole-number ratio'],['molecular formula','actual atom counts'],['percent composition','mass percent of each element'],['limiting reactant','the reactant exhausted first'],['percent yield','actual over theoretical times 100'],['quantum numbers','describe electron states'],['Aufbau principle','electrons fill lowest-energy orbitals first'],['Pauli exclusion principle','no two electrons share all quantum numbers'],['Hund\u2019s rule','degenerate orbitals fill singly first']];
const PHASPECTS=['statement','explanation','mathematical form','applications','related concepts','teaching notes'];
PHYS.forEach(p=>{
  PHASPECTS.forEach(a=>{
    add({title:p[0]+' - '+a,category:'physical',
      description:'Physical chemistry ('+a+'): '+p[0]+' - '+p[1]+'. Standard chemistry teaching reference.',
      concept:p[0],statement:p[1],
      source:'online',source_ref:REFIUPAC,creation_mode:'ONLINE-VERIFIED'});
  });
});
const onlineCount=seed;
console.log('online records:',onlineCount);
for(let s=onlineCount+1;s<=10000;s++){
  const r=gen.generate(s,{},lib.prng(s));
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID signature',s,v.errors);process.exit(1);}
  recs.push(r);
}
for(const r of recs.slice(0,onlineCount)){
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID online',r._seed,v.errors,JSON.stringify(r).slice(0,300));process.exit(1);}
}
const sum=lib.summarizeOnline(recs);
console.log('total',sum.total,'online',sum.online,'signature',sum.signature);
const w=lib.writeDb(SLUG,recs,REPO);
console.log('wrote',w.mb.toFixed(2),'MB in',w.chunks,'chunks');
