package study_0317;
import java.io.*;

public class study_1309 {
	static int mod = 9901;
	static int[][] dp ;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static public void main(String[] args) throws IOException{
		int n = Integer.parseInt(br.readLine());
		
		dp = new int[n+1][3];
		dp[0][0] = 1;
		System.out.println(dp[0][1]);
		
		for (int i = 1; i <= n; i++) {
			dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2];
			dp[i][1] = dp[i - 1][0] + dp[i - 1][2];
			dp[i][2] = dp[i - 1][0] + dp[i - 1][1];
			for (int j = 0; j < 3; j++) {
				dp[i][j] %= mod;
			}
		}
		
		int ans = (dp[n][0] + dp[n][1] + dp[n][2]) % mod;
		bw.write(ans+"\n");
		bw.flush();
	}
}
