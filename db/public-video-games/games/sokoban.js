/* Sokoban — box-pushing puzzle. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('sokoban', {
  title:'Sokoban', W:400, H:600,
  controls:{ dpad:true, buttons:[{k:'a',label:'UNDO'},{k:'b',label:'RESET'}] },
  help:'Push all crates onto the glowing targets. Arrows / WASD / numpad / pad to move. A = undo, B = reset level.',
  init:function(P){ this.level=0; this.load(P); },
  levels:[
    ['#####','#.@.#','#.$$.#','#####'],
    ['#######','#.....#','#.@$#.#','#. $ #.#','#..*. #','#######'],
    ['########','#..#...#','#..$#..#','#.$@$.#','#..*#..#','########']
  ],
  load:function(P){
    var L=this.levels[this.level];
    this.rows=L.length; this.cols=L[0].length;
    this.cs=Math.min(48,(P.W-40)/this.cols,(P.H-160)/this.rows);
    this.ox=(P.W-this.cols*this.cs)/2; this.oy=110;
    this.walls=[]; this.boxes=[]; this.targets=[]; this.px=0; this.py=0;
    for(var r=0;r<this.rows;r++) for(var c=0;c<this.cols;c++){
      var ch=L[r][c];
      if(ch==='#') this.walls.push(r+','+c);
      if(ch==='$'||ch==='*') this.boxes.push({x:c,y:r});
      if(ch==='.'||ch==='*') this.targets.push(r+','+c);
      if(ch==='@'){ this.px=c; this.py=r; }
    }
    this.hist=[]; this.moves=0; this.won=false;
  },
  wall:function(x,y){ return this.walls.indexOf(y+','+x)>=0; },
  boxAt:function(x,y){ for(var i=0;i<this.boxes.length;i++) if(this.boxes[i].x===x&&this.boxes[i].y===y) return i; return -1; },
  tryMove:function(P,dx,dy){
    if(this.won) return;
    var nx=this.px+dx, ny=this.py+dy;
    if(this.wall(nx,ny)) return;
    var bi=this.boxAt(nx,ny);
    this.hist.push({px:this.px,py:this.py,boxes:this.boxes.map(function(b){return {x:b.x,y:b.y};})});
    if(this.hist.length>200) this.hist.shift();
    if(bi>=0){
      var bx=nx+dx, by=ny+dy;
      if(this.wall(bx,by)||this.boxAt(bx,by)>=0){ this.hist.pop(); return; }
      this.boxes[bi]={x:bx,y:by};
    }
    this.px=nx; this.py=ny; this.moves++; P.beep(440,.04);
    var done=true;
    for(var i=0;i<this.targets.length;i++){
      var t=this.targets[i].split(','), found=false;
      for(var j=0;j<this.boxes.length;j++) if(this.boxes[j].x==t[1]&&this.boxes[j].y==t[0]){found=true;break;}
      if(!found){done=false;break;}
    }
    if(done){ this.won=true; P.beep(880,.3); }
  },
  update:function(P,dt){
    if(P.pressed.left) this.tryMove(P,-1,0);
    if(P.pressed.right) this.tryMove(P,1,0);
    if(P.pressed.up) this.tryMove(P,0,-1);
    if(P.pressed.down) this.tryMove(P,0,1);
    if(P.pressed.a&&this.hist.length){ var h=this.hist.pop(); this.px=h.px; this.py=h.py; this.boxes=h.boxes; this.moves++; P.beep(300,.05); }
    if(P.pressed.b){ this.load(P); P.beep(240,.08); }
    if(this.won&&(P.pressed.start)){
      this.level=(this.level+1)%this.levels.length; this.load(P);
    }
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    var self=this;
    this.walls.forEach(function(w){
      var p=w.split(',');
      ctx.fillStyle='#1d2c4d'; ctx.fillRect(self.ox+p[1]*self.cs+1,self.oy+p[0]*self.cs+1,self.cs-2,self.cs-2);
    });
    this.targets.forEach(function(t){
      var p=t.split(',');
      ctx.fillStyle='#00e5a033'; ctx.fillRect(self.ox+p[1]*self.cs+4,self.oy+p[0]*self.cs+4,self.cs-8,self.cs-8);
      ctx.strokeStyle='#00e5a0'; ctx.strokeRect(self.ox+p[1]*self.cs+4,self.oy+p[0]*self.cs+4,self.cs-8,self.cs-8);
    });
    this.boxes.forEach(function(b){
      ctx.fillStyle='#ff8b3e'; ctx.fillRect(self.ox+b.x*self.cs+3,self.oy+b.y*self.cs+3,self.cs-6,self.cs-6);
      ctx.strokeStyle='#7a3a10'; ctx.strokeRect(self.ox+b.x*self.cs+6,self.oy+b.y*self.cs+6,self.cs-12,self.cs-12);
    });
    ctx.fillStyle='#2f7bff';
    ctx.beginPath(); ctx.arc(this.ox+this.px*this.cs+this.cs/2,this.oy+this.py*this.cs+this.cs/2,this.cs/2-5,0,7); ctx.fill();
    P.text('LEVEL '+(this.level+1)+'   MOVES '+this.moves, P.W/2, 30, 15, '#9fb3d8');
    P.text('Push crates onto targets · A=undo B=reset', P.W/2, 60, 12, '#9fb3d8');
    if(this.won) P.text('SOLVED! Press START for next level', P.W/2, 86, 15, '#00e5a0');
  }
});
