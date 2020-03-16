package study_0315;
import java.io.*;
import java.util.*;

// ��Ÿ�ӿ���
// �ذ��� -> bufferedReader�� �ѹ��� ȣ���Ѵ�. �������� �Է��� ���������ص�! �ް���������

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
