package study_0317;
import java.io.*;

public class study_11727 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		int[] d = new int[1001];
		d[0] = 1;
		d[1] = 1;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		for(int i=2; i<=n; i++) {
			d[i] = d[i-1] + (2 * d[i-2]);
			d[i] %= 10007;
		}
		
		System.out.println(d[n]);
	}
}
