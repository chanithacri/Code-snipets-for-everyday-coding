import java.util.List;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * Lambdas: Lambda expressions and functional interfaces.
 */
public class Lambdas {

    @FunctionalInterface
    public interface Transformer<T, R> {
        R apply(T input);
    }

    public static <T> List<T> filter(List<T> items, Predicate<T> predicate) {
        return items.stream().filter(predicate).collect(Collectors.toList());
    }

    public static <T, R> List<R> map(List<T> items, Function<T, R> mapper) {
        return items.stream().map(mapper).collect(Collectors.toList());
    }

    public static Transformer<String, String> prefixer(String prefix) {
        return value -> prefix + value;
    }
}
