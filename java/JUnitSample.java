/**
 * JUnitSample: JUnit 5 test skeleton.
 *
 * Contains simple, side-effect-free methods that are easy to exercise from
 * unit tests.
 */
public class JUnitSample {

    public static int add(int a, int b) {
        return a + b;
    }

    public static boolean isPalindrome(String value) {
        if (value == null) {
            return false;
        }
        String cleaned = value.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return new StringBuilder(cleaned).reverse().toString().equals(cleaned);
    }
}
