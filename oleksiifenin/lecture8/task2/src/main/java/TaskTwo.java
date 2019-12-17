import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
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

    public void get(URI uri, Map<String, String> headers) {

        try {
            System.out.println(uri.toString());
            HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .uri(uri)
                    .header("Content-Type", "application/json")
                    .header("Authorization", "Bearer "+headers.get("access_token"))
                    .build();
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.statusCode());
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public HttpResponse<String> post(URI uri, Map<String, String> headers) throws IOException, InterruptedException {
        Gson gson = new Gson();

        HttpRequest request = HttpRequest.newBuilder()
                .POST(HttpRequest.BodyPublishers.ofString(gson.toJson(headers)))
                .uri(uri)
//                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                .header("Content-Type", "application/json")
                .header("Authorization", "Bearer "+headers.get("access_token"))
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        // print status code
        System.out.println(response.statusCode());

        // print response body


        return response;

    }

    public HttpResponse<String> login(String login, String password) throws IOException, InterruptedException {
        Map<String, String> headers = new HashMap<>();
        headers.put("username", "test");
        headers.put("password", "test");
       return post(URI.create("http://localhost:5002/login"), headers);

    }

    public HttpResponse<String> delete(URI uri, Map<String, String> headers) throws IOException, InterruptedException {
        Gson gson = new Gson();

        HttpRequest request = HttpRequest.newBuilder()
                .DELETE()
                .uri(uri)
//                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                .header("Content-Type", "application/json")
                .header("Authorization", "Bearer "+headers.get("access_token"))
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        // print status code
        System.out.println(response.statusCode());

        // print response body


        return response;

    }


}
