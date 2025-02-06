package stepdefinitions.tasks;

import enums.Gender;
import models.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import pageobjects.SignUpServices;
import util.RandomNumberGenerator;

@Component
public class UserSignUp {

    @Autowired
    private SignUpServices signUp;

    public void withInfo(User user){

        signUp.writeFirstName(user.getFirstName());
        signUp.writeLastName(user.getLastName());
        signUp.writeEmail(user.getEmail());
        signUp.selectGender(user.getGender());
        signUp.selectCountry(user.getCountry());
        signUp.selectBirthDay(user.getBirthDay());
        signUp.selectBirthMonth(user.getBirthMonth());
        signUp.selectBirthYear(user.getBirthYear());
        signUp.writePhone(RandomNumberGenerator.get());
        signUp.writePassword(user.getPassword());
        signUp.writeConfirmPassword(user.getPasswordConfirmation());
        //signUp.clickSubmit();
    }




}
