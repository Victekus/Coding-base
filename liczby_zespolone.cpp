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
	LiczbaZespolona operator+(const LiczbaZespolona& druga) {
        // Dodajemy rzeczywiste do rzeczywistych, urojone do urojonych
        return LiczbaZespolona(this->rzeczywista + druga.rzeczywista, 
                               this->urojona + druga.urojona);
	}
	LiczbaZespolona operator-(const LiczbaZespolona& druga) {
        // Dodajemy rzeczywiste do rzeczywistych, urojone do urojonych
        return LiczbaZespolona(this->rzeczywista - druga.rzeczywista, 
                               this->urojona - druga.urojona);	
    }
	LiczbaZespolona operator*(const LiczbaZespolona& druga) {
    return LiczbaZespolona(
        (this->rzeczywista * druga.rzeczywista) - (this->urojona * druga.urojona), // Nowa rzeczywista
        (this->rzeczywista * druga.urojona) + (this->urojona * druga.rzeczywista)  // Nowa urojona
    );
}
};    
int main() {
	double tab1[4];
	for (int x=0 ; x<4; x++){
		if (x%2==0){
			cout<<"podajesz część rzeczywistą"<<endl;
			cin >> tab1[x];
		}
		else {
			cout<<"podajesz częśc urojoną"<<endl;
			cin>>tab1[x];
		}
	}
    LiczbaZespolona z1(tab1[0],tab1[1]);   // 3 + 4i
    LiczbaZespolona z2(tab1[2], tab1[3]);   // 1 + 2i
    // Używamy naszego przeciążonego operatora!
    LiczbaZespolona z3 = z1 + z2; 
	LiczbaZespolona z4 = z1 * z2;
	LiczbaZespolona z5 = z1 - z2;
	LiczbaZespolona z6 = z2 - z1;

    cout << "Liczba 1: "; z1.wyswietl(); cout << endl;
    cout << "Liczba 2: "; z2.wyswietl(); cout << endl;
    cout << "Suma (z1 + z2): "; z3.wyswietl(); cout << endl;
	cout << "Iloczyn (z1*z2):"; z4.wyswietl(); cout << endl;
	cout << "Różnica (z1-z2):" ; z5.wyswietl(); cout <<endl;
	cout << "Różnica (z2-z1):" ; z6.wyswietl(); cout <<endl;
    return 0;
}
