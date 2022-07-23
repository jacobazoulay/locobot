;; Auto-generated. Do not edit!


(when (boundp 'interbotix_rpi_modules::PixelCommands)
  (if (not (find-package "INTERBOTIX_RPI_MODULES"))
    (make-package "INTERBOTIX_RPI_MODULES"))
  (shadow 'PixelCommands (find-package "INTERBOTIX_RPI_MODULES")))
(unless (find-package "INTERBOTIX_RPI_MODULES::PIXELCOMMANDS")
  (make-package "INTERBOTIX_RPI_MODULES::PIXELCOMMANDS"))

(in-package "ROS")
;;//! \htmlinclude PixelCommands.msg.html


(defclass interbotix_rpi_modules::PixelCommands
  :super ros::object
  :slots (_cmd_type _set_all_leds _pixel _color _brightness _period _iterations ))

(defmethod interbotix_rpi_modules::PixelCommands
  (:init
   (&key
    ((:cmd_type __cmd_type) "")
    ((:set_all_leds __set_all_leds) nil)
    ((:pixel __pixel) 0)
    ((:color __color) 0)
    ((:brightness __brightness) 0)
    ((:period __period) 0)
    ((:iterations __iterations) 0)
    )
   (send-super :init)
   (setq _cmd_type (string __cmd_type))
   (setq _set_all_leds __set_all_leds)
   (setq _pixel (round __pixel))
   (setq _color (round __color))
   (setq _brightness (round __brightness))
   (setq _period (round __period))
   (setq _iterations (round __iterations))
   self)
  (:cmd_type
   (&optional __cmd_type)
   (if __cmd_type (setq _cmd_type __cmd_type)) _cmd_type)
  (:set_all_leds
   (&optional (__set_all_leds :null))
   (if (not (eq __set_all_leds :null)) (setq _set_all_leds __set_all_leds)) _set_all_leds)
  (:pixel
   (&optional __pixel)
   (if __pixel (setq _pixel __pixel)) _pixel)
  (:color
   (&optional __color)
   (if __color (setq _color __color)) _color)
  (:brightness
   (&optional __brightness)
   (if __brightness (setq _brightness __brightness)) _brightness)
  (:period
   (&optional __period)
   (if __period (setq _period __period)) _period)
  (:iterations
   (&optional __iterations)
   (if __iterations (setq _iterations __iterations)) _iterations)
  (:serialization-length
   ()
   (+
    ;; string _cmd_type
    4 (length _cmd_type)
    ;; bool _set_all_leds
    1
    ;; uint8 _pixel
    1
    ;; uint32 _color
    4
    ;; uint8 _brightness
    1
    ;; uint32 _period
    4
    ;; uint8 _iterations
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _cmd_type
       (write-long (length _cmd_type) s) (princ _cmd_type s)
     ;; bool _set_all_leds
       (if _set_all_leds (write-byte -1 s) (write-byte 0 s))
     ;; uint8 _pixel
       (write-byte _pixel s)
     ;; uint32 _color
       (write-long _color s)
     ;; uint8 _brightness
       (write-byte _brightness s)
     ;; uint32 _period
       (write-long _period s)
     ;; uint8 _iterations
       (write-byte _iterations s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _cmd_type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _cmd_type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _set_all_leds
     (setq _set_all_leds (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; uint8 _pixel
     (setq _pixel (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint32 _color
     (setq _color (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8 _brightness
     (setq _brightness (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint32 _period
     (setq _period (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8 _iterations
     (setq _iterations (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get interbotix_rpi_modules::PixelCommands :md5sum-) "3c3edd3691d72aef2f0cabd73f60138d")
(setf (get interbotix_rpi_modules::PixelCommands :datatype-) "interbotix_rpi_modules/PixelCommands")
(setf (get interbotix_rpi_modules::PixelCommands :definition-)
      "# This message is used specifically in the interbotix_rpi_modules package
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

")



(provide :interbotix_rpi_modules/PixelCommands "3c3edd3691d72aef2f0cabd73f60138d")


