
(cl:in-package :asdf)

(defsystem "torque_controller-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "imp_cmd" :depends-on ("_package_imp_cmd"))
    (:file "_package_imp_cmd" :depends-on ("_package"))
    (:file "imp_cmd" :depends-on ("_package_imp_cmd"))
    (:file "_package_imp_cmd" :depends-on ("_package"))
    (:file "k_cmd" :depends-on ("_package_k_cmd"))
    (:file "_package_k_cmd" :depends-on ("_package"))
    (:file "k_cmd" :depends-on ("_package_k_cmd"))
    (:file "_package_k_cmd" :depends-on ("_package"))
    (:file "q_cmd" :depends-on ("_package_q_cmd"))
    (:file "_package_q_cmd" :depends-on ("_package"))
    (:file "q_cmd" :depends-on ("_package_q_cmd"))
    (:file "_package_q_cmd" :depends-on ("_package"))
  ))