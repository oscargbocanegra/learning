package util.elk;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;

public class ElasticInsertTest {
    public static void main(String[] args) {
        String url = "http://localhost:9200/automation/_doc/";

        String jsonBody = "{"
                + "\"executionId\": \"12b27564-42c7-4824-ad90-8fba4bde2222\","
                + "\"id\": \"manual-test\","
                + "\"name\": \"Manual Test\","
                + "\"status\": \"PASSED\""
                + "}";

        Response response = RestAssured
                .given()
                .log().all()  // Log de la petición
                .body(jsonBody)
                .contentType(ContentType.JSON)
                .when()
                .post(url)
                .then()
                .log().all()  // Log de la respuesta
                .extract().response();

        System.out.println("Response status code: " + response.getStatusCode());
        System.out.println("Response body: " + response.getBody().asString());
    }
}
