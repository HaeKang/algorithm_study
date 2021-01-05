import java.io.*;

public class study_1012 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int[][] arr = new int[51][51];
	static boolean[][] check = new boolean[51][51];
	static final int[] dx = {0,0,-1,1};
	static final int[] dy = {-1,1,0,0};
	static int n,m,t,k;
	
	public static void dfs(int x, int y) {
		check[x][y] = true;
		
		for(int i=0; i<4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(nx <0 || ny < 0 || nx >=n || ny >= m) {
				continue;
			}
			
			if(arr[nx][ny] == 1 && !check[nx][ny]) {
				dfs(nx,ny);
			}
		}
	}
	
	public static void init_arr(int n, int m) {
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				arr[i][j] = 0;
				check[i][j] = false;
			}
		}
	}

	
	public static void main(String[] args) throws IOException{
		t = Integer.parseInt(br.readLine());
		
		for(int tc=0; tc<t; tc++) {
			String[] str = br.readLine().split(" ");
			n = Integer.parseInt(str[0]);
			m = Integer.parseInt(str[1]);
			k = Integer.parseInt(str[2]);
			int ans = 0;
			
			init_arr(n,m);
			
			for(int i=0; i<k; i++) {
				String[] str2 = br.readLine().split(" ");
				int x = Integer.parseInt(str2[0]);
				int y = Integer.parseInt(str2[1]);
				arr[x][y] = 1;
			}
			
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if(arr[i][j] == 1 && !check[i][j]) {
						ans++;
						dfs(i,j);
					}
				}
			}
			
			bw.write(ans + "\n");
		}
		
		bw.flush();
	}
	
}
