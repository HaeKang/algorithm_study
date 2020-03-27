package study_0317;

import java.io.*;

public class study_11057 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	public static long mod = 10007;
	
	static public void main(String[] args) throws IOException{
		int n = Integer.parseInt(br.readLine());
		long[][] d = new long[n+1][10];
        for (int i=0; i<=9; i++) {
            d[1][i] = 1;
        }
        
        for (int i=2; i<=n; i++) {
            for (int j=0; j<=9; j++) {
                for (int k=0; k<=j; k++) {
                    d[i][j] += d[i-1][k];
                    d[i][j] %= mod;
                }
            }
        }
        long ans = 0;
        for (int i=0; i<10; i++) {
            ans += d[n][i];
        }
        ans %= mod;
        bw.write(ans+"\n");
        bw.flush();
	}
	
}
