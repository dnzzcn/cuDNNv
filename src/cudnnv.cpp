#include "cudnnv.h"
#include "ui_cudnnv.h"

#include <unistd.h>

#include "QDebug"
#include "QDir"
#include "QThread"
#include "QProcess"

#include "iostream"

QStringList versions;
int numberOfVersions = -1;

cuDNNv::cuDNNv(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::cuDNNv)
{
    ui->setupUi(this);

    connect(ui->switchButton, SIGNAL (released()), this, SLOT (switchHandle()), Qt::QueuedConnection);

    connect(&dropdownUpdater, SIGNAL(versionsUpdated(QStringList)), this, SLOT(updateList(QStringList)), Qt::QueuedConnection);

    dropdownUpdater.start();
}

void cuDNNv::updateList(QStringList itemList) {

    ui->comboBox->clear();

    for(int i = 0; i < itemList.size(); i++) {
        ui->comboBox->addItem(itemList[i]);
    }
}

void cuDNNv::switchHandle() {

    ui->switchButton->setEnabled(false);

    QString chosenVersion = dropdownUpdater.versionList[ui->comboBox->currentIndex()];

    QString chosenVersionName = dropdownUpdater.versionNameList[ui->comboBox->currentIndex()];

    QString statusMessage = "Switching to " + chosenVersionName;

    ui->statusLabel->setText(statusMessage);

    int e1 = QProcess::execute("mkdir packages/cudnn");

    QString tarCommandString = "tar xf packages/" + chosenVersion + " -C packages/cudnn --strip-components 1";

    QProcess::execute(tarCommandString);

    int e2 = QProcess::execute("rm -f /usr/include/cudnn.h");
    system("rm -f /usr/lib/x86_64-linux-gnu/*libcudnn*");
    system("rm -f /usr/local/cuda-*/lib64/*libcudnn*");

    int e5 = QProcess::execute("cp -P packages/cudnn/include/cudnn.h /usr/include");
    system("cp -P packages/cudnn/lib64/libcudnn* /usr/lib/x86_64-linux-gnu/");
    system("chmod a+r /usr/lib/x86_64-linux-gnu/libcudnn*");

    int e8 = QProcess::execute("rm -rf packages/cudnn");

    if(e1 != 0 || e2 != 0 || e5 != 0 || e8 != 0) {
        statusMessage = "Permission Error\n Please run cuDNNv with root permissions.";

        ui->statusLabel->setText(statusMessage);

        ui->switchButton->setEnabled(true);
    }
    else {
        statusMessage = "Succesfully switched to " + chosenVersionName;

        ui->statusLabel->setText(statusMessage);

        ui->switchButton->setEnabled(true);
    }

}

cuDNNv::~cuDNNv()
{
    delete ui;
}
