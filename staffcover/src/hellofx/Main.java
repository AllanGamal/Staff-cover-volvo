package hellofx;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class Main extends Application {

    private BorderPane layout;
    private Scene scene;

    public static void main(String[] args) {
        launch(args);
        
    }

    @Override
    public void start(Stage window) throws Exception {
        layout = new BorderPane();
        scene = new Scene(layout, 400, 80);

        Button button = new Button("Click me");
        layout.setCenter(button);

        window.setTitle("HelloFX");
        window.setScene(scene);
        window.show();
        
    }
    
}