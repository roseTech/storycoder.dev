
const ITEMS = [
    { name: 'Weapon', weight: 4, value: 0.9 },
    { name: 'CCTV', weight: 5, value: 0.7 },
    { name: 'Clothing', weight: 6, value: 0.8 },
    { name: 'Laptop', weight: 3, value: 0.6 },
    { name: 'Parrot', weight: 2, value: 0.6 },
];

const MAX_WEIGHT = 12.0;

// combinations([1, 2, 3], 2) => [[1, 2], [1, 3], [2, 3]]
function combinations(array, length) {
    return length === 0 ? [[]] : array.flatMap((element, index) => combinations(array.slice(index + 1), length - 1).map($ => [element, ...$]));
}

// combinationsAll([1, 2, 3]) => [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
function combinationsAll(array) {
    return array.flatMap((_, index) => combinations(array, index + 1));
}

function optimize(array, callable) {
    const results = array.map(callable);
    return array[results.indexOf(Math.max(...results))];
}

function f(items) {
    const sumWeight = items.reduce((sum, $) => sum + $.weight, 0);
    const sumValue = items.reduce((sum, $) => sum + $.value, 0);
    return sumWeight <= MAX_WEIGHT ? sumValue : 0;
}

const best = optimize(combinationsAll(ITEMS), f);

console.log(best.sort((a, b) => a.weight >= b.weight ? -1 : 1).map($ => $.name).join(''));
