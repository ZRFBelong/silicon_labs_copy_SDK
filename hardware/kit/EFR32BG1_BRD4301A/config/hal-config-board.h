#ifndef HAL_CONFIG_BOARD_H
#define HAL_CONFIG_BOARD_H

#include "em_device.h"
#include "hal-config-types.h"

// This file is auto-generated by Hardware Configurator in Simplicity Studio.
// Any content between $[ and ]$ will be replaced whenever the file is regenerated.
// Content outside these regions will be preserved.

// $[ACMP0]
// [ACMP0]$

// $[ACMP1]
// [ACMP1]$

// $[ADC0]
// [ADC0]$

// $[ANTDIV]
// [ANTDIV]$

// $[BATTERYMON]
// [BATTERYMON]$

// $[BTL_BUTTON]

#define BSP_BTL_BUTTON_PIN                   (14U)
#define BSP_BTL_BUTTON_PORT                  (gpioPortD)

// [BTL_BUTTON]$

// $[BULBPWM]
// [BULBPWM]$

// $[BULBPWM_COLOR]
// [BULBPWM_COLOR]$

// $[BUTTON]
#define BSP_BUTTON_PRESENT                   (1)

#define BSP_BUTTON0_PIN                      (14U)
#define BSP_BUTTON0_PORT                     (gpioPortD)

#define BSP_BUTTON1_PIN                      (15U)
#define BSP_BUTTON1_PORT                     (gpioPortD)

#define BSP_BUTTON_COUNT                     (2U)
#define BSP_BUTTON_INIT                      { { BSP_BUTTON0_PORT, BSP_BUTTON0_PIN }, { BSP_BUTTON1_PORT, BSP_BUTTON1_PIN } }
#define BSP_BUTTON_GPIO_DOUT                 (HAL_GPIO_DOUT_LOW)
#define BSP_BUTTON_GPIO_MODE                 (HAL_GPIO_MODE_INPUT)
// [BUTTON]$

// $[CMU]
#define BSP_CLK_HFXO_PRESENT                 (1)
#define BSP_CLK_HFXO_FREQ                    (38400000UL)
#define BSP_CLK_HFXO_INIT                     CMU_HFXOINIT_DEFAULT
#define BSP_CLK_HFXO_CTUNE                   (322)
#define BSP_CLK_LFXO_PRESENT                 (1)
#define BSP_CLK_LFXO_INIT                     CMU_LFXOINIT_DEFAULT
#define BSP_CLK_LFXO_FREQ                    (32768U)
#define BSP_CLK_LFXO_CTUNE                   (32U)
// [CMU]$

// $[COEX]
// [COEX]$

// $[CS5463]
// [CS5463]$

// $[DCDC]
#define BSP_DCDC_PRESENT                     (1)

#define BSP_DCDC_INIT                         EMU_DCDCINIT_DEFAULT
// [DCDC]$

// $[EMU]
// [EMU]$

// $[EXTFLASH]
#define BSP_EXTFLASH_CS_PIN                  (13U)
#define BSP_EXTFLASH_CS_PORT                 (gpioPortD)

#define BSP_EXTFLASH_INTERNAL                (0)
#define BSP_EXTFLASH_USART                   (HAL_SPI_PORT_USART1)
#define BSP_EXTFLASH_MOSI_PIN                (11U)
#define BSP_EXTFLASH_MOSI_PORT               (gpioPortB)
#define BSP_EXTFLASH_MOSI_LOC                (6U)

#define BSP_EXTFLASH_MISO_PIN                (12U)
#define BSP_EXTFLASH_MISO_PORT               (gpioPortB)
#define BSP_EXTFLASH_MISO_LOC                (6U)

#define BSP_EXTFLASH_CLK_PIN                 (13U)
#define BSP_EXTFLASH_CLK_PORT                (gpioPortB)
#define BSP_EXTFLASH_CLK_LOC                 (6U)

// [EXTFLASH]$

// $[EZRADIOPRO]
// [EZRADIOPRO]$

// $[FEM]
// [FEM]$

// $[GPIO]
#define PORTIO_GPIO_SWV_PIN                  (2U)
#define PORTIO_GPIO_SWV_PORT                 (gpioPortF)
#define PORTIO_GPIO_SWV_LOC                  (0U)

#define BSP_TRACE_SWO_PIN                    (2U)
#define BSP_TRACE_SWO_PORT                   (gpioPortF)
#define BSP_TRACE_SWO_LOC                    (0U)

// [GPIO]$

// $[I2C0]
#define PORTIO_I2C0_SCL_PIN                  (11U)
#define PORTIO_I2C0_SCL_PORT                 (gpioPortC)
#define PORTIO_I2C0_SCL_LOC                  (15U)

