// Auto-generated. Do not edit!

// (in-package torque_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class k_cmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.k_array = null;
    }
    else {
      if (initObj.hasOwnProperty('k_array')) {
        this.k_array = initObj.k_array
      }
      else {
        this.k_array = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type k_cmd
    // Serialize message field [k_array]
    bufferOffset = _arraySerializer.float64(obj.k_array, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type k_cmd
    let len;
    let data = new k_cmd(null);
    // Deserialize message field [k_array]
    data.k_array = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.k_array.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'torque_controller/k_cmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '97bad9b23c1159dce0e721054b5477af';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] k_array
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new k_cmd(null);
    if (msg.k_array !== undefined) {
      resolved.k_array = msg.k_array;
    }
    else {
      resolved.k_array = []
    }

    return resolved;
    }
};

module.exports = k_cmd;
