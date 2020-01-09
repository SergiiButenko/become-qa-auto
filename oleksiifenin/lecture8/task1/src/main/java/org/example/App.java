package org.example;

import java.net.URI;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        TaskOne.getInstance()
                .execute(
                        List.of("http://localhost:5002/", "http://localhost:5002/fail500", "http://localhost:5002/basic_auth")
                                .stream().map(n -> URI.create(n)).collect(Collectors.toList()));
    }
}

