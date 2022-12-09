public class Bazar {

    public static void main(String[] args) {
        int elephant = 10;
        int sunflower = 10;
        int bicycle = 10;
        int initialPrice = elephant + sunflower + bicycle;

        elephant += 3;
        sunflower -= 5;
        bicycle = elephant + 2;
        int finalPrice = elephant + sunflower + bicycle;

        int gainOrLoss = finalPrice - initialPrice;
        String result = gainOrLoss > 0 ? "gained " : "lost ";

        System.out.println("In the end, the bazar seller has " + result + Math.abs(gainOrLoss) + "$");
    }
}
