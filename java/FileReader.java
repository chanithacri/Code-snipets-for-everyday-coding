/**
 * Safe text file reader that wraps IOExceptions and supports line-by-line callbacks.
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.util.Objects;
import java.util.function.Consumer;

/**
 * Utility helpers for reading and writing files.
 *
 * <p>The helpers keep business logic isolated from I/O, wrap checked exceptions
 * into {@link FileAccessException}, and accept an optional logger so callers can
 * integrate with their observability stack.</p>
 *
 * <h2>Usage example</h2>
 * <pre>{@code
 * Path file = Path.of("example.txt");
 * FileReader.writeText(file, "hello world");
 * String contents = FileReader.readText(file);
 * }
 * </pre>
 */
public final class FileReader {
    private static final Consumer<String> NO_OP_LOGGER = message -> { };

    private FileReader() {
    }

    /** Exception thrown when a file operation fails. */
    public static final class FileAccessException extends IOException {
        public FileAccessException(String message, Throwable cause) {
            super(message, cause);
        }

        public FileAccessException(String message) {
            super(message);
        }
    }

    public static String readText(Path path) throws FileAccessException {
        return readText(path, StandardCharsets.UTF_8, NO_OP_LOGGER);
    }

    public static String readText(Path path, Charset charset, Consumer<String> logger) throws FileAccessException {
        Objects.requireNonNull(path, "path");
        Objects.requireNonNull(charset, "charset");
        Objects.requireNonNull(logger, "logger");
        try {
            logger.accept("readText: reading " + path);
            return Files.readString(path, charset);
        } catch (NoSuchFileException ex) {
            logger.accept("readText: not found " + path);
            throw new FileAccessException("File not found: " + path, ex);
        } catch (IOException ex) {
            logger.accept("readText: error reading " + path + " - " + ex.getMessage());
            throw new FileAccessException("Unable to read " + path, ex);
        }
    }

    public static Path writeText(Path path, String contents) throws FileAccessException {
        return writeText(path, contents, StandardCharsets.UTF_8, true, NO_OP_LOGGER);
    }

    public static Path writeText(Path path, String contents, Charset charset, boolean createDirectories,
                                 Consumer<String> logger) throws FileAccessException {
        Objects.requireNonNull(path, "path");
        Objects.requireNonNull(contents, "contents");
        Objects.requireNonNull(charset, "charset");
        Objects.requireNonNull(logger, "logger");
        try {
            if (createDirectories) {
                Path parent = path.getParent();
                if (parent != null) {
                    Files.createDirectories(parent);
                }
            }
            logger.accept("writeText: writing to " + path);
            Files.writeString(path, contents, charset);
            return path;
        } catch (IOException ex) {
            logger.accept("writeText: error writing " + path + " - " + ex.getMessage());
            throw new FileAccessException("Unable to write to " + path, ex);
        }
    }

    public static byte[] readBytes(Path path) throws FileAccessException {
        return readBytes(path, NO_OP_LOGGER);
    }

    public static byte[] readBytes(Path path, Consumer<String> logger) throws FileAccessException {
        Objects.requireNonNull(path, "path");
        Objects.requireNonNull(logger, "logger");
        try {
            logger.accept("readBytes: reading " + path);
            return Files.readAllBytes(path);
        } catch (NoSuchFileException ex) {
            logger.accept("readBytes: not found " + path);
            throw new FileAccessException("File not found: " + path, ex);
        } catch (IOException ex) {
            logger.accept("readBytes: error reading " + path + " - " + ex.getMessage());
            throw new FileAccessException("Unable to read " + path, ex);
        }
    }

    public static Path writeBytes(Path path, byte[] data) throws FileAccessException {
        return writeBytes(path, data, true, NO_OP_LOGGER);
    }

    public static Path writeBytes(Path path, byte[] data, boolean createDirectories,
                                  Consumer<String> logger) throws FileAccessException {
        Objects.requireNonNull(path, "path");
        Objects.requireNonNull(data, "data");
        Objects.requireNonNull(logger, "logger");
        try {
            if (createDirectories) {
                Path parent = path.getParent();
                if (parent != null) {
                    Files.createDirectories(parent);
                }
            }
            logger.accept("writeBytes: writing " + path);
            Files.write(path, data);
            return path;
        } catch (IOException ex) {
            logger.accept("writeBytes: error writing " + path + " - " + ex.getMessage());
            throw new FileAccessException("Unable to write to " + path, ex);
        }
    }
}
