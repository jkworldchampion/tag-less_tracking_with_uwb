
#include <boards.h>
#include <deca_spi.h>
#include <examples_defines.h>
#include <port.h>
#include <sdk_config.h>
#include <stdio.h>
#include <stdlib.h>

#include "deca_uart.h"

#define UNIT_TEST 0

extern example_ptr example_pointer;
extern int unit_test_main(void);
extern void build_examples(void);



void test_run_info(unsigned char *data)
{
    printf("%s\n", data);
}

/*********************************************************************
 *
 *       main()
 *
 *  Function description
 *   Application entry point.
 */

int main(void)
{

    /* USER CODE BEGIN 1 */
  
    /* USER CODE END 1 */

    /* MCU Configuration----------------------------------------------------------*/

    /* Reset of all peripherals (if attached). */
    build_examples();

    /* USER CODE BEGIN Init */
    deca_uart_init();
    /* USER CODE END Init */


    /* USER CODE BEGIN SysInit */
    
    /* USER CODE END SysInit */

    /* Initialize all configured peripherals */
    bsp_board_init(BSP_INIT_LEDS | BSP_INIT_BUTTONS);


    /* Initialise nRF52840-DK GPIOs */
    gpio_init();

    /* Initialise the SPI for nRF52840-DK */
    nrf52840_dk_spi_init();

    /* Configuring interrupt*/
    dw_irq_init();

    /* Small pause before startup */
    nrf_delay_ms(2);

    if (UNIT_TEST)
    {
        unit_test_main();
    }
    else
    {
        // Run the selected example as selected in example_selection.h
        example_pointer();
    }
    /* USER CODE END 2 */

    /* Infinite loop */
    /* USER CODE BEGIN WHILE */
    while (1)
    {

        /* USER CODE END WHILE */

        /* USER CODE BEGIN 3 */
    }
    /* USER CODE END 3 */
}

/*************************** End of file ****************************/
