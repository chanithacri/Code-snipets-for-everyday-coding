/**
 * EnumsWithMethods: Enums with fields and behavior.
 *
 * The {@link Priority} enum demonstrates how to attach metadata and helper
 * methods directly on an enum. Utility methods in this class showcase common
 * lookups and formatting.
 */
public class EnumsWithMethods {

    public enum Priority {
        LOW(1, "Low"),
        MEDIUM(2, "Medium"),
        HIGH(3, "High");

        private final int level;
        private final String label;

        Priority(int level, String label) {
            this.level = level;
            this.label = label;
        }

        public int getLevel() {
            return level;
        }

        public String getLabel() {
            return label;
        }

        /**
         * Convert a numeric level to the corresponding priority.
         */
        public static Priority fromLevel(int level) {
            for (Priority value : values()) {
                if (value.level == level) {
                    return value;
                }
            }
            throw new IllegalArgumentException("Unknown priority level: " + level);
        }
    }

    /**
     * Build a human-friendly description of the given priority.
     */
    public static String describe(Priority priority) {
        return String.format("Priority %s (level %d)", priority.getLabel(), priority.getLevel());
    }

    /**
     * Promote a priority by one level without exceeding HIGH.
     */
    public static Priority promote(Priority priority) {
        return switch (priority) {
            case LOW -> Priority.MEDIUM;
            case MEDIUM -> Priority.HIGH;
            case HIGH -> Priority.HIGH;
        };
    }
}
