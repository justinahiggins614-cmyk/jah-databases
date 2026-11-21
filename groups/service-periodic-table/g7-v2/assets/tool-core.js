
/* PURE TOOL FUNCTIONS — the page's own working tool, tested in Node. */
function elementByNumber(list, z){
  for(var i=0;i<list.length;i++){ if(list[i].z===z) return list[i]; }
  return null;
}
function elementBySymbol(list, sym){
  var s=String(sym).toLowerCase();
  for(var i=0;i<list.length;i++){ if(list[i].symbol.toLowerCase()===s) return list[i]; }
  return null;
}
function elementByName(list, name){
  var s=String(name).toLowerCase();
  for(var i=0;i<list.length;i++){ if(list[i].name.toLowerCase()===s) return list[i]; }
  return null;
}
function filterByCategory(list, cat){
  return list.filter(function(e){ return e.category===cat; });
}
function searchElements(list, q){
  var s=String(q||'').trim().toLowerCase();
  if(!s) return list.slice();
  return list.filter(function(e){
    return e.name.toLowerCase().indexOf(s)>=0 || e.symbol.toLowerCase()===s ||
      String(e.z)===s || e.category.toLowerCase().indexOf(s)>=0;
  });
}


if(typeof module!=='undefined'){module.exports={elementByNumber: elementByNumber, elementBySymbol: elementBySymbol, elementByName: elementByName, filterByCategory: filterByCategory, searchElements: searchElements};}
