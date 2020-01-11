import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution3 {

    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        int numSwaps=0;
        int temp;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]!=i+1){
                temp=arr[arr[i]-1];
                arr[arr[i]-1]=arr[i];
                arr[i]=temp;
                numSwaps++;
                i=0;
            }
        }
        return numSwaps;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        System.out.println(minimumSwaps(new int[]{2,3,4,1,5}));
    }
}
