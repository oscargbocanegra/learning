package util.reporting;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.cucumber.plugin.ConcurrentEventListener;
import io.cucumber.plugin.event.EventPublisher;
import io.cucumber.plugin.event.TestCaseFinished;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;

public class JReporter implements ConcurrentEventListener {

    private static final String ELASTICSEARCH_URL = "http://localhost:9200/automation/_doc/";
    private static final String executionId = "12b27564-42c7";

    public JReporter() {
        System.out.println("✅ JReporter ha sido instanciado y registrado en Cucumber.");
    }

    private void onTestCaseFinished(final TestCaseFinished event) {
        try {
            System.out.println("🔹 JReporter ejecutándose para el escenario: " + event.getTestCase().getName());
            System.out.println("🔹 Estado del escenario: " + event.getResult().getStatus());

            // Crear el objeto con la información del escenario
            ScenarioExecutionInfo scenarioExecutionInfo = new ScenarioExecutionInfo();
            scenarioExecutionInfo.setExecutionId(executionId);
            scenarioExecutionInfo.setId(event.getTestCase().getId().toString());
            scenarioExecutionInfo.setName(event.getTestCase().getName());
            scenarioExecutionInfo.setStatus(event.getResult().getStatus().toString());

            // Convertir el objeto a JSON
            ObjectMapper objectMapper = new ObjectMapper();
            String jsonBody = objectMapper.writeValueAsString(scenarioExecutionInfo);

            // Imprimir valores para depuración
            System.out.println("🔹 JSON generado:");
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
            System.out.println("✅ Response status code: " + response.getStatusCode());
            System.out.println("✅ Response body: " + response.getBody().asString());

        } catch (Exception e) {
            System.err.println("❌ Error al enviar datos a Elasticsearch: " + e.getMessage());
            e.printStackTrace();
        }
    }

    @Override
    public void setEventPublisher(EventPublisher publisher) {
        System.out.println("✅ Registrando JReporter en el EventPublisher de Cucumber...");
        publisher.registerHandlerFor(TestCaseFinished.class, this::onTestCaseFinished);
    }
}
