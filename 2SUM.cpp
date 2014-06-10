#include <iostream>
#include <map>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main(){
  map<int,bool> myMap;
  ifstream infile;
  infile.open("2sum.txt",std::ifstream::in);
  int i=0;
  string str = "";
  while(infile.good()){
    getline(infile,str);
    i = atoi(str.c_str());
    myMap.insert(pair<int,bool>(i,false));
  }
  infile.close();
  int counts = 0;
  
  for(int t=-10000;t<=10000;t++){
    // Iterate over all of the keys in the map
    map<int,bool>::iterator it;
    for(it=myMap.begin();it!=myMap.end();++it){
      int x = it->first;
      int y = t-x;
      if(x!=y && myMap.find(y)!=myMap.end()){
	counts++;
	cout <<t<<counts<<endl;
	break;
      }

    }
  }
  cout<< "The answer is "<<counts<<endl;
  return 0;
}
