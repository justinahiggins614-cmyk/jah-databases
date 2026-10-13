(function(){'use strict';
/* JAH Public Secret Menus Database generator — jahdb-public-secret-menus-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SECM-';
var FIELDS=["burgers", "sandwiches", "drinks", "sides", "burritos", "mexican", "chicken", "bowls", "mexican-chinese"];
var TOPICS={
 "bowls":["Panera: Power Breakfast Bowl (secret)","Qdoba: Impossible everything"],
 "burgers":["McDonald's: Land, Sea & Air Burger","McDonald's: McGangBang","In-N-Out Burger: Animal Style Burger","In-N-Out Burger: Protein Style","In-N-Out Burger: 3x3 / 4x4","Burger King: Suicide Burger / Quad Stacker","Wendy's: Barnyard / Meat Cube","Five Guys: Patty Melt","Shake Shack: Peanut Butter & Bacon Burger","Carl's Jr.: The Turducken of burgers","In-N-Out: Flying Dutchman","Jollibee: Amazing Aloha Yumburger","Five Guys: The Presidential","White Castle: Surf and Turf Slider"],
 "burritos":["Chipotle: Quesarito","Chipotle: Burritodilla","Moe's: The Overachiever"],
 "chicken":["Popeyes: Cajun Turkey (holiday)","KFC: Double Down","Nando's: Extra Hot + Garlic"],
 "drinks":["McDonald's: Neapolitan Shake","In-N-Out Burger: Neapolitan Shake","Starbucks: Pink Drink","Starbucks: Butterbeer Latte","Starbucks: Cookies and Cream Frappuccino","Starbucks: Medicine Ball / Honey Citrus Mint Tea","Starbucks: Cotton Candy Frappuccino","Jamba Juice: White Gummi Bear","Jamba Juice: Red Gummi Bear","Jamba Juice: Sour Patch Kid","Taco Bell: Hulk / Green Hulk","Wendy's: Frosty Float","Sonic: Purple Sprite / Rainbow Slush","Dairy Queen: Brownie Batter Blizzard","Chick-fil-A: Frosted Lemonade / Frosted Coffee","Culver's: Concrete mixer with everything","In-N-Out: Root Beer Float","Dunkin': Cold Brew with Sweet Cold Foam, extra","Starbucks: Iced Matcha with Chai"],
 "hotdogs":["Shake Shack: Shack-cago Dog"],
 "mexican":["Taco Bell: Cheesarito","Taco Bell: Enchirito","Jack in the Box: Taco ultimate"],
 "mexican-chinese":["Panda Express: Orange Chicken Burrito"],
 "sandwiches":["McDonald's: Grilled Cheese","In-N-Out Burger: Grilled Cheese (Animal Style)","Chick-fil-A: Spicy Char","Chick-fil-A: Double Down style","Subway: Pizza Sub","Subway: The Feast","Arby's: Meat Mountain","Arby's: Roast Beef 'n Cheddar with curly fries inside","Whataburger: Honey BBQ Chicken Strip Sandwich","Bojangles: Cajun Filet Biscuit, extra"],
 "sides":["In-N-Out Burger: Animal Style Fries","Chipotle: Nachos","Zaxby's: Chicken Bacon Ranch Loaded Fries","Sonic: Frito Pie Chili Cheese Tots"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/"/g,"'");
  return "# Restaurant Lab — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — secret menu item study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A secret menu item study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'secret-menu-guide',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-secret-menus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-secret-menus',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
