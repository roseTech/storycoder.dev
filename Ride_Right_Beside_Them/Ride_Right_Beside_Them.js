
const streetNames = `Egame Street
Branch Road
DartLang Lane
Azerty Avenue
Pixel Way
Less than or equal Street
OpenSourcePath
Readme Road
Frame Work Way
Element Lane
Tab Street
Night Mode Ave
Julia Lang Lane
Stack Overflowed Way
Roaming Street`;

function len(string) {
    return 10 * string.toUpperCase().split('').filter($ => ($ >= 'A') && ($ <= 'Z')).map($ => $.charCodeAt(0) - 'A'.charCodeAt() + 1).reduce((acc, $) => acc + $);
}

const streetLengths = streetNames.split('\n').map($ => [$, len($)]);
console.log(streetLengths);

const totalLength = streetLengths.map($ => $[1]).reduce((accumulator, current) => accumulator + current);
console.log(totalLength);

const everySecondLetter = streetNames.split('\n').map($ => $[1]).join('');
console.log(everySecondLetter);
