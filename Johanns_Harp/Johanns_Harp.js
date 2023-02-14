const factor = Math.pow(2.0, 1 / 12); // 12th root

console.log(factor.toFixed(5));

// check , if result is correct in three different ways

var productMultiply = 1.0;
for (var i = 0; i < 12; i += 1) {
    productMultiply *= factor;
}

const productPow = Math.pow(factor, 12);

const productReduce = new Array(12).fill(0).reduce((acc, current) => acc * factor, 1);

console.log(productMultiply);
console.log(productPow);
console.log(productReduce);
