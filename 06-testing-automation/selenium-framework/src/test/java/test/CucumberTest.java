package test;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        features = "src/test/resources/features",
        glue = {"stepdefinitions"},
        tags = "@regression",
        plugin = {
                "pretty",
                "json:target/cucumber-reports/json/Cucumber.json",
                "html:target/cucumber-reports/html/cucumber-html-report.html",
                "junit:target/cucumber-reports/junit/Cucumber.xml",
                "rerun:target/rerun.txt",
                "tech.grasshopper.extentreports.cucumber7.ExtentReportsCucumber7Adapter:"
        },
        monochrome = true
)
public class CucumberTest {
}


