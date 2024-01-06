#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdlib>
using namespace std;

int limit;
int v;
vector<int> *adj_list;
vector<int> stack;

void create_graph(){
    adj_list = (vector<int> *)malloc(sizeof(vector<int>)*v);
}
int find(int k){

        if(stack.size() == 0){
              return 0;
        }

        int flag = 0;
        for(int i = 0;i < stack.size();i++){
                    if(stack[i] == k){
                          flag = 1;
                          break;
                    }
        }
        if(flag){
          return 1;
        }
        else{
          return 0;
        }
}

void add_edge(int v1,int v2){
       adj_list[v1].push_back(v2);
}
void dfs(int vertex,int count){

        int j;
        cout<<vertex<<" ";
        if(stack.empty()){
                stack.push_back(vertex);
        }
        for(int i = 0;i < (adj_list[vertex]).size();i++){
                if(!(find((adj_list[vertex])[i]))){

                          stack.push_back((adj_list[vertex])[i]);

                          if(count <= limit){
                                dfs((adj_list[vertex])[i],count+1);
                          }
                          else{
                            stack.pop_back();
                            return;
                          }
                }
        }
}
int main( ){

  cout<<"Enter the value for limit :=";
  cin>>limit;
  cout<<"Enter the number of nodes in the graph := ";
  cin>>v;
  create_graph();
  int temp = 0;
  while(temp != -1){
        int v1,v2;
        char ch;
        cout<<"Enter thr vertices across which edge is to be added := ";
        cin>>v1>>v2;
        add_edge(v1,v2);

        cout<<"Quit?? (y/n)"<<endl;
        cin>>ch;
        if(ch == 'y'){
          break;
        }
        else{
          continue;
        }
  }
  cout<<"Enter the vertex from which you wanna start the dfs := ";

  int v0;
  cin>>v0;
  dfs(v0,1);

  cout<<endl;
  return 0;
}
