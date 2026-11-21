/* Tools for Signature Shop — the mirror's own rules, run in the page. */
var GOODS=[{"name": "Signature Lantern", "amount": 12, "desc": "a hand-held light"}, {"name": "Signature Mug", "amount": 8, "desc": "a cup for hot drinks"}, {"name": "Signature Blanket", "amount": 25, "desc": "a warm woven cover"}, {"name": "Signature Kettle", "amount": 30, "desc": "a pot for boiling water"}, {"name": "Signature Scarf", "amount": 15, "desc": "a warm neck wrap"}, {"name": "Signature Notebook", "amount": 6, "desc": "a book of blank pages"}, {"name": "Signature Candle", "amount": 9, "desc": "a wax light"}, {"name": "Signature Backpack", "amount": 40, "desc": "a bag with straps"}, {"name": "Signature Water Bottle", "amount": 14, "desc": "a bottle for water"}, {"name": "Signature Clock", "amount": 22, "desc": "a clock for the wall"}];

function findProduct(name){
  var needle=String(name||'').trim().toLowerCase();
  if(!needle){return {ok:false,error:'Type a good from the catalog, such as lantern.'};}
  for(var i=0;i<GOODS.length;i++){
    if(GOODS[i].name.toLowerCase().indexOf(needle)!==-1){return {ok:true,found:true,product:GOODS[i]};}
  }
  return {ok:true,found:false};
}
function lineTotal(amount, qty){
  var a=Number(amount), q=Number(qty);
  if(!isFinite(a)||a<0){return {ok:false,error:'The catalog number must be 0 or more.'};}
  if(!isFinite(q)||Math.floor(q)!==q||q<1){return {ok:false,error:'Type a whole quantity, 1 or more.'};}
  return {ok:true,line:a*q};
}
function cartTotal(lines){
  var total=0;
  for(var i=0;i<lines.length;i++){ total+=lines[i].line; }
  return {ok:true,total:total};
}
if(typeof module!=='undefined'){module.exports={findProduct:findProduct,lineTotal:lineTotal,cartTotal:cartTotal,GOODS:GOODS};}
