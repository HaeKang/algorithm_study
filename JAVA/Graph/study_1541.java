import java.io.*;

public class study_1541 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static String tmp;
	static boolean par = false;
	static int ans = 0;
	
	public static void main(String[] args) throws IOException{
		String[] input = br.readLine().split("\\-");
		String[] input_plus = input[0].split("\\+");
		
		for(String s : input_plus) {
			ans += Integer.parseInt(s);
		}
		
		for(int i=1; i<input.length; i++) {
			String[] tmp = input[i].split("\\+");
			for(String s2 : tmp) {
				ans -= Integer.parseInt(s2);
			}
		}
		
		bw.write(String.valueOf(ans));
		bw.flush();
	}
	
}
