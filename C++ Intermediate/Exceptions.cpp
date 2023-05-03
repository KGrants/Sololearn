#include <iostream>
using namespace std;

int main() {
   string name;
   cin >> name;
   try {
      if (name.size() < 4 or name.size() > 20)
         throw 9;
      cout << "Valid"; 
   }
   catch(int x) {
      cout << "Invalid";
   }
   
   return 0;
}