/* Tools for Signature Mail — the mirror's own rules, run in the page. */
var NAMES=[{"name": "Rin", "role": "baker"}, {"name": "Mara", "role": "gardener"}, {"name": "Theo", "role": "teacher"}, {"name": "June", "role": "sailor"}, {"name": "Ansel", "role": "carpenter"}, {"name": "Wren", "role": "painter"}, {"name": "Kofi", "role": "drummer"}, {"name": "Lena", "role": "librarian"}];

function lookupName(name){
  var needle=String(name||'').trim().toLowerCase();
  if(!needle){return {ok:false,error:'Type a name from the address book.'};}
  for(var i=0;i<NAMES.length;i++){
    if(NAMES[i].name.toLowerCase()===needle){return {ok:true,found:true,name:NAMES[i].name,role:NAMES[i].role};}
  }
  return {ok:true,found:false,name:String(name||'').trim()};
}
function composeLetter(recipient, subject){
  var r=String(recipient||'').trim(), s=String(subject||'').trim();
  var inBook=false, role='';
  for(var i=0;i<NAMES.length;i++){ if(NAMES[i].name.toLowerCase()===r.toLowerCase()){inBook=true; role=NAMES[i].role;} }
  if(!inBook){return {ok:false,error:'That name is not in the address book. Try Rin, Mara, Theo, June, Ansel, Wren, Kofi, or Lena.'};}
  if(s.length<1){return {ok:false,error:'The subject must not be empty.'};}
  return {ok:true,to:r,role:role,subject:s,
    message:'To '+r+' ('+role+') — Subject: '+s+' — ready to send.'};
}
if(typeof module!=='undefined'){module.exports={lookupName:lookupName,composeLetter:composeLetter,NAMES:NAMES};}
