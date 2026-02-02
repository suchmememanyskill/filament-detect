# channels
FM175XX_CHANNEL_NUMS                    = 4
FM175XX_CHANNEL_1                       = 0
FM175XX_CHANNEL_2                       = 1
FM175XX_CHANNEL_3                       = 2
FM175XX_CHANNEL_4                       = 3

# Error code
FM175XX_OK                              = 0
FM175XX_ERR                             = -1
FM175XX_PARAM_ERR                       = -2
FM175XX_CHIP_TYPE_ERR                   = -10
FM175XX_CHIP_COMM_ERR                   = -11
FM175XX_CARD_TIMER_ERR                  = -20
FM175XX_CARD_LENGTH_ERR                 = -21
FM175XX_CARD_COMM_ERR                   = -22
FM175XX_CARD_AUTH_ERR                   = -23
FM175XX_CARD_WAKEUP_ERR                 = -24
FM175XX_CARD_COLL_ERR                   = -25
FM175XX_CARD_SELECT_ERR                 = -26
FM175XX_CARD_ACTIVATE_ERR               = -27
FM175XX_CARD_HALT_ERR                   = -28
FM175XX_CARD_READ_ERR                   = -29
FM175XX_CARD_WRITE_ERR                  = -30

# Mask
FM175XX_RESET                           = 0
FM175XX_SET                             = 1

# FM175xx register address
FM175XX_COMMAND_REG                     = 0x01
FM175XX_COM_I_EN_REG                    = 0x02
FM175XX_DIV_I_EN_REG                    = 0x03
FM175XX_COM_IRQ_REG                     = 0x04
FM175XX_DIV_IRQ_REG                     = 0x05
FM175XX_ERROR_REG                       = 0x06
FM175XX_STATUS_1_REG                    = 0x07
FM175XX_STATUS_2_REG                    = 0x08
FM175XX_FIFO_DATA_REG                   = 0x09
FM175XX_FIFO_LEVEL_REG                  = 0x0A
FM175XX_WATER_LEVEL_REG                 = 0x0B
FM175XX_CONTROL_REG                     = 0x0C
FM175XX_BIT_FRAMING_REG                 = 0x0D
FM175XX_COLL_REG                        = 0x0E
FM175XX_MODE_REG                        = 0x11
FM175XX_TX_MODE_REG                     = 0x12
FM175XX_RX_MODE_REG                     = 0x13
FM175XX_TX_CONTROL_REG                  = 0x14
FM175XX_TX_AUTO_REG                     = 0x15
FM175XX_TX_SEL_REG                      = 0x16
FM175XX_RX_SEL_REG                      = 0x17
FM175XX_RX_THRESHOLD_REG                = 0x18
FM175XX_DEMOD_REG                       = 0x19
FM175XX_MF_TX_REG                       = 0x1C
FM175XX_MF_RX_REG                       = 0x1D
FM175XX_TPYE_B_REG                      = 0x1E
FM175XX_SERIAL_SPEED_REG                = 0x1F
FM175XX_CRC_MSB_REG                     = 0x21
FM175XX_CRC_LSB_REG                     = 0x22
FM175XX_GSN_OFF_REG                     = 0x23
FM175XX_MODE_WIDTH_REG                  = 0x24
FM175XX_RF_CFG_REG                      = 0x26
FM175XX_GSN_ON_REG                      = 0x27
FM175XX_CW_GSP_REG                      = 0x28
FM175XX_MOD_GSP_REG                     = 0x29
FM175XX_T_MODE_REG                      = 0x2A
FM175XX_T_PRESCALER_REG                 = 0x2B
FM175XX_T_RELOAD_MSB_REG                = 0x2C
FM175XX_T_RELOAD_LSB_REG                = 0x2D
FM175XX_T_COUNTER_VAL_MSB_REG           = 0x2E
FM175XX_T_COUNTER_VAL_LSB_REG           = 0x2f
FM175XX_TEST_SEL_1_REG                  = 0x31
FM175XX_TEST_SEL_2_REG                  = 0x32
FM175XX_TEST_PIN_EN_REG                 = 0x33
FM175XX_TEST_PIN_VALUE_REG              = 0x34
FM175XX_TEST_BUS_REG                    = 0x35
FM175XX_TEST_CTRL_REG                   = 0x36
FM175XX_VERSION_REG                     = 0x37
FM175XX_TEST_DAC_1_REG                  = 0x39
FM175XX_TEST_DAC_2_REG                  = 0x3A
FM175XX_TEST_ADC_REG                    = 0x3B

