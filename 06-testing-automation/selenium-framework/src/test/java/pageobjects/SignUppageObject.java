package pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

//Objects maping page: https://demo.automationtesting.in/Register.html

public class SignUppageObject {

    private WebDriver driver;
    private WebDriverWait wait;
    

    public SignUppageObject(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10)); // Esperar hasta 10 segundos
    }

    private By firstNameTextbox = By.xpath("//input[@ng-model='FirstName']");

    private By lastName = By.xpath("//input[@ng-model='LastName']");

    private By email = By.xpath("//input[@ng-model='EmailAdress']");

    private By phone = By.xpath("//input[@ng-model='Phone']");

    private By genderMale = By.xpath("//input[@value='Male']");

    private By genderFemale = By.xpath("//input[@value='FeMale']");

    private By country = By.id("countries");

    private By dateOfBirthYear = By.id("yearbox");

    private By dateOfBirthMonth = By.xpath("//select[@ng-model='monthbox']");

    private By dateOfBirthDay = By.id("daybox");

    private By password = By.id("firstpassword");

    private By confirmPassword = By.id("secondpassword");

    private By submit = By.id("submitbtn");

    public void go(String url) {this.driver.get(url);}

    public void writeFirstName(String firstName) {
        this.driver.findElement(this.firstNameTextbox).sendKeys(firstName);
    }

    public void writeLastName(String lastName) {
        this.driver.findElement(this.lastName).sendKeys(lastName);
    }

    public void writeEmail(String email) {
        this.driver.findElement(this.email).sendKeys(email);
    }

    public void writePhone(String phone) {
        this.driver.findElement(this.phone).sendKeys(phone);
    }

    public void selectMale() {
        this.driver.findElement(this.genderMale).click();
    }

    public void selectFemale() {
        this.driver.findElement(this.genderFemale).click();
    }

    public void selectCountry(String country) {
        this.driver.findElement(this.country).sendKeys(country);
    }

    public void selectBirthYear(String year) {
        this.driver.findElement(this.dateOfBirthYear).sendKeys(year);
    }

    public void selectBirthMonth(String month) {
        this.driver.findElement(this.dateOfBirthMonth).sendKeys(month);
    }

    public void selectBirthDay(String day) {
        this.driver.findElement(this.dateOfBirthDay).sendKeys(day);
    }

    public void writePassword(String password) {
        this.driver.findElement(this.password).sendKeys(password);
    }

    public void writeConfirmPassword(String confirmPassword) {
        this.driver.findElement(this.confirmPassword).sendKeys(confirmPassword);
    }

    public void clickSubmit() {
        try {
            WebElement iframe = driver.findElement(By.tagName("iframe"));
            if (iframe.isDisplayed()) {
                driver.switchTo().frame(iframe); // Cambiar al iframe
                System.out.println("Cambiando al iframe de publicidad");
            }
        } catch (Exception e) {
            System.out.println("No se encontró iframe de publicidad");
        }

        driver.switchTo().defaultContent();
        WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.id("submitbtn")));
        submitButton.click();
    }

}
