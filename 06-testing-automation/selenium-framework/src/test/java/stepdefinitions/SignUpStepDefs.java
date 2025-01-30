package stepdefinitions;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import pageobjects.SignUppageObject;

public class SignUpStepDefs {


    @Given("^Pepito wants to have an account$")
    public void pepito_wants_to_have_an_account() {


        System.setProperty("webdriver.chrome.driver", System.getProperty("user.dir") +
                "\\src\\test\\resources\\drivers\\windows\\chromedriver.exe");

        WebDriver driver = new ChromeDriver();
        SignUppageObject signUpPageObject = new SignUppageObject(driver);

        /**
         * Opcion para Configurar automáticamente ChromeDriver
         *
         *         WebDriverManager.chromedriver().setup();
         *         driver = new ChromeDriver();
         *         SignUppageObject signUpPageObject = new SignUppageObject(driver);
         */

        signUpPageObject.go("https://demo.automationtesting.in/Register.html");
        signUpPageObject.writeFirstName("Pepito");
        signUpPageObject.writeLastName("Perez");
        signUpPageObject.writeEmail("pepitoperez@email.com");
        signUpPageObject.writePhone("1234567890");
        signUpPageObject.selectMale();
        signUpPageObject.selectCountry("Mexico");
        signUpPageObject.selectBirthYear("1990");
        signUpPageObject.selectBirthMonth("January");
        signUpPageObject.selectBirthDay("1");
        signUpPageObject.writePassword("password");
        signUpPageObject.writeConfirmPassword("password");
        signUpPageObject.clickSubmit();

    }

    @When("^he sends required information to get the account$")
    public void he_sends_required_information_to_get_the_account() {
    }

    @Then("^he should be told that the account was created$")
    public void he_should_be_told_that_the_account_was_created() {
    }
}
