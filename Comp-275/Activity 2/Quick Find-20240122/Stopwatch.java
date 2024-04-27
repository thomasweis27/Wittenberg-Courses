import java.util.Formatter;
import java.util.Locale;

public class Stopwatch {
    /**
     * Initializes a new stopwatch.
     */
    private static long start;



    public Stopwatch() {
    }

    public static void start() {
        start = System.currentTimeMillis();

    }

    /**
     * Returns the elapsed CPU time (in seconds) since the stopwatch was created.
     *
     * @return elapsed CPU time (in seconds) since the stopwatch was created
     */
    public static Double elapsedTime() {
        long now = System.currentTimeMillis();
        return (now - start) / 1000.0;
    }

}
