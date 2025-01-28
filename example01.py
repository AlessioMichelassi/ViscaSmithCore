from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication

from visca import CameraObject
from visca import ClientObject
from visca import ExposureModeEnum

if __name__ == '__main__':
    app = QApplication([])

    camera = CameraObject()
    client = ClientObject(camera)
    client.connectToServer("127.0.0.1", 52381)

    # Collegamento ai segnali per debug
    client.error_SIGNAL.connect(print)
    client.info_SIGNAL.connect(print)
    client.serverMessage.connect(print)

    # Messaggi da inviare
    exposure_message = camera.exposure.setExposureMode(ExposureModeEnum.MANUAL)
    QTimer.singleShot(1000, lambda: client.enqueueViscaString(exposure_message))

    message = camera.exposure.getExposureMode()
    QTimer.singleShot(2000, lambda: client.enqueueViscaString(message))
    app.exec()
