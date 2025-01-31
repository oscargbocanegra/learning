package stepdefinitions;

import conf.DriverConfig;
import io.cucumber.spring.CucumberContextConfiguration;
import org.springframework.boot.test.context.SpringBootTest;

@CucumberContextConfiguration
@SpringBootTest(classes = DriverConfig.class)
public class CucumberSpringConfiguration {
}
