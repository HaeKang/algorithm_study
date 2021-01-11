import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static final int MAX = 102;
	static final int INF = 987654321;
	
	static int n,m, person;
	static int result = INF;
	static int[][] v = new int[MAX][MAX];
	
	
	static public void kevin() {
		for(int k =1; k<=n; k++) {
			for(int i=1; i<=n; i++) {
				for(int j=1; j<=n; j++) {
					if(i == j) {
						continue;
					} else if(v[i][k] != 0 && v[k][j] != 0) {
						if(v[i][j] == 0) {
							v[i][j] = v[i][k] + v[k][j];
						} else {
							if(v[i][j] > v[i][k] + v[k][j]) {
								v[i][j] = v[i][k] + v[k][j];
							}
						}
					}
				}
			}
		}
	}
	
	static public void init() {
		for(int i=0; i<MAX; i++) {
			for(int j=0; j<MAX; j++) {
				v[i][j] = 0;
			}
		}
	}
	
	static public void main(String args[]) throws IOException{
		String[] str = br.readLine().split(" ");
		n = Integer.parseInt(str[0]);
		m = Integer.parseInt(str[1]);
		
		init();
		
		for(int i=0; i<m; i++) {
			String[] str2 = br.readLine().split(" ");
			int x,y;
			x = Integer.parseInt(str2[0]);
			y = Integer.parseInt(str2[1]);
			v[x][y] = 1;
			v[y][x] = 1;
			
		}
		
		kevin();
		
		
		for(int i=1; i<=n; i++) {
			int sum = 0;
			for(int j=1; j<=n; j++) {
				sum += v[i][j];
			}
			if(result > sum) {
				result = sum;
				person = i;
			}
			
		}
		
		bw.write(String.valueOf(person));
		bw.flush();
		
	}
	
}
