#ifndef DROPDOWNUPDATER_H
#define DROPDOWNUPDATER_H

#include "QThread"

class DropdownUpdater : public QThread
{
    Q_OBJECT
public:
    QStringList versionList;
    QStringList versionNameList;
signals:
    void versionsUpdated(QStringList versionList);

private:
    void run();
    void retrieveVersions();

    int numberOfVersions = -1;

public slots:
};

#endif // DROPDOWNUPDATER_H
