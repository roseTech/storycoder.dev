function main() {
    var elephant = 10;
    var bicycles = 10;
    var sunflower = 10;
    const initialPrice = elephant + bicycles + sunflower;
    elephant += 3;
    sunflower -= 5;
    bicycles = elephant + 2;
    const finalPrice = elephant + bicycles + sunflower;

    const gainOrLoss = finalPrice - initialPrice;

    const prefix = gainOrLoss > 0 ? 'Gained' : 'Lost';
    const result = `${prefix} ${Math.abs(gainOrLoss)}$`;

    console.log(result);
}

main();
