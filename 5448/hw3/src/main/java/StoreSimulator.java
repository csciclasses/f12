import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class StoreSimulator {

    static List<Customer> initCustomers() {
        List<Customer> customerList = new ArrayList<Customer>();

        customerList.add(new BreezyCustomer("Aaron"));
        customerList.add(new BreezyCustomer("Becky"));
        customerList.add(new BreezyCustomer("Chuck"));

        customerList.add(new RegularCustomer("Doug"));
        customerList.add(new RegularCustomer("Eric"));
        customerList.add(new RegularCustomer("Faye"));
        customerList.add(new RegularCustomer("Garth"));

        customerList.add(new HoarderCustomer("Han"));
        customerList.add(new HoarderCustomer("Ira"));
        customerList.add(new HoarderCustomer("Jackie"));

        Collections.shuffle(customerList);

        System.out.println("Customers:");
        for (Customer c : customerList) {
            System.out.println("\t" + c);
        }

        return customerList;
    }

    static List<Video> initVideos() {
        List<Video> videoList = new ArrayList<Video>();

        videoList.add(new Video("Moonrise Kingdom", Video.Category.Comedy));
        videoList.add(new Video("Rock Of Ages", Video.Category.Comedy));
        videoList.add(new Video("Hotel Transylvania", Video.Category.Comedy));
        videoList.add(new Video("Pitch Perfect", Video.Category.Comedy));

        videoList.add(new Video("ParaNorman", Video.Category.Horror));
        videoList.add(new Video("Frankenweenie", Video.Category.Horror));
        videoList.add(new Video("Alien", Video.Category.Horror));
        videoList.add(new Video("The Shining", Video.Category.Horror));

        videoList.add(new Video("Shawshank Redemption", Video.Category.Drama));
        videoList.add(new Video("Cosmopolis", Video.Category.Drama));
        videoList.add(new Video("Lawless", Video.Category.Drama));
        videoList.add(new Video("The Master", Video.Category.Drama));

        videoList.add(new Video("The Notebook", Video.Category.Romance));
        videoList.add(new Video("Bridesmaids", Video.Category.Romance));
        videoList.add(new Video("Twilight", Video.Category.Romance));
        videoList.add(new Video("Midnight In Paris", Video.Category.Romance));

        videoList.add(new Video("Looper", Video.Category.New_Release));
        videoList.add(new Video("Dredd", Video.Category.New_Release));
        videoList.add(new Video("End Of Watch", Video.Category.New_Release));
        videoList.add(new Video("Too Many Movies", Video.Category.New_Release));

        Collections.shuffle(videoList);

        System.out.println();
        System.out.println("Videos:");
        for (Video v : videoList) {
            System.out.println("\t" + v);
        }

        return videoList;
    }

    public static void main(String[] args) {
        List<Customer> customerList = initCustomers();
        List<Video> videoList = initVideos();

        Store s = new Store(customerList, videoList);

        for (int day = 1; day <= 35; day++) {
            simulateDay(s);
            DateUtil.incrementDay();
        }

        printSummary(s);
    }

    public static void simulateDay(Store store) {
        //first thing in the day, the store processes returns
        System.out.println("\nProcess Returns -  " + DateUtil.getToday());
        store.processReturns();

        List<Customer> storeCustomers = store.getCustomers();

        //pick number of customers to visit the store
        int customersToVisitStore = Utils.getRandomNumber(5, storeCustomers.size());

        System.out.println("Simulate Day -  " + DateUtil.getToday());
        //while the store has videos to rent out.
        while (customersToVisitStore > 0 && store.getNumOfVideosAvailableForRental() > 0) {
            //pick a customer at random
            int randIndex = Utils.getRandomNumber(0, storeCustomers.size() - 1);
            Customer customer = storeCustomers.get(randIndex);

            //visit the store - if the customer can create a rental visit the store
            if (customer.canCreateRental(store.getNumOfVideosAvailableForRental())) {
                store.customerVisit(customer);
            }

            //decrement number of customers to visit store
            customersToVisitStore -= 1;
        }
    }

    public static void printSummary(Store store) {
        System.out.println("\n============== REQUIRED OUTPUT ===============");

        System.out.println("# of Videos in Store: " + store.getNumOfVideosAvailableForRental());
        for (Video v : store.getVideosAvailableForRental()) {
            System.out.println("\t" + v);
        }

        System.out.println("\nTotal Revenue: " + store.getTotalRevenue());

        List<Rental> tempRentalList;

        tempRentalList = store.getCompletedRentals();
        System.out.println("\nCompleted Rentals: " + tempRentalList.size());
        for (Rental r : tempRentalList) {
            System.out.println(r);
        }

        tempRentalList = store.getActiveRentals();
        System.out.println("\nActive Rentals: " + tempRentalList.size());
        for (Rental r : tempRentalList) {
            System.out.println(r);
        }
    }

}
