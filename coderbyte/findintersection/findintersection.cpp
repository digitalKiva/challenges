#include <iostream>
#include <string>
using namespace std;

string FindIntersection(string strArr[], int arrLength) {
  
  string a=strArr[0];
  string b=strArr[1];
  int ad, bd;
  int bdr=0;
  string result="";

  for(int ia=0; ia < a.length(); ) {
    if (a.find(",", ia) != string::npos) {
      ad = stoi(a.substr(ia, a.find(",", ia)));
      ia = a.find(",", ia)+1;
    } else {
      ad = stoi(a.substr(ia));
      ia = a.length();
    }
    for(int ib=bdr; ib < b.length(); ) {
      if (b.find(",", ib) != string::npos) {
        bd = stoi(b.substr(ib, b.find(",", ib)));
        ib = b.find(",", ib)+1;
      } else {
        bd = stoi(b.substr(ib));
        ib = b.length();
      }
      if (ad == bd) {
        result.append(to_string(ad) + ",");
        bdr = ib;
        break;
      } else if (ad < bd) {
        break;
      } else {
        bdr = ib;
      }
    }
  }

  if (result.empty()) {
    return "false";
  }
  result = result.erase(result.length()-1);
  return result;
}

int main(void) { 
   
  // keep this function call here
  string A[] = coderbyteInternalStdinFunction(stdin);
  int arrLength = sizeof(A) / sizeof(*A);
  cout << FindIntersection(A, arrLength);
  return 0;
    
}