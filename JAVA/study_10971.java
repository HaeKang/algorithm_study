package study_0323;
import java.io.*;

public class study_10971 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static boolean next_permutation(int[] a) {
		int i = a.length-1;
		while(i > 0 && a[i-1] >= a[i]) {
			i -=1;
		}
		
		if( i<=0) {
			return false;
		}
		
		int j = a.length-1;
		while(a[j] <= a[i-1]) {
			j -=1;
		}
		
		int temp = a[i-1];
		a[i-1] = a[j];
		a[j] = temp;
		
		j = a.length-1;
		while(i<j) {
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
			i +=1;
			j -=1;
		}
		return true;
	}
	
	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		int [][] a = new int[n][n];
		int[] d = new int[n];
		
		for(int i=0; i<n; i++) {
			String[] str = br.readLine().split(" ");
			for(int j=0; j<n; j++) {
				a[i][j] = Integer.parseInt(str[j]);
			}
		}
		
		for(int i =0; i<n; i++) {
			d[i] = i;
		}
		
		int ans = Integer.MAX_VALUE;
		
		do {
			boolean ok = true;
			int sum = 0;
			for(int i=0; i<n-1; i++) {
				if(a[d[i]][d[i+1]] == 0) {
					ok = false;
				} else {
					sum += a[d[i]][d[i+1]];
				}
			}
			
			if(ok && a[d[n-1]][d[0]] != 0) {
				sum += a[d[n-1]][d[0]];
				if(ans > sum) {
					ans = sum;
				}
			}
			
		}while(next_permutation(d));
		
		bw.write(ans+"\n");
		bw.flush();
	}
}
