package study_0317;
import java.io.*;
import java.util.*;

public class study_14002 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int[] a;
	static int[] v;
	static int[] d;
	
	static void print(int p) throws IOException {
		if( p == -1) {
			return;
		}
		print(v[p]);
		bw.write(a[p] +" ");
	}
	
	static public void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		
		a = new int[n];
		v = new int[n];
		d = new int[n];
		
		for(int i=0; i<n; i++) {
			a[i] = Integer.parseInt(str[i]);
		}
		
		for(int i=0; i<n; i++) {
			d[i] = 1;	// 나 자신
			v[i] = -1;	// 없을 때 -1
			for(int j=0; j<i; j++) {
				if(a[j] < a[i] && d[i] < d[j]+1) {
					d[i] = d[j]+1;
					v[i] = j;
				}
			}
		}
		
		int ans = d[0];
		int p = 0;
		
		for(int i=0; i<n; i++) {
			if(ans < d[i]) {
				ans = d[i];
				p = i;
			}
		}
		
		bw.write(ans + "\n");
		print(p);
		bw.write("\n");
		bw.flush();
	}
}
