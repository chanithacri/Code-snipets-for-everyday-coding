import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

/**
 * Annotations: Custom annotations example.
 */
public class Annotations {

    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.METHOD)
    public @interface Audited {
        String value();
    }

    public static List<String> auditLog(Object target) {
        List<String> log = new ArrayList<>();
        for (Method method : target.getClass().getDeclaredMethods()) {
            Audited marker = method.getAnnotation(Audited.class);
            if (marker != null) {
                log.add(method.getName() + ": " + marker.value());
            }
        }
        return log;
    }
}
