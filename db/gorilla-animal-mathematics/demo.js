// Demo for gorilla-animal-mathematics — executed program. Prints the gorilla's own measurements.
"use strict";
const LESSER_G = 60;
const MALE_KG = 170;
const FEMALE_KG = 90;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Gorilla mathematics");
console.log("Animal: gorilla (Gorilla gorilla and Gorilla beringei)");
console.log("Court: the Wooo Woo court");
console.log("Lesser unit: one mouse lemur = 60 g");
console.log("Adult male 170 kg = " + inUnits(MALE_KG) + " mouse lemur units");
console.log("Adult female 90 kg = " + inUnits(FEMALE_KG) + " mouse lemur units");
console.log("Human 70 kg = " + inUnits(70) + " mouse lemur units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
