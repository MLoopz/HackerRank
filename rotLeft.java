import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution2 {

    // Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d) {
        int[] arr=new int[a.length];
        int index=0;
        for (int i = 0; i < a.length; i++) {
            if(i-d<0) index=a.length+(i-d);
            else index=i-d;
           arr[index]=a[i];
        }
        return arr;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        
    }
}
