package study_0315;
import java.io.*;
import java.util.*;

public class study_1874 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		String ans = "";
		int n;
		Stack<Integer> s = new Stack<Integer>();
		int fin = 0;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		while(n-- > 0) {
			int x = 0;
			BufferedReader br2 = new BufferedReader(new InputStreamReader(System.in));
			x = Integer.parseInt(br2.readLine());
			
			if(x > fin) {
				while(x > fin) {
					s.push(++fin);
					ans += '+';
				}
				s.pop();
				ans += '-';
			} else {
				boolean found = false;
				if(!s.empty()) {
					int top = s.pop();
					ans += '-';
					
					if(top == x) {
						found = true;
					}
				}
				
				if(!found) {
					System.out.println("NO\n");
					break;
				}
			}	
		}
		
		for(int i=0; i< ans.length(); i++) {
			System.out.println(ans.charAt(i));
		}
		
		
	}
}
