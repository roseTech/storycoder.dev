const iterations = 10;
const p = 7;
const sum = new Array(iterations).fill(0).map((_, i) => (i + 1) * p).reduce((acc, value) => acc + value);
console.log(sum);
