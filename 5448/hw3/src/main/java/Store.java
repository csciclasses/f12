import java.util.ArrayList;
import java.util.List;

public class Store {

    private List<Customer> allCustomers;
    private List<Video> allVideos;

    //tracking
    private List<Rental> allRentals;

    public Store(List<Customer> allCustomers, List<Video> allVideos) {
        this.allCustomers = allCustomers;
        this.allVideos = allVideos;

        this.allRentals = new ArrayList<Rental>();
    }

    public void processReturns() {
        List<Rental> activeRentals = getActiveRentals();
        for (Rental rental : activeRentals) {
            if (rental.isDueToday()) {
                rental.returnRental();
                System.out.println(rental);
            }
        }
    }

    public void customerVisit(Customer customer) {
        //determine if customer can rent
        if (!customer.canCreateRental(getNumOfVideosAvailableForRental())) {
            throw new RuntimeException("Customer Visited and did not create a rental.");
        }

        //choose videos and create rental
        List<Video> videosToRent = customer.getVideosToRent(this);
        Rental rental = new Rental(customer, videosToRent);

        //track rental
        allRentals.add(rental);

        System.out.println(rental);
    }

    public List<Customer> getCustomers() {
        return allCustomers;
    }

    public double getTotalRevenue() {
        double totalRevenue = 0;
        for (Rental rental : allRentals) {
            totalRevenue += rental.getTotalCost();
        }

        return totalRevenue;
    }

    public List<Video> getVideosAvailableForRental() {
        List<Video> inStoreVideos = new ArrayList<Video>();
        for (Video v : allVideos) {
            if (v.isAvailableForRental()) {
                inStoreVideos.add(v);
            }
        }
        return inStoreVideos;
    }

    public List<Rental> getActiveRentals() {
        List<Rental> activeRentals = new ArrayList<Rental>();
        for (Rental rental : allRentals) {
            if (rental.isActive()) {
                activeRentals.add(rental);
            }
        }
        return activeRentals;
    }

    public int getNumOfVideosAvailableForRental() {
        return getVideosAvailableForRental().size();
    }

    public List<Rental> getCompletedRentals() {
        List<Rental> completedRentals = new ArrayList<Rental>();
        for (Rental rental : allRentals) {
            if (rental.isReturned()) {
                completedRentals.add(rental);
            }
        }
        return completedRentals;
    }
}
