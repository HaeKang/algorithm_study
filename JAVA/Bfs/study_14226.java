package study_0327;
import java.util.*;
import java.io.*;

public class study_14226 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException {
		int n = Integer.parseInt(br.readLine());
		int[][] d = new int[n+1][n+1];
		
		for(int i=0; i<=n; i++) {
			Arrays.fill(d[i], -1);
		}
		
		Queue<Integer> q= new LinkedList<Integer>();
		q.add(1);	// 화면 개수
		q.add(0);	// 클립보드 개수
		
		d[1][0] = 0;
		
		while(!q.isEmpty()) {
			int s = q.remove();
			int c = q.remove();
			
			// 복사
			if(d[s][s] == -1) {
				d[s][s] = d[s][c] + 1;
				q.add(s);
				q.add(s);
			}
			
			// 클립보드
			if (s+c <= n && d[s+c][c] == -1) {
                d[s+c][c] = d[s][c] + 1;
                q.add(s+c); 
                q.add(c);
            }
			
			//삭제
			if (s-1 >= 0 && d[s-1][c] == -1) {
                d[s-1][c] = d[s][c] + 1;
                q.add(s-1); 
                q.add(c);
            }
		}
		
		int ans = -1;
        for (int i=0; i<=n; i++) {
            if (d[n][i] != -1) {
                if (ans == -1 || ans > d[n][i]) {
                    ans = d[n][i];
                }
            }
        }
        bw.write(ans+"\n");
		bw.flush();
	}
}
