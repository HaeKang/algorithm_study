package study_0317;

import java.io.*;

public class study_11055 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		int[] a = new int[n];
		int[] d = new int[n];
		
		String[] str = br.readLine().split(" ");
		for(int i=0; i<n; i++) {
			a[i] = Integer.parseInt(str[i]);
		}
		
		for (int i = 0; i < n; i++) {
			d[i] = a[i];
			for (int j = 0; j < i; j++) {
				if (a[j] < a[i] && d[j] + a[i] > d[i]) {
					d[i] = d[j] + a[i];
				}
			}
		}
		
		int ans = d[0];
		for(int i =0; i<n; i++) {
			if(ans < d[i]) {
				ans = d[i];
			}
		}
		
		bw.write(ans+"\n");
		bw.flush();
	}
	
}
