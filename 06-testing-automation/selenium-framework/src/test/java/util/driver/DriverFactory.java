package util.driver;

import enums.Browser;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;


public class DriverFactory {

    private static String pathFormat = System.getProperty("user.dir") + "\\src\\test\\resources\\drivers\\windows\\%s";

    public static WebDriver get(Browser browser) {

        if(browser == Browser.CHROME) {
            System.setProperty("webdriver.chrome.driver", String.format(pathFormat, "chromedriver.exe"));
            return new ChromeDriver();
        }
        if(browser == Browser.FIREFOX) {
            System.setProperty("webdriver.chrome.driver", String.format(pathFormat, "geckodriver.exe"));
            return new FirefoxDriver();
        }
        if(browser == Browser.EDGE) {
            System.setProperty("webdriver.chrome.driver", String.format(pathFormat, "msedgedriver.exe"));
            return new EdgeDriver();
        }
        throw new IllegalArgumentException("Browser not supported: " + browser);
    }

}
