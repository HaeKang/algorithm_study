package study_0315;
import java.util.*;
import java.io.*;

public class study_9093 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		Stack<Character> s = new Stack<Character>();
		BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int i = Integer.parseInt(br.readLine());

		while(i-- > 0) {
			String str = br.readLine() + '\n';
			for(char ch : str.toCharArray()) {
				if(ch == ' ' || ch == '\n') {
					while(!s.isEmpty()) {
						bw.write(s.pop());
					}
					
					bw.write(ch);
					
				} else {
					s.push(ch);
				}
			}
		}
		
		bw.flush();
		
	}
}
