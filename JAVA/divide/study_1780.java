package test;
import java.io.*;

public class study_1780 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static final int MAX = 2188;
	static int[][] arr = new int[MAX][MAX];
	static int[] ans = new int[3];	// -1 0 1
	static int n;
	
	public static boolean check(int r, int c, int n) {
		for(int i=r; i<r+n; i++) {
			for(int j=c; j<c+n; j++) {
				if(arr[r][c] != arr[i][j]) {
					return false;
				}
			}
		}
		
		return true;
	}
	
	public static void divide(int r, int c, int n) {
		if(check(r,c,n)) {
			int num = arr[r][c];
			ans[num+1] += 1;
			return;
		}
		
		int size = n / 3;
		
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				divide(r+i*size, c+j*size, size);
			}
		}
		
		
	}
	
	public static void init_arr() {
		for(int i=0; i<3; i++) {
			ans[i] = 0;
		}
	}
	
	public static void main(String[] args) throws IOException{
		n = Integer.parseInt(br.readLine());
		for(int i=0; i<n; i++) {
			String[] str = br.readLine().split(" ");
			for(int j=0; j<n; j++) {
				arr[i][j] = Integer.parseInt(str[j]);
			}
		}
		
		init_arr();
		divide(0,0,n);
		
		for(int k =0; k<3; k++) {
			bw.write(String.valueOf(ans[k]) + "\n");
		}
		
		bw.flush();
	}
}
