/**
 * JavaFXApp: Simple JavaFX application skeleton.
 *
 * To avoid a hard dependency on JavaFX in this repository, the class exposes a
 * template string that can be copied into a JavaFX-enabled project. The
 * example illustrates the minimum code required to launch a window.
 */
public class JavaFXApp {

    public static String basicTemplate() {
        return """
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class DemoApp extends Application {
    @Override
    public void start(Stage stage) {
        stage.setTitle(\"Hello JavaFX\");
        stage.setScene(new Scene(new StackPane(new Label(\"Hi!\")), 320, 200));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
""";
    }
}