#define PORTIO_I2C0_SDA_PIN                  (10U)
#define PORTIO_I2C0_SDA_PORT                 (gpioPortC)
#define PORTIO_I2C0_SDA_LOC                  (15U)

#define BSP_I2C0_SCL_PIN                     (11U)
#define BSP_I2C0_SCL_PORT                    (gpioPortC)
#define BSP_I2C0_SCL_LOC                     (15U)

#define BSP_I2C0_SDA_PIN                     (10U)
#define BSP_I2C0_SDA_PORT                    (gpioPortC)
#define BSP_I2C0_SDA_LOC                     (15U)

// [I2C0]$

// $[I2CSENSOR]

#define BSP_I2CSENSOR_ENABLE_PIN             (2U)
#define BSP_I2CSENSOR_ENABLE_PORT            (gpioPortF)

#define BSP_I2CSENSOR_PERIPHERAL             (HAL_I2C_PORT_I2C0)
#define BSP_I2CSENSOR_SCL_PIN                (11U)
#define BSP_I2CSENSOR_SCL_PORT               (gpioPortC)
#define BSP_I2CSENSOR_SCL_LOC                (15U)

#define BSP_I2CSENSOR_SDA_PIN                (10U)
#define BSP_I2CSENSOR_SDA_PORT               (gpioPortC)
#define BSP_I2CSENSOR_SDA_LOC                (15U)

// [I2CSENSOR]$

// $[IDAC0]
// [IDAC0]$

// $[IOEXP]
// [IOEXP]$

// $[LED]
#define BSP_LED_PRESENT                      (1)

#define BSP_LED0_PIN                         (14U)
#define BSP_LED0_PORT                        (gpioPortD)

#define BSP_LED1_PIN                         (15U)
#define BSP_LED1_PORT                        (gpioPortD)

#define BSP_LED_COUNT                        (2U)
#define BSP_LED_INIT                         { { BSP_LED0_PORT, BSP_LED0_PIN }, { BSP_LED1_PORT, BSP_LED1_PIN } }
#define BSP_LED_POLARITY                     (0)
// [LED]$

// $[LETIMER0]
// [LETIMER0]$

// $[LEUART0]
// [LEUART0]$

// $[LFXO]
// [LFXO]$

// $[MODEM]
// [MODEM]$

// $[PA]

#define BSP_PA_VOLTAGE                       (3300U)
// [PA]$

// $[PCNT0]
// [PCNT0]$

// $[PORTIO]
// [PORTIO]$

// $[PRS]
// [PRS]$

// $[PTI]
#define PORTIO_PTI_DCLK_PIN                  (11U)
#define PORTIO_PTI_DCLK_PORT                 (gpioPortB)
#define PORTIO_PTI_DCLK_LOC                  (6U)

#define PORTIO_PTI_DFRAME_PIN                (13U)
#define PORTIO_PTI_DFRAME_PORT               (gpioPortB)
#define PORTIO_PTI_DFRAME_LOC                (6U)

#define PORTIO_PTI_DOUT_PIN                  (12U)
#define PORTIO_PTI_DOUT_PORT                 (gpioPortB)
#define PORTIO_PTI_DOUT_LOC                  (6U)

#define BSP_PTI_DFRAME_PIN                   (13U)
#define BSP_PTI_DFRAME_PORT                  (gpioPortB)
#define BSP_PTI_DFRAME_LOC                   (6U)

#define BSP_PTI_DOUT_PIN                     (12U)
#define BSP_PTI_DOUT_PORT                    (gpioPortB)
#define BSP_PTI_DOUT_LOC                     (6U)

// [PTI]$

// $[PYD1698]
// [PYD1698]$

// $[SERIAL]
#define BSP_SERIAL_APP_PORT                  (HAL_SERIAL_PORT_USART0)
#define BSP_SERIAL_APP_TX_PIN                (0U)
#define BSP_SERIAL_APP_TX_PORT               (gpioPortA)
#define BSP_SERIAL_APP_TX_LOC                (0U)

#define BSP_SERIAL_APP_RX_PIN                (1U)
#define BSP_SERIAL_APP_RX_PORT               (gpioPortA)
#define BSP_SERIAL_APP_RX_LOC                (0U)

#define BSP_SERIAL_APP_CTS_PIN               (2U)
#define BSP_SERIAL_APP_CTS_PORT              (gpioPortF)
#define BSP_SERIAL_APP_CTS_LOC               (22U)

#define BSP_SERIAL_APP_RTS_PIN               (3U)
#define BSP_SERIAL_APP_RTS_PORT              (gpioPortF)
#define BSP_SERIAL_APP_RTS_LOC               (22U)

// [SERIAL]$

// $[SPIDISPLAY]
// [SPIDISPLAY]$

