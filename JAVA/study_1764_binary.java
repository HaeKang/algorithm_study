package test;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class study_1764 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int MAX = 500001;
	static int n,m;
	
	static ArrayList<String> nList = new ArrayList<>();
	static ArrayList<String> ansList = new ArrayList<>();
	
	
	public static void main(String[] args) throws IOException{
		String[] str = br.readLine().split(" ");
		n = Integer.parseInt(str[0]);
		m = Integer.parseInt(str[1]);
		
		for(int i=0; i<n; i++) {
			String str1 = br.readLine();
			nList.add(str1);
		}
		
		Collections.sort(nList);
		String[] arr = new String[nList.size()];
		arr = nList.toArray(arr);
		
		for(int i=0; i<m; i++) {
			String str2 = br.readLine();
			int idx = Arrays.binarySearch(arr, str2);
			if(idx >= 0) {
				ansList.add(str2);
			}
		}
		
		Collections.sort(ansList);
		
		bw.write(String.valueOf(ansList.size())+"\n");
		for(String s : ansList) {
			bw.write(String.valueOf(s) + "\n");
		}
		bw.flush();
	}
	
}
