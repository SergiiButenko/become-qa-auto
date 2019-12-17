package org.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.drive", "chromedriver");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.google.ru/");
        driver.findElement(By.name("q")).sendKeys("cheese"+Keys.RETURN);
        List<WebElement> elements=driver.findElements(By.cssSelector("h3"));
        elements.stream().filter(n->n.getText().contains("Wikipedia")).collect(Collectors.toList()).get(0).click();
        Thread.sleep(2000);
        System.out.println( driver.findElement(By.name("casein")));
    }
}
