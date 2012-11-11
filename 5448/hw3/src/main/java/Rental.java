import java.util.ArrayList;
import java.util.List;

public class Rental {

    private static enum Status {
        Active,
        Returned
    }

    int rentedOnDay;
    Customer customer;

    List<Video> videoList;

    //calculated based on customer
    int rentedForDays;

    //internal tracking
    Status status;

    public Rental(Customer customer, List<Video> videosToRent) {
        this.rentedOnDay = DateUtil.getToday();
        this.rentedForDays = customer.getNumOfDaysToRent();

        this.status = Status.Active;
        this.customer = customer;

        this.videoList = new ArrayList<Video>();
        for (Video video : videosToRent) {
            addVideo(video);
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("\t%s rented %d videos on day %d for %d nights", customer, videoList.size(), rentedOnDay, rentedForDays));
        for (Video v : videoList) {
            sb.append(String.format("\n\t\t%s", v));
        }
        sb.append(String.format("\n\tTotal Cost of Rental: $%.2f\n", getTotalCost()));
        return sb.toString();
    }


    private void addVideo(Video video) {
        video.rented();
        customer.rentVideo();
        videoList.add(video);
    }

    public void returnRental() {
        for (Video video : videoList) {
            video.returned();
            customer.returnVideo();
        }
        status = Status.Returned;
    }

    public double getTotalCost() {
        double totalCost = 0.0;
        for (Video v : videoList) {
            totalCost += (v.getPricePerDay() * rentedForDays);
        }
        return totalCost;
    }

    public boolean isDueToday() {
        return status == Status.Active && DateUtil.getToday() == (rentedForDays + rentedOnDay);
    }

    public boolean isActive() {
        return status == Status.Active;
    }

    public boolean isReturned() {
        return status == Status.Returned;
    }
}
