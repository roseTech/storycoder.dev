
const peaks = [1335, 1439, 987, 312, 871, 1461, 1171, 654, 123];

let steepnessMax = 0;
let indexMax;

for (let i = 0; i < (peaks.length - 1); i++) {
    const steepness = Math.abs(peaks[i] - peaks[i + 1]);
    if (steepness > steepnessMax) {
        steepnessMax = steepness;
        indexMax = i;
    }
}

console.log(indexMax + 1);
console.log(steepnessMax);