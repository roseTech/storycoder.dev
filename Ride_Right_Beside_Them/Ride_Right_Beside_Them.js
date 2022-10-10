
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
Roaming Steet`;

function len(string) {
    return 10 * string.toUpperCase().split('').filter($ => ($ >= 'A') && ($ <= 'Z')).map($ => $.charCodeAt(0) - 'A'.charCodeAt() + 1).reduce((acc, $) => acc + $);
}

const streetLength = streetNames.split('\n').map($ => [$, len($)]);
console.log(streetLength);

const everySecondLetter = streetNames.split('\n').map($ => $[1]).join('');
console.log(everySecondLetter);
