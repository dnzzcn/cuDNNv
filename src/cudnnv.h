#ifndef CUDNNV_H
#define CUDNNV_H

#include <QMainWindow>

#include "dropdownupdater.h"

namespace Ui {
class cuDNNv;
}

class cuDNNv : public QMainWindow
{
    Q_OBJECT

public:
    explicit cuDNNv(QWidget *parent = 0);
    ~cuDNNv();

public slots:
    void updateList(QStringList itemList);
    void switchHandle();

private:
    Ui::cuDNNv *ui;

    DropdownUpdater dropdownUpdater;
};

#endif // CUDNNV_H
