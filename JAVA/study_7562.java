package study_0324;

import java.util.*;
import java.io.*;

public class study_7562 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static final int[] dx = {-2,-1,1,2,2,1,-1,-2};
    static final int[] dy = {1,2,2,1,-1,-2,-2,-1};
    
    public static void main(String[] args) throws IOException {
    	
    	int t = Integer.parseInt(br.readLine());
    	
    	while(t-- > 0) {
    		int n = Integer.parseInt(br.readLine());
    		
    		String[] str1 = br.readLine().split(" ");
    		int sx = Integer.parseInt(str1[0]);
    		int sy = Integer.parseInt(str1[1]);
    		
    		String[] str2 = br.readLine().split(" ");
    		int ex = Integer.parseInt(str2[0]);
    		int ey = Integer.parseInt(str2[1]);
    		
    		int[][] d = new int[n][n];
    		
    		for(int i=0; i<n; i++) {
    			Arrays.fill(d[i], -1);
    		}
    		
    		Queue<Integer> q = new LinkedList<>();
    		
    		q.add(sx);
    		q.add(sy);
    		d[sx][sy] = 0;
    		
    		while(!q.isEmpty()) {
    			int x = q.remove();
    			int y = q.remove();
    			for(int k = 0; k <8; k++) {
    				int nx = x + dx[k];
    				int ny = y + dy[k];
    				if (0 <= nx && nx < n && 0 <= ny && ny < n) {
    					if(d[nx][ny] == -1) {
    						d[nx][ny] = d[x][y] + 1;
    						q.add(nx);
    						q.add(ny);
    					}
    				}
    			}
    		}
    		
    		String ans = Integer.toString(d[ex][ey]);
    		bw.write(ans + "\n");
    		bw.flush();
    	}
    }
	
}
