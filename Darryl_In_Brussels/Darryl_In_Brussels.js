
const NAMES = 'Dennis, Aaron, Donald, Tim, Bjarne, Linus, Guido, James, Richard, Brian, Grace, Alan, Niklaus, Guy, Fabrice, Donald, Ken, John, Eric, Anders, Alexander, Charles, Alan, Ronald, Andrew, Leslie, Edsger, John, Keith, Barbara'.toUpperCase().split(', ');

function moreThanFive(letters) {
    return Object.values(letters).some(count => count > 5);
}

function countLetters(letters, name) {
    const result = { ...letters };
    name.split('').forEach(char => result[char] = (result[char] || 0) + 1);
    return result;
}

function findFirstNonWritableName() {
    let letters = {};
    return NAMES.findIndex(name => {
        letters = countLetters(letters, name);
        return moreThanFive(letters);
    });
}

function countWritableNames() {
    let letters = {};
    return NAMES.reduce((count, name) => {
        const newLetters = countLetters(letters, name);
        if (!moreThanFive(newLetters)) {
            letters = newLetters;
            count += 1;
        }
        return count;
    }, 0);
}

console.log(findFirstNonWritableName());
console.log(countWritableNames());
