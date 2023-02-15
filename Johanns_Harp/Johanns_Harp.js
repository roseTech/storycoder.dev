
// calculate factor, in different ways

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

// https://en.wikipedia.org/wiki/Secant_method
function secant(f, x0, x1, maxError) {
    for (let i = 0; i < 100; i += 1) {
        const fx1 = f(x1);
        const xn = x1 - f(x1) / ((f(x1) - f(x0)) / (x1 - x0));
        if (Math.abs(fx1) < maxError) {
            return xn;
        }
        [x0, x1] = [x1, xn];
    }
}

// https://en.wikipedia.org/wiki/Newton%27s_method
function newton(f, f1, initialApproximation, maxError) {
    let x = initialApproximation;
    while (true) {
        // xn = x - f(x) / f'(x)
        const fx = f(x);
        if (Math.abs(fx) < maxError) {
            break;
        }
        const f1x = f1(x);
        x -= fx / f1x;
    }
    return x;
}

const factorPow = Math.pow(2, 1 / 12); // 12th root
const factorBisection = bisection($ => Math.pow($, 12) - 2, 0, 3, 1e-5);
const factorSecant = secant($ => Math.pow($, 12) - 2, 1, 3, 1e-5);
const factorNewton = newton($ => Math.pow($, 12) - 2, $ => 12 * ($ ** 11), 1, 1e-5);


console.log(factorPow.toFixed(5));
console.log(factorBisection.toFixed(5));
console.log(factorSecant.toFixed(5));
console.log(factorNewton.toFixed(5));

const factor = factorPow;

// check if result is correct, in different ways

var productMultiply = 1.0;
for (var i = 0; i < 12; i += 1) {
    productMultiply *= factor;
}

const productPow = Math.pow(factor, 12);

const productReduce = new Array(12).fill(factor).reduce((accumulator, current) => accumulator * current, 1);

console.log(productMultiply);
console.log(productPow);
console.log(productReduce);
