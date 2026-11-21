/* Tools for Signature Library — the mirror's own rules, run in the page. */
var BOOKS=[{"title": "The Silver Lantern", "subjects": ["stories", "tales"], "pages": 214}, {"title": "Tales of the Quiet Valley", "subjects": ["stories", "tales"], "pages": 186}, {"title": "The Brass Compass", "subjects": ["travel", "maps"], "pages": 248}, {"title": "Roads of the Far Coast", "subjects": ["travel", "maps"], "pages": 301}, {"title": "How Rivers Shape Stone", "subjects": ["science", "nature"], "pages": 176}, {"title": "The Garden of Small Stars", "subjects": ["science", "nature"], "pages": 229}, {"title": "A Handbook of Knots", "subjects": ["craft", "making"], "pages": 142}, {"title": "The Weaver's Pattern Book", "subjects": ["craft", "making"], "pages": 198}, {"title": "Songs of the Harvest Moon", "subjects": ["stories", "poems"], "pages": 164}, {"title": "The Mapmaker's Apprentice", "subjects": ["travel", "stories"], "pages": 267}];

function readingDays(totalPages, perDay){
  var t=Number(totalPages), p=Number(perDay);
  if(!isFinite(t)||t<=0){return {ok:false,error:'Type a page count more than 0.'};}
  if(!isFinite(p)||p<=0){return {ok:false,error:'Type pages per day more than 0.'};}
  return {ok:true,total:t,perDay:p,days:Math.ceil(t/p)};
}
function findBooks(q){
  var needle=String(q||'').trim().toLowerCase();
  if(!needle){return {ok:false,error:'Type one subject word, such as stories or travel.'};}
  var words=needle.split(/\s+/), picked=[];
  for(var i=0;i<BOOKS.length;i++){
    var b=BOOKS[i], hay=b.subjects.join(' ')+' '+b.title.toLowerCase(), hit=false;
    for(var j=0;j<words.length;j++){ if(hay.indexOf(words[j])!==-1){hit=true;} }
    if(hit){picked.push(b);}
  }
  var total=0; for(var k=0;k<picked.length;k++){total+=picked[k].pages;}
  return {ok:true,books:picked,totalPages:total,count:picked.length};
}
if(typeof module!=='undefined'){module.exports={readingDays:readingDays,findBooks:findBooks,BOOKS:BOOKS};}
