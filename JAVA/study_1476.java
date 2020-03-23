package study_0323;
import java.io.*;

public class study_1476 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
		String[] str = br.readLine().split(" ");
		int E = Integer.parseInt(str[0]);
		int S = Integer.parseInt(str[1]);
		int M = Integer.parseInt(str[2]);
		
		int e=1, s=1, m=1;
		
		for(int i=1;; i++) {
			
			if(e == E && s==S && m==M) {
				bw.write(i+"\n");
				break;
			}
			
			e += 1;
			s += 1;
			m += 1;

			if (e == 16) {
				e = 1;
			}
			if (s == 29) {
				s = 1;
			}
			if (m == 20) {
				m = 1;
			}
		}
		bw.flush();
	}
}
