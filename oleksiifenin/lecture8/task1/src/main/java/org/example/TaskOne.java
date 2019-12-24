package org.example;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.List;

/**
 * Created by Thealeshka on 10.12.2019 inside the package - org.example
 */


public class TaskOne {
    private final HttpClient httpClient;

    {
        httpClient = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_2)
                .build();
    }

    public static TaskOne getInstance() {
        return new TaskOne();
    }

    public TaskOne() {
    }

    public void execute(List<URI> urls) {
        urls.forEach(uri -> {
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
        });

    }
}
