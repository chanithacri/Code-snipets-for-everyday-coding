/**
 * Demonstrates serializing and deserializing Java objects to disk with try-with-resources.
 */

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

/**
 * Serialization: Serialize/deserialize objects.
 */
public class Serialization {

    public static byte[] toBytes(Serializable value) throws IOException {
        try (ByteArrayOutputStream buffer = new ByteArrayOutputStream();
                ObjectOutputStream output = new ObjectOutputStream(buffer)) {
            output.writeObject(value);
            return buffer.toByteArray();
        }
    }

    @SuppressWarnings("unchecked")
    public static <T> T fromBytes(byte[] data, Class<T> type) throws IOException, ClassNotFoundException {
        try (ByteArrayInputStream buffer = new ByteArrayInputStream(data);
                ObjectInputStream input = new ObjectInputStream(buffer)) {
            Object value = input.readObject();
            return (T) type.cast(value);
        }
    }
}
