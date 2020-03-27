package study_0317;
import java.util.*;
import java.io.*;

public class study_11726 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		int[] d = new int[1001];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		d[0] = 1;
		d[1] = 1;
		
		for(int i =2; i<=n; i++) {
			d[i] = d[i-1] + d[i-2];
			d[i] %= 10007;
		}
		
		System.out.println(d[n]);
	}
}
