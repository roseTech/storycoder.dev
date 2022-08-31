function main() {
    const factor = Math.pow(2.0, 1.0 / 12.0); // 12th root

    var product = 1.0;
    for (var i = 0; i < 12; i += 1) {
        product *= factor;
    }

    console.log(product);
}
