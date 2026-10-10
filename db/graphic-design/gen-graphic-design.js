(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['layouts','typography','color','branding','composition'];
var PREFIX='JAH-DES-';
var REF_COLOR='https://inventivehq.com/blog/color-harmonies-guide-web-design';
var REF_TYPE='https://github.com/igbuend/grimbard/blob/HEAD/skills/typography/typography-research.md';
var REF_STD='Design standards (verified 2026-10-09)';
function hsl(h,s,l){h=((h%360)+360)%360;s/=100;l/=100;var c=(1-Math.abs(2*l-1))*s,x=c*(1-Math.abs((h/60)%2-1)),m=l-c/2,r=0,g=0,b=0;
if(h<60){r=c;g=x;}else if(h<120){r=x;g=c;}else if(h<180){g=c;b=x;}else if(h<240){g=x;b=c;}else if(h<300){r=x;b=c;}else{r=c;b=x;}
function f(v){return Math.round((v+m)*255).toString(16).padStart(2,'0');}return '#'+f(r)+f(g)+f(b);}
var HUE12=['Red','Red-Orange','Orange','Yellow-Orange','Yellow','Yellow-Green','Green','Blue-Green','Blue','Blue-Violet','Violet','Red-Violet'];
var HARMONIES=[
 ['Complementary',[180],'Two hues 180 degrees apart for maximum contrast.','High energy and tension; best with one dominant hue.'],
 ['Analogous',[-30,30],'Neighboring hues that feel calm and cohesive.','Serene and unified; pick one hue to lead.'],
 ['Triadic',[120,240],'Three hues evenly spaced 120 degrees apart.','Balanced and vibrant; soften two of the three.'],
 ['Split-Complementary',[150,210],'A base hue plus the two colors beside its opposite.','Lively contrast that is easier to balance.'],
 ['Tetradic',[60,180,240],'Two complementary pairs forming a rectangle.','Rich and diverse; let one pair dominate.'],
 ['Square',[90,180,270],'Four hues spaced 90 degrees apart.','Bold and even; needs careful proportioning.'],
 ['Monochromatic',[0],'One hue in tints, shades and tones.','Elegant and minimal; add texture for depth.']
];
var PAL_CTX=['brand identity','web interface','poster design','packaging'];
var TYPE_ANATOMY=[
 ['Ascender','The part of a lowercase letter that rises above the x-height.','See b, d, f, h, k, l, t.'],
 ['Descender','The part of a lowercase letter that drops below the baseline.','See g, j, p, q, y.'],
 ['X-height','The height of lowercase letters, excluding ascenders and descenders.','A larger x-height reads better at small sizes.'],
 ['Cap height','The height of capital letters measured from the baseline.','Flat letters like H and E set the line.'],
 ['Baseline','The invisible line that most letters sit on.','Every upright letter rests on it.'],
 ['Serif','Small decorative strokes at the ends of letter strokes.','Bracketed serifs appear in Garamond.'],
 ['Counter','The enclosed or partially enclosed space inside a letter.','The hole inside the letters o, e and a.'],
 ['Aperture','The opening in letters like c, e and s.','Wider apertures stay legible when small.'],
 ['Stem','The main vertical or diagonal stroke of a letter.','The upright stroke of H or T.'],
 ['Bowl','The curved part of letters like b, d, o and p.','Round bowls need optical correction.'],
 ['Terminal','The end of a stroke that carries no serif.','Ball terminals close Bodoni strokes.'],
 ['Ligature','Two or more letters joined into a single glyph.','Common pairs: fi, fl and ff.'],
 ['Kerning','Spacing adjusted between two specific letter pairs.','Classic pairs: AV, To and VA.'],
 ['Tracking','Uniform letter spacing applied across a word or block.','CSS letter-spacing controls it.'],
 ['Leading','Baseline-to-baseline vertical space between lines.','CSS line-height; 1.5 suits body text.'],
 ['Glyph','Any individual character or symbol in a font.','Includes punctuation and figures.'],
 ['Small caps','Capitals drawn at x-height for acronyms in text.','Used for NASA and WHO in running copy.'],
 ['Tabular figures','Numerals of uniform width for aligned columns.','Required in price and data tables.'],
 ['Oldstyle figures','Numerals with ascenders and descenders.','They blend into lowercase text.'],
 ['Typeface','The design family; a font is one member of it.','Poppins is a typeface; Poppins Bold 16px is a font.']
];
var FONT_CLASSES=[
 ['Old-Style Serif','Traditional, trustworthy, literary.','Garamond, Caslon','Books and long-form reading.'],
 ['Transitional Serif','Versatile, refined, academic.','Baskerville, Times New Roman','Newspapers and academic text.'],
 ['Modern Serif','Elegant, dramatic, fragile at small sizes.','Bodoni, Didot','Luxury headlines.'],
 ['Slab Serif','Sturdy, industrial, retro.','Rockwell, Clarendon','Signage and web headings.'],
 ['Grotesque Sans','Neutral, corporate, functional.','Helvetica, Arial','Corporate interfaces.'],
 ['Neo-Grotesque Sans','Modern, clean, interface-first.','Inter, Roboto','App interfaces.'],
 ['Geometric Sans','Precise, friendly, logo-ready.','Futura, Montserrat','Logos and headlines.'],
 ['Humanist Sans','Warm, readable, accessible.','Gill Sans, Open Sans','Reading and accessibility.'],
 ['Monospace','Technical, precise, code-focused.','Courier, Fira Code','Code and data tables.'],
 ['Display','Expressive, decorative, brand-specific.','Bebas Neue, Playfair Display','Headlines, heroes and logos.']
];
var TYPE_SCALES=[['Major Second',1.125],['Minor Third',1.2],['Major Third',1.25],['Perfect Fourth',1.333],['Perfect Fifth',1.5]];
function typeSteps(ratio){var s=[];for(var i=-2;i<=3;i++)s.push(Math.round(16*Math.pow(ratio,i)*10)/10);return s;}
var LAYOUTS=[
 ['12-Column Grid','Twelve equal columns that content spans in multiples; the workhorse of responsive page layout.'],
 ['8-Point Grid','All spacing set in multiples of 8px so interface elements align to a shared rhythm.'],
 ['Baseline Grid','Text baselines lock to a fixed vertical rhythm for even, calm columns of type.'],
 ['Modular Grid','Columns crossed with rows form modules that hold cards, images and widgets.'],
 ['Manuscript Grid','A single column block for continuous reading, as in books and long articles.'],
 ['Column Grid','Two or more text columns for newspapers, magazines and dense editorial pages.'],
 ['Hierarchical Grid','An intuitive content-driven arrangement where emphasis sets the structure.'],
 ['Golden Ratio','The 1 to 1.618 proportion used to size and place elements for natural balance.'],
 ['Rule of Thirds','Key subjects sit on the intersections of a 3 by 3 grid for dynamic framing.']
];
var BRAND_RULES=[
 ['Clear Space','Keep an exclusion zone around the logo equal to its cap height on all sides.'],
 ['Minimum Size','Never reproduce the logo below 24px on screen or 8mm in print.'],
 ['Color Count','Limit the brand palette to two or three core colors plus neutrals.'],
 ['Contrast','Text must pass WCAG AA contrast: 4.5 to 1 for normal text.'],
 ['Consistency','One lockup, one voice and one palette across every touchpoint.'],
 ['Scalability','The mark must read at favicon size and on a billboard alike.'],
 ['Versatility','Supply full-color, mono and reversed versions for any background.'],
 ['Type Pairing','Pair one display face with one text face; never use more than three faces.']
];
var COMPOSITION=[
 ['Rule of Thirds','Place key subjects on the intersections of a 3 by 3 grid.'],
 ['Golden Ratio','Size and place elements in a 1 to 1.618 proportion.'],
 ['Leading Lines','Use lines in the scene to pull the eye toward the subject.'],
 ['Symmetry','Mirror elements across an axis for formality and calm.'],
 ['Negative Space','Empty areas give subjects room to breathe and speak.'],
 ['Visual Hierarchy','Size, weight and color tell the eye what matters first.'],
 ['60-30-10','Split color into 60 percent dominant, 30 secondary and 10 accent.'],
 ['Contrast','Opposites in tone, size or color create emphasis.'],
 ['Alignment','Every element visually connects to another; nothing floats alone.'],
 ['Proximity','Group related items together and separate unrelated ones.']
];
var SIG_A=['Velvet','Prism','Ember','Harbor','Cinder','Juniper','Onyx','Solstice','Meridian','Halcyon'];
var SIG_B=['mark','studio','press','works','line','atelier','foundry','guild'];
function sigPalette(rnd){var n=ri(rnd,3,5),p=[],h0=ri(rnd,0,359);for(var i=0;i<n;i++)p.push(hsl(h0+i*ri(rnd,40,90),ri(rnd,45,80),ri(rnd,35,65)));return p;}
function sigFaces(rnd){var A=['Avenir','Futura','Garamond','Helvetica','Baskerville','Inter','Roboto','Montserrat','Playfair','Lora'];return pick(A,rnd)+' + '+pick(A,rnd);}
function buildOnline(rnd,cat){
  var rec={category:cat,source:'online',creation_mode:'ONLINE-VERIFIED'};
  if(cat==='color'){
    var hi=ri(rnd,0,35),deg=hi*10,hm=pick(HARMONIES,rnd),ctx=pick(PAL_CTX,rnd);
    var name=HUE12[Math.round(hi/3)%12],pal;
    if(hm[0]==='Monochromatic')pal=[hsl(deg,72,32),hsl(deg,72,52),hsl(deg,72,72)];
    else pal=[hsl(deg,72,52)].concat(hm[1].map(function(o){return hsl(deg+o,72,52);}));
    rec.title=hm[0]+' palette on '+name+' — '+ctx;
    rec.topic='color harmony';rec.palette=pal;
    rec.spec={base_hue_deg:deg,base_hue_name:name,harmony:hm[0],offsets:hm[1],saturation:72,lightness:52,geometry:hm[2],mood:hm[3],use:ctx};
    rec.source_ref=REF_COLOR;
    rec.description='A '+hm[0].toLowerCase()+' palette built on '+name+' ('+deg+' degrees) for '+ctx+'. '+hm[2]+' The swatches are '+pal.join(', ')+'. '+hm[3];
  }else if(cat==='typography'){
    var t=pick(TYPE_ANATOMY,rnd);
    rec.title='Typography anatomy: '+t[0];
    rec.topic='type anatomy';rec.spec={term:t[0],definition:t[1],example:t[2]};
    rec.source_ref=REF_TYPE;
    rec.description='The term '+t[0]+' means: '+t[1]+' '+t[2]+' Knowing type anatomy helps designers judge sizing, pairing and spacing instead of guessing.';
  }else if(cat==='layouts'){
    var L=pick(LAYOUTS,rnd);
    rec.title='Layout system: '+L[0];
    rec.topic='layout system';rec.spec={system:L[0],rule:L[1]};
    rec.source_ref=REF_STD;
    rec.description='The '+L[0]+' is a standard layout system. '+L[1]+' Apply it consistently so pages feel ordered and every element has a clear place.';
  }else if(cat==='branding'){
    var B=pick(BRAND_RULES,rnd);
    rec.title='Branding rule: '+B[0];
    rec.topic='brand guideline';rec.spec={rule:B[0],guidance:B[1]};
    rec.source_ref=REF_STD;
    rec.description='A core branding rule: '+B[0]+'. '+B[1]+' Following it keeps the brand recognizable and professional across every touchpoint.';
  }else{
    var C=pick(COMPOSITION,rnd);
    rec.title='Composition rule: '+C[0];
    rec.topic='composition';rec.spec={rule:C[0],guidance:C[1]};
    rec.source_ref=REF_STD;
    rec.description='The '+C[0]+' is a classic composition rule. '+C[1]+' Use it to guide the viewer\u2019s eye and give the layout a clear focal point.';
  }
  return rec;
}
function buildSignature(rnd,cat){
  var rec={category:cat,source:'signature',creation_mode:'SIGNATURE-GENERATED'};
  var nm=pick(SIG_A,rnd)+' '+pick(SIG_B,rnd);
  if(cat==='color'){
    var pal=sigPalette(rnd);
    rec.title='Signature palette: '+nm;rec.topic='signature palette';rec.palette=pal;
    rec.spec={name:nm,swatches:pal,swatch_count:pal.length};
    rec.description='A Signature-generated palette named '+nm+' with '+pal.length+' swatches: '+pal.join(', ')+'. It was composed by the JAH generator as an original color study, marked as a Signature creation rather than a standard harmony.';
  }else if(cat==='typography'){
    var faces=sigFaces(rnd);
    rec.title='Signature type pairing: '+faces;rec.topic='type pairing';
    rec.spec={pairing:faces,headline_size:ri(rnd,28,64),body_size:ri(rnd,14,18),line_height:1.5};
    rec.description='A Signature-generated type pairing, '+faces+', set with '+rec.spec.headline_size+'px headlines and '+rec.spec.body_size+'px body copy at 1.5 line height. An original pairing study by the JAH generator.';
  }else if(cat==='layouts'){
    var cols=ri(rnd,2,12),gut=ri(rnd,8,32),mar=ri(rnd,16,64);
    rec.title='Signature layout: '+cols+'-column study';rec.topic='layout study';
    rec.spec={columns:cols,gutter_px:gut,margin_px:mar,study:nm};
    rec.description='A Signature-generated '+cols+'-column layout study with '+gut+'px gutters and '+mar+'px margins. An original grid experiment by the JAH generator, ready to adapt to real content.';
  }else if(cat==='branding'){
    rec.title='Signature brand concept: '+nm;rec.topic='brand concept';
    rec.spec={concept:nm,colors:sigPalette(rnd),voice:pick(['bold','calm','playful','precise'],rnd)};
    rec.description='A Signature-generated brand concept named '+nm+' with a '+rec.spec.voice+' voice and an original palette. A homegrown branding study, marked as a Signature creation.';
  }else{
    rec.title='Signature composition study: '+nm;rec.topic='composition study';
    rec.spec={study:nm,rule:pick(COMPOSITION,rnd)[0],subject:pick(['still life','portrait','landscape','poster'],rnd)};
    rec.description='A Signature-generated composition study applying the '+rec.spec.rule+' to a '+rec.spec.subject+'. An original arrangement study by the JAH generator.';
  }
  return rec;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var online=!opts.forceSignature&&(rnd()<0.24||opts.forceOnline);
  var rec=online?buildOnline(rnd,cat):buildSignature(rnd,cat);
  if(rec.description.length<165)rec.description+=' Filed as a complete searchable record in the JAH Data Bases archive, with its full specifications intact.';
  rec.id=PREFIX+String(seed).padStart(7,'0');
  rec._seed=seed;
  return rec;
}
function isHex(s){return /^#[0-9a-f]{6}$/.test(s||'');}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-DES-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<150)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&(r.creation_mode!=='ONLINE-VERIFIED'||typeof r.source_ref!=='string'||!r.source_ref.length))e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(!r.spec||typeof r.spec!=='object')e.push('spec');
  if(r.palette){if(!Array.isArray(r.palette)||r.palette.length<2||r.palette.length>6||!r.palette.every(isHex))e.push('palette');
    else if(r.source==='online'&&r.category==='color'){
      var s=r.spec,exp=s.harmony==='Monochromatic'?[hsl(s.base_hue_deg,72,32),hsl(s.base_hue_deg,72,52),hsl(s.base_hue_deg,72,72)]:[hsl(s.base_hue_deg,72,52)].concat(s.offsets.map(function(o){return hsl(s.base_hue_deg+o,72,52);}));
      if(exp.join(',')!==r.palette.join(','))e.push('palette_recompute');
    }}
  if(r.topic==='type anatomy'&&r.spec.term!==undefined){
    var f=TYPE_ANATOMY.filter(function(x){return x[0]===r.spec.term;})[0];
    if(!f||f[1]!==r.spec.definition)e.push('anatomy_fact');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-graphic-design-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('graphic-design',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
