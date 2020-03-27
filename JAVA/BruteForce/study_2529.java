package study_0323;

import java.util.*;
import java.io.*;

public class study_2529 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int n;
	static char[] a = new char[20];
	static ArrayList<String> ans = new ArrayList<>();
	static boolean[] check = new boolean[10];
	
	public static boolean ok(char x, char y, char op) {
		if(op == '<') {
			if (x>y) {
				return false;
			}
		}
		if(op == '>') {
			if(x<y) {
				return false;
			}
		}
		return true;
	}
	
	public static void go(int index, String num) {
		if(index == n+1) {
			ans.add(num);
			return;
		}
		for(int i=0; i<=9; i++) {
			if(check[i]) {
				continue;
			}
			if(index == 0 || ok(num.charAt(index-1), (char)(i+'0'), a[index-1])) {
				check[i] = true;
				go(index+1, num+Integer.toString(i));
				check[i] = false;
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		for(int i=0; i<n; i++) {
			a[i] = str[i].toCharArray()[0];
		}
		
		go(0,"");
		Collections.sort(ans);
		int m = ans.size();
		bw.write(ans.get(m-1)+"\n");
		bw.write(ans.get(0)+"\n");
		bw.flush();
		
	}
}
