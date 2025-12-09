/**
 * Grab bag of Java utilities covering properties, HTTP requests, collections, and JSON handling.
 */

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import com.google.gson.Gson;

public class UtilityHelpers {

    /**
     * Load configuration from a .properties file.
     */
    public static Properties loadProperties(String filePath) throws IOException {
        Properties props = new Properties();
        try (InputStream input = new FileInputStream(filePath)) {
            props.load(input);
        }
        return props;
    }

    /**
     * Perform a simple HTTP request (GET or POST) and return the response body as a string.
     */
    public static String httpRequest(String urlStr, String method, String body) throws IOException {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod(method);
        if ("POST".equalsIgnoreCase(method) && body != null) {
            conn.setDoOutput(true);
            try (OutputStream os = conn.getOutputStream()) {
                os.write(body.getBytes());
            }
        }
        conn.connect();
        try (InputStream is = conn.getInputStream();
             BufferedReader reader = new BufferedReader(new InputStreamReader(is))) {
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                sb.append(line);
            }
            return sb.toString();
        }
    }

    /**
     * Filter a list using the given predicate.
     */
    public static <T> List<T> filter(List<T> list, Predicate<T> predicate) {
        return list.stream().filter(predicate).collect(Collectors.toList());
    }

    /**
     * Map a list to another list using the given function.
     */
    public static <T,R> List<R> map(List<T> list, Function<T,R> mapper) {
        return list.stream().map(mapper).collect(Collectors.toList());
    }

    /**
     * Remove duplicate elements from a list while preserving order.
     */
    public static <T> List<T> deduplicate(List<T> list) {
        return new ArrayList<>(new LinkedHashSet<>(list));
    }

    /**
     * Group elements of a list by a key extractor function.
     */
    public static <T,K> Map<K,List<T>> groupBy(List<T> list, Function<T,K> keyExtractor) {
        return list.stream().collect(Collectors.groupingBy(keyExtractor));
    }

    /**
     * Generate a random UUID as a string.
     */
    public static String generateUUID() {
        return UUID.randomUUID().toString();
    }

    /**
     * Generate a random alphanumeric string of the given length.
     */
    public static String randomString(int length) {
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        StringBuilder sb = new StringBuilder();
        Random rnd = new Random();
        for (int i = 0; i < length; i++) {
            sb.append(chars.charAt(rnd.nextInt(chars.length())));
        }
        return sb.toString();
    }

    /**
     * Serialize an object to JSON using Gson.
     */
    public static String toJson(Object obj) {
        Gson gson = new Gson();
        return gson.toJson(obj);
    }

    /**
     * Deserialize a JSON string into an object of the specified class using Gson.
     */
    public static <T> T fromJson(String json, Class<T> clazz) {
        Gson gson = new Gson();
        return gson.fromJson(json, clazz);
    }
}
