import java.io.*;
import java.lang.reflect.Array;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution5 {

    // Complete the countTriplets function below.
    static long countTriplets(List<Long> arr, long r) {
        HashMap<Long, Long> triplet2 = new HashMap<>();
        HashMap<Long, Long> triplet3 = new HashMap<>();
        long numTriplets = 0;
            
        for(Long num : arr) {
            //si triplet 3 contiene num triplet++;
            numTriplets += triplet3.getOrDefault(num, (long) 0);
            if (triplet2.containsKey(num)){
                triplet3.put(num*r, triplet3.getOrDefault(num*r, (long) 0) + triplet2.get(num));
            }
            triplet2.put(num*r, triplet2.getOrDefault(num*r, (long) 0) + 1);
        }
        return numTriplets;
    }

    public static void main(String[] args) throws IOException {
        ArrayList<Long> l=new ArrayList<Long>();
        l.add(Long.valueOf(1));
        l.add(Long.valueOf(3));
        l.add(Long.valueOf(9));
        l.add(Long.valueOf(9));
        l.add(Long.valueOf(27));
        l.add(Long.valueOf(81));
        System.out.println(countTriplets(l, 3));
    }
}
