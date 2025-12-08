import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * Concurrency: Executors and synchronization basics.
 */
public class Concurrency {

    public static <T> List<Future<T>> runAll(List<Callable<T>> tasks) {
        ExecutorService executor = Executors.newFixedThreadPool(Math.max(1, tasks.size()));
        try {
            return executor.invokeAll(tasks);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new RuntimeException("Task execution interrupted", e);
        } finally {
            executor.shutdown();
        }
    }

    public static <T> T waitFor(Future<T> future) {
        try {
            return future.get();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new RuntimeException("Interrupted while waiting for result", e);
        } catch (ExecutionException e) {
            throw new RuntimeException("Task failed", e.getCause());
        }
    }
}
