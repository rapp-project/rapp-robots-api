MACRO(BUILD_LIB LIB_NAME)

    STRING(TOUPPER ${LIB_NAME} LIB_UNAME)

    IF(BUILD_ALL)
        SET(BUILD_IMPL_${LIB_UNAME} "ON")
    ENDIF()

    IF(BUILD_IMPL_${LIB_UNAME})

        MESSAGE(STATUS "Building ${LIB_NAME} lib")

        SET(LIB rapp_robot_${LIB_NAME})

        add_library(${LIB} SHARED
            ${LIB_NAME}.cpp
        )

        target_link_libraries(${LIB}
            ${RAPP_SHARED_NAME}
        )

        install (TARGETS ${LIB} DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/)
        GET_PROPERTY(FULL_LIB_NAME TARGET ${LIB} PROPERTY LOCATION)

        MESSAGE(STATUS ${FULL_LIB_NAME})

        SET(RAPP_SHARED_LIBS ${RAPP_SHARED_LIBS} ${FULL_LIB_NAME} PARENT_SCOPE)

    ENDIF()

ENDMACRO()

BUILD_LIB(vision)
BUILD_LIB(communication)
BUILD_LIB(navigation)
BUILD_LIB(localization)
BUILD_LIB(info)
