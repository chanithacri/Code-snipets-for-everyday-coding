import java.util.logging.ConsoleHandler;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Logging: Logging with SLF4J/Logback.
 *
 * Uses the JDK logger for a dependency-free example.
 */
public class Logging {

    private static final Logger LOGGER = Logger.getLogger(Logging.class.getName());

    static {
        ConsoleHandler handler = new ConsoleHandler();
        handler.setLevel(Level.INFO);
        LOGGER.addHandler(handler);
        LOGGER.setUseParentHandlers(false);
    }

    public static void info(String message) {
        LOGGER.log(Level.INFO, message);
    }

    public static void warn(String message) {
        LOGGER.log(Level.WARNING, message);
    }

    public static void error(String message, Throwable error) {
        LOGGER.log(Level.SEVERE, message, error);
    }
}
