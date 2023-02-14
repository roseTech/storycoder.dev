const xayah = 165;
const yago = 41;
const zuri = 223;

function totalTimeInMinutes(){
    const totalSeconds = xayah + yago + zuri;
    return Math.floor(totalSeconds / 60);
}

console.log(totalTimeInMinutes());
