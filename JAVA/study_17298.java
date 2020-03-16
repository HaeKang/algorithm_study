package study_0315;
import java.util.*;
import java.io.*;

public class study_17298 {
	public static void main(String[]args) throws NumberFormatException, IOException {
		// C++ 스택의 empty와 햇갈리지 말자 자바는 isEmpty()다
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int[] a = new int[n];
		int[] ans = new int[n];
		Stack<Integer> s = new Stack<>();
		
		String[] n_num = br.readLine().split(" ");
				
		for(int i=0; i<n; i++) {
			a[i] = Integer.parseInt(n_num[i]);
		}
		
		s.push(0);
		for(int i=1; i<n; i++) {
			if (s.isEmpty()) {
				s.push(i);
			}
			while(!s.isEmpty() && a[s.peek()] < a[i]) {				
				ans[s.pop()] = a[i];
			}
			
			s.push(i);
		}
		
		while(!s.isEmpty()) {
			ans[s.pop()] = -1;
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i=0; i<n; i++) {
			bw.write(ans[i] + " ");
		}
		bw.write("\n");
		bw.flush();
	}
}
