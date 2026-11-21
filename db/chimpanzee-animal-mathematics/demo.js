// Demo for chimpanzee-animal-mathematics — executed program. Prints the chimpanzee's own measurements.
"use strict";
const LESSER_G = 200;
const MALE_KG = 55;
const FEMALE_KG = 45;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Chimpanzee mathematics");
console.log("Animal: chimpanzee (Pan troglodytes)");
console.log("Court: the Pant-Hoot court");
console.log("Lesser unit: one galago (bushbaby) = 200 g");
console.log("Adult male 55 kg = " + inUnits(MALE_KG) + " galago (bushbaby) units");
console.log("Adult female 45 kg = " + inUnits(FEMALE_KG) + " galago (bushbaby) units");
console.log("Human 70 kg = " + inUnits(70) + " galago (bushbaby) units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
