package util;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class HookDriver {
    public static WebDriver driver;

    @Before
    public void createDriver() {
        /*
        // Opcion para Configurar automáticamente ChromeDriver
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        SignUppageObject signUpPageObject = new SignUppageObject(driver);
        */

        System.setProperty("webdriver.chrome.driver", System.getProperty("user.dir") +
                "\\src\\test\\resources\\drivers\\windows\\chromedriver.exe");

        driver = new ChromeDriver();
    }

    @After
    public void quitDriver() {
        if (driver != null) {
            driver.quit();
        }
    }

    public WebDriver getDriver() {
        return driver;
    }
}
