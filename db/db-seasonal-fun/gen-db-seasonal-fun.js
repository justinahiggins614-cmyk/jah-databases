(function(){'use strict';
/* The The Seasonal Fun Database generator — jahdb-db-seasonal-fun-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-SEASONAL-FUN-PUB-";
var GENVER="jahdb-db-seasonal-fun-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "First Signs of Spring Walk",
  "Spring Cleaning Party",
  "Plant Something Day",
  "The First Picnic",
  "Rainy Spring Reading",
  "Summer Swim Kickoff",
  "The Longest Day Plan",
  "Berry Picking Morning",
  "Autumn Leaf Walk",
  "The First Fire Night",
  "Apple Everything Weekend",
  "Winter Cozy Nest Day"
 ],
 "Compounded": [
  "Spring Garden Launch",
  "The Spring Festival Circuit",
  "Summer Water Tour",
  "The Harvest Preserve",
  "Autumn Hiking Series",
  "The Halloween Build-Up",
  "Winter Lights Tour",
  "The Cozy Cooking Season",
  "Spring Storm Watching",
  "The Equinox Reset",
  "Summer Night Series",
  "Fall Foraging Walk"
 ],
 "Advanced": [
  "The Four-Season Garden",
  "Seasonal Ritual Year",
  "The Harvest Feast Tradition",
  "Winter Hygge Mastery",
  "The Migration Watch",
  "Seasonal Photography Project",
  "The Cabin Seasons",
  "Legacy: Family Seasonal Traditions",
  "Masterclass: Living Seasonally",
  "The Climate-Adaptive Year"
 ]
};
var BLURBS={
 "First Signs of Spring Walk": "Hunt for buds, birds, and blooms. Spring\u2019s opening credits, live.",
 "Spring Cleaning Party": "Music, friends, open windows: the annual reset as celebration.",
 "Plant Something Day": "One seed, one pot, one promise of green. Spring in miniature.",
 "The First Picnic": "Blanket, sandwiches, sunshine: the season\u2019s inaugural outdoor meal.",
 "Rainy Spring Reading": "A stormy afternoon with a book: spring\u2019s cozy counterpoint.",
 "Summer Swim Kickoff": "First dip of the season: the official start of summer.",
 "The Longest Day Plan": "Solstice celebration: maximize daylight, minimize sleep (once).",
 "Berry Picking Morning": "Stained fingers, full baskets: summer\u2019s sweetest chore.",
 "Autumn Leaf Walk": "Crunch through the color: fall\u2019s free parade.",
 "The First Fire Night": "Chilly evening, warm fire: autumn\u2019s opening ceremony.",
 "Apple Everything Weekend": "Pick, bake, press: the harvest in full delicious swing.",
 "Winter Cozy Nest Day": "Blankets, cocoa, candles: the art of staying in, perfected.",
 "Spring Garden Launch": "Plan and plant the full garden: the season\u2019s big project.",
 "The Spring Festival Circuit": "Local festivals bloom with the flowers: go to all of them.",
 "Summer Water Tour": "Lakes, rivers, pools: a summer mapped by swimming spots.",
 "The Harvest Preserve": "Can, freeze, and ferment summer\u2019s peak: winter-you says thanks.",
 "Autumn Hiking Series": "Weekly hikes through the color change: fall as a season-long show.",
 "The Halloween Build-Up": "Costumes, decor, and spooky nights: October as a full production.",
 "Winter Lights Tour": "Drive or walk the best displays: the season\u2019s free art gallery.",
 "The Cozy Cooking Season": "Soups, stews, and baking: winter\u2019s delicious defense.",
 "Spring Storm Watching": "Safe, spectacular: thunderheads as theater.",
 "The Equinox Reset": "Balance day, balance life: twice-yearly personal audits.",
 "Summer Night Series": "Outdoor movies, concerts, and markets: summer after dark.",
 "Fall Foraging Walk": "Mushrooms, nuts, and apples (know before you eat): the wild harvest.",
 "The Four-Season Garden": "A garden designed for year-round beauty and harvest: the master plan.",
 "Seasonal Ritual Year": "Twelve monthly rituals marking the year\u2019s turn: a full cycle of intention.",
 "The Harvest Feast Tradition": "An annual feast from your own growing: the year\u2019s delicious climax.",
 "Winter Hygge Mastery": "The Danish art of coziness, fully embraced: a philosophy of winter.",
 "The Migration Watch": "Follow birds or whales through the seasons: nature\u2019s grand calendar.",
 "Seasonal Photography Project": "One photo a week for a year: the seasons, documented.",
 "The Cabin Seasons": "A year of visits to one wild place: watch it change, change with it.",
 "Legacy: Family Seasonal Traditions": "The seasonal rituals worth handing down: a family\u2019s year, designed.",
 "Masterclass: Living Seasonally": "Aligning life, food, and energy with the year\u2019s natural rhythm.",
 "The Climate-Adaptive Year": "Enjoying every season as weather shifts: resilience as recreation."
};

function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}

function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — seasonal activity record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-seasonal-fun',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();