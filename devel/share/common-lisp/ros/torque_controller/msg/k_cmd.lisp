; Auto-generated. Do not edit!


(cl:in-package torque_controller-msg)


;//! \htmlinclude k_cmd.msg.html

(cl:defclass <k_cmd> (roslisp-msg-protocol:ros-message)
  ((k_array
    :reader k_array
    :initarg :k_array
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass k_cmd (<k_cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <k_cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'k_cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name torque_controller-msg:<k_cmd> is deprecated: use torque_controller-msg:k_cmd instead.")))

(cl:ensure-generic-function 'k_array-val :lambda-list '(m))
(cl:defmethod k_array-val ((m <k_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader torque_controller-msg:k_array-val is deprecated.  Use torque_controller-msg:k_array instead.")
  (k_array m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <k_cmd>) ostream)
  "Serializes a message object of type '<k_cmd>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'k_array))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'k_array))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <k_cmd>) istream)
  "Deserializes a message object of type '<k_cmd>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'k_array) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'k_array)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<k_cmd>)))
  "Returns string type for a message object of type '<k_cmd>"
  "torque_controller/k_cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'k_cmd)))
  "Returns string type for a message object of type 'k_cmd"
  "torque_controller/k_cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<k_cmd>)))
  "Returns md5sum for a message object of type '<k_cmd>"
  "97bad9b23c1159dce0e721054b5477af")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'k_cmd)))
  "Returns md5sum for a message object of type 'k_cmd"
  "97bad9b23c1159dce0e721054b5477af")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<k_cmd>)))
  "Returns full string definition for message of type '<k_cmd>"
  (cl:format cl:nil "float64[] k_array~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'k_cmd)))
  "Returns full string definition for message of type 'k_cmd"
  (cl:format cl:nil "float64[] k_array~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <k_cmd>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'k_array) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <k_cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'k_cmd
    (cl:cons ':k_array (k_array msg))
))
