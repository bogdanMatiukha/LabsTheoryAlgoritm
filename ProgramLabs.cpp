#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double distance(double x1, double y1, double z1,
    double x2, double y2, double z2)
{
    return sqrt(
        pow(x2 - x1, 2) +
        pow(y2 - y1, 2) +
        pow(z2 - z1, 2)
    );
}

double inputNumber()
{
    double number;

    while (!(cin >> number))
    {
        cout << "Invalid input! Please enter a number: ";
        cin.clear();
        cin.ignore(1000, '\n');
    }

    return number;
}

int main()
{
    double xA1, yA1, zA1;
    double xB1, yB1, zB1;
    double xC1, yC1, zC1;
    double xA2, yA2, zA2;

    cout << "Enter coordinates of A1:" << endl;
    xA1 = inputNumber();
    yA1 = inputNumber();
    zA1 = inputNumber();

    cout << "Enter coordinates of B1:" << endl;
    xB1 = inputNumber();
    yB1 = inputNumber();
    zB1 = inputNumber();

    cout << "Enter coordinates of C1:" << endl;
    xC1 = inputNumber();
    yC1 = inputNumber();
    zC1 = inputNumber();

    cout << "Enter coordinates of A2:" << endl;
    xA2 = inputNumber();
    yA2 = inputNumber();
    zA2 = inputNumber();

    double a = distance(xA1, yA1, zA1, xB1, yB1, zB1);
    double b = distance(xB1, yB1, zB1, xC1, yC1, zC1);
    double c = distance(xA1, yA1, zA1, xA2, yA2, zA2);

    double total_length = 4 * (a + b + c);

    cout << fixed << setprecision(2);
    cout << "Total length of all edges = " << total_length << endl;

    return 0;
}