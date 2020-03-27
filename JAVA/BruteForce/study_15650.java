package study_0323;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class study_15650 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int[] a = new int[10];
	
	static void go(int index, int start, int n, int m) throws IOException {
		if(index == m) {
			for(int i=0; i<m; i++) {
				String str = Integer.toString(a[i]);
				bw.write(str);
				if( i != m-1 ) {
					bw.write(" ");
				}
			}
			bw.write("\n");
			return;
		}
		
		for(int i=start; i<=n; i++) {
			a[index] = i;
			go(index+1, i+1, n, m);
		}
	}
	
	public static void main(String[] args) throws IOException {
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		go(0,1,n,m);
		bw.flush();
	}
	
}
