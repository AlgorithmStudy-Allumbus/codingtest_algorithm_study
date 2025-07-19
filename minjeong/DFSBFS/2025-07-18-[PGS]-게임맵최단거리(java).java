import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;

        // 방문여부 리스트
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;

        // 방향 벡터 만들기
        int[][] dirs ={{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

        // 큐 선언
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});

        // BFS 탐색
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            for (int[] dir : dirs) {
                int nx = x + dir[0];
                int ny = y + dir[1];

                if ((0 <= nx && nx < n && 0 <= ny && ny < m)
                    && !visited[nx][ny]
                    && maps[nx][ny] == 1) {
                    maps[nx][ny] = maps[x][y] + 1;
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny});
                }
            }
        }

        if (maps[n-1][m-1] != 1) {
            return maps[n-1][m-1];
        }
        return -1;
    }
}