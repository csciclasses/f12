public class DateUtil {
    private DateUtil() {
    }

    private static int today = 1;

    public static int getToday() {
        return today;
    }

    public static void incrementDay() {
        today += 1;
    }
}
