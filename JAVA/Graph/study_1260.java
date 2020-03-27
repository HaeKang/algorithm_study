package study_0324;
import java.util.*;
import java.io.*;

public class study_1260 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static ArrayList<Integer>[] a;	// 배열안에 ArrayList<Integer>넣음
	static boolean[] c;
	
	public static void dfs(int x) throws IOException{
		if(c[x]) {
			return;
		}
		c[x] = true;
		bw.write(x +" ");
		for (int y = 0; y < a[x].size(); y++) {
			int next = a[x].get(y);
            if (c[next] == false) {
                dfs(next);
            }
        }
		
	}
	
	public static void bfs(int x) throws IOException{
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(x);
		c[x] = true;
		
		while(!q.isEmpty()) {
			int y = q.remove();
			bw.write(y + " ");
			
			for(int i = 0; i<a[y].size(); i++) {
				int next = a[y].get(i);
				if(c[next] == false) {
					c[next] = true;
					q.add(next);
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException{
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		int start = Integer.parseInt(str[2]);
		
		a = (ArrayList<Integer>[]) new ArrayList[n+1];
		
		for(int i=0; i<=n; i++) {
			a[i] = new ArrayList<Integer>();
		}
		
		for(int i=0; i<m; i++) {
			String[] str2 = br.readLine().split(" ");
			int u = Integer.parseInt(str2[0]);
			int v = Integer.parseInt(str2[1]);
			a[u].add(v);
			a[v].add(u);
		}
		
		for(int i=1; i<=n; i++) {
			Collections.sort(a[i]);
		}
		
		
		c = new boolean[n+1];
		dfs(start);
		bw.write("\n");
		c = new boolean[n+1];
		bfs(start);
		bw.write("\n");
		bw.flush();
	}
}
