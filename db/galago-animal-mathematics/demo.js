// Demo for galago-animal-mathematics — executed program. Prints the galago's own measurements.
"use strict";
const LESSER_G = 60;
const MALE_KG = 0.25;
const FEMALE_KG = 0.22;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Galago mathematics");
console.log("Animal: galago (Galago senegalensis)");
console.log("Court: the Cry court");
console.log("Lesser unit: one mouse lemur = 60 g");
console.log("Adult male 0.25 kg = " + inUnits(MALE_KG) + " mouse lemur units");
console.log("Adult female 0.22 kg = " + inUnits(FEMALE_KG) + " mouse lemur units");
console.log("Human 70 kg = " + inUnits(70) + " mouse lemur units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
