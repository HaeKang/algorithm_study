package study_0317;
import java.io.*;

public class study_11052 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException{
		int n = Integer.parseInt(br.readLine());
		
		String[] cost = br.readLine().split(" ");
		
		int[] a = new int[n+1];	// 카드값
		int[] d = new int[n+1];	// 카드최대값
		
		for(int i=0; i<n; i++) {
			a[i+1] = Integer.parseInt(cost[i]);
		}
		

		for(int i=1; i<=n; i++) {
			for(int j=1; j<=i; j++) {
				d[i] = Math.max(d[i], d[i-j] + a[j]);
			}
		}
		
		bw.write(d[n] + "\n");
		bw.flush();
	}
}
