
# -*- coding: utf-8 -*-

__all__ = [ 'RM_Peripheral_FRC_NS' ]

from . static import Base_RM_Peripheral
from . FRC_NS_register import *

class RM_Peripheral_FRC_NS(Base_RM_Peripheral):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Peripheral_FRC_NS, self).__init__(rmio, label,
            0xB8004000, 'FRC_NS',
            u"",
            [])
        self.IPVERSION = RM_Register_FRC_NS_IPVERSION(self.zz_rmio, self.zz_label)
        self.zz_rdict['IPVERSION'] = self.IPVERSION
        self.EN = RM_Register_FRC_NS_EN(self.zz_rmio, self.zz_label)
        self.zz_rdict['EN'] = self.EN
        self.STATUS = RM_Register_FRC_NS_STATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['STATUS'] = self.STATUS
        self.DFLCTRL = RM_Register_FRC_NS_DFLCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DFLCTRL'] = self.DFLCTRL
        self.MAXLENGTH = RM_Register_FRC_NS_MAXLENGTH(self.zz_rmio, self.zz_label)
        self.zz_rdict['MAXLENGTH'] = self.MAXLENGTH
        self.ADDRFILTCTRL = RM_Register_FRC_NS_ADDRFILTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['ADDRFILTCTRL'] = self.ADDRFILTCTRL
        self.DATABUFFER = RM_Register_FRC_NS_DATABUFFER(self.zz_rmio, self.zz_label)
        self.zz_rdict['DATABUFFER'] = self.DATABUFFER
        self.WCNT = RM_Register_FRC_NS_WCNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNT'] = self.WCNT
        self.WCNTCMP0 = RM_Register_FRC_NS_WCNTCMP0(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP0'] = self.WCNTCMP0
        self.WCNTCMP1 = RM_Register_FRC_NS_WCNTCMP1(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP1'] = self.WCNTCMP1
        self.WCNTCMP2 = RM_Register_FRC_NS_WCNTCMP2(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP2'] = self.WCNTCMP2
        self.CMD = RM_Register_FRC_NS_CMD(self.zz_rmio, self.zz_label)
        self.zz_rdict['CMD'] = self.CMD
        self.WHITECTRL = RM_Register_FRC_NS_WHITECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['WHITECTRL'] = self.WHITECTRL
        self.WHITEPOLY = RM_Register_FRC_NS_WHITEPOLY(self.zz_rmio, self.zz_label)
        self.zz_rdict['WHITEPOLY'] = self.WHITEPOLY
        self.WHITEINIT = RM_Register_FRC_NS_WHITEINIT(self.zz_rmio, self.zz_label)
        self.zz_rdict['WHITEINIT'] = self.WHITEINIT
        self.FECCTRL = RM_Register_FRC_NS_FECCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['FECCTRL'] = self.FECCTRL
        self.BLOCKRAMADDR = RM_Register_FRC_NS_BLOCKRAMADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['BLOCKRAMADDR'] = self.BLOCKRAMADDR
        self.CONVRAMADDR = RM_Register_FRC_NS_CONVRAMADDR(self.zz_rmio, self.zz_label)
        self.zz_rdict['CONVRAMADDR'] = self.CONVRAMADDR
        self.CTRL = RM_Register_FRC_NS_CTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['CTRL'] = self.CTRL
        self.RXCTRL = RM_Register_FRC_NS_RXCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXCTRL'] = self.RXCTRL
        self.TRAILTXDATACTRL = RM_Register_FRC_NS_TRAILTXDATACTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRAILTXDATACTRL'] = self.TRAILTXDATACTRL
        self.TRAILRXDATA = RM_Register_FRC_NS_TRAILRXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['TRAILRXDATA'] = self.TRAILRXDATA
        self.SCNT = RM_Register_FRC_NS_SCNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['SCNT'] = self.SCNT
        self.CONVGENERATOR = RM_Register_FRC_NS_CONVGENERATOR(self.zz_rmio, self.zz_label)
        self.zz_rdict['CONVGENERATOR'] = self.CONVGENERATOR
        self.PUNCTCTRL = RM_Register_FRC_NS_PUNCTCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PUNCTCTRL'] = self.PUNCTCTRL
        self.PAUSECTRL = RM_Register_FRC_NS_PAUSECTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PAUSECTRL'] = self.PAUSECTRL
        self.IF = RM_Register_FRC_NS_IF(self.zz_rmio, self.zz_label)
        self.zz_rdict['IF'] = self.IF
        self.IEN = RM_Register_FRC_NS_IEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['IEN'] = self.IEN
        self.OTACNT = RM_Register_FRC_NS_OTACNT(self.zz_rmio, self.zz_label)
        self.zz_rdict['OTACNT'] = self.OTACNT
        self.BUFFERMODE = RM_Register_FRC_NS_BUFFERMODE(self.zz_rmio, self.zz_label)
        self.zz_rdict['BUFFERMODE'] = self.BUFFERMODE
        self.SNIFFCTRL = RM_Register_FRC_NS_SNIFFCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['SNIFFCTRL'] = self.SNIFFCTRL
        self.AUXDATA = RM_Register_FRC_NS_AUXDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUXDATA'] = self.AUXDATA
        self.RAWCTRL = RM_Register_FRC_NS_RAWCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['RAWCTRL'] = self.RAWCTRL
        self.RXRAWDATA = RM_Register_FRC_NS_RXRAWDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['RXRAWDATA'] = self.RXRAWDATA
        self.PAUSEDATA = RM_Register_FRC_NS_PAUSEDATA(self.zz_rmio, self.zz_label)
        self.zz_rdict['PAUSEDATA'] = self.PAUSEDATA
        self.LIKELYCONVSTATE = RM_Register_FRC_NS_LIKELYCONVSTATE(self.zz_rmio, self.zz_label)
        self.zz_rdict['LIKELYCONVSTATE'] = self.LIKELYCONVSTATE
        self.INTELEMENTNEXT = RM_Register_FRC_NS_INTELEMENTNEXT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENTNEXT'] = self.INTELEMENTNEXT
        self.INTWRITEPOINT = RM_Register_FRC_NS_INTWRITEPOINT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTWRITEPOINT'] = self.INTWRITEPOINT
        self.INTREADPOINT = RM_Register_FRC_NS_INTREADPOINT(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTREADPOINT'] = self.INTREADPOINT
        self.AUTOCG = RM_Register_FRC_NS_AUTOCG(self.zz_rmio, self.zz_label)
        self.zz_rdict['AUTOCG'] = self.AUTOCG
        self.CGCLKSTOP = RM_Register_FRC_NS_CGCLKSTOP(self.zz_rmio, self.zz_label)
        self.zz_rdict['CGCLKSTOP'] = self.CGCLKSTOP
        self.SEQIF = RM_Register_FRC_NS_SEQIF(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQIF'] = self.SEQIF
        self.SEQIEN = RM_Register_FRC_NS_SEQIEN(self.zz_rmio, self.zz_label)
        self.zz_rdict['SEQIEN'] = self.SEQIEN
        self.WCNTCMP3 = RM_Register_FRC_NS_WCNTCMP3(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP3'] = self.WCNTCMP3
        self.BOICTRL = RM_Register_FRC_NS_BOICTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['BOICTRL'] = self.BOICTRL
        self.DSLCTRL = RM_Register_FRC_NS_DSLCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['DSLCTRL'] = self.DSLCTRL
        self.WCNTCMP4 = RM_Register_FRC_NS_WCNTCMP4(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP4'] = self.WCNTCMP4
        self.WCNTCMP5 = RM_Register_FRC_NS_WCNTCMP5(self.zz_rmio, self.zz_label)
        self.zz_rdict['WCNTCMP5'] = self.WCNTCMP5
        self.PKTBUFCTRL = RM_Register_FRC_NS_PKTBUFCTRL(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUFCTRL'] = self.PKTBUFCTRL
        self.PKTBUFSTATUS = RM_Register_FRC_NS_PKTBUFSTATUS(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUFSTATUS'] = self.PKTBUFSTATUS
        self.PKTBUF0 = RM_Register_FRC_NS_PKTBUF0(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF0'] = self.PKTBUF0
        self.PKTBUF1 = RM_Register_FRC_NS_PKTBUF1(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF1'] = self.PKTBUF1
        self.PKTBUF2 = RM_Register_FRC_NS_PKTBUF2(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF2'] = self.PKTBUF2
        self.PKTBUF3 = RM_Register_FRC_NS_PKTBUF3(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF3'] = self.PKTBUF3
        self.PKTBUF4 = RM_Register_FRC_NS_PKTBUF4(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF4'] = self.PKTBUF4
        self.PKTBUF5 = RM_Register_FRC_NS_PKTBUF5(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF5'] = self.PKTBUF5
        self.PKTBUF6 = RM_Register_FRC_NS_PKTBUF6(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF6'] = self.PKTBUF6
        self.PKTBUF7 = RM_Register_FRC_NS_PKTBUF7(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF7'] = self.PKTBUF7
        self.PKTBUF8 = RM_Register_FRC_NS_PKTBUF8(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF8'] = self.PKTBUF8
        self.PKTBUF9 = RM_Register_FRC_NS_PKTBUF9(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF9'] = self.PKTBUF9
        self.PKTBUF10 = RM_Register_FRC_NS_PKTBUF10(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF10'] = self.PKTBUF10
        self.PKTBUF11 = RM_Register_FRC_NS_PKTBUF11(self.zz_rmio, self.zz_label)
        self.zz_rdict['PKTBUF11'] = self.PKTBUF11
        self.FCD0 = RM_Register_FRC_NS_FCD0(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD0'] = self.FCD0
        self.FCD1 = RM_Register_FRC_NS_FCD1(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD1'] = self.FCD1
        self.FCD2 = RM_Register_FRC_NS_FCD2(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD2'] = self.FCD2
        self.FCD3 = RM_Register_FRC_NS_FCD3(self.zz_rmio, self.zz_label)
        self.zz_rdict['FCD3'] = self.FCD3
        self.INTELEMENT0 = RM_Register_FRC_NS_INTELEMENT0(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT0'] = self.INTELEMENT0
        self.INTELEMENT1 = RM_Register_FRC_NS_INTELEMENT1(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT1'] = self.INTELEMENT1
        self.INTELEMENT2 = RM_Register_FRC_NS_INTELEMENT2(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT2'] = self.INTELEMENT2
        self.INTELEMENT3 = RM_Register_FRC_NS_INTELEMENT3(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT3'] = self.INTELEMENT3
        self.INTELEMENT4 = RM_Register_FRC_NS_INTELEMENT4(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT4'] = self.INTELEMENT4
        self.INTELEMENT5 = RM_Register_FRC_NS_INTELEMENT5(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT5'] = self.INTELEMENT5
        self.INTELEMENT6 = RM_Register_FRC_NS_INTELEMENT6(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT6'] = self.INTELEMENT6
        self.INTELEMENT7 = RM_Register_FRC_NS_INTELEMENT7(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT7'] = self.INTELEMENT7
        self.INTELEMENT8 = RM_Register_FRC_NS_INTELEMENT8(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT8'] = self.INTELEMENT8
        self.INTELEMENT9 = RM_Register_FRC_NS_INTELEMENT9(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT9'] = self.INTELEMENT9
        self.INTELEMENT10 = RM_Register_FRC_NS_INTELEMENT10(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT10'] = self.INTELEMENT10
        self.INTELEMENT11 = RM_Register_FRC_NS_INTELEMENT11(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT11'] = self.INTELEMENT11
        self.INTELEMENT12 = RM_Register_FRC_NS_INTELEMENT12(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT12'] = self.INTELEMENT12
        self.INTELEMENT13 = RM_Register_FRC_NS_INTELEMENT13(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT13'] = self.INTELEMENT13
        self.INTELEMENT14 = RM_Register_FRC_NS_INTELEMENT14(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT14'] = self.INTELEMENT14
        self.INTELEMENT15 = RM_Register_FRC_NS_INTELEMENT15(self.zz_rmio, self.zz_label)
        self.zz_rdict['INTELEMENT15'] = self.INTELEMENT15
        self.AHBCONFIG = RM_Register_FRC_NS_AHBCONFIG(self.zz_rmio, self.zz_label)
        self.zz_rdict['AHBCONFIG'] = self.AHBCONFIG
        self.SPARE = RM_Register_FRC_NS_SPARE(self.zz_rmio, self.zz_label)
        self.zz_rdict['SPARE'] = self.SPARE
        self.__dict__['zz_frozen'] = True