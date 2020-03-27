package study_0317;

import java.io.*;

public class study_16194 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException{
		int n = Integer.parseInt(br.readLine());
		
		String[] cost = br.readLine().split(" ");
		
		int[] a = new int[n+1];	
		int[] d = new int[n+1];	
		
		for(int i=0; i<n; i++) {
			a[i+1] = Integer.parseInt(cost[i]);
		}
		

		for(int i=1; i<=n; i++) {
			d[i] =-1;
			for(int j=1; j<=i; j++) {
				if(d[i] == -1 || d[i] > d[i-j] + a[j]) {
					d[i] = d[i-j] + a[j]; 
				}
			}
		}
		
		bw.write(d[n] + "\n");
		bw.flush();
	}
}
