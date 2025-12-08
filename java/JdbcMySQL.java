import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;

/**
 * JdbcMySQL: JDBC connect/query to MySQL.
 *
 * Helper methods keep connection handling minimal while still demonstrating
 * proper resource management with try-with-resources.
 */
public class JdbcMySQL {

    @FunctionalInterface
    public interface SqlTask<T> {
        T execute(Connection connection) throws SQLException;
    }

    public static Connection openConnection(String host, int port, String database, String user, String password)
            throws SQLException {
        String url = String.format("jdbc:mysql://%s:%d/%s", host, port, database);
        Properties props = new Properties();
        props.setProperty("user", user);
        props.setProperty("password", password);
        props.setProperty("useSSL", "true");
        props.setProperty("autoReconnect", "true");
        return DriverManager.getConnection(url, props);
    }

    public static <T> T withConnection(Connection connection, SqlTask<T> task) throws SQLException {
        try (connection) {
            return task.execute(connection);
        }
    }

    public static PreparedStatement prepare(Connection connection, String sql, Object... params) throws SQLException {
        PreparedStatement statement = connection.prepareStatement(sql);
        for (int i = 0; i < params.length; i++) {
            statement.setObject(i + 1, params[i]);
        }
        return statement;
    }
}
