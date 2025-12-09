/**
 * Thin wrapper around java.net.http.HttpClient for straightforward GET and POST requests.
 */

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.function.Consumer;

/**
 * Lightweight wrapper around {@link HttpClient} for GET and POST requests.
 *
 * <p>The helpers return a {@link HttpResult} record which keeps data transport
 * friendly for further processing. Logging is optional and defaults to a
 * no-op consumer.</p>
 *
 * <h2>Usage example</h2>
 * <pre>{@code
 * HttpClientExample.HttpResult result = HttpClientExample.get("https://example.test/api");
 * System.out.println(result.statusCode());
 * System.out.println(result.body());
 * }
 * </pre>
 */
public final class HttpClientExample {
    private static final Consumer<String> NO_OP_LOGGER = message -> { };
    private static final HttpClient DEFAULT_CLIENT = HttpClient.newBuilder()
        .connectTimeout(Duration.ofSeconds(10))
        .version(HttpClient.Version.HTTP_2)
        .build();

    private HttpClientExample() {
    }

    public static HttpResult get(String url) throws HttpRequestException {
        return get(url, DEFAULT_CLIENT, Duration.ofSeconds(10), NO_OP_LOGGER);
    }

    public static HttpResult get(String url, HttpClient client, Duration timeout, Consumer<String> logger)
            throws HttpRequestException {
        Objects.requireNonNull(url, "url");
        Objects.requireNonNull(client, "client");
        Objects.requireNonNull(timeout, "timeout");
        Objects.requireNonNull(logger, "logger");
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
            .GET()
            .timeout(timeout)
            .header("Accept", "application/json")
            .build();
        return send(request, client, logger);
    }

    public static HttpResult post(String url, String body) throws HttpRequestException {
        return post(url, body, "application/json", StandardCharsets.UTF_8, DEFAULT_CLIENT,
            Duration.ofSeconds(10), NO_OP_LOGGER);
    }

    public static HttpResult post(String url, String body, String contentType, Charset charset,
                                  HttpClient client, Duration timeout, Consumer<String> logger)
            throws HttpRequestException {
        Objects.requireNonNull(url, "url");
        Objects.requireNonNull(body, "body");
        Objects.requireNonNull(contentType, "contentType");
        Objects.requireNonNull(charset, "charset");
        Objects.requireNonNull(client, "client");
        Objects.requireNonNull(timeout, "timeout");
        Objects.requireNonNull(logger, "logger");
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
            .timeout(timeout)
            .header("Content-Type", contentType)
            .POST(HttpRequest.BodyPublishers.ofString(body, charset))
            .build();
        return send(request, client, logger);
    }

    private static HttpResult send(HttpRequest request, HttpClient client, Consumer<String> logger)
            throws HttpRequestException {
        try {
            logger.accept("http: sending " + request.method() + " " + request.uri());
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            logger.accept("http: received status " + response.statusCode());
            return new HttpResult(response.statusCode(), response.body(), response.headers().map());
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
            logger.accept("http: interrupted " + ex.getMessage());
            throw new HttpRequestException("HTTP request interrupted", ex);
        } catch (IOException ex) {
            logger.accept("http: I/O error " + ex.getMessage());
            throw new HttpRequestException("HTTP request failed", ex);
        }
    }

    /** Thrown when an HTTP request cannot be completed. */
    public static final class HttpRequestException extends Exception {
        public HttpRequestException(String message, Throwable cause) {
            super(message, cause);
        }

        public HttpRequestException(String message) {
            super(message);
        }
    }

    /** Record representing the minimal response payload. */
    public record HttpResult(int statusCode, String body, Map<String, List<String>> headers) {
        public HttpResult {
            Objects.requireNonNull(body, "body");
            Objects.requireNonNull(headers, "headers");
        }

        public List<String> header(String name) {
            return headers.getOrDefault(name, List.of());
        }
    }
}
