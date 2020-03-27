package study_0327;
import java.util.*;
import java.io.*;

public class study_13913 {
	public static final int MAX  = 1000000;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException{
		String[] str1 = br.readLine().split(" ");
		int n = Integer.parseInt(str1[0]);
		int m = Integer.parseInt(str1[1]);
		
		boolean[] check = new boolean[MAX];
		int[] dist = new int[MAX];
		int[] from = new int[MAX];
		
		check[n] = true;
		dist[n] = 0;
		
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(n);
		
		while(!q.isEmpty()) {
			int now = q.remove();
			
			if (now-1 >= 0) {
                if (check[now-1] == false) {
                    q.add(now-1);
                    check[now-1] = true;
                    dist[now-1] = dist[now] + 1;
                    from[now-1] = now;
                }
            }
			
			if (now+1 < MAX) {
                if (check[now+1] == false) {
                    q.add(now+1);
                    check[now+1] = true;
                    dist[now+1] = dist[now] + 1;
                    from[now+1] = now;
                }
            }
			
			if (now*2 < MAX) {
                if (check[now*2] == false) {
                    q.add(now*2);
                    check[now*2] = true;
                    dist[now*2] = dist[now] + 1;
                    from[now*2] = now;
                }
            }
					
		}
		
		bw.write(dist[m]+"\n");
		
		Stack<Integer> ans = new Stack<>();
		
		for(int i=m; i!=n; i=from[i]) {
			ans.push(i);
		}
		ans.push(n);
		
		while(!ans.isEmpty()) {
			bw.write(ans.pop()+" ");
		}
		
		bw.write("\n");
		bw.flush();
	}
}
