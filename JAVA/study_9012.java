package study_0315;
import java.io.*;
import java.util.*;

// 런타임에러
// 해결방법 -> bufferedReader는 한번만 호출한다. 여러개의 입력을 받으려고해도! 햇갈리지말기

public class study_9012 {	
	public static String isValid(String s) {
		int count = 0;	
		for(int i=0; i<s.length(); i++) {
			if(s.charAt(i) == '(') {
				count += 1;
			} else {
				count -= 1;
			}
			if(count < 0) {
				return("NO");
			}
		}
		
		if(count == 0) {
			return("YES");
		} else {
			return("NO");
			
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		
		while (t-- > 0) {
			String s = br.readLine();
			System.out.println(isValid(s));
			
		}	
	}
}
