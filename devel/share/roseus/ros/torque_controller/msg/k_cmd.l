;; Auto-generated. Do not edit!


(when (boundp 'torque_controller::k_cmd)
  (if (not (find-package "TORQUE_CONTROLLER"))
    (make-package "TORQUE_CONTROLLER"))
  (shadow 'k_cmd (find-package "TORQUE_CONTROLLER")))
(unless (find-package "TORQUE_CONTROLLER::K_CMD")
  (make-package "TORQUE_CONTROLLER::K_CMD"))

(in-package "ROS")
;;//! \htmlinclude k_cmd.msg.html


(defclass torque_controller::k_cmd
  :super ros::object
  :slots (_k_array ))

(defmethod torque_controller::k_cmd
  (:init
   (&key
    ((:k_array __k_array) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _k_array __k_array)
   self)
  (:k_array
   (&optional __k_array)
   (if __k_array (setq _k_array __k_array)) _k_array)
  (:serialization-length
   ()
   (+
    ;; float64[] _k_array
    (* 8    (length _k_array)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _k_array
     (write-long (length _k_array) s)
     (dotimes (i (length _k_array))
       (sys::poke (elt _k_array i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _k_array
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _k_array (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _k_array i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get torque_controller::k_cmd :md5sum-) "97bad9b23c1159dce0e721054b5477af")
(setf (get torque_controller::k_cmd :datatype-) "torque_controller/k_cmd")
(setf (get torque_controller::k_cmd :definition-)
      "float64[] k_array
")



(provide :torque_controller/k_cmd "97bad9b23c1159dce0e721054b5477af")


