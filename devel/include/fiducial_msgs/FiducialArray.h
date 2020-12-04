// Generated by gencpp from file fiducial_msgs/FiducialArray.msg
// DO NOT EDIT!


#ifndef FIDUCIAL_MSGS_MESSAGE_FIDUCIALARRAY_H
#define FIDUCIAL_MSGS_MESSAGE_FIDUCIALARRAY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <fiducial_msgs/Fiducial.h>

namespace fiducial_msgs
{
template <class ContainerAllocator>
struct FiducialArray_
{
  typedef FiducialArray_<ContainerAllocator> Type;

  FiducialArray_()
    : header()
    , image_seq(0)
    , fiducials()  {
    }
  FiducialArray_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , image_seq(0)
    , fiducials(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _image_seq_type;
  _image_seq_type image_seq;

   typedef std::vector< ::fiducial_msgs::Fiducial_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::fiducial_msgs::Fiducial_<ContainerAllocator> >::other >  _fiducials_type;
  _fiducials_type fiducials;





  typedef boost::shared_ptr< ::fiducial_msgs::FiducialArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fiducial_msgs::FiducialArray_<ContainerAllocator> const> ConstPtr;

}; // struct FiducialArray_

typedef ::fiducial_msgs::FiducialArray_<std::allocator<void> > FiducialArray;

typedef boost::shared_ptr< ::fiducial_msgs::FiducialArray > FiducialArrayPtr;
typedef boost::shared_ptr< ::fiducial_msgs::FiducialArray const> FiducialArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fiducial_msgs::FiducialArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::fiducial_msgs::FiducialArray_<ContainerAllocator1> & lhs, const ::fiducial_msgs::FiducialArray_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.image_seq == rhs.image_seq &&
    lhs.fiducials == rhs.fiducials;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::fiducial_msgs::FiducialArray_<ContainerAllocator1> & lhs, const ::fiducial_msgs::FiducialArray_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace fiducial_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fiducial_msgs::FiducialArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fiducial_msgs::FiducialArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fiducial_msgs::FiducialArray_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fd851a0658e8a35a4d4f80b76d9f17a0";
  }

  static const char* value(const ::fiducial_msgs::FiducialArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfd851a0658e8a35aULL;
  static const uint64_t static_value2 = 0x4d4f80b76d9f17a0ULL;
};

template<class ContainerAllocator>
struct DataType< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fiducial_msgs/FiducialArray";
  }

  static const char* value(const ::fiducial_msgs::FiducialArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return " # A set of fiducial vertex messages\n"
" # to an image\n"
" Header header\n"
" int32 image_seq\n"
" Fiducial[] fiducials \n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: fiducial_msgs/Fiducial\n"
" # Details of a detected fiducial.\n"
"\n"
" int32 fiducial_id\n"
" int32 direction\n"
"\n"
" # vertices\n"
" float64 x0\n"
" float64 y0\n"
" float64 x1\n"
" float64 y1\n"
" float64 x2\n"
" float64 y2\n"
" float64 x3\n"
" float64 y3\n"
;
  }

  static const char* value(const ::fiducial_msgs::FiducialArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.image_seq);
      stream.next(m.fiducials);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FiducialArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fiducial_msgs::FiducialArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fiducial_msgs::FiducialArray_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "image_seq: ";
    Printer<int32_t>::stream(s, indent + "  ", v.image_seq);
    s << indent << "fiducials[]" << std::endl;
    for (size_t i = 0; i < v.fiducials.size(); ++i)
    {
      s << indent << "  fiducials[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::fiducial_msgs::Fiducial_<ContainerAllocator> >::stream(s, indent + "    ", v.fiducials[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // FIDUCIAL_MSGS_MESSAGE_FIDUCIALARRAY_H
