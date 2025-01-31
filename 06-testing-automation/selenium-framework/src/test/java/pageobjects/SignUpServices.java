package pageobjects;

import org.openqa.selenium.WebDriver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class SignUpServices {

    @Autowired
    private  SignUpPageObject signUpPageObject;

    private WebDriver driver;

    @Autowired
    public SignUpServices(WebDriver driver) {
        if (driver == null) {
            throw new IllegalStateException("ERROR: WebDriver no ha sido inyectado correctamente.");
        }
        this.driver = driver;
    }


    public void go(String url) {this.driver.get(url);}

    public void writeFirstName(String firstName) {
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
        this.signUpPageObject.getSubmit().click();
    }

    /*public void clickSubmit(WebDriverWait wait) {

        signUpPageObject = new SignUpPageObject(driver);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10)); // 10 seconds timeout

        try {
            // Esperar a que el botón sea clickeable
            WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.id("submitbtn")));

            // Hacer scroll hasta el botón
            ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", submitButton);

            // Hacer clic en el botón usando JavaScript para evitar problemas de superposición
            ((JavascriptExecutor) driver).executeScript("arguments[0].click();", submitButton);

            System.out.println("Formulario enviado correctamente.");
        } catch (Exception e) {
            System.out.println("No se encontró ningún iframe de publicidad.");
        }

        // Asegurar que el botón "Submit" sea visible y clickeable
        WebElement submitButton = wait.until(ExpectedConditions.elementToBeClickable(By.id("submitbtn")));

        // Hacer scroll para asegurarse de que el botón es visible
        ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", submitButton);

        // Hacer clic en el botón usando JavaScript para evitar superposiciones
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", submitButton);
    }*/
}
