import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Properties;

/**
 * PropertiesReader: Read properties/config files.
 */
public class PropertiesReader {

    public static Properties fromPath(Path path) throws IOException {
        try (InputStream in = Files.newInputStream(path)) {
            Properties properties = new Properties();
            properties.load(in);
            return properties;
        }
    }

    public static String getOrDefault(Properties properties, String key, String defaultValue) {
        return properties.getProperty(key, defaultValue);
    }
}
