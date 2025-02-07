package util.reporting;

import io.cucumber.java.After;
import io.cucumber.java.Scenario;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriverException;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.UUID;

public class PhotographerHook {

    @Autowired
    private WebDriver webDriver;

    @After
    public void takeScreenshotAndCloseDriver(Scenario scenario) {
        try {
            // Take screenshot FIRST
            if (webDriver instanceof TakesScreenshot) { // Check if it supports screenshots
                final byte[] screenshot = ((TakesScreenshot) webDriver).getScreenshotAs(OutputType.BYTES);
                scenario.attach(screenshot, "image/png", UUID.randomUUID().toString());
            } else {
                System.out.println("WebDriver instance does not support screenshots.");
            }
        } catch (WebDriverException wde) {
            System.out.println("Error taking screenshot: " + wde.getMessage());
        } finally {
            // Close WebDriver in the 'finally' block to ensure it always runs
            if (webDriver != null) {
                webDriver.quit();
            }
        }
    }
}