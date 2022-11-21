function carTraffic() {
  let peopleInCar = 0;

  for (let i = 1; i <= 360; i++) {
    if (i % 6 === 0) {
      peopleInCar += 5;
    } else {
      peopleInCar++;
    }
  }

  console.log('people in car', peopleInCar);
  return peopleInCar
}

function busTraffic() {
  let peopleInBus = 0;

  for (let i = 0; i <= 360; i += 3) {
    if (i % 15 === 0 && i != 0) {
      peopleInBus += 12;
    } else if (i != 0) {
      peopleInBus += 2;
    }
  }

  console.log('people in bus', peopleInBus);
  return peopleInBus
}

function getNumberOfWalkersInIntervalInHour(intervalLength, peopleAddition) {
  let allPeopleOnStreet = 0;
  const intervals = 360 / intervalLength;
  //360 represents the 360 minutes between noon and 6pm
  for (let interval = 1; interval <= intervals; interval++) {
    for (let minute = 1; minute <= intervalLength; minute++) {
      allPeopleOnStreet += minute;
    }
  }

  console.log('people on street', allPeopleOnStreet);
  return allPeopleOnStreet;
}

const allPeople = getNumberOfWalkersInIntervalInHour(10, 1) + busTraffic() + carTraffic();
console.log('all people', allPeople);
