/**
 * Date and time formatting, parsing, and duration utilities built on java.time.
 */

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

/**
 * DateTimeUtils: LocalDateTime and formatting.
 */
public class DateTimeUtils {

    private static final DateTimeFormatter ISO_FORMATTER = DateTimeFormatter.ISO_LOCAL_DATE_TIME;

    public static String formatIso(LocalDateTime dateTime) {
        return dateTime.format(ISO_FORMATTER);
    }

    public static String formatHuman(LocalDateTime dateTime, Locale locale) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd MMM yyyy HH:mm", locale);
        return dateTime.format(formatter);
    }

    public static LocalDateTime atMidnight(LocalDate date, ZoneId zoneId) {
        return date.atStartOfDay(zoneId).toLocalDateTime();
    }
}
