/***************************************************************************//**
 * @file
 * @brief
 *******************************************************************************
 * # License
 * <b>Copyright 2018 Silicon Laboratories Inc. www.silabs.com</b>
 *******************************************************************************
 *
 * The licensor of this software is Silicon Laboratories Inc. Your use of this
 * software is governed by the terms of Silicon Labs Master Software License
 * Agreement (MSLA) available at
 * www.silabs.com/about-us/legal/master-software-license-agreement. This
 * software is distributed to you in Source Code format and is governed by the
 * sections of the MSLA applicable to Source Code.
 *
 ******************************************************************************/

#if defined(__cplusplus)
extern "C" {
#endif

#if defined(WIN32) && !defined(strnlen)
size_t strnlen(const char* s, size_t maxlen);
#endif

// OS indepedent API to generate a cryptographic random number.
int platformRandomDataFunction(unsigned char* buffer, unsigned long size);

#if defined(__cplusplus)
}
#endif
