/**
 * Test for HttpClientExample: HTTP GET/POST
 * Tests HttpClient wrapper with a stub client.
 */
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.io.IOException;
import java.net.Authenticator;
import java.net.CookieHandler;
import java.net.ProxySelector;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpHeaders;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.Executor;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLParameters;
import javax.net.ssl.SSLSession;

class StubHttpClient extends HttpClient {
    private final HttpResponse<String> response;

    StubHttpClient(HttpResponse<String> response) {
        this.response = response;
    }

    @Override
    public <T> HttpResponse<T> send(HttpRequest request, HttpResponse.BodyHandler<T> responseBodyHandler) throws IOException, InterruptedException {
        return (HttpResponse<T>) response;
    }

    @Override
    public <T> java.util.concurrent.CompletableFuture<HttpResponse<T>> sendAsync(HttpRequest request, HttpResponse.BodyHandler<T> responseBodyHandler) {
        throw new UnsupportedOperationException();
    }

    @Override
    public <T> java.util.concurrent.CompletableFuture<HttpResponse<T>> sendAsync(HttpRequest request, HttpResponse.BodyHandler<T> responseBodyHandler, HttpResponse.PushPromiseHandler<T> pushPromiseHandler) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Optional<CookieHandler> cookieHandler() { return Optional.empty(); }
    @Override
    public Optional<Duration> connectTimeout() { return Optional.of(Duration.ofSeconds(1)); }
    @Override
    public Redirect followRedirects() { return Redirect.NORMAL; }
    @Override
    public Optional<ProxySelector> proxy() { return Optional.empty(); }
    @Override
    public Optional<Executor> executor() { return Optional.empty(); }
    @Override
    public SSLContext sslContext() { return null; }
    @Override
    public SSLParameters sslParameters() { return new SSLParameters(); }
    @Override
    public Optional<Authenticator> authenticator() { return Optional.empty(); }
    @Override
    public Version version() { return Version.HTTP_1_1; }
}

public class HttpClientExampleTest {
    @Test
    void wrapsResponseIntoRecord() throws Exception {
        HttpResponse<String> mockResponse = new HttpResponse<>() {
            @Override public int statusCode() { return 200; }
            @Override public HttpRequest request() { return HttpRequest.newBuilder(URI.create("https://example.test")).build(); }
            @Override public Optional<HttpResponse<String>> previousResponse() { return Optional.empty(); }
            @Override public HttpHeaders headers() { return HttpHeaders.of(Map.of("content-type", List.of("application/json")), (k,v) -> true); }
            @Override public String body() { return "{}"; }
            @Override public Optional<SSLSession> sslSession() { return Optional.empty(); }
            @Override public URI uri() { return URI.create("https://example.test"); }
            @Override public Version version() { return Version.HTTP_1_1; }
        };

        HttpClient client = new StubHttpClient(mockResponse);
        HttpClientExample.HttpResult result = HttpClientExample.get("https://example.test", client, Duration.ofSeconds(1), msg -> {});

        assertEquals(200, result.statusCode());
        assertEquals("{}", result.body());
        assertEquals(List.of("application/json"), result.headers().get("content-type"));
    }
}
