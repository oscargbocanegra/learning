package util.reporting;

import enums.TakeScreenshotCondition;
import io.cucumber.java.After;
import io.cucumber.java.AfterStep;
import io.cucumber.java.Scenario;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriverException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;

import java.util.UUID;

public class PhotographerHook {

    @Autowired
    private WebDriver webDriver;

    @Value("${take.screenshot.condition}")
    TakeScreenshotCondition takeScreenshotCondition;

    @After
    public void takeScreenshotAfterScenario(Scenario scenario) {
        if (TakeScreenshotCondition.everyStep == takeScreenshotCondition) {
            takeScreenshot(scenario);
        }
    }

    @AfterStep
    public void takeScreenshotAfterEveryStep(Scenario scenario) {
        if (TakeScreenshotCondition.everyStep == takeScreenshotCondition) {
            takeScreenshot(scenario);
        }
    }

    @After
    public void takeScreenshotAfterFailingScenario (Scenario scenario){
        if (scenario.isFailed() && TakeScreenshotCondition.failingScenario == takeScreenshotCondition) {
            takeScreenshot(scenario);
        }
    }


    private void takeScreenshot(Scenario scenario) {
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
        }
    }
}