
function areaEllipse(a, b) {
    return a * b * Math.PI;
}

function areaRectangle(width, length) {
    return width * length;
}

function areaHexagon(side) {
    return (3.0 * Math.sqrt(3.0) * Math.pow(side, 2.0)) / 2.0;
}

function areaCircle(radius) {
    return areaEllipse(radius, radius);
}

const fabricSquareMeter = areaEllipse(1.1, 2.4) + areaRectangle(2.1, 0.8) + areaHexagon(0.9) + areaCircle(0.5);

console.log(Math.ceil(fabricSquareMeter));
