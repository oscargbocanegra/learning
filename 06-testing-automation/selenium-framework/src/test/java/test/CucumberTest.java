package test;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        features = "src/test/resources/features",
        glue = {"stepdefinitions"},
        plugin = {
                "pretty",
                "json:target/cucumber-reports/Cucumber.json", // ¡Asegúrate de que esta línea está presente!
                "html:target/cucumber-reports/cucumber-html-report.html",
                "junit:target/cucumber-reports/Cucumber.xml",
                "rerun:target/rerun.txt",
                "tech.grasshopper.extentreports.cucumber7.ExtentReportsCucumber7Adapter:"
        },
        monochrome = true
)
public class CucumberTest {
}


