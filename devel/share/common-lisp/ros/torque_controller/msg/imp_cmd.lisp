; Auto-generated. Do not edit!


(cl:in-package torque_controller-msg)


;//! \htmlinclude imp_cmd.msg.html

(cl:defclass <imp_cmd> (roslisp-msg-protocol:ros-message)
  ((q_array
    :reader q_array
    :initarg :q_array
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (tau_comp
    :reader tau_comp
    :initarg :tau_comp
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass imp_cmd (<imp_cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <imp_cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'imp_cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name torque_controller-msg:<imp_cmd> is deprecated: use torque_controller-msg:imp_cmd instead.")))

(cl:ensure-generic-function 'q_array-val :lambda-list '(m))
(cl:defmethod q_array-val ((m <imp_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader torque_controller-msg:q_array-val is deprecated.  Use torque_controller-msg:q_array instead.")
  (q_array m))

(cl:ensure-generic-function 'tau_comp-val :lambda-list '(m))
(cl:defmethod tau_comp-val ((m <imp_cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader torque_controller-msg:tau_comp-val is deprecated.  Use torque_controller-msg:tau_comp instead.")
  (tau_comp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <imp_cmd>) ostream)
  "Serializes a message object of type '<imp_cmd>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'q_array))))
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
   (cl:slot-value msg 'q_array))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'tau_comp))))
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
   (cl:slot-value msg 'tau_comp))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <imp_cmd>) istream)
  "Deserializes a message object of type '<imp_cmd>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'q_array) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'q_array)))
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
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'tau_comp) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'tau_comp)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<imp_cmd>)))
  "Returns string type for a message object of type '<imp_cmd>"
  "torque_controller/imp_cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'imp_cmd)))
  "Returns string type for a message object of type 'imp_cmd"
  "torque_controller/imp_cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<imp_cmd>)))
  "Returns md5sum for a message object of type '<imp_cmd>"
  "266a067a7bb3dfe4cf2d32857d1432a8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'imp_cmd)))
  "Returns md5sum for a message object of type 'imp_cmd"
  "266a067a7bb3dfe4cf2d32857d1432a8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<imp_cmd>)))
  "Returns full string definition for message of type '<imp_cmd>"
  (cl:format cl:nil "float64[] q_array~%float64[] tau_comp~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'imp_cmd)))
  "Returns full string definition for message of type 'imp_cmd"
  (cl:format cl:nil "float64[] q_array~%float64[] tau_comp~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <imp_cmd>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'q_array) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'tau_comp) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <imp_cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'imp_cmd
    (cl:cons ':q_array (q_array msg))
    (cl:cons ':tau_comp (tau_comp msg))
))
