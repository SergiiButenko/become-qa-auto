import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Thealeshka on 17.12.2019 inside the package - PACKAGE_NAME
 */


public class TaskTwo {
    private final HttpClient httpClient;

    {
        httpClient = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)
                .build();
    }

    public static TaskTwo getInstance() {
        return new TaskTwo();
    }

    public TaskTwo() {
    }

    public void get(URI uri) {

        try {
            System.out.println(uri.toString());
            HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(uri)
                    .build();
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.statusCode());
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static HttpRequest.BodyPublisher ofFormData(Map<Object, Object> data) {
        StringBuilder builder = new StringBuilder();
        for (Map.Entry<Object, Object> entry : data.entrySet()) {
            if (builder.length() > 0) {
                builder.append("&");
            }
            builder.append(URLEncoder.encode(entry.getKey().toString(), StandardCharsets.UTF_8));
            builder.append("=");
            builder.append(URLEncoder.encode(entry.getValue().toString(), StandardCharsets.UTF_8));
        }
        return HttpRequest.BodyPublishers.ofString(builder.toString());
    }

    public String post(URI uri, Map<String, String> headers) throws IOException, InterruptedException {
        Gson gson = new Gson();
        String json = gson.toJson(myObject)
        HttpRequest request = HttpRequest.newBuilder()
                .POST(HttpRequest.BodyPublishers.ofString(gson.toJson(myObject)))
                .uri(uri)
//                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                   .header("Content-Type", "application/json")
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        // print status code
        System.out.println(response.statusCode());

        // print response body
        return response.toString();

    }

    public void login(String login, String password) throws IOException, InterruptedException {
        Map<String, String> headers = new HashMap<>();
        headers.put("username", "test");
        headers.put("password", "test");
        System.out.println(post(URI.create("http://localhost:5002/login"), headers));

    }


}
