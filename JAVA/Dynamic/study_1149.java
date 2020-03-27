package study_0317;
import java.io.*;

public class study_1149 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static int[][] d = new int[1001][3];
	static int[][] a = new int[1001][3];
	
	static public void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		
		for(int i=0; i<n; i++) {
			String[] str = br.readLine().split(" ");
			for(int j=0; j<3; j++) {
				a[i][j] = Integer.parseInt(str[j]);
			}
		}
		
		for(int i=0; i<n; i++) {
			if(i==0) {
				d[i][0] = a[i][0];
				d[i][1] = a[i][1];
				d[i][2] = a[i][2];
			} else {
				d[i][0] = Math.min(d[i-1][1], d[i-1][2]) + a[i][0];
				d[i][1] = Math.min(d[i-1][0], d[i-1][2]) + a[i][1];
				d[i][2] = Math.min(d[i-1][0], d[i-1][1]) + a[i][2];
			}
		}
		
		bw.write(Math.min( Math.min(d[n-1][0], d[n-1][1]),d[n-1][2] ) + "\n");
		bw.flush();
	}
}
