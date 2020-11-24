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

class imp_cmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.q_array = null;
      this.tau_comp = null;
    }
    else {
      if (initObj.hasOwnProperty('q_array')) {
        this.q_array = initObj.q_array
      }
      else {
        this.q_array = [];
      }
      if (initObj.hasOwnProperty('tau_comp')) {
        this.tau_comp = initObj.tau_comp
      }
      else {
        this.tau_comp = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type imp_cmd
    // Serialize message field [q_array]
    bufferOffset = _arraySerializer.float64(obj.q_array, buffer, bufferOffset, null);
    // Serialize message field [tau_comp]
    bufferOffset = _arraySerializer.float64(obj.tau_comp, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type imp_cmd
    let len;
    let data = new imp_cmd(null);
    // Deserialize message field [q_array]
    data.q_array = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [tau_comp]
    data.tau_comp = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.q_array.length;
    length += 8 * object.tau_comp.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'torque_controller/imp_cmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '266a067a7bb3dfe4cf2d32857d1432a8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] q_array
    float64[] tau_comp
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new imp_cmd(null);
    if (msg.q_array !== undefined) {
      resolved.q_array = msg.q_array;
    }
    else {
      resolved.q_array = []
    }

    if (msg.tau_comp !== undefined) {
      resolved.tau_comp = msg.tau_comp;
    }
    else {
      resolved.tau_comp = []
    }

    return resolved;
    }
};

module.exports = imp_cmd;
