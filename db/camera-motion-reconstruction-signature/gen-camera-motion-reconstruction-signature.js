(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["structure-from-motion", "slam", "visual-odometry", "bundle-adjustment", "photogrammetry"];
var PREFIX='JAH-CAMERA-S-';
var USE="Used in photogrammetry, robot and drone visual SLAM, augmented-reality tracking, and visual-effects set reconstruction.";
var FLD=[["method", "Method"], ["inputs", "Inputs"], ["typical_accuracy", "Typical accuracy"]];
var DEMO="# {title} - reprojection error check (python3)\nimport math\nobs={d1}\nproj={d2}\nthresh={d3}\nerr=math.dist(obs, proj)\nprint(\"reprojection error: %.3f px\" % err)\nprint(\"PASS - within budget\" if err <= thresh else \"REVIEW - exceeds budget\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["structure-from-motion", "Structure from Motion", "Recovers camera poses and a sparse 3D point cloud from overlapping photographs by detecting features, matching them across views, and running bundle adjustment.", "feature matching + bundle adjustment", "unordered photo sets", "0.1-1.0 px reprojection error", "[120.5, 80.2]", "[121.1, 79.6]", "1.0"], ["slam", "ORB-SLAM Visual SLAM", "Real-time visual SLAM that tracks ORB features frame to frame, builds a covisibility map, and closes loops to correct drift.", "ORB feature tracking + loop closure", "monocular/stereo/RGB-D video", "1-3% trajectory drift", "[320.0, 240.0]", "[320.4, 239.7]", "1.0"], ["visual-odometry", "Bundle Adjustment", "Joint non-linear refinement of camera parameters and 3D point positions that minimizes total reprojection error across all views.", "initial poses + 2D-3D correspondences", "sparse reconstruction", "sub-pixel residual", "[512.0, 384.0]", "[512.2, 383.9]", "0.5"], ["bundle-adjustment", "Visual Odometry", "Estimates camera motion incrementally from consecutive frames without building a global map, the core of frame-to-frame tracking.", "consecutive image pairs", "video stream", "0.5-2% drift per 100 m", "[640.0, 360.0]", "[640.8, 360.5]", "1.5"], ["photogrammetry", "Incremental SfM", "Builds a reconstruction by registering one image at a time, triangulating new points, and running local bundle adjustment after each addition.", "seed image pair", "ordered or unordered photos", "0.2-1.0 px residual", "[100.0, 100.0]", "[100.3, 99.8]", "1.0"], ["structure-from-motion", "Global SfM", "Estimates all camera rotations and translations jointly from the full view graph before a single global bundle adjustment, avoiding sequential drift.", "complete view graph", "large photo collections", "comparable to incremental, faster", "[200.0, 150.0]", "[200.1, 150.2]", "0.5"], ["slam", "Direct Sparse Odometry", "Tracks camera motion by directly minimizing photometric error over selected pixels, skipping explicit feature detection and descriptors.", "calibrated video", "monocular video", "~1% drift on benchmark sets", "[410.0, 300.0]", "[410.6, 300.4]", "1.0"], ["visual-odometry", "Photometric Bundle Adjustment", "Refines poses by minimizing intensity differences of reprojected patches instead of geometric reprojection error of sparse points.", "patch correspondences", "image set with exposure model", "improved in low-texture scenes", "[88.0, 64.0]", "[88.2, 63.9]", "0.5"], ["bundle-adjustment", "Multi-View Stereo", "Densifies a sparse SfM result into a dense depth map or point cloud by matching pixels across many calibrated views.", "calibrated cameras + sparse points", "overlapping views", "mm-to-cm depth noise", "[720.0, 540.0]", "[720.5, 540.3]", "1.0"], ["photogrammetry", "Feature-based Tracking", "Maintains 2D feature tracks across frames with KLT or descriptor matching, the measurement front-end for most reconstruction pipelines.", "image sequence", "video frames", "sub-pixel track accuracy", "[256.0, 192.0]", "[256.2, 191.8]", "0.5"], ["structure-from-motion", "IMU-Visual Fusion", "Fuses inertial measurements with visual tracking in a tightly coupled estimator, giving metric scale and robustness during fast motion.", "camera + IMU stream", "visual-inertial sensor", "cm-level local accuracy", "[128.0, 96.0]", "[128.4, 96.1]", "1.0"], ["slam", "Rolling-Shutter Compensation", "Models the row-by-row exposure timing of rolling-shutter cameras so motion during readout does not corrupt pose estimates.", "rolling-shutter video + readout time", "CMOS camera footage", "removes systematic skew", "[900.0, 600.0]", "[900.3, 600.2]", "0.8"], ["visual-odometry", "Loop Closure", "Detects when the camera revisits a mapped place and distributes the accumulated drift with a pose-graph optimization.", "place-recognition descriptors", "long trajectories", "eliminates large-scale drift", "[50.0, 50.0]", "[50.5, 50.4]", "1.0"], ["bundle-adjustment", "Keyframe Selection", "Keeps only frames with enough new visual information as keyframes, bounding map growth while preserving reconstruction quality.", "frame stream + parallax test", "video/SLAM input", "10-30% of frames kept", "[1024.0, 768.0]", "[1024.2, 767.9]", "0.6"], ["photogrammetry", "Epipolar Geometry Estimation", "Recovers the fundamental or essential matrix between image pairs with RANSAC, establishing the geometric relation before triangulation.", "matched feature pairs", "image pairs", "inlier ratio 60-95%", "[300.0, 200.0]", "[300.4, 200.1]", "1.0"], ["structure-from-motion", "Dense Reconstruction", "Estimates depth for nearly every pixel using plane-sweep or learned stereo, producing watertight surfaces from video.", "calibrated video", "multi-view footage", "dense, cm-scale", "[640.0, 480.0]", "[640.3, 480.2]", "0.8"], ["slam", "NeRF Pose Refinement", "Jointly optimizes camera poses while training a neural radiance field, recovering accurate trajectories from casually captured video.", "image set + initial poses", "unposed photo collections", "comparable to COLMAP", "[400.0, 300.0]", "[400.2, 299.9]", "0.7"], ["visual-odometry", "Gaussian Splatting Tracking", "Tracks camera pose against a 3D Gaussian splat map by differentiable rendering, enabling real-time relocalization in prebuilt scenes.", "splat map + live frame", "mapped environment", "real-time, mm-cm", "[800.0, 450.0]", "[800.1, 450.1]", "0.5"], ["bundle-adjustment", "Event-Camera Odometry", "Estimates motion from asynchronous event streams, working in high-speed and high-dynamic-range conditions where frames blur.", "event stream", "event camera", "microsecond temporal resolution", "[160.0, 120.0]", "[160.3, 120.2]", "0.9"], ["photogrammetry", "GPS-Prior SfM", "Constrains structure-from-motion with GPS/RTK priors on camera positions, giving georeferenced reconstructions with true metric scale.", "photos + GPS tags", "aerial/survey imagery", "cm-level with RTK", "[1920.0, 1080.0]", "[1920.4, 1080.3]", "1.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-camera-motion-reconstruction-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('camera-motion-reconstruction-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
