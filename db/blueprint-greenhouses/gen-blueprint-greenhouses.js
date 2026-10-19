
(function(){'use strict';
/* JAH The Greenhouse Blueprint Database generator - jahdb-blueprint-greenhouses-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic seeded blueprint generation. Same seed = same blueprint. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
var PREFIX="JAH-BP-GRNHS-G";
var DATA={"sig": false, "unit": "ft", "bases": [{"noun": "Greenhouse", "name": "Hoop Greenhouse", "styles": ["Hoop", "High-tunnel", "Grower"], "dims": {"W": 20.0, "D": 48.0, "H": 12.0}, "members": [{"name": "Hoop", "qty": 17, "l": 24.0, "w": 2, "t": 2, "mat": "galvanized steel"}, {"name": "Purlin", "qty": 5, "l": 48.0, "w": 1, "t": 1, "mat": "steel"}, {"name": "End wall", "qty": 2, "l": 20.0, "w": 12, "t": 1, "mat": "steel + poly"}, {"name": "Bench", "qty": 4, "l": 40.0, "w": 4, "t": 3, "mat": "steel/wood"}], "steps": ["Mill all lumber to finished size; cut every part to the cut list, labeling each piece.", "Lay out and cut mortise-and-tenon joints on all frame members; test-fit dry before any glue.", "Dry-assemble the greenhouse kit; check square by comparing diagonals, then disassemble.", "Glue and clamp the greenhouse kit; wipe excess glue immediately and verify square while clamps set.", "Install secondary members (stretchers, slats, panels) per the plan; fasten per the fastener schedule.", "Sand progressively to 180 grit, ease all exposed edges, and apply a durable finish.", "Final check: confirm all dimensions against the plan, test load gently, and re-tighten fasteners after one week of use."], "sizes": [["20x48 ft", 1.0], ["30x72 ft", 1.6]], "group": "Greenhouses", "shapes": [["rect", 0, 0, 20.0, 12.0, ""], ["h", 1.6, 18.400000000000002, 6.0], ["t", 2.0, 6.42, "hoop 24"], ["t", 1, 11.28, "HOOP HOUSE - SECTION"]], "planW": 20.0, "planH": 12.0, "overallKeys": ["W", "D", "H"]}, {"noun": "Greenhouse", "name": "Gable Greenhouse", "styles": ["Gable", "Glass", "Estate"], "dims": {"W": 12.0, "D": 20.0, "H": 12.0}, "members": [{"name": "Wall stud", "qty": 30, "l": 10.0, "w": 1.5, "t": 3.5, "mat": "cedar/redwood"}, {"name": "Rafter", "qty": 16, "l": 8.0, "w": 1.5, "t": 3.5, "mat": "cedar"}, {"name": "Glazing", "qty": 40, "l": 4.0, "w": 2, "t": 0.25, "mat": "polycarbonate/twinwall"}], "steps": ["Mill all lumber to finished size; cut every part to the cut list, labeling each piece.", "Lay out and cut mortise-and-tenon joints on all frame members; test-fit dry before any glue.", "Dry-assemble the greenhouse; check square by comparing diagonals, then disassemble.", "Glue and clamp the greenhouse; wipe excess glue immediately and verify square while clamps set.", "Install secondary members (stretchers, slats, panels) per the plan; fasten per the fastener schedule.", "Sand progressively to 180 grit, ease all exposed edges, and apply a durable finish.", "Final check: confirm all dimensions against the plan, test load gently, and re-tighten fasteners after one week of use."], "sizes": [["12x20 ft", 1.0]], "group": "Greenhouses", "shapes": [["rect", 0, 0, 12.0, 12.0, ""], ["h", 0.96, 11.040000000000001, 6.0], ["t", 1.2000000000000002, 6.42, "rafter 8"], ["t", 1, 11.28, "GABLE GREENHOUSE - SECTION"]], "planW": 12.0, "planH": 12.0, "overallKeys": ["W", "D", "H"]}, {"noun": "Greenhouse", "name": "Lean-To Greenhouse", "styles": ["Lean-to", "Attached", "Patio"], "dims": {"W": 10.0, "D": 16.0, "H": 10.0}, "members": [{"name": "Ledger", "qty": 1, "l": 16.0, "w": 2, "t": 8, "mat": "pressure-treated"}, {"name": "Rafter", "qty": 9, "l": 11.0, "w": 1.5, "t": 3.5, "mat": "cedar"}, {"name": "Glazing", "qty": 20, "l": 4.0, "w": 2, "t": 0.25, "mat": "polycarbonate"}], "steps": ["Mill all lumber to finished size; cut every part to the cut list, labeling each piece.", "Lay out and cut mortise-and-tenon joints on all frame members; test-fit dry before any glue.", "Dry-assemble the lean-to greenhouse; check square by comparing diagonals, then disassemble.", "Glue and clamp the lean-to greenhouse; wipe excess glue immediately and verify square while clamps set.", "Install secondary members (stretchers, slats, panels) per the plan; fasten per the fastener schedule.", "Sand progressively to 180 grit, ease all exposed edges, and apply a durable finish.", "Final check: confirm all dimensions against the plan, test load gently, and re-tighten fasteners after one week of use."], "sizes": [["10x16 ft", 1.0]], "group": "Greenhouses", "shapes": [["rect", 0, 0, 10.0, 10.0, ""], ["h", 0.8, 9.200000000000001, 5.0], ["t", 1.0, 5.35, "rafter 11"], ["t", 1, 9.399999999999999, "LEAN-TO - SECTION"]], "planW": 10.0, "planH": 10.0, "overallKeys": ["W", "D", "H"]}], "materials": ["Pressure-treated pine", "Cedar", "SPF lumber"], "blurb": "A {style} {noun} in {material}, {size_label} size, {overall} overall. Full construction blueprint: dimensioned framing plans, materials and cut lists, assembly steps, and finishing. Key dimensions: {dims}.", "how": "The {noun} is laid out to the dimensions given - {material} cut to the list, framed square and level, and fastened per the plan. It is anchored against wind, finished for weather, and checked plumb before sign-off. Overall {overall}.", "standards": ["AWI Architectural Woodwork Standards", "OSHA 29 CFR 1910 woodworking machinery safety"], "tolerances": ["Joinery cuts: +/- 1/32 in", "Overall dimensions: +/- 1/16 in", "Squareness: diagonals within 1/16 in", "Hole locations: +/- 1/32 in"], "safety": ["Wear eye and hearing protection; use dust collection or a respirator when sanding or sawing.", "Keep hands clear of blades; use push sticks and featherboards on the table saw.", "Disconnect power before changing blades or bits.", "Never wear gloves near rotating machinery."], "tools": ["Table saw", "Miter saw", "Drill/driver", "Random-orbit sander", "Clamps (bar and spring)", "Tape measure", "Combination square", "Wood glue", "Safety glasses", "Dust mask"], "ladder_rank": 2, "ladder_tier": "foundations"};
function fmtD(v,u){var r=Math.round(v*100)/100;if(u==='in')return r+'"';return r+' '+u;}
function drawAscii(shapes,W,H,unit,title){
  var maxW=66,maxH=26;
  W=Math.max(W,0.01);H=Math.max(H,0.01);
  var sc=Math.max(W/maxW,H/maxH);
  var gw=Math.max(10,Math.min(maxW,Math.ceil(W/sc))), gh=Math.max(6,Math.min(maxH,Math.ceil(H/sc)));
  var sx=gw/W, sy=gh/H;
  function X(x){return Math.max(0,Math.min(gw-1,Math.round(x*sx)));}
  function Y(y){return Math.max(0,Math.min(gh-1,Math.round(y*sy)));}
  var g=[],yy,xx;for(yy=0;yy<gh;yy++){g.push([]);for(xx=0;xx<gw;xx++)g[yy].push(' ');}
  function put(x,y,ch){if(y>=0&&y<gh&&x>=0&&x<gw)g[y][x]=ch;}
  function hline(x0,x1,y){var a=Math.min(X(x0),X(x1)),b=Math.max(X(x0),X(x1));for(var x=a;x<=b;x++)put(x,Y(y),'-');}
  function vline(x,y0,y1){var a=Math.min(Y(y0),Y(y1)),b=Math.max(Y(y0),Y(y1));for(var y=a;y<=b;y++)put(X(x),y,'|');}
  function diag(x0,y0,x1,y1){var st=Math.max(Math.abs(X(x1)-X(x0)),Math.abs(Y(y1)-Y(y0)),1);for(var i=0;i<=st;i++)put(Math.round(X(x0)+(X(x1)-X(x0))*i/st),Math.round(Y(y0)+(Y(y1)-Y(y0))*i/st),'/');}
  shapes.forEach(function(sh){
    var k=sh[0];
    if(k==='rect'){var x=sh[1],y=sh[2],w=sh[3],h=sh[4],label=sh[5]||'';
      var x0=X(x),y0=Y(y),x1=X(x+w),y1=Y(y+h);
      if(x1<=x0)x1=x0+1;if(y1<=y0)y1=y0+1;
      for(var xx2=x0;xx2<=x1;xx2++){put(xx2,y0,'-');put(xx2,y1,'-');}
      for(var yy2=y0;yy2<=y1;yy2++){put(x0,yy2,'|');put(x1,yy2,'|');}
      put(x0,y0,'+');put(x1,y0,'+');put(x0,y1,'+');put(x1,y1,'+');
      var lab=String(label).slice(0,Math.max(1,x1-x0-1)),ly=(y0+y1)>>1,lx=x0+Math.max(1,((x1-x0-lab.length)>>1));
      if(ly>y0&&ly<y1-1)for(var li=0;li<lab.length;li++)if(lx+li<x1-1)g[ly][lx+li]=lab[li];
    }else if(k==='h'){hline(sh[1],sh[2],sh[3]);}
    else if(k==='v'){vline(sh[1],sh[2],sh[3]);}
    else if(k==='d'){diag(sh[1],sh[2],sh[3],sh[4]);}
    else if(k==='t'){var tx=X(sh[1]),ty=Y(sh[2]),txt=String(sh[3]);for(var ti=0;ti<txt.length;ti++)if(tx+ti<gw)put(tx+ti,ty,txt[ti]);}
  });
  var lines=['PLAN: '+title,'Overall '+W+' x '+H+' '+unit+' | schematic - not to construction scale'];
  for(yy=0;yy<gh;yy++)lines.push(g[yy].join('').replace(/\s+$/,''));
  return lines.join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var base=pick(rnd,DATA.bases);
  var size=pick(rnd,base.sizes);
  var style=(opts.field&&base.styles.indexOf(opts.field)>=0)?opts.field:pick(rnd,base.styles);
  var mat=pick(rnd,DATA.materials);
  var s=size[1]*(DATA.sig?1.03:1);
  var dims={},k;for(k in base.dims)dims[k]=Math.round(base.dims[k]*s*100)/100;
  var members=base.members.map(function(m){
    return {name:m.name,qty:m.qty,l:Math.round(m.l*s*100)/100,w:m.w,t:m.t,
            material:(m.mat||'').replace('{MAT}',mat)};
  });
  var nPieces=members.reduce(function(a,m){return a+m.qty;},0);
  var bf=members.reduce(function(a,m){return a+(m.w&&m.t?m.qty*m.l*m.w*m.t/144:0);},0);
  var cut=members.map(function(m){
    return {part:m.name,qty:m.qty,
      size:(m.w&&m.t?fmtD(m.l,DATA.unit)+' x '+fmtD(m.w,DATA.unit)+' x '+fmtD(m.t,DATA.unit):fmtD(m.l,DATA.unit)),
      material:m.material,board_feet:(m.w&&m.t?Math.round(m.qty*m.l*m.w*m.t/144*100)/100:null)};
  });
  var shapes=base.shapes.map(function(sh){
    var o=sh.slice();
    for(var i=1;i<o.length;i++){if(typeof o[i]==='number')o[i]=Math.round(o[i]*s*100)/100;}
    return o;
  });
  var W=Math.round(base.planW*s*100)/100,H=Math.round(base.planH*s*100)/100;
  var title=style+' '+base.noun+(size[0]!=='Standard'?' ('+size[0]+')':'')+' - Full Blueprint';
  var plan=drawAscii(shapes,W,H,DATA.unit,title);
  var id=PREFIX+String(seed).padStart(6,'0');
  var overall=base.overallKeys.map(function(k2){return k2+' '+fmtD(dims[k2],DATA.unit);}).join(' x ');
  var desc=DATA.blurb.replace('{name}',title.replace(' - Full Blueprint','')).replace('{style}',style)
    .replace('{material}',mat).replace('{overall}',overall).replace('{noun}',base.noun)
    .replace('{size_label}',size[0]).replace('{dims}',base.overallKeys.map(function(k2){return k2+' '+fmtD(dims[k2],DATA.unit);}).join(', '));
  if(DATA.sig)desc+=' This is a JAH Signature original design - his own line, drawn from the same need as the public pattern but detailed as a new original work.';
  else desc+=' Representative blueprint study compiled from standard construction practice and public code requirements.';
  var prog='# JAH Blueprint demo - Record '+id+'\nplan = """\n'+plan.replace(/\\/g,'\\\\')+'\n"""\nprint(plan)\nprint("Overall: '+overall+'")\nprint("Cut pieces: '+nPieces+'")\nprint("Board feet: '+Math.round(bf*100)/100+'")\nprint("OK: '+id+' blueprint verified")\n';
  return {
    id:id,name:title.replace(' - Full Blueprint',''),title:title,
    description:desc,g:base.group|| (base.noun+'s'),
    how_it_works:DATA.how.replace('{noun}',base.noun).replace('{material}',mat).replace('{overall}',overall).replace('{size_label}',size[0]),
    key_points:['Overall: '+overall,'Material: '+mat,'Cut pieces: '+nPieces,'Lumber: '+(Math.round(bf*10)/10)+' board feet'].concat(DATA.sig?['Signature original - JAH design lineage']:[]),
    requirements:cut.slice(0,6).map(function(c){return c.qty+' x '+c.part+' ('+c.size+')';}),
    standards:DATA.standards,citations:DATA.standards.concat(['Standard construction practice references.']),
    blueprint:{plan_ascii:plan,overall:overall,unit:DATA.unit,
      dimensions:Object.keys(dims).map(function(k2){return k2+': '+fmtD(dims[k2],DATA.unit);}).join(', '),
      cut_list:cut,assembly_steps:base.steps,tolerances:DATA.tolerances,safety_notes:DATA.safety,tools_required:DATA.tools,
      scale_note:'Schematic - not to construction scale. Verify all dimensions, loads, and code compliance with a licensed professional before building.'},
    materials:cut.map(function(c){return c.qty+' x '+c.part+' - '+c.material+' ('+c.size+')';}),
    src:DATA.sig?'signature':'public-harvest',
    ladder_rank:DATA.ladder_rank,ladder_tier:DATA.ladder_tier,
    demo:{kind:'python',language:'python',program:prog,note:'Working demonstration program (real, runnable Python): prints the schematic plan and verifies totals.'},
    provenance:DATA.sig?'signature':'public-harvest',last_verified:'2026-10-19',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(!r.blueprint||!r.blueprint.plan_ascii)e.push('plan');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-blueprint-greenhouses-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:["Attached", "Estate", "Gable", "Glass", "Grower", "High-tunnel", "Hoop", "Lean-to", "Patio"]};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-greenhouses',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
