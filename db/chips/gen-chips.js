(function () {
  'use strict';
  var VERSION = 'jahdb-chips-1.0';
/* ✳ SIGNATURE — JAH Chip Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW chip designs in the exact archive format.
   Deterministic: same seed + version => same record. Every record is
   validated by an INDEPENDENT re-verifier before it is accepted. */

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function pad6(n) { return String(n).padStart(6, '0'); }

  var ID_PREFIX = 'JAH-CHIP-';
  var STAMP = 'Official JAH Chip Archive — generated boundlessly in archive style.';
  var P = {"cores": ["VoltCore", "HelixCore", "NovaCore", "FluxCore", "TeraCore", "PulseCore", "ZenithCore", "AxiomCore", "CobaltCore", "DriftCore", "EmberCore", "FerroCore", "IonCore", "LumenCore", "OnyxCore", "KryoCore", "GravCore", "JoltCore", "NexusCore", "PrismCore", "QuantaCore", "RidgeCore", "SlateCore", "TorqueCore", "UmbraCore", "VexCore", "WeldCore", "XenCore", "YieldCore", "ZephyrCore", "VoltForge", "HelixForge", "NovaForge", "FluxForge", "TeraForge", "PulseForge", "ZenithForge", "AxiomForge", "CobaltForge", "DriftForge", "EmberForge", "FerroForge", "IonForge", "LumenForge", "OnyxForge", "KryoForge", "GravForge", "JoltForge", "NexusForge", "PrismForge", "QuantaForge", "RidgeForge", "SlateForge", "TorqueForge", "UmbraForge", "VexForge", "WeldForge", "XenForge", "YieldForge", "ZephyrForge", "VoltMesh", "HelixMesh", "NovaMesh", "FluxMesh", "TeraMesh", "PulseMesh", "ZenithMesh", "AxiomMesh", "CobaltMesh", "DriftMesh", "EmberMesh", "FerroMesh", "IonMesh", "LumenMesh", "OnyxMesh", "KryoMesh", "GravMesh", "JoltMesh", "NexusMesh", "PrismMesh", "QuantaMesh", "RidgeMesh", "SlateMesh", "TorqueMesh", "UmbraMesh", "VexMesh", "WeldMesh", "XenMesh", "YieldMesh", "ZephyrMesh", "VoltGrid", "HelixGrid", "NovaGrid", "FluxGrid", "TeraGrid", "PulseGrid", "ZenithGrid", "AxiomGrid", "CobaltGrid", "DriftGrid", "EmberGrid", "FerroGrid", "IonGrid", "LumenGrid", "OnyxGrid", "KryoGrid", "GravGrid", "JoltGrid", "NexusGrid", "PrismGrid", "QuantaGrid", "RidgeGrid", "SlateGrid", "TorqueGrid", "UmbraGrid", "VexGrid", "WeldGrid", "XenGrid", "YieldGrid", "ZephyrGrid", "VoltWeave", "HelixWeave", "NovaWeave", "FluxWeave", "TeraWeave", "PulseWeave", "ZenithWeave", "AxiomWeave", "CobaltWeave", "DriftWeave", "EmberWeave", "FerroWeave", "IonWeave", "LumenWeave", "OnyxWeave", "KryoWeave", "GravWeave", "JoltWeave", "NexusWeave", "PrismWeave", "QuantaWeave", "RidgeWeave", "SlateWeave", "TorqueWeave", "UmbraWeave", "VexWeave", "WeldWeave", "XenWeave", "YieldWeave", "ZephyrWeave", "VoltStack", "HelixStack", "NovaStack", "FluxStack", "TeraStack", "PulseStack", "ZenithStack", "AxiomStack", "CobaltStack", "DriftStack"], "suffixes": ["X1", "X4", "M7", "S9", "P2", "Q5", "R3", "T8", "V6", "Z2", "A1", "B5", "C3", "D9", "E4"], "fams": ["CPU", "GPU", "NPU", "SOC", "MCU", "FPGA", "MEMC", "SENSOR", "PMIC", "QCTRL", "PHOT", "NEURO", "DSP", "MODEM", "SEC", "CHIPLET"], "eras": ["Historic", "Modern", "Projected"]};
  var TYPES = P.fams.slice();
  function eraPick(rnd) {
    var r = rnd();
    return r < 0.25 ? 'Historic' : (r < 0.8 ? 'Modern' : 'Projected');
  }
  function buildName(ci, si) { return 'Signature ' + P.cores[ci] + ' ' + P.suffixes[si]; }
  function generate(seed, opts, rnd) {
    opts = opts || {};
    var fam = (opts.fam && P.fams.indexOf(opts.fam) >= 0) ? opts.fam : pick(rnd, P.fams);
    var era = (opts.era && P.eras.indexOf(opts.era) >= 0) ? opts.era : eraPick(rnd);
    var ci = Math.floor(rnd() * P.cores.length), si = Math.floor(rnd() * P.suffixes.length);
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + pad6(n), n: n, kind: 'chip',
      fam: fam, era: era, seed: seed,
      name: buildName(ci, si), stamp: STAMP
    };
    rec._priv = { fam: fam, era: era, ci: ci, si: si };
    return rec;
  }
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'fam', 'era', 'name'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-CHIP-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.fam && P.fams.indexOf(rec.fam) < 0) errs.push('unknown chip family ' + rec.fam);
    if (rec.era && P.eras.indexOf(rec.era) < 0) errs.push('unknown era ' + rec.era);
    if (rec._priv) {
      var p = rec._priv;
      if (!(p.ci >= 0 && p.ci < P.cores.length && p.si >= 0 && p.si < P.suffixes.length))
        errs.push('bad name indices');
      else {
        if (buildName(p.ci, p.si) !== rec.name) errs.push('name mismatch on rebuild');
        if (p.fam !== rec.fam) errs.push('fam mismatch on rebuild');
        if (p.era !== rec.era) errs.push('era mismatch on rebuild');
      }
    } else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = a[1];
      if (nm && String(nm) === String(rec.name)) errs.push('duplicate of archived chip name: ' + rec.name);
    });
    return { ok: errs.length === 0, errors: errs };
  }
  /* cross-database: borrow a theme from another database's sample */
  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts,
          JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0])));
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }
  JAHDB.registerGenerator('chips', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