// $[SPINCP]
// [SPINCP]$

// $[TIMER0]
// [TIMER0]$

// $[TIMER1]
// [TIMER1]$

// $[UARTNCP]
#define BSP_UARTNCP_USART_PORT               (HAL_SERIAL_PORT_USART0)
#define BSP_UARTNCP_TX_PIN                   (0U)
#define BSP_UARTNCP_TX_PORT                  (gpioPortA)
#define BSP_UARTNCP_TX_LOC                   (0U)

#define BSP_UARTNCP_RX_PIN                   (1U)
#define BSP_UARTNCP_RX_PORT                  (gpioPortA)
#define BSP_UARTNCP_RX_LOC                   (0U)

#define BSP_UARTNCP_CTS_PIN                  (2U)
#define BSP_UARTNCP_CTS_PORT                 (gpioPortF)
#define BSP_UARTNCP_CTS_LOC                  (22U)

#define BSP_UARTNCP_RTS_PIN                  (3U)
#define BSP_UARTNCP_RTS_PORT                 (gpioPortF)
#define BSP_UARTNCP_RTS_LOC                  (22U)

// [UARTNCP]$

// $[USART0]
#define PORTIO_USART0_CTS_PIN                (2U)
#define PORTIO_USART0_CTS_PORT               (gpioPortF)
#define PORTIO_USART0_CTS_LOC                (22U)

#define PORTIO_USART0_RTS_PIN                (3U)
#define PORTIO_USART0_RTS_PORT               (gpioPortF)
#define PORTIO_USART0_RTS_LOC                (22U)

#define PORTIO_USART0_RX_PIN                 (1U)
#define PORTIO_USART0_RX_PORT                (gpioPortA)
#define PORTIO_USART0_RX_LOC                 (0U)

#define PORTIO_USART0_TX_PIN                 (0U)
#define PORTIO_USART0_TX_PORT                (gpioPortA)
#define PORTIO_USART0_TX_LOC                 (0U)

#define BSP_USART0_TX_PIN                    (0U)
#define BSP_USART0_TX_PORT                   (gpioPortA)
#define BSP_USART0_TX_LOC                    (0U)

#define BSP_USART0_RX_PIN                    (1U)
#define BSP_USART0_RX_PORT                   (gpioPortA)
#define BSP_USART0_RX_LOC                    (0U)

#define BSP_USART0_CTS_PIN                   (2U)
#define BSP_USART0_CTS_PORT                  (gpioPortF)
#define BSP_USART0_CTS_LOC                   (22U)

#define BSP_USART0_RTS_PIN                   (3U)
#define BSP_USART0_RTS_PORT                  (gpioPortF)
#define BSP_USART0_RTS_LOC                   (22U)

// [USART0]$

// $[USART1]
#define PORTIO_USART1_CLK_PIN                (13U)
#define PORTIO_USART1_CLK_PORT               (gpioPortB)
#define PORTIO_USART1_CLK_LOC                (6U)

#define PORTIO_USART1_CS_PIN                 (13U)
#define PORTIO_USART1_CS_PORT                (gpioPortD)
#define PORTIO_USART1_CS_LOC                 (18U)

#define PORTIO_USART1_RX_PIN                 (12U)
#define PORTIO_USART1_RX_PORT                (gpioPortB)
#define PORTIO_USART1_RX_LOC                 (6U)

#define PORTIO_USART1_TX_PIN                 (11U)
#define PORTIO_USART1_TX_PORT                (gpioPortB)
#define PORTIO_USART1_TX_LOC                 (6U)

#define BSP_USART1_MOSI_PIN                  (11U)
#define BSP_USART1_MOSI_PORT                 (gpioPortB)
#define BSP_USART1_MOSI_LOC                  (6U)

#define BSP_USART1_MISO_PIN                  (12U)
#define BSP_USART1_MISO_PORT                 (gpioPortB)
#define BSP_USART1_MISO_LOC                  (6U)

#define BSP_USART1_CLK_PIN                   (13U)
#define BSP_USART1_CLK_PORT                  (gpioPortB)
#define BSP_USART1_CLK_LOC                   (6U)

#define BSP_USART1_CS_PIN                    (13U)
#define BSP_USART1_CS_PORT                   (gpioPortD)
#define BSP_USART1_CS_LOC                    (18U)

// [USART1]$

// $[VCOM]

#define BSP_VCOM_ENABLE_PIN                  (3U)
#define BSP_VCOM_ENABLE_PORT                 (gpioPortF)

// [VCOM]$

// $[VUART]
// [VUART]$

// $[WDOG]
// [WDOG]$

#if defined(_SILICON_LABS_MODULE)
#include "sl_module.h"
#endif

#endif /* HAL_CONFIG_BOARD_H */
