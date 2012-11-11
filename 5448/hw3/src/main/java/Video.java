public class Video {

    private static enum Status {
        InStore,
        Rented
    }

    /**
     * Category
     * - determines the pricePerDay for a given Video
     */
    public static enum Category {
        Comedy(0.5),
        Horror(1.0),
        Drama(1.5),
        Romance(2.0),
        New_Release(2.5);

        private double pricePerDay;

        Category(double pricePerDay) {
            this.pricePerDay = pricePerDay;
        }

        public String toString() {
            return String.format("Category<%s, %.2f>", name(), pricePerDay);
        }

        public Double getPricePerDay() {
            return pricePerDay;
        }
    }

    private String name;
    private Category category;
    private Status status;

    public Video(String name, Category category) {
        this.name = name;
        this.category = category;

        this.status = Status.InStore;
    }

    public String toString() {
        return String.format("Video<%s, %s>", name, category);
    }

    //delegates to category
    public double getPricePerDay() {
        return category.getPricePerDay();
    }

    public boolean isAvailableForRental() {
        return status == Status.InStore;
    }

    public void rented() {
        status = Status.Rented;
    }

    public void returned() {
        status = Status.InStore;
    }
}
