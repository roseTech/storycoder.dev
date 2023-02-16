
const pieces = { big: 19, medium: 11, small: 5 };
const isSatisfied = explorer => Object.values(explorer).every($ => $ >= 117);
const explorers = new Array(8).fill().map($ => ({ big: 0, medium: 0, small: 0 }));

let explorerToFeed = 0;
while (!explorers.every(isSatisfied)) {
    for (const size in pieces) {
        for (let i = 0; i < pieces[size]; i += 1) {
            explorers[explorerToFeed % explorers.length][size] += 1;
            explorerToFeed += 1;
        }
    }
}

console.log(explorers);
console.log(Object.keys(pieces).map(size => explorers.reduce((acc, current) => acc + current[size], 0)));
