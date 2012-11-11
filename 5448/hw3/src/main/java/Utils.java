import java.util.Random;

public class Utils {

    public static int getRandomNumber(int min, int max) {
        if (min > max) {
            throw new IllegalArgumentException("Min must be greater than Max");
        }

        return min + new Random().nextInt(max - min + 1);
    }
}
