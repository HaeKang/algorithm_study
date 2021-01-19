import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class study_1697 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static final int MAX = 100001;
	static int n,k;
	static boolean[] visit = new boolean[MAX];
	static int[] dis = new int[MAX];
			
	public static void init_arr() {
		for(int i=0; i<MAX; i++) {
			visit[i] = false;
			dis[i] = 0;
		}
	}
	
	public static void bfs(int start, int end) throws IOException {
		Queue<Integer> q = new LinkedList<>();
		q.add(start);
		visit[start] = true;
		
		while(!q.isEmpty()) {
			int x = q.remove();
			int distance = dis[x];
			
			if(x == end) {
				bw.write(String.valueOf(distance) + "\n");
				bw.flush();
				return;
			}
			
			if(x - 1 >= 0 && !visit[x-1]) {
				q.add(x-1);
				visit[x-1] = true;
				dis[x-1] = distance + 1;
			}
			
			if(x + 1 <MAX && !visit[x+1]) {
				q.add(x+1);
				visit[x+1] = true;
				dis[x+1] = distance + 1;
			}
			
			if(x * 2 < MAX && !visit[x*2]) {
				q.add(x*2);
				visit[x*2] = true;
				dis[x*2] = distance + 1;
			}
			
		}
		
	}
	
	
	public static void main(String args[]) throws IOException{
		String[] str = br.readLine().split(" ");
		n = Integer.parseInt(str[0]);
		k = Integer.parseInt(str[1]);
		
		init_arr();
		
		bfs(n,k);

	}
}
