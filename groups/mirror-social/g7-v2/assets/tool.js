/* Tools for Signature Social — the mirror's own rules, run in the page. */
var POSTS=[{"author": "Rin", "text": "Morning walk by the river, mist on the water.", "likes": 14, "comments": 3}, {"author": "Mara", "text": "The garden beds are planted for the season.", "likes": 21, "comments": 5}, {"author": "Theo", "text": "Solved the puzzle on the third try today.", "likes": 9, "comments": 2}, {"author": "June", "text": "Sailed past the harbor at sunrise.", "likes": 30, "comments": 7}, {"author": "Ansel", "text": "Finished the chair, sanded smooth.", "likes": 17, "comments": 4}, {"author": "Wren", "text": "New painting: blue hills at dusk.", "likes": 25, "comments": 6}, {"author": "Kofi", "text": "Drumming practice went well tonight.", "likes": 11, "comments": 1}, {"author": "Lena", "text": "Finished the big book on maps.", "likes": 19, "comments": 8}];

function postScore(likes, comments){
  var l=Number(likes), c=Number(comments);
  if(!isFinite(l)||l<0||Math.floor(l)!==l){return {ok:false,error:'Type whole likes, 0 or more.'};}
  if(!isFinite(c)||c<0||Math.floor(c)!==c){return {ok:false,error:'Type whole comments, 0 or more.'};}
  return {ok:true,score:l+2*c};
}
function rankPosts(posts){
  var copy=posts.slice();
  copy.sort(function(a,b){return (b.likes+2*b.comments)-(a.likes+2*a.comments);});
  return {ok:true,posts:copy};
}
function newPost(text){
  var t=String(text||'').trim();
  if(!t){return {ok:false,error:'Type a short message first.'};}
  if(t.length>140){return {ok:false,error:'That message is longer than 140 characters.'};}
  return {ok:true,text:t,likes:0,comments:0,score:0};
}
if(typeof module!=='undefined'){module.exports={postScore:postScore,rankPosts:rankPosts,newPost:newPost,POSTS:POSTS};}
