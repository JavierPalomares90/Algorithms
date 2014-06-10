#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#define N 875714
using namespace std;

struct node{
  bool visited;
  int leader;
  int finish;
  vector<int> linkedVertices;
  vector<int> rLinkedVertices;
};

struct node G[N+1];
struct node newG[N+1];

int t=0;
int s=0;
void dfs(node G[], int i, bool reverse){
  G[i].visited=true;
  G[i].leader=s;
  vector<int> next;
  if (reverse) next= G[i].rLinkedVertices;
  else next= G[i].linkedVertices;
  for(int j=0; j<next.size(); j++){
    if(!G[next[j]].visited) {
      dfs(G, next[j], reverse);
    }
  }
  t++;
  G[i].finish=t;    
}

void dfs_loop(node G[], bool reverse){
  t=0;
  s=0;
  for(int i=N;i>0;--i){
    if (!G[i].visited){
      s=i;
      dfs(G,i,reverse);
    }
  }
}

int main(){
  for(int i=1;i<=N;++i){
    G[i].visited=false;
  }

  FILE* fp=freopen("SCC.txt","r",stdin);
  int head, tail;
  while (scanf("%d %d", &head, &tail) > 0) {
    G[head].linkedVertices.push_back(tail);
    G[tail].rLinkedVertices.push_back(head);
  }
  fclose(fp);

  dfs_loop(G, true);//FIRST LOOP

  for(int i=1;i<=N;++i){
    newG[i].visited=false;
    newG[i].finish=0;
    newG[i].leader=0;
    vector<int> temp;
    for(int j=0; j< G[i].linkedVertices.size(); j++){
      temp.push_back(G[G[i].linkedVertices[j]].finish);
    }
    newG[G[i].finish].linkedVertices=temp;
  }

  dfs_loop(newG,false);//SECOND LOOP

  ofstream ofs("stat.txt", ofstream::out);    
  for (int k=1;k<=N;k++) ofs<< newG[k].leader<<endl;
  ofs.close();
  return 0;
}
