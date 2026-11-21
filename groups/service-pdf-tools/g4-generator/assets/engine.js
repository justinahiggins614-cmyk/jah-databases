/* Pure engine extracted verbatim from the pdf-tools service site (no document access). */

/* Pure PDF writer and reader: no document access, testable in Node.
   makePdf builds a real one-page PDF with a correct cross-reference
   table: header, six objects, xref, trailer, startxref, %%EOF. */
function latin1(s){
  return String(s||'').replace(/[^\x00-\xff]/g,'?');
}
function escapePdfText(s){
  return latin1(s).replace(/\\/g,'\\\\').replace(/\(/g,'\\(').replace(/\)/g,'\\)');
}
function pad10(n){ var s=String(n); while(s.length<10) s='0'+s; return s; }
function makePdf(title, lines){
  var t=latin1(title||'Untitled').slice(0,80);
  var ls=(lines||[]).slice(0,40).map(function(l){return latin1(l).slice(0,90);});
  var stream=['BT /F1 18 Tf 72 720 Td ('+escapePdfText(t)+') Tj ET'];
  var y=690;
  ls.forEach(function(l){ stream.push('BT /F1 12 Tf 72 '+y+' Td ('+escapePdfText(l)+') Tj ET'); y-=20; });
  var streamText=stream.join('\n');
  var objects=[
    '<< /Type /Catalog /Pages 2 0 R >>',
    '<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
    '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>',
    '<< /Length '+streamText.length+' >>\nstream\n'+streamText+'\nendstream',
    '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
    '<< /Title ('+escapePdfText(t)+') /Producer (PDF Tools) >>'
  ];
  var out='%PDF-1.4\n', offsets=[0];
  objects.forEach(function(obj,i){
    offsets.push(out.length);
    out+=(i+1)+' 0 obj\n'+obj+'\nendobj\n';
  });
  var xrefPos=out.length;
  out+='xref\n0 7\n0000000000 65535 f \n';
  for(var i=1;i<=6;i++) out+=pad10(offsets[i])+' 00000 n \n';
  out+='trailer\n<< /Size 7 /Root 1 0 R /Info 6 0 R >>\nstartxref\n'+xrefPos+'\n%%EOF\n';
  return out;
}
function countPdfPages(text){
  var m=String(text||'').match(/\/Type\s*\/Page(?!s)/g);
  return m?m.length:0;
}
function unescapePdfText(s){
  return s.replace(/\\\(/g,'(').replace(/\\\)/g,')').replace(/\\\\/g,'\\');
}
function pdfInfo(text){
  var t=String(text||'');
  var ver=/^%PDF-([0-9.]+)/.exec(t);
  var title=/\/Title\s*\(((?:[^()\\]|\\.)*)\)/.exec(t);
  var author=/\/Author\s*\(((?:[^()\\]|\\.)*)\)/.exec(t);
  return {isPdf:t.indexOf('%PDF-')===0, version:ver?ver[1]:null,
    pages:countPdfPages(t), title:title?unescapePdfText(title[1]):null,
    author:author?unescapePdfText(author[1]):null, size:t.length};
}
if(typeof window!=='undefined'){ window.PdfTool={makePdf:makePdf,countPdfPages:countPdfPages,pdfInfo:pdfInfo,escapePdfText:escapePdfText}; }

if(typeof module!=='undefined'){module.exports={makePdf:makePdf,countPdfPages:countPdfPages,pdfInfo:pdfInfo,escapePdfText:escapePdfText};}