# FM175xx command code
FM175XX_CMD_IDLE                        = 0x00
FM175XX_CMD_GEN_RANDOM_ID               = 0x02
FM175XX_CMD_CALC_CRC                    = 0x03
FM175XX_CMD_TRANSMIT                    = 0x04
FM175XX_CMD_NO_CMD_CHANGE               = 0x07
FM175XX_CMD_RECEIVE                     = 0x08
FM175XX_CMD_TRANSCEIVE                  = 0x0C
FM175XX_CMD_MF_AUTHENT                  = 0x0E
FM175XX_CMD_SOFT_RESET                  = 0x0F

# FM175XX RF command code
FM175XX_RF_CMD_REQA                     = 0x26
FM175XX_RF_CMD_WUPA                     = 0x52
FM175XX_RF_CMD_ANTICOL                  = [0x93, 0x95, 0x97]
FM175XX_RF_CMD_SELECT                   = [0x93, 0x95, 0x97]
FM175XX_RF_CMD_HALT                     = [0x50, 0x00]

# Chip Type
FM175XX_CHIP_TYPE_UNKNOWN               = 0x00
FM175XX_CHIP_TYPE_FM17580               = 0x01

# Chip version
FM175XX_CHIP_VER_FM17580                = 0xA1

# Carrier wave setting
FM175XX_CW_DISABLE                      = 0
FM175XX_CW1_ENABLE                      = 1
FM175XX_CW2_ENABLE                      = 2
FM175XX_CW_ENABLE                       = 3

FM175XX_CARD_INFO_READ                  = 0
FM175XX_CARD_INFO_CLEAR                 = 1

# About NTAG215 Card
FM175XX_NTAG215_TOTAL_PAGES             = 135
FM175XX_NTAG215_USER_START_PAGE         = 4
FM175XX_NTAG215_USER_END_PAGE           = 129
FM175XX_NTAG215_BYTES_PER_PAGE          = 4
FM175XX_NTAG215_TOTAL_SIZE              = 540
FM175XX_ULTRALIGHT_TOTAL_PAGES          = 44

FM175XX_ULTRALIGHT_VALID_END_PAGES      = [FM175XX_NTAG215_TOTAL_PAGES, FM175XX_ULTRALIGHT_TOTAL_PAGES]

# About M1 Card
# EEPROM
FM175XX_M1_CARD_EEPROM_SIZE             = 1024
FM175XX_M1_CARD_SECTORS                 = 16
FM175XX_M1_CARD_BLOCKS_PER_SEC          = 4
FM175XX_M1_CARD_BYTES_PER_BLK           = 16
FM175XX_M1_CARD_BYTES_PER_SEC           = 64
# Authentication mode
FM175XX_M1_CARD_AUTH_MODE_A             = 0
FM175XX_M1_CARD_AUTH_MODE_B             = 1
# Access Control Block
FM175XX_M1_CARD_ACCESS_CODE             = [0x87, 0x87, 0x87, 0x69]
FM175XX_M1_CARD_HKDF_SALT_KEY_A         = b"Snapmaker_qwertyuiop[,.;]"
FM175XX_M1_CARD_HKDF_SALT_KEY_B         = b"Snapmaker_qwertyuiop[,.;]_1q2w3e"

# Self test
FM175XX_SELF_TEST_STAGE_READY           = 0
FM175XX_SELF_TEST_STAGE_DOING           = 1
FM175XX_SELF_TEST_STAGE_STOP            = 2

FM175XX_MIN_TIME                        = 0.200