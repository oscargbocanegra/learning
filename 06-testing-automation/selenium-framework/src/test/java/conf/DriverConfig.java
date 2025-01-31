package conf;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import java.util.Objects;

@Configuration
@ComponentScan(basePackages = {"pageobjects", "stepdefinitions"})
public class DriverConfig {

    @Bean(destroyMethod = "quit") // Cierra el WebDriver al final
    public WebDriver webDriver() {
        String os = System.getProperty("os.name").toLowerCase();
        String driverPath;

        if (os.contains("win")) {
            driverPath = driverPath = Objects.requireNonNull(getClass().getClassLoader()
                            .getResource("drivers/windows/chromedriver.exe"))
                    .getPath();
        } else if (os.contains("linux")) {
            driverPath = getClass().getClassLoader().getResource("drivers/linux/chromedriver").getPath();
        } else if (os.contains("mac")) {
            driverPath = getClass().getClassLoader().getResource("drivers/mac/chromedriver").getPath();
        } else {
            throw new UnsupportedOperationException("Sistema operativo no soportado: " + os);
        }

        System.setProperty("webdriver.chrome.driver", driverPath);

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--start-maximized");
        options.addArguments("--disable-notifications");
        options.addArguments("--remote-allow-origins=*");

        return new ChromeDriver(options);
    }
}