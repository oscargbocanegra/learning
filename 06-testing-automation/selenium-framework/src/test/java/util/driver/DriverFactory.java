package util.driver;

import enums.Browser;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class DriverFactory {

    private static String pathFormat = System.getProperty("user.dir") + "\\src\\test\\resources\\drivers\\windows\\%s";

    public static WebDriver get(Browser browser) {
        if (browser == Browser.chrome) {
            System.setProperty("webdriver.chrome.driver", String.format(pathFormat, "chromedriver.exe"));
            return new ChromeDriver();
        }
        if (browser == Browser.firefox) {
            System.setProperty("webdriver.gecko.driver", String.format(pathFormat, "geckodriver.exe")); // Corregido
            return new FirefoxDriver();
        }
        if (browser == Browser.edge) {
            System.setProperty("webdriver.edge.driver", String.format(pathFormat, "msedgedriver.exe")); // Corregido
            return new EdgeDriver();
        }
        throw new IllegalArgumentException("Browser not supported: " + browser);
    }
}