/* Pure engine extracted verbatim from the word-processor service site (no document access). */

/* Pure word-count and download builders: no document access, testable in Node. */
function countWords(text){
  var words=(text||'').replace(/<[^>]*>/g,' ').split(/\s+/).filter(function(w){return w.length>0;});
  var sentences=(text||'').split(/[.!?]+/).filter(function(s){return s.trim().length>0;}).length;
  return {words:words.length, characters:(text||'').length, sentences:sentences};
}
function plainTextFromHtml(html){
  var t=(html||'').replace(/<\/(p|div|h[1-6]|li|tr)>/gi,'\n').replace(/<br\s*\/?>/gi,'\n').replace(/<[^>]*>/g,'');
  return t.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&nbsp;/g,' ').replace(/\n{3,}/g,'\n\n').trim();
}
function buildTxt(editorHtml){
  return plainTextFromHtml(editorHtml)+'\n';
}
function buildHtmlPage(editorHtml){
  return '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>My document</title>\n</head>\n<body style="font-family:Georgia,serif;max-width:700px;margin:2em auto;line-height:1.6">\n'+editorHtml+'\n</body>\n</html>\n';
}
if(typeof window!=='undefined'){ window.WPTool={countWords:countWords,plainTextFromHtml:plainTextFromHtml,buildTxt:buildTxt,buildHtmlPage:buildHtmlPage}; }

if(typeof module!=='undefined'){module.exports={countWords:countWords,plainTextFromHtml:plainTextFromHtml,buildTxt:buildTxt,buildHtmlPage:buildHtmlPage};}
