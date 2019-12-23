import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.net.URI;
import java.util.HashMap;

/**
 * Created by Thealeshka on 17.12.2019 inside the package - PACKAGE_NAME
 */


public class App {
    public static void main(String[] args) throws IOException, InterruptedException {
        ObjectMapper mapper = new ObjectMapper();
        HashMap<String, String> result = mapper.readValue(TaskTwo.getInstance().login("test", "test").body(), HashMap.class);
        TaskTwo executor = TaskTwo.getInstance();
        executor.post(URI.create("http://localhost:5002/items"), result);
        executor.get(URI.create("http://localhost:5002/items"), result);
        executor.delete(URI.create("http://localhost:5002/items/0"), result);
    }
}
