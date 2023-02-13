package 최솟값찾기;

import java.io.*;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class 최솟값찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        Deque<Node> deque = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            int tmp = Integer.parseInt(st.nextToken());

            while (!deque.isEmpty() && deque.getLast().value > tmp) {
                deque.removeLast();
            }
            deque.addLast(new Node(i, tmp));

            if (deque.getFirst().idx <= i -L) {
                deque.removeFirst();
            }

            bw.write(deque.getFirst().value + " ");
        }

        bw.flush();
        bw.close();
    }

    static class Node {
        public int idx;
        public int value;

        Node(int idx, int value) {
            this.idx = idx;
            this.value = value;
        }
    }
}


/*
input:
12 3
1 5 2 3 6 2 3 7 3 5 2 6

output:
1 1 1 2 2 2 2 2 3 3 2 2
*/
