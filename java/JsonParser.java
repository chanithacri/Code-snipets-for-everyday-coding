import java.util.HashMap;
import java.util.Map;

/**
 * JsonParser: Parse JSON with Jackson/Gson.
 *
 * Provides minimal parsing for flat JSON objects without introducing external
 * dependencies. The parser expects simple string key/value pairs, making it
 * suitable for configuration-style payloads.
 */
public class JsonParser {

    public static Map<String, String> parseFlatObject(String json) {
        Map<String, String> result = new HashMap<>();
        if (json == null || json.isBlank()) {
            return result;
        }
        String trimmed = json.trim();
        if (trimmed.startsWith("{") && trimmed.endsWith("}")) {
            trimmed = trimmed.substring(1, trimmed.length() - 1);
        }
        if (trimmed.isBlank()) {
            return result;
        }
        for (String entry : trimmed.split(",")) {
            String[] parts = entry.split(":", 2);
            if (parts.length != 2) {
                continue;
            }
            String key = unquote(parts[0].trim());
            String value = unquote(parts[1].trim());
            result.put(key, value);
        }
        return result;
    }

    private static String unquote(String text) {
        if ((text.startsWith("\"") && text.endsWith("\"")) || (text.startsWith("'") && text.endsWith("'"))) {
            return text.substring(1, text.length() - 1);
        }
        return text;
    }
}
