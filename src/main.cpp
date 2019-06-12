#include "cudnnv.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    cuDNNv window;
    window.show();

    return a.exec();
}
