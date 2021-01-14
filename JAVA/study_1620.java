import java.io.*;
import java.util.HashMap;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int MAX = 100001;
	static int n,m;
	static HashMap<String, Integer> d = new HashMap<String, Integer>();
	static String[] d2 = new String[MAX];
	
	static public void main(String args[]) throws IOException{
		String[] str = br.readLine().split(" ");
		n = Integer.parseInt(str[0]);
		m = Integer.parseInt(str[1]);
		
		for(int i =0; i<n; i++) {
			String name = br.readLine();
			d.put(name, i+1);
			d2[i+1] = name;
		}
		
		for(int i=0; i<m; i++) {
			String tmp = br.readLine();
			boolean isnum = false;
			
			for(int j=0; j<tmp.length(); j++) {
				char tmp_c = tmp.charAt(j);
				if('0' <= tmp_c && tmp_c <= '9') {
					isnum = true;
				}
			}
			
			
			if(isnum) {
				int tmp_num = Integer.parseInt(tmp);
				bw.write(String.valueOf(d2[tmp_num]) + '\n');
			} else {
				bw.write(String.valueOf(d.get(tmp))+'\n');
			}
		}
		
		bw.flush();
	}
}
