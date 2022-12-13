/***************************************************************************//**
 * @file
 * @brief Kernel Flag Example
 *******************************************************************************
 * # License
 * <b>Copyright 2018 Silicon Laboratories Inc. www.silabs.com</b>
 *******************************************************************************
 *
 * The licensor of this software is Silicon Laboratories Inc.  Your use of this
 * software is governed by the terms of Silicon Labs Master Software License
 * Agreement (MSLA) available at
 * www.silabs.com/about-us/legal/master-software-license-agreement.  This
 * software is distributed to you in Source Code format and is governed by the
 * sections of the MSLA applicable to Source Code.
 *
 ******************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                               MODULE
 ********************************************************************************************************
 *******************************************************************************************************/

#ifndef  _EX_KERNEL_FLAG_H_
#define  _EX_KERNEL_FLAG_H_

/********************************************************************************************************
 ********************************************************************************************************
 *                                            INCLUDE FILES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                               DEFINES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                             DATA TYPES
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                         FUNCTION PROTOTYPES
 ********************************************************************************************************
 *******************************************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

void Ex_KernelFlag(void);
void Ex_KernelFlagPendAbort(void);

#ifdef __cplusplus
}
#endif

/********************************************************************************************************
 ********************************************************************************************************
 *                                        CONFIGURATION ERRORS
 ********************************************************************************************************
 *******************************************************************************************************/

/********************************************************************************************************
 ********************************************************************************************************
 *                                             MODULE END
 ********************************************************************************************************
 *******************************************************************************************************/

#endif
