import java.util.*;

public class Diccionarios {
    public static void main(String[] args) {
        HashMap<String, String> diccionario = new HashMap<>();
        diccionario.put("casa", "house");
        diccionario.put("perro", "dog");
        diccionario.put("gato", "cat");
        diccionario.put("rojo", "red");
        diccionario.put("azul", "blue");

        /*
        System.out.println(diccionario.get("casa"));
        System.out.println(diccionario.get("perro"));
        System.out.println(diccionario.get("gato"));
        System.out.println(diccionario.get("rojo"));
        System.out.println(diccionario.get("azul"));
         */

        for (String key : diccionario.keySet()) {
            System.out.println(key + " -> " + diccionario.get(key));
        }
    }
}
