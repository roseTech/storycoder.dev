
// calculate factor, in three different ways

const factorPow = Math.pow(2, 1 / 12); // 12th root

// https://en.wikipedia.org/wiki/Newton%27s_method
let factorNewton = 1.0; // estimation
for (let i = 0; i < 5; i += 1) {
    // xn = x - f(x) / f'(x)
    factorNewton = factorNewton - (((factorNewton ** 12) - 2) / (12 * (factorNewton ** 11)))
}

// https://en.wikipedia.org/wiki/Bisection_method
function bisection(f, a, b, maxError) {
    const c = (a + b) / 2;
    const fa = f(a);
    const fb = f(b);
    const fc = f(c);
    if (Math.abs(fc) < maxError) {
        return c;
    } else if (Math.sign(fa) != Math.sign(fc)) {
        return bisection(f, a, c, maxError);
    } else if (Math.sign(fb) != Math.sign(fc)) {
        return bisection(f, c, b, maxError);
    } else {
        console.error('No Solution');
        return c;
    }
}
const factorBisection = bisection($ => Math.pow($, 12) - 2, 0, 3, 1e-5)

console.log(factorNewton.toFixed(5));
console.log(factorPow.toFixed(5));
console.log(factorBisection.toFixed(5));

const factor = factorPow;

// check if result is correct, in three different ways

var productMultiply = 1.0;
for (var i = 0; i < 12; i += 1) {
    productMultiply *= factor;
}

const productPow = Math.pow(factor, 12);

const productReduce = new Array(12).fill(factor).reduce((accumulator, current) => accumulator * current, 1);

console.log(productMultiply);
console.log(productPow);
console.log(productReduce);
