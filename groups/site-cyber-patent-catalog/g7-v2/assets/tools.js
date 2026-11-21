
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
var CPC = {"A01": "Agriculture & forestry", "A21": "Baking", "A22": "Butchery & meat", "A23": "Foods & foodstuffs", "A24": "Tobacco", "A41": "Clothing", "A42": "Headwear", "A43": "Footwear", "A44": "Jewellery & haberdashery", "A45": "Luggage & hand articles", "A46": "Brushware", "A47": "Furniture", "A61": "Medical & veterinary", "A62": "Life-saving & fire-fighting", "A63": "Sports & games", "B01": "Chemical processes", "B29": "Plastics", "B41": "Printing", "B60": "Vehicles", "C07": "Organic chemistry", "C08": "Polymers", "F16": "Machine elements", "G01": "Measuring & testing", "G02": "Optics", "G06": "Computing", "G06F21": "System security", "H01": "Electric devices", "H04": "Electric communication", "H04L9": "Cryptography", "H04L63": "Network security", "H04W12": "Wireless network security", "H04K": "Secret communication"};
var SECTIONS = {"A": "Human necessities", "B": "Performing operations; transporting", "C": "Chemistry; metallurgy", "D": "Textiles; paper", "E": "Fixed constructions", "F": "Mechanical engineering", "G": "Physics", "H": "Electricity"};
function cpcLookup(code){
  if(code==null) return {error:'Enter a class code, for example A44.'};
  var c=String(code).trim().toUpperCase();
  if(!c) return {error:'Enter a class code, for example A44.'};
  if(CPC[c]) return {code:c, name:CPC[c], section:SECTIONS[c[0]] || ''};
  if(SECTIONS[c]) return {code:c, name:'Section: '+SECTIONS[c], section:SECTIONS[c]};
  return {error:'Class '+c+' is not in the lookup table on this page.'};
}
function patentAge(year){
  var y=Number(year);
  if(!isFinite(y)||Math.floor(y)!==y) return {error:'Enter a whole year, for example 1990.'};
  if(y<1800||y>2026) return {error:'Enter a year between 1800 and 2026.'};
  return {year:y, age:2026-y};
}
var TITLES = ["Porphyric Insecticides", "Expression of HIV binding proteins.", "Lactam derivatives.", "NUCLEOTIDIC SEQUENCES OF cDNA DERIVED FROM THE HEPATITIS C GENOME, RECOMBINANT &hellip;", "METHOD FOR CONTROLLING PESTS IN CULTURES OF USEFUL TRANSGENIC PLANTS THROUGH &hellip;", "COMPOSITIONS PESTICIDES IN GEL", "TRANSDIFFERENTIATION OF PANCREATIC ACINAR CELLS", "ANTAGONISTS OF MUSCARINIC ACETILCOLINE RECEPTORS. PHARMACEUTICAL COMPOSITIONS", "COMPOSITIONS WITH HIGHER LEVELS OF PHYTOESTEROL OBTAINED FROM PLANTS WITH LOWER &hellip;", "USE OF THE HUMAN CORIONIC GONADOTROPHINE (GCH) ASSOCIATED WITH A CYCLODEXTRINE, &hellip;", "DETERGENTS THAT HAVE ACCEPTABLE COLOR", "DERIVATIVES OF ARIL SULFONAMIDE CONTAINING O-SULFATE AND O-PHOSPHATE, USEFUL AS &hellip;", "DERIVATIVES OF CARABXAMIDAS AZABICICLICAS ITS PREPARATION AND ITS APPLICATION &hellip;", "A PROCESS AND A SYSTEM FOR THE PREPARATION OF SULFENIL PERFLUORO RENT CHLORIDE.", "Concentrados herbicidas acuosos", "FORMULATIONS OF 3- (5-AMINO-2-METIL-4-OXO-4H-QUINAZOLIN-3-IL) -PIPERIDINA-2,6- &hellip;", "FINGOLIMOD STABLE SOLID DOSAGE FORMS", "FORMULATIONS / COMPOSITIONS THAT INCLUDE A BTK INHIBITOR", "PROCESS FOR THE SIMULTANEOUS PREPARATION OF SODIUM AND POTASSIUM ALCOXIDES", "SITE-SPECIFIC ANTIBODY-DRUG CONJUGATES WITH PEPTIDE-CONTAINING LINKERS", "OLIGONUCLEOTIDE CONJUGATES TARGETED TO THE TRANSFERRIN RECEPTOR", "PROCEDURE FOR OBTAINING GRAPE SUGAR FREE OF OTHER MINERAL OR ORGANIC SUBSTANCES &hellip;", "Verfahren zur prozesssteuerung", "TOTAL WORLD CLOCK"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var t=TITLES[Math.floor(r()*TITLES.length)];
  return 'Fun: the workshop once built a device from "'+t+'" — it worked perfectly, twice, and then asked for a patent of its own.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { cpcLookup: cpcLookup, patentAge: patentAge, makeFun: makeFun };
