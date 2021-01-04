import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
		int[] dp = new int[41];
		dp[0] = 0;
		dp[1] = 1;
		
		for(int i=2; i<=40; i++) {
			dp[i] = dp[i-1] + dp[i-2];
		}
		
		int n = Integer.parseInt(br.readLine());
		
		for(int j=0; j<n; j++) {
			int m = Integer.parseInt(br.readLine());
			
			if(m == 0) {
				bw.write("1 0\n");
			} else {
				int zero = dp[m-1];
				int one = dp[m];
				bw.write(zero + " " + one + "\n");
			}
		}
		
		bw.flush();
	}
}
