package study_0323;
import java.io.*;

public class study_6064 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
		int t = Integer.parseInt(br.readLine());
		
		while(t-->0) {
			String[] str = br.readLine().split(" ");
			int m = Integer.parseInt(str[0]);
			int n = Integer.parseInt(str[1]);
			int x = Integer.parseInt(str[2]);
			int y = Integer.parseInt(str[3]);
			boolean ok = false;
			
			x -= 1;
			y -= 1;
			
			for(int k = x; k<(n*m); k+=m) {
				if(k%n == y) {
					ok = true;
					bw.write(k+1+"\n");
					break;
				}
			}
			
			if(!ok) {
				bw.write(-1+"\n");
			}
		}
		
		bw.flush();
	}
}
