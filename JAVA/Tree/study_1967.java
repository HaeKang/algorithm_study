package study_0328;
import java.util.*;
import java.io.*;

class Edge{
	int to, cost;
	Edge(int to, int cost){
		this.to = to;
		this.cost = cost;
	}
}

public class study_1967 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static ArrayList<Edge>[] a;
	static boolean[] check = new boolean[10001];
    static int[] dist = new int[10001];
    
    static void bfs(int start) {
    	Arrays.fill(dist, 0);
    	Arrays.fill(check, false);
    	
    	Queue<Integer> q = new LinkedList<Integer>();
    	check[start] =true;
    	q.add(start);
    	
    	while(!q.isEmpty()) {
    		int x = q.remove();
    		for(int i=0; i<a[x].size(); i++) {
    			Edge e = a[x].get(i);
    			if(check[e.to] == false) {
    				dist[e.to] = dist[x] + e.cost;
    				q.add(e.to);
    				check[e.to] = true;
    			}
    			
    		}
    	}
    }
	
	public static void main(String[] args) throws IOException{
		int n  = Integer.parseInt(br.readLine());
		a = (ArrayList<Edge>[]) new ArrayList[n+1];
		
		for(int i=0; i<=n; i++) {
			a[i] = new ArrayList<Edge>();
		}
		
		for(int i=0; i<n-1; i++) {
			String[] str = br.readLine().split(" ");
			int u = Integer.parseInt(str[0]);
			int v = Integer.parseInt(str[1]);
			int w = Integer.parseInt(str[2]);
			a[u].add(new Edge(v,w));
			a[v].add(new Edge(u,w));
		}
		
		bfs(1);
		int start = 1;
		for(int i=2; i<=n; i++) {
			if(dist[i] > dist[start]) {
				start = i;
			}
		}
		
		bfs(start);
		int ans = dist[1];
		for(int i=2; i<=n; i++) {
			if(ans < dist[i]) {
				ans = dist[i];
			}
		}
		
		bw.write(ans+"\n");
		bw.flush();
	}
}
