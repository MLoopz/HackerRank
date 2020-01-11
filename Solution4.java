import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution4 {

    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] queries) {
        long max=0;
        long[] arr=new long[n+2];
        for (int i = 0; i < queries.length; i++) {
            arr[queries[i][0]]+=queries[i][2];
            arr[queries[i][1]+1]-=queries[i][2];
            if(queries[i][0]>max) max=arr[queries[i][0]];
        }
        //max
        long sum=0;
        for (int j = 0; j < arr.length; j++) {
            sum+=arr[j];
            arr[j]=sum;
            if(arr[j]>max) max=arr[j];
        }
        
        return max;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        System.out.println(arrayManipulation(5, new int[][]{{1,2,100},{2,5,100},{3,4,100}}));
        System.out.println(arrayManipulation(10, new int[][]{{2,6,8},{3,5,7},{1,8,1},{5,9,15}}));
    }
}
