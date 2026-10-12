/* JAH Public Recipes Database generator — jahdb-public-recipes-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Generates COMPLETE original recipes (full ingredients + steps), clearly
   labeled src:"signature-generated-sample" — never presented as public-domain harvest. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-RCP-';
var GENRES=['mains','sides','soups','breads','desserts','breakfast'];

var DISHES={
 mains:[
  ['Harbor Fish Stew','Coastal',['2 lbs mixed firm white fish, cut in chunks','1 onion, diced','3 cloves garlic, minced','1 can (28 oz) crushed tomatoes','2 cups fish stock','1 teaspoon smoked paprika','olive oil, salt, pepper, parsley'],['Soften onion and garlic in olive oil 6 minutes.','Add paprika, tomatoes and stock; simmer 15 minutes.','Add fish; simmer 8 minutes until opaque.','Season, scatter parsley, serve with crusty bread.'],'35 min','15 min'],
  ['Ember-Roast Chicken','Farmhouse',['1 whole chicken (4 lbs)','2 tablespoons butter, softened','1 lemon, halved','4 sprigs thyme','1 head garlic, halved','salt and coarse pepper'],['Heat oven to 425\u00b0F.','Rub chicken with butter, salt and pepper; stuff with lemon, thyme, garlic.','Roast 1 hour 15 minutes until juices run clear.','Rest 15 minutes before carving.'],'15 min','1 hr 15 min'],
  ['Golden Lentil Curry','Indian-inspired',['2 cups red lentils, rinsed','1 onion, chopped','2 tablespoons curry powder','1 can coconut milk','3 cups vegetable broth','2 cups spinach'],['Sizzle onion 5 minutes; stir in curry powder 1 minute.','Add lentils, broth, coconut milk; simmer 20 minutes.','Fold in spinach until wilted; salt to taste.'],'10 min','25 min']
 ],
 sides:[
  ['Honey-Glazed Roots','Garden',['2 lbs mixed carrots and parsnips','3 tablespoons honey','2 tablespoons olive oil','1 teaspoon thyme leaves','salt and pepper'],['Heat oven to 400\u00b0F.','Toss roots with oil, honey, thyme, salt.','Roast 30 minutes, turning once, until caramelized.'],'10 min','30 min'],
  ['Herbed Rice Pilaf','Pantry',['1.5 cups long-grain rice','3 cups chicken broth','1 onion, finely diced','2 tablespoons butter','parsley and dill, chopped'],['Saut\u00e9 onion in butter 4 minutes.','Add rice; toast 2 minutes.','Add broth; cover and simmer 18 minutes.','Fluff with herbs.'],'8 min','20 min']
 ],
 soups:[
  ['Orchard Apple Soup','Orchard',['4 tart apples, chopped','1 onion, diced','3 cups vegetable stock','1 cup cream','1 teaspoon curry powder','butter, salt'],['Soften onion in butter 5 minutes.','Add apples, curry powder, stock; simmer 20 minutes.','Blend smooth; stir in cream.','Serve warm with a swirl of cream.'],'10 min','25 min'],
  ['Midnight Barley Broth','Hearth',['1 cup pearl barley','2 carrots, diced','2 celery stalks, diced','1 leek, sliced','6 cups beef or vegetable broth','bay leaf, thyme'],['Simmer everything 45 minutes until barley is tender.','Remove bay leaf; season boldly.','Serve steaming with dark bread.'],'15 min','45 min']
 ],
 breads:[
  ['Overnight Farm Loaf','Bakery',['4 cups bread flour','2 teaspoons salt','1 teaspoon instant yeast','2 cups cool water'],['Mix to a shaggy dough; rest 12 hours covered.','Shape into a round; proof 1 hour.','Bake at 450\u00b0F in a covered pot 30 minutes, uncovered 15.','Cool fully before slicing.'],'20 min + overnight','45 min'],
  ['Buttermilk Skillet Cornbread','Southern',['1.5 cups cornmeal','0.5 cup flour','1 cup buttermilk','2 eggs','0.25 cup melted butter','2 tablespoons sugar','1 tablespoon baking powder'],['Heat oven to 425\u00b0F with skillet inside.','Whisk dry and wet separately; combine briefly.','Pour into hot skillet; bake 20 minutes.'],'10 min','20 min']
 ],
 desserts:[
  ['Dark Orchard Cake','Orchard',['3 apples, thinly sliced','2 cups flour','1 cup sugar','0.5 cup butter','2 eggs','1 teaspoon cinnamon','0.5 cup walnuts'],['Heat oven to 350\u00b0F; butter a 9-inch pan.','Cream butter and sugar; beat in eggs.','Fold in flour, cinnamon, walnuts; spread in pan.','Fan apple slices on top; bake 45 minutes.'],'20 min','45 min'],
  ['Honey Custard Cups','Dairy',['2 cups milk','4 eggs','0.5 cup honey','1 teaspoon vanilla','nutmeg'],['Heat oven to 325\u00b0F.','Warm milk with honey; whisk into beaten eggs with vanilla.','Pour into cups; bake in a water bath 40 minutes.','Chill; dust with nutmeg.'],'15 min','40 min']
 ],
 breakfast:[
  ['Skillet Morning Hash','Farmhouse',['3 potatoes, diced','1 bell pepper, diced','1 onion, diced','4 eggs','smoked paprika, salt, oil'],['Crisp potatoes in oil 12 minutes.','Add pepper and onion; cook 8 minutes more.','Make wells; crack in eggs; cover 4 minutes.'],'10 min','25 min'],
  ['Oat & Orchard Porridge','Orchard',['1 cup rolled oats','2.5 cups milk','1 apple, grated','2 tablespoons honey','cinnamon, walnuts'],['Simmer oats and milk 8 minutes, stirring.','Stir in apple, honey, cinnamon.','Top with walnuts; serve hot.'],'5 min','10 min']
 ]
};
function normGenre(g){return GENRES.indexOf(g)>=0?g:'';}
function buildRecipe(s,genre,topic){
  var g=genre||pick(s,GENRES);
  var d=pick(s,DISHES[g]);
  var title=topic?('Recipe: '+topic+' (in the spirit of '+d[0]+')'):d[0];
  var servings=ri(s,2,8);
  var ings=d[2].slice(), steps=d[3].slice();
  return {title:title,genre:g,cuisine:d[1],course:g,servings:servings,prep:d[4],cook:d[5],
    desc:title+' \u2014 '+d[1]+' '+g+' for '+servings+'. Full recipe: '+ings.length+' ingredients, '+steps.length+' steps, every quantity and instruction included.',
    ings:ings,steps:steps};
}
function demoProgram(rid,title,ings,steps,servings){
  var j=function(x){return JSON.stringify(x);};
  return '/* JAH recipe demo program \u2014 jahdb-demo-1.0\n'+
   ' * Database: public-recipes \u00b7 Record: '+rid+' \u00b7 '+title+'\n'+
   ' * Interactive cooking guide + serving scaler.\n'+
   ' * RUN ON PC: save as demo.js, then run:  node demo.js\n'+
   ' * RUN IN BROWSER: press F12, paste into the console, press Enter. */\n'+
   '(function(){var R={title:'+j(title)+',servings:'+servings+',ingredients:'+j(ings)+',steps:'+j(steps)+'};\n'+
   'function scale(to){var f=to/R.servings;console.log("Scaled to "+to+" servings:");R.ingredients.forEach(function(g){console.log("  [ ] "+g+"  (\u00d7"+f.toFixed(2)+")");});}\n'+
   'console.log("== "+R.title+" ==");\n'+
   'R.ingredients.forEach(function(g){console.log("  [ ] "+g);});\n'+
   'R.steps.forEach(function(st,i){console.log("  Step "+(i+1)+": "+st);});\n'+
   'console.log("Tip: call scale(N) to rescale the shopping list to N servings.");\n'+
   'this.scale=scale;})();';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120)||null;
  var genre=normGenre(opts.genre)||null;
  var s=rnd, b=buildRecipe(s,genre,topic);
  var id=PREFIX+String(seed).padStart(7,'0');
  return {
   id:id,title:b.title,description:b.desc,genre:b.genre,type:'public recipe',
   cuisine:b.cuisine,course:b.course,servings:b.servings,prep_time:b.prep,cook_time:b.cook,
   ingredients:b.ings,steps:b.steps,
   source_cookbook:'JAH Boundless Generator (original, 2026)',
   source_note:'Original Signature recipe created for this database; clearly labeled sample.',
   image:'',image_full:'',image_credit:'',
   demo:{engine:'jahdb-demo-1.0',kind:'cook-along',title:'Interactive cooking guide \u2014 '+b.title,language:'javascript',
     program:demoProgram(id,b.title,b.ings,b.steps,b.servings)},
   src:'signature-generated-sample',_seed:seed,topic:topic||undefined
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-RCP-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(!Array.isArray(r.ingredients)||r.ingredients.length<3)e.push('ingredients');
  if(!Array.isArray(r.steps)||r.steps.length<2)e.push('steps');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('jahdb-demo-1.0')<0)e.push('demo');
  if(r.src!=='signature-generated-sample')e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-recipes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-recipes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
