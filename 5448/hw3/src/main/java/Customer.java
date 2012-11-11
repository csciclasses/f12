import java.util.List;

public abstract class Customer {
    private String name;

    private int minVideosPerRental;
    private int maxVideosPerRental;

    private int minRentalDays;
    private int maxRentalDays;

    //tracks the current number of videos rented by the Customer
    private int rentedVideosCount;

    private static final int MAX_VIDEOS_PER_CUSTOMER = 3;

    protected Customer(String name, int minVideosPerRental, int maxVideosPerRental, int minRentalDays, int maxRentalDays) {
        this.name = name;
        this.minVideosPerRental = minVideosPerRental;
        this.maxVideosPerRental = maxVideosPerRental;
        this.minRentalDays = minRentalDays;
        this.maxRentalDays = maxRentalDays;

        this.rentedVideosCount = 0;
    }

    public String toString() {
        return String.format("%s<%s>", getClass().getName(), name);
    }

    public int getNumOfDaysToRent() {
        return Utils.getRandomNumber(minRentalDays, maxRentalDays);
    }

    public void rentVideo() {
        rentedVideosCount += 1;
    }

    public void returnVideo() {
        this.rentedVideosCount -= 1;
    }

    public boolean canCreateRental(int numOfVideosAvailableForRental) {
        return rentedVideosCount < MAX_VIDEOS_PER_CUSTOMER &&
                minVideosPerRental <= numOfVideosAvailableForRental &&
                (rentedVideosCount + minVideosPerRental) <= MAX_VIDEOS_PER_CUSTOMER;
    }

    private int getNumOfVideosToRent(int numOfVideosAvailableForRental) {
        if (!canCreateRental(numOfVideosAvailableForRental)) {
            throw new RuntimeException("Invalid State. Cannot Create a Rental but wants to know how many videos to rent.");
        }

        int numOfVideosToRent = Math.min(numOfVideosAvailableForRental, maxVideosPerRental);
        return Utils.getRandomNumber(minVideosPerRental, numOfVideosToRent);
    }

    public List<Video> getVideosToRent(Store store) {
        int numOfVideosAvailableForRental = store.getNumOfVideosAvailableForRental();
        int numOfVideosToRent = getNumOfVideosToRent(numOfVideosAvailableForRental);

        List<Video> videosAvailableForRental = store.getVideosAvailableForRental();
        return videosAvailableForRental.subList(0, numOfVideosToRent);
    }
}
