import java.util.Random;

public class RegularCustomer extends Customer {
    private static final int MIN_VIDEOS_PER_RENTAL = 1;
    private static final int MAX_VIDEOS_PER_RENTAL = 3;

    private static final int MIN_DAYS_TO_RENT = 3;
    private static final int MAX_DAYS_TO_RENT = 5;

    public RegularCustomer(String name) {
        super(name, MIN_VIDEOS_PER_RENTAL, MAX_VIDEOS_PER_RENTAL, MIN_DAYS_TO_RENT, MAX_DAYS_TO_RENT);
    }

    @Override
    public int getNumOfDaysToRent() {
        return Utils.getRandomNumber(MIN_DAYS_TO_RENT, MAX_DAYS_TO_RENT);
    }
}
