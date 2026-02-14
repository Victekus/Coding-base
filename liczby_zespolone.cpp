#include <iostream>
using namespace std;
class LiczbaZespolona {
private:
    double rzeczywista;  // Część rzeczywista (a)
    double urojona;      // Część urojona (b)
    
public:
    // KONSTRUKTOR
    LiczbaZespolona(double r = 0, double u = 0) {
        rzeczywista = r;
        urojona = u;
    }
 double getRzeczywista() { return rzeczywista; }
    double getUrojona() { return urojona; }
    
    // WYŚWIETLANIE
    void wyswietl() {
        if (urojona >= 0)
            cout << rzeczywista << " + " << urojona << "i";
        else
            cout << rzeczywista << " - " << (-urojona) << "i";
    }
};    

