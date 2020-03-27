package study_0317;
import java.io.*;

public class study_1463 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		int[] d = new int[1000001];
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		d[1] = 0;
		
		for(int i=2; i<=n; i++) {
			d[i] = d[i-1] +1;
			if (i % 2 == 0 && d[i] > d[i / 2] + 1) {
				d[i] = d[i / 2] + 1;
			}
			if (i % 3 == 0 && d[i] > d[i / 3] + 1) {
				d[i] = d[i / 3] + 1;
			}
		}
		
		System.out.println(d[n]);
	}
}
