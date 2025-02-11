/*
package util.reporting;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.cucumber.java.After;
import io.cucumber.java.Scenario;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;

public class HookReporter {

    private static final String ELASTICSEARCH_URL = "http://localhost:9200/automation/_doc/";
    private static final String executionId = "12b27564-42c7";

    @After
    public void reportFinalScenarioStatus(Scenario scenario) {
        try {
            // Verificar si scenario contiene datos
            System.out.println("Hook @After ejecutándose para el escenario: " + scenario.getName());
            System.out.println("Scenario ID: " + scenario.getId());
            System.out.println("Scenario Status: " + scenario.getStatus());

            // Crear el objeto con la información del escenario
            ScenarioExecutionInfo scenarioExecutionInfo = new ScenarioExecutionInfo();
            scenarioExecutionInfo.setExecutionId(executionId);
            scenarioExecutionInfo.setId(scenario.getId());
            scenarioExecutionInfo.setName(scenario.getName());
            scenarioExecutionInfo.setStatus(scenario.getStatus().toString());

            // Imprimir valores antes de enviarlos
            System.out.println("Execution ID: " + scenarioExecutionInfo.getExecutionId());
            System.out.println("Scenario ID: " + scenarioExecutionInfo.getId());
            System.out.println("Scenario Name: " + scenarioExecutionInfo.getName());
            System.out.println("Scenario Status: " + scenarioExecutionInfo.getStatus());

            // Convertir a JSON
            ObjectMapper objectMapper = new ObjectMapper();
            String jsonBody = objectMapper.writeValueAsString(scenarioExecutionInfo);

            // Imprimir JSON antes de enviarlo
            System.out.println("JSON generado:");
            System.out.println(jsonBody);

            // Enviar datos a Elasticsearch con logs detallados
            Response response = RestAssured
                    .given()
                    .log().all()  // Log de la petición
                    .body(jsonBody)
                    .contentType(ContentType.JSON)
                    .when()
                    .post(ELASTICSEARCH_URL)
                    .then()
                    .log().all()  // Log de la respuesta
                    .extract().response();

            // Imprimir respuesta para depuración
            System.out.println("Response status code: " + response.getStatusCode());
            System.out.println("Response body: " + response.getBody().asString());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
*/
