public class HoarderCustomer extends Customer {

    private static final int VIDEOS_PER_RENTAL = 3;

    private static final int RENTAL_DAYS = 7;

    public HoarderCustomer(String name) {
        super(name, VIDEOS_PER_RENTAL, VIDEOS_PER_RENTAL, RENTAL_DAYS, RENTAL_DAYS);
    }
}

