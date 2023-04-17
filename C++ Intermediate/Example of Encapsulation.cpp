#include <iostream>
using namespace std;

//class definition
class Car{
    
    //private area
    private:
        int horsepowers;

    //public area
    public:
        //complete the setter function
        void setHorsepowers(int a) {
            horsepowers = a;
        }
    
        //complete the getter function
        int getHorsepowers() {
            if (horsepowers > 800){
                cout<<"Too much"<<endl;
            }
            return horsepowers;
        }
        

};


int main() {
    //getting input
    int horsepowers;
    cin >> horsepowers;
    //creating the object of class Car
    Car car;
    car.setHorsepowers(horsepowers);
    cout << car.getHorsepowers();

    return 0;
}