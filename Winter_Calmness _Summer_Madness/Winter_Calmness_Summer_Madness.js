function carTraffic() {

  let peopleCounter = 0;  
  for (let i = 0; i <= 360; i++) {
    if (i % 6 === 0) {
      peopleCounter += 5;
    } else {
      peopleCounter++;
    }
  }
  /*i%6===0?peopleCounter +=5: peopleCounter ++   */
}


function busTraffic() {

    let peopleCounter = 0
    for (let i = 0; i <= 360; i += 3) {
     
        if (i % 15 === 0) {
            peopleCounter += 12
        } else {
            peopleCounter += 2
        }
    }
}




function getNumberOfWalkersInIntervalInHour(intervalLength, peopleAddition) {
  const intervals = 60 / intervalLength;
  const numberOfPeopleInInterval = intervalLength * (intervalLength + 1);
  const allPeople = numberOfPeopleInInterval * interval;

  return allPeople;
}
