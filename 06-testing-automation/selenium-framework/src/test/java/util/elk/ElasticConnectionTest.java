package util.elk;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class ElasticConnectionTest {
    public static void main(String[] args) {
        String url = "http://localhost:9200/";
        Response response = RestAssured.get(url);

        System.out.println("Response status: " + response.getStatusCode());
        System.out.println("Response body: " + response.getBody().asString());
    }
}
