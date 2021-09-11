cmake_minimum_required(VERSION 3.16)
project(hmm)
set(CMAKE_CXX_STANDARD 17)


################################
# setting path to include files 
################################

include_directories( 
    ${CMAKE_CURRENT_SOURCE_DIR}/../include 
) 

######################
# compiled libraries
######################

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../lib)

message(STATUS "${CMAKE_SOURCE_DIR}")
message(STATUS "${CMAKE_CURRENT_SOURCE_DIR}")

add_library(model STATIC model.cpp)
add_library(alpha SHARED alpha.cpp)
add_library(beta  SHARED beta.cpp)
add_library(learn SHARED learning.cpp)

export(TARGETS model NAMESPACE model:: FILE ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modelConfig.cmake)
export(TARGETS alpha NAMESPACE model:: FILE ${CMAKE_CURRENT_SOURCE_DIR}/cmake/alphaConfig.cmake)
export(TARGETS beta  NAMESPACE model:: FILE ${CMAKE_CURRENT_SOURCE_DIR}/cmake/betaConfig.cmake)
export(TARGETS learn NAMESPACE model:: FILE ${CMAKE_CURRENT_SOURCE_DIR}/cmake/learnConfig.cmake)
