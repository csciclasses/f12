public class BreezyCustomer extends Customer {

    private static final int MIN_VIDEOS_PER_RENTAL = 1;
    private static final int MAX_VIDEOS_PER_RENTAL = 2;

    private static final int MIN_RENTAL_DAYS = 1;
    private static final int MAX_RENTAL_DAYS = 2;

    public BreezyCustomer(String name) {
        super(name, MIN_VIDEOS_PER_RENTAL, MAX_VIDEOS_PER_RENTAL, MIN_RENTAL_DAYS, MAX_RENTAL_DAYS);
    }
}
