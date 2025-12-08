import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * CollectionsStreams: Collections and streams utilities.
 */
public class CollectionsStreams {

    public static List<Integer> filterEven(List<Integer> numbers) {
        return numbers.stream().filter(n -> n % 2 == 0).collect(Collectors.toList());
    }

    public static List<String> upperCase(List<String> values) {
        return values.stream().map(String::toUpperCase).collect(Collectors.toList());
    }

    public static int sum(List<Integer> numbers) {
        return numbers.stream().mapToInt(Integer::intValue).sum();
    }

    public static Map<String, Long> countByFirstLetter(List<String> words) {
        return words.stream()
                .collect(Collectors.groupingBy(w -> w.substring(0, 1).toLowerCase(), Collectors.counting()));
    }

    public static List<String> sortByLength(List<String> words) {
        return words.stream().sorted(Comparator.comparingInt(String::length)).collect(Collectors.toList());
    }
}
