main() {
  int elephant = 10;
  int bicycles = 10;
  int sunflower = 10;
  int initialPrice = elephant + bicycles + sunflower;
  elephant += 3;
  sunflower -= 5;
  bicycles = elephant + 2;
  int finalPrice = elephant + bicycles + sunflower;

  int gainOrLoss = finalPrice - initialPrice;
  print('in the end the bazar seller has gained $gainOrLoss \$');
  print('so his idea to change prices was smart');
}
