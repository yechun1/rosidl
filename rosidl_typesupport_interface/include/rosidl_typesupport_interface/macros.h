// Copyright 2016 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef ROSIDL_TYPESUPPORT_INTERFACE__MACROS_H_
#define ROSIDL_TYPESUPPORT_INTERFACE__MACROS_H_

#define ROSIDL_TYPESUPPORT_INTERFACE__SYMBOL_NAME( \
    typesupport_name, function_name, package_name, interface_type, interface_name) \
  typesupport_name ## __ ## function_name ## __ ## \
  package_name ## __ ## interface_type ## __ ## interface_name

#define ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME( \
    typesupport_name, package_name, interface_type, message_name) \
  ROSIDL_TYPESUPPORT_INTERFACE__SYMBOL_NAME( \
    typesupport_name, get_message_type_support_handle, \
    package_name, interface_type, message_name)

#define ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME( \
    typesupport_name, package_name, service_name) \
  ROSIDL_TYPESUPPORT_INTERFACE__SYMBOL_NAME( \
    typesupport_name, get_service_type_support_handle, \
    package_name, srv, service_name)

#endif  // ROSIDL_TYPESUPPORT_INTERFACE__MACROS_H_
