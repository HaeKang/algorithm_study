package study_0323;
import java.io.*;

public class study_10972 {
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
		int[] a = new int[n];
		
		String[] str = br.readLine().split(" ");
		for(int i=0; i<n; i++) {
			a[i] = Integer.parseInt(str[i]);
		}
		
		if(next_permutation(a)) {
			for(int i=0; i<n; i++) {
				String ans = Integer.toString(a[i]);
				bw.write(ans+ " ");
			}
			bw.write("\n");
		} else {
			bw.write("-1\n");
		}
		
		bw.flush();
	}
}
