(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['electronics','clothing','home','books','sports','toys'];
var PRANGE={electronics:[15,2500],clothing:[10,400],home:[12,1200],books:[5,80],sports:[15,900],toys:[6,150]};
var WORDS={
 electronics:['Wireless Headphones','Smart Speaker','4K Drone','LED Monitor','Mechanical Keyboard','Portable Charger','Bluetooth Earbuds','Action Camera'],
 clothing:['Cotton Hoodie','Denim Jacket','Running Shoes','Wool Sweater','Canvas Backpack','Linen Shirt','Trail Boots','Windbreaker'],
 home:['Ceramic Vase Set','Bamboo Cutting Board','LED Floor Lamp','Memory Foam Pillow','Cast Iron Skillet','Wool Area Rug','Espresso Maker','Air Purifier'],
 books:['Mystery Novel','Science Textbook','Cookbook Collection','History Atlas','Poetry Anthology','Travel Guide','Children\'s Picture Book','Biography'],
 sports:['Yoga Mat Pro','Aluminum Bat','Tennis Racket','Dumbbell Set','Camping Tent','Fishing Rod','Basketball','Resistance Bands'],
 toys:['Building Block Set','Remote Control Car','Plush Bear','Puzzle 1000pc','Doll House','Science Kit','Board Game','Train Set']};
var BRANDS=['NovaGear','BluePeak','CraftLine','SummitWorks','Harbor & Co','IronOak','LumenLab','PrimeField','AeroNest','StoneBridge','QuickStep','BrightHouse','TerraMade','Skyward','OldMill','FreshLane','CorePlus','WildPath','UrbanNest','TrueForm'];
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
  var brand=pick(BRANDS,rnd);
  var name=brand+' '+pick(WORDS[cat],rnd)+' '+ri(rnd,100,999);
  var pr=PRANGE[cat];
  var price=Math.round((pr[0]+rnd()*(pr[1]-pr[0]))*100)/100;
  var rating=Math.round((3+rnd()*2)*10)/10;
  var rc=ri(rnd,0,50000);
  var id='JAH-PROD-'+String(seed).padStart(6,'0');
  var desc=name+' by '+brand+'. '+cat+' — rated '+rating+'/5 across '+rc+' reviews.';
  return {id:id,product_id:id,name:name,title:name,description:desc.slice(0,600),
    category:cat,price:price,currency:'USD',rating:rating,review_count:rc,brand:brand};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(typeof r.id!=='string'||!/^JAH-PROD-\d{6}$/.test(r.id))e.push('id');
  if(r.product_id!==r.id)e.push('product_id');
  if(typeof r.name!=='string'||!r.name)e.push('name');
  if(r.title!==r.name)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.price!=='number'||r.price<=0)e.push('price');
  if(r.currency!=='USD')e.push('currency');
  if(typeof r.rating!=='number'||r.rating<1.0||r.rating>5.0)e.push('rating');
  if(typeof r.review_count!=='number'||r.review_count<0||r.review_count%1!==0)e.push('review_count');
  if(typeof r.brand!=='string'||!r.brand)e.push('brand');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-ecommerce-products-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ecommerce-products',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
