public class arrays {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println(numbers[0]);
        System.out.println(numbers[1]);
        System.out.println(numbers[2]);
        System.out.println(numbers[3]);
        System.out.println(numbers[4]);

        int[] numbers2 = new int[5];
        numbers2[0] = 1;
        System.out.println(numbers2[0]);

        /*Arrays multi-dimencionales */
        int[][] matrix = new int[4][4];
        int[][] matrix2 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        System.out.println(matrix2[0][0]);
        System.out.println(matrix[0][2]);    


    }
}
