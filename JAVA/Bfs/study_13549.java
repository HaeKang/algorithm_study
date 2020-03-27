package study_0327;
import java.util.*;
import java.io.*;

public class study_13549 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	public static final int MAX = 1000000;
	
	public static void main(String[] args) throws IOException{	
		String[] str1 = br.readLine().split(" ");
		int n = Integer.parseInt(str1[0]);
		int m = Integer.parseInt(str1[1]);
		
		boolean[] c = new boolean[MAX];
        int[] d = new int[MAX];
        c[n] = true;
        d[n] = 0;
        
        Queue<Integer> q = new LinkedList<Integer>();
        Queue<Integer> next_q = new LinkedList<Integer>();
        
        q.add(n);
        
        while(!q.isEmpty()) {
        	int now = q.remove();
        	
        	if (now * 2 < MAX) {
    			if (c[now * 2] == false) {
    				q.add(now * 2);
    				c[now * 2] = true;
    				d[now * 2] = d[now];
    			}
    		}

    		if (now - 1 >= 0) {
    			if (c[now - 1] == false) {
    				next_q.add(now - 1);
    				c[now - 1] = true;
    				d[now - 1] = d[now] + 1;
    			}
    		}

    		if (now + 1 < MAX) {
    			if (c[now + 1] == false) {
    				next_q.add(now + 1);
    				c[now + 1] = true;
    				d[now + 1] = d[now] + 1;
    			}
    		}

    		// 현재큐 바꿔줌
    		if (q.isEmpty()) {
    			q = next_q;
    			next_q = new LinkedList<Integer>();
    		}
        	
        }
		
        bw.write(d[m] + "\n");
		bw.flush();
	}
	
}
