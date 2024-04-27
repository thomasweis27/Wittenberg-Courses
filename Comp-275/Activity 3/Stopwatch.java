import java.util.Formatter;
import java.util.Locale;

public class Stopwatch {
    /**
     * Initializes a new stopwatch.
     */
    private long start;

    public Stopwatch() {}

    public void start() {
        start = System.currentTimeMillis();

    }

    /**
     * Returns the elapsed CPU time (in seconds) since the stopwatch was created.
     *
     * @return elapsed CPU time (in seconds) since the stopwatch was created
     */
    public  Double elapsedTime() {
        long now = System.currentTimeMillis();
        return (now - start) / 1000.0;
    }

}
