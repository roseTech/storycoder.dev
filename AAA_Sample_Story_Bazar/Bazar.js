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
    console.log(`in the hend the bazar seller has gained ${gainOrLoss} $`);
    if (gainOrLoss < 0) {
        console.log('so his idea to change prices was not smart');
    } else {
        console.log('he was a smart dude and could fill his pouch');
    }
}

main();
