package stepdefinitions;

import builders.data.UserBuilder;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import org.springframework.beans.factory.annotation.Autowired;
import stepdefinitions.tasks.NavigateTo;
import stepdefinitions.tasks.UserSignUp;

public class SignUpStepDefs {

    @Autowired
    private UserSignUp signUp;

    @Autowired
    private NavigateTo navigate;

    @Given("^Pepito wants to have an account$")
    public void pepito_wants_to_have_an_account() {
        navigate.signUpPage();
    }

    @When("^he sends required information to get the account$")
    public void he_sends_required_information_to_get_the_account() throws InterruptedException {
        signUp.withInfo(
                UserBuilder
                        .anUser()
                        .but()
                        .withoutBirthDay()
                        .withoutEmail()
                        .build()
        );

        Thread.sleep(7000);
    }

    @Then("^he should be told that the account was created$")
    public void he_should_be_told_that_the_account_was_created() {
    }
}
