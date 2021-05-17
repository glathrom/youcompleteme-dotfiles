cmake_minimum_required(VERSION 3.10)
project(attendance)
set(CMAKE_CXX_STANDARD 20)

# setting paths for libraries and executable outputs
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin) 

# setting path to include files 
include_directories( 
    ${CMAKE_SOURCE_DIR}/include 
    ${HOME}/.local/include/opencv4
) 

find_package(OpenCV)
MESSAGE(STATUS "Include dirs ${OpenCV_INCLUDE_DIRS}")
MESSAGE(STATUS "Link Libraries ${OpenCV_LIBS}")

################################################################
# generate a shared library from src file
################################################################

#add_library(mnist SHARED ${CMAKE_SOURCE_DIR}/mnist.cpp)

################################################################
# compling the program from the library just created
################################################################


set(SOURCES ${CMAKE_SOURCE_DIR}/src/display.cpp)
add_executable(mydisplay ${SOURCES})
target_link_libraries(mydisplay PRIVATE opencv_imgcodecs opencv_core opencv_highgui)


set(SOURCES ${CMAKE_SOURCE_DIR}/src/basics.cpp)
add_executable(basics ${SOURCES})
target_link_libraries(basics PRIVATE opencv_imgcodecs opencv_core opencv_highgui opencv_imgproc)

set(SOURCES ${CMAKE_SOURCE_DIR}/src/face.cpp)
add_executable(faces ${SOURCES})
target_link_libraries(faces PRIVATE opencv_imgcodecs opencv_core opencv_highgui opencv_imgproc opencv_objdetect)
