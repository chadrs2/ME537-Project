;; Auto-generated. Do not edit!


(when (boundp 'torque_controller::q_cmd)
  (if (not (find-package "TORQUE_CONTROLLER"))
    (make-package "TORQUE_CONTROLLER"))
  (shadow 'q_cmd (find-package "TORQUE_CONTROLLER")))
(unless (find-package "TORQUE_CONTROLLER::Q_CMD")
  (make-package "TORQUE_CONTROLLER::Q_CMD"))

(in-package "ROS")
;;//! \htmlinclude q_cmd.msg.html


(defclass torque_controller::q_cmd
  :super ros::object
  :slots (_q_array ))

(defmethod torque_controller::q_cmd
  (:init
   (&key
    ((:q_array __q_array) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _q_array __q_array)
   self)
  (:q_array
   (&optional __q_array)
   (if __q_array (setq _q_array __q_array)) _q_array)
  (:serialization-length
   ()
   (+
    ;; float64[] _q_array
    (* 8    (length _q_array)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _q_array
     (write-long (length _q_array) s)
     (dotimes (i (length _q_array))
       (sys::poke (elt _q_array i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _q_array
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _q_array (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _q_array i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get torque_controller::q_cmd :md5sum-) "cc698571bcbd99704d5af623bbfb7675")
(setf (get torque_controller::q_cmd :datatype-) "torque_controller/q_cmd")
(setf (get torque_controller::q_cmd :definition-)
      "float64[] q_array
")



(provide :torque_controller/q_cmd "cc698571bcbd99704d5af623bbfb7675")


