cmake_minimum_required(VERSION 3.10)
project(mnist)
set(CMAKE_CXX_STANDARD 11)

# setting paths for libraries and executable outputs
set(CMAKE_SOURCE_DIR ${CMAKE_BINARY_DIR}/src)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin) 

# setting path to include files 
include_directories(${CMAKE_BINARY_DIR}/include) 

################################################################
# generate a shared library from src file
################################################################

add_library(mnist SHARED ${CMAKE_SOURCE_DIR}/mnist.cpp)

################################################################
# compling the testing program from the library just created
################################################################

link_directories(${CMAKE_BINARY_DIR}/lib)

set(SOURCES ${CMAKE_SOURCE_DIR}/load.cpp)
add_executable(myload ${SOURCES})
target_link_libraries(myload libmnist.so)
