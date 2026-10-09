(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}
function fill(s,m){return s.replace(/\{(\w+)\}/g,function(_,k){return m[k]!=null?m[k]:'';});}

var CATS=['research','shopping','lookup','monitoring','general'];
var ACTIONS=['search','click','read','synthesize'];

var PLACES=['Tokyo','Paris','Cairo','Sydney','Oslo','Lima','Nairobi','Seoul'];
var POPS={'Tokyo':'14 million','Paris':'2.1 million','Cairo':'9.5 million','Sydney':'5.3 million','Oslo':'700,000','Lima':'9.8 million','Nairobi':'4.4 million','Seoul':'9.7 million'};
var PRODUCTS=['headphones','blender','laptop','tent','watch','backpack','keyboard','lamp'];
var STORES=['Harbor Books','QuickMart','Northwind Outfitters','Bright Shelf','Cedar Supply'];
var SITES=['shop.example.com','store.example.org','market.example.net'];

function researchTask(rnd){
  var place=pick(rnd,PLACES),pop=POPS[place];
  return {
   goal:'Find the current population of '+place+'.',
   actions:[
    {action:'search',target:'web search engine',result:'Searched "population of '+place+'".'},
    {action:'click',target:'encyclopedia result',result:'Opened demographics.'},
    {action:'read',target:'demographics',result:'Found the latest figure.'},
    {action:'synthesize',target:'results',result:'Cross-checked two sources.'}],
   answer:'The current population of '+place+' is about '+pop+'.',
   success:true};
}
function shoppingTask(rnd){
  var product=pick(rnd,PRODUCTS),price=ri(rnd,20,200)*5,site=pick(rnd,SITES);
  var best=price-ri(rnd,5,30);
  return {
   goal:'Find the cheapest '+product+' under $'+price+'.',
   actions:[
    {action:'search',target:'shopping search',result:'Searched "buy '+product+' under $'+price+'".'},
    {action:'click',target:site,result:'Opened the listing.'},
    {action:'read',target:'price and shipping',result:'Read price and shipping.'},
    {action:'click',target:'second retailer',result:'Opened a competitor.'},
    {action:'synthesize',target:'prices',result:'Compared final prices.'}],
   answer:'The cheapest '+product+' under $'+price+' is $'+best+' at '+site+', shipping included.',
   success:true};
}
function lookupTask(rnd){
  var store=pick(rnd,STORES),days=ri(rnd,1,3);
  var ok=rnd()<0.85;
  return {
   goal:"Look up "+store+"'s opening hours this weekend.",
   actions:[
    {action:'search',target:'web search engine',result:'Searched "'+store+' opening hours".'},
    {action:'click',target:'store page',result:'Opened the store page.'},
    {action:'read',target:'hours',result:ok?'Read weekend hours.':'Hours failed to load.'}],
   answer:ok?store+' is open 9:00 AM to 9:00 PM on Saturday and 10:00 AM to 6:00 PM on Sunday.':'The official hours page did not load; the lookup could not be completed.',
   success:ok};
}
function monitoringTask(rnd){
  var product=pick(rnd,PRODUCTS),start=ri(rnd,50,300),drop=ri(rnd,5,40),end=start-drop;
  return {
   goal:'Track the price of a '+product+' for a week and report the lowest price.',
   actions:[
    {action:'search',target:'price tracker',result:'Found the listing.'},
    {action:'read',target:'day-1 price',result:'Start price $'+start+'.'},
    {action:'read',target:'day-4 price',result:'Mid-week check.'},
    {action:'read',target:'day-7 price',result:'Final price $'+end+'.'},
    {action:'synthesize',target:'history',result:'Computed the weekly low.'}],
   answer:'The lowest observed price for the '+product+' this week was $'+end+' (started at $'+start+').',
   success:true};
}
function generalTask(rnd){
  var product=pick(rnd,PRODUCTS),site=pick(rnd,SITES);
  var rating=(3.5+rnd()*1.5).toFixed(1);
  return {
   goal:'Gather three user reviews of a popular '+product+'.',
   actions:[
    {action:'search',target:'review search',result:'Searched "'+product+' user reviews".'},
    {action:'click',target:site,result:'Opened reviews.'},
    {action:'read',target:'top reviews',result:'Read three reviews.'},
    {action:'synthesize',target:'themes',result:'Summarized praise and complaints.'}],
   answer:'Three reviews of the '+product+' average '+rating+' stars; users praise durability and complain about the manual.',
   success:true};
}

var BUILDERS={research:researchTask,shopping:shoppingTask,lookup:lookupTask,monitoring:monitoringTask,general:generalTask};

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var domain=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var t=BUILDERS[domain](rnd);
  var id='JAH-WEBTASK-'+pad6(seed);
  return {id:id,task_id:id,goal:t.goal,actions:t.actions,
    pages_visited:ri(rnd,2,8),final_answer:t.answer,success:t.success,
    domain:domain,title:t.goal.slice(0,80)};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-WEBTASK-\d{6}$/.test(r.id))e.push('id');
  if(r.task_id!==r.id)e.push('task_id');
  if(typeof r.goal!=='string'||!r.goal.length||r.goal.length>600)e.push('goal');
  if(!Array.isArray(r.actions)||r.actions.length<3||r.actions.length>6)e.push('actions');
  else r.actions.forEach(function(a,i){
    if(!a||typeof a!=='object'){e.push('actions['+i+']');return;}
    if(ACTIONS.indexOf(a.action)<0)e.push('actions['+i+'].action');
    if(typeof a.target!=='string'||!a.target.length)e.push('actions['+i+'].target');
    if(typeof a.result!=='string'||!a.result.length)e.push('actions['+i+'].result');
  });
  if(typeof r.pages_visited!=='number'||r.pages_visited<1)e.push('pages_visited');
  if(typeof r.final_answer!=='string'||!r.final_answer.length||r.final_answer.length>600)e.push('final_answer');
  if(typeof r.success!=='boolean')e.push('success');
  if(CATS.indexOf(r.domain)<0)e.push('domain');
  if(r.title!==String(r.goal).slice(0,80))e.push('title');
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-web-browsing-tasks-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('web-browsing-tasks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
