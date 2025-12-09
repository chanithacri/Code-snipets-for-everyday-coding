/**
 * Test for FileReader: Read/write files
 * Tests file read/write helpers.
 */
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import static org.junit.jupiter.api.Assertions.*;

import java.nio.file.Files;
import java.nio.file.Path;

public class FileReaderTest {
    @TempDir
    Path tempDir;

    @Test
    void writesAndReadsText() throws Exception {
        Path file = tempDir.resolve("example.txt");
        FileReader.writeText(file, "hello");
        String contents = FileReader.readText(file);
        assertEquals("hello", contents);
    }

    @Test
    void throwsForMissingFile() {
        Path missing = tempDir.resolve("missing.txt");
        assertThrows(FileReader.FileAccessException.class, () -> FileReader.readText(missing));
    }

    @Test
    void writesAndReadsBytes() throws Exception {
        Path file = tempDir.resolve("data.bin");
        byte[] payload = new byte[] {1,2,3};
        FileReader.writeBytes(file, payload);
        byte[] read = FileReader.readBytes(file);
        assertArrayEquals(payload, read);
    }
}
