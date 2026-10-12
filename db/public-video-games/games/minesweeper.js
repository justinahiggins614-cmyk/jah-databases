/* Minesweeper — classic mine-clearing puzzle. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('minesweeper', {
  title:'Minesweeper', W:400, H:560,
  controls:{ tap:true },
  help:'Tap / click a square to reveal. Right-click or long-press to flag a mine. Clear all safe squares.',
  init:function(P){ this.reset(P); window.__msGame=this; },
  reset:function(P){
    this.n=9; this.mines=10; this.cs=36; this.ox=(P.W-this.n*this.cs)/2; this.oy=70;
    this.g=[]; this.over=false; this.won=false; this.flags=0; this.revealed=0; this.started=false;
    this.flagMode=false;
    for(var r=0;r<this.n;r++){ this.g.push([]); for(var c=0;c<this.n;c++) this.g[r].push({m:false,n:0,open:false,fl:false}); }
  },
  arm:function(P,sr,sc){
    var placed=0, guard={};
    for(var dr=-1;dr<=1;dr++) for(var dc=-1;dc<=1;dc++) guard[(sr+dr)+','+(sc+dc)]=1;
    while(placed<this.mines){
      var r=(Math.random()*this.n)|0, c=(Math.random()*this.n)|0;
      if(this.g[r][c].m||guard[r+','+c]) continue;
      this.g[r][c].m=true; placed++;
    }
    for(var r2=0;r2<this.n;r2++) for(var c2=0;c2<this.n;c2++){
      if(this.g[r2][c2].m) continue;
      var n=0;
      for(var dr2=-1;dr2<=1;dr2++) for(var dc2=-1;dc2<=1;dc2++){
        var rr=r2+dr2, cc=c2+dc2;
        if(rr>=0&&cc>=0&&rr<this.n&&cc<this.n&&this.g[rr][cc].m) n++;
      }
      this.g[r2][c2].n=n;
    }
    this.started=true;
  },
  open:function(P,r,c){
    var cell=this.g[r][c];
    if(cell.open||cell.fl||this.over||this.won) return;
    if(!this.started) this.arm(P,r,c);
    if(cell.m){ this.over=true; P.beep(140,.4,'sawtooth'); return; }
    cell.open=true; this.revealed++; P.beep(520,.04);
    if(cell.n===0){
      for(var dr=-1;dr<=1;dr++) for(var dc=-1;dc<=1;dc++){
        var rr=r+dr, cc=c+dc;
        if(rr>=0&&cc>=0&&rr<this.n&&cc<this.n&&!this.g[rr][cc].open) this.open(P,rr,cc);
      }
    }
    if(this.revealed===this.n*this.n-this.mines){ this.won=true; P.beep(880,.3); }
  },
  flag:function(r,c){
    var cell=this.g[r][c];
    if(cell.open||this.over||this.won) return;
    cell.fl=!cell.fl; this.flags+=cell.fl?1:-1; PVG.beep(340,.05);
  },
  cellAt:function(P,x,y){
    var c=((x-this.ox)/this.cs)|0, r=((y-this.oy)/this.cs)|0;
    return (r>=0&&c>=0&&r<this.n&&c<this.n)?{r:r,c:c}:null;
  },
  update:function(P,dt){
    if(this.over||this.won){ if(P.pressed.start||P.pressed.a) this.reset(P); return; }
    var taps=P.tapQ;
    for(var i=0;i<taps.length;i++){
      var t=taps[i];
      if(t.y>P.H-52&&t.x>P.W/2-80&&t.x<P.W/2+80){ this.flagMode=!this.flagMode; PVG.beep(500,.05); continue; }
      var cl=this.cellAt(P,t.x,t.y);
      if(cl){ if(this.flagMode) this.flag(cl.r,cl.c); else this.open(P,cl.r,cl.c); }
    }
    P.clearTaps();
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    for(var r=0;r<this.n;r++) for(var c=0;c<this.n;c++){
      var cell=this.g[r][c], x=this.ox+c*this.cs, y=this.oy+r*this.cs;
      ctx.fillStyle=cell.open?'#132a55':'#1d2c4d';
      ctx.fillRect(x+1,y+1,this.cs-2,this.cs-2);
      if(cell.open&&!cell.m&&cell.n>0){
        var cols=['','#2f7bff','#00e5a0','#e5484d','#9b5de5','#ff8b3e','#00e5e5','#ffd43b','#e8f1ff'];
        P.text(cell.n, x+this.cs/2, y+this.cs/2+1, 18, cols[cell.n]||'#fff');
      }
      if(!cell.open&&cell.fl) P.text('⚑', x+this.cs/2, y+this.cs/2+1, 18, '#ffb020');
      if(this.over&&cell.m) P.text('✸', x+this.cs/2, y+this.cs/2+1, 18, '#e5484d');
    }
    P.text('MINES '+this.mines+'   FLAGS '+this.flags, P.W/2, 24, 15, '#9fb3d8');
    ctx.fillStyle=this.flagMode?'#ffb020':'#14305e';
    ctx.fillRect(P.W/2-80,P.H-48,160,36);
    P.text(this.flagMode?'⚑ FLAG MODE':'⛏ DIG MODE', P.W/2, P.H-30, 15, '#070b16');
    P.text('Tap board to '+(this.flagMode?'flag':'reveal')+' · tap button to switch', P.W/2, P.H-8, 11, '#9fb3d8');
    if(this.over) P.text('BOOM — START to retry', P.W/2, P.H/2, 17, '#ff6b6b');
    if(this.won) P.text('CLEARED! — START for new board', P.W/2, P.H/2, 17, '#00e5a0');
  }
});
/* right-click flags too (desktop) */
window.addEventListener('contextmenu', function(e){
  var c=e.target;
  if(c&&c.tagName==='CANVAS'&&window.__msGame){
    e.preventDefault();
    var r=c.getBoundingClientRect();
    var x=(e.clientX-r.left)*c.width/r.width, y=(e.clientY-r.top)*c.height/r.height;
    var cl=window.__msGame.cellAt({W:c.width,H:c.height},x,y);
    if(cl) window.__msGame.flag(cl.r,cl.c);
  }
});
