package pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.time.Duration;

@Service
public class SignUpServices {

    @Autowired
    private  SignUpPageObject signUpPageObject;

    @Autowired
    private WebDriverWait wait;

    @Autowired
    private WebDriver driver;

    public void go(String url) {this.driver.get(url);}

    public void writeFirstName(String firstName) {
        this.wait.until(ExpectedConditions.visibilityOf(this.signUpPageObject.getFirstNameTextbox()));
        this.signUpPageObject.getFirstNameTextbox().sendKeys(firstName);
    }

    public void writeLastName(String lastName) {
        this.signUpPageObject.getLastName().sendKeys(lastName);
    }

    public void writeEmail(String email) {
        this.signUpPageObject.getEmail().sendKeys(email);
    }

    public void writePhone(String phone) {
        this.signUpPageObject.getPhone().sendKeys(phone);
    }

    public void selectMale() {
        this.signUpPageObject.getGenderMale().click();
    }

    public void selectFemale() {
        this.signUpPageObject.getGenderFemale().click();
    }

    public void selectCountry(String country) {
        this.signUpPageObject.getCountry().sendKeys(country);
    }

    public void selectBirthYear(String year) {
        this.signUpPageObject.getDateOfBirthYear().sendKeys(year);
    }

    public void selectBirthMonth(String month) {
        this.signUpPageObject.getDateOfBirthMonth().sendKeys(month);
    }

    public void selectBirthDay(String day) {
        this.signUpPageObject.getDateOfBirthDay().sendKeys(day);
    }

    public void writePassword(String password) {
        this.signUpPageObject.getPassword().sendKeys(password);
    }

    public void writeConfirmPassword(String confirmPassword) {
        this.signUpPageObject.getConfirmPassword().sendKeys(confirmPassword);
    }

    public void clickSubmit() {

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.id("submitbtn")));
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", submitButton);
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", submitButton);
    }

}
