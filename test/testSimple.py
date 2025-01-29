from visca.cameraObject import CameraObject
from visca.dictionary.enumerations import WhiteBalanceModeEnum

camera = CameraObject()
print("set whiteBalanceMode: ", camera.color.setWhiteBalanceMode(WhiteBalanceModeEnum.MANUAL))
print("get whiteBalanceMode: ", camera.color.getWhiteBalanceMode())
print("onePushTrigger: ", camera.color.onePushTrigger())
cmd = camera.color.setLevelUp()
print(f"cmd: {cmd}")