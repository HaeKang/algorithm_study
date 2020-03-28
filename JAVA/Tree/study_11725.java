package study_0328;
import java.util.*;
import java.io.*;

public class study_11725 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException{
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer>[] a = (ArrayList<Integer>[]) new ArrayList[n+1];
		
		for(int i=0; i<=n; i++) {
			a[i] = new ArrayList<Integer>();
		}
		
		for(int i=0; i<n-1; i++) {
			String[] str = br.readLine().split(" ");
			int u = Integer.parseInt(str[0]);
			int v = Integer.parseInt(str[1]);
			a[u].add(v);
			a[v].add(u);
		}
		
		boolean[] check = new boolean[n+1];
		int[] parent = new int[n+1];
		Queue<Integer> q = new LinkedList<Integer>();
		
		q.add(1);
		check[1] = true;
		parent[1] = 0;
		
		while(!q.isEmpty()) {
			int x = q.remove();
			
			for(int i=0; i<a[x].size(); i++) {
				int y = a[x].get(i);
				if(!check[y]) {
					parent[y] = x;
					check[y] = true;
					q.add(y);
				}
				
			}
		}
		
		for(int i=2; i<=n; i++) {
			bw.write(parent[i] + "\n");
		}
		bw.flush();
	}
}
