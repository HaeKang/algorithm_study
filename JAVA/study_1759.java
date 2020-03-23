package study_0323;
import java.io.*;
import java.util.Arrays;

public class study_1759 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	
	public static boolean check(String pw) {
		int ja = 0;
		int mo = 0;
		
		for(char x : pw.toCharArray()) {
			if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') {
                mo += 1;
            } else {
                ja += 1;
            }
		}
		
		return ja >=2 && mo >=1;
	}
	
	public static void go(int n, String[] alpha, String pw, int i) throws IOException {
		if(pw.length() == n) {
			if(check(pw)) {
				bw.write(pw+"\n");
			}
			return;
		}
		
		if(i >= alpha.length) {
			return;
		}
		
		go(n, alpha, pw+alpha[i], i+1);
		go(n, alpha,pw,i+1);
	}
	
	public static void main(String[] args) throws IOException{
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		
		String[] str2 = br.readLine().split(" ");
		String[] alpha = new String[m];
		
		for(int i=0; i<m; i++) {
			alpha[i] = str2[i];
		}
		
		Arrays.sort(alpha);
		go(n,alpha,"",0);
		
		bw.flush();
	}
}
