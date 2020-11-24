;; Auto-generated. Do not edit!


(when (boundp 'torque_controller::imp_cmd)
  (if (not (find-package "TORQUE_CONTROLLER"))
    (make-package "TORQUE_CONTROLLER"))
  (shadow 'imp_cmd (find-package "TORQUE_CONTROLLER")))
(unless (find-package "TORQUE_CONTROLLER::IMP_CMD")
  (make-package "TORQUE_CONTROLLER::IMP_CMD"))

(in-package "ROS")
;;//! \htmlinclude imp_cmd.msg.html


(defclass torque_controller::imp_cmd
  :super ros::object
  :slots (_q_array _tau_comp ))

(defmethod torque_controller::imp_cmd
  (:init
   (&key
    ((:q_array __q_array) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:tau_comp __tau_comp) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _q_array __q_array)
   (setq _tau_comp __tau_comp)
   self)
  (:q_array
   (&optional __q_array)
   (if __q_array (setq _q_array __q_array)) _q_array)
  (:tau_comp
   (&optional __tau_comp)
   (if __tau_comp (setq _tau_comp __tau_comp)) _tau_comp)
  (:serialization-length
   ()
   (+
    ;; float64[] _q_array
    (* 8    (length _q_array)) 4
    ;; float64[] _tau_comp
    (* 8    (length _tau_comp)) 4
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
     ;; float64[] _tau_comp
     (write-long (length _tau_comp) s)
     (dotimes (i (length _tau_comp))
       (sys::poke (elt _tau_comp i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
   ;; float64[] _tau_comp
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _tau_comp (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _tau_comp i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get torque_controller::imp_cmd :md5sum-) "266a067a7bb3dfe4cf2d32857d1432a8")
(setf (get torque_controller::imp_cmd :datatype-) "torque_controller/imp_cmd")
(setf (get torque_controller::imp_cmd :definition-)
      "float64[] q_array
float64[] tau_comp
")



(provide :torque_controller/imp_cmd "266a067a7bb3dfe4cf2d32857d1432a8")


