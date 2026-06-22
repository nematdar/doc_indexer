<!-- Source: https://doc.qt.io/qtforpython-6/api.html -->
# Modules API[Â¶](#modules-api "Link to this heading")
## Basic modules[Â¶](#basic-modules "Link to this heading")
These are the main modules that help you build a Widget-based UI.
[`Qt Core`](PySide6/QtCore/index.html#module-PySide6.QtCore "PySide6.QtCore")
Core non-graphical classes used by other modules.
[`Qt GUI`](PySide6/QtGui/index.html#module-PySide6.QtGui "PySide6.QtGui")
Base classes for graphical user interface (GUI) components.
[`Qt Widgets`](PySide6/QtWidgets/index.html#module-PySide6.QtWidgets "PySide6.QtWidgets")
Classes to extend Qt GUI with Python widgets.
## QML and Qt Quick[Â¶](#qml-and-qt-quick "Link to this heading")
Use these modules to interact with the [QML Language](https://doc.qt.io/qt-6/qmlapplications.html),
from Python.
[`Qt Qml`](PySide6/QtQml/index.html#module-PySide6.QtQml "PySide6.QtQml")
Classes for QML and JavaScript languages.
[`Qt Quick`](PySide6/QtQuick/index.html#module-PySide6.QtQuick "PySide6.QtQuick")
A declarative framework for building highly dynamic applications
with custom UIs.
[`Qt Quick Controls`](PySide6/QtQuickControls2/index.html#module-PySide6.QtQuickControls2 "PySide6.QtQuickControls2")
Lightweight QML types for creating performant user interfaces for
desktop, embedded, and mobile devices.
[`Qt Quick Widgets`](PySide6/QtQuickWidgets/index.html#module-PySide6.QtQuickWidgets "PySide6.QtQuickWidgets")
Provides a Python widget class for displaying a Qt Quick user interface.
## All the modules[Â¶](#all-the-modules "Link to this heading")
There are many other modules currently supported by PySide6, here you can find a complete list
of them.
* [Qt Modules Supported by Qt for Python](modules.html)
---
<!-- Source: https://doc.qt.io/qtforpython-6/PySide6/QtCore/index.html#module-PySide6.QtCore -->
# PySide6.QtCore[Â¶](#pyside6-qtcore "Link to this heading")
* [Functions](QtCore_globals.html)
* [Enumerations](QtCore_globals.html#enumerations)
* [PySide6.QtCore.QAbstractAnimation](QAbstractAnimation.html)
* [PySide6.QtCore.QAbstractEventDispatcher](QAbstractEventDispatcher.html)
* [PySide6.QtCore.QAbstractItemModel](QAbstractItemModel.html)
* [PySide6.QtCore.QAbstractListModel](QAbstractListModel.html)
* [PySide6.QtCore.QAbstractNativeEventFilter](QAbstractNativeEventFilter.html)
* [PySide6.QtCore.QAbstractProxyModel](QAbstractProxyModel.html)
* [PySide6.QtCore.QAbstractTableModel](QAbstractTableModel.html)
* [PySide6.QtCore.QAnimationGroup](QAnimationGroup.html)
* [PySide6.QtCore.QBasicMutex](QBasicMutex.html)
* [PySide6.QtCore.QBasicReadWriteLock](QBasicReadWriteLock.html)
* [PySide6.QtCore.QBasicTimer](QBasicTimer.html)
* [PySide6.QtCore.QBitArray](QBitArray.html)
* [PySide6.QtCore.QBluetoothPermission](QBluetoothPermission.html)
* [PySide6.QtCore.QBuffer](QBuffer.html)
* [PySide6.QtCore.QByteArray](QByteArray.html)
* [PySide6.QtCore.QByteArrayMatcher](QByteArrayMatcher.html)
* [PySide6.QtCore.QCalendar](QCalendar.html)
* [PySide6.QtCore.QCalendarPermission](QCalendarPermission.html)
* [PySide6.QtCore.QCameraPermission](QCameraPermission.html)
* [PySide6.QtCore.QCborArray](QCborArray.html)
* [PySide6.QtCore.QCborError](QCborError.html)
* [PySide6.QtCore.QCborMap](QCborMap.html)
* [PySide6.QtCore.QCborParserError](QCborParserError.html)
* [PySide6.QtCore.QCborStreamReader](QCborStreamReader.html)
* [PySide6.QtCore.QCborStreamWriter](QCborStreamWriter.html)
* [PySide6.QtCore.QCborStringResultByteArray](QCborStringResultByteArray.html)
* [PySide6.QtCore.QCborStringResultString](QCborStringResultString.html)
* [PySide6.QtCore.QCborValue](QCborValue.html)
* [PySide6.QtCore.QChildEvent](QChildEvent.html)
* [PySide6.QtCore.QCollator](QCollator.html)
* [PySide6.QtCore.QCollatorSortKey](QCollatorSortKey.html)
* [PySide6.QtCore.QCommandLineOption](QCommandLineOption.html)
* [PySide6.QtCore.QCommandLineParser](QCommandLineParser.html)
* [PySide6.QtCore.QConcatenateTablesProxyModel](QConcatenateTablesProxyModel.html)
* [PySide6.QtCore.QContactsPermission](QContactsPermission.html)
* [PySide6.QtCore.QCoreApplication](QCoreApplication.html)
* [PySide6.QtCore.QCryptographicHash](QCryptographicHash.html)
* [PySide6.QtCore.QDataStream](QDataStream.html)
* [PySide6.QtCore.QDate](QDate.html)
* [PySide6.QtCore.QDateTime](QDateTime.html)
* [PySide6.QtCore.QDeadlineTimer](QDeadlineTimer.html)
* [PySide6.QtCore.QDir](QDir.html)
* [PySide6.QtCore.QDirIterator](QDirIterator.html)
* [PySide6.QtCore.QDirListing](QDirListing.html)
* [PySide6.QtCore.QDynamicPropertyChangeEvent](QDynamicPropertyChangeEvent.html)
* [PySide6.QtCore.QEasingCurve](QEasingCurve.html)
* [PySide6.QtCore.QElapsedTimer](QElapsedTimer.html)
* [PySide6.QtCore.QEvent](QEvent.html)
* [PySide6.QtCore.QEventLoop](QEventLoop.html)
* [PySide6.QtCore.QFactoryInterface](QFactoryInterface.html)
* [PySide6.QtCore.QFile](QFile.html)
* [PySide6.QtCore.QFileDevice](QFileDevice.html)
* [PySide6.QtCore.QFileInfo](QFileInfo.html)
* [PySide6.QtCore.QFileSelector](QFileSelector.html)
* [PySide6.QtCore.QFileSystemWatcher](QFileSystemWatcher.html)
* [PySide6.QtCore.QFutureInterfaceBase](QFutureInterfaceBase.html)
* [PySide6.QtCore.QGenericArgument](QGenericArgument.html)
* [PySide6.QtCore.QGenericReturnArgument](QGenericReturnArgument.html)
* [PySide6.QtCore.QHashSeed](QHashSeed.html)
* [PySide6.QtCore.QIODevice](QIODevice.html)
* [PySide6.QtCore.QIODeviceBase](QIODeviceBase.html)
* [PySide6.QtCore.QIdentityProxyModel](QIdentityProxyModel.html)
* [PySide6.QtCore.QItemSelection](QItemSelection.html)
* [PySide6.QtCore.QItemSelectionModel](QItemSelectionModel.html)
* [PySide6.QtCore.QItemSelectionRange](QItemSelectionRange.html)
* [PySide6.QtCore.QJsonArray](QJsonArray.html)
* [PySide6.QtCore.QJsonDocument](QJsonDocument.html)
* [PySide6.QtCore.QJsonParseError](QJsonParseError.html)
* [PySide6.QtCore.QJsonValue](QJsonValue.html)
* [PySide6.QtCore.QKeyCombination](QKeyCombination.html)
* [PySide6.QtCore.QLibrary](QLibrary.html)
* [PySide6.QtCore.QLibraryInfo](QLibraryInfo.html)
* [PySide6.QtCore.QLine](QLine.html)
* [PySide6.QtCore.QLineF](QLineF.html)
* [PySide6.QtCore.QLocale](QLocale.html)
* [PySide6.QtCore.QLocationPermission](QLocationPermission.html)
* [PySide6.QtCore.QLockFile](QLockFile.html)
* [PySide6.QtCore.QLoggingCategory](QLoggingCategory.html)
* [PySide6.QtCore.QMargins](QMargins.html)
* [PySide6.QtCore.QMarginsF](QMarginsF.html)
* [PySide6.QtCore.QMessageAuthenticationCode](QMessageAuthenticationCode.html)
* [PySide6.QtCore.QMessageLogContext](QMessageLogContext.html)
* [PySide6.QtCore.QMessageLogger](QMessageLogger.html)
* [PySide6.QtCore.QMetaClassInfo](QMetaClassInfo.html)
* [PySide6.QtCore.QMetaEnum](QMetaEnum.html)
* [PySide6.QtCore.QMetaMethod](QMetaMethod.html)
* [PySide6.QtCore.QMetaObject](QMetaObject.html)
* [PySide6.QtCore.QMetaProperty](QMetaProperty.html)
* [PySide6.QtCore.QMetaType](QMetaType.html)
* [PySide6.QtCore.QMicrophonePermission](QMicrophonePermission.html)
* [PySide6.QtCore.QMimeData](QMimeData.html)
* [PySide6.QtCore.QMimeDatabase](QMimeDatabase.html)
* [PySide6.QtCore.QMimeType](QMimeType.html)
* [PySide6.QtCore.QModelIndex](QModelIndex.html)
* [PySide6.QtCore.QModelRoleData](QModelRoleData.html)
* [PySide6.QtCore.QModelRoleDataSpan](QModelRoleDataSpan.html)
* [PySide6.QtCore.QMutex](QMutex.html)
* [PySide6.QtCore.QNativeIpcKey](QNativeIpcKey.html)
* [PySide6.QtCore.QObject](QObject.html)
* [PySide6.QtCore.QOperatingSystemVersion](QOperatingSystemVersion.html)
* [PySide6.QtCore.QOperatingSystemVersionBase](QOperatingSystemVersionBase.html)
* [PySide6.QtCore.QParallelAnimationGroup](QParallelAnimationGroup.html)
* [PySide6.QtCore.QPauseAnimation](QPauseAnimation.html)
* [PySide6.QtCore.QPermission](QPermission.html)
* [PySide6.QtCore.QPersistentModelIndex](QPersistentModelIndex.html)
* [PySide6.QtCore.QPluginLoader](QPluginLoader.html)
* [PySide6.QtCore.QPoint](QPoint.html)
* [PySide6.QtCore.QPointF](QPointF.html)
* [PySide6.QtCore.QProcess](QProcess.html)
* [PySide6.QtCore.QProcessEnvironment](QProcessEnvironment.html)
* [PySide6.QtCore.QPropertyAnimation](QPropertyAnimation.html)
* [PySide6.QtCore.QRandomGenerator](QRandomGenerator.html)
* [PySide6.QtCore.QRandomGenerator64](QRandomGenerator64.html)
* [PySide6.QtCore.QRangeModel](QRangeModel.html)
* [PySide6.QtCore.QReadLocker](QReadLocker.html)
* [PySide6.QtCore.QReadWriteLock](QReadWriteLock.html)
* [PySide6.QtCore.QRect](QRect.html)
* [PySide6.QtCore.QRectF](QRectF.html)
* [PySide6.QtCore.QRecursiveMutex](QRecursiveMutex.html)
* [PySide6.QtCore.QRegularExpression](QRegularExpression.html)
* [PySide6.QtCore.QRegularExpressionMatch](QRegularExpressionMatch.html)
* [PySide6.QtCore.QRegularExpressionMatchIterator](QRegularExpressionMatchIterator.html)
* [PySide6.QtCore.QResource](QResource.html)
* [PySide6.QtCore.QRunnable](QRunnable.html)
* [PySide6.QtCore.QSaveFile](QSaveFile.html)
* [PySide6.QtCore.QSemaphore](QSemaphore.html)
* [PySide6.QtCore.QSemaphoreReleaser](QSemaphoreReleaser.html)
* [PySide6.QtCore.QSequentialAnimationGroup](QSequentialAnimationGroup.html)
* [PySide6.QtCore.QSettings](QSettings.html)
* [PySide6.QtCore.QSharedMemory](QSharedMemory.html)
* [PySide6.QtCore.QSignalBlocker](QSignalBlocker.html)
* [PySide6.QtCore.QSignalMapper](QSignalMapper.html)
* [PySide6.QtCore.QSize](QSize.html)
* [PySide6.QtCore.QSizeF](QSizeF.html)
* [PySide6.QtCore.QSocketDescriptor](QSocketDescriptor.html)
* [PySide6.QtCore.QSocketNotifier](QSocketNotifier.html)
* [PySide6.QtCore.QSortFilterProxyModel](QSortFilterProxyModel.html)
* [PySide6.QtCore.QStandardPaths](QStandardPaths.html)
* [PySide6.QtCore.QStorageInfo](QStorageInfo.html)
* [PySide6.QtCore.QStringConverter](QStringConverter.html)
* [PySide6.QtCore.QStringConverterBase](QStringConverterBase.html)
* [PySide6.QtCore.QStringDecoder](QStringDecoder.html)
* [PySide6.QtCore.QStringEncoder](QStringEncoder.html)
* [PySide6.QtCore.QStringListModel](QStringListModel.html)
* [PySide6.QtCore.QSysInfo](QSysInfo.html)
* [PySide6.QtCore.QSystemSemaphore](QSystemSemaphore.html)
* [PySide6.QtCore.QTemporaryDir](QTemporaryDir.html)
* [PySide6.QtCore.QTemporaryFile](QTemporaryFile.html)
* [PySide6.QtCore.QTextBoundaryFinder](QTextBoundaryFinder.html)
* [PySide6.QtCore.QTextStream](QTextStream.html)
* [PySide6.QtCore.QTextStreamManipulator](QTextStreamManipulator.html)
* [PySide6.QtCore.QThread](QThread.html)
* [PySide6.QtCore.QThreadPool](QThreadPool.html)
* [PySide6.QtCore.QTime](QTime.html)
* [PySide6.QtCore.QTimeLine](QTimeLine.html)
* [PySide6.QtCore.QTimeZone](QTimeZone.html)
* [PySide6.QtCore.QTimer](QTimer.html)
* [PySide6.QtCore.QTimerEvent](QTimerEvent.html)
* [PySide6.QtCore.QTranslator](QTranslator.html)
* [PySide6.QtCore.QTransposeProxyModel](QTransposeProxyModel.html)
* [PySide6.QtCore.QUrl](QUrl.html)
* [PySide6.QtCore.QUrlQuery](QUrlQuery.html)
* [PySide6.QtCore.QUuid](QUuid.html)
* [PySide6.QtCore.QVariantAnimation](QVariantAnimation.html)
* [PySide6.QtCore.QVersionNumber](QVersionNumber.html)
* [PySide6.QtCore.QWaitCondition](QWaitCondition.html)
* [PySide6.QtCore.QWriteLocker](QWriteLocker.html)
* [PySide6.QtCore.QXmlStreamAttribute](QXmlStreamAttribute.html)
* [PySide6.QtCore.QXmlStreamAttributes](QXmlStreamAttributes.html)
* [PySide6.QtCore.QXmlStreamEntityDeclaration](QXmlStreamEntityDeclaration.html)
* [PySide6.QtCore.QXmlStreamEntityResolver](QXmlStreamEntityResolver.html)
* [PySide6.QtCore.QXmlStreamNamespaceDeclaration](QXmlStreamNamespaceDeclaration.html)
* [PySide6.QtCore.QXmlStreamNotationDeclaration](QXmlStreamNotationDeclaration.html)
* [PySide6.QtCore.QXmlStreamReader](QXmlStreamReader.html)
* [PySide6.QtCore.QXmlStreamWriter](QXmlStreamWriter.html)
* [PySide6.QtCore.Qt](Qt.html)
* [PySide6.QtCore.Property](Property.html)
* [PySide6.QtCore.Signal](Signal.html)
## Detailed Description[Â¶](#detailed-description "Link to this heading")
The Qt Core module is part of Qtâs essential modules.
The Qt Core module adds these features to C++:
> * a very powerful mechanism for seamless object communication called signals and slots
> * queryable and designable object properties
> * hierarchical and queryable object trees
The following pages provide more information about Qtâs core features:
> * [The Meta-Object System](../../overviews/qtcore-metaobjects.html#the-meta-object-system)
> * [The Property System](../../overviews/qtcore-properties.html#the-property-system)
> * [Object Model](../../overviews/qtcore-object.html#object-model)
> * [Object Trees & Ownership](../../overviews/qtcore-objecttrees.html#object-trees-ownership)
> * [Signals & Slots](../../overviews/qtcore-signalsandslots.html#signals-slots)
### Using the Module[Â¶](#using-the-module "Link to this heading")
To include the definitions of modules classes, use the following
directive:
```
import PySide6.QtCore
```
### Threading and Concurrent Programming[Â¶](#threading-and-concurrent-programming "Link to this heading")
Qt provides thread support in the form of platform-independent
threading classes, a thread-safe way of posting events, and
signal-slot connections across threads. Multithreaded programming is
also a useful paradigm for performing time-consuming operations
without freezing the user interface of an application.
The Thread Support in Qt page contains information on implementing
threads in applications. Additional concurrent classes are provided by
the Qt Concurrent module.
### Input/Output and Resources[Â¶](#input-output-and-resources "Link to this heading")
Qt provides a resource system for organizing application files and
assets, a set of containers, and classes for receiving input and
printing output.
> * [Serializing Qt Data Types](../../overviews/qtcore-datastreamformat.html#serializing-qt-data-types)
In addition, Qt Core provides a platform-independent mechanism for
storing binary files in the applicationâs executable.
> * [The Qt Resource System](../../tutorials/basictutorial/qrcfiles.html#tutorial-qrcfiles)
### Additional Frameworks[Â¶](#additional-frameworks "Link to this heading")
Qt Core also provides some of Qtâs key frameworks.
> * [The Animation Framework](../../overviews/qtcore-animation-overview.html#the-animation-framework)
> * [CBOR Support in Qt](../../overviews/qtcore-cbor.html#cbor-support-in-qt)
> * [JSON Support in Qt](../../overviews/qtcore-json.html#json-support-in-qt)
> * [Inter-Process Communication](../../overviews/qtcore-ipc.html#inter-process-communication)
> * [The Event System](../../overviews/qtcore-eventsandfilters.html#the-event-system)
> * [Application Permissions](../../overviews/qtcore-permissions.html#application-permissions)
## List of Classes by Function[Â¶](#list-of-classes-by-function "Link to this heading")
> * [Animation Framework](../../groups/qtcore-animation.html#animation-framework)
> * [Event Classes](../../groups/qtcore-events.html#event-classes)
> * [Input/Output and Networking](../../groups/qtcore-io.html#input-output-and-networking)
## List of Classes[Â¶](#list-of-classes "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **A** | * [`QAbstractAnimation`](QAbstractAnimation.html#PySide6.QtCore.QAbstractAnimation "PySide6.QtCore.QAbstractAnimation") | * [`QAbstractEventDispatcher`](QAbstractEventDispatcher.html#PySide6.QtCore.QAbstractEventDispatcher "PySide6.QtCore.QAbstractEventDispatcher") | * [`QAbstractItemModel`](QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel "PySide6.QtCore.QAbstractItemModel") |
|  | * [`QAbstractListModel`](QAbstractListModel.html#PySide6.QtCore.QAbstractListModel "PySide6.QtCore.QAbstractListModel") | * [`QAbstractNativeEventFilter`](QAbstractNativeEventFilter.html#PySide6.QtCore.QAbstractNativeEventFilter "PySide6.QtCore.QAbstractNativeEventFilter") | * [`QAbstractProxyModel`](QAbstractProxyModel.html#PySide6.QtCore.QAbstractProxyModel "PySide6.QtCore.QAbstractProxyModel") |
|  | * [`QAbstractTableModel`](QAbstractTableModel.html#PySide6.QtCore.QAbstractTableModel "PySide6.QtCore.QAbstractTableModel") | * [`QAnimationGroup`](QAnimationGroup.html#PySide6.QtCore.QAnimationGroup "PySide6.QtCore.QAnimationGroup") |  |
| **B** | * [`QBasicMutex`](QBasicMutex.html#PySide6.QtCore.QBasicMutex "PySide6.QtCore.QBasicMutex") | * [`QBasicReadWriteLock`](QBasicReadWriteLock.html#PySide6.QtCore.QBasicReadWriteLock "PySide6.QtCore.QBasicReadWriteLock") | * [`QBasicTimer`](QBasicTimer.html#PySide6.QtCore.QBasicTimer "PySide6.QtCore.QBasicTimer") |
|  | * [`QBitArray`](QBitArray.html#PySide6.QtCore.QBitArray "PySide6.QtCore.QBitArray") | * [`QBluetoothPermission`](QBluetoothPermission.html#PySide6.QtCore.QBluetoothPermission "PySide6.QtCore.QBluetoothPermission") | * [`QBuffer`](QBuffer.html#PySide6.QtCore.QBuffer "PySide6.QtCore.QBuffer") |
|  | * [`QByteArray`](QByteArray.html#PySide6.QtCore.QByteArray "PySide6.QtCore.QByteArray") | * [`QByteArrayMatcher`](QByteArrayMatcher.html#PySide6.QtCore.QByteArrayMatcher "PySide6.QtCore.QByteArrayMatcher") |  |
| **C** | * [`Connection`](QMetaObject.html#PySide6.QtCore.QMetaObject.Connection "PySide6.QtCore.QMetaObject.Connection") | * [`QCalendar`](QCalendar.html#PySide6.QtCore.QCalendar "PySide6.QtCore.QCalendar") | * [`QCalendarPermission`](QCalendarPermission.html#PySide6.QtCore.QCalendarPermission "PySide6.QtCore.QCalendarPermission") |
|  | * [`QCameraPermission`](QCameraPermission.html#PySide6.QtCore.QCameraPermission "PySide6.QtCore.QCameraPermission") | * [`QCborArray`](QCborArray.html#PySide6.QtCore.QCborArray "PySide6.QtCore.QCborArray") | * [`QCborError`](QCborError.html#PySide6.QtCore.QCborError "PySide6.QtCore.QCborError") |
|  | * [`QCborMap`](QCborMap.html#PySide6.QtCore.QCborMap "PySide6.QtCore.QCborMap") | * [`QCborParserError`](QCborParserError.html#PySide6.QtCore.QCborParserError "PySide6.QtCore.QCborParserError") | * [`QCborStreamReader`](QCborStreamReader.html#PySide6.QtCore.QCborStreamReader "PySide6.QtCore.QCborStreamReader") |
|  | * [`QCborStreamWriter`](QCborStreamWriter.html#PySide6.QtCore.QCborStreamWriter "PySide6.QtCore.QCborStreamWriter") | * [`QCborStringResultByteArray`](QCborStringResultByteArray.html#PySide6.QtCore.QCborStringResultByteArray "PySide6.QtCore.QCborStringResultByteArray") | * [`QCborStringResultString`](QCborStringResultString.html#PySide6.QtCore.QCborStringResultString "PySide6.QtCore.QCborStringResultString") |
|  | * [`QCborValue`](QCborValue.html#PySide6.QtCore.QCborValue "PySide6.QtCore.QCborValue") | * [`QChildEvent`](QChildEvent.html#PySide6.QtCore.QChildEvent "PySide6.QtCore.QChildEvent") | * [`QCollator`](QCollator.html#PySide6.QtCore.QCollator "PySide6.QtCore.QCollator") |
|  | * [`QCollatorSortKey`](QCollatorSortKey.html#PySide6.QtCore.QCollatorSortKey "PySide6.QtCore.QCollatorSortKey") | * [`QCommandLineOption`](QCommandLineOption.html#PySide6.QtCore.QCommandLineOption "PySide6.QtCore.QCommandLineOption") | * [`QCommandLineParser`](QCommandLineParser.html#PySide6.QtCore.QCommandLineParser "PySide6.QtCore.QCommandLineParser") |
|  | * [`QConcatenateTablesProxyModel`](QConcatenateTablesProxyModel.html#PySide6.QtCore.QConcatenateTablesProxyModel "PySide6.QtCore.QConcatenateTablesProxyModel") | * [`QContactsPermission`](QContactsPermission.html#PySide6.QtCore.QContactsPermission "PySide6.QtCore.QContactsPermission") | * [`QCoreApplication`](QCoreApplication.html#PySide6.QtCore.QCoreApplication "PySide6.QtCore.QCoreApplication") |
|  | * [`QCryptographicHash`](QCryptographicHash.html#PySide6.QtCore.QCryptographicHash "PySide6.QtCore.QCryptographicHash") |  | |
| **D** | * [`DirEntry`](QDirListing.html#PySide6.QtCore.QDirListing.DirEntry "PySide6.QtCore.QDirListing.DirEntry") | * [`QDataStream`](QDataStream.html#PySide6.QtCore.QDataStream "PySide6.QtCore.QDataStream") | * [`QDate`](QDate.html#PySide6.QtCore.QDate "PySide6.QtCore.QDate") |
|  | * [`QDateTime`](QDateTime.html#PySide6.QtCore.QDateTime "PySide6.QtCore.QDateTime") | * [`QDeadlineTimer`](QDeadlineTimer.html#PySide6.QtCore.QDeadlineTimer "PySide6.QtCore.QDeadlineTimer") | * [`QDir`](QDir.html#PySide6.QtCore.QDir "PySide6.QtCore.QDir") |
|  | * [`QDirIterator`](QDirIterator.html#PySide6.QtCore.QDirIterator "PySide6.QtCore.QDirIterator") | * [`QDirListing`](QDirListing.html#PySide6.QtCore.QDirListing "PySide6.QtCore.QDirListing") | * [`QDynamicPropertyChangeEvent`](QDynamicPropertyChangeEvent.html#PySide6.QtCore.QDynamicPropertyChangeEvent "PySide6.QtCore.QDynamicPropertyChangeEvent") |
| **E** | * [`QEasingCurve`](QEasingCurve.html#PySide6.QtCore.QEasingCurve "PySide6.QtCore.QEasingCurve") | * [`QElapsedTimer`](QElapsedTimer.html#PySide6.QtCore.QElapsedTimer "PySide6.QtCore.QElapsedTimer") | * [`QEvent`](QEvent.html#PySide6.QtCore.QEvent "PySide6.QtCore.QEvent") |
|  | * [`QEventLoop`](QEventLoop.html#PySide6.QtCore.QEventLoop "PySide6.QtCore.QEventLoop") |  | |
| **F** | * [`FromBase64Result`](QByteArray.html#PySide6.QtCore.QByteArray.FromBase64Result "PySide6.QtCore.QByteArray.FromBase64Result") | * [`QFactoryInterface`](QFactoryInterface.html#PySide6.QtCore.QFactoryInterface "PySide6.QtCore.QFactoryInterface") | * [`QFile`](QFile.html#PySide6.QtCore.QFile "PySide6.QtCore.QFile") |
|  | * [`QFileDevice`](QFileDevice.html#PySide6.QtCore.QFileDevice "PySide6.QtCore.QFileDevice") | * [`QFileInfo`](QFileInfo.html#PySide6.QtCore.QFileInfo "PySide6.QtCore.QFileInfo") | * [`QFileSelector`](QFileSelector.html#PySide6.QtCore.QFileSelector "PySide6.QtCore.QFileSelector") |
|  | * [`QFileSystemWatcher`](QFileSystemWatcher.html#PySide6.QtCore.QFileSystemWatcher "PySide6.QtCore.QFileSystemWatcher") | * [`QFutureInterfaceBase`](QFutureInterfaceBase.html#PySide6.QtCore.QFutureInterfaceBase "PySide6.QtCore.QFutureInterfaceBase") |  |
| **G** | * [`QGenericArgument`](QGenericArgument.html#PySide6.QtCore.QGenericArgument "PySide6.QtCore.QGenericArgument") | * [`QGenericReturnArgument`](QGenericReturnArgument.html#PySide6.QtCore.QGenericReturnArgument "PySide6.QtCore.QGenericReturnArgument") |  |
| **H** | * [`QHashSeed`](QHashSeed.html#PySide6.QtCore.QHashSeed "PySide6.QtCore.QHashSeed") | | |
| **I** | * [`QIODevice`](QIODevice.html#PySide6.QtCore.QIODevice "PySide6.QtCore.QIODevice") | * [`QIODeviceBase`](QIODeviceBase.html#PySide6.QtCore.QIODeviceBase "PySide6.QtCore.QIODeviceBase") | * [`QIdentityProxyModel`](QIdentityProxyModel.html#PySide6.QtCore.QIdentityProxyModel "PySide6.QtCore.QIdentityProxyModel") |
|  | * [`QItemSelection`](QItemSelection.html#PySide6.QtCore.QItemSelection "PySide6.QtCore.QItemSelection") | * [`QItemSelectionModel`](QItemSelectionModel.html#PySide6.QtCore.QItemSelectionModel "PySide6.QtCore.QItemSelectionModel") | * [`QItemSelectionRange`](QItemSelectionRange.html#PySide6.QtCore.QItemSelectionRange "PySide6.QtCore.QItemSelectionRange") |
| **J** | * [`QJsonArray`](QJsonArray.html#PySide6.QtCore.QJsonArray "PySide6.QtCore.QJsonArray") | * [`QJsonDocument`](QJsonDocument.html#PySide6.QtCore.QJsonDocument "PySide6.QtCore.QJsonDocument") | * [`QJsonParseError`](QJsonParseError.html#PySide6.QtCore.QJsonParseError "PySide6.QtCore.QJsonParseError") |
|  | * [`QJsonValue`](QJsonValue.html#PySide6.QtCore.QJsonValue "PySide6.QtCore.QJsonValue") |  | |
| **K** | * [`QKeyCombination`](QKeyCombination.html#PySide6.QtCore.QKeyCombination "PySide6.QtCore.QKeyCombination") | | |
| **L** | * [`QLibrary`](QLibrary.html#PySide6.QtCore.QLibrary "PySide6.QtCore.QLibrary") | * [`QLibraryInfo`](QLibraryInfo.html#PySide6.QtCore.QLibraryInfo "PySide6.QtCore.QLibraryInfo") | * [`QLine`](QLine.html#PySide6.QtCore.QLine "PySide6.QtCore.QLine") |
|  | * [`QLineF`](QLineF.html#PySide6.QtCore.QLineF "PySide6.QtCore.QLineF") | * [`QLocale`](QLocale.html#PySide6.QtCore.QLocale "PySide6.QtCore.QLocale") | * [`QLocationPermission`](QLocationPermission.html#PySide6.QtCore.QLocationPermission "PySide6.QtCore.QLocationPermission") |
|  | * [`QLockFile`](QLockFile.html#PySide6.QtCore.QLockFile "PySide6.QtCore.QLockFile") | * [`QLoggingCategory`](QLoggingCategory.html#PySide6.QtCore.QLoggingCategory "PySide6.QtCore.QLoggingCategory") |  |
| **M** | * [`QMargins`](QMargins.html#PySide6.QtCore.QMargins "PySide6.QtCore.QMargins") | * [`QMarginsF`](QMarginsF.html#PySide6.QtCore.QMarginsF "PySide6.QtCore.QMarginsF") | * [`QMessageAuthenticationCode`](QMessageAuthenticationCode.html#PySide6.QtCore.QMessageAuthenticationCode "PySide6.QtCore.QMessageAuthenticationCode") |
|  | * [`QMessageLogContext`](QMessageLogContext.html#PySide6.QtCore.QMessageLogContext "PySide6.QtCore.QMessageLogContext") | * [`QMessageLogger`](QMessageLogger.html#PySide6.QtCore.QMessageLogger "PySide6.QtCore.QMessageLogger") | * [`QMetaClassInfo`](QMetaClassInfo.html#PySide6.QtCore.QMetaClassInfo "PySide6.QtCore.QMetaClassInfo") |
|  | * [`QMetaEnum`](QMetaEnum.html#PySide6.QtCore.QMetaEnum "PySide6.QtCore.QMetaEnum") | * [`QMetaMethod`](QMetaMethod.html#PySide6.QtCore.QMetaMethod "PySide6.QtCore.QMetaMethod") | * [`QMetaObject`](QMetaObject.html#PySide6.QtCore.QMetaObject "PySide6.QtCore.QMetaObject") |
|  | * [`QMetaProperty`](QMetaProperty.html#PySide6.QtCore.QMetaProperty "PySide6.QtCore.QMetaProperty") | * [`QMetaType`](QMetaType.html#PySide6.QtCore.QMetaType "PySide6.QtCore.QMetaType") | * [`QMicrophonePermission`](QMicrophonePermission.html#PySide6.QtCore.QMicrophonePermission "PySide6.QtCore.QMicrophonePermission") |
|  | * [`QMimeData`](QMimeData.html#PySide6.QtCore.QMimeData "PySide6.QtCore.QMimeData") | * [`QMimeDatabase`](QMimeDatabase.html#PySide6.QtCore.QMimeDatabase "PySide6.QtCore.QMimeDatabase") | * [`QMimeType`](QMimeType.html#PySide6.QtCore.QMimeType "PySide6.QtCore.QMimeType") |
|  | * [`QModelIndex`](QModelIndex.html#PySide6.QtCore.QModelIndex "PySide6.QtCore.QModelIndex") | * [`QModelRoleData`](QModelRoleData.html#PySide6.QtCore.QModelRoleData "PySide6.QtCore.QModelRoleData") | * [`QModelRoleDataSpan`](QModelRoleDataSpan.html#PySide6.QtCore.QModelRoleDataSpan "PySide6.QtCore.QModelRoleDataSpan") |
|  | * [`QMutex`](QMutex.html#PySide6.QtCore.QMutex "PySide6.QtCore.QMutex") |  | |
| **N** | * [`QNativeIpcKey`](QNativeIpcKey.html#PySide6.QtCore.QNativeIpcKey "PySide6.QtCore.QNativeIpcKey") | | |
| **O** | * [`OffsetData`](QTimeZone.html#PySide6.QtCore.QTimeZone.OffsetData "PySide6.QtCore.QTimeZone.OffsetData") | * [`QObject`](QObject.html#PySide6.QtCore.QObject "PySide6.QtCore.QObject") | * [`QOperatingSystemVersion`](QOperatingSystemVersion.html#PySide6.QtCore.QOperatingSystemVersion "PySide6.QtCore.QOperatingSystemVersion") |
|  | * [`QOperatingSystemVersionBase`](QOperatingSystemVersionBase.html#PySide6.QtCore.QOperatingSystemVersionBase "PySide6.QtCore.QOperatingSystemVersionBase") |  | |
| **P** | * [`QParallelAnimationGroup`](QParallelAnimationGroup.html#PySide6.QtCore.QParallelAnimationGroup "PySide6.QtCore.QParallelAnimationGroup") | * [`QPauseAnimation`](QPauseAnimation.html#PySide6.QtCore.QPauseAnimation "PySide6.QtCore.QPauseAnimation") | * [`QPermission`](QPermission.html#PySide6.QtCore.QPermission "PySide6.QtCore.QPermission") |
|  | * [`QPersistentModelIndex`](QPersistentModelIndex.html#PySide6.QtCore.QPersistentModelIndex "PySide6.QtCore.QPersistentModelIndex") | * [`QPluginLoader`](QPluginLoader.html#PySide6.QtCore.QPluginLoader "PySide6.QtCore.QPluginLoader") | * [`QPoint`](QPoint.html#PySide6.QtCore.QPoint "PySide6.QtCore.QPoint") |
|  | * [`QPointF`](QPointF.html#PySide6.QtCore.QPointF "PySide6.QtCore.QPointF") | * [`QProcess`](QProcess.html#PySide6.QtCore.QProcess "PySide6.QtCore.QProcess") | * [`QProcessEnvironment`](QProcessEnvironment.html#PySide6.QtCore.QProcessEnvironment "PySide6.QtCore.QProcessEnvironment") |
|  | * [`QPropertyAnimation`](QPropertyAnimation.html#PySide6.QtCore.QPropertyAnimation "PySide6.QtCore.QPropertyAnimation") | * [`Property`](Property.html#PySide6.QtCore.Property "PySide6.QtCore.Property") |  |
| **Q** | * [`Qt`](Qt.html#PySide6.QtCore.Qt "PySide6.QtCore.Qt") | | |
| **R** | * [`QRandomGenerator`](QRandomGenerator.html#PySide6.QtCore.QRandomGenerator "PySide6.QtCore.QRandomGenerator") | * [`QRandomGenerator64`](QRandomGenerator64.html#PySide6.QtCore.QRandomGenerator64 "PySide6.QtCore.QRandomGenerator64") | * [`QRangeModel`](QRangeModel.html#PySide6.QtCore.QRangeModel "PySide6.QtCore.QRangeModel") |
|  | * [`QReadLocker`](QReadLocker.html#PySide6.QtCore.QReadLocker "PySide6.QtCore.QReadLocker") | * [`QReadWriteLock`](QReadWriteLock.html#PySide6.QtCore.QReadWriteLock "PySide6.QtCore.QReadWriteLock") | * [`QRect`](QRect.html#PySide6.QtCore.QRect "PySide6.QtCore.QRect") |
|  | * [`QRectF`](QRectF.html#PySide6.QtCore.QRectF "PySide6.QtCore.QRectF") | * [`QRecursiveMutex`](QRecursiveMutex.html#PySide6.QtCore.QRecursiveMutex "PySide6.QtCore.QRecursiveMutex") | * [`QRegularExpression`](QRegularExpression.html#PySide6.QtCore.QRegularExpression "PySide6.QtCore.QRegularExpression") |
|  | * [`QRegularExpressionMatch`](QRegularExpressionMatch.html#PySide6.QtCore.QRegularExpressionMatch "PySide6.QtCore.QRegularExpressionMatch") | * [`QRegularExpressionMatchIterator`](QRegularExpressionMatchIterator.html#PySide6.QtCore.QRegularExpressionMatchIterator "PySide6.QtCore.QRegularExpressionMatchIterator") | * [`QResource`](QResource.html#PySide6.QtCore.QResource "PySide6.QtCore.QResource") |
|  | * [`QRunnable`](QRunnable.html#PySide6.QtCore.QRunnable "PySide6.QtCore.QRunnable") |  | |
| **S** | * [`QSaveFile`](QSaveFile.html#PySide6.QtCore.QSaveFile "PySide6.QtCore.QSaveFile") | * [`QSemaphore`](QSemaphore.html#PySide6.QtCore.QSemaphore "PySide6.QtCore.QSemaphore") | * [`QSemaphoreReleaser`](QSemaphoreReleaser.html#PySide6.QtCore.QSemaphoreReleaser "PySide6.QtCore.QSemaphoreReleaser") |
|  | * [`QSequentialAnimationGroup`](QSequentialAnimationGroup.html#PySide6.QtCore.QSequentialAnimationGroup "PySide6.QtCore.QSequentialAnimationGroup") | * [`QSettings`](QSettings.html#PySide6.QtCore.QSettings "PySide6.QtCore.QSettings") | * [`QSharedMemory`](QSharedMemory.html#PySide6.QtCore.QSharedMemory "PySide6.QtCore.QSharedMemory") |
|  | * [`QSignalBlocker`](QSignalBlocker.html#PySide6.QtCore.QSignalBlocker "PySide6.QtCore.QSignalBlocker") | * [`QSignalMapper`](QSignalMapper.html#PySide6.QtCore.QSignalMapper "PySide6.QtCore.QSignalMapper") | * [`QSize`](QSize.html#PySide6.QtCore.QSize "PySide6.QtCore.QSize") |
|  | * [`QSizeF`](QSizeF.html#PySide6.QtCore.QSizeF "PySide6.QtCore.QSizeF") | * [`QSocketDescriptor`](QSocketDescriptor.html#PySide6.QtCore.QSocketDescriptor "PySide6.QtCore.QSocketDescriptor") | * [`QSocketNotifier`](QSocketNotifier.html#PySide6.QtCore.QSocketNotifier "PySide6.QtCore.QSocketNotifier") |
|  | * [`QSortFilterProxyModel`](QSortFilterProxyModel.html#PySide6.QtCore.QSortFilterProxyModel "PySide6.QtCore.QSortFilterProxyModel") | * [`QStandardPaths`](QStandardPaths.html#PySide6.QtCore.QStandardPaths "PySide6.QtCore.QStandardPaths") | * [`QStorageInfo`](QStorageInfo.html#PySide6.QtCore.QStorageInfo "PySide6.QtCore.QStorageInfo") |
|  | * [`QStringConverter`](QStringConverter.html#PySide6.QtCore.QStringConverter "PySide6.QtCore.QStringConverter") | * [`QStringConverterBase`](QStringConverterBase.html#PySide6.QtCore.QStringConverterBase "PySide6.QtCore.QStringConverterBase") | * [`QStringDecoder`](QStringDecoder.html#PySide6.QtCore.QStringDecoder "PySide6.QtCore.QStringDecoder") |
|  | * [`QStringEncoder`](QStringEncoder.html#PySide6.QtCore.QStringEncoder "PySide6.QtCore.QStringEncoder") | * [`QStringListModel`](QStringListModel.html#PySide6.QtCore.QStringListModel "PySide6.QtCore.QStringListModel") | * [`QSysInfo`](QSysInfo.html#PySide6.QtCore.QSysInfo "PySide6.QtCore.QSysInfo") |
|  | * [`QSystemSemaphore`](QSystemSemaphore.html#PySide6.QtCore.QSystemSemaphore "PySide6.QtCore.QSystemSemaphore") | * [`State`](QStringConverterBase.html#PySide6.QtCore.QStringConverterBase.State "PySide6.QtCore.QStringConverterBase.State") | * [`SystemId`](QCalendar.html#PySide6.QtCore.QCalendar.SystemId "PySide6.QtCore.QCalendar.SystemId") |
|  | * [`Signal`](Signal.html#PySide6.QtCore.Signal "PySide6.QtCore.Signal") |  | |
| **T** | * [`QTemporaryDir`](QTemporaryDir.html#PySide6.QtCore.QTemporaryDir "PySide6.QtCore.QTemporaryDir") | * [`QTemporaryFile`](QTemporaryFile.html#PySide6.QtCore.QTemporaryFile "PySide6.QtCore.QTemporaryFile") | * [`QTextBoundaryFinder`](QTextBoundaryFinder.html#PySide6.QtCore.QTextBoundaryFinder "PySide6.QtCore.QTextBoundaryFinder") |
|  | * [`QTextStream`](QTextStream.html#PySide6.QtCore.QTextStream "PySide6.QtCore.QTextStream") | * [`QTextStreamManipulator`](QTextStreamManipulator.html#PySide6.QtCore.QTextStreamManipulator "PySide6.QtCore.QTextStreamManipulator") | * [`QThread`](QThread.html#PySide6.QtCore.QThread "PySide6.QtCore.QThread") |
|  | * [`QThreadPool`](QThreadPool.html#PySide6.QtCore.QThreadPool "PySide6.QtCore.QThreadPool") | * [`QTime`](QTime.html#PySide6.QtCore.QTime "PySide6.QtCore.QTime") | * [`QTimeLine`](QTimeLine.html#PySide6.QtCore.QTimeLine "PySide6.QtCore.QTimeLine") |
|  | * [`QTimeZone`](QTimeZone.html#PySide6.QtCore.QTimeZone "PySide6.QtCore.QTimeZone") | * [`QTimer`](QTimer.html#PySide6.QtCore.QTimer "PySide6.QtCore.QTimer") | * [`QTimerEvent`](QTimerEvent.html#PySide6.QtCore.QTimerEvent "PySide6.QtCore.QTimerEvent") |
|  | * [`QTranslator`](QTranslator.html#PySide6.QtCore.QTranslator "PySide6.QtCore.QTranslator") | * [`QTransposeProxyModel`](QTransposeProxyModel.html#PySide6.QtCore.QTransposeProxyModel "PySide6.QtCore.QTransposeProxyModel") | * [`TimerInfo`](QAbstractEventDispatcher.html#PySide6.QtCore.QAbstractEventDispatcher.TimerInfo "PySide6.QtCore.QAbstractEventDispatcher.TimerInfo") |
| **U** | * [`QUrl`](QUrl.html#PySide6.QtCore.QUrl "PySide6.QtCore.QUrl") | * [`QUrlQuery`](QUrlQuery.html#PySide6.QtCore.QUrlQuery "PySide6.QtCore.QUrlQuery") | * [`QUuid`](QUuid.html#PySide6.QtCore.QUuid "PySide6.QtCore.QUuid") |
|  | * [`UnixProcessParameters`](QProcess.html#PySide6.QtCore.QProcess.UnixProcessParameters "PySide6.QtCore.QProcess.UnixProcessParameters") |  | |
| **V** | * [`QVariantAnimation`](QVariantAnimation.html#PySide6.QtCore.QVariantAnimation "PySide6.QtCore.QVariantAnimation") | * [`QVersionNumber`](QVersionNumber.html#PySide6.QtCore.QVersionNumber "PySide6.QtCore.QVersionNumber") |  |
| **W** | * [`QWaitCondition`](QWaitCondition.html#PySide6.QtCore.QWaitCondition "PySide6.QtCore.QWaitCondition") | * [`QWriteLocker`](QWriteLocker.html#PySide6.QtCore.QWriteLocker "PySide6.QtCore.QWriteLocker") |  |
| **X** | * [`QXmlStreamAttribute`](QXmlStreamAttribute.html#PySide6.QtCore.QXmlStreamAttribute "PySide6.QtCore.QXmlStreamAttribute") | * [`QXmlStreamAttributes`](QXmlStreamAttributes.html#PySide6.QtCore.QXmlStreamAttributes "PySide6.QtCore.QXmlStreamAttributes") | * [`QXmlStreamEntityDeclaration`](QXmlStreamEntityDeclaration.html#PySide6.QtCore.QXmlStreamEntityDeclaration "PySide6.QtCore.QXmlStreamEntityDeclaration") |
|  | * [`QXmlStreamEntityResolver`](QXmlStreamEntityResolver.html#PySide6.QtCore.QXmlStreamEntityResolver "PySide6.QtCore.QXmlStreamEntityResolver") | * [`QXmlStreamNamespaceDeclaration`](QXmlStreamNamespaceDeclaration.html#PySide6.QtCore.QXmlStreamNamespaceDeclaration "PySide6.QtCore.QXmlStreamNamespaceDeclaration") | * [`QXmlStreamNotationDeclaration`](QXmlStreamNotationDeclaration.html#PySide6.QtCore.QXmlStreamNotationDeclaration "PySide6.QtCore.QXmlStreamNotationDeclaration") |
|  | * [`QXmlStreamReader`](QXmlStreamReader.html#PySide6.QtCore.QXmlStreamReader "PySide6.QtCore.QXmlStreamReader") | * [`QXmlStreamWriter`](QXmlStreamWriter.html#PySide6.QtCore.QXmlStreamWriter "PySide6.QtCore.QXmlStreamWriter") |  |
| **Y** | * [`YearMonthDay`](QCalendar.html#PySide6.QtCore.QCalendar.YearMonthDay "PySide6.QtCore.QCalendar.YearMonthDay") | | |
## List of Decorators[Â¶](#list-of-decorators "Link to this heading")
|  |  |
| --- | --- |
| **C** | * [`@ClassInfo`](ClassInfo.html#PySide6.QtCore.ClassInfo "PySide6.QtCore.ClassInfo") |
| **E** | * [`@QEnum`](QEnum.html#PySide6.QtCore.QEnum "PySide6.QtCore.QEnum") |
| **F** | * [`@QFlag`](QFlag.html#PySide6.QtCore.QFlag "PySide6.QtCore.QFlag") |
| **S** | * [`@Slot`](Slot.html#PySide6.QtCore.Slot "PySide6.QtCore.Slot") |
## List of Functions[Â¶](#list-of-functions "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **A** | * [`Q_ARG()`](QtCore_globals.html#PySide6.QtCore.Q_ARG "PySide6.QtCore.Q_ARG") | * [`qAbs()`](QtCore_globals.html#PySide6.QtCore.qAbs "PySide6.QtCore.qAbs") | * [`qAddPostRoutine()`](QtCore_globals.html#PySide6.QtCore.qAddPostRoutine "PySide6.QtCore.qAddPostRoutine") |
| **C** | * [`qCompress()`](QtCore_globals.html#PySide6.QtCore.qCompress "PySide6.QtCore.qCompress") | * [`qCritical()`](QtCore_globals.html#PySide6.QtCore.qCritical "PySide6.QtCore.qCritical") | * [`qCDebug()`](QtCore_globals.html#PySide6.QtCore.qCDebug "PySide6.QtCore.qCDebug") |
|  | * [`qCCritical()`](QtCore_globals.html#PySide6.QtCore.qCCritical "PySide6.QtCore.qCCritical") | * [`qCInfo()`](QtCore_globals.html#PySide6.QtCore.qCInfo "PySide6.QtCore.qCInfo") | * [`qCWarning()`](QtCore_globals.html#PySide6.QtCore.qCWarning "PySide6.QtCore.qCWarning") |
| **D** | * [`qDebug()`](QtCore_globals.html#PySide6.QtCore.qDebug "PySide6.QtCore.qDebug") | | |
| **F** | * [`qFastCos()`](QtCore_globals.html#PySide6.QtCore.qFastCos "PySide6.QtCore.qFastCos") | * [`qFastSin()`](QtCore_globals.html#PySide6.QtCore.qFastSin "PySide6.QtCore.qFastSin") | * [`qFormatLogMessage()`](QtCore_globals.html#PySide6.QtCore.qFormatLogMessage "PySide6.QtCore.qFormatLogMessage") |
|  | * [`qFuzzyCompare()`](QtCore_globals.html#PySide6.QtCore.qFuzzyCompare "PySide6.QtCore.qFuzzyCompare") | * [`qFuzzyIsNull()`](QtCore_globals.html#PySide6.QtCore.qFuzzyIsNull "PySide6.QtCore.qFuzzyIsNull") | * [`qFatal()`](QtCore_globals.html#PySide6.QtCore.qFatal "PySide6.QtCore.qFatal") |
| **I** | * [`qIsFinite()`](QtCore_globals.html#PySide6.QtCore.qIsFinite "PySide6.QtCore.qIsFinite") | * [`qIsInf()`](QtCore_globals.html#PySide6.QtCore.qIsInf "PySide6.QtCore.qIsInf") | * [`qIsNaN()`](QtCore_globals.html#PySide6.QtCore.qIsNaN "PySide6.QtCore.qIsNaN") |
|  | * [`qIsNull()`](QtCore_globals.html#PySide6.QtCore.qIsNull "PySide6.QtCore.qIsNull") | * [`qInfo()`](QtCore_globals.html#PySide6.QtCore.qInfo "PySide6.QtCore.qInfo") | * [`__init_feature__()`](QtCore_globals.html#PySide6.QtCore.__init_feature__ "PySide6.QtCore.__init_feature__") |
|  | * [`qInstallMessageHandler()`](QtCore_globals.html#PySide6.QtCore.qInstallMessageHandler "PySide6.QtCore.qInstallMessageHandler") |  | |
| **M** | * [`__moduleShutdown()`](QtCore_globals.html#PySide6.QtCore.__moduleShutdown "PySide6.QtCore.__moduleShutdown") | | |
| **Q** | * [`qtTrId()`](QtCore_globals.html#PySide6.QtCore.qtTrId "PySide6.QtCore.qtTrId") | | |
| **R** | * [`Q_RETURN_ARG()`](QtCore_globals.html#PySide6.QtCore.Q_RETURN_ARG "PySide6.QtCore.Q_RETURN_ARG") | * [`qRegisterResourceData()`](QtCore_globals.html#PySide6.QtCore.qRegisterResourceData "PySide6.QtCore.qRegisterResourceData") |  |
| **S** | * [`qSetMessagePattern()`](QtCore_globals.html#PySide6.QtCore.qSetMessagePattern "PySide6.QtCore.qSetMessagePattern") | * [`SIGNAL()`](QtCore_globals.html#PySide6.QtCore.SIGNAL "PySide6.QtCore.SIGNAL") | * [`SLOT()`](QtCore_globals.html#PySide6.QtCore.SLOT "PySide6.QtCore.SLOT") |
| **T** | * [`QT_TR_NOOP()`](QtCore_globals.html#PySide6.QtCore.QT_TR_NOOP "PySide6.QtCore.QT_TR_NOOP") | * [`QT_TR_NOOP_UTF8()`](QtCore_globals.html#PySide6.QtCore.QT_TR_NOOP_UTF8 "PySide6.QtCore.QT_TR_NOOP_UTF8") | * [`QT_TRANSLATE_NOOP()`](QtCore_globals.html#PySide6.QtCore.QT_TRANSLATE_NOOP "PySide6.QtCore.QT_TRANSLATE_NOOP") |
|  | * [`QT_TRANSLATE_NOOP3()`](QtCore_globals.html#PySide6.QtCore.QT_TRANSLATE_NOOP3 "PySide6.QtCore.QT_TRANSLATE_NOOP3") | * [`QT_TRANSLATE_NOOP_UTF8()`](QtCore_globals.html#PySide6.QtCore.QT_TRANSLATE_NOOP_UTF8 "PySide6.QtCore.QT_TRANSLATE_NOOP_UTF8") |  |
| **U** | * [`qUncompress()`](QtCore_globals.html#PySide6.QtCore.qUncompress "PySide6.QtCore.qUncompress") | * [`qUnregisterResourceData()`](QtCore_globals.html#PySide6.QtCore.qUnregisterResourceData "PySide6.QtCore.qUnregisterResourceData") |  |
| **V** | * [`qVersion()`](QtCore_globals.html#PySide6.QtCore.qVersion "PySide6.QtCore.qVersion") | | |
| **W** | * [`qWarning()`](QtCore_globals.html#PySide6.QtCore.qWarning "PySide6.QtCore.qWarning") | | |
## List of Enumerations[Â¶](#list-of-enumerations "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **C** | * [`QCborKnownTags`](QtCore_globals.html#PySide6.QtCore.QCborKnownTags "PySide6.QtCore.QCborKnownTags") | * [`QCborSimpleType`](QtCore_globals.html#PySide6.QtCore.QCborSimpleType "PySide6.QtCore.QCborSimpleType") | * [`QCborTag`](QtCore_globals.html#PySide6.QtCore.QCborTag "PySide6.QtCore.QCborTag") |
| **Q** | * [`QtMsgType`](QtCore_globals.html#PySide6.QtCore.QtMsgType "PySide6.QtCore.QtMsgType") | | |
---
<!-- Source: https://doc.qt.io/qtforpython-6/PySide6/QtGui/index.html#module-PySide6.QtGui -->
# PySide6.QtGui[Â¶](#pyside6-qtgui "Link to this heading")
* [Functions](QtGui_globals.html)
* [PySide6.QtGui.QAbstractFileIconProvider](QAbstractFileIconProvider.html)
* [PySide6.QtGui.QAbstractTextDocumentLayout](QAbstractTextDocumentLayout.html)
* [PySide6.QtGui.QAccessibilityHints](QAccessibilityHints.html)
* [PySide6.QtGui.QAccessible](QAccessible.html)
* [PySide6.QtGui.QAccessibleActionInterface](QAccessibleActionInterface.html)
* [PySide6.QtGui.QAccessibleAnnouncementEvent](QAccessibleAnnouncementEvent.html)
* [PySide6.QtGui.QAccessibleAttributesInterface](QAccessibleAttributesInterface.html)
* [PySide6.QtGui.QAccessibleEditableTextInterface](QAccessibleEditableTextInterface.html)
* [PySide6.QtGui.QAccessibleEvent](QAccessibleEvent.html)
* [PySide6.QtGui.QAccessibleInterface](QAccessibleInterface.html)
* [PySide6.QtGui.QAccessibleObject](QAccessibleObject.html)
* [PySide6.QtGui.QAccessibleSelectionInterface](QAccessibleSelectionInterface.html)
* [PySide6.QtGui.QAccessibleStateChangeEvent](QAccessibleStateChangeEvent.html)
* [PySide6.QtGui.QAccessibleTableCellInterface](QAccessibleTableCellInterface.html)
* [PySide6.QtGui.QAccessibleTableModelChangeEvent](QAccessibleTableModelChangeEvent.html)
* [PySide6.QtGui.QAccessibleTextCursorEvent](QAccessibleTextCursorEvent.html)
* [PySide6.QtGui.QAccessibleTextInsertEvent](QAccessibleTextInsertEvent.html)
* [PySide6.QtGui.QAccessibleTextInterface](QAccessibleTextInterface.html)
* [PySide6.QtGui.QAccessibleTextRemoveEvent](QAccessibleTextRemoveEvent.html)
* [PySide6.QtGui.QAccessibleTextSelectionEvent](QAccessibleTextSelectionEvent.html)
* [PySide6.QtGui.QAccessibleTextUpdateEvent](QAccessibleTextUpdateEvent.html)
* [PySide6.QtGui.QAccessibleValueChangeEvent](QAccessibleValueChangeEvent.html)
* [PySide6.QtGui.QAccessibleValueInterface](QAccessibleValueInterface.html)
* [PySide6.QtGui.QAction](QAction.html)
* [PySide6.QtGui.QActionEvent](QActionEvent.html)
* [PySide6.QtGui.QActionGroup](QActionGroup.html)
* [PySide6.QtGui.QBackingStore](QBackingStore.html)
* [PySide6.QtGui.QBitmap](QBitmap.html)
* [PySide6.QtGui.QBrush](QBrush.html)
* [PySide6.QtGui.QChildWindowEvent](QChildWindowEvent.html)
* [PySide6.QtGui.QClipboard](QClipboard.html)
* [PySide6.QtGui.QCloseEvent](QCloseEvent.html)
* [PySide6.QtGui.QColor](QColor.html)
* [PySide6.QtGui.QColorConstants](QColorConstants.html)
* [PySide6.QtGui.QColorSpace](QColorSpace.html)
* [PySide6.QtGui.QColorTransform](QColorTransform.html)
* [PySide6.QtGui.QConicalGradient](QConicalGradient.html)
* [PySide6.QtGui.QContextMenuEvent](QContextMenuEvent.html)
* [PySide6.QtGui.QCursor](QCursor.html)
* [PySide6.QtGui.QDesktopServices](QDesktopServices.html)
* [PySide6.QtGui.QDoubleValidator](QDoubleValidator.html)
* [PySide6.QtGui.QDrag](QDrag.html)
* [PySide6.QtGui.QDragEnterEvent](QDragEnterEvent.html)
* [PySide6.QtGui.QDragLeaveEvent](QDragLeaveEvent.html)
* [PySide6.QtGui.QDragMoveEvent](QDragMoveEvent.html)
* [PySide6.QtGui.QDropEvent](QDropEvent.html)
* [PySide6.QtGui.QEnterEvent](QEnterEvent.html)
* [PySide6.QtGui.QEventPoint](QEventPoint.html)
* [PySide6.QtGui.QExposeEvent](QExposeEvent.html)
* [PySide6.QtGui.QFileOpenEvent](QFileOpenEvent.html)
* [PySide6.QtGui.QFocusEvent](QFocusEvent.html)
* [PySide6.QtGui.QFont](QFont.html)
* [PySide6.QtGui.QFontDatabase](QFontDatabase.html)
* [PySide6.QtGui.QFontInfo](QFontInfo.html)
* [PySide6.QtGui.QFontMetrics](QFontMetrics.html)
* [PySide6.QtGui.QFontMetricsF](QFontMetricsF.html)
* [PySide6.QtGui.QFontVariableAxis](QFontVariableAxis.html)
* [PySide6.QtGui.QGlyphRun](QGlyphRun.html)
* [PySide6.QtGui.QGradient](QGradient.html)
* [PySide6.QtGui.QGuiApplication](QGuiApplication.html)
* [PySide6.QtGui.QHelpEvent](QHelpEvent.html)
* [PySide6.QtGui.QHideEvent](QHideEvent.html)
* [PySide6.QtGui.QHoverEvent](QHoverEvent.html)
* [PySide6.QtGui.QIcon](QIcon.html)
* [PySide6.QtGui.QIconDragEvent](QIconDragEvent.html)
* [PySide6.QtGui.QIconEngine](QIconEngine.html)
* [PySide6.QtGui.QImage](QImage.html)
* [PySide6.QtGui.QImageIOHandler](QImageIOHandler.html)
* [PySide6.QtGui.QImageReader](QImageReader.html)
* [PySide6.QtGui.QImageWriter](QImageWriter.html)
* [PySide6.QtGui.QInputDevice](QInputDevice.html)
* [PySide6.QtGui.QInputEvent](QInputEvent.html)
* [PySide6.QtGui.QInputMethod](QInputMethod.html)
* [PySide6.QtGui.QInputMethodEvent](QInputMethodEvent.html)
* [PySide6.QtGui.QInputMethodQueryEvent](QInputMethodQueryEvent.html)
* [PySide6.QtGui.QIntValidator](QIntValidator.html)
* [PySide6.QtGui.QKeyEvent](QKeyEvent.html)
* [PySide6.QtGui.QKeySequence](QKeySequence.html)
* [PySide6.QtGui.QLinearGradient](QLinearGradient.html)
* [PySide6.QtGui.QMatrix2x2](QMatrix2x2.html)
* [PySide6.QtGui.QMatrix2x3](QMatrix2x3.html)
* [PySide6.QtGui.QMatrix2x4](QMatrix2x4.html)
* [PySide6.QtGui.QMatrix3x2](QMatrix3x2.html)
* [PySide6.QtGui.QMatrix3x3](QMatrix3x3.html)
* [PySide6.QtGui.QMatrix3x4](QMatrix3x4.html)
* [PySide6.QtGui.QMatrix4x2](QMatrix4x2.html)
* [PySide6.QtGui.QMatrix4x3](QMatrix4x3.html)
* [PySide6.QtGui.QMatrix4x4](QMatrix4x4.html)
* [PySide6.QtGui.QMouseEvent](QMouseEvent.html)
* [PySide6.QtGui.QMoveEvent](QMoveEvent.html)
* [PySide6.QtGui.QMovie](QMovie.html)
* [PySide6.QtGui.QNativeGestureEvent](QNativeGestureEvent.html)
* [PySide6.QtGui.QNativeInterface](QNativeInterface.html)
* [PySide6.QtGui.QOffscreenSurface](QOffscreenSurface.html)
* [PySide6.QtGui.QOpenGLContext](QOpenGLContext.html)
* [PySide6.QtGui.QOpenGLContextGroup](QOpenGLContextGroup.html)
* [PySide6.QtGui.QOpenGLExtraFunctions](QOpenGLExtraFunctions.html)
* [PySide6.QtGui.QOpenGLFunctions](QOpenGLFunctions.html)
* [PySide6.QtGui.QPageLayout](QPageLayout.html)
* [PySide6.QtGui.QPageRanges](QPageRanges.html)
* [PySide6.QtGui.QPageSize](QPageSize.html)
* [PySide6.QtGui.QPagedPaintDevice](QPagedPaintDevice.html)
* [PySide6.QtGui.QPaintDevice](QPaintDevice.html)
* [PySide6.QtGui.QPaintDeviceWindow](QPaintDeviceWindow.html)
* [PySide6.QtGui.QPaintEngine](QPaintEngine.html)
* [PySide6.QtGui.QPaintEngineState](QPaintEngineState.html)
* [PySide6.QtGui.QPaintEvent](QPaintEvent.html)
* [PySide6.QtGui.QPainter](QPainter.html)
* [PySide6.QtGui.QPainterPath](QPainterPath.html)
* [PySide6.QtGui.QPainterPathStroker](QPainterPathStroker.html)
* [PySide6.QtGui.QPainterStateGuard](QPainterStateGuard.html)
* [PySide6.QtGui.QPalette](QPalette.html)
* [PySide6.QtGui.QPdfOutputIntent](QPdfOutputIntent.html)
* [PySide6.QtGui.QPdfWriter](QPdfWriter.html)
* [PySide6.QtGui.QPen](QPen.html)
* [PySide6.QtGui.QPicture](QPicture.html)
* [PySide6.QtGui.QPixelFormat](QPixelFormat.html)
* [PySide6.QtGui.QPixmap](QPixmap.html)
* [PySide6.QtGui.QPixmapCache](QPixmapCache.html)
* [PySide6.QtGui.QPlatformSurfaceEvent](QPlatformSurfaceEvent.html)
* [PySide6.QtGui.QPointerEvent](QPointerEvent.html)
* [PySide6.QtGui.QPointingDevice](QPointingDevice.html)
* [PySide6.QtGui.QPointingDeviceUniqueId](QPointingDeviceUniqueId.html)
* [PySide6.QtGui.QPolygon](QPolygon.html)
* [PySide6.QtGui.QPolygonF](QPolygonF.html)
* [PySide6.QtGui.QQuaternion](QQuaternion.html)
* [PySide6.QtGui.QRadialGradient](QRadialGradient.html)
* [PySide6.QtGui.QRasterWindow](QRasterWindow.html)
* [PySide6.QtGui.QRawFont](QRawFont.html)
* [PySide6.QtGui.QRegion](QRegion.html)
* [PySide6.QtGui.QRegularExpressionValidator](QRegularExpressionValidator.html)
* [PySide6.QtGui.QResizeEvent](QResizeEvent.html)
* [PySide6.QtGui.QRgba64](QRgba64.html)
* [PySide6.QtGui.QRhi](QRhi.html)
* [PySide6.QtGui.QRhiAdapter](QRhiAdapter.html)
* [PySide6.QtGui.QRhiBuffer](QRhiBuffer.html)
* [PySide6.QtGui.QRhiColorAttachment](QRhiColorAttachment.html)
* [PySide6.QtGui.QRhiCommandBuffer](QRhiCommandBuffer.html)
* [PySide6.QtGui.QRhiComputePipeline](QRhiComputePipeline.html)
* [PySide6.QtGui.QRhiDepthStencilClearValue](QRhiDepthStencilClearValue.html)
* [PySide6.QtGui.QRhiDriverInfo](QRhiDriverInfo.html)
* [PySide6.QtGui.QRhiGles2InitParams](QRhiGles2InitParams.html)
* [PySide6.QtGui.QRhiGles2NativeHandles](QRhiGles2NativeHandles.html)
* [PySide6.QtGui.QRhiGraphicsPipeline](QRhiGraphicsPipeline.html)
* [PySide6.QtGui.QRhiInitParams](QRhiInitParams.html)
* [PySide6.QtGui.QRhiNativeHandles](QRhiNativeHandles.html)
* [PySide6.QtGui.QRhiNullInitParams](QRhiNullInitParams.html)
* [PySide6.QtGui.QRhiReadbackDescription](QRhiReadbackDescription.html)
* [PySide6.QtGui.QRhiReadbackResult](QRhiReadbackResult.html)
* [PySide6.QtGui.QRhiRenderBuffer](QRhiRenderBuffer.html)
* [PySide6.QtGui.QRhiRenderPassDescriptor](QRhiRenderPassDescriptor.html)
* [PySide6.QtGui.QRhiRenderTarget](QRhiRenderTarget.html)
* [PySide6.QtGui.QRhiResource](QRhiResource.html)
* [PySide6.QtGui.QRhiResourceUpdateBatch](QRhiResourceUpdateBatch.html)
* [PySide6.QtGui.QRhiSampler](QRhiSampler.html)
* [PySide6.QtGui.QRhiScissor](QRhiScissor.html)
* [PySide6.QtGui.QRhiShaderResourceBinding](QRhiShaderResourceBinding.html)
* [PySide6.QtGui.QRhiShaderResourceBindings](QRhiShaderResourceBindings.html)
* [PySide6.QtGui.QRhiShaderStage](QRhiShaderStage.html)
* [PySide6.QtGui.QRhiStats](QRhiStats.html)
* [PySide6.QtGui.QRhiSwapChain](QRhiSwapChain.html)
* [PySide6.QtGui.QRhiSwapChainRenderTarget](QRhiSwapChainRenderTarget.html)
* [PySide6.QtGui.QRhiTexture](QRhiTexture.html)
* [PySide6.QtGui.QRhiTextureCopyDescription](QRhiTextureCopyDescription.html)
* [PySide6.QtGui.QRhiTextureRenderTarget](QRhiTextureRenderTarget.html)
* [PySide6.QtGui.QRhiTextureRenderTargetDescription](QRhiTextureRenderTargetDescription.html)
* [PySide6.QtGui.QRhiTextureSubresourceUploadDescription](QRhiTextureSubresourceUploadDescription.html)
* [PySide6.QtGui.QRhiTextureUploadDescription](QRhiTextureUploadDescription.html)
* [PySide6.QtGui.QRhiTextureUploadEntry](QRhiTextureUploadEntry.html)
* [PySide6.QtGui.QRhiVertexInputAttribute](QRhiVertexInputAttribute.html)
* [PySide6.QtGui.QRhiVertexInputBinding](QRhiVertexInputBinding.html)
* [PySide6.QtGui.QRhiVertexInputLayout](QRhiVertexInputLayout.html)
* [PySide6.QtGui.QRhiViewport](QRhiViewport.html)
* [PySide6.QtGui.QScreen](QScreen.html)
* [PySide6.QtGui.QScrollEvent](QScrollEvent.html)
* [PySide6.QtGui.QScrollPrepareEvent](QScrollPrepareEvent.html)
* [PySide6.QtGui.QSessionManager](QSessionManager.html)
* [PySide6.QtGui.QShader](QShader.html)
* [PySide6.QtGui.QShaderCode](QShaderCode.html)
* [PySide6.QtGui.QShaderKey](QShaderKey.html)
* [PySide6.QtGui.QShaderVersion](QShaderVersion.html)
* [PySide6.QtGui.QShortcut](QShortcut.html)
* [PySide6.QtGui.QShortcutEvent](QShortcutEvent.html)
* [PySide6.QtGui.QShowEvent](QShowEvent.html)
* [PySide6.QtGui.QSinglePointEvent](QSinglePointEvent.html)
* [PySide6.QtGui.QStandardItem](QStandardItem.html)
* [PySide6.QtGui.QStandardItemModel](QStandardItemModel.html)
* [PySide6.QtGui.QStaticText](QStaticText.html)
* [PySide6.QtGui.QStatusTipEvent](QStatusTipEvent.html)
* [PySide6.QtGui.QStyleHints](QStyleHints.html)
* [PySide6.QtGui.QSurface](QSurface.html)
* [PySide6.QtGui.QSurfaceFormat](QSurfaceFormat.html)
* [PySide6.QtGui.QSyntaxHighlighter](QSyntaxHighlighter.html)
* [PySide6.QtGui.QTabletEvent](QTabletEvent.html)
* [PySide6.QtGui.QTextBlock](QTextBlock.html)
* [PySide6.QtGui.QTextBlockFormat](QTextBlockFormat.html)
* [PySide6.QtGui.QTextBlockGroup](QTextBlockGroup.html)
* [PySide6.QtGui.QTextBlockUserData](QTextBlockUserData.html)
* [PySide6.QtGui.QTextCharFormat](QTextCharFormat.html)
* [PySide6.QtGui.QTextCursor](QTextCursor.html)
* [PySide6.QtGui.QTextDocument](QTextDocument.html)
* [PySide6.QtGui.QTextDocumentFragment](QTextDocumentFragment.html)
* [PySide6.QtGui.QTextDocumentWriter](QTextDocumentWriter.html)
* [PySide6.QtGui.QTextFormat](QTextFormat.html)
* [PySide6.QtGui.QTextFragment](QTextFragment.html)
* [PySide6.QtGui.QTextFrame](QTextFrame.html)
* [PySide6.QtGui.QTextFrameFormat](QTextFrameFormat.html)
* [PySide6.QtGui.QTextImageFormat](QTextImageFormat.html)
* [PySide6.QtGui.QTextInlineObject](QTextInlineObject.html)
* [PySide6.QtGui.QTextItem](QTextItem.html)
* [PySide6.QtGui.QTextLayout](QTextLayout.html)
* [PySide6.QtGui.QTextLength](QTextLength.html)
* [PySide6.QtGui.QTextLine](QTextLine.html)
* [PySide6.QtGui.QTextList](QTextList.html)
* [PySide6.QtGui.QTextListFormat](QTextListFormat.html)
* [PySide6.QtGui.QTextObject](QTextObject.html)
* [PySide6.QtGui.QTextObjectInterface](QTextObjectInterface.html)
* [PySide6.QtGui.QTextOption](QTextOption.html)
* [PySide6.QtGui.QTextTable](QTextTable.html)
* [PySide6.QtGui.QTextTableCell](QTextTableCell.html)
* [PySide6.QtGui.QTextTableCellFormat](QTextTableCellFormat.html)
* [PySide6.QtGui.QTextTableFormat](QTextTableFormat.html)
* [PySide6.QtGui.QToolBarChangeEvent](QToolBarChangeEvent.html)
* [PySide6.QtGui.QTouchEvent](QTouchEvent.html)
* [PySide6.QtGui.QTransform](QTransform.html)
* [PySide6.QtGui.QUndoCommand](QUndoCommand.html)
* [PySide6.QtGui.QUndoGroup](QUndoGroup.html)
* [PySide6.QtGui.QUndoStack](QUndoStack.html)
* [PySide6.QtGui.QValidator](QValidator.html)
* [PySide6.QtGui.QVector2D](QVector2D.html)
* [PySide6.QtGui.QVector3D](QVector3D.html)
* [PySide6.QtGui.QVector4D](QVector4D.html)
* [PySide6.QtGui.QWhatsThisClickedEvent](QWhatsThisClickedEvent.html)
* [PySide6.QtGui.QWheelEvent](QWheelEvent.html)
* [PySide6.QtGui.QWindow](QWindow.html)
* [PySide6.QtGui.QWindowStateChangeEvent](QWindowStateChangeEvent.html)
* [PySide6.QtGui.Qt](Qt.html)
## Detailed Description[Â¶](#detailed-description "Link to this heading")
The Qt GUI module provides classes for windowing system integration,
event handling, OpenGL and OpenGL ES integration, 2D graphics, basic
imaging, fonts, and text. These classes are used internally by Qtâs
user interface technologies and can also be used directly, for
instance to write applications using low-level OpenGL ES graphics
APIs.
For application developers writing user interfaces, Qt provides higher
level APIs, like Qt Quick, that are much more suitable than the
enablers found in the Qt GUI module.
### Application Windows[Â¶](#application-windows "Link to this heading")
The most important classes in the Qt GUI module are
[`QGuiApplication`](QGuiApplication.html#PySide6.QtGui.QGuiApplication "PySide6.QtGui.QGuiApplication"),
[`QWindow`](QWindow.html#PySide6.QtGui.QWindow "PySide6.QtGui.QWindow") and [`QScreen`](QScreen.html#PySide6.QtGui.QScreen "PySide6.QtGui.QScreen").
A Qt application that wants to show content on screen will need to make
use of these.
[`QGuiApplication`](QGuiApplication.html#PySide6.QtGui.QGuiApplication "PySide6.QtGui.QGuiApplication") contains the
main event loop, where all events from the window system and other
sources are processed and dispatched. It also handles the
applicationâs initialization and finalization.
The [`QWindow`](QWindow.html#PySide6.QtGui.QWindow "PySide6.QtGui.QWindow") class represents a window
in the underlying windowing system. It provides a number of virtual
functions to handle events ( [`QEvent`](../QtCore/QEvent.html#PySide6.QtCore.QEvent "PySide6.QtCore.QEvent") )
from the windowing system, such as touch-input, exposure, focus, key
strokes, and geometry changes.
### 2D Graphics[Â¶](#d-graphics "Link to this heading")
The Qt GUI module contains classes for 2D graphics, imaging, fonts,
and advanced typography.
A [`QWindow`](QWindow.html#PySide6.QtGui.QWindow "PySide6.QtGui.QWindow") created with the surface
type [`RasterSurface`](QSurface.html#PySide6.QtGui.QSurface.SurfaceType "PySide6.QtGui.QSurface.SurfaceType") can be used in
combination with [`QBackingStore`](QBackingStore.html#PySide6.QtGui.QBackingStore "PySide6.QtGui.QBackingStore")
and [`QPainter`](QPainter.html#PySide6.QtGui.QPainter "PySide6.QtGui.QPainter") , Qtâs highly optimized
2D vector graphics API. [`QPainter`](QPainter.html#PySide6.QtGui.QPainter "PySide6.QtGui.QPainter")
supports drawing lines, polygons, vector paths, images, and text. For
more information, see [Paint System](../../overviews/qtgui-paintsystem.html#paint-system) and
Raster Window Example .
Qt can load and save images using the
[`QImage`](QImage.html#PySide6.QtGui.QImage "PySide6.QtGui.QImage") and
[`QPixmap`](QPixmap.html#PySide6.QtGui.QPixmap "PySide6.QtGui.QPixmap") classes. By default, Qt
supports the most common image formats including JPEG and PNG among
others. Users can add support for additional formats via the
`QImageIOPlugin` class. For more information,
see [Reading and Writing Image
Files](../../overviews/qtgui-paintsystem-images.html#reading-and-writing-image-files) .
Typography in Qt is done with
[`QTextDocument`](QTextDocument.html#PySide6.QtGui.QTextDocument "PySide6.QtGui.QTextDocument") , which uses the
[`QPainter`](QPainter.html#PySide6.QtGui.QPainter "PySide6.QtGui.QPainter") API in combination with Qtâs
font classes, primarily [`QFont`](QFont.html#PySide6.QtGui.QFont "PySide6.QtGui.QFont") .
Applications that prefer more low-level APIs to text and font handling
can use classes like [`QRawFont`](QRawFont.html#PySide6.QtGui.QRawFont "PySide6.QtGui.QRawFont") and
[`QGlyphRun`](QGlyphRun.html#PySide6.QtGui.QGlyphRun "PySide6.QtGui.QGlyphRun") .
### OpenGL and OpenGL ES Integration[Â¶](#opengl-and-opengl-es-integration "Link to this heading")
[`QWindow`](QWindow.html#PySide6.QtGui.QWindow "PySide6.QtGui.QWindow") supports rendering using
OpenGL and OpenGL ES, depending on what the platform supports. OpenGL
rendering is enabled by setting the
[`QWindow`](QWindow.html#PySide6.QtGui.QWindow "PySide6.QtGui.QWindow") âs surface type to
[`OpenGLSurface`](QSurface.html#PySide6.QtGui.QSurface.SurfaceType "PySide6.QtGui.QSurface.SurfaceType") , choosing the format
attributes with [`QSurfaceFormat`](QSurfaceFormat.html#PySide6.QtGui.QSurfaceFormat "PySide6.QtGui.QSurfaceFormat")
, and then creating a
[`QOpenGLContext`](QOpenGLContext.html#PySide6.QtGui.QOpenGLContext "PySide6.QtGui.QOpenGLContext") to manage the
native OpenGL context. In addition, Qt has
[`QOpenGLPaintDevice`](../QtOpenGL/QOpenGLPaintDevice.html#PySide6.QtOpenGL.QOpenGLPaintDevice "PySide6.QtOpenGL.QOpenGLPaintDevice") ,
which enables the use of OpenGL accelerated
[`QPainter`](QPainter.html#PySide6.QtGui.QPainter "PySide6.QtGui.QPainter") rendering, as well as
convenience classes that simplify the writing of OpenGL code and hides
the complexities of extension handling and the differences between
OpenGL ES 2 and desktop OpenGL. The convenience classes include
[`QOpenGLFunctions`](QOpenGLFunctions.html#PySide6.QtGui.QOpenGLFunctions "PySide6.QtGui.QOpenGLFunctions") that lets an
application use all the OpenGL ES 2 functions on desktop OpenGL
without having to manually resolve the OpenGL function pointers. This
enables cross-platform development of applications targeting mobile or
embedded devices, and provides classes that wrap native OpenGL
functionality in a simpler Qt API.
For more information, see the OpenGL Window Example .
The Qt GUI module also contains a few math classes to aid with the
most common mathematical operations related to 3D graphics. These
classes include [`QMatrix4x4`](QMatrix4x4.html#PySide6.QtGui.QMatrix4x4 "PySide6.QtGui.QMatrix4x4") ,
[`QVector4D`](QVector4D.html#PySide6.QtGui.QVector4D "PySide6.QtGui.QVector4D") , and
[`QQuaternion`](QQuaternion.html#PySide6.QtGui.QQuaternion "PySide6.QtGui.QQuaternion") .
A [`QWindow`](QWindow.html#PySide6.QtGui.QWindow "PySide6.QtGui.QWindow") created with the
[`OpenGLSurface`](QSurface.html#PySide6.QtGui.QSurface.SurfaceType "PySide6.QtGui.QSurface.SurfaceType") can be used in combination
with [`QPainter`](QPainter.html#PySide6.QtGui.QPainter "PySide6.QtGui.QPainter") and
[`QOpenGLPaintDevice`](../QtOpenGL/QOpenGLPaintDevice.html#PySide6.QtOpenGL.QOpenGLPaintDevice "PySide6.QtOpenGL.QOpenGLPaintDevice") to
have OpenGL hardware-accelerated 2D graphics by sacrificing some of
the visual quality.
### Drag and Drop[Â¶](#drag-and-drop "Link to this heading")
Qt GUI includes support for drag and drop. The
[Drag and Drop](../../overviews/qtgui-dnd.html#drag-and-drop) overview has more information.
### Using the Module[Â¶](#using-the-module "Link to this heading")
To include the definitions of modules classes, use the following
directive:
```
import PySide6.QtGui
```
## List of Classes by Function[Â¶](#list-of-classes-by-function "Link to this heading")
> * [Painting Classes](../../groups/qtgui-painting.html#painting-classes)
> * [Rendering in 3D](../../groups/qtgui-painting-3d.html#rendering-in-3d)
> * [Rich Text Processing APIs](../../groups/qtgui-richtext-processing.html#rich-text-processing-apis)
## List of Classes[Â¶](#list-of-classes "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **A** | * [`Attribute`](QInputMethodEvent.html#PySide6.QtGui.QInputMethodEvent.Attribute "PySide6.QtGui.QInputMethodEvent.Attribute") | * [`Axes`](QQuaternion.html#PySide6.QtGui.QQuaternion.Axes "PySide6.QtGui.QQuaternion.Axes") | * [`QAbstractFileIconProvider`](QAbstractFileIconProvider.html#PySide6.QtGui.QAbstractFileIconProvider "PySide6.QtGui.QAbstractFileIconProvider") |
|  | * [`QAbstractTextDocumentLayout`](QAbstractTextDocumentLayout.html#PySide6.QtGui.QAbstractTextDocumentLayout "PySide6.QtGui.QAbstractTextDocumentLayout") | * [`QAccessibilityHints`](QAccessibilityHints.html#PySide6.QtGui.QAccessibilityHints "PySide6.QtGui.QAccessibilityHints") | * [`QAccessible`](QAccessible.html#PySide6.QtGui.QAccessible "PySide6.QtGui.QAccessible") |
|  | * [`QAccessibleActionInterface`](QAccessibleActionInterface.html#PySide6.QtGui.QAccessibleActionInterface "PySide6.QtGui.QAccessibleActionInterface") | * [`QAccessibleAnnouncementEvent`](QAccessibleAnnouncementEvent.html#PySide6.QtGui.QAccessibleAnnouncementEvent "PySide6.QtGui.QAccessibleAnnouncementEvent") | * [`QAccessibleAttributesInterface`](QAccessibleAttributesInterface.html#PySide6.QtGui.QAccessibleAttributesInterface "PySide6.QtGui.QAccessibleAttributesInterface") |
|  | * [`QAccessibleEditableTextInterface`](QAccessibleEditableTextInterface.html#PySide6.QtGui.QAccessibleEditableTextInterface "PySide6.QtGui.QAccessibleEditableTextInterface") | * [`QAccessibleEvent`](QAccessibleEvent.html#PySide6.QtGui.QAccessibleEvent "PySide6.QtGui.QAccessibleEvent") | * [`QAccessibleInterface`](QAccessibleInterface.html#PySide6.QtGui.QAccessibleInterface "PySide6.QtGui.QAccessibleInterface") |
|  | * [`QAccessibleObject`](QAccessibleObject.html#PySide6.QtGui.QAccessibleObject "PySide6.QtGui.QAccessibleObject") | * [`QAccessibleSelectionInterface`](QAccessibleSelectionInterface.html#PySide6.QtGui.QAccessibleSelectionInterface "PySide6.QtGui.QAccessibleSelectionInterface") | * [`QAccessibleStateChangeEvent`](QAccessibleStateChangeEvent.html#PySide6.QtGui.QAccessibleStateChangeEvent "PySide6.QtGui.QAccessibleStateChangeEvent") |
|  | * [`QAccessibleTableCellInterface`](QAccessibleTableCellInterface.html#PySide6.QtGui.QAccessibleTableCellInterface "PySide6.QtGui.QAccessibleTableCellInterface") | * [`QAccessibleTableModelChangeEvent`](QAccessibleTableModelChangeEvent.html#PySide6.QtGui.QAccessibleTableModelChangeEvent "PySide6.QtGui.QAccessibleTableModelChangeEvent") | * [`QAccessibleTextCursorEvent`](QAccessibleTextCursorEvent.html#PySide6.QtGui.QAccessibleTextCursorEvent "PySide6.QtGui.QAccessibleTextCursorEvent") |
|  | * [`QAccessibleTextInsertEvent`](QAccessibleTextInsertEvent.html#PySide6.QtGui.QAccessibleTextInsertEvent "PySide6.QtGui.QAccessibleTextInsertEvent") | * [`QAccessibleTextInterface`](QAccessibleTextInterface.html#PySide6.QtGui.QAccessibleTextInterface "PySide6.QtGui.QAccessibleTextInterface") | * [`QAccessibleTextRemoveEvent`](QAccessibleTextRemoveEvent.html#PySide6.QtGui.QAccessibleTextRemoveEvent "PySide6.QtGui.QAccessibleTextRemoveEvent") |
|  | * [`QAccessibleTextSelectionEvent`](QAccessibleTextSelectionEvent.html#PySide6.QtGui.QAccessibleTextSelectionEvent "PySide6.QtGui.QAccessibleTextSelectionEvent") | * [`QAccessibleTextUpdateEvent`](QAccessibleTextUpdateEvent.html#PySide6.QtGui.QAccessibleTextUpdateEvent "PySide6.QtGui.QAccessibleTextUpdateEvent") | * [`QAccessibleValueChangeEvent`](QAccessibleValueChangeEvent.html#PySide6.QtGui.QAccessibleValueChangeEvent "PySide6.QtGui.QAccessibleValueChangeEvent") |
|  | * [`QAccessibleValueInterface`](QAccessibleValueInterface.html#PySide6.QtGui.QAccessibleValueInterface "PySide6.QtGui.QAccessibleValueInterface") | * [`QAction`](QAction.html#PySide6.QtGui.QAction "PySide6.QtGui.QAction") | * [`QActionEvent`](QActionEvent.html#PySide6.QtGui.QActionEvent "PySide6.QtGui.QActionEvent") |
|  | * [`QActionGroup`](QActionGroup.html#PySide6.QtGui.QActionGroup "PySide6.QtGui.QActionGroup") |  | |
| **B** | * [`QBackingStore`](QBackingStore.html#PySide6.QtGui.QBackingStore "PySide6.QtGui.QBackingStore") | * [`QBitmap`](QBitmap.html#PySide6.QtGui.QBitmap "PySide6.QtGui.QBitmap") | * [`QBrush`](QBrush.html#PySide6.QtGui.QBrush "PySide6.QtGui.QBrush") |
| **C** | * [`QChildWindowEvent`](QChildWindowEvent.html#PySide6.QtGui.QChildWindowEvent "PySide6.QtGui.QChildWindowEvent") | * [`QClipboard`](QClipboard.html#PySide6.QtGui.QClipboard "PySide6.QtGui.QClipboard") | * [`QCloseEvent`](QCloseEvent.html#PySide6.QtGui.QCloseEvent "PySide6.QtGui.QCloseEvent") |
|  | * [`QColor`](QColor.html#PySide6.QtGui.QColor "PySide6.QtGui.QColor") | * [`QColorConstants`](QColorConstants.html#PySide6.QtGui.QColorConstants "PySide6.QtGui.QColorConstants") | * [`QColorSpace`](QColorSpace.html#PySide6.QtGui.QColorSpace "PySide6.QtGui.QColorSpace") |
|  | * [`QColorTransform`](QColorTransform.html#PySide6.QtGui.QColorTransform "PySide6.QtGui.QColorTransform") | * [`QConicalGradient`](QConicalGradient.html#PySide6.QtGui.QConicalGradient "PySide6.QtGui.QConicalGradient") | * [`QContextMenuEvent`](QContextMenuEvent.html#PySide6.QtGui.QContextMenuEvent "PySide6.QtGui.QContextMenuEvent") |
|  | * [`QCursor`](QCursor.html#PySide6.QtGui.QCursor "PySide6.QtGui.QCursor") |  | |
| **D** | * [`Data`](QRhiShaderResourceBinding.html#PySide6.QtGui.QRhiShaderResourceBinding.Data "PySide6.QtGui.QRhiShaderResourceBinding.Data") | * [`QDesktopServices`](QDesktopServices.html#PySide6.QtGui.QDesktopServices "PySide6.QtGui.QDesktopServices") | * [`QDoubleValidator`](QDoubleValidator.html#PySide6.QtGui.QDoubleValidator "PySide6.QtGui.QDoubleValidator") |
|  | * [`QDrag`](QDrag.html#PySide6.QtGui.QDrag "PySide6.QtGui.QDrag") | * [`QDragEnterEvent`](QDragEnterEvent.html#PySide6.QtGui.QDragEnterEvent "PySide6.QtGui.QDragEnterEvent") | * [`QDragLeaveEvent`](QDragLeaveEvent.html#PySide6.QtGui.QDragLeaveEvent "PySide6.QtGui.QDragLeaveEvent") |
|  | * [`QDragMoveEvent`](QDragMoveEvent.html#PySide6.QtGui.QDragMoveEvent "PySide6.QtGui.QDragMoveEvent") | * [`QDropEvent`](QDropEvent.html#PySide6.QtGui.QDropEvent "PySide6.QtGui.QDropEvent") |  |
| **E** | * [`Element`](QPainterPath.html#PySide6.QtGui.QPainterPath.Element "PySide6.QtGui.QPainterPath.Element") | * [`QEnterEvent`](QEnterEvent.html#PySide6.QtGui.QEnterEvent "PySide6.QtGui.QEnterEvent") | * [`QEventPoint`](QEventPoint.html#PySide6.QtGui.QEventPoint "PySide6.QtGui.QEventPoint") |
|  | * [`QExposeEvent`](QExposeEvent.html#PySide6.QtGui.QExposeEvent "PySide6.QtGui.QExposeEvent") |  | |
| **F** | * [`FormatRange`](QTextLayout.html#PySide6.QtGui.QTextLayout.FormatRange "PySide6.QtGui.QTextLayout.FormatRange") | * [`QFileOpenEvent`](QFileOpenEvent.html#PySide6.QtGui.QFileOpenEvent "PySide6.QtGui.QFileOpenEvent") | * [`QFocusEvent`](QFocusEvent.html#PySide6.QtGui.QFocusEvent "PySide6.QtGui.QFocusEvent") |
|  | * [`QFont`](QFont.html#PySide6.QtGui.QFont "PySide6.QtGui.QFont") | * [`QFontDatabase`](QFontDatabase.html#PySide6.QtGui.QFontDatabase "PySide6.QtGui.QFontDatabase") | * [`QFontInfo`](QFontInfo.html#PySide6.QtGui.QFontInfo "PySide6.QtGui.QFontInfo") |
|  | * [`QFontMetrics`](QFontMetrics.html#PySide6.QtGui.QFontMetrics "PySide6.QtGui.QFontMetrics") | * [`QFontMetricsF`](QFontMetricsF.html#PySide6.QtGui.QFontMetricsF "PySide6.QtGui.QFontMetricsF") | * [`QFontVariableAxis`](QFontVariableAxis.html#PySide6.QtGui.QFontVariableAxis "PySide6.QtGui.QFontVariableAxis") |
| **G** | * [`QGlyphRun`](QGlyphRun.html#PySide6.QtGui.QGlyphRun "PySide6.QtGui.QGlyphRun") | * [`QGradient`](QGradient.html#PySide6.QtGui.QGradient "PySide6.QtGui.QGradient") | * [`QGuiApplication`](QGuiApplication.html#PySide6.QtGui.QGuiApplication "PySide6.QtGui.QGuiApplication") |
| **H** | * [`QHelpEvent`](QHelpEvent.html#PySide6.QtGui.QHelpEvent "PySide6.QtGui.QHelpEvent") | * [`QHideEvent`](QHideEvent.html#PySide6.QtGui.QHideEvent "PySide6.QtGui.QHideEvent") | * [`QHoverEvent`](QHoverEvent.html#PySide6.QtGui.QHoverEvent "PySide6.QtGui.QHoverEvent") |
| **I** | * [`QIcon`](QIcon.html#PySide6.QtGui.QIcon "PySide6.QtGui.QIcon") | * [`QIconDragEvent`](QIconDragEvent.html#PySide6.QtGui.QIconDragEvent "PySide6.QtGui.QIconDragEvent") | * [`QIconEngine`](QIconEngine.html#PySide6.QtGui.QIconEngine "PySide6.QtGui.QIconEngine") |
|  | * [`QImage`](QImage.html#PySide6.QtGui.QImage "PySide6.QtGui.QImage") | * [`QImageIOHandler`](QImageIOHandler.html#PySide6.QtGui.QImageIOHandler "PySide6.QtGui.QImageIOHandler") | * [`QImageReader`](QImageReader.html#PySide6.QtGui.QImageReader "PySide6.QtGui.QImageReader") |
|  | * [`QImageWriter`](QImageWriter.html#PySide6.QtGui.QImageWriter "PySide6.QtGui.QImageWriter") | * [`QInputDevice`](QInputDevice.html#PySide6.QtGui.QInputDevice "PySide6.QtGui.QInputDevice") | * [`QInputEvent`](QInputEvent.html#PySide6.QtGui.QInputEvent "PySide6.QtGui.QInputEvent") |
|  | * [`QInputMethod`](QInputMethod.html#PySide6.QtGui.QInputMethod "PySide6.QtGui.QInputMethod") | * [`QInputMethodEvent`](QInputMethodEvent.html#PySide6.QtGui.QInputMethodEvent "PySide6.QtGui.QInputMethodEvent") | * [`QInputMethodQueryEvent`](QInputMethodQueryEvent.html#PySide6.QtGui.QInputMethodQueryEvent "PySide6.QtGui.QInputMethodQueryEvent") |
|  | * [`QIntValidator`](QIntValidator.html#PySide6.QtGui.QIntValidator "PySide6.QtGui.QIntValidator") | * [`iterator`](QTextFrame.html#PySide6.QtGui.QTextFrame.iterator "PySide6.QtGui.QTextFrame.iterator") | * [`iterator`](QTextBlock.html#PySide6.QtGui.QTextBlock.iterator "PySide6.QtGui.QTextBlock.iterator") |
| **K** | * [`Key`](QPixmapCache.html#PySide6.QtGui.QPixmapCache.Key "PySide6.QtGui.QPixmapCache.Key") | * [`QKeyEvent`](QKeyEvent.html#PySide6.QtGui.QKeyEvent "PySide6.QtGui.QKeyEvent") | * [`QKeySequence`](QKeySequence.html#PySide6.QtGui.QKeySequence "PySide6.QtGui.QKeySequence") |
| **L** | * [`QLinearGradient`](QLinearGradient.html#PySide6.QtGui.QLinearGradient "PySide6.QtGui.QLinearGradient") | | |
| **M** | * [`QMatrix2x2`](QMatrix2x2.html#PySide6.QtGui.QMatrix2x2 "PySide6.QtGui.QMatrix2x2") | * [`QMatrix2x3`](QMatrix2x3.html#PySide6.QtGui.QMatrix2x3 "PySide6.QtGui.QMatrix2x3") | * [`QMatrix2x4`](QMatrix2x4.html#PySide6.QtGui.QMatrix2x4 "PySide6.QtGui.QMatrix2x4") |
|  | * [`QMatrix3x2`](QMatrix3x2.html#PySide6.QtGui.QMatrix3x2 "PySide6.QtGui.QMatrix3x2") | * [`QMatrix3x3`](QMatrix3x3.html#PySide6.QtGui.QMatrix3x3 "PySide6.QtGui.QMatrix3x3") | * [`QMatrix3x4`](QMatrix3x4.html#PySide6.QtGui.QMatrix3x4 "PySide6.QtGui.QMatrix3x4") |
|  | * [`QMatrix4x2`](QMatrix4x2.html#PySide6.QtGui.QMatrix4x2 "PySide6.QtGui.QMatrix4x2") | * [`QMatrix4x3`](QMatrix4x3.html#PySide6.QtGui.QMatrix4x3 "PySide6.QtGui.QMatrix4x3") | * [`QMatrix4x4`](QMatrix4x4.html#PySide6.QtGui.QMatrix4x4 "PySide6.QtGui.QMatrix4x4") |
|  | * [`QMouseEvent`](QMouseEvent.html#PySide6.QtGui.QMouseEvent "PySide6.QtGui.QMouseEvent") | * [`QMoveEvent`](QMoveEvent.html#PySide6.QtGui.QMoveEvent "PySide6.QtGui.QMoveEvent") | * [`QMovie`](QMovie.html#PySide6.QtGui.QMovie "PySide6.QtGui.QMovie") |
| **N** | * [`QNativeGestureEvent`](QNativeGestureEvent.html#PySide6.QtGui.QNativeGestureEvent "PySide6.QtGui.QNativeGestureEvent") | * [`QNativeInterface`](QNativeInterface.html#PySide6.QtGui.QNativeInterface "PySide6.QtGui.QNativeInterface") |  |
| **O** | * [`QOffscreenSurface`](QOffscreenSurface.html#PySide6.QtGui.QOffscreenSurface "PySide6.QtGui.QOffscreenSurface") | * [`QOpenGLContext`](QOpenGLContext.html#PySide6.QtGui.QOpenGLContext "PySide6.QtGui.QOpenGLContext") | * [`QOpenGLContextGroup`](QOpenGLContextGroup.html#PySide6.QtGui.QOpenGLContextGroup "PySide6.QtGui.QOpenGLContextGroup") |
|  | * [`QOpenGLExtraFunctions`](QOpenGLExtraFunctions.html#PySide6.QtGui.QOpenGLExtraFunctions "PySide6.QtGui.QOpenGLExtraFunctions") | * [`QOpenGLFunctions`](QOpenGLFunctions.html#PySide6.QtGui.QOpenGLFunctions "PySide6.QtGui.QOpenGLFunctions") |  |
| **P** | * [`PaintContext`](QAbstractTextDocumentLayout.html#PySide6.QtGui.QAbstractTextDocumentLayout.PaintContext "PySide6.QtGui.QAbstractTextDocumentLayout.PaintContext") | * [`PixmapFragment`](QPainter.html#PySide6.QtGui.QPainter.PixmapFragment "PySide6.QtGui.QPainter.PixmapFragment") | * [`QPageLayout`](QPageLayout.html#PySide6.QtGui.QPageLayout "PySide6.QtGui.QPageLayout") |
|  | * [`QPageRanges`](QPageRanges.html#PySide6.QtGui.QPageRanges "PySide6.QtGui.QPageRanges") | * [`QPageSize`](QPageSize.html#PySide6.QtGui.QPageSize "PySide6.QtGui.QPageSize") | * [`QPagedPaintDevice`](QPagedPaintDevice.html#PySide6.QtGui.QPagedPaintDevice "PySide6.QtGui.QPagedPaintDevice") |
|  | * [`QPaintDevice`](QPaintDevice.html#PySide6.QtGui.QPaintDevice "PySide6.QtGui.QPaintDevice") | * [`QPaintDeviceWindow`](QPaintDeviceWindow.html#PySide6.QtGui.QPaintDeviceWindow "PySide6.QtGui.QPaintDeviceWindow") | * [`QPaintEngine`](QPaintEngine.html#PySide6.QtGui.QPaintEngine "PySide6.QtGui.QPaintEngine") |
|  | * [`QPaintEngineState`](QPaintEngineState.html#PySide6.QtGui.QPaintEngineState "PySide6.QtGui.QPaintEngineState") | * [`QPaintEvent`](QPaintEvent.html#PySide6.QtGui.QPaintEvent "PySide6.QtGui.QPaintEvent") | * [`QPainter`](QPainter.html#PySide6.QtGui.QPainter "PySide6.QtGui.QPainter") |
|  | * [`QPainterPath`](QPainterPath.html#PySide6.QtGui.QPainterPath "PySide6.QtGui.QPainterPath") | * [`QPainterPathStroker`](QPainterPathStroker.html#PySide6.QtGui.QPainterPathStroker "PySide6.QtGui.QPainterPathStroker") | * [`QPainterStateGuard`](QPainterStateGuard.html#PySide6.QtGui.QPainterStateGuard "PySide6.QtGui.QPainterStateGuard") |
|  | * [`QPalette`](QPalette.html#PySide6.QtGui.QPalette "PySide6.QtGui.QPalette") | * [`QPdfOutputIntent`](QPdfOutputIntent.html#PySide6.QtGui.QPdfOutputIntent "PySide6.QtGui.QPdfOutputIntent") | * [`QPdfWriter`](QPdfWriter.html#PySide6.QtGui.QPdfWriter "PySide6.QtGui.QPdfWriter") |
|  | * [`QPen`](QPen.html#PySide6.QtGui.QPen "PySide6.QtGui.QPen") | * [`QPicture`](QPicture.html#PySide6.QtGui.QPicture "PySide6.QtGui.QPicture") | * [`QPixelFormat`](QPixelFormat.html#PySide6.QtGui.QPixelFormat "PySide6.QtGui.QPixelFormat") |
|  | * [`QPixmap`](QPixmap.html#PySide6.QtGui.QPixmap "PySide6.QtGui.QPixmap") | * [`QPixmapCache`](QPixmapCache.html#PySide6.QtGui.QPixmapCache "PySide6.QtGui.QPixmapCache") | * [`QPlatformSurfaceEvent`](QPlatformSurfaceEvent.html#PySide6.QtGui.QPlatformSurfaceEvent "PySide6.QtGui.QPlatformSurfaceEvent") |
|  | * [`QPointerEvent`](QPointerEvent.html#PySide6.QtGui.QPointerEvent "PySide6.QtGui.QPointerEvent") | * [`QPointingDevice`](QPointingDevice.html#PySide6.QtGui.QPointingDevice "PySide6.QtGui.QPointingDevice") | * [`QPointingDeviceUniqueId`](QPointingDeviceUniqueId.html#PySide6.QtGui.QPointingDeviceUniqueId "PySide6.QtGui.QPointingDeviceUniqueId") |
|  | * [`QPolygon`](QPolygon.html#PySide6.QtGui.QPolygon "PySide6.QtGui.QPolygon") | * [`QPolygonF`](QPolygonF.html#PySide6.QtGui.QPolygonF "PySide6.QtGui.QPolygonF") |  |
| **Q** | * [`QQuaternion`](QQuaternion.html#PySide6.QtGui.QQuaternion "PySide6.QtGui.QQuaternion") | * [`Qt`](Qt.html#PySide6.QtGui.Qt "PySide6.QtGui.Qt") |  |
| **R** | * [`QRadialGradient`](QRadialGradient.html#PySide6.QtGui.QRadialGradient "PySide6.QtGui.QRadialGradient") | * [`QRasterWindow`](QRasterWindow.html#PySide6.QtGui.QRasterWindow "PySide6.QtGui.QRasterWindow") | * [`QRawFont`](QRawFont.html#PySide6.QtGui.QRawFont "PySide6.QtGui.QRawFont") |
|  | * [`QRegion`](QRegion.html#PySide6.QtGui.QRegion "PySide6.QtGui.QRegion") | * [`QRegularExpressionValidator`](QRegularExpressionValidator.html#PySide6.QtGui.QRegularExpressionValidator "PySide6.QtGui.QRegularExpressionValidator") | * [`QResizeEvent`](QResizeEvent.html#PySide6.QtGui.QResizeEvent "PySide6.QtGui.QResizeEvent") |
|  | * [`QRgba64`](QRgba64.html#PySide6.QtGui.QRgba64 "PySide6.QtGui.QRgba64") | * [`QRhi`](QRhi.html#PySide6.QtGui.QRhi "PySide6.QtGui.QRhi") | * [`QRhiAdapter`](QRhiAdapter.html#PySide6.QtGui.QRhiAdapter "PySide6.QtGui.QRhiAdapter") |
|  | * [`QRhiBuffer`](QRhiBuffer.html#PySide6.QtGui.QRhiBuffer "PySide6.QtGui.QRhiBuffer") | * [`QRhiColorAttachment`](QRhiColorAttachment.html#PySide6.QtGui.QRhiColorAttachment "PySide6.QtGui.QRhiColorAttachment") | * [`QRhiCommandBuffer`](QRhiCommandBuffer.html#PySide6.QtGui.QRhiCommandBuffer "PySide6.QtGui.QRhiCommandBuffer") |
|  | * [`QRhiComputePipeline`](QRhiComputePipeline.html#PySide6.QtGui.QRhiComputePipeline "PySide6.QtGui.QRhiComputePipeline") | * [`QRhiDepthStencilClearValue`](QRhiDepthStencilClearValue.html#PySide6.QtGui.QRhiDepthStencilClearValue "PySide6.QtGui.QRhiDepthStencilClearValue") | * [`QRhiDriverInfo`](QRhiDriverInfo.html#PySide6.QtGui.QRhiDriverInfo "PySide6.QtGui.QRhiDriverInfo") |
|  | * [`QRhiGles2InitParams`](QRhiGles2InitParams.html#PySide6.QtGui.QRhiGles2InitParams "PySide6.QtGui.QRhiGles2InitParams") | * [`QRhiGles2NativeHandles`](QRhiGles2NativeHandles.html#PySide6.QtGui.QRhiGles2NativeHandles "PySide6.QtGui.QRhiGles2NativeHandles") | * [`QRhiGraphicsPipeline`](QRhiGraphicsPipeline.html#PySide6.QtGui.QRhiGraphicsPipeline "PySide6.QtGui.QRhiGraphicsPipeline") |
|  | * [`QRhiInitParams`](QRhiInitParams.html#PySide6.QtGui.QRhiInitParams "PySide6.QtGui.QRhiInitParams") | * [`QRhiNativeHandles`](QRhiNativeHandles.html#PySide6.QtGui.QRhiNativeHandles "PySide6.QtGui.QRhiNativeHandles") | * [`QRhiNullInitParams`](QRhiNullInitParams.html#PySide6.QtGui.QRhiNullInitParams "PySide6.QtGui.QRhiNullInitParams") |
|  | * [`QRhiReadbackDescription`](QRhiReadbackDescription.html#PySide6.QtGui.QRhiReadbackDescription "PySide6.QtGui.QRhiReadbackDescription") | * [`QRhiReadbackResult`](QRhiReadbackResult.html#PySide6.QtGui.QRhiReadbackResult "PySide6.QtGui.QRhiReadbackResult") | * [`QRhiRenderBuffer`](QRhiRenderBuffer.html#PySide6.QtGui.QRhiRenderBuffer "PySide6.QtGui.QRhiRenderBuffer") |
|  | * [`QRhiRenderPassDescriptor`](QRhiRenderPassDescriptor.html#PySide6.QtGui.QRhiRenderPassDescriptor "PySide6.QtGui.QRhiRenderPassDescriptor") | * [`QRhiRenderTarget`](QRhiRenderTarget.html#PySide6.QtGui.QRhiRenderTarget "PySide6.QtGui.QRhiRenderTarget") | * [`QRhiResource`](QRhiResource.html#PySide6.QtGui.QRhiResource "PySide6.QtGui.QRhiResource") |
|  | * [`QRhiResourceUpdateBatch`](QRhiResourceUpdateBatch.html#PySide6.QtGui.QRhiResourceUpdateBatch "PySide6.QtGui.QRhiResourceUpdateBatch") | * [`QRhiSampler`](QRhiSampler.html#PySide6.QtGui.QRhiSampler "PySide6.QtGui.QRhiSampler") | * [`QRhiScissor`](QRhiScissor.html#PySide6.QtGui.QRhiScissor "PySide6.QtGui.QRhiScissor") |
|  | * [`QRhiShaderResourceBinding`](QRhiShaderResourceBinding.html#PySide6.QtGui.QRhiShaderResourceBinding "PySide6.QtGui.QRhiShaderResourceBinding") | * [`QRhiShaderResourceBindings`](QRhiShaderResourceBindings.html#PySide6.QtGui.QRhiShaderResourceBindings "PySide6.QtGui.QRhiShaderResourceBindings") | * [`QRhiShaderStage`](QRhiShaderStage.html#PySide6.QtGui.QRhiShaderStage "PySide6.QtGui.QRhiShaderStage") |
|  | * [`QRhiStats`](QRhiStats.html#PySide6.QtGui.QRhiStats "PySide6.QtGui.QRhiStats") | * [`QRhiSwapChain`](QRhiSwapChain.html#PySide6.QtGui.QRhiSwapChain "PySide6.QtGui.QRhiSwapChain") | * [`QRhiSwapChainRenderTarget`](QRhiSwapChainRenderTarget.html#PySide6.QtGui.QRhiSwapChainRenderTarget "PySide6.QtGui.QRhiSwapChainRenderTarget") |
|  | * [`QRhiTexture`](QRhiTexture.html#PySide6.QtGui.QRhiTexture "PySide6.QtGui.QRhiTexture") | * [`QRhiTextureCopyDescription`](QRhiTextureCopyDescription.html#PySide6.QtGui.QRhiTextureCopyDescription "PySide6.QtGui.QRhiTextureCopyDescription") | * [`QRhiTextureRenderTarget`](QRhiTextureRenderTarget.html#PySide6.QtGui.QRhiTextureRenderTarget "PySide6.QtGui.QRhiTextureRenderTarget") |
|  | * [`QRhiTextureRenderTargetDescription`](QRhiTextureRenderTargetDescription.html#PySide6.QtGui.QRhiTextureRenderTargetDescription "PySide6.QtGui.QRhiTextureRenderTargetDescription") | * [`QRhiTextureSubresourceUploadDescription`](QRhiTextureSubresourceUploadDescription.html#PySide6.QtGui.QRhiTextureSubresourceUploadDescription "PySide6.QtGui.QRhiTextureSubresourceUploadDescription") | * [`QRhiTextureUploadDescription`](QRhiTextureUploadDescription.html#PySide6.QtGui.QRhiTextureUploadDescription "PySide6.QtGui.QRhiTextureUploadDescription") |
|  | * [`QRhiTextureUploadEntry`](QRhiTextureUploadEntry.html#PySide6.QtGui.QRhiTextureUploadEntry "PySide6.QtGui.QRhiTextureUploadEntry") | * [`QRhiVertexInputAttribute`](QRhiVertexInputAttribute.html#PySide6.QtGui.QRhiVertexInputAttribute "PySide6.QtGui.QRhiVertexInputAttribute") | * [`QRhiVertexInputBinding`](QRhiVertexInputBinding.html#PySide6.QtGui.QRhiVertexInputBinding "PySide6.QtGui.QRhiVertexInputBinding") |
|  | * [`QRhiVertexInputLayout`](QRhiVertexInputLayout.html#PySide6.QtGui.QRhiVertexInputLayout "PySide6.QtGui.QRhiVertexInputLayout") | * [`QRhiViewport`](QRhiViewport.html#PySide6.QtGui.QRhiViewport "PySide6.QtGui.QRhiViewport") | * [`Range`](QPageRanges.html#PySide6.QtGui.QPageRanges.Range "PySide6.QtGui.QPageRanges.Range") |
| **S** | * [`QScreen`](QScreen.html#PySide6.QtGui.QScreen "PySide6.QtGui.QScreen") | * [`QScrollEvent`](QScrollEvent.html#PySide6.QtGui.QScrollEvent "PySide6.QtGui.QScrollEvent") | * [`QScrollPrepareEvent`](QScrollPrepareEvent.html#PySide6.QtGui.QScrollPrepareEvent "PySide6.QtGui.QScrollPrepareEvent") |
|  | * [`QSessionManager`](QSessionManager.html#PySide6.QtGui.QSessionManager "PySide6.QtGui.QSessionManager") | * [`QShader`](QShader.html#PySide6.QtGui.QShader "PySide6.QtGui.QShader") | * [`QShaderCode`](QShaderCode.html#PySide6.QtGui.QShaderCode "PySide6.QtGui.QShaderCode") |
|  | * [`QShaderKey`](QShaderKey.html#PySide6.QtGui.QShaderKey "PySide6.QtGui.QShaderKey") | * [`QShaderVersion`](QShaderVersion.html#PySide6.QtGui.QShaderVersion "PySide6.QtGui.QShaderVersion") | * [`QShortcut`](QShortcut.html#PySide6.QtGui.QShortcut "PySide6.QtGui.QShortcut") |
|  | * [`QShortcutEvent`](QShortcutEvent.html#PySide6.QtGui.QShortcutEvent "PySide6.QtGui.QShortcutEvent") | * [`QShowEvent`](QShowEvent.html#PySide6.QtGui.QShowEvent "PySide6.QtGui.QShowEvent") | * [`QSinglePointEvent`](QSinglePointEvent.html#PySide6.QtGui.QSinglePointEvent "PySide6.QtGui.QSinglePointEvent") |
|  | * [`QStandardItem`](QStandardItem.html#PySide6.QtGui.QStandardItem "PySide6.QtGui.QStandardItem") | * [`QStandardItemModel`](QStandardItemModel.html#PySide6.QtGui.QStandardItemModel "PySide6.QtGui.QStandardItemModel") | * [`QStaticText`](QStaticText.html#PySide6.QtGui.QStaticText "PySide6.QtGui.QStaticText") |
|  | * [`QStatusTipEvent`](QStatusTipEvent.html#PySide6.QtGui.QStatusTipEvent "PySide6.QtGui.QStatusTipEvent") | * [`QStyleHints`](QStyleHints.html#PySide6.QtGui.QStyleHints "PySide6.QtGui.QStyleHints") | * [`QSurface`](QSurface.html#PySide6.QtGui.QSurface "PySide6.QtGui.QSurface") |
|  | * [`QSurfaceFormat`](QSurfaceFormat.html#PySide6.QtGui.QSurfaceFormat "PySide6.QtGui.QSurfaceFormat") | * [`QSyntaxHighlighter`](QSyntaxHighlighter.html#PySide6.QtGui.QSyntaxHighlighter "PySide6.QtGui.QSyntaxHighlighter") | * [`ScaledPixmapArgument`](QIconEngine.html#PySide6.QtGui.QIconEngine.ScaledPixmapArgument "PySide6.QtGui.QIconEngine.ScaledPixmapArgument") |
|  | * [`Selection`](QAbstractTextDocumentLayout.html#PySide6.QtGui.QAbstractTextDocumentLayout.Selection "PySide6.QtGui.QAbstractTextDocumentLayout.Selection") | * [`State`](QAccessible.html#PySide6.QtGui.QAccessible.State "PySide6.QtGui.QAccessible.State") | * [`StencilOpState`](QRhiGraphicsPipeline.html#PySide6.QtGui.QRhiGraphicsPipeline.StencilOpState "PySide6.QtGui.QRhiGraphicsPipeline.StencilOpState") |
|  | * [`StorageBufferData`](QRhiShaderResourceBinding.html#PySide6.QtGui.QRhiShaderResourceBinding.Data.StorageBufferData "PySide6.QtGui.QRhiShaderResourceBinding.Data.StorageBufferData") | * [`StorageImageData`](QRhiShaderResourceBinding.html#PySide6.QtGui.QRhiShaderResourceBinding.Data.StorageImageData "PySide6.QtGui.QRhiShaderResourceBinding.Data.StorageImageData") | * [`Svg`](QColorConstants.html#PySide6.QtGui.QColorConstants.Svg "PySide6.QtGui.QColorConstants.Svg") |
| **T** | * [`QTabletEvent`](QTabletEvent.html#PySide6.QtGui.QTabletEvent "PySide6.QtGui.QTabletEvent") | * [`QTextBlock`](QTextBlock.html#PySide6.QtGui.QTextBlock "PySide6.QtGui.QTextBlock") | * [`QTextBlockFormat`](QTextBlockFormat.html#PySide6.QtGui.QTextBlockFormat "PySide6.QtGui.QTextBlockFormat") |
|  | * [`QTextBlockGroup`](QTextBlockGroup.html#PySide6.QtGui.QTextBlockGroup "PySide6.QtGui.QTextBlockGroup") | * [`QTextBlockUserData`](QTextBlockUserData.html#PySide6.QtGui.QTextBlockUserData "PySide6.QtGui.QTextBlockUserData") | * [`QTextCharFormat`](QTextCharFormat.html#PySide6.QtGui.QTextCharFormat "PySide6.QtGui.QTextCharFormat") |
|  | * [`QTextCursor`](QTextCursor.html#PySide6.QtGui.QTextCursor "PySide6.QtGui.QTextCursor") | * [`QTextDocument`](QTextDocument.html#PySide6.QtGui.QTextDocument "PySide6.QtGui.QTextDocument") | * [`QTextDocumentFragment`](QTextDocumentFragment.html#PySide6.QtGui.QTextDocumentFragment "PySide6.QtGui.QTextDocumentFragment") |
|  | * [`QTextDocumentWriter`](QTextDocumentWriter.html#PySide6.QtGui.QTextDocumentWriter "PySide6.QtGui.QTextDocumentWriter") | * [`QTextFormat`](QTextFormat.html#PySide6.QtGui.QTextFormat "PySide6.QtGui.QTextFormat") | * [`QTextFragment`](QTextFragment.html#PySide6.QtGui.QTextFragment "PySide6.QtGui.QTextFragment") |
|  | * [`QTextFrame`](QTextFrame.html#PySide6.QtGui.QTextFrame "PySide6.QtGui.QTextFrame") | * [`QTextFrameFormat`](QTextFrameFormat.html#PySide6.QtGui.QTextFrameFormat "PySide6.QtGui.QTextFrameFormat") | * [`QTextImageFormat`](QTextImageFormat.html#PySide6.QtGui.QTextImageFormat "PySide6.QtGui.QTextImageFormat") |
|  | * [`QTextInlineObject`](QTextInlineObject.html#PySide6.QtGui.QTextInlineObject "PySide6.QtGui.QTextInlineObject") | * [`QTextItem`](QTextItem.html#PySide6.QtGui.QTextItem "PySide6.QtGui.QTextItem") | * [`QTextLayout`](QTextLayout.html#PySide6.QtGui.QTextLayout "PySide6.QtGui.QTextLayout") |
|  | * [`QTextLength`](QTextLength.html#PySide6.QtGui.QTextLength "PySide6.QtGui.QTextLength") | * [`QTextLine`](QTextLine.html#PySide6.QtGui.QTextLine "PySide6.QtGui.QTextLine") | * [`QTextList`](QTextList.html#PySide6.QtGui.QTextList "PySide6.QtGui.QTextList") |
|  | * [`QTextListFormat`](QTextListFormat.html#PySide6.QtGui.QTextListFormat "PySide6.QtGui.QTextListFormat") | * [`QTextObject`](QTextObject.html#PySide6.QtGui.QTextObject "PySide6.QtGui.QTextObject") | * [`QTextObjectInterface`](QTextObjectInterface.html#PySide6.QtGui.QTextObjectInterface "PySide6.QtGui.QTextObjectInterface") |
|  | * [`QTextOption`](QTextOption.html#PySide6.QtGui.QTextOption "PySide6.QtGui.QTextOption") | * [`QTextTable`](QTextTable.html#PySide6.QtGui.QTextTable "PySide6.QtGui.QTextTable") | * [`QTextTableCell`](QTextTableCell.html#PySide6.QtGui.QTextTableCell "PySide6.QtGui.QTextTableCell") |
|  | * [`QTextTableCellFormat`](QTextTableCellFormat.html#PySide6.QtGui.QTextTableCellFormat "PySide6.QtGui.QTextTableCellFormat") | * [`QTextTableFormat`](QTextTableFormat.html#PySide6.QtGui.QTextTableFormat "PySide6.QtGui.QTextTableFormat") | * [`QToolBarChangeEvent`](QToolBarChangeEvent.html#PySide6.QtGui.QToolBarChangeEvent "PySide6.QtGui.QToolBarChangeEvent") |
|  | * [`QTouchEvent`](QTouchEvent.html#PySide6.QtGui.QTouchEvent "PySide6.QtGui.QTouchEvent") | * [`QTransform`](QTransform.html#PySide6.QtGui.QTransform "PySide6.QtGui.QTransform") | * [`Tab`](QTextOption.html#PySide6.QtGui.QTextOption.Tab "PySide6.QtGui.QTextOption.Tab") |
|  | * [`Tag`](QFont.html#PySide6.QtGui.QFont.Tag "PySide6.QtGui.QFont.Tag") | * [`TargetBlend`](QRhiGraphicsPipeline.html#PySide6.QtGui.QRhiGraphicsPipeline.TargetBlend "PySide6.QtGui.QRhiGraphicsPipeline.TargetBlend") | * [`TextureAndSampler`](QRhiShaderResourceBinding.html#PySide6.QtGui.QRhiShaderResourceBinding.TextureAndSampler "PySide6.QtGui.QRhiShaderResourceBinding.TextureAndSampler") |
| **U** | * [`QUndoCommand`](QUndoCommand.html#PySide6.QtGui.QUndoCommand "PySide6.QtGui.QUndoCommand") | * [`QUndoGroup`](QUndoGroup.html#PySide6.QtGui.QUndoGroup "PySide6.QtGui.QUndoGroup") | * [`QUndoStack`](QUndoStack.html#PySide6.QtGui.QUndoStack "PySide6.QtGui.QUndoStack") |
| **V** | * [`QValidator`](QValidator.html#PySide6.QtGui.QValidator "PySide6.QtGui.QValidator") | * [`QVector2D`](QVector2D.html#PySide6.QtGui.QVector2D "PySide6.QtGui.QVector2D") | * [`QVector3D`](QVector3D.html#PySide6.QtGui.QVector3D "PySide6.QtGui.QVector3D") |
|  | * [`QVector4D`](QVector4D.html#PySide6.QtGui.QVector4D "PySide6.QtGui.QVector4D") | * [`ViewFormat`](QRhiTexture.html#PySide6.QtGui.QRhiTexture.ViewFormat "PySide6.QtGui.QRhiTexture.ViewFormat") |  |
| **W** | * [`QWaylandApplication`](QNativeInterface.html#PySide6.QtGui.QNativeInterface.QWaylandApplication "PySide6.QtGui.QNativeInterface.QWaylandApplication") | * [`QWhatsThisClickedEvent`](QWhatsThisClickedEvent.html#PySide6.QtGui.QWhatsThisClickedEvent "PySide6.QtGui.QWhatsThisClickedEvent") | * [`QWheelEvent`](QWheelEvent.html#PySide6.QtGui.QWheelEvent "PySide6.QtGui.QWheelEvent") |
|  | * [`QWindow`](QWindow.html#PySide6.QtGui.QWindow "PySide6.QtGui.QWindow") | * [`QWindowStateChangeEvent`](QWindowStateChangeEvent.html#PySide6.QtGui.QWindowStateChangeEvent "PySide6.QtGui.QWindowStateChangeEvent") |  |
| **X** | * [`QX11Application`](QNativeInterface.html#PySide6.QtGui.QNativeInterface.QX11Application "PySide6.QtGui.QNativeInterface.QX11Application") | | |
## List of Functions[Â¶](#list-of-functions "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **A** | * [`qAlpha()`](QtGui_globals.html#PySide6.QtGui.qAlpha "PySide6.QtGui.qAlpha") | | |
| **B** | * [`qBlue()`](QtGui_globals.html#PySide6.QtGui.qBlue "PySide6.QtGui.qBlue") | | |
| **F** | * [`qFuzzyCompare()`](QtGui_globals.html#PySide6.QtGui.qFuzzyCompare "PySide6.QtGui.qFuzzyCompare") | | |
| **G** | * [`qGray()`](QtGui_globals.html#PySide6.QtGui.qGray "PySide6.QtGui.qGray") | * [`qGreen()`](QtGui_globals.html#PySide6.QtGui.qGreen "PySide6.QtGui.qGreen") |  |
| **I** | * [`qIsGray()`](QtGui_globals.html#PySide6.QtGui.qIsGray "PySide6.QtGui.qIsGray") | | |
| **P** | * [`qPixelFormatAlpha()`](QtGui_globals.html#PySide6.QtGui.qPixelFormatAlpha "PySide6.QtGui.qPixelFormatAlpha") | * [`qPixelFormatCmyk()`](QtGui_globals.html#PySide6.QtGui.qPixelFormatCmyk "PySide6.QtGui.qPixelFormatCmyk") | * [`qPixelFormatGrayscale()`](QtGui_globals.html#PySide6.QtGui.qPixelFormatGrayscale "PySide6.QtGui.qPixelFormatGrayscale") |
|  | * [`qPixelFormatHsl()`](QtGui_globals.html#PySide6.QtGui.qPixelFormatHsl "PySide6.QtGui.qPixelFormatHsl") | * [`qPixelFormatHsv()`](QtGui_globals.html#PySide6.QtGui.qPixelFormatHsv "PySide6.QtGui.qPixelFormatHsv") | * [`qPixelFormatRgba()`](QtGui_globals.html#PySide6.QtGui.qPixelFormatRgba "PySide6.QtGui.qPixelFormatRgba") |
|  | * [`qPixelFormatYuv()`](QtGui_globals.html#PySide6.QtGui.qPixelFormatYuv "PySide6.QtGui.qPixelFormatYuv") |  | |
| **R** | * [`qRed()`](QtGui_globals.html#PySide6.QtGui.qRed "PySide6.QtGui.qRed") | * [`qRgb()`](QtGui_globals.html#PySide6.QtGui.qRgb "PySide6.QtGui.qRgb") | * [`qRgba()`](QtGui_globals.html#PySide6.QtGui.qRgba "PySide6.QtGui.qRgba") |
---
<!-- Source: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html#module-PySide6.QtWidgets -->
# PySide6.QtWidgets[Â¶](#pyside6-qtwidgets "Link to this heading")
* [Functions](QtWidgets_globals.html)
* [PySide6.QtWidgets.QAbstractButton](QAbstractButton.html)
* [PySide6.QtWidgets.QAbstractGraphicsShapeItem](QAbstractGraphicsShapeItem.html)
* [PySide6.QtWidgets.QAbstractItemDelegate](QAbstractItemDelegate.html)
* [PySide6.QtWidgets.QAbstractItemView](QAbstractItemView.html)
* [PySide6.QtWidgets.QAbstractScrollArea](QAbstractScrollArea.html)
* [PySide6.QtWidgets.QAbstractSlider](QAbstractSlider.html)
* [PySide6.QtWidgets.QAbstractSpinBox](QAbstractSpinBox.html)
* [PySide6.QtWidgets.QAccessibleWidget](QAccessibleWidget.html)
* [PySide6.QtWidgets.QApplication](QApplication.html)
* [PySide6.QtWidgets.QBoxLayout](QBoxLayout.html)
* [PySide6.QtWidgets.QButtonGroup](QButtonGroup.html)
* [PySide6.QtWidgets.QCalendarWidget](QCalendarWidget.html)
* [PySide6.QtWidgets.QCheckBox](QCheckBox.html)
* [PySide6.QtWidgets.QColorDialog](QColorDialog.html)
* [PySide6.QtWidgets.QColormap](QColormap.html)
* [PySide6.QtWidgets.QColumnView](QColumnView.html)
* [PySide6.QtWidgets.QComboBox](QComboBox.html)
* [PySide6.QtWidgets.QCommandLinkButton](QCommandLinkButton.html)
* [PySide6.QtWidgets.QCommonStyle](QCommonStyle.html)
* [PySide6.QtWidgets.QCompleter](QCompleter.html)
* [PySide6.QtWidgets.QDataWidgetMapper](QDataWidgetMapper.html)
* [PySide6.QtWidgets.QDateEdit](QDateEdit.html)
* [PySide6.QtWidgets.QDateTimeEdit](QDateTimeEdit.html)
* [PySide6.QtWidgets.QDial](QDial.html)
* [PySide6.QtWidgets.QDialog](QDialog.html)
* [PySide6.QtWidgets.QDialogButtonBox](QDialogButtonBox.html)
* [PySide6.QtWidgets.QDockWidget](QDockWidget.html)
* [PySide6.QtWidgets.QDoubleSpinBox](QDoubleSpinBox.html)
* [PySide6.QtWidgets.QErrorMessage](QErrorMessage.html)
* [PySide6.QtWidgets.QFileDialog](QFileDialog.html)
* [PySide6.QtWidgets.QFileIconProvider](QFileIconProvider.html)
* [PySide6.QtWidgets.QFileSystemModel](QFileSystemModel.html)
* [PySide6.QtWidgets.QFocusFrame](QFocusFrame.html)
* [PySide6.QtWidgets.QFontComboBox](QFontComboBox.html)
* [PySide6.QtWidgets.QFontDialog](QFontDialog.html)
* [PySide6.QtWidgets.QFormLayout](QFormLayout.html)
* [PySide6.QtWidgets.QFrame](QFrame.html)
* [PySide6.QtWidgets.QGesture](QGesture.html)
* [PySide6.QtWidgets.QGestureEvent](QGestureEvent.html)
* [PySide6.QtWidgets.QGestureRecognizer](QGestureRecognizer.html)
* [PySide6.QtWidgets.QGraphicsAnchor](QGraphicsAnchor.html)
* [PySide6.QtWidgets.QGraphicsAnchorLayout](QGraphicsAnchorLayout.html)
* [PySide6.QtWidgets.QGraphicsBlurEffect](QGraphicsBlurEffect.html)
* [PySide6.QtWidgets.QGraphicsColorizeEffect](QGraphicsColorizeEffect.html)
* [PySide6.QtWidgets.QGraphicsDropShadowEffect](QGraphicsDropShadowEffect.html)
* [PySide6.QtWidgets.QGraphicsEffect](QGraphicsEffect.html)
* [PySide6.QtWidgets.QGraphicsEllipseItem](QGraphicsEllipseItem.html)
* [PySide6.QtWidgets.QGraphicsGridLayout](QGraphicsGridLayout.html)
* [PySide6.QtWidgets.QGraphicsItem](QGraphicsItem.html)
* [PySide6.QtWidgets.QGraphicsItemAnimation](QGraphicsItemAnimation.html)
* [PySide6.QtWidgets.QGraphicsItemGroup](QGraphicsItemGroup.html)
* [PySide6.QtWidgets.QGraphicsLayout](QGraphicsLayout.html)
* [PySide6.QtWidgets.QGraphicsLayoutItem](QGraphicsLayoutItem.html)
* [PySide6.QtWidgets.QGraphicsLineItem](QGraphicsLineItem.html)
* [PySide6.QtWidgets.QGraphicsLinearLayout](QGraphicsLinearLayout.html)
* [PySide6.QtWidgets.QGraphicsObject](QGraphicsObject.html)
* [PySide6.QtWidgets.QGraphicsOpacityEffect](QGraphicsOpacityEffect.html)
* [PySide6.QtWidgets.QGraphicsPathItem](QGraphicsPathItem.html)
* [PySide6.QtWidgets.QGraphicsPixmapItem](QGraphicsPixmapItem.html)
* [PySide6.QtWidgets.QGraphicsPolygonItem](QGraphicsPolygonItem.html)
* [PySide6.QtWidgets.QGraphicsProxyWidget](QGraphicsProxyWidget.html)
* [PySide6.QtWidgets.QGraphicsRectItem](QGraphicsRectItem.html)
* [PySide6.QtWidgets.QGraphicsRotation](QGraphicsRotation.html)
* [PySide6.QtWidgets.QGraphicsScale](QGraphicsScale.html)
* [PySide6.QtWidgets.QGraphicsScene](QGraphicsScene.html)
* [PySide6.QtWidgets.QGraphicsSceneContextMenuEvent](QGraphicsSceneContextMenuEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneDragDropEvent](QGraphicsSceneDragDropEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneEvent](QGraphicsSceneEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneHelpEvent](QGraphicsSceneHelpEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneHoverEvent](QGraphicsSceneHoverEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneMouseEvent](QGraphicsSceneMouseEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneMoveEvent](QGraphicsSceneMoveEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneResizeEvent](QGraphicsSceneResizeEvent.html)
* [PySide6.QtWidgets.QGraphicsSceneWheelEvent](QGraphicsSceneWheelEvent.html)
* [PySide6.QtWidgets.QGraphicsSimpleTextItem](QGraphicsSimpleTextItem.html)
* [PySide6.QtWidgets.QGraphicsTextItem](QGraphicsTextItem.html)
* [PySide6.QtWidgets.QGraphicsTransform](QGraphicsTransform.html)
* [PySide6.QtWidgets.QGraphicsView](QGraphicsView.html)
* [PySide6.QtWidgets.QGraphicsWidget](QGraphicsWidget.html)
* [PySide6.QtWidgets.QGridLayout](QGridLayout.html)
* [PySide6.QtWidgets.QGroupBox](QGroupBox.html)
* [PySide6.QtWidgets.QHBoxLayout](QHBoxLayout.html)
* [PySide6.QtWidgets.QHeaderView](QHeaderView.html)
* [PySide6.QtWidgets.QInputDialog](QInputDialog.html)
* [PySide6.QtWidgets.QItemDelegate](QItemDelegate.html)
* [PySide6.QtWidgets.QItemEditorCreatorBase](QItemEditorCreatorBase.html)
* [PySide6.QtWidgets.QItemEditorFactory](QItemEditorFactory.html)
* [PySide6.QtWidgets.QKeySequenceEdit](QKeySequenceEdit.html)
* [PySide6.QtWidgets.QLCDNumber](QLCDNumber.html)
* [PySide6.QtWidgets.QLabel](QLabel.html)
* [PySide6.QtWidgets.QLayout](QLayout.html)
* [PySide6.QtWidgets.QLayoutItem](QLayoutItem.html)
* [PySide6.QtWidgets.QLineEdit](QLineEdit.html)
* [PySide6.QtWidgets.QListView](QListView.html)
* [PySide6.QtWidgets.QListWidget](QListWidget.html)
* [PySide6.QtWidgets.QListWidgetItem](QListWidgetItem.html)
* [PySide6.QtWidgets.QMainWindow](QMainWindow.html)
* [PySide6.QtWidgets.QMdiArea](QMdiArea.html)
* [PySide6.QtWidgets.QMdiSubWindow](QMdiSubWindow.html)
* [PySide6.QtWidgets.QMenu](QMenu.html)
* [PySide6.QtWidgets.QMenuBar](QMenuBar.html)
* [PySide6.QtWidgets.QMessageBox](QMessageBox.html)
* [PySide6.QtWidgets.QPanGesture](QPanGesture.html)
* [PySide6.QtWidgets.QPinchGesture](QPinchGesture.html)
* [PySide6.QtWidgets.QPlainTextDocumentLayout](QPlainTextDocumentLayout.html)
* [PySide6.QtWidgets.QPlainTextEdit](QPlainTextEdit.html)
* [PySide6.QtWidgets.QProgressBar](QProgressBar.html)
* [PySide6.QtWidgets.QProgressDialog](QProgressDialog.html)
* [PySide6.QtWidgets.QProxyStyle](QProxyStyle.html)
* [PySide6.QtWidgets.QPushButton](QPushButton.html)
* [PySide6.QtWidgets.QRadioButton](QRadioButton.html)
* [PySide6.QtWidgets.QRhiWidget](QRhiWidget.html)
* [PySide6.QtWidgets.QRubberBand](QRubberBand.html)
* [PySide6.QtWidgets.QScrollArea](QScrollArea.html)
* [PySide6.QtWidgets.QScrollBar](QScrollBar.html)
* [PySide6.QtWidgets.QScroller](QScroller.html)
* [PySide6.QtWidgets.QScrollerProperties](QScrollerProperties.html)
* [PySide6.QtWidgets.QSizeGrip](QSizeGrip.html)
* [PySide6.QtWidgets.QSizePolicy](QSizePolicy.html)
* [PySide6.QtWidgets.QSlider](QSlider.html)
* [PySide6.QtWidgets.QSpacerItem](QSpacerItem.html)
* [PySide6.QtWidgets.QSpinBox](QSpinBox.html)
* [PySide6.QtWidgets.QSplashScreen](QSplashScreen.html)
* [PySide6.QtWidgets.QSplitter](QSplitter.html)
* [PySide6.QtWidgets.QSplitterHandle](QSplitterHandle.html)
* [PySide6.QtWidgets.QStackedLayout](QStackedLayout.html)
* [PySide6.QtWidgets.QStackedWidget](QStackedWidget.html)
* [PySide6.QtWidgets.QStatusBar](QStatusBar.html)
* [PySide6.QtWidgets.QStyle](QStyle.html)
* [PySide6.QtWidgets.QStyleFactory](QStyleFactory.html)
* [PySide6.QtWidgets.QStyleHintReturn](QStyleHintReturn.html)
* [PySide6.QtWidgets.QStyleHintReturnMask](QStyleHintReturnMask.html)
* [PySide6.QtWidgets.QStyleHintReturnVariant](QStyleHintReturnVariant.html)
* [PySide6.QtWidgets.QStyleOption](QStyleOption.html)
* [PySide6.QtWidgets.QStyleOptionButton](QStyleOptionButton.html)
* [PySide6.QtWidgets.QStyleOptionComboBox](QStyleOptionComboBox.html)
* [PySide6.QtWidgets.QStyleOptionComplex](QStyleOptionComplex.html)
* [PySide6.QtWidgets.QStyleOptionDockWidget](QStyleOptionDockWidget.html)
* [PySide6.QtWidgets.QStyleOptionFocusRect](QStyleOptionFocusRect.html)
* [PySide6.QtWidgets.QStyleOptionFrame](QStyleOptionFrame.html)
* [PySide6.QtWidgets.QStyleOptionGraphicsItem](QStyleOptionGraphicsItem.html)
* [PySide6.QtWidgets.QStyleOptionGroupBox](QStyleOptionGroupBox.html)
* [PySide6.QtWidgets.QStyleOptionHeader](QStyleOptionHeader.html)
* [PySide6.QtWidgets.QStyleOptionHeaderV2](QStyleOptionHeaderV2.html)
* [PySide6.QtWidgets.QStyleOptionMenuItem](QStyleOptionMenuItem.html)
* [PySide6.QtWidgets.QStyleOptionMenuItemV2](QStyleOptionMenuItemV2.html)
* [PySide6.QtWidgets.QStyleOptionProgressBar](QStyleOptionProgressBar.html)
* [PySide6.QtWidgets.QStyleOptionRubberBand](QStyleOptionRubberBand.html)
* [PySide6.QtWidgets.QStyleOptionSizeGrip](QStyleOptionSizeGrip.html)
* [PySide6.QtWidgets.QStyleOptionSlider](QStyleOptionSlider.html)
* [PySide6.QtWidgets.QStyleOptionSpinBox](QStyleOptionSpinBox.html)
* [PySide6.QtWidgets.QStyleOptionTab](QStyleOptionTab.html)
* [PySide6.QtWidgets.QStyleOptionTabBarBase](QStyleOptionTabBarBase.html)
* [PySide6.QtWidgets.QStyleOptionTabWidgetFrame](QStyleOptionTabWidgetFrame.html)
* [PySide6.QtWidgets.QStyleOptionTitleBar](QStyleOptionTitleBar.html)
* [PySide6.QtWidgets.QStyleOptionToolBar](QStyleOptionToolBar.html)
* [PySide6.QtWidgets.QStyleOptionToolBox](QStyleOptionToolBox.html)
* [PySide6.QtWidgets.QStyleOptionToolButton](QStyleOptionToolButton.html)
* [PySide6.QtWidgets.QStyleOptionViewItem](QStyleOptionViewItem.html)
* [PySide6.QtWidgets.QStylePainter](QStylePainter.html)
* [PySide6.QtWidgets.QStyledItemDelegate](QStyledItemDelegate.html)
* [PySide6.QtWidgets.QSwipeGesture](QSwipeGesture.html)
* [PySide6.QtWidgets.QSystemTrayIcon](QSystemTrayIcon.html)
* [PySide6.QtWidgets.QTabBar](QTabBar.html)
* [PySide6.QtWidgets.QTabWidget](QTabWidget.html)
* [PySide6.QtWidgets.QTableView](QTableView.html)
* [PySide6.QtWidgets.QTableWidget](QTableWidget.html)
* [PySide6.QtWidgets.QTableWidgetItem](QTableWidgetItem.html)
* [PySide6.QtWidgets.QTableWidgetSelectionRange](QTableWidgetSelectionRange.html)
* [PySide6.QtWidgets.QTapAndHoldGesture](QTapAndHoldGesture.html)
* [PySide6.QtWidgets.QTapGesture](QTapGesture.html)
* [PySide6.QtWidgets.QTextBrowser](QTextBrowser.html)
* [PySide6.QtWidgets.QTextEdit](QTextEdit.html)
* [PySide6.QtWidgets.QTileRules](QTileRules.html)
* [PySide6.QtWidgets.QTimeEdit](QTimeEdit.html)
* [PySide6.QtWidgets.QToolBar](QToolBar.html)
* [PySide6.QtWidgets.QToolBox](QToolBox.html)
* [PySide6.QtWidgets.QToolButton](QToolButton.html)
* [PySide6.QtWidgets.QToolTip](QToolTip.html)
* [PySide6.QtWidgets.QTreeView](QTreeView.html)
* [PySide6.QtWidgets.QTreeWidget](QTreeWidget.html)
* [PySide6.QtWidgets.QTreeWidgetItem](QTreeWidgetItem.html)
* [PySide6.QtWidgets.QTreeWidgetItemIterator](QTreeWidgetItemIterator.html)
* [PySide6.QtWidgets.QUndoView](QUndoView.html)
* [PySide6.QtWidgets.QVBoxLayout](QVBoxLayout.html)
* [PySide6.QtWidgets.QWhatsThis](QWhatsThis.html)
* [PySide6.QtWidgets.QWidget](QWidget.html)
* [PySide6.QtWidgets.QWidgetAction](QWidgetAction.html)
* [PySide6.QtWidgets.QWidgetItem](QWidgetItem.html)
* [PySide6.QtWidgets.QWizard](QWizard.html)
* [PySide6.QtWidgets.QWizardPage](QWizardPage.html)
## Detailed Description[Â¶](#detailed-description "Link to this heading")
A module which provides a set of C++ technologies for building user
interfaces
The QtWidgets module provides a set of UI elements to create classic
desktop-style user interfaces.
### Widgets[Â¶](#widgets "Link to this heading")
Widgets are the primary elements for creating user interfaces in Qt. They can
display data and status information, receive user input, and provide a
container for other widgets that should be grouped together. A widget that is
not embedded in a parent widget is called a window.
> ![../../_images/parent-child-widgets.png](../../_images/parent-child-widgets.png)
The [`QWidget`](QWidget.html#PySide6.QtWidgets.QWidget "PySide6.QtWidgets.QWidget") class provides the
basic capability to render to the screen, and to handle user input
events. All UI elements that Qt provides are either subclasses of
[`QWidget`](QWidget.html#PySide6.QtWidgets.QWidget "PySide6.QtWidgets.QWidget") , or are used in
connection with a [`QWidget`](QWidget.html#PySide6.QtWidgets.QWidget "PySide6.QtWidgets.QWidget")
subclass. Creating custom widgets is done by subclassing
[`QWidget`](QWidget.html#PySide6.QtWidgets.QWidget "PySide6.QtWidgets.QWidget") or a suitable subclass and
reimplementing the virtual event handlers.
> * [Window and Dialog Widgets](../../overviews/qtwidgets-application-windows.html#window-and-dialog-widgets)
> * [Application Main Window](../../overviews/qtwidgets-mainwindow.html#application-main-window)
> * [Dialog Windows](../../overviews/qtwidgets-dialogs.html#dialog-windows)
> * [Keyboard Focus in Widgets](../../overviews/qtwidgets-focus.html#keyboard-focus-in-widgets)
### Styles[Â¶](#styles "Link to this heading")
[Styles](../../overviews/qtwidgets-style-reference.html#styles-and-style-aware-widgets) draw on behalf of
widgets and encapsulate the look and feel of a GUI. Qtâs built-in
widgets use the [`QStyle`](QStyle.html#PySide6.QtWidgets.QStyle "PySide6.QtWidgets.QStyle") class to
perform nearly all of their drawing, ensuring that they look exactly
like the equivalent native widgets.
[Qt Style Sheets](../../overviews/qtwidgets-stylesheet.html#qt-style-sheets) are a powerful mechanism that
allows you to customize the appearance of widgets, in addition to what
is already possible by subclassing
[`QStyle`](QStyle.html#PySide6.QtWidgets.QStyle "PySide6.QtWidgets.QStyle") .
### Layouts[Â¶](#layouts "Link to this heading")
[Layouts](../../overviews/qtwidgets-layout.html#layout-management) are an elegant and flexible way to
automatically arrange child widgets within their container. Each
widget reports its size requirements to the layout through the
[`sizeHint`](QWidget.html#id31 "PySide6.QtWidgets.QWidget.sizeHint") and
[`sizePolicy`](QWidget.html#id33 "PySide6.QtWidgets.QWidget.sizePolicy") properties,
and the layout distributes the available space accordingly.
[Qt Widgets Designer](../../tutorials/basictutorial/uifiles.html#tutorial-uifiles) is a powerful tool for interactively
creating and arranging widgets in layouts.
### Model/View Classes[Â¶](#model-view-classes "Link to this heading")
The [model/view](../../overviews/qtwidgets-model-view-programming.html#model-view-programming) architecture provides
classes that manage the way data is presented to the user. Data-driven
applications which use lists and tables are structured to separate the
data and view using models, views, and delegates.
> ![../../_images/fusion-treeview.png](../../_images/fusion-treeview.png)
### Graphics View[Â¶](#graphics-view "Link to this heading")
The [Graphics View Framework](../../overviews/qtwidgets-graphicsview.html#graphics-view-framework) is for
managing and interacting with a large number of custom-made 2D
graphical items, and a view widget for visualizing the items, with
support for zooming and rotation.
> ![../../_images/graphicsview-items.png](../../_images/graphicsview-items.png)
### Using the Module[Â¶](#using-the-module "Link to this heading")
To include the definitions of modules classes, use the following
directive:
```
import PySide6.QtWidgets
```
## List of Classes by Function[Â¶](#list-of-classes-by-function "Link to this heading")
> * [Widgets Classes](../../overviews/qtwidgets-widget-classes.html#widgets-classes)
## List of Classes[Â¶](#list-of-classes "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **A** | * [`QAbstractButton`](QAbstractButton.html#PySide6.QtWidgets.QAbstractButton "PySide6.QtWidgets.QAbstractButton") | * [`QAbstractGraphicsShapeItem`](QAbstractGraphicsShapeItem.html#PySide6.QtWidgets.QAbstractGraphicsShapeItem "PySide6.QtWidgets.QAbstractGraphicsShapeItem") | * [`QAbstractItemDelegate`](QAbstractItemDelegate.html#PySide6.QtWidgets.QAbstractItemDelegate "PySide6.QtWidgets.QAbstractItemDelegate") |
|  | * [`QAbstractItemView`](QAbstractItemView.html#PySide6.QtWidgets.QAbstractItemView "PySide6.QtWidgets.QAbstractItemView") | * [`QAbstractScrollArea`](QAbstractScrollArea.html#PySide6.QtWidgets.QAbstractScrollArea "PySide6.QtWidgets.QAbstractScrollArea") | * [`QAbstractSlider`](QAbstractSlider.html#PySide6.QtWidgets.QAbstractSlider "PySide6.QtWidgets.QAbstractSlider") |
|  | * [`QAbstractSpinBox`](QAbstractSpinBox.html#PySide6.QtWidgets.QAbstractSpinBox "PySide6.QtWidgets.QAbstractSpinBox") | * [`QAccessibleWidget`](QAccessibleWidget.html#PySide6.QtWidgets.QAccessibleWidget "PySide6.QtWidgets.QAccessibleWidget") | * [`QApplication`](QApplication.html#PySide6.QtWidgets.QApplication "PySide6.QtWidgets.QApplication") |
| **B** | * [`QBoxLayout`](QBoxLayout.html#PySide6.QtWidgets.QBoxLayout "PySide6.QtWidgets.QBoxLayout") | * [`QButtonGroup`](QButtonGroup.html#PySide6.QtWidgets.QButtonGroup "PySide6.QtWidgets.QButtonGroup") |  |
| **C** | * [`QCalendarWidget`](QCalendarWidget.html#PySide6.QtWidgets.QCalendarWidget "PySide6.QtWidgets.QCalendarWidget") | * [`QCheckBox`](QCheckBox.html#PySide6.QtWidgets.QCheckBox "PySide6.QtWidgets.QCheckBox") | * [`QColorDialog`](QColorDialog.html#PySide6.QtWidgets.QColorDialog "PySide6.QtWidgets.QColorDialog") |
|  | * [`QColormap`](QColormap.html#PySide6.QtWidgets.QColormap "PySide6.QtWidgets.QColormap") | * [`QColumnView`](QColumnView.html#PySide6.QtWidgets.QColumnView "PySide6.QtWidgets.QColumnView") | * [`QComboBox`](QComboBox.html#PySide6.QtWidgets.QComboBox "PySide6.QtWidgets.QComboBox") |
|  | * [`QCommandLinkButton`](QCommandLinkButton.html#PySide6.QtWidgets.QCommandLinkButton "PySide6.QtWidgets.QCommandLinkButton") | * [`QCommonStyle`](QCommonStyle.html#PySide6.QtWidgets.QCommonStyle "PySide6.QtWidgets.QCommonStyle") | * [`QCompleter`](QCompleter.html#PySide6.QtWidgets.QCompleter "PySide6.QtWidgets.QCompleter") |
| **D** | * [`QDataWidgetMapper`](QDataWidgetMapper.html#PySide6.QtWidgets.QDataWidgetMapper "PySide6.QtWidgets.QDataWidgetMapper") | * [`QDateEdit`](QDateEdit.html#PySide6.QtWidgets.QDateEdit "PySide6.QtWidgets.QDateEdit") | * [`QDateTimeEdit`](QDateTimeEdit.html#PySide6.QtWidgets.QDateTimeEdit "PySide6.QtWidgets.QDateTimeEdit") |
|  | * [`QDial`](QDial.html#PySide6.QtWidgets.QDial "PySide6.QtWidgets.QDial") | * [`QDialog`](QDialog.html#PySide6.QtWidgets.QDialog "PySide6.QtWidgets.QDialog") | * [`QDialogButtonBox`](QDialogButtonBox.html#PySide6.QtWidgets.QDialogButtonBox "PySide6.QtWidgets.QDialogButtonBox") |
|  | * [`QDockWidget`](QDockWidget.html#PySide6.QtWidgets.QDockWidget "PySide6.QtWidgets.QDockWidget") | * [`QDoubleSpinBox`](QDoubleSpinBox.html#PySide6.QtWidgets.QDoubleSpinBox "PySide6.QtWidgets.QDoubleSpinBox") |  |
| **E** | * [`ExtraSelection`](QTextEdit.html#PySide6.QtWidgets.QTextEdit.ExtraSelection "PySide6.QtWidgets.QTextEdit.ExtraSelection") | * [`QErrorMessage`](QErrorMessage.html#PySide6.QtWidgets.QErrorMessage "PySide6.QtWidgets.QErrorMessage") |  |
| **F** | * [`QFileDialog`](QFileDialog.html#PySide6.QtWidgets.QFileDialog "PySide6.QtWidgets.QFileDialog") | * [`QFileIconProvider`](QFileIconProvider.html#PySide6.QtWidgets.QFileIconProvider "PySide6.QtWidgets.QFileIconProvider") | * [`QFileSystemModel`](QFileSystemModel.html#PySide6.QtWidgets.QFileSystemModel "PySide6.QtWidgets.QFileSystemModel") |
|  | * [`QFocusFrame`](QFocusFrame.html#PySide6.QtWidgets.QFocusFrame "PySide6.QtWidgets.QFocusFrame") | * [`QFontComboBox`](QFontComboBox.html#PySide6.QtWidgets.QFontComboBox "PySide6.QtWidgets.QFontComboBox") | * [`QFontDialog`](QFontDialog.html#PySide6.QtWidgets.QFontDialog "PySide6.QtWidgets.QFontDialog") |
|  | * [`QFormLayout`](QFormLayout.html#PySide6.QtWidgets.QFormLayout "PySide6.QtWidgets.QFormLayout") | * [`QFrame`](QFrame.html#PySide6.QtWidgets.QFrame "PySide6.QtWidgets.QFrame") |  |
| **G** | * [`QGesture`](QGesture.html#PySide6.QtWidgets.QGesture "PySide6.QtWidgets.QGesture") | * [`QGestureEvent`](QGestureEvent.html#PySide6.QtWidgets.QGestureEvent "PySide6.QtWidgets.QGestureEvent") | * [`QGestureRecognizer`](QGestureRecognizer.html#PySide6.QtWidgets.QGestureRecognizer "PySide6.QtWidgets.QGestureRecognizer") |
|  | * [`QGraphicsAnchor`](QGraphicsAnchor.html#PySide6.QtWidgets.QGraphicsAnchor "PySide6.QtWidgets.QGraphicsAnchor") | * [`QGraphicsAnchorLayout`](QGraphicsAnchorLayout.html#PySide6.QtWidgets.QGraphicsAnchorLayout "PySide6.QtWidgets.QGraphicsAnchorLayout") | * [`QGraphicsBlurEffect`](QGraphicsBlurEffect.html#PySide6.QtWidgets.QGraphicsBlurEffect "PySide6.QtWidgets.QGraphicsBlurEffect") |
|  | * [`QGraphicsColorizeEffect`](QGraphicsColorizeEffect.html#PySide6.QtWidgets.QGraphicsColorizeEffect "PySide6.QtWidgets.QGraphicsColorizeEffect") | * [`QGraphicsDropShadowEffect`](QGraphicsDropShadowEffect.html#PySide6.QtWidgets.QGraphicsDropShadowEffect "PySide6.QtWidgets.QGraphicsDropShadowEffect") | * [`QGraphicsEffect`](QGraphicsEffect.html#PySide6.QtWidgets.QGraphicsEffect "PySide6.QtWidgets.QGraphicsEffect") |
|  | * [`QGraphicsEllipseItem`](QGraphicsEllipseItem.html#PySide6.QtWidgets.QGraphicsEllipseItem "PySide6.QtWidgets.QGraphicsEllipseItem") | * [`QGraphicsGridLayout`](QGraphicsGridLayout.html#PySide6.QtWidgets.QGraphicsGridLayout "PySide6.QtWidgets.QGraphicsGridLayout") | * [`QGraphicsItem`](QGraphicsItem.html#PySide6.QtWidgets.QGraphicsItem "PySide6.QtWidgets.QGraphicsItem") |
|  | * [`QGraphicsItemAnimation`](QGraphicsItemAnimation.html#PySide6.QtWidgets.QGraphicsItemAnimation "PySide6.QtWidgets.QGraphicsItemAnimation") | * [`QGraphicsItemGroup`](QGraphicsItemGroup.html#PySide6.QtWidgets.QGraphicsItemGroup "PySide6.QtWidgets.QGraphicsItemGroup") | * [`QGraphicsLayout`](QGraphicsLayout.html#PySide6.QtWidgets.QGraphicsLayout "PySide6.QtWidgets.QGraphicsLayout") |
|  | * [`QGraphicsLayoutItem`](QGraphicsLayoutItem.html#PySide6.QtWidgets.QGraphicsLayoutItem "PySide6.QtWidgets.QGraphicsLayoutItem") | * [`QGraphicsLineItem`](QGraphicsLineItem.html#PySide6.QtWidgets.QGraphicsLineItem "PySide6.QtWidgets.QGraphicsLineItem") | * [`QGraphicsLinearLayout`](QGraphicsLinearLayout.html#PySide6.QtWidgets.QGraphicsLinearLayout "PySide6.QtWidgets.QGraphicsLinearLayout") |
|  | * [`QGraphicsObject`](QGraphicsObject.html#PySide6.QtWidgets.QGraphicsObject "PySide6.QtWidgets.QGraphicsObject") | * [`QGraphicsOpacityEffect`](QGraphicsOpacityEffect.html#PySide6.QtWidgets.QGraphicsOpacityEffect "PySide6.QtWidgets.QGraphicsOpacityEffect") | * [`QGraphicsPathItem`](QGraphicsPathItem.html#PySide6.QtWidgets.QGraphicsPathItem "PySide6.QtWidgets.QGraphicsPathItem") |
|  | * [`QGraphicsPixmapItem`](QGraphicsPixmapItem.html#PySide6.QtWidgets.QGraphicsPixmapItem "PySide6.QtWidgets.QGraphicsPixmapItem") | * [`QGraphicsPolygonItem`](QGraphicsPolygonItem.html#PySide6.QtWidgets.QGraphicsPolygonItem "PySide6.QtWidgets.QGraphicsPolygonItem") | * [`QGraphicsProxyWidget`](QGraphicsProxyWidget.html#PySide6.QtWidgets.QGraphicsProxyWidget "PySide6.QtWidgets.QGraphicsProxyWidget") |
|  | * [`QGraphicsRectItem`](QGraphicsRectItem.html#PySide6.QtWidgets.QGraphicsRectItem "PySide6.QtWidgets.QGraphicsRectItem") | * [`QGraphicsRotation`](QGraphicsRotation.html#PySide6.QtWidgets.QGraphicsRotation "PySide6.QtWidgets.QGraphicsRotation") | * [`QGraphicsScale`](QGraphicsScale.html#PySide6.QtWidgets.QGraphicsScale "PySide6.QtWidgets.QGraphicsScale") |
|  | * [`QGraphicsScene`](QGraphicsScene.html#PySide6.QtWidgets.QGraphicsScene "PySide6.QtWidgets.QGraphicsScene") | * [`QGraphicsSceneContextMenuEvent`](QGraphicsSceneContextMenuEvent.html#PySide6.QtWidgets.QGraphicsSceneContextMenuEvent "PySide6.QtWidgets.QGraphicsSceneContextMenuEvent") | * [`QGraphicsSceneDragDropEvent`](QGraphicsSceneDragDropEvent.html#PySide6.QtWidgets.QGraphicsSceneDragDropEvent "PySide6.QtWidgets.QGraphicsSceneDragDropEvent") |
|  | * [`QGraphicsSceneEvent`](QGraphicsSceneEvent.html#PySide6.QtWidgets.QGraphicsSceneEvent "PySide6.QtWidgets.QGraphicsSceneEvent") | * [`QGraphicsSceneHelpEvent`](QGraphicsSceneHelpEvent.html#PySide6.QtWidgets.QGraphicsSceneHelpEvent "PySide6.QtWidgets.QGraphicsSceneHelpEvent") | * [`QGraphicsSceneHoverEvent`](QGraphicsSceneHoverEvent.html#PySide6.QtWidgets.QGraphicsSceneHoverEvent "PySide6.QtWidgets.QGraphicsSceneHoverEvent") |
|  | * [`QGraphicsSceneMouseEvent`](QGraphicsSceneMouseEvent.html#PySide6.QtWidgets.QGraphicsSceneMouseEvent "PySide6.QtWidgets.QGraphicsSceneMouseEvent") | * [`QGraphicsSceneMoveEvent`](QGraphicsSceneMoveEvent.html#PySide6.QtWidgets.QGraphicsSceneMoveEvent "PySide6.QtWidgets.QGraphicsSceneMoveEvent") | * [`QGraphicsSceneResizeEvent`](QGraphicsSceneResizeEvent.html#PySide6.QtWidgets.QGraphicsSceneResizeEvent "PySide6.QtWidgets.QGraphicsSceneResizeEvent") |
|  | * [`QGraphicsSceneWheelEvent`](QGraphicsSceneWheelEvent.html#PySide6.QtWidgets.QGraphicsSceneWheelEvent "PySide6.QtWidgets.QGraphicsSceneWheelEvent") | * [`QGraphicsSimpleTextItem`](QGraphicsSimpleTextItem.html#PySide6.QtWidgets.QGraphicsSimpleTextItem "PySide6.QtWidgets.QGraphicsSimpleTextItem") | * [`QGraphicsTextItem`](QGraphicsTextItem.html#PySide6.QtWidgets.QGraphicsTextItem "PySide6.QtWidgets.QGraphicsTextItem") |
|  | * [`QGraphicsTransform`](QGraphicsTransform.html#PySide6.QtWidgets.QGraphicsTransform "PySide6.QtWidgets.QGraphicsTransform") | * [`QGraphicsView`](QGraphicsView.html#PySide6.QtWidgets.QGraphicsView "PySide6.QtWidgets.QGraphicsView") | * [`QGraphicsWidget`](QGraphicsWidget.html#PySide6.QtWidgets.QGraphicsWidget "PySide6.QtWidgets.QGraphicsWidget") |
|  | * [`QGridLayout`](QGridLayout.html#PySide6.QtWidgets.QGridLayout "PySide6.QtWidgets.QGridLayout") | * [`QGroupBox`](QGroupBox.html#PySide6.QtWidgets.QGroupBox "PySide6.QtWidgets.QGroupBox") |  |
| **H** | * [`QHBoxLayout`](QHBoxLayout.html#PySide6.QtWidgets.QHBoxLayout "PySide6.QtWidgets.QHBoxLayout") | * [`QHeaderView`](QHeaderView.html#PySide6.QtWidgets.QHeaderView "PySide6.QtWidgets.QHeaderView") |  |
| **I** | * [`QInputDialog`](QInputDialog.html#PySide6.QtWidgets.QInputDialog "PySide6.QtWidgets.QInputDialog") | * [`QItemDelegate`](QItemDelegate.html#PySide6.QtWidgets.QItemDelegate "PySide6.QtWidgets.QItemDelegate") | * [`QItemEditorCreatorBase`](QItemEditorCreatorBase.html#PySide6.QtWidgets.QItemEditorCreatorBase "PySide6.QtWidgets.QItemEditorCreatorBase") |
|  | * [`QItemEditorFactory`](QItemEditorFactory.html#PySide6.QtWidgets.QItemEditorFactory "PySide6.QtWidgets.QItemEditorFactory") |  | |
| **K** | * [`QKeySequenceEdit`](QKeySequenceEdit.html#PySide6.QtWidgets.QKeySequenceEdit "PySide6.QtWidgets.QKeySequenceEdit") | | |
| **L** | * [`QLCDNumber`](QLCDNumber.html#PySide6.QtWidgets.QLCDNumber "PySide6.QtWidgets.QLCDNumber") | * [`QLabel`](QLabel.html#PySide6.QtWidgets.QLabel "PySide6.QtWidgets.QLabel") | * [`QLayout`](QLayout.html#PySide6.QtWidgets.QLayout "PySide6.QtWidgets.QLayout") |
|  | * [`QLayoutItem`](QLayoutItem.html#PySide6.QtWidgets.QLayoutItem "PySide6.QtWidgets.QLayoutItem") | * [`QLineEdit`](QLineEdit.html#PySide6.QtWidgets.QLineEdit "PySide6.QtWidgets.QLineEdit") | * [`QListView`](QListView.html#PySide6.QtWidgets.QListView "PySide6.QtWidgets.QListView") |
|  | * [`QListWidget`](QListWidget.html#PySide6.QtWidgets.QListWidget "PySide6.QtWidgets.QListWidget") | * [`QListWidgetItem`](QListWidgetItem.html#PySide6.QtWidgets.QListWidgetItem "PySide6.QtWidgets.QListWidgetItem") |  |
| **M** | * [`QMainWindow`](QMainWindow.html#PySide6.QtWidgets.QMainWindow "PySide6.QtWidgets.QMainWindow") | * [`QMdiArea`](QMdiArea.html#PySide6.QtWidgets.QMdiArea "PySide6.QtWidgets.QMdiArea") | * [`QMdiSubWindow`](QMdiSubWindow.html#PySide6.QtWidgets.QMdiSubWindow "PySide6.QtWidgets.QMdiSubWindow") |
|  | * [`QMenu`](QMenu.html#PySide6.QtWidgets.QMenu "PySide6.QtWidgets.QMenu") | * [`QMenuBar`](QMenuBar.html#PySide6.QtWidgets.QMenuBar "PySide6.QtWidgets.QMenuBar") | * [`QMessageBox`](QMessageBox.html#PySide6.QtWidgets.QMessageBox "PySide6.QtWidgets.QMessageBox") |
| **P** | * [`QPanGesture`](QPanGesture.html#PySide6.QtWidgets.QPanGesture "PySide6.QtWidgets.QPanGesture") | * [`QPinchGesture`](QPinchGesture.html#PySide6.QtWidgets.QPinchGesture "PySide6.QtWidgets.QPinchGesture") | * [`QPlainTextDocumentLayout`](QPlainTextDocumentLayout.html#PySide6.QtWidgets.QPlainTextDocumentLayout "PySide6.QtWidgets.QPlainTextDocumentLayout") |
|  | * [`QPlainTextEdit`](QPlainTextEdit.html#PySide6.QtWidgets.QPlainTextEdit "PySide6.QtWidgets.QPlainTextEdit") | * [`QProgressBar`](QProgressBar.html#PySide6.QtWidgets.QProgressBar "PySide6.QtWidgets.QProgressBar") | * [`QProgressDialog`](QProgressDialog.html#PySide6.QtWidgets.QProgressDialog "PySide6.QtWidgets.QProgressDialog") |
|  | * [`QProxyStyle`](QProxyStyle.html#PySide6.QtWidgets.QProxyStyle "PySide6.QtWidgets.QProxyStyle") | * [`QPushButton`](QPushButton.html#PySide6.QtWidgets.QPushButton "PySide6.QtWidgets.QPushButton") |  |
| **R** | * [`QRadioButton`](QRadioButton.html#PySide6.QtWidgets.QRadioButton "PySide6.QtWidgets.QRadioButton") | * [`QRhiWidget`](QRhiWidget.html#PySide6.QtWidgets.QRhiWidget "PySide6.QtWidgets.QRhiWidget") | * [`QRubberBand`](QRubberBand.html#PySide6.QtWidgets.QRubberBand "PySide6.QtWidgets.QRubberBand") |
| **S** | * [`QScrollArea`](QScrollArea.html#PySide6.QtWidgets.QScrollArea "PySide6.QtWidgets.QScrollArea") | * [`QScrollBar`](QScrollBar.html#PySide6.QtWidgets.QScrollBar "PySide6.QtWidgets.QScrollBar") | * [`QScroller`](QScroller.html#PySide6.QtWidgets.QScroller "PySide6.QtWidgets.QScroller") |
|  | * [`QScrollerProperties`](QScrollerProperties.html#PySide6.QtWidgets.QScrollerProperties "PySide6.QtWidgets.QScrollerProperties") | * [`QSizeGrip`](QSizeGrip.html#PySide6.QtWidgets.QSizeGrip "PySide6.QtWidgets.QSizeGrip") | * [`QSizePolicy`](QSizePolicy.html#PySide6.QtWidgets.QSizePolicy "PySide6.QtWidgets.QSizePolicy") |
|  | * [`QSlider`](QSlider.html#PySide6.QtWidgets.QSlider "PySide6.QtWidgets.QSlider") | * [`QSpacerItem`](QSpacerItem.html#PySide6.QtWidgets.QSpacerItem "PySide6.QtWidgets.QSpacerItem") | * [`QSpinBox`](QSpinBox.html#PySide6.QtWidgets.QSpinBox "PySide6.QtWidgets.QSpinBox") |
|  | * [`QSplashScreen`](QSplashScreen.html#PySide6.QtWidgets.QSplashScreen "PySide6.QtWidgets.QSplashScreen") | * [`QSplitter`](QSplitter.html#PySide6.QtWidgets.QSplitter "PySide6.QtWidgets.QSplitter") | * [`QSplitterHandle`](QSplitterHandle.html#PySide6.QtWidgets.QSplitterHandle "PySide6.QtWidgets.QSplitterHandle") |
|  | * [`QStackedLayout`](QStackedLayout.html#PySide6.QtWidgets.QStackedLayout "PySide6.QtWidgets.QStackedLayout") | * [`QStackedWidget`](QStackedWidget.html#PySide6.QtWidgets.QStackedWidget "PySide6.QtWidgets.QStackedWidget") | * [`QStatusBar`](QStatusBar.html#PySide6.QtWidgets.QStatusBar "PySide6.QtWidgets.QStatusBar") |
|  | * [`QStyle`](QStyle.html#PySide6.QtWidgets.QStyle "PySide6.QtWidgets.QStyle") | * [`QStyleFactory`](QStyleFactory.html#PySide6.QtWidgets.QStyleFactory "PySide6.QtWidgets.QStyleFactory") | * [`QStyleHintReturn`](QStyleHintReturn.html#PySide6.QtWidgets.QStyleHintReturn "PySide6.QtWidgets.QStyleHintReturn") |
|  | * [`QStyleHintReturnMask`](QStyleHintReturnMask.html#PySide6.QtWidgets.QStyleHintReturnMask "PySide6.QtWidgets.QStyleHintReturnMask") | * [`QStyleHintReturnVariant`](QStyleHintReturnVariant.html#PySide6.QtWidgets.QStyleHintReturnVariant "PySide6.QtWidgets.QStyleHintReturnVariant") | * [`QStyleOption`](QStyleOption.html#PySide6.QtWidgets.QStyleOption "PySide6.QtWidgets.QStyleOption") |
|  | * [`QStyleOptionButton`](QStyleOptionButton.html#PySide6.QtWidgets.QStyleOptionButton "PySide6.QtWidgets.QStyleOptionButton") | * [`QStyleOptionComboBox`](QStyleOptionComboBox.html#PySide6.QtWidgets.QStyleOptionComboBox "PySide6.QtWidgets.QStyleOptionComboBox") | * [`QStyleOptionComplex`](QStyleOptionComplex.html#PySide6.QtWidgets.QStyleOptionComplex "PySide6.QtWidgets.QStyleOptionComplex") |
|  | * [`QStyleOptionDockWidget`](QStyleOptionDockWidget.html#PySide6.QtWidgets.QStyleOptionDockWidget "PySide6.QtWidgets.QStyleOptionDockWidget") | * [`QStyleOptionFocusRect`](QStyleOptionFocusRect.html#PySide6.QtWidgets.QStyleOptionFocusRect "PySide6.QtWidgets.QStyleOptionFocusRect") | * [`QStyleOptionFrame`](QStyleOptionFrame.html#PySide6.QtWidgets.QStyleOptionFrame "PySide6.QtWidgets.QStyleOptionFrame") |
|  | * [`QStyleOptionGraphicsItem`](QStyleOptionGraphicsItem.html#PySide6.QtWidgets.QStyleOptionGraphicsItem "PySide6.QtWidgets.QStyleOptionGraphicsItem") | * [`QStyleOptionGroupBox`](QStyleOptionGroupBox.html#PySide6.QtWidgets.QStyleOptionGroupBox "PySide6.QtWidgets.QStyleOptionGroupBox") | * [`QStyleOptionHeader`](QStyleOptionHeader.html#PySide6.QtWidgets.QStyleOptionHeader "PySide6.QtWidgets.QStyleOptionHeader") |
|  | * [`QStyleOptionHeaderV2`](QStyleOptionHeaderV2.html#PySide6.QtWidgets.QStyleOptionHeaderV2 "PySide6.QtWidgets.QStyleOptionHeaderV2") | * [`QStyleOptionMenuItem`](QStyleOptionMenuItem.html#PySide6.QtWidgets.QStyleOptionMenuItem "PySide6.QtWidgets.QStyleOptionMenuItem") | * [`QStyleOptionMenuItemV2`](QStyleOptionMenuItemV2.html#PySide6.QtWidgets.QStyleOptionMenuItemV2 "PySide6.QtWidgets.QStyleOptionMenuItemV2") |
|  | * [`QStyleOptionProgressBar`](QStyleOptionProgressBar.html#PySide6.QtWidgets.QStyleOptionProgressBar "PySide6.QtWidgets.QStyleOptionProgressBar") | * [`QStyleOptionRubberBand`](QStyleOptionRubberBand.html#PySide6.QtWidgets.QStyleOptionRubberBand "PySide6.QtWidgets.QStyleOptionRubberBand") | * [`QStyleOptionSizeGrip`](QStyleOptionSizeGrip.html#PySide6.QtWidgets.QStyleOptionSizeGrip "PySide6.QtWidgets.QStyleOptionSizeGrip") |
|  | * [`QStyleOptionSlider`](QStyleOptionSlider.html#PySide6.QtWidgets.QStyleOptionSlider "PySide6.QtWidgets.QStyleOptionSlider") | * [`QStyleOptionSpinBox`](QStyleOptionSpinBox.html#PySide6.QtWidgets.QStyleOptionSpinBox "PySide6.QtWidgets.QStyleOptionSpinBox") | * [`QStyleOptionTab`](QStyleOptionTab.html#PySide6.QtWidgets.QStyleOptionTab "PySide6.QtWidgets.QStyleOptionTab") |
|  | * [`QStyleOptionTabBarBase`](QStyleOptionTabBarBase.html#PySide6.QtWidgets.QStyleOptionTabBarBase "PySide6.QtWidgets.QStyleOptionTabBarBase") | * [`QStyleOptionTabWidgetFrame`](QStyleOptionTabWidgetFrame.html#PySide6.QtWidgets.QStyleOptionTabWidgetFrame "PySide6.QtWidgets.QStyleOptionTabWidgetFrame") | * [`QStyleOptionTitleBar`](QStyleOptionTitleBar.html#PySide6.QtWidgets.QStyleOptionTitleBar "PySide6.QtWidgets.QStyleOptionTitleBar") |
|  | * [`QStyleOptionToolBar`](QStyleOptionToolBar.html#PySide6.QtWidgets.QStyleOptionToolBar "PySide6.QtWidgets.QStyleOptionToolBar") | * [`QStyleOptionToolBox`](QStyleOptionToolBox.html#PySide6.QtWidgets.QStyleOptionToolBox "PySide6.QtWidgets.QStyleOptionToolBox") | * [`QStyleOptionToolButton`](QStyleOptionToolButton.html#PySide6.QtWidgets.QStyleOptionToolButton "PySide6.QtWidgets.QStyleOptionToolButton") |
|  | * [`QStyleOptionViewItem`](QStyleOptionViewItem.html#PySide6.QtWidgets.QStyleOptionViewItem "PySide6.QtWidgets.QStyleOptionViewItem") | * [`QStylePainter`](QStylePainter.html#PySide6.QtWidgets.QStylePainter "PySide6.QtWidgets.QStylePainter") | * [`QStyledItemDelegate`](QStyledItemDelegate.html#PySide6.QtWidgets.QStyledItemDelegate "PySide6.QtWidgets.QStyledItemDelegate") |
|  | * [`QSwipeGesture`](QSwipeGesture.html#PySide6.QtWidgets.QSwipeGesture "PySide6.QtWidgets.QSwipeGesture") | * [`QSystemTrayIcon`](QSystemTrayIcon.html#PySide6.QtWidgets.QSystemTrayIcon "PySide6.QtWidgets.QSystemTrayIcon") |  |
| **T** | * [`QTabBar`](QTabBar.html#PySide6.QtWidgets.QTabBar "PySide6.QtWidgets.QTabBar") | * [`QTabWidget`](QTabWidget.html#PySide6.QtWidgets.QTabWidget "PySide6.QtWidgets.QTabWidget") | * [`QTableView`](QTableView.html#PySide6.QtWidgets.QTableView "PySide6.QtWidgets.QTableView") |
|  | * [`QTableWidget`](QTableWidget.html#PySide6.QtWidgets.QTableWidget "PySide6.QtWidgets.QTableWidget") | * [`QTableWidgetItem`](QTableWidgetItem.html#PySide6.QtWidgets.QTableWidgetItem "PySide6.QtWidgets.QTableWidgetItem") | * [`QTableWidgetSelectionRange`](QTableWidgetSelectionRange.html#PySide6.QtWidgets.QTableWidgetSelectionRange "PySide6.QtWidgets.QTableWidgetSelectionRange") |
|  | * [`QTapAndHoldGesture`](QTapAndHoldGesture.html#PySide6.QtWidgets.QTapAndHoldGesture "PySide6.QtWidgets.QTapAndHoldGesture") | * [`QTapGesture`](QTapGesture.html#PySide6.QtWidgets.QTapGesture "PySide6.QtWidgets.QTapGesture") | * [`QTextBrowser`](QTextBrowser.html#PySide6.QtWidgets.QTextBrowser "PySide6.QtWidgets.QTextBrowser") |
|  | * [`QTextEdit`](QTextEdit.html#PySide6.QtWidgets.QTextEdit "PySide6.QtWidgets.QTextEdit") | * [`QTileRules`](QTileRules.html#PySide6.QtWidgets.QTileRules "PySide6.QtWidgets.QTileRules") | * [`QTimeEdit`](QTimeEdit.html#PySide6.QtWidgets.QTimeEdit "PySide6.QtWidgets.QTimeEdit") |
|  | * [`QToolBar`](QToolBar.html#PySide6.QtWidgets.QToolBar "PySide6.QtWidgets.QToolBar") | * [`QToolBox`](QToolBox.html#PySide6.QtWidgets.QToolBox "PySide6.QtWidgets.QToolBox") | * [`QToolButton`](QToolButton.html#PySide6.QtWidgets.QToolButton "PySide6.QtWidgets.QToolButton") |
|  | * [`QToolTip`](QToolTip.html#PySide6.QtWidgets.QToolTip "PySide6.QtWidgets.QToolTip") | * [`QTreeView`](QTreeView.html#PySide6.QtWidgets.QTreeView "PySide6.QtWidgets.QTreeView") | * [`QTreeWidget`](QTreeWidget.html#PySide6.QtWidgets.QTreeWidget "PySide6.QtWidgets.QTreeWidget") |
|  | * [`QTreeWidgetItem`](QTreeWidgetItem.html#PySide6.QtWidgets.QTreeWidgetItem "PySide6.QtWidgets.QTreeWidgetItem") | * [`QTreeWidgetItemIterator`](QTreeWidgetItemIterator.html#PySide6.QtWidgets.QTreeWidgetItemIterator "PySide6.QtWidgets.QTreeWidgetItemIterator") | * [`TakeRowResult`](QFormLayout.html#PySide6.QtWidgets.QFormLayout.TakeRowResult "PySide6.QtWidgets.QFormLayout.TakeRowResult") |
| **U** | * [`QUndoView`](QUndoView.html#PySide6.QtWidgets.QUndoView "PySide6.QtWidgets.QUndoView") | | |
| **V** | * [`QVBoxLayout`](QVBoxLayout.html#PySide6.QtWidgets.QVBoxLayout "PySide6.QtWidgets.QVBoxLayout") | | |
| **W** | * [`QWhatsThis`](QWhatsThis.html#PySide6.QtWidgets.QWhatsThis "PySide6.QtWidgets.QWhatsThis") | * [`QWidget`](QWidget.html#PySide6.QtWidgets.QWidget "PySide6.QtWidgets.QWidget") | * [`QWidgetAction`](QWidgetAction.html#PySide6.QtWidgets.QWidgetAction "PySide6.QtWidgets.QWidgetAction") |
|  | * [`QWidgetItem`](QWidgetItem.html#PySide6.QtWidgets.QWidgetItem "PySide6.QtWidgets.QWidgetItem") | * [`QWizard`](QWizard.html#PySide6.QtWidgets.QWizard "PySide6.QtWidgets.QWizard") | * [`QWizardPage`](QWizardPage.html#PySide6.QtWidgets.QWizardPage "PySide6.QtWidgets.QWizardPage") |
## List of Functions[Â¶](#list-of-functions "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **D** | * [`qDrawPlainRect()`](QtWidgets_globals.html#PySide6.QtWidgets.qDrawPlainRect "PySide6.QtWidgets.qDrawPlainRect") | * [`qDrawPlainRoundedRect()`](QtWidgets_globals.html#PySide6.QtWidgets.qDrawPlainRoundedRect "PySide6.QtWidgets.qDrawPlainRoundedRect") | * [`qDrawShadeLine()`](QtWidgets_globals.html#PySide6.QtWidgets.qDrawShadeLine "PySide6.QtWidgets.qDrawShadeLine") |
|  | * [`qDrawShadePanel()`](QtWidgets_globals.html#PySide6.QtWidgets.qDrawShadePanel "PySide6.QtWidgets.qDrawShadePanel") | * [`qDrawShadeRect()`](QtWidgets_globals.html#PySide6.QtWidgets.qDrawShadeRect "PySide6.QtWidgets.qDrawShadeRect") | * [`qDrawWinButton()`](QtWidgets_globals.html#PySide6.QtWidgets.qDrawWinButton "PySide6.QtWidgets.qDrawWinButton") |
|  | * [`qDrawWinPanel()`](QtWidgets_globals.html#PySide6.QtWidgets.qDrawWinPanel "PySide6.QtWidgets.qDrawWinPanel") |  | |
---
<!-- Source: https://doc.qt.io/qtforpython-6/PySide6/QtQml/index.html#module-PySide6.QtQml -->
# PySide6.QtQml[Â¶](#pyside6-qtqml "Link to this heading")
* [Functions](QtQml_globals.html)
* [Enumerations](QtQml_globals.html#enumerations)
* [PySide6.QtQml.QJSEngine](QJSEngine.html)
* [PySide6.QtQml.QJSManagedValue](QJSManagedValue.html)
* [PySide6.QtQml.QJSPrimitiveValue](QJSPrimitiveValue.html)
* [PySide6.QtQml.QJSValue](QJSValue.html)
* [PySide6.QtQml.QJSValueIterator](QJSValueIterator.html)
* [PySide6.QtQml.QQmlAbstractUrlInterceptor](QQmlAbstractUrlInterceptor.html)
* [PySide6.QtQml.QQmlApplicationEngine](QQmlApplicationEngine.html)
* [PySide6.QtQml.QQmlComponent](QQmlComponent.html)
* [PySide6.QtQml.QQmlContext](QQmlContext.html)
* [PySide6.QtQml.QQmlDebuggingEnabler](QQmlDebuggingEnabler.html)
* [PySide6.QtQml.QQmlEngine](QQmlEngine.html)
* [PySide6.QtQml.QQmlError](QQmlError.html)
* [PySide6.QtQml.QQmlExpression](QQmlExpression.html)
* [PySide6.QtQml.QQmlExtensionInterface](QQmlExtensionInterface.html)
* [PySide6.QtQml.QQmlExtensionPlugin](QQmlExtensionPlugin.html)
* [PySide6.QtQml.QQmlFile](QQmlFile.html)
* [PySide6.QtQml.QQmlFileSelector](QQmlFileSelector.html)
* [PySide6.QtQml.QQmlImageProviderBase](QQmlImageProviderBase.html)
* [PySide6.QtQml.QQmlIncubationController](QQmlIncubationController.html)
* [PySide6.QtQml.QQmlIncubator](QQmlIncubator.html)
* [PySide6.QtQml.QQmlListReference](QQmlListReference.html)
* [PySide6.QtQml.QQmlNetworkAccessManagerFactory](QQmlNetworkAccessManagerFactory.html)
* [PySide6.QtQml.QQmlParserStatus](QQmlParserStatus.html)
* [PySide6.QtQml.QQmlProperty](QQmlProperty.html)
* [PySide6.QtQml.QQmlPropertyMap](QQmlPropertyMap.html)
* [PySide6.QtQml.QQmlPropertyValueSource](QQmlPropertyValueSource.html)
* [PySide6.QtQml.QQmlScriptString](QQmlScriptString.html)
* [PySide6.QtQml.QQmlTypesExtensionInterface](QQmlTypesExtensionInterface.html)
* [PySide6.QtQml.ListProperty](ListProperty.html)
* [`QPyQmlParserStatus`](QPyQmlParserStatus.html)
* [`QPyQmlPropertyValueSource`](QPyQmlPropertyValueSource.html)
## Detailed Description[Â¶](#detailed-description "Link to this heading")
The Qt Qml module implements the QML language and offers APIs to register types
for it.
The Qt Qml module provides a framework for developing applications and
libraries with the [The QML Reference](../../overviews/qtqml-qmlreference.html#the-qml-reference) . It defines and implements the
language and engine infrastructure, and provides an API to enable application
developers to register custom QML types and modules and integrate QML code with
JavaScript and Python. The Qt Qml module provides both a QML API a Python API.
### Using the Module[Â¶](#using-the-module "Link to this heading")
To include the definitions of modules classes, use the following
directive:
```
import PySide6.QtQml
```
### Registering QML Types and QML Modules[Â¶](#registering-qml-types-and-qml-modules "Link to this heading")
See [Python-QML integration](../../tutorials/qmlintegration/qmlintegration.html#tutorial-qmlintegration).
### Tweaking the engine[Â¶](#tweaking-the-engine "Link to this heading")
There are a number of knobs you can turn to customize the behavior of the QML
engine. The page on [Configuring the JavaScript Engine](../../overviews/qtqml-javascript-finetuning.html#configuring-the-javascript-engine) lists the
environment variables you may use to this effect. The description of
[The QML Disk Cache](../../overviews/qtqml-qmldiskcache.html#the-qml-disk-cache) describes the options related to how your QML
components are compiled and loaded.
## List of QML types[Â¶](#list-of-qml-types "Link to this heading")
> * [QtQml QML Types](https://doc.qt.io/qt-6/qtqml-qmlmodule.html)
## List of Classes[Â¶](#list-of-classes "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **J** | * [`QJSEngine`](QJSEngine.html#PySide6.QtQml.QJSEngine "PySide6.QtQml.QJSEngine") | * [`QJSManagedValue`](QJSManagedValue.html#PySide6.QtQml.QJSManagedValue "PySide6.QtQml.QJSManagedValue") | * [`QJSPrimitiveValue`](QJSPrimitiveValue.html#PySide6.QtQml.QJSPrimitiveValue "PySide6.QtQml.QJSPrimitiveValue") |
|  | * [`QJSValue`](QJSValue.html#PySide6.QtQml.QJSValue "PySide6.QtQml.QJSValue") | * [`QJSValueIterator`](QJSValueIterator.html#PySide6.QtQml.QJSValueIterator "PySide6.QtQml.QJSValueIterator") |  |
| **L** | * [`ListProperty`](ListProperty.html#PySide6.QtQml.ListProperty "PySide6.QtQml.ListProperty") | | |
| **P** | * [`PropertyPair`](QQmlContext.html#PySide6.QtQml.QQmlContext.PropertyPair "PySide6.QtQml.QQmlContext.PropertyPair") | * [`QPyQmlParserStatus`](QPyQmlParserStatus.html#PySide6.QtQml.QPyQmlParserStatus "PySide6.QtQml.QPyQmlParserStatus") | * [`QPyQmlPropertyValueSource`](QPyQmlPropertyValueSource.html#PySide6.QtQml.QPyQmlPropertyValueSource "PySide6.QtQml.QPyQmlPropertyValueSource") |
| **Q** | * [`QQmlAbstractUrlInterceptor`](QQmlAbstractUrlInterceptor.html#PySide6.QtQml.QQmlAbstractUrlInterceptor "PySide6.QtQml.QQmlAbstractUrlInterceptor") | * [`QQmlApplicationEngine`](QQmlApplicationEngine.html#PySide6.QtQml.QQmlApplicationEngine "PySide6.QtQml.QQmlApplicationEngine") | * [`QQmlComponent`](QQmlComponent.html#PySide6.QtQml.QQmlComponent "PySide6.QtQml.QQmlComponent") |
|  | * [`QQmlContext`](QQmlContext.html#PySide6.QtQml.QQmlContext "PySide6.QtQml.QQmlContext") | * [`QQmlDebuggingEnabler`](QQmlDebuggingEnabler.html#PySide6.QtQml.QQmlDebuggingEnabler "PySide6.QtQml.QQmlDebuggingEnabler") | * [`QQmlEngine`](QQmlEngine.html#PySide6.QtQml.QQmlEngine "PySide6.QtQml.QQmlEngine") |
|  | * [`QQmlError`](QQmlError.html#PySide6.QtQml.QQmlError "PySide6.QtQml.QQmlError") | * [`QQmlExpression`](QQmlExpression.html#PySide6.QtQml.QQmlExpression "PySide6.QtQml.QQmlExpression") | * [`QQmlExtensionInterface`](QQmlExtensionInterface.html#PySide6.QtQml.QQmlExtensionInterface "PySide6.QtQml.QQmlExtensionInterface") |
|  | * [`QQmlExtensionPlugin`](QQmlExtensionPlugin.html#PySide6.QtQml.QQmlExtensionPlugin "PySide6.QtQml.QQmlExtensionPlugin") | * [`QQmlFile`](QQmlFile.html#PySide6.QtQml.QQmlFile "PySide6.QtQml.QQmlFile") | * [`QQmlFileSelector`](QQmlFileSelector.html#PySide6.QtQml.QQmlFileSelector "PySide6.QtQml.QQmlFileSelector") |
|  | * [`QQmlImageProviderBase`](QQmlImageProviderBase.html#PySide6.QtQml.QQmlImageProviderBase "PySide6.QtQml.QQmlImageProviderBase") | * [`QQmlIncubationController`](QQmlIncubationController.html#PySide6.QtQml.QQmlIncubationController "PySide6.QtQml.QQmlIncubationController") | * [`QQmlIncubator`](QQmlIncubator.html#PySide6.QtQml.QQmlIncubator "PySide6.QtQml.QQmlIncubator") |
|  | * [`QQmlListReference`](QQmlListReference.html#PySide6.QtQml.QQmlListReference "PySide6.QtQml.QQmlListReference") | * [`QQmlNetworkAccessManagerFactory`](QQmlNetworkAccessManagerFactory.html#PySide6.QtQml.QQmlNetworkAccessManagerFactory "PySide6.QtQml.QQmlNetworkAccessManagerFactory") | * [`QQmlParserStatus`](QQmlParserStatus.html#PySide6.QtQml.QQmlParserStatus "PySide6.QtQml.QQmlParserStatus") |
|  | * [`QQmlProperty`](QQmlProperty.html#PySide6.QtQml.QQmlProperty "PySide6.QtQml.QQmlProperty") | * [`QQmlPropertyMap`](QQmlPropertyMap.html#PySide6.QtQml.QQmlPropertyMap "PySide6.QtQml.QQmlPropertyMap") | * [`QQmlPropertyValueSource`](QQmlPropertyValueSource.html#PySide6.QtQml.QQmlPropertyValueSource "PySide6.QtQml.QQmlPropertyValueSource") |
|  | * [`QQmlScriptString`](QQmlScriptString.html#PySide6.QtQml.QQmlScriptString "PySide6.QtQml.QQmlScriptString") | * [`QQmlTypesExtensionInterface`](QQmlTypesExtensionInterface.html#PySide6.QtQml.QQmlTypesExtensionInterface "PySide6.QtQml.QQmlTypesExtensionInterface") |  |
## List of Decorators[Â¶](#list-of-decorators "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **Q** | * [`@QmlAnonymous`](QmlAnonymous.html#PySide6.QtQml.QmlAnonymous "PySide6.QtQml.QmlAnonymous") | * [`@QmlAttached`](QmlAttached.html#PySide6.QtQml.QmlAttached "PySide6.QtQml.QmlAttached") | * [`@QmlElement`](QmlElement.html#PySide6.QtQml.QmlElement "PySide6.QtQml.QmlElement") |
|  | * [`@QmlExtended`](QmlExtended.html#PySide6.QtQml.QmlExtended "PySide6.QtQml.QmlExtended") | * [`@QmlForeign`](QmlForeign.html#PySide6.QtQml.QmlForeign "PySide6.QtQml.QmlForeign") | * [`@QmlNamedElement`](QmlNamedElement.html#PySide6.QtQml.QmlNamedElement "PySide6.QtQml.QmlNamedElement") |
|  | * [`@QmlSingleton`](QmlSingleton.html#PySide6.QtQml.QmlSingleton "PySide6.QtQml.QmlSingleton") | * [`@QmlUncreatable`](QmlUncreatable.html#PySide6.QtQml.QmlUncreatable "PySide6.QtQml.QmlUncreatable") |  |
## List of Functions[Â¶](#list-of-functions "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **Q** | * [`qjsEngine()`](QtQml_globals.html#PySide6.QtQml.qjsEngine "PySide6.QtQml.qjsEngine") | * [`qmlClearTypeRegistrations()`](QtQml_globals.html#PySide6.QtQml.qmlClearTypeRegistrations "PySide6.QtQml.qmlClearTypeRegistrations") | * [`qmlContext()`](QtQml_globals.html#PySide6.QtQml.qmlContext "PySide6.QtQml.qmlContext") |
|  | * [`qmlEngine()`](QtQml_globals.html#PySide6.QtQml.qmlEngine "PySide6.QtQml.qmlEngine") | * [`qmlProtectModule()`](QtQml_globals.html#PySide6.QtQml.qmlProtectModule "PySide6.QtQml.qmlProtectModule") | * [`qmlRegisterModule()`](QtQml_globals.html#PySide6.QtQml.qmlRegisterModule "PySide6.QtQml.qmlRegisterModule") |
|  | * [`qmlRegisterSingletonType()`](QtQml_globals.html#id3 "PySide6.QtQml.qmlRegisterSingletonType") | * [`qmlRegisterType()`](QtQml_globals.html#id0 "PySide6.QtQml.qmlRegisterType") | * [`qmlRegisterUncreatableMetaObject()`](QtQml_globals.html#PySide6.QtQml.qmlRegisterUncreatableMetaObject "PySide6.QtQml.qmlRegisterUncreatableMetaObject") |
|  | * [`qmlTypeId()`](QtQml_globals.html#PySide6.QtQml.qmlTypeId "PySide6.QtQml.qmlTypeId") | * [`qmlAttachedPropertiesObject()`](QtQml_globals.html#PySide6.QtQml.qmlAttachedPropertiesObject "PySide6.QtQml.qmlAttachedPropertiesObject") | * [`qmlRegisterSingletonInstance()`](QtQml_globals.html#PySide6.QtQml.qmlRegisterSingletonInstance "PySide6.QtQml.qmlRegisterSingletonInstance") |
|  | * [`qmlRegisterUncreatableType()`](QtQml_globals.html#PySide6.QtQml.qmlRegisterUncreatableType "PySide6.QtQml.qmlRegisterUncreatableType") |  | |
## List of Enumerations[Â¶](#list-of-enumerations "Link to this heading")
|  |  |
| --- | --- |
| **M** | * [`QML_HAS_ATTACHED_PROPERTIES`](QtQml_globals.html#PySide6.QtQml.QML_HAS_ATTACHED_PROPERTIES "PySide6.QtQml.QML_HAS_ATTACHED_PROPERTIES") |
| **Q** | * [`QQmlModuleImportSpecialVersions`](QtQml_globals.html#PySide6.QtQml.QQmlModuleImportSpecialVersions "PySide6.QtQml.QQmlModuleImportSpecialVersions") |
---
<!-- Source: https://doc.qt.io/qtforpython-6/PySide6/QtQuick/index.html#module-PySide6.QtQuick -->
# PySide6.QtQuick[Â¶](#pyside6-qtquick "Link to this heading")
* [PySide6.QtQuick.QQuickAsyncImageProvider](QQuickAsyncImageProvider.html)
* [PySide6.QtQuick.QQuickFramebufferObject](QQuickFramebufferObject.html)
* [PySide6.QtQuick.QQuickGraphicsConfiguration](QQuickGraphicsConfiguration.html)
* [PySide6.QtQuick.QQuickGraphicsDevice](QQuickGraphicsDevice.html)
* [PySide6.QtQuick.QQuickImageProvider](QQuickImageProvider.html)
* [PySide6.QtQuick.QQuickImageResponse](QQuickImageResponse.html)
* [PySide6.QtQuick.QQuickItem](QQuickItem.html)
* [PySide6.QtQuick.QQuickItemGrabResult](QQuickItemGrabResult.html)
* [PySide6.QtQuick.QQuickOpenGLUtils](QQuickOpenGLUtils.html)
* [PySide6.QtQuick.QQuickPaintedItem](QQuickPaintedItem.html)
* [PySide6.QtQuick.QQuickRenderControl](QQuickRenderControl.html)
* [PySide6.QtQuick.QQuickRenderTarget](QQuickRenderTarget.html)
* [PySide6.QtQuick.QQuickRhiItem](QQuickRhiItem.html)
* [PySide6.QtQuick.QQuickRhiItemRenderer](QQuickRhiItemRenderer.html)
* [PySide6.QtQuick.QQuickTextDocument](QQuickTextDocument.html)
* [PySide6.QtQuick.QQuickTextureFactory](QQuickTextureFactory.html)
* [PySide6.QtQuick.QQuickTransform](QQuickTransform.html)
* [PySide6.QtQuick.QQuickView](QQuickView.html)
* [PySide6.QtQuick.QQuickWindow](QQuickWindow.html)
* [PySide6.QtQuick.QSGBasicGeometryNode](QSGBasicGeometryNode.html)
* [PySide6.QtQuick.QSGClipNode](QSGClipNode.html)
* [PySide6.QtQuick.QSGDynamicTexture](QSGDynamicTexture.html)
* [PySide6.QtQuick.QSGFlatColorMaterial](QSGFlatColorMaterial.html)
* [PySide6.QtQuick.QSGGeometry](QSGGeometry.html)
* [PySide6.QtQuick.QSGGeometryNode](QSGGeometryNode.html)
* [PySide6.QtQuick.QSGImageNode](QSGImageNode.html)
* [PySide6.QtQuick.QSGMaterial](QSGMaterial.html)
* [PySide6.QtQuick.QSGMaterialShader](QSGMaterialShader.html)
* [PySide6.QtQuick.QSGMaterialType](QSGMaterialType.html)
* [PySide6.QtQuick.QSGNinePatchNode](QSGNinePatchNode.html)
* [PySide6.QtQuick.QSGNode](QSGNode.html)
* [PySide6.QtQuick.QSGNodeVisitor](QSGNodeVisitor.html)
* [PySide6.QtQuick.QSGOpacityNode](QSGOpacityNode.html)
* [PySide6.QtQuick.QSGOpaqueTextureMaterial](QSGOpaqueTextureMaterial.html)
* [PySide6.QtQuick.QSGRectangleNode](QSGRectangleNode.html)
* [PySide6.QtQuick.QSGRenderNode](QSGRenderNode.html)
* [PySide6.QtQuick.QSGRendererInterface](QSGRendererInterface.html)
* [PySide6.QtQuick.QSGRootNode](QSGRootNode.html)
* [PySide6.QtQuick.QSGSimpleRectNode](QSGSimpleRectNode.html)
* [PySide6.QtQuick.QSGSimpleTextureNode](QSGSimpleTextureNode.html)
* [PySide6.QtQuick.QSGTextNode](QSGTextNode.html)
* [PySide6.QtQuick.QSGTexture](QSGTexture.html)
* [PySide6.QtQuick.QSGTextureMaterial](QSGTextureMaterial.html)
* [PySide6.QtQuick.QSGTextureProvider](QSGTextureProvider.html)
* [PySide6.QtQuick.QSGTransformNode](QSGTransformNode.html)
* [PySide6.QtQuick.QSGVertexColorMaterial](QSGVertexColorMaterial.html)
## Detailed Description[Â¶](#detailed-description "Link to this heading")
The Qt Quick module implements the âstandard libraryâ for QML
The Qt Quick module is the standard library for writing QML applications. While
the Qt Qml module provides the QML engine and language infrastructure, the Qt
Quick module provides all the basic types necessary for creating user
interfaces with QML. It provides a visual canvas and includes types for
creating and animating visual components, receiving user input, creating data
models and views and delayed object instantiation.
The Qt Quick module provides both a QML API, which supplies QML types for
creating user interfaces with the QML language, and a Python API for extending
QML applications with Python code.
Note
A set of Qt Quick-based UI controls is also available to create user interfaces.
See [`PySide6.QtQuickControls2`](../QtQuickControls2/index.html#module-PySide6.QtQuickControls2 "PySide6.QtQuickControls2") for more information.
If youâre new to QML and Qt Quick, please see
[Getting started with Qt Quick applications](../../overviews/qtquick-qmlapplications.html#getting-started-with-qt-quick-applications)
for an introduction to writing QML applications.
### Using the Module[Â¶](#using-the-module "Link to this heading")
To include the definitions of modules classes, use the following
directive:
```
import PySide6.QtQuick
```
### Important Concepts in Qt Quick[Â¶](#important-concepts-in-qt-quick "Link to this heading")
Qt Quick provides everything you need to create a rich application with a fluid
and dynamic user interface. It enables you to build user interfaces around the
behavior of user interface components and how they connect with one another,
and it provides a visual canvas with its own coordinate system and rendering
engine. Animation and transition effects are first class concepts in Qt Quick,
and you can add visual effects through specialized components for particle and
shader effects.
> * [Important Concepts In Qt Quick - The Visual Canvas](../../overviews/qtquick-visualcanvas-topic.html#important-concepts-in-qt-quick-the-visual-canvas)
> * [Important Concepts In Qt Quick - User Input](../../overviews/qtquick-input-topic.html#important-concepts-in-qt-quick-user-input)
> * [Important Concepts In Qt Quick - Positioning](../../overviews/qtquick-positioning-topic.html#important-concepts-in-qt-quick-positioning)
> * [Important Concepts in Qt Quick - States, Transitions and Animations](../../overviews/qtquick-statesanimations-topic.html#important-concepts-in-qt-quick-states-transitions-and-animations)
> * [Important Concepts In Qt Quick - Data - Models, Views, and Data Storage](../../overviews/qtquick-modelviewsdata-topic.html#important-concepts-in-qt-quick-data-models-views-and-data-storage)
> * [Important Concepts In Qt Quick - Graphical Effects](../../overviews/qtquick-effects-topic.html#important-concepts-in-qt-quick-graphical-effects)
> * [MultiEffect](https://doc.qt.io/qt-6/qml-qtquick-effects-multieffect.html)
> * [Important Concepts In Qt Quick - Convenience Types](../../overviews/qtquick-convenience-topic.html#important-concepts-in-qt-quick-convenience-types)
When using the Qt Quick module, you will need to know how to write QML
applications using the QML language. In particular, QML Basics and QML
Essentials from the QML Applications page.
To find out more about using the QML language, see [`Qt Qml`](../QtQml/index.html#module-PySide6.QtQml "PySide6.QtQml").
### C++ Extension Points[Â¶](#c-extension-points "Link to this heading")
> * [C++ Extension Points](../../overviews/qtquick-cppextensionpoints.html#c-extension-points-provided-by-qt-quick)
### Articles and Guides[Â¶](#articles-and-guides "Link to this heading")
> * [Qt Quick Guidelines](../../overviews/qtquick-bestpractices.html#best-practices-for-qml-and-qt-quick)
> * [Qt Quick Tools and Utilities](../../overviews/qtquick-tools-and-utilities.html#qt-quick-tools-and-utilities)
Further information for writing QML applications:
> * [Getting started with Qt Quick applications](../../overviews/qtquick-qmlapplications.html#getting-started-with-qt-quick-applications) - Essential information for application development with QML and Qt Quick
> * [`Qt Qml`](../QtQml/index.html#module-PySide6.QtQml "PySide6.QtQml") - Documentation for the Qt QML module, which provides the QML engine and language infrastructure
> * [Qt Quick How-tos](../../overviews/qtquick-how-tos.html#qt-quick-how-tos) - shows how to achieve specific tasks in Qt Quick
### Qt Academy Courses[Â¶](#qt-academy-courses "Link to this heading")
> * [Introduction to Qt Quick](https://www.qt.io/academy/course-catalog#introduction-to-qt-quick)
## List of Classes by Function[Â¶](#list-of-classes-by-function "Link to this heading")
> * [Qt Quick Scene Graph Material Classes](../../groups/qtquick-scenegraph-materials.html#qt-quick-scene-graph-material-classes)
> * [Qt Quick Scene Graph Node classes](../../groups/qtquick-scenegraph-nodes.html#qt-quick-scene-graph-node-classes)
## List of QML types[Â¶](#list-of-qml-types "Link to this heading")
> * [QtQuick QML Types](https://doc.qt.io/qt-6/qtquick-qmlmodule.html)
## List of Classes[Â¶](#list-of-classes "Link to this heading")
|  |  |  |  |
| --- | --- | --- | --- |
| **A** | * [`Attribute`](QSGGeometry.html#PySide6.QtQuick.QSGGeometry.Attribute "PySide6.QtQuick.QSGGeometry.Attribute") | * [`AttributeSet`](QSGGeometry.html#PySide6.QtQuick.QSGGeometry.AttributeSet "PySide6.QtQuick.QSGGeometry.AttributeSet") |  |
| **C** | * [`ColoredPoint2D`](QSGGeometry.html#PySide6.QtQuick.QSGGeometry.ColoredPoint2D "PySide6.QtQuick.QSGGeometry.ColoredPoint2D") | | |
| **G** | * [`GraphicsPipelineState`](QSGMaterialShader.html#PySide6.QtQuick.QSGMaterialShader.GraphicsPipelineState "PySide6.QtQuick.QSGMaterialShader.GraphicsPipelineState") | * [`GraphicsStateInfo`](QQuickWindow.html#PySide6.QtQuick.QQuickWindow.GraphicsStateInfo "PySide6.QtQuick.QQuickWindow.GraphicsStateInfo") |  |
| **P** | * [`Point2D`](QSGGeometry.html#PySide6.QtQuick.QSGGeometry.Point2D "PySide6.QtQuick.QSGGeometry.Point2D") | | |
| **Q** | * [`QQuickAsyncImageProvider`](QQuickAsyncImageProvider.html#PySide6.QtQuick.QQuickAsyncImageProvider "PySide6.QtQuick.QQuickAsyncImageProvider") | * [`QQuickFramebufferObject`](QQuickFramebufferObject.html#PySide6.QtQuick.QQuickFramebufferObject "PySide6.QtQuick.QQuickFramebufferObject") | * [`QQuickGraphicsConfiguration`](QQuickGraphicsConfiguration.html#PySide6.QtQuick.QQuickGraphicsConfiguration "PySide6.QtQuick.QQuickGraphicsConfiguration") |
|  | * [`QQuickGraphicsDevice`](QQuickGraphicsDevice.html#PySide6.QtQuick.QQuickGraphicsDevice "PySide6.QtQuick.QQuickGraphicsDevice") | * [`QQuickImageProvider`](QQuickImageProvider.html#PySide6.QtQuick.QQuickImageProvider "PySide6.QtQuick.QQuickImageProvider") | * [`QQuickImageResponse`](QQuickImageResponse.html#PySide6.QtQuick.QQuickImageResponse "PySide6.QtQuick.QQuickImageResponse") |
|  | * [`QQuickItem`](QQuickItem.html#PySide6.QtQuick.QQuickItem "PySide6.QtQuick.QQuickItem") | * [`QQuickItemGrabResult`](QQuickItemGrabResult.html#PySide6.QtQuick.QQuickItemGrabResult "PySide6.QtQuick.QQuickItemGrabResult") | * [`QQuickOpenGLUtils`](QQuickOpenGLUtils.html#PySide6.QtQuick.QQuickOpenGLUtils "PySide6.QtQuick.QQuickOpenGLUtils") |
|  | * [`QQuickPaintedItem`](QQuickPaintedItem.html#PySide6.QtQuick.QQuickPaintedItem "PySide6.QtQuick.QQuickPaintedItem") | * [`QQuickRenderControl`](QQuickRenderControl.html#PySide6.QtQuick.QQuickRenderControl "PySide6.QtQuick.QQuickRenderControl") | * [`QQuickRenderTarget`](QQuickRenderTarget.html#PySide6.QtQuick.QQuickRenderTarget "PySide6.QtQuick.QQuickRenderTarget") |
|  | * [`QQuickRhiItem`](QQuickRhiItem.html#PySide6.QtQuick.QQuickRhiItem "PySide6.QtQuick.QQuickRhiItem") | * [`QQuickRhiItemRenderer`](QQuickRhiItemRenderer.html#PySide6.QtQuick.QQuickRhiItemRenderer "PySide6.QtQuick.QQuickRhiItemRenderer") | * [`QQuickTextDocument`](QQuickTextDocument.html#PySide6.QtQuick.QQuickTextDocument "PySide6.QtQuick.QQuickTextDocument") |
|  | * [`QQuickTextureFactory`](QQuickTextureFactory.html#PySide6.QtQuick.QQuickTextureFactory "PySide6.QtQuick.QQuickTextureFactory") | * [`QQuickTransform`](QQuickTransform.html#PySide6.QtQuick.QQuickTransform "PySide6.QtQuick.QQuickTransform") | * [`QQuickView`](QQuickView.html#PySide6.QtQuick.QQuickView "PySide6.QtQuick.QQuickView") |
|  | * [`QQuickWindow`](QQuickWindow.html#PySide6.QtQuick.QQuickWindow "PySide6.QtQuick.QQuickWindow") |  | |
| **R** | * [`RenderState`](QSGMaterialShader.html#PySide6.QtQuick.QSGMaterialShader.RenderState "PySide6.QtQuick.QSGMaterialShader.RenderState") | * [`RenderState`](QSGRenderNode.html#PySide6.QtQuick.QSGRenderNode.RenderState "PySide6.QtQuick.QSGRenderNode.RenderState") | * [`Renderer`](QQuickFramebufferObject.html#PySide6.QtQuick.QQuickFramebufferObject.Renderer "PySide6.QtQuick.QQuickFramebufferObject.Renderer") |
| **S** | * [`QSGBasicGeometryNode`](QSGBasicGeometryNode.html#PySide6.QtQuick.QSGBasicGeometryNode "PySide6.QtQuick.QSGBasicGeometryNode") | * [`QSGClipNode`](QSGClipNode.html#PySide6.QtQuick.QSGClipNode "PySide6.QtQuick.QSGClipNode") | * [`QSGDynamicTexture`](QSGDynamicTexture.html#PySide6.QtQuick.QSGDynamicTexture "PySide6.QtQuick.QSGDynamicTexture") |
|  | * [`QSGFlatColorMaterial`](QSGFlatColorMaterial.html#PySide6.QtQuick.QSGFlatColorMaterial "PySide6.QtQuick.QSGFlatColorMaterial") | * [`QSGGeometry`](QSGGeometry.html#PySide6.QtQuick.QSGGeometry "PySide6.QtQuick.QSGGeometry") | * [`QSGGeometryNode`](QSGGeometryNode.html#PySide6.QtQuick.QSGGeometryNode "PySide6.QtQuick.QSGGeometryNode") |
|  | * [`QSGImageNode`](QSGImageNode.html#PySide6.QtQuick.QSGImageNode "PySide6.QtQuick.QSGImageNode") | * [`QSGMaterial`](QSGMaterial.html#PySide6.QtQuick.QSGMaterial "PySide6.QtQuick.QSGMaterial") | * [`QSGMaterialShader`](QSGMaterialShader.html#PySide6.QtQuick.QSGMaterialShader "PySide6.QtQuick.QSGMaterialShader") |
|  | * [`QSGMaterialType`](QSGMaterialType.html#PySide6.QtQuick.QSGMaterialType "PySide6.QtQuick.QSGMaterialType") | * [`QSGNinePatchNode`](QSGNinePatchNode.html#PySide6.QtQuick.QSGNinePatchNode "PySide6.QtQuick.QSGNinePatchNode") | * [`QSGNode`](QSGNode.html#PySide6.QtQuick.QSGNode "PySide6.QtQuick.QSGNode") |
|  | * [`QSGNodeVisitor`](QSGNodeVisitor.html#PySide6.QtQuick.QSGNodeVisitor "PySide6.QtQuick.QSGNodeVisitor") | * [`QSGOpacityNode`](QSGOpacityNode.html#PySide6.QtQuick.QSGOpacityNode "PySide6.QtQuick.QSGOpacityNode") | * [`QSGOpaqueTextureMaterial`](QSGOpaqueTextureMaterial.html#PySide6.QtQuick.QSGOpaqueTextureMaterial "PySide6.QtQuick.QSGOpaqueTextureMaterial") |
|  | * [`QSGRectangleNode`](QSGRectangleNode.html#PySide6.QtQuick.QSGRectangleNode "PySide6.QtQuick.QSGRectangleNode") | * [`QSGRenderNode`](QSGRenderNode.html#PySide6.QtQuick.QSGRenderNode "PySide6.QtQuick.QSGRenderNode") | * [`QSGRendererInterface`](QSGRendererInterface.html#PySide6.QtQuick.QSGRendererInterface "PySide6.QtQuick.QSGRendererInterface") |
|  | * [`QSGRootNode`](QSGRootNode.html#PySide6.QtQuick.QSGRootNode "PySide6.QtQuick.QSGRootNode") | * [`QSGSimpleRectNode`](QSGSimpleRectNode.html#PySide6.QtQuick.QSGSimpleRectNode "PySide6.QtQuick.QSGSimpleRectNode") | * [`QSGSimpleTextureNode`](QSGSimpleTextureNode.html#PySide6.QtQuick.QSGSimpleTextureNode "PySide6.QtQuick.QSGSimpleTextureNode") |
|  | * [`QSGTextNode`](QSGTextNode.html#PySide6.QtQuick.QSGTextNode "PySide6.QtQuick.QSGTextNode") | * [`QSGTexture`](QSGTexture.html#PySide6.QtQuick.QSGTexture "PySide6.QtQuick.QSGTexture") | * [`QSGTextureMaterial`](QSGTextureMaterial.html#PySide6.QtQuick.QSGTextureMaterial "PySide6.QtQuick.QSGTextureMaterial") |
|  | * [`QSGTextureProvider`](QSGTextureProvider.html#PySide6.QtQuick.QSGTextureProvider "PySide6.QtQuick.QSGTextureProvider") | * [`QSGTransformNode`](QSGTransformNode.html#PySide6.QtQuick.QSGTransformNode "PySide6.QtQuick.QSGTransformNode") | * [`QSGVertexColorMaterial`](QSGVertexColorMaterial.html#PySide6.QtQuick.QSGVertexColorMaterial "PySide6.QtQuick.QSGVertexColorMaterial") |
| **T** | * [`TexturedPoint2D`](QSGGeometry.html#PySide6.QtQuick.QSGGeometry.TexturedPoint2D "PySide6.QtQuick.QSGGeometry.TexturedPoint2D") | | |
| **U** | * [`UpdatePaintNodeData`](QQuickItem.html#PySide6.QtQuick.QQuickItem.UpdatePaintNodeData "PySide6.QtQuick.QQuickItem.UpdatePaintNodeData") | | |
---
<!-- Source: https://doc.qt.io/qtforpython-6/PySide6/QtQuickControls2/index.html#module-PySide6.QtQuickControls2 -->
# PySide6.QtQuickControls2[Â¶](#pyside6-qtquickcontrols2 "Link to this heading")
* [PySide6.QtQuickControls2.QQuickAttachedPropertyPropagator](QQuickAttachedPropertyPropagator.html)
* [PySide6.QtQuickControls2.QQuickStyle](QQuickStyle.html)
## Detailed Description[Â¶](#detailed-description "Link to this heading")
Provides a set of UI controls for Qt Quick.
Qt Quick Controls provides a set of controls that can be used to build complete
interfaces in Qt Quick. The module was introduced in Qt 5.7.
> ![../../_images/qtquickcontrols-styles.png](../../_images/qtquickcontrols-styles.png)
Qt Quick Controls comes with a selection customizable styles. See
[Styling Qt Quick Controls](../../overviews/qtquickcontrols-styles.html#styling-qt-quick-controls) for more details.
### Using the Module[Â¶](#using-the-module "Link to this heading")
To include the definitions of modules classes, use the following
directive:
```
import PySide6.QtQuickControls2
```
### Versions[Â¶](#versions "Link to this heading")
Qt Quick Controls 2.0 was introduced in Qt 5.7. Subsequent minor Qt releases
increment the import version of the Qt Quick Controls modules by one, until Qt
5.12, where the import versions match Qtâs minor version.
In Qt 6, both the major and minor versions match, and version numbers may be
omitted from imports in QML. If the version is omitted, the latest version will
be used.
### Topics[Â¶](#topics "Link to this heading")
> * [Getting Started](https://doc.qt.io/qt-6/qtquickcontrols2-gettingstarted.html)
> * [Guidelines](https://doc.qt.io/qt-6/qtquickcontrols2-guidelines.html)
> * [Styling](https://doc.qt.io/qt-6/qtquickcontrols2-styles.html)
> * [Icons](https://doc.qt.io/qt-6/qtquickcontrols2-icons.html)
> * [Customization](https://doc.qt.io/qt-6/qtquickcontrols2-customize.html)
> * [Using File Selectors](https://doc.qt.io/qt-6/qtquickcontrols2-fileselectors.html)
> * [Deployment](https://doc.qt.io/qt-6/qtquickcontrols2-deployment.html)
> * [Configuration File](https://doc.qt.io/qt-6/qtquickcontrols2-configuration.html)
> * [Environment Variables](https://doc.qt.io/qt-6/qtquickcontrols2-environment.html)
## List of QML types[Â¶](#list-of-qml-types "Link to this heading")
> * [QtQuickControls2 QML Types](https://doc.qt.io/qt-6/qtquick-controls-qmlmodule.html)
## List of Classes[Â¶](#list-of-classes "Link to this heading")
|  |  |  |
| --- | --- | --- |
| **Q** | * [`QQuickAttachedPropertyPropagator`](QQuickAttachedPropertyPropagator.html#PySide6.QtQuickControls2.QQuickAttachedPropertyPropagator "PySide6.QtQuickControls2.QQuickAttachedPropertyPropagator") | * [`QQuickStyle`](QQuickStyle.html#PySide6.QtQuickControls2.QQuickStyle "PySide6.QtQuickControls2.QQuickStyle") |
---
<!-- Source: https://doc.qt.io/qtforpython-6/PySide6/QtQuickWidgets/index.html#module-PySide6.QtQuickWidgets -->
# PySide6.QtQuickWidgets[Â¶](#pyside6-qtquickwidgets "Link to this heading")
* [PySide6.QtQuickWidgets.QQuickWidget](QQuickWidget.html)
## Detailed Description[Â¶](#detailed-description "Link to this heading")
Provides a C++ widget class for displaying a Qt Quick user interface.
The Qt Quick Widgets module is a convenience wrapper for [`QQuickWindow`](../QtQuick/QQuickWindow.html#PySide6.QtQuick.QQuickWindow "PySide6.QtQuick.QQuickWindow") . It will automatically load and display a QML scene when given the URL of the main `qml` file. Alternatively, you can instantiate QML objects using QQmlComponent and place them in a manually set-up [`QQuickWidget`](QQuickWidget.html#PySide6.QtQuickWidgets.QQuickWidget "PySide6.QtQuickWidgets.QQuickWidget") .
Typical usage:
> ```
> QQuickWidget *view = new QQuickWidget;
> view->setSource(QUrl::fromLocalFile("myqmlfile.qml"));
> view->show();
> ```
[`QQuickWidget`](QQuickWidget.html#PySide6.QtQuickWidgets.QQuickWidget "PySide6.QtQuickWidgets.QQuickWidget") also manages resizing the view and the root item. By default, the [`resizeMode`](QQuickWidget.html#id0 "PySide6.QtQuickWidgets.QQuickWidget.resizeMode") is set to [`SizeViewToRootObject`](QQuickWidget.html#PySide6.QtQuickWidgets.QQuickWidget.ResizeMode "PySide6.QtQuickWidgets.QQuickWidget.ResizeMode") , which will load the component and resize it to fit the view. Alternatively, you can set [`resizeMode`](QQuickWidget.html#id0 "PySide6.QtQuickWidgets.QQuickWidget.resizeMode") to [`SizeViewToRootObject`](QQuickWidget.html#PySide6.QtQuickWidgets.QQuickWidget.ResizeMode "PySide6.QtQuickWidgets.QQuickWidget.ResizeMode") , which will resize the view to the root item.
### Building with qmake quickwidgets[Â¶](#building-with-qmake-quickwidgets "Link to this heading")
To configure the module for building with qmake, add the module as a value of the `QT` variable in the projectâs .pro file:
> ```
> QT += quickwidgets
> ```
# Licenses and Attributions[Â¶](#licenses-and-attributions "Link to this heading")
Qt Quick Widget is available under commercial licenses from The Qt Company. In addition, it is available under free software licenses. Since Qt 5.4, these free software licenses are GNU Lesser General Public License, version 3, or the GNU General Public License, version 2. See Qt Licensing for more details.
## List of QML types[Â¶](#list-of-qml-types "Link to this heading")
> * [QtQuickWidgets QML Types](https://doc.qt.io/qt-6/qt-labs-animation-qmlmodule.html)
## List of Classes[Â¶](#list-of-classes "Link to this heading")
|  |  |
| --- | --- |
| **Q** | * [`QQuickWidget`](QQuickWidget.html#PySide6.QtQuickWidgets.QQuickWidget "PySide6.QtQuickWidgets.QQuickWidget") |
---
<!-- Source: https://doc.qt.io/qtforpython-6/modules.html -->
# Qt Modules Supported by Qt for Python[Â¶](#qt-modules-supported-by-qt-for-python "Link to this heading")
[`Qt Bluetooth`](PySide6/QtBluetooth/index.html#module-PySide6.QtBluetooth "PySide6.QtBluetooth")
Provides access to Bluetooth hardware.
[`Qt Canvas Painter`](PySide6/QtCanvasPainter/index.html#module-PySide6.QtCanvasPainter "PySide6.QtCanvasPainter")
Provides an API for accelerated, imperative 2D painting.
`Qt Charts`
Deprecated since Qt 6.10 in favor of [`Qt Graphs`](PySide6/QtGraphs/index.html#module-PySide6.QtGraphs "PySide6.QtGraphs").
UI Components for displaying charts.
[`Qt Concurrent`](PySide6/QtConcurrent/index.html#module-PySide6.QtConcurrent "PySide6.QtConcurrent")
Classes for writing multi-threaded programs without using low-level
threading primitives.
[`Qt Core`](PySide6/QtCore/index.html#module-PySide6.QtCore "PySide6.QtCore")
Core non-graphical classes used by other modules.
`Qt Data Visualization`
Deprecated since Qt 6.10 in favor of [`Qt Graphs`](PySide6/QtGraphs/index.html#module-PySide6.QtGraphs "PySide6.QtGraphs").
UI Components for creating 3D data visualizations.
[`Qt D-Bus`](PySide6/QtDBus/index.html#module-PySide6.QtDBus "PySide6.QtDBus")
Classes for inter-process communication over the D-Bus protocol.
[`Qt Designer`](PySide6/QtDesigner/index.html#module-PySide6.QtDesigner "PySide6.QtDesigner")
Provides classes to extend *Qt Widgets Designer*.
[`Qt GUI`](PySide6/QtGui/index.html#module-PySide6.QtGui "PySide6.QtGui")
Base classes for graphical user interface (GUI) components.
[`Qt Graphs`](PySide6/QtGraphs/index.html#module-PySide6.QtGraphs "PySide6.QtGraphs")
Provides functionality for visualizing data in 3D as bar, scatter, and
surface graphs, as well as 2D in area, bar, donut, line, pie, scatter, and
spline graphs.
[`QtGraphs Widgets`](PySide6/QtGraphsWidgets/index.html#module-PySide6.QtGraphsWidgets "PySide6.QtGraphsWidgets")
Provides the widget-based graphs API.
[`Qt Help`](PySide6/QtHelp/index.html#module-PySide6.QtHelp "PySide6.QtHelp")
Classes for integrating documentation into applications.
[`Qt HTTP Server`](PySide6/QtHttpServer/index.html#module-PySide6.QtHttpServer "PySide6.QtHttpServer")
A framework for embedding an HTTP server into a Qt application.
[`Qt Location`](PySide6/QtLocation/index.html#module-PySide6.QtLocation "PySide6.QtLocation")
Provides QML and Python interfaces to create location-aware applications.
[`Qt Multimedia`](PySide6/QtMultimedia/index.html#module-PySide6.QtMultimedia "PySide6.QtMultimedia")
A rich set of QML types and Python classes to handle multimedia content.
Also includes APIs to handle camera access.
[`Qt Multimedia Widgets`](PySide6/QtMultimediaWidgets/index.html#module-PySide6.QtMultimediaWidgets "PySide6.QtMultimediaWidgets")
Provides the widget-based multimedia API.
[`Qt Network`](PySide6/QtNetwork/index.html#module-PySide6.QtNetwork "PySide6.QtNetwork")
Classes to make network programming easier and more portable.
[`Qt Network Authorization`](PySide6/QtNetworkAuth/index.html#module-PySide6.QtNetworkAuth "PySide6.QtNetworkAuth")
Provides support for OAuth-based authorization to online services.
[`Qt NFC`](PySide6/QtNfc/index.html#module-PySide6.QtNfc "PySide6.QtNfc")
Provides access to Near-Field communication (NFC) hardware. On desktop
platforms NDEF access is only supported for Type 4 tags.
[`Qt OpenGL`](PySide6/QtOpenGL/index.html#module-PySide6.QtOpenGL "PySide6.QtOpenGL")
Classes that make it easy to use OpenGL in Qt applications.
[`Qt OpenGL Widgets`](PySide6/QtOpenGLWidgets/index.html#module-PySide6.QtOpenGLWidgets "PySide6.QtOpenGLWidgets")
Provides a widget for rendering OpenGL graphics.
[`Qt Positioning`](PySide6/QtPositioning/index.html#module-PySide6.QtPositioning "PySide6.QtPositioning")
Provides access to position, satellite info and area monitoring classes.
[`Qt PDF`](PySide6/QtPdf/index.html#module-PySide6.QtPdf "PySide6.QtPdf")
Classes and functions for rendering PDF documents on desktop platforms.
[`Qt PDF Widgets`](PySide6/QtPdfWidgets/index.html#module-PySide6.QtPdfWidgets "PySide6.QtPdfWidgets")
A PDF viewer widget.
[`Qt Print Support`](PySide6/QtPrintSupport/index.html#module-PySide6.QtPrintSupport "PySide6.QtPrintSupport")
Classes to make printing easier and more portable.
[`Qt Qml`](PySide6/QtQml/index.html#module-PySide6.QtQml "PySide6.QtQml")
Classes for QML and JavaScript languages.
[`Qt Quick`](PySide6/QtQuick/index.html#module-PySide6.QtQuick "PySide6.QtQuick")
A declarative framework for building highly dynamic applications
with custom UIs.
[`Qt Quick 3D`](PySide6/QtQuick3D/index.html#module-PySide6.QtQuick3D "PySide6.QtQuick3D")
Provides a high-level API for creating 3D content or UIs based on Qt Quick.
[`Qt Quick Controls`](PySide6/QtQuickControls2/index.html#module-PySide6.QtQuickControls2 "PySide6.QtQuickControls2")
Lightweight QML types for creating performant user interfaces for
desktop, embedded, and mobile devices.
[`Qt Quick Test`](PySide6/QtQuickTest/index.html#module-PySide6.QtQuickTest "PySide6.QtQuickTest")
A unit test framework for QML applications where test cases are written as JavaScript functions.
[`Qt Quick Widgets`](PySide6/QtQuickWidgets/index.html#module-PySide6.QtQuickWidgets "PySide6.QtQuickWidgets")
Provides a Python widget class for displaying a Qt Quick user interface.
[`Qt Remote Objects`](PySide6/QtRemoteObjects/index.html#module-PySide6.QtRemoteObjects "PySide6.QtRemoteObjects")
Provides an easy to use mechanism for sharing a QObjectâs API
(Properties/Signals/Slots) between processes or devices.
[`Qt SCXML`](PySide6/QtScxml/index.html#module-PySide6.QtScxml "PySide6.QtScxml")
Provides classes and tools for creating state machines from SCXML files and
embedding them in applications.
[`Qt Sensors`](PySide6/QtSensors/index.html#module-PySide6.QtSensors "PySide6.QtSensors")
Provides access to sensor hardware.
[`Qt Serial Bus`](PySide6/QtSerialBus/index.html#module-PySide6.QtSerialBus "PySide6.QtSerialBus")
Provides access to serial industrial bus interfaces. Currently, the
module supports the CAN bus and Modbus protocols.
[`Qt Serial Port`](PySide6/QtSerialPort/index.html#module-PySide6.QtSerialPort "PySide6.QtSerialPort")
Provides classes to interact with hardware and virtual serial ports.
[`Qt Spatial Audio`](PySide6/QtSpatialAudio/index.html#module-PySide6.QtSpatialAudio "PySide6.QtSpatialAudio")
Provides support for spatial audio. Create sound scenes in 3D space containing
different sound sources and room related properties such as reverb.
[`Qt SQL`](PySide6/QtSql/index.html#module-PySide6.QtSql "PySide6.QtSql")
Classes for database integration using SQL.
[`Qt State Machine`](PySide6/QtStateMachine/index.html#module-PySide6.QtStateMachine "PySide6.QtStateMachine")
Provides classes for creating and executing state graphs.
[`Qt SVG`](PySide6/QtSvg/index.html#module-PySide6.QtSvg "PySide6.QtSvg")
Classes for displaying the contents of SVG files. Supports a subset of the
SVG 1.2 Tiny standard. A separate library (Qt SVG Widgets) provides support
for rendering SVG files in a widget UI.
[`Qt SVG Widgets`](PySide6/QtSvgWidgets/index.html#module-PySide6.QtSvgWidgets "PySide6.QtSvgWidgets")
Provides support for rendering SVG files in a widget UI.
[`Qt Test`](PySide6/QtTest/index.html#module-PySide6.QtTest "PySide6.QtTest")
Provides classes for unit testing Qt applications and libraries.
[`QtTextToSpeech`](PySide6/QtTextToSpeech/index.html#module-PySide6.QtTextToSpeech "PySide6.QtTextToSpeech")
Provides support for synthesizing speech from text and playing it as audio
output.
[`Qt UI Tools`](PySide6/QtUiTools/index.html#module-PySide6.QtUiTools "PySide6.QtUiTools")
Classes for loading QWidget based forms created in *Qt Widgets Designer*
dynamically, at runtime.
[`Qt WebChannel`](PySide6/QtWebChannel/index.html#module-PySide6.QtWebChannel "PySide6.QtWebChannel")
Provides access to QObject or QML objects from HTML clients for
seamless integration of Qt applications with HTML/JavaScript clients.
[`QtWebEngine Core Classes`](PySide6/QtWebEngineCore/index.html#module-PySide6.QtWebEngineCore "PySide6.QtWebEngineCore")
Provides public API shared by both QtWebEngine and QtWebEngineWidgets.
[`QtWebEngine Widgets Classes`](PySide6/QtWebEngineWidgets/index.html#module-PySide6.QtWebEngineWidgets "PySide6.QtWebEngineWidgets")
Provides Python classes for rendering web content in a QWidget based
application.
[`QtWebEngine QML Types`](PySide6/QtWebEngineQuick/index.html#module-PySide6.QtWebEngineQuick "PySide6.QtWebEngineQuick")
Provides QML types for rendering web content within a QML application.
[`Qt WebSockets`](PySide6/QtWebSockets/index.html#module-PySide6.QtWebSockets "PySide6.QtWebSockets")
Provides WebSocket communication compliant with RFC 6455.
[`Qt WebView`](PySide6/QtWebView/index.html#module-PySide6.QtWebView "PySide6.QtWebView")
Displays web content in a QML application by using APIs native to the platform,
without the need to include a full web browser stack.
[`Qt Widgets`](PySide6/QtWidgets/index.html#module-PySide6.QtWidgets "PySide6.QtWidgets")
Classes to extend Qt GUI with Python widgets.
[`Qt XML`](PySide6/QtXml/index.html#module-PySide6.QtXml "PySide6.QtXml")
Handling of XML in a Document Object Model (DOM) API.
[`Qt 3D Animation Classes`](PySide6/Qt3DAnimation/index.html#module-PySide6.Qt3DAnimation "PySide6.Qt3DAnimation")
The Qt 3D Animation modules provides a set of prebuilt elements to
help you get started with Qt 3D.
[`Qt 3D Core Classes`](PySide6/Qt3DCore/index.html#module-PySide6.Qt3DCore "PySide6.Qt3DCore")
The Qt 3D module contains functionality to support near-realtime
simulation systems.
[`Qt 3D Extras Classes`](PySide6/Qt3DExtras/index.html#module-PySide6.Qt3DExtras "PySide6.Qt3DExtras")
Provides a set of prebuilt elements to help you get started with Qt 3D.
[`Qt 3D Input Classes`](PySide6/Qt3DInput/index.html#module-PySide6.Qt3DInput "PySide6.Qt3DInput")
Provides classes for handling user input in
applications using Qt3D.
[`Qt 3D Logic Classes`](PySide6/Qt3DLogic/index.html#module-PySide6.Qt3DLogic "PySide6.Qt3DLogic")
Enables synchronizing frames with the Qt 3D backend.
[`Qt 3D Render Classes`](PySide6/Qt3DRender/index.html#module-PySide6.Qt3DRender "PySide6.Qt3DRender")
Contains functionality to support 2D and 3D rendering using Qt 3D.
[`QtAsyncio`](PySide6/QtAsyncio/index.html#module-PySide6.QtAsyncio "PySide6.QtAsyncio")
Provides integration between asyncio and Qtâs event loop.
[`Qt CoAP`](PySide6/QtCoap/index.html#module-PySide6.QtCoap "PySide6.QtCoap")
Implements the client side of CoAP defined by RFC 7252.
[`Qt OPC UA`](PySide6/QtOpcUa/index.html#module-PySide6.QtOpcUa "PySide6.QtOpcUa")
Protocol for data modeling and exchange of data in industrial applications.
[`Qt MQTT`](PySide6/QtMqtt/index.html#module-PySide6.QtMqtt "PySide6.QtMqtt")
Provides an implementation of the MQTT protocol specification.