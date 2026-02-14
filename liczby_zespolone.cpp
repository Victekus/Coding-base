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
int main() {
    LiczbaZespolona z1(3, 4);   // 3 + 4i
    LiczbaZespolona z2(1, 2);   // 1 + 2i
    
    cout << "Liczba 1: ";
    z1.wyswietl();
    cout << "\n";
    
    cout << "Liczba 2: ";
    z2.wyswietl();
    cout << "\n";
    
    return 0;
}
