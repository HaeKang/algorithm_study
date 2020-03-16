package study_0315;
import java.util.*;
import java.io.*;

public class study_17413 {
	public static void print(Stack<Character> s) {
		while(!s.empty()) {
			System.out.print(s.pop());
		}
	}
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		boolean tag = false;
		Stack<Character> s = new Stack<>();
		
		for(int i = 0; i<str.length(); i++) {
			Character str_i = str.charAt(i);
			if(str_i == '<') {
				tag = true;
				print(s);
				System.out.print(str_i);
			} else if (str_i == '>') {
				tag = false;
				System.out.print(str_i);
			} else if (tag) {
				System.out.print(str_i);
			} else {
				if(str_i == ' ') {
					print(s);
					System.out.print(str_i);
				} else {
					s.push(str_i);
				}
			}
		}
		
		print(s);
		
	}
}
