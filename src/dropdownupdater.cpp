#include "dropdownupdater.h"

#include <unistd.h>

#include "QDir"
#include "QDebug"

void DropdownUpdater::run()
{
    retrieveVersions();
}

void DropdownUpdater::retrieveVersions() {

    QString sourcePath = "packages/";
    QString targetPath = "/home/deniz/arge/build/build-cuDNNv-Desktop_Qt_5_10_0_GCC_64bit-Debug/target/";

    QDir sourceDir(sourcePath);

    while(true) {
        sleep(1);

        QStringList checkList;

        checkList = sourceDir.entryList(QStringList() << "*.tgz", QDir::Files);

        if(checkList.size() != numberOfVersions) {
            versionList.clear();
            versionNameList.clear();

            versionList = sourceDir.entryList(QStringList() << "*.tgz", QDir::Files);

            numberOfVersions = versionList.size();

            for(int i = 0; i < numberOfVersions; i++) {
                QString versionName = versionList[i];

                QStringList splitVersion = versionName.split("-");

                if(splitVersion.size() == 5) {
                    QString CUDAVersion = splitVersion[1];
                    QString cuDNNVersion = splitVersion.last();

                    QStringList cuDNNVersionList = cuDNNVersion.split(".");
                    cuDNNVersionList.removeLast();
                    cuDNNVersion = cuDNNVersionList.join(".");

                    QString version = cuDNNVersion + " - CUDA " + CUDAVersion;

                    versionNameList.append(version);
                }
            }

            emit versionsUpdated(versionNameList);
        }
    }


}
