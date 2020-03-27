package study_0324;
import java.io.*;
import java.util.*;

class Edge{
	int from, to;
	Edge(int from, int to){
		this.from = from;
		this.to = to;
	}
}

public class study_13023 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void main(String[] args) throws IOException{
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int m = Integer.parseInt(str[1]);
		boolean[][] a = new boolean[n][n];
		ArrayList<Integer>[] g = (ArrayList<Integer>[]) new ArrayList[n];	// 배열안에 벡터같은 느낌
		ArrayList<Edge> edges = new ArrayList<Edge>();
		
		for(int i=0; i<n; i++) {
			g[i] = new ArrayList<Integer>();
		}
		
		for(int i=0; i<m; i++) {
			String[] str2 = br.readLine().split(" ");
			int from = Integer.parseInt(str2[0]);
			int to = Integer.parseInt(str2[1]);
			edges.add(new Edge(from, to));
			edges.add(new Edge(to,from));
			
			a[from][to] = a[to][from] = true;
			
			g[from].add(to);
			g[to].add(from);
			
		}
		
		 m *= 2;
	     for  (int i=0; i<m; i++) {
	        for (int j=0; j<m; j++) {
	                int A = edges.get(i).from;
	                int B = edges.get(i).to;
	                int C = edges.get(j).from;
	                int D = edges.get(j).to;
	                if (A == B || A == C || A == D || B == C || B == D || C == D) {
	                    continue;
	                }
	                if (!a[B][C]) continue;
	                for (int E : g[D]) {
	                    if (A == E || B == E || C == E || D == E) {
	                        continue;
	                    }
	                    bw.write("1\n");
	                    bw.flush();
	                    return;
	                }
	            }
	       }
	        
	    bw.write("0\n");	
		bw.flush();
	}
}
