import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(min(n));
    }
    
    public static String min(int number) {
        if(number % 2 == 0){
            return number+" is even";
        } else {
            return number+" is odd";
        }
    }
}