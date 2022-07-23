
"use strict";

let GripperMove = require('./GripperMove.js')
let SetToolModbus = require('./SetToolModbus.js')
let GetErr = require('./GetErr.js')
let SetLoad = require('./SetLoad.js')
let ClearErr = require('./ClearErr.js')
let SetAxis = require('./SetAxis.js')
let GripperState = require('./GripperState.js')
let GetDigitalIO = require('./GetDigitalIO.js')
let Move = require('./Move.js')
let SetDigitalIO = require('./SetDigitalIO.js')
let SetInt16 = require('./SetInt16.js')
let TCPOffset = require('./TCPOffset.js')
let ConfigToolModbus = require('./ConfigToolModbus.js')
let GripperConfig = require('./GripperConfig.js')
let GetControllerDigitalIO = require('./GetControllerDigitalIO.js')
let GetAnalogIO = require('./GetAnalogIO.js')

module.exports = {
  GripperMove: GripperMove,
  SetToolModbus: SetToolModbus,
  GetErr: GetErr,
  SetLoad: SetLoad,
  ClearErr: ClearErr,
  SetAxis: SetAxis,
  GripperState: GripperState,
  GetDigitalIO: GetDigitalIO,
  Move: Move,
  SetDigitalIO: SetDigitalIO,
  SetInt16: SetInt16,
  TCPOffset: TCPOffset,
  ConfigToolModbus: ConfigToolModbus,
  GripperConfig: GripperConfig,
  GetControllerDigitalIO: GetControllerDigitalIO,
  GetAnalogIO: GetAnalogIO,
};
