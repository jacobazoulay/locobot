
(cl:in-package :asdf)

(defsystem "interbotix_rpi_modules-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "PixelCommands" :depends-on ("_package_PixelCommands"))
    (:file "_package_PixelCommands" :depends-on ("_package"))
  ))