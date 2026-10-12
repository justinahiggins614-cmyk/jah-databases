/* Blocks — falling-block puzzle (tetromino-style). Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('blocks', {
  title:'Blocks', W:360, H:600,
  controls:{ dpad:false, buttons:[{k:'left',label:'◀'},{k:'right',label:'▶'},{k:'down',label:'▼'},{k:'a',label:'⟳'},{k:'b',label:'⤓'}] },
  help:'←/→ move, ↓ soft drop, ↑ or Z rotate, SPACE hard drop. Numpad 4/6/2/8/5/0 work too.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.cols=10; this.rows=20; this.cs=24; this.ox=(P.W-this.cols*this.cs)/2; this.oy=40;
    this.grid=[]; for(var r=0;r<this.rows;r++){ this.grid.push([]); for(var c=0;c<this.cols;c++) this.grid[r].push(0); }
    this.score=0; this.lines=0; this.level=1; this.over=false; this.acc=0;
    this.shapes=[
      {c:'#00e5e5',m:[[1,1,1,1]]},
      {c:'#ffd43b',m:[[1,1],[1,1]]},
      {c:'#9b5de5',m:[[0,1,0],[1,1,1]]},
      {c:'#00e5a0',m:[[0,1,1],[1,1,0]]},
      {c:'#e5484d',m:[[1,1,0],[0,1,1]]},
      {c:'#2f7bff',m:[[1,0,0],[1,1,1]]},
      {c:'#ff8b3e',m:[[0,0,1],[1,1,1]]}
    ];
    this.next=(Math.random()*7)|0;
    this.spawn(P);
  },
  spawn:function(P){
    var s=this.shapes[this.next]; this.next=(Math.random()*7)|0;
    this.cur={m:s.m.map(function(r){return r.slice();}),c:s.c,x:3,y:0};
    if(this.collide(this.cur)){ this.over=true; P.beep(150,.4,'sawtooth'); }
  },
  collide:function(p){
    for(var r=0;r<p.m.length;r++) for(var c=0;c<p.m[r].length;c++){
      if(!p.m[r][c]) continue;
      var x=p.x+c, y=p.y+r;
      if(x<0||x>=this.cols||y>=this.rows) return true;
      if(y>=0&&this.grid[y][x]) return true;
    }
    return false;
  },
  rot:function(p){
    var m=p.m, n=m.length, out=[];
    for(var r=0;r<n;r++){ out.push([]); for(var c=0;c<n;c++) out[r].push(0); }
    for(var r2=0;r2<n;r2++) for(var c2=0;c2<n;c2++) out[c2][n-1-r2]=m[r2][c2];
    return out;
  },
  lock:function(P){
    var p=this.cur;
    for(var r=0;r<p.m.length;r++) for(var c=0;c<p.m[r].length;c++)
      if(p.m[r][c]&&p.y+r>=0) this.grid[p.y+r][p.x+c]=p.c;
    var cleared=0;
    for(var r2=this.rows-1;r2>=0;r2--){
      var full=true;
      for(var c2=0;c2<this.cols;c2++) if(!this.grid[r2][c2]){full=false;break;}
      if(full){ this.grid.splice(r2,1); this.grid.unshift(new Array(this.cols).fill(0)); cleared++; r2++; }
    }
    if(cleared){
      this.lines+=cleared; this.score+=[0,100,300,500,800][cleared]*this.level;
      this.level=1+((this.lines/10)|0); P.beep(660+cleared*120,.09);
    }
    this.spawn(P);
  },
  update:function(P,dt){
    if(this.over){ if(P.pressed.start||P.pressed.a) this.reset(P); return; }
    var k=P.keys, p=this.cur;
    if(P.pressed.left){ p.x--; if(this.collide(p))p.x++; }
    if(P.pressed.right){ p.x++; if(this.collide(p))p.x--; }
    if(P.pressed.up||P.pressed.a){
      var old=p.m; p.m=this.rot(p);
      if(this.collide(p)) p.m=old; else P.beep(420,.04);
    }
    if(P.pressed.b||P.pressed.start){ while(!this.collide({m:p.m,c:p.c,x:p.x,y:p.y+1})){p.y++;} this.lock(P); P.beep(300,.07); return; }
    var fall=Math.max(0.06, 0.8-this.level*0.06);
    this.acc+=dt;
    if(k.down) this.acc+=dt*9;
    if(this.acc>=fall){ this.acc=0; p.y++; if(this.collide(p)){ p.y--; this.lock(P); } }
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    ctx.strokeStyle='#1d2c4d'; ctx.strokeRect(this.ox-2,this.oy-2,this.cols*this.cs+4,this.rows*this.cs+4);
    for(var r=0;r<this.rows;r++) for(var c=0;c<this.cols;c++){
      if(this.grid[r][c]){ ctx.fillStyle=this.grid[r][c]; ctx.fillRect(this.ox+c*this.cs+1,this.oy+r*this.cs+1,this.cs-2,this.cs-2); }
    }
    var p=this.cur;
    ctx.fillStyle=p.c;
    for(var r2=0;r2<p.m.length;r2++) for(var c2=0;c2<p.m[r2].length;c2++)
      if(p.m[r2][c2]&&p.y+r2>=0) ctx.fillRect(this.ox+(p.x+c2)*this.cs+1,this.oy+(p.y+r2)*this.cs+1,this.cs-2,this.cs-2);
    P.text('SCORE '+this.score, P.W/2, 14, 14, '#9fb3d8');
    P.text('LINES '+this.lines+'  LV '+this.level, P.W/2, P.H-12, 13, '#9fb3d8');
    if(this.over) P.text('GAME OVER — START to retry', P.W/2, P.H/2, 15, '#ff6b6b');
  }
});
