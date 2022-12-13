/***************************************************************************//**
 * @file
 * @brief Coulomb Counter examples functions
 *******************************************************************************
 * # License
 * <b>Copyright 2021 Silicon Laboratories Inc. www.silabs.com</b>
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

#ifndef COULOMB_APP_H
#define COULOMB_APP_H

/***************************************************************************//**
 * Initialize Coulomb Counter example
 ******************************************************************************/
void coulomb_app_init(void);

/***************************************************************************//**
 * Coulomb Counter ticking function
 ******************************************************************************/
void coulomb_app_process_action(void);

#endif  // COULOMB_APP_H
