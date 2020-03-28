package study_0328;
import java.util.*;
import java.io.*;

class Node{
	int left, right;
	Node(int left, int right){
		this.left = left;
		this.right = right;
	}
}
public class study_1991 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	static void preorder(Node[] a, int x) {
        if (x == -1) return;
        System.out.print((char)(x+'A'));
        preorder(a,a[x].left);
        preorder(a,a[x].right);
    }
    static void inorder(Node[] a, int x) {
        if (x == -1) return;
        inorder(a,a[x].left);
        System.out.print((char)(x+'A'));
        inorder(a,a[x].right);
    }
    static void postorder(Node[] a, int x) {
        if (x == -1) return;
        postorder(a,a[x].left);
        postorder(a,a[x].right);
        System.out.print((char)(x+'A'));
    }
    
    public static void main(String[] args) throws IOException{
    	int n = Integer.parseInt(br.readLine());
    	Node[] a = new Node[26];
    	
    	for (int i=0; i<n; i++) {
    		String str = br.readLine();
    		str = str.replaceAll(" ", "");
    		
    		char str2[] = str.toCharArray();
      		
            int x = str2[0] - 'A';
            char y = str2[1];
            char z = str2[2];
            
            
            int left = -1;
            int right = -1;
            
            if (y != '.') {
                left = y-'A';
            }
            if (z != '.') {
                right = z-'A';
            }
            a[x] = new Node(left, right);
        }
    	
        preorder(a,0);
        System.out.println();
        
        inorder(a,0);
        System.out.println();
        
        postorder(a,0);
        System.out.println();
    	
    }
    
}
