
/* PURE TOOL FUNCTIONS — the page's own working tool, tested in Node. */
var FC_SETS = null;
function csvParse(text){
  var rows=[], row=[], cur='', inQ=false;
  for(var i=0;i<text.length;i++){
    var c=text[i];
    if(inQ){
      if(c==='"'){ if(text[i+1]==='"'){cur+='"';i++;} else {inQ=false;} }
      else {cur+=c;}
    } else if(c==='"'){ inQ=true; }
    else if(c===','){ row.push(cur); cur=''; }
    else if(c==='\n' || c==='\r'){ if(c==='\r' && text[i+1]==='\n') i++; row.push(cur); cur=''; rows.push(row); row=[]; }
    else {cur+=c;}
  }
  if(cur!=='' || row.length){ row.push(cur); rows.push(row); }
  return rows.filter(function(r){ return r.length>1 || (r.length===1 && r[0].trim()!==''); });
}
function csvToJson(text){
  var rows=csvParse(text);
  if(!rows.length) return '[]';
  var headers=rows[0].map(function(h){return h.trim();});
  var out=rows.slice(1).map(function(r){
    var o={};
    headers.forEach(function(h,i){ o[h]=(i<r.length?r[i]:''); });
    return o;
  });
  return JSON.stringify(out, null, 2);
}
function jsonToCsv(text){
  var data=JSON.parse(text);
  if(!Array.isArray(data) || !data.length) throw new Error('JSON must be a list of records.');
  var headers=[];
  data.forEach(function(r){ Object.keys(r).forEach(function(k){ if(headers.indexOf(k)<0) headers.push(k); }); });
  function cell(v){
    var s=(v===null||v===undefined)?'':String(v);
    return /[",\n]/.test(s) ? '"'+s.replace(/"/g,'""')+'"' : s;
  }
  var lines=[headers.map(cell).join(',')];
  data.forEach(function(r){ lines.push(headers.map(function(h){ return cell(r[h]); }).join(',')); });
  return lines.join('\n');
}
function textToJson(text){ return JSON.stringify({text: text}, null, 2); }
function escHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function mdInline(s){
  s=escHtml(s);
  s=s.replace(/`([^`]+)`/g,'<code>$1</code>');
  s=s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
  s=s.replace(/\*([^*]+)\*/g,'<em>$1</em>');
  s=s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2">$1</a>');
  return s;
}
function markdownToHtml(md){
  var lines=md.split('\n'), out=[], inList=false;
  function closeList(){ if(inList){ out.push('</ul>'); inList=false; } }
  lines.forEach(function(line){
    var m;
    if((m=line.match(/^(#{1,6})\s+(.*)$/))){ closeList(); out.push('<h'+m[1].length+'>'+mdInline(m[2])+'</h'+m[1].length+'>'); }
    else if((m=line.match(/^[-*]\s+(.*)$/))){ if(!inList){ out.push('<ul>'); inList=true; } out.push('<li>'+mdInline(m[1])+'</li>'); }
    else if(line.trim()===''){ closeList(); }
    else { closeList(); out.push('<p>'+mdInline(line)+'</p>'); }
  });
  closeList();
  return out.join('\n');
}
function htmlToText(htmlStr){
  var s=htmlStr.replace(/<(h[1-6]|p|div|li|tr|br)[^>]*>/gi,'\n');
  s=s.replace(/<[^>]+>/g,'');
  s=s.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&nbsp;/g,' ');
  return s.replace(/\n{3,}/g,'\n\n').trim();
}
function changeCase(text, mode){
  if(mode==='upper') return text.toUpperCase();
  if(mode==='lower') return text.toLowerCase();
  if(mode==='title') return text.replace(/\w\S*/g,function(w){ return w.charAt(0).toUpperCase()+w.slice(1).toLowerCase(); });
  if(mode==='sentence') return text.replace(/(^\s*[a-z]|[.!?]\s+[a-z])/g,function(m){ return m.toUpperCase(); });
  return text;
}
function prettyJson(text){ return JSON.stringify(JSON.parse(text), null, 2); }
function minifyJson(text){ return JSON.stringify(JSON.parse(text)); }


if(typeof module!=='undefined'){module.exports={csvParse: csvParse, csvToJson: csvToJson, jsonToCsv: jsonToCsv, textToJson: textToJson, markdownToHtml: markdownToHtml, htmlToText: htmlToText, changeCase: changeCase, prettyJson: prettyJson, minifyJson: minifyJson};}
