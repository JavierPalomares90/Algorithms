#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main(){
  ifstream infile;
  infile.open("median.txt",std::ifstream::in);
  int medianSum;
  int median = 20000;
  int i;
  char temp[256];
  int k=0;
  vector<int> heapLow;
  vector<int> heapHigh;
  make_heap(heapLow.begin(),heapHigh.end());
  make_heap(heapHigh.begin(),heapHigh.end());
  while(infile.good()){
    infile.getline(temp,256);
    i = atoi(temp);
    nums.push_back(i);
    k++;
  }

}
