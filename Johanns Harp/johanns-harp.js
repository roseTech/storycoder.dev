function main() {
    var factor = Math.pow(2, 1 / 12); // 12th root

    var product = 1.0;
    for (var i = 0; i < 12; i += 1) {
        product *= factor;
    }

    console.log(product);
}
