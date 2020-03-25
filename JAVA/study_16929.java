package study_0324;
import java.io.*;
import java.util.*;

public class study_16929 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static ArrayList<Integer>[] a;	// 연결되어있는 목록
    static int[] check;
    static int[] dist;
    
    static int go(int p, int x) {
    	if(check[x] == 1) {
    		return x;
    	}
    	
    	check[x] = 1;
    	
    	for(int y=0; y<a[x].size(); y++) {
    		
    		int node = a[x].get(y);
    		
    		if(node == p) {
    			continue;
    		}
    		
    		int res = go(x,node);
    		
    		if(res == -2) {
    			return -2;
    		}
    		
    		if(res >=0) {
    			check[x] = 2;
    			
    			if(x == res) {
    				return -2;
    			} else {
    				return res;
    			}
    		}
    	}
    	
    	return -1;
    }
    
	
	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		a = new ArrayList[n];
		dist = new int[n];
		check = new int[n];
		
		for(int i=0; i<n; i++) {
			a[i] = new ArrayList<>();
		}
		
		for(int i=0; i<n; i++) {
			String str[] = br.readLine().split(" ");
			int u = Integer.parseInt(str[0]) -1;
			int v = Integer.parseInt(str[1]) -1;
			a[u].add(v);
			a[v].add(u);
		}
		
		go(-1,0);
		Queue<Integer> q = new LinkedList<>();
		
		for(int i=0; i<n; i++) {
			if(check[i] == 2) {
				dist[i] = 0;
				q.add(i);
			} else {
				dist[i] = -1;
			}
		}
		
		while(!q.isEmpty()) {
			int x = q.remove();
			
			for(int y = 0; y < a[x].size(); y++) {
				
				int node = a[x].get(y);
				
				if(dist[node] == -1) {
					q.add(node);
					dist[node] = dist[x]+1;
				}
				
			}
			
		}
		
		for(int i=0; i<n; i++) {
			bw.write(dist[i] + " ");
		}
		
		bw.write("\n");
		bw.flush();
		return;
	}
}
