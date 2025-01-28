public class Trycatchexample {
    public static void main(String[] args) {
        try {
            int[] array = new int[5];
            array[0] = 10; // Writing to the array
            array[1] = 11; // Writing to the array
            array[2] = 12; // Writing to the array
            array[3] = 13; // Writing to the array
            array[4] = 14; // Writing to the array
            array[5] = 15; // Writing to the array
            array[6] = 16; // Writing to the array
            array[7] = 17; // Writing to the array
            System.out.println(array[0]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
