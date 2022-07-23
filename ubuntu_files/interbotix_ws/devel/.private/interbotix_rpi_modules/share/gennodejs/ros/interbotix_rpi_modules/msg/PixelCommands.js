// Auto-generated. Do not edit!

// (in-package interbotix_rpi_modules.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class PixelCommands {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cmd_type = null;
      this.set_all_leds = null;
      this.pixel = null;
      this.color = null;
      this.brightness = null;
      this.period = null;
      this.iterations = null;
    }
    else {
      if (initObj.hasOwnProperty('cmd_type')) {
        this.cmd_type = initObj.cmd_type
      }
      else {
        this.cmd_type = '';
      }
      if (initObj.hasOwnProperty('set_all_leds')) {
        this.set_all_leds = initObj.set_all_leds
      }
      else {
        this.set_all_leds = false;
      }
      if (initObj.hasOwnProperty('pixel')) {
        this.pixel = initObj.pixel
      }
      else {
        this.pixel = 0;
      }
      if (initObj.hasOwnProperty('color')) {
        this.color = initObj.color
      }
      else {
        this.color = 0;
      }
      if (initObj.hasOwnProperty('brightness')) {
        this.brightness = initObj.brightness
      }
      else {
        this.brightness = 0;
      }
      if (initObj.hasOwnProperty('period')) {
        this.period = initObj.period
      }
      else {
        this.period = 0;
      }
      if (initObj.hasOwnProperty('iterations')) {
        this.iterations = initObj.iterations
      }
      else {
        this.iterations = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PixelCommands
    // Serialize message field [cmd_type]
    bufferOffset = _serializer.string(obj.cmd_type, buffer, bufferOffset);
    // Serialize message field [set_all_leds]
    bufferOffset = _serializer.bool(obj.set_all_leds, buffer, bufferOffset);
    // Serialize message field [pixel]
    bufferOffset = _serializer.uint8(obj.pixel, buffer, bufferOffset);
    // Serialize message field [color]
    bufferOffset = _serializer.uint32(obj.color, buffer, bufferOffset);
    // Serialize message field [brightness]
    bufferOffset = _serializer.uint8(obj.brightness, buffer, bufferOffset);
    // Serialize message field [period]
    bufferOffset = _serializer.uint32(obj.period, buffer, bufferOffset);
    // Serialize message field [iterations]
    bufferOffset = _serializer.uint8(obj.iterations, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PixelCommands
    let len;
    let data = new PixelCommands(null);
    // Deserialize message field [cmd_type]
    data.cmd_type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [set_all_leds]
    data.set_all_leds = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [pixel]
    data.pixel = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [color]
    data.color = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [brightness]
    data.brightness = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [period]
    data.period = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [iterations]
    data.iterations = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.cmd_type);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'interbotix_rpi_modules/PixelCommands';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3c3edd3691d72aef2f0cabd73f60138d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # This message is used specifically in the interbotix_rpi_modules package
    #
    # Configure NeoPixel Leds on a Raspberry Pi
    
    string cmd_type       # Either 'pulse', 'blink', 'brightness', or 'color'.
                          # Note that the 'pulse' and 'brightness' options will
                          # affect all Leds even if 'set_all_leds' is set to False.
    bool set_all_leds     # Set to True to configure all LEDs
    uint8 pixel           # Index of NeoPixel to change (only considered if 'set_all_leds' is false)
    uint32 color			    # Value indicates Color to be used (HEX - RGB)
    uint8 brightness      # Value indicates LED brightness level (0-255)
    uint32 period			    # time delay for blink or pulse (milliseconds)
    uint8 iterations		  # iterations = number of iterations for blink or pulse
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PixelCommands(null);
    if (msg.cmd_type !== undefined) {
      resolved.cmd_type = msg.cmd_type;
    }
    else {
      resolved.cmd_type = ''
    }

    if (msg.set_all_leds !== undefined) {
      resolved.set_all_leds = msg.set_all_leds;
    }
    else {
      resolved.set_all_leds = false
    }

    if (msg.pixel !== undefined) {
      resolved.pixel = msg.pixel;
    }
    else {
      resolved.pixel = 0
    }

    if (msg.color !== undefined) {
      resolved.color = msg.color;
    }
    else {
      resolved.color = 0
    }

    if (msg.brightness !== undefined) {
      resolved.brightness = msg.brightness;
    }
    else {
      resolved.brightness = 0
    }

    if (msg.period !== undefined) {
      resolved.period = msg.period;
    }
    else {
      resolved.period = 0
    }

    if (msg.iterations !== undefined) {
      resolved.iterations = msg.iterations;
    }
    else {
      resolved.iterations = 0
    }

    return resolved;
    }
};

module.exports = PixelCommands;
