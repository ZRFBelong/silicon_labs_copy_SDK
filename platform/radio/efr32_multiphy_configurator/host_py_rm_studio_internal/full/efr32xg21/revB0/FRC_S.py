
# -*- coding: utf-8 -*-

__all__ = [ 'RM_Peripheral_FRC_S' ]

from . static import Base_RM_Peripheral
from . FRC_S_register import *

class RM_Peripheral_FRC_S(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_FRC_S, self).__init__(rmio, label,
            0xA8004000, 'FRC_S',
            u"",
            [])
        self.IPVERSION = RM_Register_FRC_S_IPVERSION(self.zz_rmio, self.zz_label)
        self.zz_rdict['IPVERSION'] = self.IPVERSION
        self.EN = RM_Register_FRC_S_EN(self.zz_rmio, self.zz_label)
        self.zz_rdict['EN'] = self.EN
        self.STATUS = RM_Register_FRC_S_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.DFLCTRL = RM_Register_FRC_S_DFLCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DFLCTRL'] = self.DFLCTRL
        self.MAXLENGTH = RM_Register_FRC_S_MAXLENGTH(self.zz_rmio, self.zz_label)
        self.zz_rdict['MAXLENGTH'] = self.MAXLENGTH
        self.ADDRFILTCTRL = RM_Register_FRC_S_ADDRFILTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADDRFILTCTRL'] = self.ADDRFILTCTRL
        self.DATABUFFER = RM_Register_FRC_S_DATABUFFER(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATABUFFER'] = self.DATABUFFER
        self.WCNT = RM_Register_FRC_S_WCNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNT'] = self.WCNT
        self.WCNTCMP0 = RM_Register_FRC_S_WCNTCMP0(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP0'] = self.WCNTCMP0
        self.WCNTCMP1 = RM_Register_FRC_S_WCNTCMP1(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP1'] = self.WCNTCMP1
        self.WCNTCMP2 = RM_Register_FRC_S_WCNTCMP2(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP2'] = self.WCNTCMP2
        self.CMD = RM_Register_FRC_S_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.WHITECTRL = RM_Register_FRC_S_WHITECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['WHITECTRL'] = self.WHITECTRL
        self.WHITEPOLY = RM_Register_FRC_S_WHITEPOLY(self.zz_rmio, self.zz_label)
        self.zz_rdict['WHITEPOLY'] = self.WHITEPOLY
        self.WHITEINIT = RM_Register_FRC_S_WHITEINIT(self.zz_rmio, self.zz_label)
        self.zz_rdict['WHITEINIT'] = self.WHITEINIT
        self.FECCTRL = RM_Register_FRC_S_FECCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['FECCTRL'] = self.FECCTRL
        self.BLOCKRAMADDR = RM_Register_FRC_S_BLOCKRAMADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['BLOCKRAMADDR'] = self.BLOCKRAMADDR
        self.CONVRAMADDR = RM_Register_FRC_S_CONVRAMADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['CONVRAMADDR'] = self.CONVRAMADDR
        self.CTRL = RM_Register_FRC_S_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.RXCTRL = RM_Register_FRC_S_RXCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXCTRL'] = self.RXCTRL
        self.TRAILTXDATACTRL = RM_Register_FRC_S_TRAILTXDATACTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRAILTXDATACTRL'] = self.TRAILTXDATACTRL
        self.TRAILRXDATA = RM_Register_FRC_S_TRAILRXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRAILRXDATA'] = self.TRAILRXDATA
        self.SCNT = RM_Register_FRC_S_SCNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCNT'] = self.SCNT
        self.CONVGENERATOR = RM_Register_FRC_S_CONVGENERATOR(self.zz_rmio, self.zz_label)
        self.zz_rdict['CONVGENERATOR'] = self.CONVGENERATOR
        self.PUNCTCTRL = RM_Register_FRC_S_PUNCTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PUNCTCTRL'] = self.PUNCTCTRL
        self.PAUSECTRL = RM_Register_FRC_S_PAUSECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PAUSECTRL'] = self.PAUSECTRL
        self.IF = RM_Register_FRC_S_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IEN = RM_Register_FRC_S_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.MIRRORIF = RM_Register_FRC_S_MIRRORIF(self.zz_rmio, self.zz_label)
        self.zz_rdict['MIRRORIF'] = self.MIRRORIF
        self.BUFFERMODE = RM_Register_FRC_S_BUFFERMODE(self.zz_rmio, self.zz_label)
        self.zz_rdict['BUFFERMODE'] = self.BUFFERMODE
        self.SNIFFCTRL = RM_Register_FRC_S_SNIFFCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNIFFCTRL'] = self.SNIFFCTRL
        self.AUXDATA = RM_Register_FRC_S_AUXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUXDATA'] = self.AUXDATA
        self.RAWCTRL = RM_Register_FRC_S_RAWCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['RAWCTRL'] = self.RAWCTRL
        self.RXRAWDATA = RM_Register_FRC_S_RXRAWDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXRAWDATA'] = self.RXRAWDATA
        self.PAUSEDATA = RM_Register_FRC_S_PAUSEDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['PAUSEDATA'] = self.PAUSEDATA
        self.LIKELYCONVSTATE = RM_Register_FRC_S_LIKELYCONVSTATE(self.zz_rmio, self.zz_label)
        self.zz_rdict['LIKELYCONVSTATE'] = self.LIKELYCONVSTATE
        self.INTELEMENTNEXT = RM_Register_FRC_S_INTELEMENTNEXT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENTNEXT'] = self.INTELEMENTNEXT
        self.INTWRITEPOINT = RM_Register_FRC_S_INTWRITEPOINT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTWRITEPOINT'] = self.INTWRITEPOINT
        self.INTREADPOINT = RM_Register_FRC_S_INTREADPOINT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTREADPOINT'] = self.INTREADPOINT
        self.AUTOCG = RM_Register_FRC_S_AUTOCG(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUTOCG'] = self.AUTOCG
        self.CGCLKSTOP = RM_Register_FRC_S_CGCLKSTOP(self.zz_rmio, self.zz_label)
        self.zz_rdict['CGCLKSTOP'] = self.CGCLKSTOP
        self.RAMBASEADDR = RM_Register_FRC_S_RAMBASEADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['RAMBASEADDR'] = self.RAMBASEADDR
        self.FCD0 = RM_Register_FRC_S_FCD0(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD0'] = self.FCD0
        self.FCD1 = RM_Register_FRC_S_FCD1(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD1'] = self.FCD1
        self.FCD2 = RM_Register_FRC_S_FCD2(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD2'] = self.FCD2
        self.FCD3 = RM_Register_FRC_S_FCD3(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD3'] = self.FCD3
        self.INTELEMENT0 = RM_Register_FRC_S_INTELEMENT0(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT0'] = self.INTELEMENT0
        self.INTELEMENT1 = RM_Register_FRC_S_INTELEMENT1(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT1'] = self.INTELEMENT1
        self.INTELEMENT2 = RM_Register_FRC_S_INTELEMENT2(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT2'] = self.INTELEMENT2
        self.INTELEMENT3 = RM_Register_FRC_S_INTELEMENT3(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT3'] = self.INTELEMENT3
        self.INTELEMENT4 = RM_Register_FRC_S_INTELEMENT4(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT4'] = self.INTELEMENT4
        self.INTELEMENT5 = RM_Register_FRC_S_INTELEMENT5(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT5'] = self.INTELEMENT5
        self.INTELEMENT6 = RM_Register_FRC_S_INTELEMENT6(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT6'] = self.INTELEMENT6
        self.INTELEMENT7 = RM_Register_FRC_S_INTELEMENT7(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT7'] = self.INTELEMENT7
        self.INTELEMENT8 = RM_Register_FRC_S_INTELEMENT8(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT8'] = self.INTELEMENT8
        self.INTELEMENT9 = RM_Register_FRC_S_INTELEMENT9(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT9'] = self.INTELEMENT9
        self.INTELEMENT10 = RM_Register_FRC_S_INTELEMENT10(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT10'] = self.INTELEMENT10
        self.INTELEMENT11 = RM_Register_FRC_S_INTELEMENT11(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT11'] = self.INTELEMENT11
        self.INTELEMENT12 = RM_Register_FRC_S_INTELEMENT12(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT12'] = self.INTELEMENT12
        self.INTELEMENT13 = RM_Register_FRC_S_INTELEMENT13(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT13'] = self.INTELEMENT13
        self.INTELEMENT14 = RM_Register_FRC_S_INTELEMENT14(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT14'] = self.INTELEMENT14
        self.INTELEMENT15 = RM_Register_FRC_S_INTELEMENT15(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT15'] = self.INTELEMENT15
        self.__dict__['zz_frozen'] = True