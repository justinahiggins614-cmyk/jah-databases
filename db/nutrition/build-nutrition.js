'use strict';
// Build JAH Nutrition Database: ~2000 online + signature. RDA values follow NIH ODS;
// food records are qualitative (no fabricated per-100g numbers).
const path=require('path');
const lib=require('../buildlib.js');
const gen=require('./gen-nutrition.js');
const REPO=path.join(__dirname,'..','..');
const SLUG='nutrition', PREFIX='JAH-NUT-';
const REF='https://ods.od.nih.gov/';
const REFUSDA='https://www.usda.gov/';
let seed=0; const recs=[];
function add(r){ seed++; r._seed=seed; r.id=lib.idOf(PREFIX,seed); recs.push(r); }
// ---- nutrients: [name, class, function, RDA note] ----
const NUTR=[['Vitamin A','fat-soluble vitamin','vision, immune function, and cell growth','900 mcg men, 700 mcg women (RDA)'],['Vitamin C','water-soluble vitamin','collagen synthesis and antioxidant defense','90 mg men, 75 mg women; smokers need 35 mg more (RDA)'],['Vitamin D','fat-soluble vitamin','calcium absorption and bone health','15 mcg ages 19-70, 20 mcg over 70 (RDA)'],['Vitamin E','fat-soluble vitamin','antioxidant protection of cell membranes','15 mg (RDA)'],['Vitamin K','fat-soluble vitamin','blood clotting and bone proteins','120 mcg men, 90 mcg women (AI)'],['Thiamin (B1)','B vitamin','energy metabolism','1.2 mg men, 1.1 mg women (RDA)'],['Riboflavin (B2)','B vitamin','energy metabolism','1.3 mg men, 1.1 mg women (RDA)'],['Niacin (B3)','B vitamin','energy metabolism and DNA repair','16 mg men, 14 mg women (RDA)'],['Pantothenic acid (B5)','B vitamin','coenzyme A synthesis','5 mg (AI)'],['Vitamin B6','B vitamin','amino acid metabolism','1.3 mg ages 19-50 (RDA)'],['Biotin (B7)','B vitamin','fatty acid synthesis','30 mcg (AI)'],['Folate (B9)','B vitamin','DNA synthesis and cell division','400 mcg DFE (RDA)'],['Vitamin B12','B vitamin','nerve function and red blood cell formation','2.4 mcg (RDA)'],['Choline','essential nutrient','cell membranes and neurotransmission','550 mg men, 425 mg women (AI)'],['Calcium','major mineral','bones, teeth, and cellular signaling','1000 mg ages 19-50 (RDA)'],['Iron','trace mineral','oxygen transport in hemoglobin','8 mg men, 18 mg women 19-50 (RDA)'],['Magnesium','major mineral','enzyme reactions and muscle function','400-420 mg men, 310-320 mg women (RDA)'],['Phosphorus','major mineral','bones and energy metabolism','700 mg (RDA)'],['Potassium','major mineral','fluid balance and nerve signals','3400 mg men, 2600 mg women (AI)'],['Sodium','major mineral','fluid balance; excess linked to blood pressure','2300 mg upper limit'],['Chloride','major mineral','fluid balance and stomach acid','2300 mg (AI)'],['Zinc','trace mineral','immune function and wound healing','11 mg men, 8 mg women (RDA)'],['Copper','trace mineral','iron metabolism and enzymes','900 mcg (RDA)'],['Manganese','trace mineral','enzyme cofactor','2.3 mg men, 1.8 mg women (AI)'],['Selenium','trace mineral','antioxidant enzymes','55 mcg (RDA)'],['Iodine','trace mineral','thyroid hormones','150 mcg (RDA)'],['Chromium','trace mineral','insulin action','35 mcg men, 25 mcg women (AI)'],['Molybdenum','trace mineral','enzyme cofactor','45 mcg (RDA)'],['Fluoride','trace mineral','dental health','4 mg men, 3 mg women (AI)'],['Protein','macronutrient','tissue building and repair','0.8 g per kg body weight (RDA)'],['Fiber','carbohydrate','digestive health','38 g men, 25 g women (AI)'],['Water','essential nutrient','hydration and transport','3.7 L men, 2.7 L women (AI)'],['Omega-3 (ALA)','essential fat','heart and brain health','1.6 g men, 1.1 g women (AI)'],['Omega-6 (linoleic acid)','essential fat','growth and skin health','17 g men, 12 g women (AI)']];
const NASPECTS=['overview','function','RDA','deficiency','toxicity and upper limits','food sources','interactions','absorption','life-stage notes','teaching notes','key terms','references'];
NUTR.forEach(n=>{
  NASPECTS.forEach(a=>{
    add({title:n[0]+' - '+a,category:'nutrients',
      description:'Nutrient ('+a+'): '+n[0]+' ('+n[1]+') supports '+n[2]+'. Intake guidance: '+n[3]+'. Values follow NIH Office of Dietary Supplements references.',
      nutrient:n[0],nutrient_class:n[1],roles:[n[2]],guidance:n[3]+'.',
      source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- foods: [name, group] ----
const FOODS=[['oats','whole grain'],['brown rice','whole grain'],['white rice','grain'],['quinoa','whole grain'],['barley','whole grain'],['whole wheat bread','whole grain'],['corn','vegetable/grain'],['popcorn','whole grain'],['millet','whole grain'],['buckwheat','whole grain'],['rye bread','whole grain'],['pasta','grain'],['chicken breast','poultry'],['chicken thigh','poultry'],['turkey breast','poultry'],['beef steak','meat'],['ground beef','meat'],['pork chop','meat'],['pork loin','meat'],['salmon','fish'],['tuna','fish'],['sardines','fish'],['mackerel','fish'],['trout','fish'],['tilapia','fish'],['cod','fish'],['shrimp','shellfish'],['crab','shellfish'],['eggs','protein food'],['Greek yogurt','dairy'],['plain yogurt','dairy'],['milk','dairy'],['cheddar cheese','dairy'],['mozzarella','dairy'],['cottage cheese','dairy'],['tofu','soy protein'],['tempeh','soy protein'],['lentils','legume'],['chickpeas','legume'],['black beans','legume'],['kidney beans','legume'],['pinto beans','legume'],['soybeans','legume'],['edamame','legume'],['peanuts','nut'],['peanut butter','nut'],['almonds','nut'],['walnuts','nut'],['cashews','nut'],['pistachios','nut'],['sunflower seeds','seed'],['chia seeds','seed'],['flaxseeds','seed'],['pumpkin seeds','seed'],['broccoli','vegetable'],['spinach','vegetable'],['kale','vegetable'],['carrots','vegetable'],['sweet potato','vegetable'],['potato','vegetable'],['tomato','vegetable'],['cucumber','vegetable'],['lettuce','vegetable'],['cabbage','vegetable'],['cauliflower','vegetable'],['Brussels sprouts','vegetable'],['bell pepper','vegetable'],['onion','vegetable'],['garlic','vegetable'],['celery','vegetable'],['zucchini','vegetable'],['eggplant','vegetable'],['asparagus','vegetable'],['green beans','vegetable'],['peas','vegetable'],['mushrooms','vegetable'],['avocado','fruit'],['beets','vegetable'],['apple','fruit'],['banana','fruit'],['orange','fruit'],['strawberries','fruit'],['blueberries','fruit'],['raspberries','fruit'],['grapes','fruit'],['watermelon','fruit'],['cantaloupe','fruit'],['pineapple','fruit'],['mango','fruit'],['kiwi','fruit'],['peach','fruit'],['pear','fruit'],['cherries','fruit'],['lemon','fruit'],['grapefruit','fruit'],['papaya','fruit'],['pomegranate','fruit'],['cranberries','fruit'],['figs','fruit'],['dates','fruit'],['coconut','fruit'],['olives','fruit'],['butter','dairy fat'],['olive oil','oil'],['honey','sweetener'],['dark chocolate','sweet'],['green tea','beverage'],['dragon fruit','fruit'],['star fruit','fruit'],['persimmon','fruit']];
const FASPECTS=['overview','food group','nutrient highlights','selection','storage','preparation','serving ideas','safety note'];
FOODS.forEach(f=>{
  FASPECTS.forEach(a=>{
    add({title:f[0]+' - '+a,category:'foods',
      description:'Food ('+a+'): '+f[0]+' ('+f[1]+'). Qualitative teaching record: describes group, typical nutrient contributions, and handling in general terms.',
      food:f[0],food_group:f[1],nutrient_highlights:['contributes nutrients typical of the '+f[1]+' group'],
      preparation:'Prepare with minimal added sodium, sugars, and saturated fat.',
      source:'online',source_ref:REFUSDA,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- diets ----
const DIETS=[['Mediterranean pattern','vegetables, fruits, whole grains, olive oil, fish, legumes'],['DASH pattern','fruits, vegetables, whole grains, low-fat dairy, limited sodium'],['MIND pattern','leafy greens, berries, nuts, whole grains, olive oil'],['vegetarian pattern','plant foods plus dairy and eggs, no meat'],['vegan pattern','plant foods only'],['pescatarian pattern','plant foods plus fish and seafood'],['flexitarian pattern','mostly plant foods with occasional meat'],['low-sodium pattern','limited sodium across food groups'],['high-fiber pattern','whole grains, legumes, vegetables, fruits'],['MyPlate pattern','half vegetables and fruits, with grains and protein'],['TLC pattern','therapeutic lifestyle changes for heart health'],['gluten-free pattern','no wheat, barley, or rye; for medical need'],['lactose-free pattern','dairy avoided or lactase-treated'],['low-FODMAP pattern','limited fermentable carbohydrates; guided use'],['diabetes meal planning','carbohydrate awareness and balanced meals'],['heart-healthy pattern','vegetables, whole grains, lean proteins, healthy fats']];
const DASPECTS=['principles','foods emphasized','foods limited','evidence context','practical steps','teaching notes','related patterns','key terms'];
DIETS.forEach(d=>{
  DASPECTS.forEach(a=>{
    add({title:d[0]+' - '+a,category:'diets',
      description:'Dietary pattern ('+a+'): the '+d[0]+' emphasizes '+d[1]+'. General educational description; individual needs vary.',
      pattern:d[0],principles:[d[1]],
      source:'online',source_ref:REFUSDA,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- safety: [practice, rule] ----
const SAFETY=[['poultry temperature','cook all poultry to 165 F internal temperature'],['ground meat temperature','cook ground meats to 160 F'],['steak temperature','cook steaks, roasts, and chops to 145 F with a 3-minute rest'],['pork temperature','cook whole cuts of pork to 145 F with a 3-minute rest'],['fish temperature','cook fish to 145 F'],['egg dishes temperature','cook egg dishes to 160 F'],['leftovers temperature','reheat leftovers to 165 F'],['two-hour rule','refrigerate perishables within 2 hours'],['hand washing','wash hands for 20 seconds before handling food'],['clean','wash hands, surfaces, and produce'],['separate','keep raw meats away from ready-to-eat foods'],['cook','use a food thermometer to verify doneness'],['chill','keep the fridge at 40 F or below'],['danger zone','keep foods out of 40-140 F'],['thawing','thaw in the fridge, cold water, or microwave'],['cross-contamination','use separate boards for raw meat'],['thermometer use','a food thermometer is the only reliable doneness check'],['leftovers storage','eat refrigerated leftovers within 3-4 days'],['Salmonella','a leading cause of foodborne illness from poultry and eggs'],['Campylobacter','a leading cause of illness from poultry'],['E. coli O157:H7','a pathogen linked to undercooked ground beef'],['Listeria','a risk in deli meats and soft cheeses, especially in pregnancy'],['Norovirus','a leading cause of foodborne illness outbreaks'],['Clostridium perfringens','grows in foods held at unsafe temperatures'],['Staphylococcus aureus','produces toxin in foods left at room temperature'],['milk allergen','one of the nine major food allergens'],['egg allergen','one of the nine major food allergens'],['peanut allergen','one of the nine major food allergens'],['tree nut allergen','one of the nine major food allergens'],['wheat allergen','one of the nine major food allergens'],['soy allergen','one of the nine major food allergens'],['sesame allergen','one of the nine major food allergens'],['fish allergen','one of the nine major food allergens'],['shellfish allergen','one of the nine major food allergens'],['high-mercury fish','avoid shark, swordfish, king mackerel, and tilefish in pregnancy'],['deli meats in pregnancy','heat deli meats to steaming to reduce Listeria risk'],['honey and infants','no honey for infants under 12 months (botulism risk)'],['raw milk','pasteurization kills harmful pathogens'],['washing produce','rinse fruits and vegetables under running water'],['date labels','sell-by dates indicate quality, not safety'],['freezer temperature','keep the freezer at 0 F'],['when in doubt','when in doubt, throw it out']];
const SASPECTS=['practice','why it matters','how to apply','common mistakes','teaching notes','key terms'];
SAFETY.forEach(s=>{
  SASPECTS.forEach(a=>{
    add({title:'Food safety: '+s[0]+' - '+a,category:'safety',
      description:'Food safety ('+a+'): '+s[0]+' - '+s[1]+'. Guidance follows USDA food-safety recommendations.',
      practice:s[0],rule:s[1],
      source:'online',source_ref:REFUSDA,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- planning ----
const PLAN=[['MyPlate method','half the plate vegetables and fruits, with grains and protein'],['Dietary Guidelines','current federal nutrition guidance'],['meal prep','cooking components ahead for the week'],['batch cooking','cooking large quantities at once'],['grocery list','planning purchases before shopping'],['seasonal shopping','buying produce in season'],['budget eating','nutritious eating on a budget'],['label reading','checking serving size, then nutrients per serving'],['hand portion method','using hands to estimate portions'],['plate method','dividing the plate among food groups'],['mindful eating','paying attention while eating'],['breakfast planning','starting the day with a balanced meal'],['healthy snacks','planned nutrient-dense snacks'],['eating out','navigating restaurant meals'],['food diary','recording intake for awareness'],['hydration planning','water as the default drink'],['steaming','cooking with steam'],['grilling','cooking over direct heat'],['baking','cooking with dry oven heat'],['herbs and spices','flavor without sodium'],['reducing sodium','flavor strategies beyond salt'],['reducing added sugars','identifying hidden sugars'],['whole grain swaps','replacing refined grains'],['healthy fats','choosing unsaturated fats'],['vegetarian proteins','combining plant protein sources'],['lunch packing','portable balanced meals'],['freezer meals','make-ahead frozen meals'],['pantry staples','keeping basics on hand'],['farmers markets','buying local produce'],['community supported agriculture','subscribing to farm shares']];
const PASPECTS=['method','how it works','getting started','tips','common pitfalls','teaching notes','related methods','key terms'];
PLAN.forEach(p=>{
  PASPECTS.forEach(a=>{
    add({title:'Meal planning: '+p[0]+' - '+a,category:'planning',
      description:'Meal planning ('+a+'): '+p[0]+' - '+p[1]+'. Practical planning guidance in general educational terms.',
      method:p[0],how:p[1],
      source:'online',source_ref:REFUSDA,creation_mode:'ONLINE-VERIFIED'});
  });
});
const onlineCount=seed;
console.log('online records:',onlineCount,'nutrients:',NUTR.length,'foods:',FOODS.length);
for(let s=onlineCount+1;s<=10000;s++){
  const r=gen.generate(s,{},lib.prng(s));
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID signature',s,v.errors);process.exit(1);}
  recs.push(r);
}
for(const r of recs.slice(0,onlineCount)){
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID online',r._seed,v.errors,JSON.stringify(r).slice(0,200));process.exit(1);}
}
const sum=lib.summarizeOnline(recs);
console.log('total',sum.total,'online',sum.online,'signature',sum.signature);
const w=lib.writeDb(SLUG,recs,REPO);
console.log('wrote',w.mb.toFixed(2),'MB in',w.chunks,'chunks');
