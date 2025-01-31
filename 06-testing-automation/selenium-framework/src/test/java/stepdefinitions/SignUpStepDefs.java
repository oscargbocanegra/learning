package stepdefinitions;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pageobjects.SignUpServices;


public class SignUpStepDefs {

    @Autowired
    private final SignUpServices signUp;

    @Autowired
    public SignUpStepDefs(SignUpServices signUp) {
        this.signUp = signUp;
    }

    @Given("^Pepito wants to have an account$")
    public void pepito_wants_to_have_an_account() {

        signUp.go("https://demo.automationtesting.in/Register.html");
        signUp.writeFirstName("Pepito");
        signUp.writeLastName("Perez");
        signUp.writeEmail("pepitoperez@email.com");
        signUp.writePhone("1234567890");
        signUp.selectMale();
        signUp.selectCountry("Mexico");
        signUp.selectBirthYear("1990");
        signUp.selectBirthMonth("January");
        signUp.selectBirthDay("1");
        signUp.writePassword("password");
        signUp.writeConfirmPassword("password");
        signUp.clickSubmit();
    }

    @When("^he sends required information to get the account$")
    public void he_sends_required_information_to_get_the_account() {
    }

    @Then("^he should be told that the account was created$")
    public void he_should_be_told_that_the_account_was_created() {
    }
}
