(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['nutrients','foods','diets','safety','planning'];
var PREFIX='JAH-NUT-';
var NUTR=[['Vitamin A','fat-soluble vitamin','vision and immune function'],['Vitamin C','water-soluble vitamin','collagen synthesis and antioxidant defense'],['Vitamin D','fat-soluble vitamin','calcium absorption and bone health'],['Vitamin E','fat-soluble vitamin','antioxidant protection of membranes'],['Vitamin K','fat-soluble vitamin','blood clotting and bone proteins'],['Thiamin (B1)','B vitamin','energy metabolism'],['Riboflavin (B2)','B vitamin','energy metabolism'],['Niacin (B3)','B vitamin','energy metabolism and DNA repair'],['Vitamin B6','B vitamin','amino acid metabolism'],['Folate (B9)','B vitamin','DNA synthesis and cell division'],['Vitamin B12','B vitamin','nerve function and red blood cell formation'],['Calcium','major mineral','bones, teeth, and signaling'],['Iron','trace mineral','oxygen transport in blood'],['Magnesium','major mineral','enzyme reactions and muscle function'],['Potassium','major mineral','fluid balance and nerve signals'],['Zinc','trace mineral','immune function and wound healing'],['Protein','macronutrient','tissue building and repair'],['Fiber','carbohydrate','digestive health'],['Omega-3 fats','essential fat','heart and brain health'],['Water','essential nutrient','hydration and transport']];
var FOODS=[['oats','whole grain'],['brown rice','whole grain'],['lentils','legume'],['chickpeas','legume'],['almonds','nut'],['walnuts','nut'],['salmon','fish'],['chicken breast','poultry'],['eggs','protein food'],['Greek yogurt','dairy'],['broccoli','vegetable'],['spinach','vegetable'],['carrots','vegetable'],['sweet potato','vegetable'],['apple','fruit'],['banana','fruit'],['orange','fruit'],['blueberries','fruit'],['olive oil','fat'],['avocado','fruit']];
var DIETS=[['Mediterranean pattern','vegetables, fruits, whole grains, olive oil, fish'],['DASH pattern','fruits, vegetables, low-fat dairy, limited sodium'],['plant-based pattern','mostly plant foods with varied protein sources'],['balanced omnivore pattern','varied foods across all groups in moderation']];
var SAFETY=[['poultry safe temperature','cook all poultry to 165 F internal temperature'],['ground meat safe temperature','cook ground meats to 160 F'],['steak safe temperature','cook steaks and chops to 145 F with a 3-minute rest'],['leftovers','reheat leftovers to 165 F'],['hand washing','wash hands 20 seconds before handling food'],['cross-contamination','keep raw meats separate from ready-to-eat foods'],['refrigeration','refrigerate perishables within 2 hours'],['thermometer use','a food thermometer is the only reliable doneness check']];
var PLAN=[['MyPlate method','half the plate vegetables and fruits, with grains and protein'],['meal timing','regular meals support steady energy'],['portion awareness','compare servings with reference amounts'],['label reading','check serving size, then nutrients per serving'],['hydration planning','water as the default drink through the day']];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var rec={id:id,category:cat,source:'signature',source_ref:'JAH Signature Generator',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
  if(cat==='nutrients'){
    var n=pick(NUTR,rnd);
    rec.title='Nutrient study: '+n[0];
    rec.description='A teaching record for '+n[0]+' ('+n[1]+'): supports '+n[2]+'. Describes roles, food sources, and intake guidance in general educational terms without fabricated exact values.';
    rec.nutrient=n[0];rec.nutrient_class=n[1];rec.roles=[n[2]];
    rec.guidance='Follow established dietary reference intakes from public health authorities.';
  }else if(cat==='foods'){
    var f=pick(FOODS,rnd);
    rec.title='Food study: '+f[0];
    rec.description='A teaching record for '+f[0]+' ('+f[1]+'). Describes its food group, typical nutrient contributions, and preparation notes in general qualitative terms.';
    rec.food=f[0];rec.food_group=f[1];
    rec.nutrient_highlights=['contributes nutrients typical of its food group'];
    rec.preparation='Prepare with minimal added sodium, sugars, and saturated fat.';
  }else if(cat==='diets'){
    var d=pick(DIETS,rnd);
    rec.title='Dietary pattern: '+d[0];
    rec.description='A teaching record for the '+d[0]+': emphasizes '+d[1]+'. Describes principles and practical steps in general educational terms.';
    rec.pattern=d[0];rec.principles=[d[1]];
  }else if(cat==='safety'){
    var s=pick(SAFETY,rnd);
    rec.title='Food safety: '+s[0];
    rec.description='A teaching record: '+s[0]+' - '+s[1]+'. A core food-safety practice stated in plain terms.';
    rec.practice=s[0];rec.rule=s[1];
  }else{
    var p=pick(PLAN,rnd);
    rec.title='Meal planning: '+p[0];
    rec.description='A teaching record for '+p[0]+': '+p[1]+'. A practical planning method in general educational terms.';
    rec.method=p[0];rec.how=p[1];
  }
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-NUT-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.category==='nutrients'&&typeof r.nutrient!=='string')e.push('nutrient');
  if(r.category==='foods'&&typeof r.food!=='string')e.push('food');
  if(r.category==='diets'&&typeof r.pattern!=='string')e.push('pattern');
  if(r.category==='safety'&&(typeof r.practice!=='string'||typeof r.rule!=='string'))e.push('safety');
  if(r.category==='planning'&&typeof r.method!=='string')e.push('method');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-nutrition-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nutrition',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
