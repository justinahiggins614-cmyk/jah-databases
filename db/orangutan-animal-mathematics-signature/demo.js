// Demo for orangutan-animal-mathematics — executed program. Prints the orangutan's own measurements.
"use strict";
const LESSER_G = 400;
const MALE_KG = 75;
const FEMALE_KG = 40;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Orangutan mathematics");
console.log("Animal: orangutan (Pongo abelii, Pongo pygmaeus, and Pongo tapanuliensis)");
console.log("Court: the Long Call court");
console.log("Lesser unit: one slow loris = 400 g");
console.log("Adult male 75 kg = " + inUnits(MALE_KG) + " slow loris units");
console.log("Adult female 40 kg = " + inUnits(FEMALE_KG) + " slow loris units");
console.log("Human 70 kg = " + inUnits(70) + " slow loris units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
