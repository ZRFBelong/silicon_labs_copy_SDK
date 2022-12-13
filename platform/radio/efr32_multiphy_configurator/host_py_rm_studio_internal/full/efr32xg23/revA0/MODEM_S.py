
# -*- coding: utf-8 -*-

__all__ = [ 'RM_Peripheral_MODEM_S' ]

from . static import Base_RM_Peripheral
from . MODEM_S_register import *

class RM_Peripheral_MODEM_S(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_MODEM_S, self).__init__(rmio, label,
            0xA8014000, 'MODEM_S',
            u"",
            [])
        self.IPVERSION = RM_Register_MODEM_S_IPVERSION(self.zz_rmio, self.zz_label)
        self.zz_rdict['IPVERSION'] = self.IPVERSION
        self.EN = RM_Register_MODEM_S_EN(self.zz_rmio, self.zz_label)
        self.zz_rdict['EN'] = self.EN
        self.IF = RM_Register_MODEM_S_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IEN = RM_Register_MODEM_S_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.SEQIF = RM_Register_MODEM_S_SEQIF(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQIF'] = self.SEQIF
        self.SEQIEN = RM_Register_MODEM_S_SEQIEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQIEN'] = self.SEQIEN
        self.STATUS = RM_Register_MODEM_S_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.STATUS2 = RM_Register_MODEM_S_STATUS2(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS2'] = self.STATUS2
        self.STATUS3 = RM_Register_MODEM_S_STATUS3(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS3'] = self.STATUS3
        self.STATUS4 = RM_Register_MODEM_S_STATUS4(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS4'] = self.STATUS4
        self.STATUS5 = RM_Register_MODEM_S_STATUS5(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS5'] = self.STATUS5
        self.STATUS6 = RM_Register_MODEM_S_STATUS6(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS6'] = self.STATUS6
        self.STATUS7 = RM_Register_MODEM_S_STATUS7(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS7'] = self.STATUS7
        self.TIMDETSTATUS = RM_Register_MODEM_S_TIMDETSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['TIMDETSTATUS'] = self.TIMDETSTATUS
        self.FSMSTATUS = RM_Register_MODEM_S_FSMSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['FSMSTATUS'] = self.FSMSTATUS
        self.FREQOFFEST = RM_Register_MODEM_S_FREQOFFEST(self.zz_rmio, self.zz_label)
        self.zz_rdict['FREQOFFEST'] = self.FREQOFFEST
        self.AFCADJRX = RM_Register_MODEM_S_AFCADJRX(self.zz_rmio, self.zz_label)
        self.zz_rdict['AFCADJRX'] = self.AFCADJRX
        self.AFCADJTX = RM_Register_MODEM_S_AFCADJTX(self.zz_rmio, self.zz_label)
        self.zz_rdict['AFCADJTX'] = self.AFCADJTX
        self.MIXCTRL = RM_Register_MODEM_S_MIXCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['MIXCTRL'] = self.MIXCTRL
        self.CTRL0 = RM_Register_MODEM_S_CTRL0(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL0'] = self.CTRL0
        self.CTRL1 = RM_Register_MODEM_S_CTRL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL1'] = self.CTRL1
        self.CTRL2 = RM_Register_MODEM_S_CTRL2(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL2'] = self.CTRL2
        self.CTRL3 = RM_Register_MODEM_S_CTRL3(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL3'] = self.CTRL3
        self.CTRL4 = RM_Register_MODEM_S_CTRL4(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL4'] = self.CTRL4
        self.CTRL5 = RM_Register_MODEM_S_CTRL5(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL5'] = self.CTRL5
        self.CTRL6 = RM_Register_MODEM_S_CTRL6(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL6'] = self.CTRL6
        self.TXBR = RM_Register_MODEM_S_TXBR(self.zz_rmio, self.zz_label)
        self.zz_rdict['TXBR'] = self.TXBR
        self.RXBR = RM_Register_MODEM_S_RXBR(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXBR'] = self.RXBR
        self.CF = RM_Register_MODEM_S_CF(self.zz_rmio, self.zz_label)
        self.zz_rdict['CF'] = self.CF
        self.PRE = RM_Register_MODEM_S_PRE(self.zz_rmio, self.zz_label)
        self.zz_rdict['PRE'] = self.PRE
        self.SYNC0 = RM_Register_MODEM_S_SYNC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNC0'] = self.SYNC0
        self.SYNC1 = RM_Register_MODEM_S_SYNC1(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNC1'] = self.SYNC1
        self.TIMING = RM_Register_MODEM_S_TIMING(self.zz_rmio, self.zz_label)
        self.zz_rdict['TIMING'] = self.TIMING
        self.DSSS0 = RM_Register_MODEM_S_DSSS0(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSSS0'] = self.DSSS0
        self.MODINDEX = RM_Register_MODEM_S_MODINDEX(self.zz_rmio, self.zz_label)
        self.zz_rdict['MODINDEX'] = self.MODINDEX
        self.AFC = RM_Register_MODEM_S_AFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['AFC'] = self.AFC
        self.AFCADJLIM = RM_Register_MODEM_S_AFCADJLIM(self.zz_rmio, self.zz_label)
        self.zz_rdict['AFCADJLIM'] = self.AFCADJLIM
        self.SHAPING0 = RM_Register_MODEM_S_SHAPING0(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING0'] = self.SHAPING0
        self.SHAPING1 = RM_Register_MODEM_S_SHAPING1(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING1'] = self.SHAPING1
        self.SHAPING2 = RM_Register_MODEM_S_SHAPING2(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING2'] = self.SHAPING2
        self.SHAPING3 = RM_Register_MODEM_S_SHAPING3(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING3'] = self.SHAPING3
        self.SHAPING4 = RM_Register_MODEM_S_SHAPING4(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING4'] = self.SHAPING4
        self.SHAPING5 = RM_Register_MODEM_S_SHAPING5(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING5'] = self.SHAPING5
        self.SHAPING6 = RM_Register_MODEM_S_SHAPING6(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING6'] = self.SHAPING6
        self.SHAPING7 = RM_Register_MODEM_S_SHAPING7(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING7'] = self.SHAPING7
        self.SHAPING8 = RM_Register_MODEM_S_SHAPING8(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING8'] = self.SHAPING8
        self.SHAPING9 = RM_Register_MODEM_S_SHAPING9(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING9'] = self.SHAPING9
        self.SHAPING10 = RM_Register_MODEM_S_SHAPING10(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING10'] = self.SHAPING10
        self.SHAPING11 = RM_Register_MODEM_S_SHAPING11(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING11'] = self.SHAPING11
        self.SHAPING12 = RM_Register_MODEM_S_SHAPING12(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING12'] = self.SHAPING12
        self.SHAPING13 = RM_Register_MODEM_S_SHAPING13(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING13'] = self.SHAPING13
        self.SHAPING14 = RM_Register_MODEM_S_SHAPING14(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING14'] = self.SHAPING14
        self.SHAPING15 = RM_Register_MODEM_S_SHAPING15(self.zz_rmio, self.zz_label)
        self.zz_rdict['SHAPING15'] = self.SHAPING15
        self.OOKSHAPING = RM_Register_MODEM_S_OOKSHAPING(self.zz_rmio, self.zz_label)
        self.zz_rdict['OOKSHAPING'] = self.OOKSHAPING
        self.RAMPCTRL = RM_Register_MODEM_S_RAMPCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['RAMPCTRL'] = self.RAMPCTRL
        self.RAMPLEV = RM_Register_MODEM_S_RAMPLEV(self.zz_rmio, self.zz_label)
        self.zz_rdict['RAMPLEV'] = self.RAMPLEV
        self.ANARAMPCTRL = RM_Register_MODEM_S_ANARAMPCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMPCTRL'] = self.ANARAMPCTRL
        self.ANARAMP0 = RM_Register_MODEM_S_ANARAMP0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP0'] = self.ANARAMP0
        self.ANARAMP1 = RM_Register_MODEM_S_ANARAMP1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP1'] = self.ANARAMP1
        self.ANARAMP2 = RM_Register_MODEM_S_ANARAMP2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP2'] = self.ANARAMP2
        self.ANARAMP3 = RM_Register_MODEM_S_ANARAMP3(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP3'] = self.ANARAMP3
        self.ANARAMP4 = RM_Register_MODEM_S_ANARAMP4(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP4'] = self.ANARAMP4
        self.ANARAMP5 = RM_Register_MODEM_S_ANARAMP5(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP5'] = self.ANARAMP5
        self.ANARAMP6 = RM_Register_MODEM_S_ANARAMP6(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP6'] = self.ANARAMP6
        self.ANARAMP7 = RM_Register_MODEM_S_ANARAMP7(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP7'] = self.ANARAMP7
        self.ANARAMP8 = RM_Register_MODEM_S_ANARAMP8(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP8'] = self.ANARAMP8
        self.ANARAMP9 = RM_Register_MODEM_S_ANARAMP9(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP9'] = self.ANARAMP9
        self.ANARAMP10 = RM_Register_MODEM_S_ANARAMP10(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANARAMP10'] = self.ANARAMP10
        self.DCCOMP = RM_Register_MODEM_S_DCCOMP(self.zz_rmio, self.zz_label)
        self.zz_rdict['DCCOMP'] = self.DCCOMP
        self.DCCOMPFILTINIT = RM_Register_MODEM_S_DCCOMPFILTINIT(self.zz_rmio, self.zz_label)
        self.zz_rdict['DCCOMPFILTINIT'] = self.DCCOMPFILTINIT
        self.DCESTI = RM_Register_MODEM_S_DCESTI(self.zz_rmio, self.zz_label)
        self.zz_rdict['DCESTI'] = self.DCESTI
        self.SRCCHF = RM_Register_MODEM_S_SRCCHF(self.zz_rmio, self.zz_label)
        self.zz_rdict['SRCCHF'] = self.SRCCHF
        self.INTAFC = RM_Register_MODEM_S_INTAFC(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTAFC'] = self.INTAFC
        self.DSATHD0 = RM_Register_MODEM_S_DSATHD0(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSATHD0'] = self.DSATHD0
        self.DSATHD1 = RM_Register_MODEM_S_DSATHD1(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSATHD1'] = self.DSATHD1
        self.DSATHD2 = RM_Register_MODEM_S_DSATHD2(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSATHD2'] = self.DSATHD2
        self.DSATHD3 = RM_Register_MODEM_S_DSATHD3(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSATHD3'] = self.DSATHD3
        self.DSATHD4 = RM_Register_MODEM_S_DSATHD4(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSATHD4'] = self.DSATHD4
        self.DSACTRL = RM_Register_MODEM_S_DSACTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSACTRL'] = self.DSACTRL
        self.DIGMIXCTRL = RM_Register_MODEM_S_DIGMIXCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DIGMIXCTRL'] = self.DIGMIXCTRL
        self.VITERBIDEMOD = RM_Register_MODEM_S_VITERBIDEMOD(self.zz_rmio, self.zz_label)
        self.zz_rdict['VITERBIDEMOD'] = self.VITERBIDEMOD
        self.VTCORRCFG0 = RM_Register_MODEM_S_VTCORRCFG0(self.zz_rmio, self.zz_label)
        self.zz_rdict['VTCORRCFG0'] = self.VTCORRCFG0
        self.VTCORRCFG1 = RM_Register_MODEM_S_VTCORRCFG1(self.zz_rmio, self.zz_label)
        self.zz_rdict['VTCORRCFG1'] = self.VTCORRCFG1
        self.VTTRACK = RM_Register_MODEM_S_VTTRACK(self.zz_rmio, self.zz_label)
        self.zz_rdict['VTTRACK'] = self.VTTRACK
        self.VTBLETIMING = RM_Register_MODEM_S_VTBLETIMING(self.zz_rmio, self.zz_label)
        self.zz_rdict['VTBLETIMING'] = self.VTBLETIMING
        self.BREST = RM_Register_MODEM_S_BREST(self.zz_rmio, self.zz_label)
        self.zz_rdict['BREST'] = self.BREST
        self.AUTOCG = RM_Register_MODEM_S_AUTOCG(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUTOCG'] = self.AUTOCG
        self.CGCLKSTOP = RM_Register_MODEM_S_CGCLKSTOP(self.zz_rmio, self.zz_label)
        self.zz_rdict['CGCLKSTOP'] = self.CGCLKSTOP
        self.POE = RM_Register_MODEM_S_POE(self.zz_rmio, self.zz_label)
        self.zz_rdict['POE'] = self.POE
        self.DIRECTMODE = RM_Register_MODEM_S_DIRECTMODE(self.zz_rmio, self.zz_label)
        self.zz_rdict['DIRECTMODE'] = self.DIRECTMODE
        self.LONGRANGE1 = RM_Register_MODEM_S_LONGRANGE1(self.zz_rmio, self.zz_label)
        self.zz_rdict['LONGRANGE1'] = self.LONGRANGE1
        self.LONGRANGE2 = RM_Register_MODEM_S_LONGRANGE2(self.zz_rmio, self.zz_label)
        self.zz_rdict['LONGRANGE2'] = self.LONGRANGE2
        self.LONGRANGE3 = RM_Register_MODEM_S_LONGRANGE3(self.zz_rmio, self.zz_label)
        self.zz_rdict['LONGRANGE3'] = self.LONGRANGE3
        self.LONGRANGE4 = RM_Register_MODEM_S_LONGRANGE4(self.zz_rmio, self.zz_label)
        self.zz_rdict['LONGRANGE4'] = self.LONGRANGE4
        self.LONGRANGE5 = RM_Register_MODEM_S_LONGRANGE5(self.zz_rmio, self.zz_label)
        self.zz_rdict['LONGRANGE5'] = self.LONGRANGE5
        self.LONGRANGE6 = RM_Register_MODEM_S_LONGRANGE6(self.zz_rmio, self.zz_label)
        self.zz_rdict['LONGRANGE6'] = self.LONGRANGE6
        self.LRFRC = RM_Register_MODEM_S_LRFRC(self.zz_rmio, self.zz_label)
        self.zz_rdict['LRFRC'] = self.LRFRC
        self.COH0 = RM_Register_MODEM_S_COH0(self.zz_rmio, self.zz_label)
        self.zz_rdict['COH0'] = self.COH0
        self.COH1 = RM_Register_MODEM_S_COH1(self.zz_rmio, self.zz_label)
        self.zz_rdict['COH1'] = self.COH1
        self.COH2 = RM_Register_MODEM_S_COH2(self.zz_rmio, self.zz_label)
        self.zz_rdict['COH2'] = self.COH2
        self.COH3 = RM_Register_MODEM_S_COH3(self.zz_rmio, self.zz_label)
        self.zz_rdict['COH3'] = self.COH3
        self.CMD = RM_Register_MODEM_S_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.SYNCPROPERTIES = RM_Register_MODEM_S_SYNCPROPERTIES(self.zz_rmio, self.zz_label)
        self.zz_rdict['SYNCPROPERTIES'] = self.SYNCPROPERTIES
        self.DIGIGAINCTRL = RM_Register_MODEM_S_DIGIGAINCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DIGIGAINCTRL'] = self.DIGIGAINCTRL
        self.PRSCTRL = RM_Register_MODEM_S_PRSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PRSCTRL'] = self.PRSCTRL
        self.PADEBUG = RM_Register_MODEM_S_PADEBUG(self.zz_rmio, self.zz_label)
        self.zz_rdict['PADEBUG'] = self.PADEBUG
        self.REALTIMCFE = RM_Register_MODEM_S_REALTIMCFE(self.zz_rmio, self.zz_label)
        self.zz_rdict['REALTIMCFE'] = self.REALTIMCFE
        self.ETSCTRL = RM_Register_MODEM_S_ETSCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETSCTRL'] = self.ETSCTRL
        self.ETSTIM = RM_Register_MODEM_S_ETSTIM(self.zz_rmio, self.zz_label)
        self.zz_rdict['ETSTIM'] = self.ETSTIM
        self.ANTSWCTRL = RM_Register_MODEM_S_ANTSWCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANTSWCTRL'] = self.ANTSWCTRL
        self.ANTSWCTRL1 = RM_Register_MODEM_S_ANTSWCTRL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANTSWCTRL1'] = self.ANTSWCTRL1
        self.ANTSWSTART = RM_Register_MODEM_S_ANTSWSTART(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANTSWSTART'] = self.ANTSWSTART
        self.ANTSWEND = RM_Register_MODEM_S_ANTSWEND(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANTSWEND'] = self.ANTSWEND
        self.TRECPMPATT = RM_Register_MODEM_S_TRECPMPATT(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRECPMPATT'] = self.TRECPMPATT
        self.TRECPMDET = RM_Register_MODEM_S_TRECPMDET(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRECPMDET'] = self.TRECPMDET
        self.TRECSCFG = RM_Register_MODEM_S_TRECSCFG(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRECSCFG'] = self.TRECSCFG
        self.CFGANTPATT = RM_Register_MODEM_S_CFGANTPATT(self.zz_rmio, self.zz_label)
        self.zz_rdict['CFGANTPATT'] = self.CFGANTPATT
        self.CHFCOE00 = RM_Register_MODEM_S_CHFCOE00(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE00'] = self.CHFCOE00
        self.CHFCOE01 = RM_Register_MODEM_S_CHFCOE01(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE01'] = self.CHFCOE01
        self.CHFCOE02 = RM_Register_MODEM_S_CHFCOE02(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE02'] = self.CHFCOE02
        self.CHFCOE03 = RM_Register_MODEM_S_CHFCOE03(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE03'] = self.CHFCOE03
        self.CHFCOE04 = RM_Register_MODEM_S_CHFCOE04(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE04'] = self.CHFCOE04
        self.CHFCOE05 = RM_Register_MODEM_S_CHFCOE05(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE05'] = self.CHFCOE05
        self.CHFCOE06 = RM_Register_MODEM_S_CHFCOE06(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE06'] = self.CHFCOE06
        self.CHFCOE10 = RM_Register_MODEM_S_CHFCOE10(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE10'] = self.CHFCOE10
        self.CHFCOE11 = RM_Register_MODEM_S_CHFCOE11(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE11'] = self.CHFCOE11
        self.CHFCOE12 = RM_Register_MODEM_S_CHFCOE12(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE12'] = self.CHFCOE12
        self.CHFCOE13 = RM_Register_MODEM_S_CHFCOE13(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE13'] = self.CHFCOE13
        self.CHFCOE14 = RM_Register_MODEM_S_CHFCOE14(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE14'] = self.CHFCOE14
        self.CHFCOE15 = RM_Register_MODEM_S_CHFCOE15(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE15'] = self.CHFCOE15
        self.CHFCOE16 = RM_Register_MODEM_S_CHFCOE16(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCOE16'] = self.CHFCOE16
        self.CHFCTRL = RM_Register_MODEM_S_CHFCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFCTRL'] = self.CHFCTRL
        self.CHFLATENCYCTRL = RM_Register_MODEM_S_CHFLATENCYCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CHFLATENCYCTRL'] = self.CHFLATENCYCTRL
        self.FRMSCHTIME = RM_Register_MODEM_S_FRMSCHTIME(self.zz_rmio, self.zz_label)
        self.zz_rdict['FRMSCHTIME'] = self.FRMSCHTIME
        self.PREFILTCOEFF = RM_Register_MODEM_S_PREFILTCOEFF(self.zz_rmio, self.zz_label)
        self.zz_rdict['PREFILTCOEFF'] = self.PREFILTCOEFF
        self.RXRESTART = RM_Register_MODEM_S_RXRESTART(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXRESTART'] = self.RXRESTART
        self.SQ = RM_Register_MODEM_S_SQ(self.zz_rmio, self.zz_label)
        self.zz_rdict['SQ'] = self.SQ
        self.SQEXT = RM_Register_MODEM_S_SQEXT(self.zz_rmio, self.zz_label)
        self.zz_rdict['SQEXT'] = self.SQEXT
        self.SQI = RM_Register_MODEM_S_SQI(self.zz_rmio, self.zz_label)
        self.zz_rdict['SQI'] = self.SQI
        self.ANTDIVCTRL = RM_Register_MODEM_S_ANTDIVCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANTDIVCTRL'] = self.ANTDIVCTRL
        self.ANTDIVFW = RM_Register_MODEM_S_ANTDIVFW(self.zz_rmio, self.zz_label)
        self.zz_rdict['ANTDIVFW'] = self.ANTDIVFW
        self.PHDMODANTDIV = RM_Register_MODEM_S_PHDMODANTDIV(self.zz_rmio, self.zz_label)
        self.zz_rdict['PHDMODANTDIV'] = self.PHDMODANTDIV
        self.PHANTDECSION = RM_Register_MODEM_S_PHANTDECSION(self.zz_rmio, self.zz_label)
        self.zz_rdict['PHANTDECSION'] = self.PHANTDECSION
        self.PHDMODCTRL = RM_Register_MODEM_S_PHDMODCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PHDMODCTRL'] = self.PHDMODCTRL
        self.IRCAL = RM_Register_MODEM_S_IRCAL(self.zz_rmio, self.zz_label)
        self.zz_rdict['IRCAL'] = self.IRCAL
        self.IRCALCOEF = RM_Register_MODEM_S_IRCALCOEF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IRCALCOEF'] = self.IRCALCOEF
        self.IRCALCOEFWR0 = RM_Register_MODEM_S_IRCALCOEFWR0(self.zz_rmio, self.zz_label)
        self.zz_rdict['IRCALCOEFWR0'] = self.IRCALCOEFWR0
        self.IRCALCOEFWR1 = RM_Register_MODEM_S_IRCALCOEFWR1(self.zz_rmio, self.zz_label)
        self.zz_rdict['IRCALCOEFWR1'] = self.IRCALCOEFWR1
        self.ADCTRL1 = RM_Register_MODEM_S_ADCTRL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADCTRL1'] = self.ADCTRL1
        self.ADCTRL2 = RM_Register_MODEM_S_ADCTRL2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADCTRL2'] = self.ADCTRL2
        self.ADQUAL0 = RM_Register_MODEM_S_ADQUAL0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL0'] = self.ADQUAL0
        self.ADQUAL1 = RM_Register_MODEM_S_ADQUAL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL1'] = self.ADQUAL1
        self.ADQUAL2 = RM_Register_MODEM_S_ADQUAL2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL2'] = self.ADQUAL2
        self.ADQUAL3 = RM_Register_MODEM_S_ADQUAL3(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL3'] = self.ADQUAL3
        self.ADQUAL4 = RM_Register_MODEM_S_ADQUAL4(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL4'] = self.ADQUAL4
        self.ADQUAL5 = RM_Register_MODEM_S_ADQUAL5(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL5'] = self.ADQUAL5
        self.ADQUAL6 = RM_Register_MODEM_S_ADQUAL6(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL6'] = self.ADQUAL6
        self.ADQUAL7 = RM_Register_MODEM_S_ADQUAL7(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL7'] = self.ADQUAL7
        self.ADQUAL8 = RM_Register_MODEM_S_ADQUAL8(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL8'] = self.ADQUAL8
        self.ADQUAL9 = RM_Register_MODEM_S_ADQUAL9(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL9'] = self.ADQUAL9
        self.ADQUAL10 = RM_Register_MODEM_S_ADQUAL10(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADQUAL10'] = self.ADQUAL10
        self.ADFSM0 = RM_Register_MODEM_S_ADFSM0(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM0'] = self.ADFSM0
        self.ADFSM1 = RM_Register_MODEM_S_ADFSM1(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM1'] = self.ADFSM1
        self.ADFSM2 = RM_Register_MODEM_S_ADFSM2(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM2'] = self.ADFSM2
        self.ADFSM3 = RM_Register_MODEM_S_ADFSM3(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM3'] = self.ADFSM3
        self.ADFSM4 = RM_Register_MODEM_S_ADFSM4(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM4'] = self.ADFSM4
        self.ADFSM5 = RM_Register_MODEM_S_ADFSM5(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM5'] = self.ADFSM5
        self.ADFSM6 = RM_Register_MODEM_S_ADFSM6(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM6'] = self.ADFSM6
        self.ADFSM7 = RM_Register_MODEM_S_ADFSM7(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM7'] = self.ADFSM7
        self.ADFSM8 = RM_Register_MODEM_S_ADFSM8(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM8'] = self.ADFSM8
        self.ADFSM9 = RM_Register_MODEM_S_ADFSM9(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM9'] = self.ADFSM9
        self.ADFSM10 = RM_Register_MODEM_S_ADFSM10(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM10'] = self.ADFSM10
        self.ADFSM11 = RM_Register_MODEM_S_ADFSM11(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM11'] = self.ADFSM11
        self.ADFSM12 = RM_Register_MODEM_S_ADFSM12(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM12'] = self.ADFSM12
        self.ADFSM13 = RM_Register_MODEM_S_ADFSM13(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM13'] = self.ADFSM13
        self.ADFSM14 = RM_Register_MODEM_S_ADFSM14(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM14'] = self.ADFSM14
        self.ADFSM15 = RM_Register_MODEM_S_ADFSM15(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM15'] = self.ADFSM15
        self.ADFSM16 = RM_Register_MODEM_S_ADFSM16(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM16'] = self.ADFSM16
        self.ADFSM17 = RM_Register_MODEM_S_ADFSM17(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM17'] = self.ADFSM17
        self.ADFSM18 = RM_Register_MODEM_S_ADFSM18(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM18'] = self.ADFSM18
        self.ADFSM19 = RM_Register_MODEM_S_ADFSM19(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM19'] = self.ADFSM19
        self.ADFSM20 = RM_Register_MODEM_S_ADFSM20(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM20'] = self.ADFSM20
        self.ADFSM21 = RM_Register_MODEM_S_ADFSM21(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM21'] = self.ADFSM21
        self.ADFSM22 = RM_Register_MODEM_S_ADFSM22(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM22'] = self.ADFSM22
        self.ADFSM23 = RM_Register_MODEM_S_ADFSM23(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM23'] = self.ADFSM23
        self.ADFSM24 = RM_Register_MODEM_S_ADFSM24(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM24'] = self.ADFSM24
        self.ADFSM25 = RM_Register_MODEM_S_ADFSM25(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM25'] = self.ADFSM25
        self.ADFSM26 = RM_Register_MODEM_S_ADFSM26(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM26'] = self.ADFSM26
        self.ADFSM27 = RM_Register_MODEM_S_ADFSM27(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM27'] = self.ADFSM27
        self.ADFSM28 = RM_Register_MODEM_S_ADFSM28(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM28'] = self.ADFSM28
        self.ADFSM29 = RM_Register_MODEM_S_ADFSM29(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM29'] = self.ADFSM29
        self.ADFSM30 = RM_Register_MODEM_S_ADFSM30(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADFSM30'] = self.ADFSM30
        self.BCRCTRL0 = RM_Register_MODEM_S_BCRCTRL0(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRCTRL0'] = self.BCRCTRL0
        self.BCRCTRL1 = RM_Register_MODEM_S_BCRCTRL1(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRCTRL1'] = self.BCRCTRL1
        self.BCRDEMODCTRL = RM_Register_MODEM_S_BCRDEMODCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODCTRL'] = self.BCRDEMODCTRL
        self.BCRDEMODOOK = RM_Register_MODEM_S_BCRDEMODOOK(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODOOK'] = self.BCRDEMODOOK
        self.BCRDEMODAFC0 = RM_Register_MODEM_S_BCRDEMODAFC0(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODAFC0'] = self.BCRDEMODAFC0
        self.BCRDEMODAFC1 = RM_Register_MODEM_S_BCRDEMODAFC1(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODAFC1'] = self.BCRDEMODAFC1
        self.BCRDEMOD4FSK0 = RM_Register_MODEM_S_BCRDEMOD4FSK0(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMOD4FSK0'] = self.BCRDEMOD4FSK0
        self.BCRDEMOD4FSK1 = RM_Register_MODEM_S_BCRDEMOD4FSK1(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMOD4FSK1'] = self.BCRDEMOD4FSK1
        self.BCRDEMODANT = RM_Register_MODEM_S_BCRDEMODANT(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODANT'] = self.BCRDEMODANT
        self.BCRDEMODRSSI = RM_Register_MODEM_S_BCRDEMODRSSI(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODRSSI'] = self.BCRDEMODRSSI
        self.BCRDEMODARR0 = RM_Register_MODEM_S_BCRDEMODARR0(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODARR0'] = self.BCRDEMODARR0
        self.BCRDEMODARR1 = RM_Register_MODEM_S_BCRDEMODARR1(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODARR1'] = self.BCRDEMODARR1
        self.BCRDEMODARR2 = RM_Register_MODEM_S_BCRDEMODARR2(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODARR2'] = self.BCRDEMODARR2
        self.BCRDEMODKSI = RM_Register_MODEM_S_BCRDEMODKSI(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODKSI'] = self.BCRDEMODKSI
        self.BCRDEMODPMEXP = RM_Register_MODEM_S_BCRDEMODPMEXP(self.zz_rmio, self.zz_label)
        self.zz_rdict['BCRDEMODPMEXP'] = self.BCRDEMODPMEXP
        self.SPARE = RM_Register_MODEM_S_SPARE(self.zz_rmio, self.zz_label)
        self.zz_rdict['SPARE'] = self.SPARE
        self.__dict__['zz_frozen'] = True