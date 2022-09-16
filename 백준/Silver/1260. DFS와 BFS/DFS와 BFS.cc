#include <iostream>
#include <queue>
#define MAX 1001
using namespace std;

int N, E, START;
bool graph[MAX][MAX];
bool visited[MAX];
queue<int> q;

void DFS(int start) {
    visited[start] = true;
    cout << start << " ";

    for (int i = 1; i <= N; i++) {
        if (graph[start][i] == true && visited[i] == false) {
            DFS(i);
        }
    }
}

void BFS(int start) {
    q.push(start);
    visited[start] = true;
    cout << start << " ";

    while (!q.empty()) {
        start = q.front();
        q.pop();

        for (int i = 1; i <= N; i++) {
            if (graph[start][i] == true && visited[i] == false) {
                q.push(i);
                visited[i] = true;
                cout << i << " ";
            }
        }
    }
}

int main() {
    cin >> N >> E >> START;

    for (int i = 0; i < E; i++)
    {
        int u, v;
        cin >> u >> v;
        graph[u][v] = true;
        graph[v][u] = true;
    }
    
    DFS(START);

    for (int i = 0; i <= N; i++)
        visited[i] = false;
    
    cout << '\n';

    BFS(START);

    return 0;
}