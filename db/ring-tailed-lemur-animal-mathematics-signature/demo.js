// Demo for ring-tailed-lemur-animal-mathematics — executed program. Prints the ring-tailed lemur's own measurements.
"use strict";
const LESSER_G = 60;
const MALE_KG = 2.5;
const FEMALE_KG = 2.2;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Ring-Tailed Lemur mathematics");
console.log("Animal: ring-tailed lemur (Lemur catta)");
console.log("Court: the Squeak court");
console.log("Lesser unit: one mouse lemur = 60 g");
console.log("Adult male 2.5 kg = " + inUnits(MALE_KG) + " mouse lemur units");
console.log("Adult female 2.2 kg = " + inUnits(FEMALE_KG) + " mouse lemur units");
console.log("Human 70 kg = " + inUnits(70) + " mouse lemur units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
