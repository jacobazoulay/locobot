; Auto-generated. Do not edit!


(cl:in-package interbotix_rpi_modules-msg)


;//! \htmlinclude PixelCommands.msg.html

(cl:defclass <PixelCommands> (roslisp-msg-protocol:ros-message)
  ((cmd_type
    :reader cmd_type
    :initarg :cmd_type
    :type cl:string
    :initform "")
   (set_all_leds
    :reader set_all_leds
    :initarg :set_all_leds
    :type cl:boolean
    :initform cl:nil)
   (pixel
    :reader pixel
    :initarg :pixel
    :type cl:fixnum
    :initform 0)
   (color
    :reader color
    :initarg :color
    :type cl:integer
    :initform 0)
   (brightness
    :reader brightness
    :initarg :brightness
    :type cl:fixnum
    :initform 0)
   (period
    :reader period
    :initarg :period
    :type cl:integer
    :initform 0)
   (iterations
    :reader iterations
    :initarg :iterations
    :type cl:fixnum
    :initform 0))
)

(cl:defclass PixelCommands (<PixelCommands>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PixelCommands>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PixelCommands)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name interbotix_rpi_modules-msg:<PixelCommands> is deprecated: use interbotix_rpi_modules-msg:PixelCommands instead.")))

(cl:ensure-generic-function 'cmd_type-val :lambda-list '(m))
(cl:defmethod cmd_type-val ((m <PixelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interbotix_rpi_modules-msg:cmd_type-val is deprecated.  Use interbotix_rpi_modules-msg:cmd_type instead.")
  (cmd_type m))

(cl:ensure-generic-function 'set_all_leds-val :lambda-list '(m))
(cl:defmethod set_all_leds-val ((m <PixelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interbotix_rpi_modules-msg:set_all_leds-val is deprecated.  Use interbotix_rpi_modules-msg:set_all_leds instead.")
  (set_all_leds m))

(cl:ensure-generic-function 'pixel-val :lambda-list '(m))
(cl:defmethod pixel-val ((m <PixelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interbotix_rpi_modules-msg:pixel-val is deprecated.  Use interbotix_rpi_modules-msg:pixel instead.")
  (pixel m))

(cl:ensure-generic-function 'color-val :lambda-list '(m))
(cl:defmethod color-val ((m <PixelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interbotix_rpi_modules-msg:color-val is deprecated.  Use interbotix_rpi_modules-msg:color instead.")
  (color m))

(cl:ensure-generic-function 'brightness-val :lambda-list '(m))
(cl:defmethod brightness-val ((m <PixelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interbotix_rpi_modules-msg:brightness-val is deprecated.  Use interbotix_rpi_modules-msg:brightness instead.")
  (brightness m))

(cl:ensure-generic-function 'period-val :lambda-list '(m))
(cl:defmethod period-val ((m <PixelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interbotix_rpi_modules-msg:period-val is deprecated.  Use interbotix_rpi_modules-msg:period instead.")
  (period m))

(cl:ensure-generic-function 'iterations-val :lambda-list '(m))
(cl:defmethod iterations-val ((m <PixelCommands>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader interbotix_rpi_modules-msg:iterations-val is deprecated.  Use interbotix_rpi_modules-msg:iterations instead.")
  (iterations m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PixelCommands>) ostream)
  "Serializes a message object of type '<PixelCommands>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'cmd_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'cmd_type))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'set_all_leds) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pixel)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'color)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'color)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'color)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'color)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brightness)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'period)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'period)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'period)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'period)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'iterations)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PixelCommands>) istream)
  "Deserializes a message object of type '<PixelCommands>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cmd_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'cmd_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'set_all_leds) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'pixel)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'color)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'color)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'color)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'color)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'brightness)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'period)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'period)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'period)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'period)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'iterations)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PixelCommands>)))
  "Returns string type for a message object of type '<PixelCommands>"
  "interbotix_rpi_modules/PixelCommands")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PixelCommands)))
  "Returns string type for a message object of type 'PixelCommands"
  "interbotix_rpi_modules/PixelCommands")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PixelCommands>)))
  "Returns md5sum for a message object of type '<PixelCommands>"
  "3c3edd3691d72aef2f0cabd73f60138d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PixelCommands)))
  "Returns md5sum for a message object of type 'PixelCommands"
  "3c3edd3691d72aef2f0cabd73f60138d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PixelCommands>)))
  "Returns full string definition for message of type '<PixelCommands>"
  (cl:format cl:nil "# This message is used specifically in the interbotix_rpi_modules package~%#~%# Configure NeoPixel Leds on a Raspberry Pi~%~%string cmd_type       # Either 'pulse', 'blink', 'brightness', or 'color'.~%                      # Note that the 'pulse' and 'brightness' options will~%                      # affect all Leds even if 'set_all_leds' is set to False.~%bool set_all_leds     # Set to True to configure all LEDs~%uint8 pixel           # Index of NeoPixel to change (only considered if 'set_all_leds' is false)~%uint32 color			    # Value indicates Color to be used (HEX - RGB)~%uint8 brightness      # Value indicates LED brightness level (0-255)~%uint32 period			    # time delay for blink or pulse (milliseconds)~%uint8 iterations		  # iterations = number of iterations for blink or pulse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PixelCommands)))
  "Returns full string definition for message of type 'PixelCommands"
  (cl:format cl:nil "# This message is used specifically in the interbotix_rpi_modules package~%#~%# Configure NeoPixel Leds on a Raspberry Pi~%~%string cmd_type       # Either 'pulse', 'blink', 'brightness', or 'color'.~%                      # Note that the 'pulse' and 'brightness' options will~%                      # affect all Leds even if 'set_all_leds' is set to False.~%bool set_all_leds     # Set to True to configure all LEDs~%uint8 pixel           # Index of NeoPixel to change (only considered if 'set_all_leds' is false)~%uint32 color			    # Value indicates Color to be used (HEX - RGB)~%uint8 brightness      # Value indicates LED brightness level (0-255)~%uint32 period			    # time delay for blink or pulse (milliseconds)~%uint8 iterations		  # iterations = number of iterations for blink or pulse~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PixelCommands>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'cmd_type))
     1
     1
     4
     1
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PixelCommands>))
  "Converts a ROS message object to a list"
  (cl:list 'PixelCommands
    (cl:cons ':cmd_type (cmd_type msg))
    (cl:cons ':set_all_leds (set_all_leds msg))
    (cl:cons ':pixel (pixel msg))
    (cl:cons ':color (color msg))
    (cl:cons ':brightness (brightness msg))
    (cl:cons ':period (period msg))
    (cl:cons ':iterations (iterations msg))
))
