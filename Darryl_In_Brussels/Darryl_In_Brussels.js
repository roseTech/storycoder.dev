
const NAMES = 'Dennis, Aaron, Donald, Tim, Bjarne, Linus, Guido, James, Richard, Brian, Grace, Alan, Niklaus, Guy, Fabrice, Donald, Ken, John, Eric, Anders, Alexander, Charles, Alan, Ronald, Andrew, Leslie, Edsger, John, Keith, Barbara'.toUpperCase().split(', ');
const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

const ZERO = Object.fromEntries(ALPHABET.split('').map(char => [char, 0]));

function moreThanFive(letters) {
    return Object.values(letters).some(count => count > 5);
}

function countLetters(letters, name) {
    name.split('').forEach(char => letters[char] += 1);
    return letters;
}

function findFirstNonWritableName() {
    const letters = { ...ZERO };
    for (const nameIndex in NAMES) {
        countLetters(letters, NAMES[nameIndex]);
        if (moreThanFive(letters)) {
            return nameIndex;
        }
    }
}

function countWritableNames() {
    let letters = { ...ZERO };
    let count = 0;
    for (const name of NAMES) {
        const newLetters = countLetters({ ...letters }, name);
        if (!moreThanFive(newLetters)) {
            letters = newLetters;
            count += 1;
        }
    }
    return count;
}

console.log(findFirstNonWritableName());
console.log(countWritableNames());
