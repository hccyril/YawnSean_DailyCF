import java.io.*;
import java.util.StringTokenizer;

public class Main {

    private static char[] ch = new char[26];

    static {
        for (int i = 0; i < 26; i++)
            ch[i] = (char) ('A' + i);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            if (1 == n) {
                pw.println("A");
                continue;
            } else if (2 == n) {
                pw.println("AB");
                continue;
            }
            StringBuilder sb = new StringBuilder();
            boolean[] visited = new boolean[n];
            if ((n & 1) == 1) {
                sb.append(ch[n / 2]);
                visited[n / 2] = true;
            }
            sb.append(ch[n / 2 - 1]);
            visited[n / 2 - 1] = true;
            for (int i = n - 1; i >= 0; i--) {
                if (!visited[i])
                    sb.append(ch[i]);
            }
            pw.println(new String(sb));
        }
        pw.close();
    }
}
