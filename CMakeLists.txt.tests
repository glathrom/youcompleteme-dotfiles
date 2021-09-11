cmake_minimum_required(VERSION 3.16)
project(hmm)
set(CMAKE_CXX_STANDARD 17)


################################
# setting path to include files 
################################

include_directories( 
    ../include 
) 

link_directories(
    ../lib
)

set(CMAKE_PREFIX_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../src)
find_package(model REQUIRED)
message(STATUS "model_DIR = ${model_DIR}")

find_package(alpha REQUIRED) 
message(STATUS "alpha_DIR = ${alpha_DIR}")

find_package(beta REQUIRED)
message(STATUS "beta_DIR = ${beta_DIR}")

find_package(learn REQUIRED)
message(STATUS "learn_DIR = ${learn_DIR}")

######################
# target executable
######################

add_executable(test_model test_model.cpp)
target_link_libraries(test_model model)

add_executable(test_alpha test_alpha_pass.cpp)
target_link_libraries(test_alpha model alpha)

add_executable(test_beta test_beta_pass.cpp)
target_link_libraries(test_beta model beta)

add_executable(test_learn test_learning.cpp)
target_link_libraries(test_learn model learn)
