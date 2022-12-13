
# -*- coding: utf-8 -*-

from . static import Base_RM_Register
from . MODEM_S_field import *


class RM_Register_MODEM_S_IPVERSION(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_IPVERSION, self).__init__(rmio, label,
            0xa8014000, 0x000,
            'IPVERSION', 'MODEM_S.IPVERSION', 'read-only',
            u"",
            0x00000002, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.IPVERSION = RM_Field_MODEM_S_IPVERSION_IPVERSION(self)
        self.zz_fdict['IPVERSION'] = self.IPVERSION
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_EN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_EN, self).__init__(rmio, label,
            0xa8014000, 0x004,
            'EN', 'MODEM_S.EN', 'read-write',
            u"",
            0x00000000, 0x00000001,
            0x00001000, 0x00002000,
            0x00003000)

        self.EN = RM_Field_MODEM_S_EN_EN(self)
        self.zz_fdict['EN'] = self.EN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_IF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_IF, self).__init__(rmio, label,
            0xa8014000, 0x008,
            'IF', 'MODEM_S.IF', 'read-write',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TXFRAMESENT = RM_Field_MODEM_S_IF_TXFRAMESENT(self)
        self.zz_fdict['TXFRAMESENT'] = self.TXFRAMESENT
        self.TXSYNCSENT = RM_Field_MODEM_S_IF_TXSYNCSENT(self)
        self.zz_fdict['TXSYNCSENT'] = self.TXSYNCSENT
        self.TXPRESENT = RM_Field_MODEM_S_IF_TXPRESENT(self)
        self.zz_fdict['TXPRESENT'] = self.TXPRESENT
        self.TXRAMPDONE = RM_Field_MODEM_S_IF_TXRAMPDONE(self)
        self.zz_fdict['TXRAMPDONE'] = self.TXRAMPDONE
        self.LDTNOARR = RM_Field_MODEM_S_IF_LDTNOARR(self)
        self.zz_fdict['LDTNOARR'] = self.LDTNOARR
        self.PHDSADET = RM_Field_MODEM_S_IF_PHDSADET(self)
        self.zz_fdict['PHDSADET'] = self.PHDSADET
        self.PHYUNCODEDET = RM_Field_MODEM_S_IF_PHYUNCODEDET(self)
        self.zz_fdict['PHYUNCODEDET'] = self.PHYUNCODEDET
        self.PHYCODEDET = RM_Field_MODEM_S_IF_PHYCODEDET(self)
        self.zz_fdict['PHYCODEDET'] = self.PHYCODEDET
        self.RXTIMDET = RM_Field_MODEM_S_IF_RXTIMDET(self)
        self.zz_fdict['RXTIMDET'] = self.RXTIMDET
        self.RXPREDET = RM_Field_MODEM_S_IF_RXPREDET(self)
        self.zz_fdict['RXPREDET'] = self.RXPREDET
        self.RXFRAMEDET0 = RM_Field_MODEM_S_IF_RXFRAMEDET0(self)
        self.zz_fdict['RXFRAMEDET0'] = self.RXFRAMEDET0
        self.RXFRAMEDET1 = RM_Field_MODEM_S_IF_RXFRAMEDET1(self)
        self.zz_fdict['RXFRAMEDET1'] = self.RXFRAMEDET1
        self.RXTIMLOST = RM_Field_MODEM_S_IF_RXTIMLOST(self)
        self.zz_fdict['RXTIMLOST'] = self.RXTIMLOST
        self.RXPRELOST = RM_Field_MODEM_S_IF_RXPRELOST(self)
        self.zz_fdict['RXPRELOST'] = self.RXPRELOST
        self.RXFRAMEDETOF = RM_Field_MODEM_S_IF_RXFRAMEDETOF(self)
        self.zz_fdict['RXFRAMEDETOF'] = self.RXFRAMEDETOF
        self.RXTIMNF = RM_Field_MODEM_S_IF_RXTIMNF(self)
        self.zz_fdict['RXTIMNF'] = self.RXTIMNF
        self.FRCTIMOUT = RM_Field_MODEM_S_IF_FRCTIMOUT(self)
        self.zz_fdict['FRCTIMOUT'] = self.FRCTIMOUT
        self.ETS = RM_Field_MODEM_S_IF_ETS(self)
        self.zz_fdict['ETS'] = self.ETS
        self.CFGANTPATTRD = RM_Field_MODEM_S_IF_CFGANTPATTRD(self)
        self.zz_fdict['CFGANTPATTRD'] = self.CFGANTPATTRD
        self.RXRESTARTRSSIMAPRE = RM_Field_MODEM_S_IF_RXRESTARTRSSIMAPRE(self)
        self.zz_fdict['RXRESTARTRSSIMAPRE'] = self.RXRESTARTRSSIMAPRE
        self.RXRESTARTRSSIMASYNC = RM_Field_MODEM_S_IF_RXRESTARTRSSIMASYNC(self)
        self.zz_fdict['RXRESTARTRSSIMASYNC'] = self.RXRESTARTRSSIMASYNC
        self.SQDET = RM_Field_MODEM_S_IF_SQDET(self)
        self.zz_fdict['SQDET'] = self.SQDET
        self.SQNOTDET = RM_Field_MODEM_S_IF_SQNOTDET(self)
        self.zz_fdict['SQNOTDET'] = self.SQNOTDET
        self.ANTDIVRDY = RM_Field_MODEM_S_IF_ANTDIVRDY(self)
        self.zz_fdict['ANTDIVRDY'] = self.ANTDIVRDY
        self.SOFTRESETDONE = RM_Field_MODEM_S_IF_SOFTRESETDONE(self)
        self.zz_fdict['SOFTRESETDONE'] = self.SOFTRESETDONE
        self.SQPRENOTDET = RM_Field_MODEM_S_IF_SQPRENOTDET(self)
        self.zz_fdict['SQPRENOTDET'] = self.SQPRENOTDET
        self.SQFRAMENOTDET = RM_Field_MODEM_S_IF_SQFRAMENOTDET(self)
        self.zz_fdict['SQFRAMENOTDET'] = self.SQFRAMENOTDET
        self.SQAFCOUTOFBAND = RM_Field_MODEM_S_IF_SQAFCOUTOFBAND(self)
        self.zz_fdict['SQAFCOUTOFBAND'] = self.SQAFCOUTOFBAND
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_IEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_IEN, self).__init__(rmio, label,
            0xa8014000, 0x00C,
            'IEN', 'MODEM_S.IEN', 'read-write',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TXFRAMESENT = RM_Field_MODEM_S_IEN_TXFRAMESENT(self)
        self.zz_fdict['TXFRAMESENT'] = self.TXFRAMESENT
        self.TXSYNCSENT = RM_Field_MODEM_S_IEN_TXSYNCSENT(self)
        self.zz_fdict['TXSYNCSENT'] = self.TXSYNCSENT
        self.TXPRESENT = RM_Field_MODEM_S_IEN_TXPRESENT(self)
        self.zz_fdict['TXPRESENT'] = self.TXPRESENT
        self.TXRAMPDONE = RM_Field_MODEM_S_IEN_TXRAMPDONE(self)
        self.zz_fdict['TXRAMPDONE'] = self.TXRAMPDONE
        self.LDTNOARR = RM_Field_MODEM_S_IEN_LDTNOARR(self)
        self.zz_fdict['LDTNOARR'] = self.LDTNOARR
        self.PHDSADET = RM_Field_MODEM_S_IEN_PHDSADET(self)
        self.zz_fdict['PHDSADET'] = self.PHDSADET
        self.PHYUNCODEDET = RM_Field_MODEM_S_IEN_PHYUNCODEDET(self)
        self.zz_fdict['PHYUNCODEDET'] = self.PHYUNCODEDET
        self.PHYCODEDET = RM_Field_MODEM_S_IEN_PHYCODEDET(self)
        self.zz_fdict['PHYCODEDET'] = self.PHYCODEDET
        self.RXTIMDET = RM_Field_MODEM_S_IEN_RXTIMDET(self)
        self.zz_fdict['RXTIMDET'] = self.RXTIMDET
        self.RXPREDET = RM_Field_MODEM_S_IEN_RXPREDET(self)
        self.zz_fdict['RXPREDET'] = self.RXPREDET
        self.RXFRAMEDET0 = RM_Field_MODEM_S_IEN_RXFRAMEDET0(self)
        self.zz_fdict['RXFRAMEDET0'] = self.RXFRAMEDET0
        self.RXFRAMEDET1 = RM_Field_MODEM_S_IEN_RXFRAMEDET1(self)
        self.zz_fdict['RXFRAMEDET1'] = self.RXFRAMEDET1
        self.RXTIMLOST = RM_Field_MODEM_S_IEN_RXTIMLOST(self)
        self.zz_fdict['RXTIMLOST'] = self.RXTIMLOST
        self.RXPRELOST = RM_Field_MODEM_S_IEN_RXPRELOST(self)
        self.zz_fdict['RXPRELOST'] = self.RXPRELOST
        self.RXFRAMEDETOF = RM_Field_MODEM_S_IEN_RXFRAMEDETOF(self)
        self.zz_fdict['RXFRAMEDETOF'] = self.RXFRAMEDETOF
        self.RXTIMNF = RM_Field_MODEM_S_IEN_RXTIMNF(self)
        self.zz_fdict['RXTIMNF'] = self.RXTIMNF
        self.FRCTIMOUT = RM_Field_MODEM_S_IEN_FRCTIMOUT(self)
        self.zz_fdict['FRCTIMOUT'] = self.FRCTIMOUT
        self.ETS = RM_Field_MODEM_S_IEN_ETS(self)
        self.zz_fdict['ETS'] = self.ETS
        self.CFGANTPATTRD = RM_Field_MODEM_S_IEN_CFGANTPATTRD(self)
        self.zz_fdict['CFGANTPATTRD'] = self.CFGANTPATTRD
        self.RXRESTARTRSSIMAPRE = RM_Field_MODEM_S_IEN_RXRESTARTRSSIMAPRE(self)
        self.zz_fdict['RXRESTARTRSSIMAPRE'] = self.RXRESTARTRSSIMAPRE
        self.RXRESTARTRSSIMASYNC = RM_Field_MODEM_S_IEN_RXRESTARTRSSIMASYNC(self)
        self.zz_fdict['RXRESTARTRSSIMASYNC'] = self.RXRESTARTRSSIMASYNC
        self.SQDET = RM_Field_MODEM_S_IEN_SQDET(self)
        self.zz_fdict['SQDET'] = self.SQDET
        self.SQNOTDET = RM_Field_MODEM_S_IEN_SQNOTDET(self)
        self.zz_fdict['SQNOTDET'] = self.SQNOTDET
        self.ANTDIVRDY = RM_Field_MODEM_S_IEN_ANTDIVRDY(self)
        self.zz_fdict['ANTDIVRDY'] = self.ANTDIVRDY
        self.SOFTRESETDONE = RM_Field_MODEM_S_IEN_SOFTRESETDONE(self)
        self.zz_fdict['SOFTRESETDONE'] = self.SOFTRESETDONE
        self.SQPRENOTDET = RM_Field_MODEM_S_IEN_SQPRENOTDET(self)
        self.zz_fdict['SQPRENOTDET'] = self.SQPRENOTDET
        self.SQFRAMENOTDET = RM_Field_MODEM_S_IEN_SQFRAMENOTDET(self)
        self.zz_fdict['SQFRAMENOTDET'] = self.SQFRAMENOTDET
        self.SQAFCOUTOFBAND = RM_Field_MODEM_S_IEN_SQAFCOUTOFBAND(self)
        self.zz_fdict['SQAFCOUTOFBAND'] = self.SQAFCOUTOFBAND
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SEQIF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SEQIF, self).__init__(rmio, label,
            0xa8014000, 0x010,
            'SEQIF', 'MODEM_S.SEQIF', 'read-write',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TXFRAMESENT = RM_Field_MODEM_S_SEQIF_TXFRAMESENT(self)
        self.zz_fdict['TXFRAMESENT'] = self.TXFRAMESENT
        self.TXSYNCSENT = RM_Field_MODEM_S_SEQIF_TXSYNCSENT(self)
        self.zz_fdict['TXSYNCSENT'] = self.TXSYNCSENT
        self.TXPRESENT = RM_Field_MODEM_S_SEQIF_TXPRESENT(self)
        self.zz_fdict['TXPRESENT'] = self.TXPRESENT
        self.TXRAMPDONE = RM_Field_MODEM_S_SEQIF_TXRAMPDONE(self)
        self.zz_fdict['TXRAMPDONE'] = self.TXRAMPDONE
        self.LDTNOARR = RM_Field_MODEM_S_SEQIF_LDTNOARR(self)
        self.zz_fdict['LDTNOARR'] = self.LDTNOARR
        self.PHDSADET = RM_Field_MODEM_S_SEQIF_PHDSADET(self)
        self.zz_fdict['PHDSADET'] = self.PHDSADET
        self.PHYUNCODEDET = RM_Field_MODEM_S_SEQIF_PHYUNCODEDET(self)
        self.zz_fdict['PHYUNCODEDET'] = self.PHYUNCODEDET
        self.PHYCODEDET = RM_Field_MODEM_S_SEQIF_PHYCODEDET(self)
        self.zz_fdict['PHYCODEDET'] = self.PHYCODEDET
        self.RXTIMDET = RM_Field_MODEM_S_SEQIF_RXTIMDET(self)
        self.zz_fdict['RXTIMDET'] = self.RXTIMDET
        self.RXPREDET = RM_Field_MODEM_S_SEQIF_RXPREDET(self)
        self.zz_fdict['RXPREDET'] = self.RXPREDET
        self.RXFRAMEDET0 = RM_Field_MODEM_S_SEQIF_RXFRAMEDET0(self)
        self.zz_fdict['RXFRAMEDET0'] = self.RXFRAMEDET0
        self.RXFRAMEDET1 = RM_Field_MODEM_S_SEQIF_RXFRAMEDET1(self)
        self.zz_fdict['RXFRAMEDET1'] = self.RXFRAMEDET1
        self.RXTIMLOST = RM_Field_MODEM_S_SEQIF_RXTIMLOST(self)
        self.zz_fdict['RXTIMLOST'] = self.RXTIMLOST
        self.RXPRELOST = RM_Field_MODEM_S_SEQIF_RXPRELOST(self)
        self.zz_fdict['RXPRELOST'] = self.RXPRELOST
        self.RXFRAMEDETOF = RM_Field_MODEM_S_SEQIF_RXFRAMEDETOF(self)
        self.zz_fdict['RXFRAMEDETOF'] = self.RXFRAMEDETOF
        self.RXTIMNF = RM_Field_MODEM_S_SEQIF_RXTIMNF(self)
        self.zz_fdict['RXTIMNF'] = self.RXTIMNF
        self.FRCTIMOUT = RM_Field_MODEM_S_SEQIF_FRCTIMOUT(self)
        self.zz_fdict['FRCTIMOUT'] = self.FRCTIMOUT
        self.ETS = RM_Field_MODEM_S_SEQIF_ETS(self)
        self.zz_fdict['ETS'] = self.ETS
        self.CFGANTPATTRD = RM_Field_MODEM_S_SEQIF_CFGANTPATTRD(self)
        self.zz_fdict['CFGANTPATTRD'] = self.CFGANTPATTRD
        self.RXRESTARTRSSIMAPRE = RM_Field_MODEM_S_SEQIF_RXRESTARTRSSIMAPRE(self)
        self.zz_fdict['RXRESTARTRSSIMAPRE'] = self.RXRESTARTRSSIMAPRE
        self.RXRESTARTRSSIMASYNC = RM_Field_MODEM_S_SEQIF_RXRESTARTRSSIMASYNC(self)
        self.zz_fdict['RXRESTARTRSSIMASYNC'] = self.RXRESTARTRSSIMASYNC
        self.SQDET = RM_Field_MODEM_S_SEQIF_SQDET(self)
        self.zz_fdict['SQDET'] = self.SQDET
        self.SQNOTDET = RM_Field_MODEM_S_SEQIF_SQNOTDET(self)
        self.zz_fdict['SQNOTDET'] = self.SQNOTDET
        self.ANTDIVRDY = RM_Field_MODEM_S_SEQIF_ANTDIVRDY(self)
        self.zz_fdict['ANTDIVRDY'] = self.ANTDIVRDY
        self.SOFTRESETDONE = RM_Field_MODEM_S_SEQIF_SOFTRESETDONE(self)
        self.zz_fdict['SOFTRESETDONE'] = self.SOFTRESETDONE
        self.SQPRENOTDET = RM_Field_MODEM_S_SEQIF_SQPRENOTDET(self)
        self.zz_fdict['SQPRENOTDET'] = self.SQPRENOTDET
        self.SQFRAMENOTDET = RM_Field_MODEM_S_SEQIF_SQFRAMENOTDET(self)
        self.zz_fdict['SQFRAMENOTDET'] = self.SQFRAMENOTDET
        self.SQAFCOUTOFBAND = RM_Field_MODEM_S_SEQIF_SQAFCOUTOFBAND(self)
        self.zz_fdict['SQAFCOUTOFBAND'] = self.SQAFCOUTOFBAND
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SEQIEN(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SEQIEN, self).__init__(rmio, label,
            0xa8014000, 0x014,
            'SEQIEN', 'MODEM_S.SEQIEN', 'read-write',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TXFRAMESENT = RM_Field_MODEM_S_SEQIEN_TXFRAMESENT(self)
        self.zz_fdict['TXFRAMESENT'] = self.TXFRAMESENT
        self.TXSYNCSENT = RM_Field_MODEM_S_SEQIEN_TXSYNCSENT(self)
        self.zz_fdict['TXSYNCSENT'] = self.TXSYNCSENT
        self.TXPRESENT = RM_Field_MODEM_S_SEQIEN_TXPRESENT(self)
        self.zz_fdict['TXPRESENT'] = self.TXPRESENT
        self.TXRAMPDONE = RM_Field_MODEM_S_SEQIEN_TXRAMPDONE(self)
        self.zz_fdict['TXRAMPDONE'] = self.TXRAMPDONE
        self.LDTNOARR = RM_Field_MODEM_S_SEQIEN_LDTNOARR(self)
        self.zz_fdict['LDTNOARR'] = self.LDTNOARR
        self.PHDSADET = RM_Field_MODEM_S_SEQIEN_PHDSADET(self)
        self.zz_fdict['PHDSADET'] = self.PHDSADET
        self.PHYUNCODEDET = RM_Field_MODEM_S_SEQIEN_PHYUNCODEDET(self)
        self.zz_fdict['PHYUNCODEDET'] = self.PHYUNCODEDET
        self.PHYCODEDET = RM_Field_MODEM_S_SEQIEN_PHYCODEDET(self)
        self.zz_fdict['PHYCODEDET'] = self.PHYCODEDET
        self.RXTIMDET = RM_Field_MODEM_S_SEQIEN_RXTIMDET(self)
        self.zz_fdict['RXTIMDET'] = self.RXTIMDET
        self.RXPREDET = RM_Field_MODEM_S_SEQIEN_RXPREDET(self)
        self.zz_fdict['RXPREDET'] = self.RXPREDET
        self.RXFRAMEDET0 = RM_Field_MODEM_S_SEQIEN_RXFRAMEDET0(self)
        self.zz_fdict['RXFRAMEDET0'] = self.RXFRAMEDET0
        self.RXFRAMEDET1 = RM_Field_MODEM_S_SEQIEN_RXFRAMEDET1(self)
        self.zz_fdict['RXFRAMEDET1'] = self.RXFRAMEDET1
        self.RXTIMLOST = RM_Field_MODEM_S_SEQIEN_RXTIMLOST(self)
        self.zz_fdict['RXTIMLOST'] = self.RXTIMLOST
        self.RXPRELOST = RM_Field_MODEM_S_SEQIEN_RXPRELOST(self)
        self.zz_fdict['RXPRELOST'] = self.RXPRELOST
        self.RXFRAMEDETOF = RM_Field_MODEM_S_SEQIEN_RXFRAMEDETOF(self)
        self.zz_fdict['RXFRAMEDETOF'] = self.RXFRAMEDETOF
        self.RXTIMNF = RM_Field_MODEM_S_SEQIEN_RXTIMNF(self)
        self.zz_fdict['RXTIMNF'] = self.RXTIMNF
        self.FRCTIMOUT = RM_Field_MODEM_S_SEQIEN_FRCTIMOUT(self)
        self.zz_fdict['FRCTIMOUT'] = self.FRCTIMOUT
        self.ETS = RM_Field_MODEM_S_SEQIEN_ETS(self)
        self.zz_fdict['ETS'] = self.ETS
        self.CFGANTPATTRD = RM_Field_MODEM_S_SEQIEN_CFGANTPATTRD(self)
        self.zz_fdict['CFGANTPATTRD'] = self.CFGANTPATTRD
        self.RXRESTARTRSSIMAPRE = RM_Field_MODEM_S_SEQIEN_RXRESTARTRSSIMAPRE(self)
        self.zz_fdict['RXRESTARTRSSIMAPRE'] = self.RXRESTARTRSSIMAPRE
        self.RXRESTARTRSSIMASYNC = RM_Field_MODEM_S_SEQIEN_RXRESTARTRSSIMASYNC(self)
        self.zz_fdict['RXRESTARTRSSIMASYNC'] = self.RXRESTARTRSSIMASYNC
        self.SQDET = RM_Field_MODEM_S_SEQIEN_SQDET(self)
        self.zz_fdict['SQDET'] = self.SQDET
        self.SQNOTDET = RM_Field_MODEM_S_SEQIEN_SQNOTDET(self)
        self.zz_fdict['SQNOTDET'] = self.SQNOTDET
        self.ANTDIVRDY = RM_Field_MODEM_S_SEQIEN_ANTDIVRDY(self)
        self.zz_fdict['ANTDIVRDY'] = self.ANTDIVRDY
        self.SOFTRESETDONE = RM_Field_MODEM_S_SEQIEN_SOFTRESETDONE(self)
        self.zz_fdict['SOFTRESETDONE'] = self.SOFTRESETDONE
        self.SQPRENOTDET = RM_Field_MODEM_S_SEQIEN_SQPRENOTDET(self)
        self.zz_fdict['SQPRENOTDET'] = self.SQPRENOTDET
        self.SQFRAMENOTDET = RM_Field_MODEM_S_SEQIEN_SQFRAMENOTDET(self)
        self.zz_fdict['SQFRAMENOTDET'] = self.SQFRAMENOTDET
        self.SQAFCOUTOFBAND = RM_Field_MODEM_S_SEQIEN_SQAFCOUTOFBAND(self)
        self.zz_fdict['SQAFCOUTOFBAND'] = self.SQAFCOUTOFBAND
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_STATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_STATUS, self).__init__(rmio, label,
            0xa8014000, 0x018,
            'STATUS', 'MODEM_S.STATUS', 'read-only',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DEMODSTATE = RM_Field_MODEM_S_STATUS_DEMODSTATE(self)
        self.zz_fdict['DEMODSTATE'] = self.DEMODSTATE
        self.BCRCFEDSADET = RM_Field_MODEM_S_STATUS_BCRCFEDSADET(self)
        self.zz_fdict['BCRCFEDSADET'] = self.BCRCFEDSADET
        self.FRAMEDETID = RM_Field_MODEM_S_STATUS_FRAMEDETID(self)
        self.zz_fdict['FRAMEDETID'] = self.FRAMEDETID
        self.ANTSEL = RM_Field_MODEM_S_STATUS_ANTSEL(self)
        self.zz_fdict['ANTSEL'] = self.ANTSEL
        self.TIMSEQINV = RM_Field_MODEM_S_STATUS_TIMSEQINV(self)
        self.zz_fdict['TIMSEQINV'] = self.TIMSEQINV
        self.TIMLOSTCAUSE = RM_Field_MODEM_S_STATUS_TIMLOSTCAUSE(self)
        self.zz_fdict['TIMLOSTCAUSE'] = self.TIMLOSTCAUSE
        self.DSADETECTED = RM_Field_MODEM_S_STATUS_DSADETECTED(self)
        self.zz_fdict['DSADETECTED'] = self.DSADETECTED
        self.DSAFREQESTDONE = RM_Field_MODEM_S_STATUS_DSAFREQESTDONE(self)
        self.zz_fdict['DSAFREQESTDONE'] = self.DSAFREQESTDONE
        self.VITERBIDEMODTIMDET = RM_Field_MODEM_S_STATUS_VITERBIDEMODTIMDET(self)
        self.zz_fdict['VITERBIDEMODTIMDET'] = self.VITERBIDEMODTIMDET
        self.VITERBIDEMODFRAMEDET = RM_Field_MODEM_S_STATUS_VITERBIDEMODFRAMEDET(self)
        self.zz_fdict['VITERBIDEMODFRAMEDET'] = self.VITERBIDEMODFRAMEDET
        self.STAMPSTATE = RM_Field_MODEM_S_STATUS_STAMPSTATE(self)
        self.zz_fdict['STAMPSTATE'] = self.STAMPSTATE
        self.TRECSDSAADET = RM_Field_MODEM_S_STATUS_TRECSDSAADET(self)
        self.zz_fdict['TRECSDSAADET'] = self.TRECSDSAADET
        self.CORR = RM_Field_MODEM_S_STATUS_CORR(self)
        self.zz_fdict['CORR'] = self.CORR
        self.WEAKSYMBOLS = RM_Field_MODEM_S_STATUS_WEAKSYMBOLS(self)
        self.zz_fdict['WEAKSYMBOLS'] = self.WEAKSYMBOLS
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_STATUS2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_STATUS2, self).__init__(rmio, label,
            0xa8014000, 0x01C,
            'STATUS2', 'MODEM_S.STATUS2', 'read-only',
            u"",
            0x00000000, 0xFFFCFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CHPWRACCUMUX = RM_Field_MODEM_S_STATUS2_CHPWRACCUMUX(self)
        self.zz_fdict['CHPWRACCUMUX'] = self.CHPWRACCUMUX
        self.BBSSMUX = RM_Field_MODEM_S_STATUS2_BBSSMUX(self)
        self.zz_fdict['BBSSMUX'] = self.BBSSMUX
        self.LRBLECI = RM_Field_MODEM_S_STATUS2_LRBLECI(self)
        self.zz_fdict['LRBLECI'] = self.LRBLECI
        self.UNCODEDPHY = RM_Field_MODEM_S_STATUS2_UNCODEDPHY(self)
        self.zz_fdict['UNCODEDPHY'] = self.UNCODEDPHY
        self.CODEDPHY = RM_Field_MODEM_S_STATUS2_CODEDPHY(self)
        self.zz_fdict['CODEDPHY'] = self.CODEDPHY
        self.RTCOST = RM_Field_MODEM_S_STATUS2_RTCOST(self)
        self.zz_fdict['RTCOST'] = self.RTCOST
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_STATUS3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_STATUS3, self).__init__(rmio, label,
            0xa8014000, 0x020,
            'STATUS3', 'MODEM_S.STATUS3', 'read-only',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.BBPFOUTABS1 = RM_Field_MODEM_S_STATUS3_BBPFOUTABS1(self)
        self.zz_fdict['BBPFOUTABS1'] = self.BBPFOUTABS1
        self.BBPFOUTABS = RM_Field_MODEM_S_STATUS3_BBPFOUTABS(self)
        self.zz_fdict['BBPFOUTABS'] = self.BBPFOUTABS
        self.LRDSALIVE = RM_Field_MODEM_S_STATUS3_LRDSALIVE(self)
        self.zz_fdict['LRDSALIVE'] = self.LRDSALIVE
        self.COHDSALIVE = RM_Field_MODEM_S_STATUS3_COHDSALIVE(self)
        self.zz_fdict['COHDSALIVE'] = self.COHDSALIVE
        self.LRDSADET = RM_Field_MODEM_S_STATUS3_LRDSADET(self)
        self.zz_fdict['LRDSADET'] = self.LRDSADET
        self.COHDSADET = RM_Field_MODEM_S_STATUS3_COHDSADET(self)
        self.zz_fdict['COHDSADET'] = self.COHDSADET
        self.SYNCSECPEAKABTH = RM_Field_MODEM_S_STATUS3_SYNCSECPEAKABTH(self)
        self.zz_fdict['SYNCSECPEAKABTH'] = self.SYNCSECPEAKABTH
        self.SOFTRSTDONE = RM_Field_MODEM_S_STATUS3_SOFTRSTDONE(self)
        self.zz_fdict['SOFTRSTDONE'] = self.SOFTRSTDONE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_STATUS4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_STATUS4, self).__init__(rmio, label,
            0xa8014000, 0x024,
            'STATUS4', 'MODEM_S.STATUS4', 'read-only',
            u"",
            0x00000000, 0x01FF01FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANT0RSSI = RM_Field_MODEM_S_STATUS4_ANT0RSSI(self)
        self.zz_fdict['ANT0RSSI'] = self.ANT0RSSI
        self.ANT1RSSI = RM_Field_MODEM_S_STATUS4_ANT1RSSI(self)
        self.zz_fdict['ANT1RSSI'] = self.ANT1RSSI
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_STATUS5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_STATUS5, self).__init__(rmio, label,
            0xa8014000, 0x028,
            'STATUS5', 'MODEM_S.STATUS5', 'read-only',
            u"",
            0x00000000, 0x000001FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RXRESTARTMAFLTDOUT = RM_Field_MODEM_S_STATUS5_RXRESTARTMAFLTDOUT(self)
        self.zz_fdict['RXRESTARTMAFLTDOUT'] = self.RXRESTARTMAFLTDOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_STATUS6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_STATUS6, self).__init__(rmio, label,
            0xa8014000, 0x02C,
            'STATUS6', 'MODEM_S.STATUS6', 'read-only',
            u"",
            0x00000000, 0xC00FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANT0CORR = RM_Field_MODEM_S_STATUS6_ANT0CORR(self)
        self.zz_fdict['ANT0CORR'] = self.ANT0CORR
        self.ANT1CORR = RM_Field_MODEM_S_STATUS6_ANT1CORR(self)
        self.zz_fdict['ANT1CORR'] = self.ANT1CORR
        self.ANT0OUT = RM_Field_MODEM_S_STATUS6_ANT0OUT(self)
        self.zz_fdict['ANT0OUT'] = self.ANT0OUT
        self.ANT1OUT = RM_Field_MODEM_S_STATUS6_ANT1OUT(self)
        self.zz_fdict['ANT1OUT'] = self.ANT1OUT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_STATUS7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_STATUS7, self).__init__(rmio, label,
            0xa8014000, 0x030,
            'STATUS7', 'MODEM_S.STATUS7', 'read-only',
            u"",
            0x00000000, 0xBFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.FDEVEST = RM_Field_MODEM_S_STATUS7_FDEVEST(self)
        self.zz_fdict['FDEVEST'] = self.FDEVEST
        self.DEMODSOFT = RM_Field_MODEM_S_STATUS7_DEMODSOFT(self)
        self.zz_fdict['DEMODSOFT'] = self.DEMODSOFT
        self.CFEPHDIFF = RM_Field_MODEM_S_STATUS7_CFEPHDIFF(self)
        self.zz_fdict['CFEPHDIFF'] = self.CFEPHDIFF
        self.MINCOSTPASS = RM_Field_MODEM_S_STATUS7_MINCOSTPASS(self)
        self.zz_fdict['MINCOSTPASS'] = self.MINCOSTPASS
        self.CFEDSADET = RM_Field_MODEM_S_STATUS7_CFEDSADET(self)
        self.zz_fdict['CFEDSADET'] = self.CFEDSADET
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_TIMDETSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_TIMDETSTATUS, self).__init__(rmio, label,
            0xa8014000, 0x034,
            'TIMDETSTATUS', 'MODEM_S.TIMDETSTATUS', 'read-only',
            u"",
            0x00000000, 0x1F0FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TIMDETCORR = RM_Field_MODEM_S_TIMDETSTATUS_TIMDETCORR(self)
        self.zz_fdict['TIMDETCORR'] = self.TIMDETCORR
        self.TIMDETFREQOFFEST = RM_Field_MODEM_S_TIMDETSTATUS_TIMDETFREQOFFEST(self)
        self.zz_fdict['TIMDETFREQOFFEST'] = self.TIMDETFREQOFFEST
        self.TIMDETPREERRORS = RM_Field_MODEM_S_TIMDETSTATUS_TIMDETPREERRORS(self)
        self.zz_fdict['TIMDETPREERRORS'] = self.TIMDETPREERRORS
        self.TIMDETPASS = RM_Field_MODEM_S_TIMDETSTATUS_TIMDETPASS(self)
        self.zz_fdict['TIMDETPASS'] = self.TIMDETPASS
        self.TIMDETINDEX = RM_Field_MODEM_S_TIMDETSTATUS_TIMDETINDEX(self)
        self.zz_fdict['TIMDETINDEX'] = self.TIMDETINDEX
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_FSMSTATUS(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_FSMSTATUS, self).__init__(rmio, label,
            0xa8014000, 0x038,
            'FSMSTATUS', 'MODEM_S.FSMSTATUS', 'read-only',
            u"",
            0x00000000, 0x00FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DETSTATE = RM_Field_MODEM_S_FSMSTATUS_DETSTATE(self)
        self.zz_fdict['DETSTATE'] = self.DETSTATE
        self.DSASTATE = RM_Field_MODEM_S_FSMSTATUS_DSASTATE(self)
        self.zz_fdict['DSASTATE'] = self.DSASTATE
        self.LRBLESTATE = RM_Field_MODEM_S_FSMSTATUS_LRBLESTATE(self)
        self.zz_fdict['LRBLESTATE'] = self.LRBLESTATE
        self.NBBLESTATE = RM_Field_MODEM_S_FSMSTATUS_NBBLESTATE(self)
        self.zz_fdict['NBBLESTATE'] = self.NBBLESTATE
        self.ANTDIVSTATE = RM_Field_MODEM_S_FSMSTATUS_ANTDIVSTATE(self)
        self.zz_fdict['ANTDIVSTATE'] = self.ANTDIVSTATE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_FREQOFFEST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_FREQOFFEST, self).__init__(rmio, label,
            0xa8014000, 0x03C,
            'FREQOFFEST', 'MODEM_S.FREQOFFEST', 'read-only',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.FREQOFFEST = RM_Field_MODEM_S_FREQOFFEST_FREQOFFEST(self)
        self.zz_fdict['FREQOFFEST'] = self.FREQOFFEST
        self.CORRVAL = RM_Field_MODEM_S_FREQOFFEST_CORRVAL(self)
        self.zz_fdict['CORRVAL'] = self.CORRVAL
        self.SOFTVAL = RM_Field_MODEM_S_FREQOFFEST_SOFTVAL(self)
        self.zz_fdict['SOFTVAL'] = self.SOFTVAL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_AFCADJRX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_AFCADJRX, self).__init__(rmio, label,
            0xa8014000, 0x040,
            'AFCADJRX', 'MODEM_S.AFCADJRX', 'read-write',
            u"",
            0x00000000, 0xF1F7FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.AFCADJRX = RM_Field_MODEM_S_AFCADJRX_AFCADJRX(self)
        self.zz_fdict['AFCADJRX'] = self.AFCADJRX
        self.AFCSCALEM = RM_Field_MODEM_S_AFCADJRX_AFCSCALEM(self)
        self.zz_fdict['AFCSCALEM'] = self.AFCSCALEM
        self.AFCSCALEE = RM_Field_MODEM_S_AFCADJRX_AFCSCALEE(self)
        self.zz_fdict['AFCSCALEE'] = self.AFCSCALEE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_AFCADJTX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_AFCADJTX, self).__init__(rmio, label,
            0xa8014000, 0x044,
            'AFCADJTX', 'MODEM_S.AFCADJTX', 'read-write',
            u"",
            0x00000000, 0xF1F7FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.AFCADJTX = RM_Field_MODEM_S_AFCADJTX_AFCADJTX(self)
        self.zz_fdict['AFCADJTX'] = self.AFCADJTX
        self.AFCSCALEM = RM_Field_MODEM_S_AFCADJTX_AFCSCALEM(self)
        self.zz_fdict['AFCSCALEM'] = self.AFCSCALEM
        self.AFCSCALEE = RM_Field_MODEM_S_AFCADJTX_AFCSCALEE(self)
        self.zz_fdict['AFCSCALEE'] = self.AFCSCALEE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_MIXCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_MIXCTRL, self).__init__(rmio, label,
            0xa8014000, 0x048,
            'MIXCTRL', 'MODEM_S.MIXCTRL', 'read-write',
            u"",
            0x00000000, 0x00000010,
            0x00001000, 0x00002000,
            0x00003000)

        self.DIGIQSWAPEN = RM_Field_MODEM_S_MIXCTRL_DIGIQSWAPEN(self)
        self.zz_fdict['DIGIQSWAPEN'] = self.DIGIQSWAPEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CTRL0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CTRL0, self).__init__(rmio, label,
            0xa8014000, 0x04C,
            'CTRL0', 'MODEM_S.CTRL0', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.FDM0DIFFDIS = RM_Field_MODEM_S_CTRL0_FDM0DIFFDIS(self)
        self.zz_fdict['FDM0DIFFDIS'] = self.FDM0DIFFDIS
        self.MAPFSK = RM_Field_MODEM_S_CTRL0_MAPFSK(self)
        self.zz_fdict['MAPFSK'] = self.MAPFSK
        self.CODING = RM_Field_MODEM_S_CTRL0_CODING(self)
        self.zz_fdict['CODING'] = self.CODING
        self.MODFORMAT = RM_Field_MODEM_S_CTRL0_MODFORMAT(self)
        self.zz_fdict['MODFORMAT'] = self.MODFORMAT
        self.DUALCORROPTDIS = RM_Field_MODEM_S_CTRL0_DUALCORROPTDIS(self)
        self.zz_fdict['DUALCORROPTDIS'] = self.DUALCORROPTDIS
        self.OOKASYNCPIN = RM_Field_MODEM_S_CTRL0_OOKASYNCPIN(self)
        self.zz_fdict['OOKASYNCPIN'] = self.OOKASYNCPIN
        self.DSSSLEN = RM_Field_MODEM_S_CTRL0_DSSSLEN(self)
        self.zz_fdict['DSSSLEN'] = self.DSSSLEN
        self.DSSSSHIFTS = RM_Field_MODEM_S_CTRL0_DSSSSHIFTS(self)
        self.zz_fdict['DSSSSHIFTS'] = self.DSSSSHIFTS
        self.DSSSDOUBLE = RM_Field_MODEM_S_CTRL0_DSSSDOUBLE(self)
        self.zz_fdict['DSSSDOUBLE'] = self.DSSSDOUBLE
        self.DETDIS = RM_Field_MODEM_S_CTRL0_DETDIS(self)
        self.zz_fdict['DETDIS'] = self.DETDIS
        self.DIFFENCMODE = RM_Field_MODEM_S_CTRL0_DIFFENCMODE(self)
        self.zz_fdict['DIFFENCMODE'] = self.DIFFENCMODE
        self.SHAPING = RM_Field_MODEM_S_CTRL0_SHAPING(self)
        self.zz_fdict['SHAPING'] = self.SHAPING
        self.DEMODRAWDATASEL = RM_Field_MODEM_S_CTRL0_DEMODRAWDATASEL(self)
        self.zz_fdict['DEMODRAWDATASEL'] = self.DEMODRAWDATASEL
        self.FRAMEDETDEL = RM_Field_MODEM_S_CTRL0_FRAMEDETDEL(self)
        self.zz_fdict['FRAMEDETDEL'] = self.FRAMEDETDEL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CTRL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CTRL1, self).__init__(rmio, label,
            0xa8014000, 0x050,
            'CTRL1', 'MODEM_S.CTRL1', 'read-write',
            u"",
            0x00000000, 0xFFFFDFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SYNCBITS = RM_Field_MODEM_S_CTRL1_SYNCBITS(self)
        self.zz_fdict['SYNCBITS'] = self.SYNCBITS
        self.SYNCERRORS = RM_Field_MODEM_S_CTRL1_SYNCERRORS(self)
        self.zz_fdict['SYNCERRORS'] = self.SYNCERRORS
        self.DUALSYNC = RM_Field_MODEM_S_CTRL1_DUALSYNC(self)
        self.zz_fdict['DUALSYNC'] = self.DUALSYNC
        self.TXSYNC = RM_Field_MODEM_S_CTRL1_TXSYNC(self)
        self.zz_fdict['TXSYNC'] = self.TXSYNC
        self.SYNCDATA = RM_Field_MODEM_S_CTRL1_SYNCDATA(self)
        self.zz_fdict['SYNCDATA'] = self.SYNCDATA
        self.SYNC1INV = RM_Field_MODEM_S_CTRL1_SYNC1INV(self)
        self.zz_fdict['SYNC1INV'] = self.SYNC1INV
        self.COMPMODE = RM_Field_MODEM_S_CTRL1_COMPMODE(self)
        self.zz_fdict['COMPMODE'] = self.COMPMODE
        self.RESYNCPER = RM_Field_MODEM_S_CTRL1_RESYNCPER(self)
        self.zz_fdict['RESYNCPER'] = self.RESYNCPER
        self.PHASEDEMOD = RM_Field_MODEM_S_CTRL1_PHASEDEMOD(self)
        self.zz_fdict['PHASEDEMOD'] = self.PHASEDEMOD
        self.FREQOFFESTPER = RM_Field_MODEM_S_CTRL1_FREQOFFESTPER(self)
        self.zz_fdict['FREQOFFESTPER'] = self.FREQOFFESTPER
        self.FREQOFFESTLIM = RM_Field_MODEM_S_CTRL1_FREQOFFESTLIM(self)
        self.zz_fdict['FREQOFFESTLIM'] = self.FREQOFFESTLIM
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CTRL2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CTRL2, self).__init__(rmio, label,
            0xa8014000, 0x054,
            'CTRL2', 'MODEM_S.CTRL2', 'read-write',
            u"",
            0x00001000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SQITHRESH = RM_Field_MODEM_S_CTRL2_SQITHRESH(self)
        self.zz_fdict['SQITHRESH'] = self.SQITHRESH
        self.RXFRCDIS = RM_Field_MODEM_S_CTRL2_RXFRCDIS(self)
        self.zz_fdict['RXFRCDIS'] = self.RXFRCDIS
        self.RXPINMODE = RM_Field_MODEM_S_CTRL2_RXPINMODE(self)
        self.zz_fdict['RXPINMODE'] = self.RXPINMODE
        self.TXPINMODE = RM_Field_MODEM_S_CTRL2_TXPINMODE(self)
        self.zz_fdict['TXPINMODE'] = self.TXPINMODE
        self.DATAFILTER = RM_Field_MODEM_S_CTRL2_DATAFILTER(self)
        self.zz_fdict['DATAFILTER'] = self.DATAFILTER
        self.BRDIVA = RM_Field_MODEM_S_CTRL2_BRDIVA(self)
        self.zz_fdict['BRDIVA'] = self.BRDIVA
        self.BRDIVB = RM_Field_MODEM_S_CTRL2_BRDIVB(self)
        self.zz_fdict['BRDIVB'] = self.BRDIVB
        self.DEVMULA = RM_Field_MODEM_S_CTRL2_DEVMULA(self)
        self.zz_fdict['DEVMULA'] = self.DEVMULA
        self.DEVMULB = RM_Field_MODEM_S_CTRL2_DEVMULB(self)
        self.zz_fdict['DEVMULB'] = self.DEVMULB
        self.RATESELMODE = RM_Field_MODEM_S_CTRL2_RATESELMODE(self)
        self.zz_fdict['RATESELMODE'] = self.RATESELMODE
        self.DEVWEIGHTDIS = RM_Field_MODEM_S_CTRL2_DEVWEIGHTDIS(self)
        self.zz_fdict['DEVWEIGHTDIS'] = self.DEVWEIGHTDIS
        self.DMASEL = RM_Field_MODEM_S_CTRL2_DMASEL(self)
        self.zz_fdict['DMASEL'] = self.DMASEL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CTRL3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CTRL3, self).__init__(rmio, label,
            0xa8014000, 0x058,
            'CTRL3', 'MODEM_S.CTRL3', 'read-write',
            u"",
            0x00008000, 0xFFFFFF87,
            0x00001000, 0x00002000,
            0x00003000)

        self.PRSDINEN = RM_Field_MODEM_S_CTRL3_PRSDINEN(self)
        self.zz_fdict['PRSDINEN'] = self.PRSDINEN
        self.TIMINGBASESGAIN = RM_Field_MODEM_S_CTRL3_TIMINGBASESGAIN(self)
        self.zz_fdict['TIMINGBASESGAIN'] = self.TIMINGBASESGAIN
        self.RAMTESTEN = RM_Field_MODEM_S_CTRL3_RAMTESTEN(self)
        self.zz_fdict['RAMTESTEN'] = self.RAMTESTEN
        self.ANTDIVMODE = RM_Field_MODEM_S_CTRL3_ANTDIVMODE(self)
        self.zz_fdict['ANTDIVMODE'] = self.ANTDIVMODE
        self.ANTDIVREPEATDIS = RM_Field_MODEM_S_CTRL3_ANTDIVREPEATDIS(self)
        self.zz_fdict['ANTDIVREPEATDIS'] = self.ANTDIVREPEATDIS
        self.TSAMPMODE = RM_Field_MODEM_S_CTRL3_TSAMPMODE(self)
        self.zz_fdict['TSAMPMODE'] = self.TSAMPMODE
        self.TSAMPDEL = RM_Field_MODEM_S_CTRL3_TSAMPDEL(self)
        self.zz_fdict['TSAMPDEL'] = self.TSAMPDEL
        self.TSAMPLIM = RM_Field_MODEM_S_CTRL3_TSAMPLIM(self)
        self.zz_fdict['TSAMPLIM'] = self.TSAMPLIM
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CTRL4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CTRL4, self).__init__(rmio, label,
            0xa8014000, 0x05C,
            'CTRL4', 'MODEM_S.CTRL4', 'read-write',
            u"",
            0x03000000, 0xBFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ISICOMP = RM_Field_MODEM_S_CTRL4_ISICOMP(self)
        self.zz_fdict['ISICOMP'] = self.ISICOMP
        self.DEVOFFCOMP = RM_Field_MODEM_S_CTRL4_DEVOFFCOMP(self)
        self.zz_fdict['DEVOFFCOMP'] = self.DEVOFFCOMP
        self.PREDISTGAIN = RM_Field_MODEM_S_CTRL4_PREDISTGAIN(self)
        self.zz_fdict['PREDISTGAIN'] = self.PREDISTGAIN
        self.PREDISTDEB = RM_Field_MODEM_S_CTRL4_PREDISTDEB(self)
        self.zz_fdict['PREDISTDEB'] = self.PREDISTDEB
        self.PREDISTAVG = RM_Field_MODEM_S_CTRL4_PREDISTAVG(self)
        self.zz_fdict['PREDISTAVG'] = self.PREDISTAVG
        self.PREDISTRST = RM_Field_MODEM_S_CTRL4_PREDISTRST(self)
        self.zz_fdict['PREDISTRST'] = self.PREDISTRST
        self.PHASECLICKFILT = RM_Field_MODEM_S_CTRL4_PHASECLICKFILT(self)
        self.zz_fdict['PHASECLICKFILT'] = self.PHASECLICKFILT
        self.SOFTDSSSMODE = RM_Field_MODEM_S_CTRL4_SOFTDSSSMODE(self)
        self.zz_fdict['SOFTDSSSMODE'] = self.SOFTDSSSMODE
        self.ADCSATLEVEL = RM_Field_MODEM_S_CTRL4_ADCSATLEVEL(self)
        self.zz_fdict['ADCSATLEVEL'] = self.ADCSATLEVEL
        self.ADCSATDENS = RM_Field_MODEM_S_CTRL4_ADCSATDENS(self)
        self.zz_fdict['ADCSATDENS'] = self.ADCSATDENS
        self.OFFSETPHASEMASKING = RM_Field_MODEM_S_CTRL4_OFFSETPHASEMASKING(self)
        self.zz_fdict['OFFSETPHASEMASKING'] = self.OFFSETPHASEMASKING
        self.OFFSETPHASESCALING = RM_Field_MODEM_S_CTRL4_OFFSETPHASESCALING(self)
        self.zz_fdict['OFFSETPHASESCALING'] = self.OFFSETPHASESCALING
        self.CLKUNDIVREQ = RM_Field_MODEM_S_CTRL4_CLKUNDIVREQ(self)
        self.zz_fdict['CLKUNDIVREQ'] = self.CLKUNDIVREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CTRL5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CTRL5, self).__init__(rmio, label,
            0xa8014000, 0x060,
            'CTRL5', 'MODEM_S.CTRL5', 'read-write',
            u"",
            0x00000000, 0x6F7FFFFE,
            0x00001000, 0x00002000,
            0x00003000)

        self.BRCALEN = RM_Field_MODEM_S_CTRL5_BRCALEN(self)
        self.zz_fdict['BRCALEN'] = self.BRCALEN
        self.BRCALMODE = RM_Field_MODEM_S_CTRL5_BRCALMODE(self)
        self.zz_fdict['BRCALMODE'] = self.BRCALMODE
        self.BRCALAVG = RM_Field_MODEM_S_CTRL5_BRCALAVG(self)
        self.zz_fdict['BRCALAVG'] = self.BRCALAVG
        self.DETDEL = RM_Field_MODEM_S_CTRL5_DETDEL(self)
        self.zz_fdict['DETDEL'] = self.DETDEL
        self.TDEDGE = RM_Field_MODEM_S_CTRL5_TDEDGE(self)
        self.zz_fdict['TDEDGE'] = self.TDEDGE
        self.TREDGE = RM_Field_MODEM_S_CTRL5_TREDGE(self)
        self.zz_fdict['TREDGE'] = self.TREDGE
        self.DSSSCTD = RM_Field_MODEM_S_CTRL5_DSSSCTD(self)
        self.zz_fdict['DSSSCTD'] = self.DSSSCTD
        self.BBSS = RM_Field_MODEM_S_CTRL5_BBSS(self)
        self.zz_fdict['BBSS'] = self.BBSS
        self.POEPER = RM_Field_MODEM_S_CTRL5_POEPER(self)
        self.zz_fdict['POEPER'] = self.POEPER
        self.DEMODRAWDATASEL2 = RM_Field_MODEM_S_CTRL5_DEMODRAWDATASEL2(self)
        self.zz_fdict['DEMODRAWDATASEL2'] = self.DEMODRAWDATASEL2
        self.FOEPREAVG = RM_Field_MODEM_S_CTRL5_FOEPREAVG(self)
        self.zz_fdict['FOEPREAVG'] = self.FOEPREAVG
        self.LINCORR = RM_Field_MODEM_S_CTRL5_LINCORR(self)
        self.zz_fdict['LINCORR'] = self.LINCORR
        self.RESYNCBAUDTRANS = RM_Field_MODEM_S_CTRL5_RESYNCBAUDTRANS(self)
        self.zz_fdict['RESYNCBAUDTRANS'] = self.RESYNCBAUDTRANS
        self.RESYNCLIMIT = RM_Field_MODEM_S_CTRL5_RESYNCLIMIT(self)
        self.zz_fdict['RESYNCLIMIT'] = self.RESYNCLIMIT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CTRL6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CTRL6, self).__init__(rmio, label,
            0xa8014000, 0x064,
            'CTRL6', 'MODEM_S.CTRL6', 'read-write',
            u"",
            0x00000000, 0xF6FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TDREW = RM_Field_MODEM_S_CTRL6_TDREW(self)
        self.zz_fdict['TDREW'] = self.TDREW
        self.PREBASES = RM_Field_MODEM_S_CTRL6_PREBASES(self)
        self.zz_fdict['PREBASES'] = self.PREBASES
        self.PSTIMABORT0 = RM_Field_MODEM_S_CTRL6_PSTIMABORT0(self)
        self.zz_fdict['PSTIMABORT0'] = self.PSTIMABORT0
        self.PSTIMABORT1 = RM_Field_MODEM_S_CTRL6_PSTIMABORT1(self)
        self.zz_fdict['PSTIMABORT1'] = self.PSTIMABORT1
        self.PSTIMABORT2 = RM_Field_MODEM_S_CTRL6_PSTIMABORT2(self)
        self.zz_fdict['PSTIMABORT2'] = self.PSTIMABORT2
        self.PSTIMABORT3 = RM_Field_MODEM_S_CTRL6_PSTIMABORT3(self)
        self.zz_fdict['PSTIMABORT3'] = self.PSTIMABORT3
        self.ARW = RM_Field_MODEM_S_CTRL6_ARW(self)
        self.zz_fdict['ARW'] = self.ARW
        self.TIMTHRESHGAIN = RM_Field_MODEM_S_CTRL6_TIMTHRESHGAIN(self)
        self.zz_fdict['TIMTHRESHGAIN'] = self.TIMTHRESHGAIN
        self.CPLXCORREN = RM_Field_MODEM_S_CTRL6_CPLXCORREN(self)
        self.zz_fdict['CPLXCORREN'] = self.CPLXCORREN
        self.DSSS3SYMBOLSYNCEN = RM_Field_MODEM_S_CTRL6_DSSS3SYMBOLSYNCEN(self)
        self.zz_fdict['DSSS3SYMBOLSYNCEN'] = self.DSSS3SYMBOLSYNCEN
        self.TXDBPSKINV = RM_Field_MODEM_S_CTRL6_TXDBPSKINV(self)
        self.zz_fdict['TXDBPSKINV'] = self.TXDBPSKINV
        self.TXDBPSKRAMPEN = RM_Field_MODEM_S_CTRL6_TXDBPSKRAMPEN(self)
        self.zz_fdict['TXDBPSKRAMPEN'] = self.TXDBPSKRAMPEN
        self.CODINGB = RM_Field_MODEM_S_CTRL6_CODINGB(self)
        self.zz_fdict['CODINGB'] = self.CODINGB
        self.RXRESTARTUPONRSSI = RM_Field_MODEM_S_CTRL6_RXRESTARTUPONRSSI(self)
        self.zz_fdict['RXRESTARTUPONRSSI'] = self.RXRESTARTUPONRSSI
        self.RXRESTARTUPONSHORTRSSI = RM_Field_MODEM_S_CTRL6_RXRESTARTUPONSHORTRSSI(self)
        self.zz_fdict['RXRESTARTUPONSHORTRSSI'] = self.RXRESTARTUPONSHORTRSSI
        self.RXBRCALCDIS = RM_Field_MODEM_S_CTRL6_RXBRCALCDIS(self)
        self.zz_fdict['RXBRCALCDIS'] = self.RXBRCALCDIS
        self.DEMODRESTARTALL = RM_Field_MODEM_S_CTRL6_DEMODRESTARTALL(self)
        self.zz_fdict['DEMODRESTARTALL'] = self.DEMODRESTARTALL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_TXBR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_TXBR, self).__init__(rmio, label,
            0xa8014000, 0x068,
            'TXBR', 'MODEM_S.TXBR', 'read-write',
            u"",
            0x00000000, 0x00FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TXBRNUM = RM_Field_MODEM_S_TXBR_TXBRNUM(self)
        self.zz_fdict['TXBRNUM'] = self.TXBRNUM
        self.TXBRDEN = RM_Field_MODEM_S_TXBR_TXBRDEN(self)
        self.zz_fdict['TXBRDEN'] = self.TXBRDEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_RXBR(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_RXBR, self).__init__(rmio, label,
            0xa8014000, 0x06C,
            'RXBR', 'MODEM_S.RXBR', 'read-write',
            u"",
            0x00000000, 0x00001FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RXBRNUM = RM_Field_MODEM_S_RXBR_RXBRNUM(self)
        self.zz_fdict['RXBRNUM'] = self.RXBRNUM
        self.RXBRDEN = RM_Field_MODEM_S_RXBR_RXBRDEN(self)
        self.zz_fdict['RXBRDEN'] = self.RXBRDEN
        self.RXBRINT = RM_Field_MODEM_S_RXBR_RXBRINT(self)
        self.zz_fdict['RXBRINT'] = self.RXBRINT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CF, self).__init__(rmio, label,
            0xa8014000, 0x070,
            'CF', 'MODEM_S.CF', 'read-write',
            u"",
            0x00000000, 0xCFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DEC0 = RM_Field_MODEM_S_CF_DEC0(self)
        self.zz_fdict['DEC0'] = self.DEC0
        self.DEC1 = RM_Field_MODEM_S_CF_DEC1(self)
        self.zz_fdict['DEC1'] = self.DEC1
        self.DEC2 = RM_Field_MODEM_S_CF_DEC2(self)
        self.zz_fdict['DEC2'] = self.DEC2
        self.CFOSR = RM_Field_MODEM_S_CF_CFOSR(self)
        self.zz_fdict['CFOSR'] = self.CFOSR
        self.DEC1GAIN = RM_Field_MODEM_S_CF_DEC1GAIN(self)
        self.zz_fdict['DEC1GAIN'] = self.DEC1GAIN
        self.ADCBITORDERI = RM_Field_MODEM_S_CF_ADCBITORDERI(self)
        self.zz_fdict['ADCBITORDERI'] = self.ADCBITORDERI
        self.ADCBITORDERQ = RM_Field_MODEM_S_CF_ADCBITORDERQ(self)
        self.zz_fdict['ADCBITORDERQ'] = self.ADCBITORDERQ
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_PRE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_PRE, self).__init__(rmio, label,
            0xa8014000, 0x074,
            'PRE', 'MODEM_S.PRE', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.BASE = RM_Field_MODEM_S_PRE_BASE(self)
        self.zz_fdict['BASE'] = self.BASE
        self.BASEBITS = RM_Field_MODEM_S_PRE_BASEBITS(self)
        self.zz_fdict['BASEBITS'] = self.BASEBITS
        self.PRESYMB4FSK = RM_Field_MODEM_S_PRE_PRESYMB4FSK(self)
        self.zz_fdict['PRESYMB4FSK'] = self.PRESYMB4FSK
        self.PREERRORS = RM_Field_MODEM_S_PRE_PREERRORS(self)
        self.zz_fdict['PREERRORS'] = self.PREERRORS
        self.DSSSPRE = RM_Field_MODEM_S_PRE_DSSSPRE(self)
        self.zz_fdict['DSSSPRE'] = self.DSSSPRE
        self.SYNCSYMB4FSK = RM_Field_MODEM_S_PRE_SYNCSYMB4FSK(self)
        self.zz_fdict['SYNCSYMB4FSK'] = self.SYNCSYMB4FSK
        self.PREAMBDETEN = RM_Field_MODEM_S_PRE_PREAMBDETEN(self)
        self.zz_fdict['PREAMBDETEN'] = self.PREAMBDETEN
        self.PREWNDERRORS = RM_Field_MODEM_S_PRE_PREWNDERRORS(self)
        self.zz_fdict['PREWNDERRORS'] = self.PREWNDERRORS
        self.TXBASES = RM_Field_MODEM_S_PRE_TXBASES(self)
        self.zz_fdict['TXBASES'] = self.TXBASES
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SYNC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SYNC0, self).__init__(rmio, label,
            0xa8014000, 0x078,
            'SYNC0', 'MODEM_S.SYNC0', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SYNC0 = RM_Field_MODEM_S_SYNC0_SYNC0(self)
        self.zz_fdict['SYNC0'] = self.SYNC0
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SYNC1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SYNC1, self).__init__(rmio, label,
            0xa8014000, 0x07C,
            'SYNC1', 'MODEM_S.SYNC1', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SYNC1 = RM_Field_MODEM_S_SYNC1_SYNC1(self)
        self.zz_fdict['SYNC1'] = self.SYNC1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_TIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_TIMING, self).__init__(rmio, label,
            0xa8014000, 0x080,
            'TIMING', 'MODEM_S.TIMING', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TIMTHRESH = RM_Field_MODEM_S_TIMING_TIMTHRESH(self)
        self.zz_fdict['TIMTHRESH'] = self.TIMTHRESH
        self.TIMINGBASES = RM_Field_MODEM_S_TIMING_TIMINGBASES(self)
        self.zz_fdict['TIMINGBASES'] = self.TIMINGBASES
        self.ADDTIMSEQ = RM_Field_MODEM_S_TIMING_ADDTIMSEQ(self)
        self.zz_fdict['ADDTIMSEQ'] = self.ADDTIMSEQ
        self.TIMSEQINVEN = RM_Field_MODEM_S_TIMING_TIMSEQINVEN(self)
        self.zz_fdict['TIMSEQINVEN'] = self.TIMSEQINVEN
        self.TIMSEQSYNC = RM_Field_MODEM_S_TIMING_TIMSEQSYNC(self)
        self.zz_fdict['TIMSEQSYNC'] = self.TIMSEQSYNC
        self.FDM0THRESH = RM_Field_MODEM_S_TIMING_FDM0THRESH(self)
        self.zz_fdict['FDM0THRESH'] = self.FDM0THRESH
        self.OFFSUBNUM = RM_Field_MODEM_S_TIMING_OFFSUBNUM(self)
        self.zz_fdict['OFFSUBNUM'] = self.OFFSUBNUM
        self.OFFSUBDEN = RM_Field_MODEM_S_TIMING_OFFSUBDEN(self)
        self.zz_fdict['OFFSUBDEN'] = self.OFFSUBDEN
        self.TSAGCDEL = RM_Field_MODEM_S_TIMING_TSAGCDEL(self)
        self.zz_fdict['TSAGCDEL'] = self.TSAGCDEL
        self.FASTRESYNC = RM_Field_MODEM_S_TIMING_FASTRESYNC(self)
        self.zz_fdict['FASTRESYNC'] = self.FASTRESYNC
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DSSS0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DSSS0, self).__init__(rmio, label,
            0xa8014000, 0x084,
            'DSSS0', 'MODEM_S.DSSS0', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DSSS0 = RM_Field_MODEM_S_DSSS0_DSSS0(self)
        self.zz_fdict['DSSS0'] = self.DSSS0
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_MODINDEX(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_MODINDEX, self).__init__(rmio, label,
            0xa8014000, 0x088,
            'MODINDEX', 'MODEM_S.MODINDEX', 'read-write',
            u"",
            0x00000000, 0x003F03FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.MODINDEXM = RM_Field_MODEM_S_MODINDEX_MODINDEXM(self)
        self.zz_fdict['MODINDEXM'] = self.MODINDEXM
        self.MODINDEXE = RM_Field_MODEM_S_MODINDEX_MODINDEXE(self)
        self.zz_fdict['MODINDEXE'] = self.MODINDEXE
        self.FREQGAINE = RM_Field_MODEM_S_MODINDEX_FREQGAINE(self)
        self.zz_fdict['FREQGAINE'] = self.FREQGAINE
        self.FREQGAINM = RM_Field_MODEM_S_MODINDEX_FREQGAINM(self)
        self.zz_fdict['FREQGAINM'] = self.FREQGAINM
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_AFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_AFC, self).__init__(rmio, label,
            0xa8014000, 0x08C,
            'AFC', 'MODEM_S.AFC', 'read-write',
            u"",
            0x00000000, 0x7FFFFC00,
            0x00001000, 0x00002000,
            0x00003000)

        self.AFCRXMODE = RM_Field_MODEM_S_AFC_AFCRXMODE(self)
        self.zz_fdict['AFCRXMODE'] = self.AFCRXMODE
        self.AFCTXMODE = RM_Field_MODEM_S_AFC_AFCTXMODE(self)
        self.zz_fdict['AFCTXMODE'] = self.AFCTXMODE
        self.AFCRXCLR = RM_Field_MODEM_S_AFC_AFCRXCLR(self)
        self.zz_fdict['AFCRXCLR'] = self.AFCRXCLR
        self.AFCDEL = RM_Field_MODEM_S_AFC_AFCDEL(self)
        self.zz_fdict['AFCDEL'] = self.AFCDEL
        self.AFCAVGPER = RM_Field_MODEM_S_AFC_AFCAVGPER(self)
        self.zz_fdict['AFCAVGPER'] = self.AFCAVGPER
        self.AFCLIMRESET = RM_Field_MODEM_S_AFC_AFCLIMRESET(self)
        self.zz_fdict['AFCLIMRESET'] = self.AFCLIMRESET
        self.AFCONESHOT = RM_Field_MODEM_S_AFC_AFCONESHOT(self)
        self.zz_fdict['AFCONESHOT'] = self.AFCONESHOT
        self.AFCENINTCOMP = RM_Field_MODEM_S_AFC_AFCENINTCOMP(self)
        self.zz_fdict['AFCENINTCOMP'] = self.AFCENINTCOMP
        self.AFCDSAFREQOFFEST = RM_Field_MODEM_S_AFC_AFCDSAFREQOFFEST(self)
        self.zz_fdict['AFCDSAFREQOFFEST'] = self.AFCDSAFREQOFFEST
        self.AFCDELDET = RM_Field_MODEM_S_AFC_AFCDELDET(self)
        self.zz_fdict['AFCDELDET'] = self.AFCDELDET
        self.AFCGEAR = RM_Field_MODEM_S_AFC_AFCGEAR(self)
        self.zz_fdict['AFCGEAR'] = self.AFCGEAR
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_AFCADJLIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_AFCADJLIM, self).__init__(rmio, label,
            0xa8014000, 0x090,
            'AFCADJLIM', 'MODEM_S.AFCADJLIM', 'read-write',
            u"",
            0x00000000, 0x0003FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.AFCADJLIM = RM_Field_MODEM_S_AFCADJLIM_AFCADJLIM(self)
        self.zz_fdict['AFCADJLIM'] = self.AFCADJLIM
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING0, self).__init__(rmio, label,
            0xa8014000, 0x094,
            'SHAPING0', 'MODEM_S.SHAPING0', 'read-write',
            u"",
            0x22130A04, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF0 = RM_Field_MODEM_S_SHAPING0_COEFF0(self)
        self.zz_fdict['COEFF0'] = self.COEFF0
        self.COEFF1 = RM_Field_MODEM_S_SHAPING0_COEFF1(self)
        self.zz_fdict['COEFF1'] = self.COEFF1
        self.COEFF2 = RM_Field_MODEM_S_SHAPING0_COEFF2(self)
        self.zz_fdict['COEFF2'] = self.COEFF2
        self.COEFF3 = RM_Field_MODEM_S_SHAPING0_COEFF3(self)
        self.zz_fdict['COEFF3'] = self.COEFF3
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING1, self).__init__(rmio, label,
            0xa8014000, 0x098,
            'SHAPING1', 'MODEM_S.SHAPING1', 'read-write',
            u"",
            0x4F4A4132, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF4 = RM_Field_MODEM_S_SHAPING1_COEFF4(self)
        self.zz_fdict['COEFF4'] = self.COEFF4
        self.COEFF5 = RM_Field_MODEM_S_SHAPING1_COEFF5(self)
        self.zz_fdict['COEFF5'] = self.COEFF5
        self.COEFF6 = RM_Field_MODEM_S_SHAPING1_COEFF6(self)
        self.zz_fdict['COEFF6'] = self.COEFF6
        self.COEFF7 = RM_Field_MODEM_S_SHAPING1_COEFF7(self)
        self.zz_fdict['COEFF7'] = self.COEFF7
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING2, self).__init__(rmio, label,
            0xa8014000, 0x09C,
            'SHAPING2', 'MODEM_S.SHAPING2', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF8 = RM_Field_MODEM_S_SHAPING2_COEFF8(self)
        self.zz_fdict['COEFF8'] = self.COEFF8
        self.COEFF9 = RM_Field_MODEM_S_SHAPING2_COEFF9(self)
        self.zz_fdict['COEFF9'] = self.COEFF9
        self.COEFF10 = RM_Field_MODEM_S_SHAPING2_COEFF10(self)
        self.zz_fdict['COEFF10'] = self.COEFF10
        self.COEFF11 = RM_Field_MODEM_S_SHAPING2_COEFF11(self)
        self.zz_fdict['COEFF11'] = self.COEFF11
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING3, self).__init__(rmio, label,
            0xa8014000, 0x0A0,
            'SHAPING3', 'MODEM_S.SHAPING3', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF12 = RM_Field_MODEM_S_SHAPING3_COEFF12(self)
        self.zz_fdict['COEFF12'] = self.COEFF12
        self.COEFF13 = RM_Field_MODEM_S_SHAPING3_COEFF13(self)
        self.zz_fdict['COEFF13'] = self.COEFF13
        self.COEFF14 = RM_Field_MODEM_S_SHAPING3_COEFF14(self)
        self.zz_fdict['COEFF14'] = self.COEFF14
        self.COEFF15 = RM_Field_MODEM_S_SHAPING3_COEFF15(self)
        self.zz_fdict['COEFF15'] = self.COEFF15
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING4, self).__init__(rmio, label,
            0xa8014000, 0x0A4,
            'SHAPING4', 'MODEM_S.SHAPING4', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF16 = RM_Field_MODEM_S_SHAPING4_COEFF16(self)
        self.zz_fdict['COEFF16'] = self.COEFF16
        self.COEFF17 = RM_Field_MODEM_S_SHAPING4_COEFF17(self)
        self.zz_fdict['COEFF17'] = self.COEFF17
        self.COEFF18 = RM_Field_MODEM_S_SHAPING4_COEFF18(self)
        self.zz_fdict['COEFF18'] = self.COEFF18
        self.COEFF19 = RM_Field_MODEM_S_SHAPING4_COEFF19(self)
        self.zz_fdict['COEFF19'] = self.COEFF19
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING5, self).__init__(rmio, label,
            0xa8014000, 0x0A8,
            'SHAPING5', 'MODEM_S.SHAPING5', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF20 = RM_Field_MODEM_S_SHAPING5_COEFF20(self)
        self.zz_fdict['COEFF20'] = self.COEFF20
        self.COEFF21 = RM_Field_MODEM_S_SHAPING5_COEFF21(self)
        self.zz_fdict['COEFF21'] = self.COEFF21
        self.COEFF22 = RM_Field_MODEM_S_SHAPING5_COEFF22(self)
        self.zz_fdict['COEFF22'] = self.COEFF22
        self.COEFF23 = RM_Field_MODEM_S_SHAPING5_COEFF23(self)
        self.zz_fdict['COEFF23'] = self.COEFF23
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING6, self).__init__(rmio, label,
            0xa8014000, 0x0AC,
            'SHAPING6', 'MODEM_S.SHAPING6', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF24 = RM_Field_MODEM_S_SHAPING6_COEFF24(self)
        self.zz_fdict['COEFF24'] = self.COEFF24
        self.COEFF25 = RM_Field_MODEM_S_SHAPING6_COEFF25(self)
        self.zz_fdict['COEFF25'] = self.COEFF25
        self.COEFF26 = RM_Field_MODEM_S_SHAPING6_COEFF26(self)
        self.zz_fdict['COEFF26'] = self.COEFF26
        self.COEFF27 = RM_Field_MODEM_S_SHAPING6_COEFF27(self)
        self.zz_fdict['COEFF27'] = self.COEFF27
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING7, self).__init__(rmio, label,
            0xa8014000, 0x0B0,
            'SHAPING7', 'MODEM_S.SHAPING7', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF28 = RM_Field_MODEM_S_SHAPING7_COEFF28(self)
        self.zz_fdict['COEFF28'] = self.COEFF28
        self.COEFF29 = RM_Field_MODEM_S_SHAPING7_COEFF29(self)
        self.zz_fdict['COEFF29'] = self.COEFF29
        self.COEFF30 = RM_Field_MODEM_S_SHAPING7_COEFF30(self)
        self.zz_fdict['COEFF30'] = self.COEFF30
        self.COEFF31 = RM_Field_MODEM_S_SHAPING7_COEFF31(self)
        self.zz_fdict['COEFF31'] = self.COEFF31
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING8(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING8, self).__init__(rmio, label,
            0xa8014000, 0x0B4,
            'SHAPING8', 'MODEM_S.SHAPING8', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF32 = RM_Field_MODEM_S_SHAPING8_COEFF32(self)
        self.zz_fdict['COEFF32'] = self.COEFF32
        self.COEFF33 = RM_Field_MODEM_S_SHAPING8_COEFF33(self)
        self.zz_fdict['COEFF33'] = self.COEFF33
        self.COEFF34 = RM_Field_MODEM_S_SHAPING8_COEFF34(self)
        self.zz_fdict['COEFF34'] = self.COEFF34
        self.COEFF35 = RM_Field_MODEM_S_SHAPING8_COEFF35(self)
        self.zz_fdict['COEFF35'] = self.COEFF35
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING9(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING9, self).__init__(rmio, label,
            0xa8014000, 0x0B8,
            'SHAPING9', 'MODEM_S.SHAPING9', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF36 = RM_Field_MODEM_S_SHAPING9_COEFF36(self)
        self.zz_fdict['COEFF36'] = self.COEFF36
        self.COEFF37 = RM_Field_MODEM_S_SHAPING9_COEFF37(self)
        self.zz_fdict['COEFF37'] = self.COEFF37
        self.COEFF38 = RM_Field_MODEM_S_SHAPING9_COEFF38(self)
        self.zz_fdict['COEFF38'] = self.COEFF38
        self.COEFF39 = RM_Field_MODEM_S_SHAPING9_COEFF39(self)
        self.zz_fdict['COEFF39'] = self.COEFF39
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING10(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING10, self).__init__(rmio, label,
            0xa8014000, 0x0BC,
            'SHAPING10', 'MODEM_S.SHAPING10', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF40 = RM_Field_MODEM_S_SHAPING10_COEFF40(self)
        self.zz_fdict['COEFF40'] = self.COEFF40
        self.COEFF41 = RM_Field_MODEM_S_SHAPING10_COEFF41(self)
        self.zz_fdict['COEFF41'] = self.COEFF41
        self.COEFF42 = RM_Field_MODEM_S_SHAPING10_COEFF42(self)
        self.zz_fdict['COEFF42'] = self.COEFF42
        self.COEFF43 = RM_Field_MODEM_S_SHAPING10_COEFF43(self)
        self.zz_fdict['COEFF43'] = self.COEFF43
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING11(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING11, self).__init__(rmio, label,
            0xa8014000, 0x0C0,
            'SHAPING11', 'MODEM_S.SHAPING11', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF44 = RM_Field_MODEM_S_SHAPING11_COEFF44(self)
        self.zz_fdict['COEFF44'] = self.COEFF44
        self.COEFF45 = RM_Field_MODEM_S_SHAPING11_COEFF45(self)
        self.zz_fdict['COEFF45'] = self.COEFF45
        self.COEFF46 = RM_Field_MODEM_S_SHAPING11_COEFF46(self)
        self.zz_fdict['COEFF46'] = self.COEFF46
        self.COEFF47 = RM_Field_MODEM_S_SHAPING11_COEFF47(self)
        self.zz_fdict['COEFF47'] = self.COEFF47
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING12(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING12, self).__init__(rmio, label,
            0xa8014000, 0x0C4,
            'SHAPING12', 'MODEM_S.SHAPING12', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF48 = RM_Field_MODEM_S_SHAPING12_COEFF48(self)
        self.zz_fdict['COEFF48'] = self.COEFF48
        self.COEFF49 = RM_Field_MODEM_S_SHAPING12_COEFF49(self)
        self.zz_fdict['COEFF49'] = self.COEFF49
        self.COEFF50 = RM_Field_MODEM_S_SHAPING12_COEFF50(self)
        self.zz_fdict['COEFF50'] = self.COEFF50
        self.COEFF51 = RM_Field_MODEM_S_SHAPING12_COEFF51(self)
        self.zz_fdict['COEFF51'] = self.COEFF51
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING13(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING13, self).__init__(rmio, label,
            0xa8014000, 0x0C8,
            'SHAPING13', 'MODEM_S.SHAPING13', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF52 = RM_Field_MODEM_S_SHAPING13_COEFF52(self)
        self.zz_fdict['COEFF52'] = self.COEFF52
        self.COEFF53 = RM_Field_MODEM_S_SHAPING13_COEFF53(self)
        self.zz_fdict['COEFF53'] = self.COEFF53
        self.COEFF54 = RM_Field_MODEM_S_SHAPING13_COEFF54(self)
        self.zz_fdict['COEFF54'] = self.COEFF54
        self.COEFF55 = RM_Field_MODEM_S_SHAPING13_COEFF55(self)
        self.zz_fdict['COEFF55'] = self.COEFF55
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING14(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING14, self).__init__(rmio, label,
            0xa8014000, 0x0CC,
            'SHAPING14', 'MODEM_S.SHAPING14', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF56 = RM_Field_MODEM_S_SHAPING14_COEFF56(self)
        self.zz_fdict['COEFF56'] = self.COEFF56
        self.COEFF57 = RM_Field_MODEM_S_SHAPING14_COEFF57(self)
        self.zz_fdict['COEFF57'] = self.COEFF57
        self.COEFF58 = RM_Field_MODEM_S_SHAPING14_COEFF58(self)
        self.zz_fdict['COEFF58'] = self.COEFF58
        self.COEFF59 = RM_Field_MODEM_S_SHAPING14_COEFF59(self)
        self.zz_fdict['COEFF59'] = self.COEFF59
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SHAPING15(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SHAPING15, self).__init__(rmio, label,
            0xa8014000, 0x0D0,
            'SHAPING15', 'MODEM_S.SHAPING15', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COEFF60 = RM_Field_MODEM_S_SHAPING15_COEFF60(self)
        self.zz_fdict['COEFF60'] = self.COEFF60
        self.COEFF61 = RM_Field_MODEM_S_SHAPING15_COEFF61(self)
        self.zz_fdict['COEFF61'] = self.COEFF61
        self.COEFF62 = RM_Field_MODEM_S_SHAPING15_COEFF62(self)
        self.zz_fdict['COEFF62'] = self.COEFF62
        self.COEFF63 = RM_Field_MODEM_S_SHAPING15_COEFF63(self)
        self.zz_fdict['COEFF63'] = self.COEFF63
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_OOKSHAPING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_OOKSHAPING, self).__init__(rmio, label,
            0xa8014000, 0x0D4,
            'OOKSHAPING', 'MODEM_S.OOKSHAPING', 'read-write',
            u"",
            0x00000000, 0x0007FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.OOKSHAPINGEN = RM_Field_MODEM_S_OOKSHAPING_OOKSHAPINGEN(self)
        self.zz_fdict['OOKSHAPINGEN'] = self.OOKSHAPINGEN
        self.OOKSHAPINGSTEP = RM_Field_MODEM_S_OOKSHAPING_OOKSHAPINGSTEP(self)
        self.zz_fdict['OOKSHAPINGSTEP'] = self.OOKSHAPINGSTEP
        self.OOKSHAPINGRATE = RM_Field_MODEM_S_OOKSHAPING_OOKSHAPINGRATE(self)
        self.zz_fdict['OOKSHAPINGRATE'] = self.OOKSHAPINGRATE
        self.OOKSHAPINGLUTSIZE = RM_Field_MODEM_S_OOKSHAPING_OOKSHAPINGLUTSIZE(self)
        self.zz_fdict['OOKSHAPINGLUTSIZE'] = self.OOKSHAPINGLUTSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_RAMPCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_RAMPCTRL, self).__init__(rmio, label,
            0xa8014000, 0x0D8,
            'RAMPCTRL', 'MODEM_S.RAMPCTRL', 'read-write',
            u"",
            0x00000555, 0x00FF1FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RAMPRATE0 = RM_Field_MODEM_S_RAMPCTRL_RAMPRATE0(self)
        self.zz_fdict['RAMPRATE0'] = self.RAMPRATE0
        self.RAMPRATE1 = RM_Field_MODEM_S_RAMPCTRL_RAMPRATE1(self)
        self.zz_fdict['RAMPRATE1'] = self.RAMPRATE1
        self.RAMPRATE2 = RM_Field_MODEM_S_RAMPCTRL_RAMPRATE2(self)
        self.zz_fdict['RAMPRATE2'] = self.RAMPRATE2
        self.RAMPDIS = RM_Field_MODEM_S_RAMPCTRL_RAMPDIS(self)
        self.zz_fdict['RAMPDIS'] = self.RAMPDIS
        self.RAMPVAL = RM_Field_MODEM_S_RAMPCTRL_RAMPVAL(self)
        self.zz_fdict['RAMPVAL'] = self.RAMPVAL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_RAMPLEV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_RAMPLEV, self).__init__(rmio, label,
            0xa8014000, 0x0DC,
            'RAMPLEV', 'MODEM_S.RAMPLEV', 'read-write',
            u"",
            0x009F9F9F, 0x00FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RAMPLEV0 = RM_Field_MODEM_S_RAMPLEV_RAMPLEV0(self)
        self.zz_fdict['RAMPLEV0'] = self.RAMPLEV0
        self.RAMPLEV1 = RM_Field_MODEM_S_RAMPLEV_RAMPLEV1(self)
        self.zz_fdict['RAMPLEV1'] = self.RAMPLEV1
        self.RAMPLEV2 = RM_Field_MODEM_S_RAMPLEV_RAMPLEV2(self)
        self.zz_fdict['RAMPLEV2'] = self.RAMPLEV2
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMPCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMPCTRL, self).__init__(rmio, label,
            0xa8014000, 0x0E0,
            'ANARAMPCTRL', 'MODEM_S.ANARAMPCTRL', 'read-write',
            u"",
            0x00000A81, 0x00001FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPEN = RM_Field_MODEM_S_ANARAMPCTRL_ANARAMPEN(self)
        self.zz_fdict['ANARAMPEN'] = self.ANARAMPEN
        self.RAMPOVREN = RM_Field_MODEM_S_ANARAMPCTRL_RAMPOVREN(self)
        self.zz_fdict['RAMPOVREN'] = self.RAMPOVREN
        self.RAMPOVRUPD = RM_Field_MODEM_S_ANARAMPCTRL_RAMPOVRUPD(self)
        self.zz_fdict['RAMPOVRUPD'] = self.RAMPOVRUPD
        self.ANARAMPLUTODEV = RM_Field_MODEM_S_ANARAMPCTRL_ANARAMPLUTODEV(self)
        self.zz_fdict['ANARAMPLUTODEV'] = self.ANARAMPLUTODEV
        self.VMIDCTRL = RM_Field_MODEM_S_ANARAMPCTRL_VMIDCTRL(self)
        self.zz_fdict['VMIDCTRL'] = self.VMIDCTRL
        self.MUTEDLY = RM_Field_MODEM_S_ANARAMPCTRL_MUTEDLY(self)
        self.zz_fdict['MUTEDLY'] = self.MUTEDLY
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP0, self).__init__(rmio, label,
            0xa8014000, 0x0E4,
            'ANARAMP0', 'MODEM_S.ANARAMP0', 'read-write',
            u"",
            0x08418C40, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT0 = RM_Field_MODEM_S_ANARAMP0_ANARAMPLUT0(self)
        self.zz_fdict['ANARAMPLUT0'] = self.ANARAMPLUT0
        self.ANARAMPLUT1 = RM_Field_MODEM_S_ANARAMP0_ANARAMPLUT1(self)
        self.zz_fdict['ANARAMPLUT1'] = self.ANARAMPLUT1
        self.ANARAMPLUT2 = RM_Field_MODEM_S_ANARAMP0_ANARAMPLUT2(self)
        self.zz_fdict['ANARAMPLUT2'] = self.ANARAMPLUT2
        self.ANARAMPLUT3 = RM_Field_MODEM_S_ANARAMP0_ANARAMPLUT3(self)
        self.zz_fdict['ANARAMPLUT3'] = self.ANARAMPLUT3
        self.ANARAMPLUT4 = RM_Field_MODEM_S_ANARAMP0_ANARAMPLUT4(self)
        self.zz_fdict['ANARAMPLUT4'] = self.ANARAMPLUT4
        self.ANARAMPLUT5 = RM_Field_MODEM_S_ANARAMP0_ANARAMPLUT5(self)
        self.zz_fdict['ANARAMPLUT5'] = self.ANARAMPLUT5
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP1, self).__init__(rmio, label,
            0xa8014000, 0x0E8,
            'ANARAMP1', 'MODEM_S.ANARAMP1', 'read-write',
            u"",
            0x18A4A0C5, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT6 = RM_Field_MODEM_S_ANARAMP1_ANARAMPLUT6(self)
        self.zz_fdict['ANARAMPLUT6'] = self.ANARAMPLUT6
        self.ANARAMPLUT7 = RM_Field_MODEM_S_ANARAMP1_ANARAMPLUT7(self)
        self.zz_fdict['ANARAMPLUT7'] = self.ANARAMPLUT7
        self.ANARAMPLUT8 = RM_Field_MODEM_S_ANARAMP1_ANARAMPLUT8(self)
        self.zz_fdict['ANARAMPLUT8'] = self.ANARAMPLUT8
        self.ANARAMPLUT9 = RM_Field_MODEM_S_ANARAMP1_ANARAMPLUT9(self)
        self.zz_fdict['ANARAMPLUT9'] = self.ANARAMPLUT9
        self.ANARAMPLUT10 = RM_Field_MODEM_S_ANARAMP1_ANARAMPLUT10(self)
        self.zz_fdict['ANARAMPLUT10'] = self.ANARAMPLUT10
        self.ANARAMPLUT11 = RM_Field_MODEM_S_ANARAMP1_ANARAMPLUT11(self)
        self.zz_fdict['ANARAMPLUT11'] = self.ANARAMPLUT11
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP2, self).__init__(rmio, label,
            0xa8014000, 0x0EC,
            'ANARAMP2', 'MODEM_S.ANARAMP2', 'read-write',
            u"",
            0x020ED60D, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT12 = RM_Field_MODEM_S_ANARAMP2_ANARAMPLUT12(self)
        self.zz_fdict['ANARAMPLUT12'] = self.ANARAMPLUT12
        self.ANARAMPLUT13 = RM_Field_MODEM_S_ANARAMP2_ANARAMPLUT13(self)
        self.zz_fdict['ANARAMPLUT13'] = self.ANARAMPLUT13
        self.ANARAMPLUT14 = RM_Field_MODEM_S_ANARAMP2_ANARAMPLUT14(self)
        self.zz_fdict['ANARAMPLUT14'] = self.ANARAMPLUT14
        self.ANARAMPLUT15 = RM_Field_MODEM_S_ANARAMP2_ANARAMPLUT15(self)
        self.zz_fdict['ANARAMPLUT15'] = self.ANARAMPLUT15
        self.ANARAMPLUT16 = RM_Field_MODEM_S_ANARAMP2_ANARAMPLUT16(self)
        self.zz_fdict['ANARAMPLUT16'] = self.ANARAMPLUT16
        self.ANARAMPLUT17 = RM_Field_MODEM_S_ANARAMP2_ANARAMPLUT17(self)
        self.zz_fdict['ANARAMPLUT17'] = self.ANARAMPLUT17
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP3, self).__init__(rmio, label,
            0xa8014000, 0x0F0,
            'ANARAMP3', 'MODEM_S.ANARAMP3', 'read-write',
            u"",
            0x06210821, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT18 = RM_Field_MODEM_S_ANARAMP3_ANARAMPLUT18(self)
        self.zz_fdict['ANARAMPLUT18'] = self.ANARAMPLUT18
        self.ANARAMPLUT19 = RM_Field_MODEM_S_ANARAMP3_ANARAMPLUT19(self)
        self.zz_fdict['ANARAMPLUT19'] = self.ANARAMPLUT19
        self.ANARAMPLUT20 = RM_Field_MODEM_S_ANARAMP3_ANARAMPLUT20(self)
        self.zz_fdict['ANARAMPLUT20'] = self.ANARAMPLUT20
        self.ANARAMPLUT21 = RM_Field_MODEM_S_ANARAMP3_ANARAMPLUT21(self)
        self.zz_fdict['ANARAMPLUT21'] = self.ANARAMPLUT21
        self.ANARAMPLUT22 = RM_Field_MODEM_S_ANARAMP3_ANARAMPLUT22(self)
        self.zz_fdict['ANARAMPLUT22'] = self.ANARAMPLUT22
        self.ANARAMPLUT23 = RM_Field_MODEM_S_ANARAMP3_ANARAMPLUT23(self)
        self.zz_fdict['ANARAMPLUT23'] = self.ANARAMPLUT23
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP4, self).__init__(rmio, label,
            0xa8014000, 0x0F4,
            'ANARAMP4', 'MODEM_S.ANARAMP4', 'read-write',
            u"",
            0x08420C63, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT24 = RM_Field_MODEM_S_ANARAMP4_ANARAMPLUT24(self)
        self.zz_fdict['ANARAMPLUT24'] = self.ANARAMPLUT24
        self.ANARAMPLUT25 = RM_Field_MODEM_S_ANARAMP4_ANARAMPLUT25(self)
        self.zz_fdict['ANARAMPLUT25'] = self.ANARAMPLUT25
        self.ANARAMPLUT26 = RM_Field_MODEM_S_ANARAMP4_ANARAMPLUT26(self)
        self.zz_fdict['ANARAMPLUT26'] = self.ANARAMPLUT26
        self.ANARAMPLUT27 = RM_Field_MODEM_S_ANARAMP4_ANARAMPLUT27(self)
        self.zz_fdict['ANARAMPLUT27'] = self.ANARAMPLUT27
        self.ANARAMPLUT28 = RM_Field_MODEM_S_ANARAMP4_ANARAMPLUT28(self)
        self.zz_fdict['ANARAMPLUT28'] = self.ANARAMPLUT28
        self.ANARAMPLUT29 = RM_Field_MODEM_S_ANARAMP4_ANARAMPLUT29(self)
        self.zz_fdict['ANARAMPLUT29'] = self.ANARAMPLUT29
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP5, self).__init__(rmio, label,
            0xa8014000, 0x0F8,
            'ANARAMP5', 'MODEM_S.ANARAMP5', 'read-write',
            u"",
            0x0C6294A5, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT30 = RM_Field_MODEM_S_ANARAMP5_ANARAMPLUT30(self)
        self.zz_fdict['ANARAMPLUT30'] = self.ANARAMPLUT30
        self.ANARAMPLUT31 = RM_Field_MODEM_S_ANARAMP5_ANARAMPLUT31(self)
        self.zz_fdict['ANARAMPLUT31'] = self.ANARAMPLUT31
        self.ANARAMPLUT32 = RM_Field_MODEM_S_ANARAMP5_ANARAMPLUT32(self)
        self.zz_fdict['ANARAMPLUT32'] = self.ANARAMPLUT32
        self.ANARAMPLUT33 = RM_Field_MODEM_S_ANARAMP5_ANARAMPLUT33(self)
        self.zz_fdict['ANARAMPLUT33'] = self.ANARAMPLUT33
        self.ANARAMPLUT34 = RM_Field_MODEM_S_ANARAMP5_ANARAMPLUT34(self)
        self.zz_fdict['ANARAMPLUT34'] = self.ANARAMPLUT34
        self.ANARAMPLUT35 = RM_Field_MODEM_S_ANARAMP5_ANARAMPLUT35(self)
        self.zz_fdict['ANARAMPLUT35'] = self.ANARAMPLUT35
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP6, self).__init__(rmio, label,
            0xa8014000, 0x0FC,
            'ANARAMP6', 'MODEM_S.ANARAMP6', 'read-write',
            u"",
            0x10739CE6, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT36 = RM_Field_MODEM_S_ANARAMP6_ANARAMPLUT36(self)
        self.zz_fdict['ANARAMPLUT36'] = self.ANARAMPLUT36
        self.ANARAMPLUT37 = RM_Field_MODEM_S_ANARAMP6_ANARAMPLUT37(self)
        self.zz_fdict['ANARAMPLUT37'] = self.ANARAMPLUT37
        self.ANARAMPLUT38 = RM_Field_MODEM_S_ANARAMP6_ANARAMPLUT38(self)
        self.zz_fdict['ANARAMPLUT38'] = self.ANARAMPLUT38
        self.ANARAMPLUT39 = RM_Field_MODEM_S_ANARAMP6_ANARAMPLUT39(self)
        self.zz_fdict['ANARAMPLUT39'] = self.ANARAMPLUT39
        self.ANARAMPLUT40 = RM_Field_MODEM_S_ANARAMP6_ANARAMPLUT40(self)
        self.zz_fdict['ANARAMPLUT40'] = self.ANARAMPLUT40
        self.ANARAMPLUT41 = RM_Field_MODEM_S_ANARAMP6_ANARAMPLUT41(self)
        self.zz_fdict['ANARAMPLUT41'] = self.ANARAMPLUT41
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP7, self).__init__(rmio, label,
            0xa8014000, 0x100,
            'ANARAMP7', 'MODEM_S.ANARAMP7', 'read-write',
            u"",
            0x1494A508, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT42 = RM_Field_MODEM_S_ANARAMP7_ANARAMPLUT42(self)
        self.zz_fdict['ANARAMPLUT42'] = self.ANARAMPLUT42
        self.ANARAMPLUT43 = RM_Field_MODEM_S_ANARAMP7_ANARAMPLUT43(self)
        self.zz_fdict['ANARAMPLUT43'] = self.ANARAMPLUT43
        self.ANARAMPLUT44 = RM_Field_MODEM_S_ANARAMP7_ANARAMPLUT44(self)
        self.zz_fdict['ANARAMPLUT44'] = self.ANARAMPLUT44
        self.ANARAMPLUT45 = RM_Field_MODEM_S_ANARAMP7_ANARAMPLUT45(self)
        self.zz_fdict['ANARAMPLUT45'] = self.ANARAMPLUT45
        self.ANARAMPLUT46 = RM_Field_MODEM_S_ANARAMP7_ANARAMPLUT46(self)
        self.zz_fdict['ANARAMPLUT46'] = self.ANARAMPLUT46
        self.ANARAMPLUT47 = RM_Field_MODEM_S_ANARAMP7_ANARAMPLUT47(self)
        self.zz_fdict['ANARAMPLUT47'] = self.ANARAMPLUT47
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP8(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP8, self).__init__(rmio, label,
            0xa8014000, 0x104,
            'ANARAMP8', 'MODEM_S.ANARAMP8', 'read-write',
            u"",
            0x18C5AD4A, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT48 = RM_Field_MODEM_S_ANARAMP8_ANARAMPLUT48(self)
        self.zz_fdict['ANARAMPLUT48'] = self.ANARAMPLUT48
        self.ANARAMPLUT49 = RM_Field_MODEM_S_ANARAMP8_ANARAMPLUT49(self)
        self.zz_fdict['ANARAMPLUT49'] = self.ANARAMPLUT49
        self.ANARAMPLUT50 = RM_Field_MODEM_S_ANARAMP8_ANARAMPLUT50(self)
        self.zz_fdict['ANARAMPLUT50'] = self.ANARAMPLUT50
        self.ANARAMPLUT51 = RM_Field_MODEM_S_ANARAMP8_ANARAMPLUT51(self)
        self.zz_fdict['ANARAMPLUT51'] = self.ANARAMPLUT51
        self.ANARAMPLUT52 = RM_Field_MODEM_S_ANARAMP8_ANARAMPLUT52(self)
        self.zz_fdict['ANARAMPLUT52'] = self.ANARAMPLUT52
        self.ANARAMPLUT53 = RM_Field_MODEM_S_ANARAMP8_ANARAMPLUT53(self)
        self.zz_fdict['ANARAMPLUT53'] = self.ANARAMPLUT53
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP9(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP9, self).__init__(rmio, label,
            0xa8014000, 0x108,
            'ANARAMP9', 'MODEM_S.ANARAMP9', 'read-write',
            u"",
            0x2307B9AD, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT54 = RM_Field_MODEM_S_ANARAMP9_ANARAMPLUT54(self)
        self.zz_fdict['ANARAMPLUT54'] = self.ANARAMPLUT54
        self.ANARAMPLUT55 = RM_Field_MODEM_S_ANARAMP9_ANARAMPLUT55(self)
        self.zz_fdict['ANARAMPLUT55'] = self.ANARAMPLUT55
        self.ANARAMPLUT56 = RM_Field_MODEM_S_ANARAMP9_ANARAMPLUT56(self)
        self.zz_fdict['ANARAMPLUT56'] = self.ANARAMPLUT56
        self.ANARAMPLUT57 = RM_Field_MODEM_S_ANARAMP9_ANARAMPLUT57(self)
        self.zz_fdict['ANARAMPLUT57'] = self.ANARAMPLUT57
        self.ANARAMPLUT58 = RM_Field_MODEM_S_ANARAMP9_ANARAMPLUT58(self)
        self.zz_fdict['ANARAMPLUT58'] = self.ANARAMPLUT58
        self.ANARAMPLUT59 = RM_Field_MODEM_S_ANARAMP9_ANARAMPLUT59(self)
        self.zz_fdict['ANARAMPLUT59'] = self.ANARAMPLUT59
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANARAMP10(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANARAMP10, self).__init__(rmio, label,
            0xa8014000, 0x10C,
            'ANARAMP10', 'MODEM_S.ANARAMP10', 'read-write',
            u"",
            0x000FF2F3, 0x000FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANARAMPLUT60 = RM_Field_MODEM_S_ANARAMP10_ANARAMPLUT60(self)
        self.zz_fdict['ANARAMPLUT60'] = self.ANARAMPLUT60
        self.ANARAMPLUT61 = RM_Field_MODEM_S_ANARAMP10_ANARAMPLUT61(self)
        self.zz_fdict['ANARAMPLUT61'] = self.ANARAMPLUT61
        self.ANARAMPLUT62 = RM_Field_MODEM_S_ANARAMP10_ANARAMPLUT62(self)
        self.zz_fdict['ANARAMPLUT62'] = self.ANARAMPLUT62
        self.ANARAMPLUT63 = RM_Field_MODEM_S_ANARAMP10_ANARAMPLUT63(self)
        self.zz_fdict['ANARAMPLUT63'] = self.ANARAMPLUT63
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DCCOMP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DCCOMP, self).__init__(rmio, label,
            0xa8014000, 0x110,
            'DCCOMP', 'MODEM_S.DCCOMP', 'read-write',
            u"",
            0x00000030, 0x001FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DCESTIEN = RM_Field_MODEM_S_DCCOMP_DCESTIEN(self)
        self.zz_fdict['DCESTIEN'] = self.DCESTIEN
        self.DCCOMPEN = RM_Field_MODEM_S_DCCOMP_DCCOMPEN(self)
        self.zz_fdict['DCCOMPEN'] = self.DCCOMPEN
        self.DCRSTEN = RM_Field_MODEM_S_DCCOMP_DCRSTEN(self)
        self.zz_fdict['DCRSTEN'] = self.DCRSTEN
        self.DCCOMPFREEZE = RM_Field_MODEM_S_DCCOMP_DCCOMPFREEZE(self)
        self.zz_fdict['DCCOMPFREEZE'] = self.DCCOMPFREEZE
        self.DCCOMPGEAR = RM_Field_MODEM_S_DCCOMP_DCCOMPGEAR(self)
        self.zz_fdict['DCCOMPGEAR'] = self.DCCOMPGEAR
        self.DCLIMIT = RM_Field_MODEM_S_DCCOMP_DCLIMIT(self)
        self.zz_fdict['DCLIMIT'] = self.DCLIMIT
        self.DCGAINGEAREN = RM_Field_MODEM_S_DCCOMP_DCGAINGEAREN(self)
        self.zz_fdict['DCGAINGEAREN'] = self.DCGAINGEAREN
        self.DCGAINGEAR = RM_Field_MODEM_S_DCCOMP_DCGAINGEAR(self)
        self.zz_fdict['DCGAINGEAR'] = self.DCGAINGEAR
        self.DCGAINGEARSMPS = RM_Field_MODEM_S_DCCOMP_DCGAINGEARSMPS(self)
        self.zz_fdict['DCGAINGEARSMPS'] = self.DCGAINGEARSMPS
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DCCOMPFILTINIT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DCCOMPFILTINIT, self).__init__(rmio, label,
            0xa8014000, 0x114,
            'DCCOMPFILTINIT', 'MODEM_S.DCCOMPFILTINIT', 'read-write',
            u"",
            0x00000000, 0x7FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DCCOMPINITVALI = RM_Field_MODEM_S_DCCOMPFILTINIT_DCCOMPINITVALI(self)
        self.zz_fdict['DCCOMPINITVALI'] = self.DCCOMPINITVALI
        self.DCCOMPINITVALQ = RM_Field_MODEM_S_DCCOMPFILTINIT_DCCOMPINITVALQ(self)
        self.zz_fdict['DCCOMPINITVALQ'] = self.DCCOMPINITVALQ
        self.DCCOMPINIT = RM_Field_MODEM_S_DCCOMPFILTINIT_DCCOMPINIT(self)
        self.zz_fdict['DCCOMPINIT'] = self.DCCOMPINIT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DCESTI(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DCESTI, self).__init__(rmio, label,
            0xa8014000, 0x118,
            'DCESTI', 'MODEM_S.DCESTI', 'read-only',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DCCOMPESTIVALI = RM_Field_MODEM_S_DCESTI_DCCOMPESTIVALI(self)
        self.zz_fdict['DCCOMPESTIVALI'] = self.DCCOMPESTIVALI
        self.DCCOMPESTIVALQ = RM_Field_MODEM_S_DCESTI_DCCOMPESTIVALQ(self)
        self.zz_fdict['DCCOMPESTIVALQ'] = self.DCCOMPESTIVALQ
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SRCCHF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SRCCHF, self).__init__(rmio, label,
            0xa8014000, 0x11C,
            'SRCCHF', 'MODEM_S.SRCCHF', 'read-write',
            u"",
            0x00000000, 0x8FFFF000,
            0x00001000, 0x00002000,
            0x00003000)

        self.SRCRATIO2 = RM_Field_MODEM_S_SRCCHF_SRCRATIO2(self)
        self.zz_fdict['SRCRATIO2'] = self.SRCRATIO2
        self.SRCENABLE2 = RM_Field_MODEM_S_SRCCHF_SRCENABLE2(self)
        self.zz_fdict['SRCENABLE2'] = self.SRCENABLE2
        self.INTOSR = RM_Field_MODEM_S_SRCCHF_INTOSR(self)
        self.zz_fdict['INTOSR'] = self.INTOSR
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_INTAFC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_INTAFC, self).__init__(rmio, label,
            0xa8014000, 0x120,
            'INTAFC', 'MODEM_S.INTAFC', 'read-write',
            u"",
            0x00000000, 0x00FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.FOEPREAVG0 = RM_Field_MODEM_S_INTAFC_FOEPREAVG0(self)
        self.zz_fdict['FOEPREAVG0'] = self.FOEPREAVG0
        self.FOEPREAVG1 = RM_Field_MODEM_S_INTAFC_FOEPREAVG1(self)
        self.zz_fdict['FOEPREAVG1'] = self.FOEPREAVG1
        self.FOEPREAVG2 = RM_Field_MODEM_S_INTAFC_FOEPREAVG2(self)
        self.zz_fdict['FOEPREAVG2'] = self.FOEPREAVG2
        self.FOEPREAVG3 = RM_Field_MODEM_S_INTAFC_FOEPREAVG3(self)
        self.zz_fdict['FOEPREAVG3'] = self.FOEPREAVG3
        self.FOEPREAVG4 = RM_Field_MODEM_S_INTAFC_FOEPREAVG4(self)
        self.zz_fdict['FOEPREAVG4'] = self.FOEPREAVG4
        self.FOEPREAVG5 = RM_Field_MODEM_S_INTAFC_FOEPREAVG5(self)
        self.zz_fdict['FOEPREAVG5'] = self.FOEPREAVG5
        self.FOEPREAVG6 = RM_Field_MODEM_S_INTAFC_FOEPREAVG6(self)
        self.zz_fdict['FOEPREAVG6'] = self.FOEPREAVG6
        self.FOEPREAVG7 = RM_Field_MODEM_S_INTAFC_FOEPREAVG7(self)
        self.zz_fdict['FOEPREAVG7'] = self.FOEPREAVG7
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DSATHD0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DSATHD0, self).__init__(rmio, label,
            0xa8014000, 0x124,
            'DSATHD0', 'MODEM_S.DSATHD0', 'read-write',
            u"",
            0x07830464, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SPIKETHD = RM_Field_MODEM_S_DSATHD0_SPIKETHD(self)
        self.zz_fdict['SPIKETHD'] = self.SPIKETHD
        self.UNMODTHD = RM_Field_MODEM_S_DSATHD0_UNMODTHD(self)
        self.zz_fdict['UNMODTHD'] = self.UNMODTHD
        self.FDEVMINTHD = RM_Field_MODEM_S_DSATHD0_FDEVMINTHD(self)
        self.zz_fdict['FDEVMINTHD'] = self.FDEVMINTHD
        self.FDEVMAXTHD = RM_Field_MODEM_S_DSATHD0_FDEVMAXTHD(self)
        self.zz_fdict['FDEVMAXTHD'] = self.FDEVMAXTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DSATHD1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DSATHD1, self).__init__(rmio, label,
            0xa8014000, 0x128,
            'DSATHD1', 'MODEM_S.DSATHD1', 'read-write',
            u"",
            0x3AC81388, 0x7FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.POWABSTHD = RM_Field_MODEM_S_DSATHD1_POWABSTHD(self)
        self.zz_fdict['POWABSTHD'] = self.POWABSTHD
        self.POWRELTHD = RM_Field_MODEM_S_DSATHD1_POWRELTHD(self)
        self.zz_fdict['POWRELTHD'] = self.POWRELTHD
        self.DSARSTCNT = RM_Field_MODEM_S_DSATHD1_DSARSTCNT(self)
        self.zz_fdict['DSARSTCNT'] = self.DSARSTCNT
        self.RSSIJMPTHD = RM_Field_MODEM_S_DSATHD1_RSSIJMPTHD(self)
        self.zz_fdict['RSSIJMPTHD'] = self.RSSIJMPTHD
        self.FREQLATDLY = RM_Field_MODEM_S_DSATHD1_FREQLATDLY(self)
        self.zz_fdict['FREQLATDLY'] = self.FREQLATDLY
        self.PWRFLTBYP = RM_Field_MODEM_S_DSATHD1_PWRFLTBYP(self)
        self.zz_fdict['PWRFLTBYP'] = self.PWRFLTBYP
        self.AMPFLTBYP = RM_Field_MODEM_S_DSATHD1_AMPFLTBYP(self)
        self.zz_fdict['AMPFLTBYP'] = self.AMPFLTBYP
        self.PWRDETDIS = RM_Field_MODEM_S_DSATHD1_PWRDETDIS(self)
        self.zz_fdict['PWRDETDIS'] = self.PWRDETDIS
        self.FREQSCALE = RM_Field_MODEM_S_DSATHD1_FREQSCALE(self)
        self.zz_fdict['FREQSCALE'] = self.FREQSCALE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DSATHD2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DSATHD2, self).__init__(rmio, label,
            0xa8014000, 0x12C,
            'DSATHD2', 'MODEM_S.DSATHD2', 'read-write',
            u"",
            0x0C660664, 0x7FFFFEFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.POWABSTHDLOG = RM_Field_MODEM_S_DSATHD2_POWABSTHDLOG(self)
        self.zz_fdict['POWABSTHDLOG'] = self.POWABSTHDLOG
        self.JUMPDETEN = RM_Field_MODEM_S_DSATHD2_JUMPDETEN(self)
        self.zz_fdict['JUMPDETEN'] = self.JUMPDETEN
        self.FDADJTHD = RM_Field_MODEM_S_DSATHD2_FDADJTHD(self)
        self.zz_fdict['FDADJTHD'] = self.FDADJTHD
        self.PMDETPASSTHD = RM_Field_MODEM_S_DSATHD2_PMDETPASSTHD(self)
        self.zz_fdict['PMDETPASSTHD'] = self.PMDETPASSTHD
        self.FREQESTTHD = RM_Field_MODEM_S_DSATHD2_FREQESTTHD(self)
        self.zz_fdict['FREQESTTHD'] = self.FREQESTTHD
        self.INTERFERDET = RM_Field_MODEM_S_DSATHD2_INTERFERDET(self)
        self.zz_fdict['INTERFERDET'] = self.INTERFERDET
        self.PMDETFORCE = RM_Field_MODEM_S_DSATHD2_PMDETFORCE(self)
        self.zz_fdict['PMDETFORCE'] = self.PMDETFORCE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DSATHD3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DSATHD3, self).__init__(rmio, label,
            0xa8014000, 0x130,
            'DSATHD3', 'MODEM_S.DSATHD3', 'read-write',
            u"",
            0x07830464, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SPIKETHDLO = RM_Field_MODEM_S_DSATHD3_SPIKETHDLO(self)
        self.zz_fdict['SPIKETHDLO'] = self.SPIKETHDLO
        self.UNMODTHDLO = RM_Field_MODEM_S_DSATHD3_UNMODTHDLO(self)
        self.zz_fdict['UNMODTHDLO'] = self.UNMODTHDLO
        self.FDEVMINTHDLO = RM_Field_MODEM_S_DSATHD3_FDEVMINTHDLO(self)
        self.zz_fdict['FDEVMINTHDLO'] = self.FDEVMINTHDLO
        self.FDEVMAXTHDLO = RM_Field_MODEM_S_DSATHD3_FDEVMAXTHDLO(self)
        self.zz_fdict['FDEVMAXTHDLO'] = self.FDEVMAXTHDLO
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DSATHD4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DSATHD4, self).__init__(rmio, label,
            0xa8014000, 0x134,
            'DSATHD4', 'MODEM_S.DSATHD4', 'read-write',
            u"",
            0x00821388, 0x07FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.POWABSTHDLO = RM_Field_MODEM_S_DSATHD4_POWABSTHDLO(self)
        self.zz_fdict['POWABSTHDLO'] = self.POWABSTHDLO
        self.ARRTOLERTHD0LO = RM_Field_MODEM_S_DSATHD4_ARRTOLERTHD0LO(self)
        self.zz_fdict['ARRTOLERTHD0LO'] = self.ARRTOLERTHD0LO
        self.ARRTOLERTHD1LO = RM_Field_MODEM_S_DSATHD4_ARRTOLERTHD1LO(self)
        self.zz_fdict['ARRTOLERTHD1LO'] = self.ARRTOLERTHD1LO
        self.SWTHD = RM_Field_MODEM_S_DSATHD4_SWTHD(self)
        self.zz_fdict['SWTHD'] = self.SWTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DSACTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DSACTRL, self).__init__(rmio, label,
            0xa8014000, 0x138,
            'DSACTRL', 'MODEM_S.DSACTRL', 'read-write',
            u"",
            0x000A2090, 0xFFEFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DSAMODE = RM_Field_MODEM_S_DSACTRL_DSAMODE(self)
        self.zz_fdict['DSAMODE'] = self.DSAMODE
        self.ARRTHD = RM_Field_MODEM_S_DSACTRL_ARRTHD(self)
        self.zz_fdict['ARRTHD'] = self.ARRTHD
        self.ARRTOLERTHD0 = RM_Field_MODEM_S_DSACTRL_ARRTOLERTHD0(self)
        self.zz_fdict['ARRTOLERTHD0'] = self.ARRTOLERTHD0
        self.ARRTOLERTHD1 = RM_Field_MODEM_S_DSACTRL_ARRTOLERTHD1(self)
        self.zz_fdict['ARRTOLERTHD1'] = self.ARRTOLERTHD1
        self.SCHPRD = RM_Field_MODEM_S_DSACTRL_SCHPRD(self)
        self.zz_fdict['SCHPRD'] = self.SCHPRD
        self.FREQAVGSYM = RM_Field_MODEM_S_DSACTRL_FREQAVGSYM(self)
        self.zz_fdict['FREQAVGSYM'] = self.FREQAVGSYM
        self.TRANRSTDSA = RM_Field_MODEM_S_DSACTRL_TRANRSTDSA(self)
        self.zz_fdict['TRANRSTDSA'] = self.TRANRSTDSA
        self.DSARSTON = RM_Field_MODEM_S_DSACTRL_DSARSTON(self)
        self.zz_fdict['DSARSTON'] = self.DSARSTON
        self.GAINREDUCDLY = RM_Field_MODEM_S_DSACTRL_GAINREDUCDLY(self)
        self.zz_fdict['GAINREDUCDLY'] = self.GAINREDUCDLY
        self.LOWDUTY = RM_Field_MODEM_S_DSACTRL_LOWDUTY(self)
        self.zz_fdict['LOWDUTY'] = self.LOWDUTY
        self.RESTORE = RM_Field_MODEM_S_DSACTRL_RESTORE(self)
        self.zz_fdict['RESTORE'] = self.RESTORE
        self.AGCBAUDEN = RM_Field_MODEM_S_DSACTRL_AGCBAUDEN(self)
        self.zz_fdict['AGCBAUDEN'] = self.AGCBAUDEN
        self.AMPJUPTHD = RM_Field_MODEM_S_DSACTRL_AMPJUPTHD(self)
        self.zz_fdict['AMPJUPTHD'] = self.AMPJUPTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DIGMIXCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DIGMIXCTRL, self).__init__(rmio, label,
            0xa8014000, 0x13C,
            'DIGMIXCTRL', 'MODEM_S.DIGMIXCTRL', 'read-write',
            u"",
            0x00000000, 0x007FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DIGMIXFREQ = RM_Field_MODEM_S_DIGMIXCTRL_DIGMIXFREQ(self)
        self.zz_fdict['DIGMIXFREQ'] = self.DIGMIXFREQ
        self.DIGMIXMODE = RM_Field_MODEM_S_DIGMIXCTRL_DIGMIXMODE(self)
        self.zz_fdict['DIGMIXMODE'] = self.DIGMIXMODE
        self.MIXERCONJ = RM_Field_MODEM_S_DIGMIXCTRL_MIXERCONJ(self)
        self.zz_fdict['MIXERCONJ'] = self.MIXERCONJ
        self.DIGMIXFB = RM_Field_MODEM_S_DIGMIXCTRL_DIGMIXFB(self)
        self.zz_fdict['DIGMIXFB'] = self.DIGMIXFB
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_VITERBIDEMOD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_VITERBIDEMOD, self).__init__(rmio, label,
            0xa8014000, 0x140,
            'VITERBIDEMOD', 'MODEM_S.VITERBIDEMOD', 'read-write',
            u"",
            0x00206100, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.VTDEMODEN = RM_Field_MODEM_S_VITERBIDEMOD_VTDEMODEN(self)
        self.zz_fdict['VTDEMODEN'] = self.VTDEMODEN
        self.HARDDECISION = RM_Field_MODEM_S_VITERBIDEMOD_HARDDECISION(self)
        self.zz_fdict['HARDDECISION'] = self.HARDDECISION
        self.VITERBIKSI1 = RM_Field_MODEM_S_VITERBIDEMOD_VITERBIKSI1(self)
        self.zz_fdict['VITERBIKSI1'] = self.VITERBIKSI1
        self.VITERBIKSI2 = RM_Field_MODEM_S_VITERBIDEMOD_VITERBIKSI2(self)
        self.zz_fdict['VITERBIKSI2'] = self.VITERBIKSI2
        self.VITERBIKSI3 = RM_Field_MODEM_S_VITERBIDEMOD_VITERBIKSI3(self)
        self.zz_fdict['VITERBIKSI3'] = self.VITERBIKSI3
        self.SYNTHAFC = RM_Field_MODEM_S_VITERBIDEMOD_SYNTHAFC(self)
        self.zz_fdict['SYNTHAFC'] = self.SYNTHAFC
        self.CORRCYCLE = RM_Field_MODEM_S_VITERBIDEMOD_CORRCYCLE(self)
        self.zz_fdict['CORRCYCLE'] = self.CORRCYCLE
        self.CORRSTPSIZE = RM_Field_MODEM_S_VITERBIDEMOD_CORRSTPSIZE(self)
        self.zz_fdict['CORRSTPSIZE'] = self.CORRSTPSIZE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_VTCORRCFG0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_VTCORRCFG0, self).__init__(rmio, label,
            0xa8014000, 0x144,
            'VTCORRCFG0', 'MODEM_S.VTCORRCFG0', 'read-write',
            u"",
            0x123556B7, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.EXPECTPATT = RM_Field_MODEM_S_VTCORRCFG0_EXPECTPATT(self)
        self.zz_fdict['EXPECTPATT'] = self.EXPECTPATT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_VTCORRCFG1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_VTCORRCFG1, self).__init__(rmio, label,
            0xa8014000, 0x148,
            'VTCORRCFG1', 'MODEM_S.VTCORRCFG1', 'read-write',
            u"",
            0x5020C000, 0xF7FDFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.VITERBIKSI3WB = RM_Field_MODEM_S_VTCORRCFG1_VITERBIKSI3WB(self)
        self.zz_fdict['VITERBIKSI3WB'] = self.VITERBIKSI3WB
        self.KSI3SWENABLE = RM_Field_MODEM_S_VTCORRCFG1_KSI3SWENABLE(self)
        self.zz_fdict['KSI3SWENABLE'] = self.KSI3SWENABLE
        self.VTFRQLIM = RM_Field_MODEM_S_VTCORRCFG1_VTFRQLIM(self)
        self.zz_fdict['VTFRQLIM'] = self.VTFRQLIM
        self.EXPSYNCLEN = RM_Field_MODEM_S_VTCORRCFG1_EXPSYNCLEN(self)
        self.zz_fdict['EXPSYNCLEN'] = self.EXPSYNCLEN
        self.EXPECTHT = RM_Field_MODEM_S_VTCORRCFG1_EXPECTHT(self)
        self.zz_fdict['EXPECTHT'] = self.EXPECTHT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_VTTRACK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_VTTRACK, self).__init__(rmio, label,
            0xa8014000, 0x14C,
            'VTTRACK', 'MODEM_S.VTTRACK', 'read-write',
            u"",
            0x0D803B88, 0x3FFF3FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.FREQTRACKMODE = RM_Field_MODEM_S_VTTRACK_FREQTRACKMODE(self)
        self.zz_fdict['FREQTRACKMODE'] = self.FREQTRACKMODE
        self.TIMTRACKTHD = RM_Field_MODEM_S_VTTRACK_TIMTRACKTHD(self)
        self.zz_fdict['TIMTRACKTHD'] = self.TIMTRACKTHD
        self.TIMEACQUTHD = RM_Field_MODEM_S_VTTRACK_TIMEACQUTHD(self)
        self.zz_fdict['TIMEACQUTHD'] = self.TIMEACQUTHD
        self.TIMGEAR = RM_Field_MODEM_S_VTTRACK_TIMGEAR(self)
        self.zz_fdict['TIMGEAR'] = self.TIMGEAR
        self.FREQBIAS = RM_Field_MODEM_S_VTTRACK_FREQBIAS(self)
        self.zz_fdict['FREQBIAS'] = self.FREQBIAS
        self.HIPWRTHD = RM_Field_MODEM_S_VTTRACK_HIPWRTHD(self)
        self.zz_fdict['HIPWRTHD'] = self.HIPWRTHD
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_VTBLETIMING(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_VTBLETIMING, self).__init__(rmio, label,
            0xa8014000, 0x150,
            'VTBLETIMING', 'MODEM_S.VTBLETIMING', 'read-write',
            u"",
            0x00000000, 0x8000FFF3,
            0x00001000, 0x00002000,
            0x00003000)

        self.VTBLETIMINGSEL = RM_Field_MODEM_S_VTBLETIMING_VTBLETIMINGSEL(self)
        self.zz_fdict['VTBLETIMINGSEL'] = self.VTBLETIMINGSEL
        self.TIMINGDELAY = RM_Field_MODEM_S_VTBLETIMING_TIMINGDELAY(self)
        self.zz_fdict['TIMINGDELAY'] = self.TIMINGDELAY
        self.FLENOFF = RM_Field_MODEM_S_VTBLETIMING_FLENOFF(self)
        self.zz_fdict['FLENOFF'] = self.FLENOFF
        self.DISDEMODOF = RM_Field_MODEM_S_VTBLETIMING_DISDEMODOF(self)
        self.zz_fdict['DISDEMODOF'] = self.DISDEMODOF
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BREST(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BREST, self).__init__(rmio, label,
            0xa8014000, 0x154,
            'BREST', 'MODEM_S.BREST', 'read-only',
            u"",
            0x00000000, 0x000007FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.BRESTINT = RM_Field_MODEM_S_BREST_BRESTINT(self)
        self.zz_fdict['BRESTINT'] = self.BRESTINT
        self.BRESTNUM = RM_Field_MODEM_S_BREST_BRESTNUM(self)
        self.zz_fdict['BRESTNUM'] = self.BRESTNUM
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_AUTOCG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_AUTOCG, self).__init__(rmio, label,
            0xa8014000, 0x158,
            'AUTOCG', 'MODEM_S.AUTOCG', 'read-write',
            u"",
            0x00000000, 0x0000FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.AUTOCGEN = RM_Field_MODEM_S_AUTOCG_AUTOCGEN(self)
        self.zz_fdict['AUTOCGEN'] = self.AUTOCGEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CGCLKSTOP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CGCLKSTOP, self).__init__(rmio, label,
            0xa8014000, 0x15C,
            'CGCLKSTOP', 'MODEM_S.CGCLKSTOP', 'read-write',
            u"",
            0x00000000, 0x0000FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.FORCEOFF = RM_Field_MODEM_S_CGCLKSTOP_FORCEOFF(self)
        self.zz_fdict['FORCEOFF'] = self.FORCEOFF
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_POE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_POE, self).__init__(rmio, label,
            0xa8014000, 0x160,
            'POE', 'MODEM_S.POE', 'read-only',
            u"",
            0x00000000, 0x03FF03FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.POEI = RM_Field_MODEM_S_POE_POEI(self)
        self.zz_fdict['POEI'] = self.POEI
        self.POEQ = RM_Field_MODEM_S_POE_POEQ(self)
        self.zz_fdict['POEQ'] = self.POEQ
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DIRECTMODE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DIRECTMODE, self).__init__(rmio, label,
            0xa8014000, 0x164,
            'DIRECTMODE', 'MODEM_S.DIRECTMODE', 'read-write',
            u"",
            0x0000010C, 0x00001F0F,
            0x00001000, 0x00002000,
            0x00003000)

        self.DMENABLE = RM_Field_MODEM_S_DIRECTMODE_DMENABLE(self)
        self.zz_fdict['DMENABLE'] = self.DMENABLE
        self.SYNCASYNC = RM_Field_MODEM_S_DIRECTMODE_SYNCASYNC(self)
        self.zz_fdict['SYNCASYNC'] = self.SYNCASYNC
        self.SYNCPREAM = RM_Field_MODEM_S_DIRECTMODE_SYNCPREAM(self)
        self.zz_fdict['SYNCPREAM'] = self.SYNCPREAM
        self.CLKWIDTH = RM_Field_MODEM_S_DIRECTMODE_CLKWIDTH(self)
        self.zz_fdict['CLKWIDTH'] = self.CLKWIDTH
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_LONGRANGE1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_LONGRANGE1, self).__init__(rmio, label,
            0xa8014000, 0x16C,
            'LONGRANGE1', 'MODEM_S.LONGRANGE1', 'read-write',
            u"",
            0x40000000, 0xFFFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LRSS = RM_Field_MODEM_S_LONGRANGE1_LRSS(self)
        self.zz_fdict['LRSS'] = self.LRSS
        self.LRTIMEOUTTHD = RM_Field_MODEM_S_LONGRANGE1_LRTIMEOUTTHD(self)
        self.zz_fdict['LRTIMEOUTTHD'] = self.LRTIMEOUTTHD
        self.CHPWRACCUDEL = RM_Field_MODEM_S_LONGRANGE1_CHPWRACCUDEL(self)
        self.zz_fdict['CHPWRACCUDEL'] = self.CHPWRACCUDEL
        self.HYSVAL = RM_Field_MODEM_S_LONGRANGE1_HYSVAL(self)
        self.zz_fdict['HYSVAL'] = self.HYSVAL
        self.AVGWIN = RM_Field_MODEM_S_LONGRANGE1_AVGWIN(self)
        self.zz_fdict['AVGWIN'] = self.AVGWIN
        self.LRSPIKETHADD = RM_Field_MODEM_S_LONGRANGE1_LRSPIKETHADD(self)
        self.zz_fdict['LRSPIKETHADD'] = self.LRSPIKETHADD
        self.LOGICBASEDPUGATE = RM_Field_MODEM_S_LONGRANGE1_LOGICBASEDPUGATE(self)
        self.zz_fdict['LOGICBASEDPUGATE'] = self.LOGICBASEDPUGATE
        self.LOGICBASEDLRDEMODGATE = RM_Field_MODEM_S_LONGRANGE1_LOGICBASEDLRDEMODGATE(self)
        self.zz_fdict['LOGICBASEDLRDEMODGATE'] = self.LOGICBASEDLRDEMODGATE
        self.PREFILTLEN = RM_Field_MODEM_S_LONGRANGE1_PREFILTLEN(self)
        self.zz_fdict['PREFILTLEN'] = self.PREFILTLEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_LONGRANGE2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_LONGRANGE2, self).__init__(rmio, label,
            0xa8014000, 0x170,
            'LONGRANGE2', 'MODEM_S.LONGRANGE2', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LRCHPWRTH1 = RM_Field_MODEM_S_LONGRANGE2_LRCHPWRTH1(self)
        self.zz_fdict['LRCHPWRTH1'] = self.LRCHPWRTH1
        self.LRCHPWRTH2 = RM_Field_MODEM_S_LONGRANGE2_LRCHPWRTH2(self)
        self.zz_fdict['LRCHPWRTH2'] = self.LRCHPWRTH2
        self.LRCHPWRTH3 = RM_Field_MODEM_S_LONGRANGE2_LRCHPWRTH3(self)
        self.zz_fdict['LRCHPWRTH3'] = self.LRCHPWRTH3
        self.LRCHPWRTH4 = RM_Field_MODEM_S_LONGRANGE2_LRCHPWRTH4(self)
        self.zz_fdict['LRCHPWRTH4'] = self.LRCHPWRTH4
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_LONGRANGE3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_LONGRANGE3, self).__init__(rmio, label,
            0xa8014000, 0x174,
            'LONGRANGE3', 'MODEM_S.LONGRANGE3', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LRCHPWRTH5 = RM_Field_MODEM_S_LONGRANGE3_LRCHPWRTH5(self)
        self.zz_fdict['LRCHPWRTH5'] = self.LRCHPWRTH5
        self.LRCHPWRTH6 = RM_Field_MODEM_S_LONGRANGE3_LRCHPWRTH6(self)
        self.zz_fdict['LRCHPWRTH6'] = self.LRCHPWRTH6
        self.LRCHPWRTH7 = RM_Field_MODEM_S_LONGRANGE3_LRCHPWRTH7(self)
        self.zz_fdict['LRCHPWRTH7'] = self.LRCHPWRTH7
        self.LRCHPWRTH8 = RM_Field_MODEM_S_LONGRANGE3_LRCHPWRTH8(self)
        self.zz_fdict['LRCHPWRTH8'] = self.LRCHPWRTH8
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_LONGRANGE4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_LONGRANGE4, self).__init__(rmio, label,
            0xa8014000, 0x178,
            'LONGRANGE4', 'MODEM_S.LONGRANGE4', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LRCHPWRTH9 = RM_Field_MODEM_S_LONGRANGE4_LRCHPWRTH9(self)
        self.zz_fdict['LRCHPWRTH9'] = self.LRCHPWRTH9
        self.LRCHPWRTH10 = RM_Field_MODEM_S_LONGRANGE4_LRCHPWRTH10(self)
        self.zz_fdict['LRCHPWRTH10'] = self.LRCHPWRTH10
        self.LRCHPWRSH1 = RM_Field_MODEM_S_LONGRANGE4_LRCHPWRSH1(self)
        self.zz_fdict['LRCHPWRSH1'] = self.LRCHPWRSH1
        self.LRCHPWRSH2 = RM_Field_MODEM_S_LONGRANGE4_LRCHPWRSH2(self)
        self.zz_fdict['LRCHPWRSH2'] = self.LRCHPWRSH2
        self.LRCHPWRSH3 = RM_Field_MODEM_S_LONGRANGE4_LRCHPWRSH3(self)
        self.zz_fdict['LRCHPWRSH3'] = self.LRCHPWRSH3
        self.LRCHPWRSH4 = RM_Field_MODEM_S_LONGRANGE4_LRCHPWRSH4(self)
        self.zz_fdict['LRCHPWRSH4'] = self.LRCHPWRSH4
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_LONGRANGE5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_LONGRANGE5, self).__init__(rmio, label,
            0xa8014000, 0x17C,
            'LONGRANGE5', 'MODEM_S.LONGRANGE5', 'read-write',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LRCHPWRSH5 = RM_Field_MODEM_S_LONGRANGE5_LRCHPWRSH5(self)
        self.zz_fdict['LRCHPWRSH5'] = self.LRCHPWRSH5
        self.LRCHPWRSH6 = RM_Field_MODEM_S_LONGRANGE5_LRCHPWRSH6(self)
        self.zz_fdict['LRCHPWRSH6'] = self.LRCHPWRSH6
        self.LRCHPWRSH7 = RM_Field_MODEM_S_LONGRANGE5_LRCHPWRSH7(self)
        self.zz_fdict['LRCHPWRSH7'] = self.LRCHPWRSH7
        self.LRCHPWRSH8 = RM_Field_MODEM_S_LONGRANGE5_LRCHPWRSH8(self)
        self.zz_fdict['LRCHPWRSH8'] = self.LRCHPWRSH8
        self.LRCHPWRSH9 = RM_Field_MODEM_S_LONGRANGE5_LRCHPWRSH9(self)
        self.zz_fdict['LRCHPWRSH9'] = self.LRCHPWRSH9
        self.LRCHPWRSH10 = RM_Field_MODEM_S_LONGRANGE5_LRCHPWRSH10(self)
        self.zz_fdict['LRCHPWRSH10'] = self.LRCHPWRSH10
        self.LRCHPWRSH11 = RM_Field_MODEM_S_LONGRANGE5_LRCHPWRSH11(self)
        self.zz_fdict['LRCHPWRSH11'] = self.LRCHPWRSH11
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_LONGRANGE6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_LONGRANGE6, self).__init__(rmio, label,
            0xa8014000, 0x180,
            'LONGRANGE6', 'MODEM_S.LONGRANGE6', 'read-write',
            u"",
            0x00000000, 0xFFF7FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LRCHPWRSPIKETH = RM_Field_MODEM_S_LONGRANGE6_LRCHPWRSPIKETH(self)
        self.zz_fdict['LRCHPWRSPIKETH'] = self.LRCHPWRSPIKETH
        self.LRSPIKETHD = RM_Field_MODEM_S_LONGRANGE6_LRSPIKETHD(self)
        self.zz_fdict['LRSPIKETHD'] = self.LRSPIKETHD
        self.LRCHPWRTH11 = RM_Field_MODEM_S_LONGRANGE6_LRCHPWRTH11(self)
        self.zz_fdict['LRCHPWRTH11'] = self.LRCHPWRTH11
        self.LRCHPWRSH12 = RM_Field_MODEM_S_LONGRANGE6_LRCHPWRSH12(self)
        self.zz_fdict['LRCHPWRSH12'] = self.LRCHPWRSH12
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_LRFRC(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_LRFRC, self).__init__(rmio, label,
            0xa8014000, 0x184,
            'LRFRC', 'MODEM_S.LRFRC', 'read-write',
            u"",
            0x00000101, 0x000001FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CI500 = RM_Field_MODEM_S_LRFRC_CI500(self)
        self.zz_fdict['CI500'] = self.CI500
        self.FRCACKTIMETHD = RM_Field_MODEM_S_LRFRC_FRCACKTIMETHD(self)
        self.zz_fdict['FRCACKTIMETHD'] = self.FRCACKTIMETHD
        self.LRCORRMODE = RM_Field_MODEM_S_LRFRC_LRCORRMODE(self)
        self.zz_fdict['LRCORRMODE'] = self.LRCORRMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_COH0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_COH0, self).__init__(rmio, label,
            0xa8014000, 0x188,
            'COH0', 'MODEM_S.COH0', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COHDYNAMICBBSSEN = RM_Field_MODEM_S_COH0_COHDYNAMICBBSSEN(self)
        self.zz_fdict['COHDYNAMICBBSSEN'] = self.COHDYNAMICBBSSEN
        self.COHDYNAMICSYNCTHRESH = RM_Field_MODEM_S_COH0_COHDYNAMICSYNCTHRESH(self)
        self.zz_fdict['COHDYNAMICSYNCTHRESH'] = self.COHDYNAMICSYNCTHRESH
        self.COHDYNAMICPRETHRESH = RM_Field_MODEM_S_COH0_COHDYNAMICPRETHRESH(self)
        self.zz_fdict['COHDYNAMICPRETHRESH'] = self.COHDYNAMICPRETHRESH
        self.COHCHPWRLOCK = RM_Field_MODEM_S_COH0_COHCHPWRLOCK(self)
        self.zz_fdict['COHCHPWRLOCK'] = self.COHCHPWRLOCK
        self.COHCHPWRRESTART = RM_Field_MODEM_S_COH0_COHCHPWRRESTART(self)
        self.zz_fdict['COHCHPWRRESTART'] = self.COHCHPWRRESTART
        self.COHDYNAMICPRETHRESHSEL = RM_Field_MODEM_S_COH0_COHDYNAMICPRETHRESHSEL(self)
        self.zz_fdict['COHDYNAMICPRETHRESHSEL'] = self.COHDYNAMICPRETHRESHSEL
        self.COHCHPWRTH0 = RM_Field_MODEM_S_COH0_COHCHPWRTH0(self)
        self.zz_fdict['COHCHPWRTH0'] = self.COHCHPWRTH0
        self.COHCHPWRTH1 = RM_Field_MODEM_S_COH0_COHCHPWRTH1(self)
        self.zz_fdict['COHCHPWRTH1'] = self.COHCHPWRTH1
        self.COHCHPWRTH2 = RM_Field_MODEM_S_COH0_COHCHPWRTH2(self)
        self.zz_fdict['COHCHPWRTH2'] = self.COHCHPWRTH2
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_COH1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_COH1, self).__init__(rmio, label,
            0xa8014000, 0x18C,
            'COH1', 'MODEM_S.COH1', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SYNCTHRESH0 = RM_Field_MODEM_S_COH1_SYNCTHRESH0(self)
        self.zz_fdict['SYNCTHRESH0'] = self.SYNCTHRESH0
        self.SYNCTHRESH1 = RM_Field_MODEM_S_COH1_SYNCTHRESH1(self)
        self.zz_fdict['SYNCTHRESH1'] = self.SYNCTHRESH1
        self.SYNCTHRESH2 = RM_Field_MODEM_S_COH1_SYNCTHRESH2(self)
        self.zz_fdict['SYNCTHRESH2'] = self.SYNCTHRESH2
        self.SYNCTHRESH3 = RM_Field_MODEM_S_COH1_SYNCTHRESH3(self)
        self.zz_fdict['SYNCTHRESH3'] = self.SYNCTHRESH3
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_COH2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_COH2, self).__init__(rmio, label,
            0xa8014000, 0x190,
            'COH2', 'MODEM_S.COH2', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SYNCTHRESHDELTA0 = RM_Field_MODEM_S_COH2_SYNCTHRESHDELTA0(self)
        self.zz_fdict['SYNCTHRESHDELTA0'] = self.SYNCTHRESHDELTA0
        self.SYNCTHRESHDELTA1 = RM_Field_MODEM_S_COH2_SYNCTHRESHDELTA1(self)
        self.zz_fdict['SYNCTHRESHDELTA1'] = self.SYNCTHRESHDELTA1
        self.SYNCTHRESHDELTA2 = RM_Field_MODEM_S_COH2_SYNCTHRESHDELTA2(self)
        self.zz_fdict['SYNCTHRESHDELTA2'] = self.SYNCTHRESHDELTA2
        self.SYNCTHRESHDELTA3 = RM_Field_MODEM_S_COH2_SYNCTHRESHDELTA3(self)
        self.zz_fdict['SYNCTHRESHDELTA3'] = self.SYNCTHRESHDELTA3
        self.DSAPEAKCHPWRTH = RM_Field_MODEM_S_COH2_DSAPEAKCHPWRTH(self)
        self.zz_fdict['DSAPEAKCHPWRTH'] = self.DSAPEAKCHPWRTH
        self.FIXEDCDTHFORIIR = RM_Field_MODEM_S_COH2_FIXEDCDTHFORIIR(self)
        self.zz_fdict['FIXEDCDTHFORIIR'] = self.FIXEDCDTHFORIIR
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_COH3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_COH3, self).__init__(rmio, label,
            0xa8014000, 0x194,
            'COH3', 'MODEM_S.COH3', 'read-write',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.COHDSAEN = RM_Field_MODEM_S_COH3_COHDSAEN(self)
        self.zz_fdict['COHDSAEN'] = self.COHDSAEN
        self.COHDSAADDWNDSIZE = RM_Field_MODEM_S_COH3_COHDSAADDWNDSIZE(self)
        self.zz_fdict['COHDSAADDWNDSIZE'] = self.COHDSAADDWNDSIZE
        self.CDSS = RM_Field_MODEM_S_COH3_CDSS(self)
        self.zz_fdict['CDSS'] = self.CDSS
        self.DSAPEAKCHKEN = RM_Field_MODEM_S_COH3_DSAPEAKCHKEN(self)
        self.zz_fdict['DSAPEAKCHKEN'] = self.DSAPEAKCHKEN
        self.DSAPEAKINDLEN = RM_Field_MODEM_S_COH3_DSAPEAKINDLEN(self)
        self.zz_fdict['DSAPEAKINDLEN'] = self.DSAPEAKINDLEN
        self.DSAPEAKCHPWREN = RM_Field_MODEM_S_COH3_DSAPEAKCHPWREN(self)
        self.zz_fdict['DSAPEAKCHPWREN'] = self.DSAPEAKCHPWREN
        self.LOGICBASEDCOHDEMODGATE = RM_Field_MODEM_S_COH3_LOGICBASEDCOHDEMODGATE(self)
        self.zz_fdict['LOGICBASEDCOHDEMODGATE'] = self.LOGICBASEDCOHDEMODGATE
        self.DYNIIRCOEFOPTION = RM_Field_MODEM_S_COH3_DYNIIRCOEFOPTION(self)
        self.zz_fdict['DYNIIRCOEFOPTION'] = self.DYNIIRCOEFOPTION
        self.ONEPEAKQUALEN = RM_Field_MODEM_S_COH3_ONEPEAKQUALEN(self)
        self.zz_fdict['ONEPEAKQUALEN'] = self.ONEPEAKQUALEN
        self.PEAKCHKTIMOUT = RM_Field_MODEM_S_COH3_PEAKCHKTIMOUT(self)
        self.zz_fdict['PEAKCHKTIMOUT'] = self.PEAKCHKTIMOUT
        self.COHDSADETDIS = RM_Field_MODEM_S_COH3_COHDSADETDIS(self)
        self.zz_fdict['COHDSADETDIS'] = self.COHDSADETDIS
        self.COHDSACMPLX = RM_Field_MODEM_S_COH3_COHDSACMPLX(self)
        self.zz_fdict['COHDSACMPLX'] = self.COHDSACMPLX
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CMD(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CMD, self).__init__(rmio, label,
            0xa8014000, 0x198,
            'CMD', 'MODEM_S.CMD', 'write-only',
            u"",
            0x00000000, 0x0000003B,
            0x00001000, 0x00002000,
            0x00003000)

        self.PRESTOP = RM_Field_MODEM_S_CMD_PRESTOP(self)
        self.zz_fdict['PRESTOP'] = self.PRESTOP
        self.CHPWRACCUCLR = RM_Field_MODEM_S_CMD_CHPWRACCUCLR(self)
        self.zz_fdict['CHPWRACCUCLR'] = self.CHPWRACCUCLR
        self.AFCTXLOCK = RM_Field_MODEM_S_CMD_AFCTXLOCK(self)
        self.zz_fdict['AFCTXLOCK'] = self.AFCTXLOCK
        self.AFCTXCLEAR = RM_Field_MODEM_S_CMD_AFCTXCLEAR(self)
        self.zz_fdict['AFCTXCLEAR'] = self.AFCTXCLEAR
        self.AFCRXCLEAR = RM_Field_MODEM_S_CMD_AFCRXCLEAR(self)
        self.zz_fdict['AFCRXCLEAR'] = self.AFCRXCLEAR
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SYNCPROPERTIES(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SYNCPROPERTIES, self).__init__(rmio, label,
            0xa8014000, 0x1A4,
            'SYNCPROPERTIES', 'MODEM_S.SYNCPROPERTIES', 'read-write',
            u"",
            0x00000000, 0x0001FF00,
            0x00001000, 0x00002000,
            0x00003000)

        self.STATICSYNCTHRESHEN = RM_Field_MODEM_S_SYNCPROPERTIES_STATICSYNCTHRESHEN(self)
        self.zz_fdict['STATICSYNCTHRESHEN'] = self.STATICSYNCTHRESHEN
        self.STATICSYNCTHRESH = RM_Field_MODEM_S_SYNCPROPERTIES_STATICSYNCTHRESH(self)
        self.zz_fdict['STATICSYNCTHRESH'] = self.STATICSYNCTHRESH
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_DIGIGAINCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_DIGIGAINCTRL, self).__init__(rmio, label,
            0xa8014000, 0x1A8,
            'DIGIGAINCTRL', 'MODEM_S.DIGIGAINCTRL', 'read-write',
            u"",
            0x00000000, 0x000001FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.DIGIGAINEN = RM_Field_MODEM_S_DIGIGAINCTRL_DIGIGAINEN(self)
        self.zz_fdict['DIGIGAINEN'] = self.DIGIGAINEN
        self.DIGIGAINSEL = RM_Field_MODEM_S_DIGIGAINCTRL_DIGIGAINSEL(self)
        self.zz_fdict['DIGIGAINSEL'] = self.DIGIGAINSEL
        self.DIGIGAINDOUBLE = RM_Field_MODEM_S_DIGIGAINCTRL_DIGIGAINDOUBLE(self)
        self.zz_fdict['DIGIGAINDOUBLE'] = self.DIGIGAINDOUBLE
        self.DIGIGAINHALF = RM_Field_MODEM_S_DIGIGAINCTRL_DIGIGAINHALF(self)
        self.zz_fdict['DIGIGAINHALF'] = self.DIGIGAINHALF
        self.DEC0GAIN = RM_Field_MODEM_S_DIGIGAINCTRL_DEC0GAIN(self)
        self.zz_fdict['DEC0GAIN'] = self.DEC0GAIN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_PRSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_PRSCTRL, self).__init__(rmio, label,
            0xa8014000, 0x1AC,
            'PRSCTRL', 'MODEM_S.PRSCTRL', 'read-write',
            u"",
            0x00000000, 0x000FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.POSTPONESEL = RM_Field_MODEM_S_PRSCTRL_POSTPONESEL(self)
        self.zz_fdict['POSTPONESEL'] = self.POSTPONESEL
        self.ADVANCESEL = RM_Field_MODEM_S_PRSCTRL_ADVANCESEL(self)
        self.zz_fdict['ADVANCESEL'] = self.ADVANCESEL
        self.NEWWNDSEL = RM_Field_MODEM_S_PRSCTRL_NEWWNDSEL(self)
        self.zz_fdict['NEWWNDSEL'] = self.NEWWNDSEL
        self.WEAKSEL = RM_Field_MODEM_S_PRSCTRL_WEAKSEL(self)
        self.zz_fdict['WEAKSEL'] = self.WEAKSEL
        self.SYNCSENTSEL = RM_Field_MODEM_S_PRSCTRL_SYNCSENTSEL(self)
        self.zz_fdict['SYNCSENTSEL'] = self.SYNCSENTSEL
        self.PRESENTSEL = RM_Field_MODEM_S_PRSCTRL_PRESENTSEL(self)
        self.zz_fdict['PRESENTSEL'] = self.PRESENTSEL
        self.LOWCORRSEL = RM_Field_MODEM_S_PRSCTRL_LOWCORRSEL(self)
        self.zz_fdict['LOWCORRSEL'] = self.LOWCORRSEL
        self.ANT0SEL = RM_Field_MODEM_S_PRSCTRL_ANT0SEL(self)
        self.zz_fdict['ANT0SEL'] = self.ANT0SEL
        self.ANT1SEL = RM_Field_MODEM_S_PRSCTRL_ANT1SEL(self)
        self.zz_fdict['ANT1SEL'] = self.ANT1SEL
        self.IFADCCLKSEL = RM_Field_MODEM_S_PRSCTRL_IFADCCLKSEL(self)
        self.zz_fdict['IFADCCLKSEL'] = self.IFADCCLKSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_PADEBUG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_PADEBUG, self).__init__(rmio, label,
            0xa8014000, 0x1B0,
            'PADEBUG', 'MODEM_S.PADEBUG', 'read-write',
            u"",
            0x00000000, 0x00001E00,
            0x00001000, 0x00002000,
            0x00003000)

        self.MANPACLKAMPCTRL = RM_Field_MODEM_S_PADEBUG_MANPACLKAMPCTRL(self)
        self.zz_fdict['MANPACLKAMPCTRL'] = self.MANPACLKAMPCTRL
        self.ENMANPACLKAMPCTRL = RM_Field_MODEM_S_PADEBUG_ENMANPACLKAMPCTRL(self)
        self.zz_fdict['ENMANPACLKAMPCTRL'] = self.ENMANPACLKAMPCTRL
        self.ENMANPAPOWER = RM_Field_MODEM_S_PADEBUG_ENMANPAPOWER(self)
        self.zz_fdict['ENMANPAPOWER'] = self.ENMANPAPOWER
        self.ENMANPASELSLICE = RM_Field_MODEM_S_PADEBUG_ENMANPASELSLICE(self)
        self.zz_fdict['ENMANPASELSLICE'] = self.ENMANPASELSLICE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_REALTIMCFE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_REALTIMCFE, self).__init__(rmio, label,
            0xa8014000, 0x1B4,
            'REALTIMCFE', 'MODEM_S.REALTIMCFE', 'read-write',
            u"",
            0x001F81F4, 0xE03FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.MINCOSTTHD = RM_Field_MODEM_S_REALTIMCFE_MINCOSTTHD(self)
        self.zz_fdict['MINCOSTTHD'] = self.MINCOSTTHD
        self.RTSCHWIN = RM_Field_MODEM_S_REALTIMCFE_RTSCHWIN(self)
        self.zz_fdict['RTSCHWIN'] = self.RTSCHWIN
        self.RTSCHMODE = RM_Field_MODEM_S_REALTIMCFE_RTSCHMODE(self)
        self.zz_fdict['RTSCHMODE'] = self.RTSCHMODE
        self.TRACKINGWIN = RM_Field_MODEM_S_REALTIMCFE_TRACKINGWIN(self)
        self.zz_fdict['TRACKINGWIN'] = self.TRACKINGWIN
        self.SYNCACQWIN = RM_Field_MODEM_S_REALTIMCFE_SYNCACQWIN(self)
        self.zz_fdict['SYNCACQWIN'] = self.SYNCACQWIN
        self.EXTENSCHBYP = RM_Field_MODEM_S_REALTIMCFE_EXTENSCHBYP(self)
        self.zz_fdict['EXTENSCHBYP'] = self.EXTENSCHBYP
        self.SINEWEN = RM_Field_MODEM_S_REALTIMCFE_SINEWEN(self)
        self.zz_fdict['SINEWEN'] = self.SINEWEN
        self.VTAFCFRAME = RM_Field_MODEM_S_REALTIMCFE_VTAFCFRAME(self)
        self.zz_fdict['VTAFCFRAME'] = self.VTAFCFRAME
        self.RTCFEEN = RM_Field_MODEM_S_REALTIMCFE_RTCFEEN(self)
        self.zz_fdict['RTCFEEN'] = self.RTCFEEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ETSCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ETSCTRL, self).__init__(rmio, label,
            0xa8014000, 0x1B8,
            'ETSCTRL', 'MODEM_S.ETSCTRL', 'read-write',
            u"",
            0x00000000, 0x3FFFF7FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ETSLOC = RM_Field_MODEM_S_ETSCTRL_ETSLOC(self)
        self.zz_fdict['ETSLOC'] = self.ETSLOC
        self.CAPSIGONPRS = RM_Field_MODEM_S_ETSCTRL_CAPSIGONPRS(self)
        self.zz_fdict['CAPSIGONPRS'] = self.CAPSIGONPRS
        self.CAPTRIG = RM_Field_MODEM_S_ETSCTRL_CAPTRIG(self)
        self.zz_fdict['CAPTRIG'] = self.CAPTRIG
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ETSTIM(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ETSTIM, self).__init__(rmio, label,
            0xa8014000, 0x1BC,
            'ETSTIM', 'MODEM_S.ETSTIM', 'read-write',
            u"",
            0x00000000, 0x0003FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ETSTIMVAL = RM_Field_MODEM_S_ETSTIM_ETSTIMVAL(self)
        self.zz_fdict['ETSTIMVAL'] = self.ETSTIMVAL
        self.ETSCOUNTEREN = RM_Field_MODEM_S_ETSTIM_ETSCOUNTEREN(self)
        self.zz_fdict['ETSCOUNTEREN'] = self.ETSCOUNTEREN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANTSWCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANTSWCTRL, self).__init__(rmio, label,
            0xa8014000, 0x1C0,
            'ANTSWCTRL', 'MODEM_S.ANTSWCTRL', 'read-write',
            u"",
            0x003C0000, 0x01FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANTDFLTSEL = RM_Field_MODEM_S_ANTSWCTRL_ANTDFLTSEL(self)
        self.zz_fdict['ANTDFLTSEL'] = self.ANTDFLTSEL
        self.ANTCOUNT = RM_Field_MODEM_S_ANTSWCTRL_ANTCOUNT(self)
        self.zz_fdict['ANTCOUNT'] = self.ANTCOUNT
        self.ANTSWTYPE = RM_Field_MODEM_S_ANTSWCTRL_ANTSWTYPE(self)
        self.zz_fdict['ANTSWTYPE'] = self.ANTSWTYPE
        self.ANTSWRST = RM_Field_MODEM_S_ANTSWCTRL_ANTSWRST(self)
        self.zz_fdict['ANTSWRST'] = self.ANTSWRST
        self.CFGANTPATTEN = RM_Field_MODEM_S_ANTSWCTRL_CFGANTPATTEN(self)
        self.zz_fdict['CFGANTPATTEN'] = self.CFGANTPATTEN
        self.ANTSWENABLE = RM_Field_MODEM_S_ANTSWCTRL_ANTSWENABLE(self)
        self.zz_fdict['ANTSWENABLE'] = self.ANTSWENABLE
        self.EXTDSTOPPULSECNT = RM_Field_MODEM_S_ANTSWCTRL_EXTDSTOPPULSECNT(self)
        self.zz_fdict['EXTDSTOPPULSECNT'] = self.EXTDSTOPPULSECNT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANTSWCTRL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANTSWCTRL1, self).__init__(rmio, label,
            0xa8014000, 0x1C4,
            'ANTSWCTRL1', 'MODEM_S.ANTSWCTRL1', 'read-write',
            u"",
            0x0006AAAA, 0x00FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TIMEPERIOD = RM_Field_MODEM_S_ANTSWCTRL1_TIMEPERIOD(self)
        self.zz_fdict['TIMEPERIOD'] = self.TIMEPERIOD
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANTSWSTART(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANTSWSTART, self).__init__(rmio, label,
            0xa8014000, 0x1C8,
            'ANTSWSTART', 'MODEM_S.ANTSWSTART', 'read-write',
            u"",
            0x00000000, 0x0003FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANTSWSTARTTIM = RM_Field_MODEM_S_ANTSWSTART_ANTSWSTARTTIM(self)
        self.zz_fdict['ANTSWSTARTTIM'] = self.ANTSWSTARTTIM
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANTSWEND(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANTSWEND, self).__init__(rmio, label,
            0xa8014000, 0x1CC,
            'ANTSWEND', 'MODEM_S.ANTSWEND', 'read-write',
            u"",
            0x00000000, 0x0003FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANTSWENDTIM = RM_Field_MODEM_S_ANTSWEND_ANTSWENDTIM(self)
        self.zz_fdict['ANTSWENDTIM'] = self.ANTSWENDTIM
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_TRECPMPATT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_TRECPMPATT, self).__init__(rmio, label,
            0xa8014000, 0x1D0,
            'TRECPMPATT', 'MODEM_S.TRECPMPATT', 'read-write',
            u"",
            0x55555555, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PMEXPECTPATT = RM_Field_MODEM_S_TRECPMPATT_PMEXPECTPATT(self)
        self.zz_fdict['PMEXPECTPATT'] = self.PMEXPECTPATT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_TRECPMDET(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_TRECPMDET, self).__init__(rmio, label,
            0xa8014000, 0x1D4,
            'TRECPMDET', 'MODEM_S.TRECPMDET', 'read-write',
            u"",
            0x00000017, 0xBEFFC3FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PMACQUINGWIN = RM_Field_MODEM_S_TRECPMDET_PMACQUINGWIN(self)
        self.zz_fdict['PMACQUINGWIN'] = self.PMACQUINGWIN
        self.PMCOSTVALTHD = RM_Field_MODEM_S_TRECPMDET_PMCOSTVALTHD(self)
        self.zz_fdict['PMCOSTVALTHD'] = self.PMCOSTVALTHD
        self.PMTIMEOUTSEL = RM_Field_MODEM_S_TRECPMDET_PMTIMEOUTSEL(self)
        self.zz_fdict['PMTIMEOUTSEL'] = self.PMTIMEOUTSEL
        self.PHSCALE = RM_Field_MODEM_S_TRECPMDET_PHSCALE(self)
        self.zz_fdict['PHSCALE'] = self.PHSCALE
        self.PMMINCOSTTHD = RM_Field_MODEM_S_TRECPMDET_PMMINCOSTTHD(self)
        self.zz_fdict['PMMINCOSTTHD'] = self.PMMINCOSTTHD
        self.COSTHYST = RM_Field_MODEM_S_TRECPMDET_COSTHYST(self)
        self.zz_fdict['COSTHYST'] = self.COSTHYST
        self.PREAMSCH = RM_Field_MODEM_S_TRECPMDET_PREAMSCH(self)
        self.zz_fdict['PREAMSCH'] = self.PREAMSCH
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_TRECSCFG(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_TRECSCFG, self).__init__(rmio, label,
            0xa8014000, 0x1D8,
            'TRECSCFG', 'MODEM_S.TRECSCFG', 'read-write',
            u"",
            0x00020004, 0x01FF5FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.TRECSOSR = RM_Field_MODEM_S_TRECSCFG_TRECSOSR(self)
        self.zz_fdict['TRECSOSR'] = self.TRECSOSR
        self.DTIMLOSSTHD = RM_Field_MODEM_S_TRECSCFG_DTIMLOSSTHD(self)
        self.zz_fdict['DTIMLOSSTHD'] = self.DTIMLOSSTHD
        self.DTIMLOSSEN = RM_Field_MODEM_S_TRECSCFG_DTIMLOSSEN(self)
        self.zz_fdict['DTIMLOSSEN'] = self.DTIMLOSSEN
        self.PMOFFSET = RM_Field_MODEM_S_TRECSCFG_PMOFFSET(self)
        self.zz_fdict['PMOFFSET'] = self.PMOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CFGANTPATT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CFGANTPATT, self).__init__(rmio, label,
            0xa8014000, 0x1DC,
            'CFGANTPATT', 'MODEM_S.CFGANTPATT', 'read-write',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CFGANTPATTVAL = RM_Field_MODEM_S_CFGANTPATT_CFGANTPATTVAL(self)
        self.zz_fdict['CFGANTPATTVAL'] = self.CFGANTPATTVAL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE00(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE00, self).__init__(rmio, label,
            0xa8014000, 0x1E4,
            'CHFCOE00', 'MODEM_S.CHFCOE00', 'read-write',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET0COEFF0 = RM_Field_MODEM_S_CHFCOE00_SET0COEFF0(self)
        self.zz_fdict['SET0COEFF0'] = self.SET0COEFF0
        self.SET0COEFF1 = RM_Field_MODEM_S_CHFCOE00_SET0COEFF1(self)
        self.zz_fdict['SET0COEFF1'] = self.SET0COEFF1
        self.SET0COEFF2 = RM_Field_MODEM_S_CHFCOE00_SET0COEFF2(self)
        self.zz_fdict['SET0COEFF2'] = self.SET0COEFF2
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE01(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE01, self).__init__(rmio, label,
            0xa8014000, 0x1E8,
            'CHFCOE01', 'MODEM_S.CHFCOE01', 'read-write',
            u"",
            0x00000000, 0x003FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET0COEFF3 = RM_Field_MODEM_S_CHFCOE01_SET0COEFF3(self)
        self.zz_fdict['SET0COEFF3'] = self.SET0COEFF3
        self.SET0COEFF4 = RM_Field_MODEM_S_CHFCOE01_SET0COEFF4(self)
        self.zz_fdict['SET0COEFF4'] = self.SET0COEFF4
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE02(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE02, self).__init__(rmio, label,
            0xa8014000, 0x1EC,
            'CHFCOE02', 'MODEM_S.CHFCOE02', 'read-write',
            u"",
            0x00000000, 0x007FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET0COEFF5 = RM_Field_MODEM_S_CHFCOE02_SET0COEFF5(self)
        self.zz_fdict['SET0COEFF5'] = self.SET0COEFF5
        self.SET0COEFF6 = RM_Field_MODEM_S_CHFCOE02_SET0COEFF6(self)
        self.zz_fdict['SET0COEFF6'] = self.SET0COEFF6
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE03(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE03, self).__init__(rmio, label,
            0xa8014000, 0x1F0,
            'CHFCOE03', 'MODEM_S.CHFCOE03', 'read-write',
            u"",
            0x00000000, 0x00FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET0COEFF7 = RM_Field_MODEM_S_CHFCOE03_SET0COEFF7(self)
        self.zz_fdict['SET0COEFF7'] = self.SET0COEFF7
        self.SET0COEFF8 = RM_Field_MODEM_S_CHFCOE03_SET0COEFF8(self)
        self.zz_fdict['SET0COEFF8'] = self.SET0COEFF8
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE04(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE04, self).__init__(rmio, label,
            0xa8014000, 0x1F4,
            'CHFCOE04', 'MODEM_S.CHFCOE04', 'read-write',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET0COEFF9 = RM_Field_MODEM_S_CHFCOE04_SET0COEFF9(self)
        self.zz_fdict['SET0COEFF9'] = self.SET0COEFF9
        self.SET0COEFF10 = RM_Field_MODEM_S_CHFCOE04_SET0COEFF10(self)
        self.zz_fdict['SET0COEFF10'] = self.SET0COEFF10
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE05(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE05, self).__init__(rmio, label,
            0xa8014000, 0x1F8,
            'CHFCOE05', 'MODEM_S.CHFCOE05', 'read-write',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET0COEFF11 = RM_Field_MODEM_S_CHFCOE05_SET0COEFF11(self)
        self.zz_fdict['SET0COEFF11'] = self.SET0COEFF11
        self.SET0COEFF12 = RM_Field_MODEM_S_CHFCOE05_SET0COEFF12(self)
        self.zz_fdict['SET0COEFF12'] = self.SET0COEFF12
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE06(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE06, self).__init__(rmio, label,
            0xa8014000, 0x1FC,
            'CHFCOE06', 'MODEM_S.CHFCOE06', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET0COEFF13 = RM_Field_MODEM_S_CHFCOE06_SET0COEFF13(self)
        self.zz_fdict['SET0COEFF13'] = self.SET0COEFF13
        self.SET0COEFF14 = RM_Field_MODEM_S_CHFCOE06_SET0COEFF14(self)
        self.zz_fdict['SET0COEFF14'] = self.SET0COEFF14
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE10(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE10, self).__init__(rmio, label,
            0xa8014000, 0x200,
            'CHFCOE10', 'MODEM_S.CHFCOE10', 'read-write',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET1COEFF0 = RM_Field_MODEM_S_CHFCOE10_SET1COEFF0(self)
        self.zz_fdict['SET1COEFF0'] = self.SET1COEFF0
        self.SET1COEFF1 = RM_Field_MODEM_S_CHFCOE10_SET1COEFF1(self)
        self.zz_fdict['SET1COEFF1'] = self.SET1COEFF1
        self.SET1COEFF2 = RM_Field_MODEM_S_CHFCOE10_SET1COEFF2(self)
        self.zz_fdict['SET1COEFF2'] = self.SET1COEFF2
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE11(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE11, self).__init__(rmio, label,
            0xa8014000, 0x204,
            'CHFCOE11', 'MODEM_S.CHFCOE11', 'read-write',
            u"",
            0x00000000, 0x003FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET1COEFF3 = RM_Field_MODEM_S_CHFCOE11_SET1COEFF3(self)
        self.zz_fdict['SET1COEFF3'] = self.SET1COEFF3
        self.SET1COEFF4 = RM_Field_MODEM_S_CHFCOE11_SET1COEFF4(self)
        self.zz_fdict['SET1COEFF4'] = self.SET1COEFF4
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE12(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE12, self).__init__(rmio, label,
            0xa8014000, 0x208,
            'CHFCOE12', 'MODEM_S.CHFCOE12', 'read-write',
            u"",
            0x00000000, 0x007FFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET1COEFF5 = RM_Field_MODEM_S_CHFCOE12_SET1COEFF5(self)
        self.zz_fdict['SET1COEFF5'] = self.SET1COEFF5
        self.SET1COEFF6 = RM_Field_MODEM_S_CHFCOE12_SET1COEFF6(self)
        self.zz_fdict['SET1COEFF6'] = self.SET1COEFF6
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE13(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE13, self).__init__(rmio, label,
            0xa8014000, 0x20C,
            'CHFCOE13', 'MODEM_S.CHFCOE13', 'read-write',
            u"",
            0x00000000, 0x00FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET1COEFF7 = RM_Field_MODEM_S_CHFCOE13_SET1COEFF7(self)
        self.zz_fdict['SET1COEFF7'] = self.SET1COEFF7
        self.SET1COEFF8 = RM_Field_MODEM_S_CHFCOE13_SET1COEFF8(self)
        self.zz_fdict['SET1COEFF8'] = self.SET1COEFF8
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE14(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE14, self).__init__(rmio, label,
            0xa8014000, 0x210,
            'CHFCOE14', 'MODEM_S.CHFCOE14', 'read-write',
            u"",
            0x00000000, 0x0FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET1COEFF9 = RM_Field_MODEM_S_CHFCOE14_SET1COEFF9(self)
        self.zz_fdict['SET1COEFF9'] = self.SET1COEFF9
        self.SET1COEFF10 = RM_Field_MODEM_S_CHFCOE14_SET1COEFF10(self)
        self.zz_fdict['SET1COEFF10'] = self.SET1COEFF10
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE15(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE15, self).__init__(rmio, label,
            0xa8014000, 0x214,
            'CHFCOE15', 'MODEM_S.CHFCOE15', 'read-write',
            u"",
            0x00000000, 0x3FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET1COEFF11 = RM_Field_MODEM_S_CHFCOE15_SET1COEFF11(self)
        self.zz_fdict['SET1COEFF11'] = self.SET1COEFF11
        self.SET1COEFF12 = RM_Field_MODEM_S_CHFCOE15_SET1COEFF12(self)
        self.zz_fdict['SET1COEFF12'] = self.SET1COEFF12
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCOE16(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCOE16, self).__init__(rmio, label,
            0xa8014000, 0x218,
            'CHFCOE16', 'MODEM_S.CHFCOE16', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SET1COEFF13 = RM_Field_MODEM_S_CHFCOE16_SET1COEFF13(self)
        self.zz_fdict['SET1COEFF13'] = self.SET1COEFF13
        self.SET1COEFF14 = RM_Field_MODEM_S_CHFCOE16_SET1COEFF14(self)
        self.zz_fdict['SET1COEFF14'] = self.SET1COEFF14
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFCTRL, self).__init__(rmio, label,
            0xa8014000, 0x21C,
            'CHFCTRL', 'MODEM_S.CHFCTRL', 'read-write',
            u"",
            0x00000000, 0x80000003,
            0x00001000, 0x00002000,
            0x00003000)

        self.FWSWCOEFFEN = RM_Field_MODEM_S_CHFCTRL_FWSWCOEFFEN(self)
        self.zz_fdict['FWSWCOEFFEN'] = self.FWSWCOEFFEN
        self.FWSELCOEFF = RM_Field_MODEM_S_CHFCTRL_FWSELCOEFF(self)
        self.zz_fdict['FWSELCOEFF'] = self.FWSELCOEFF
        self.SWCOEFFEN = RM_Field_MODEM_S_CHFCTRL_SWCOEFFEN(self)
        self.zz_fdict['SWCOEFFEN'] = self.SWCOEFFEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_CHFLATENCYCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_CHFLATENCYCTRL, self).__init__(rmio, label,
            0xa8014000, 0x220,
            'CHFLATENCYCTRL', 'MODEM_S.CHFLATENCYCTRL', 'read-write',
            u"",
            0x00000000, 0x00000003,
            0x00001000, 0x00002000,
            0x00003000)

        self.CHFLATENCY = RM_Field_MODEM_S_CHFLATENCYCTRL_CHFLATENCY(self)
        self.zz_fdict['CHFLATENCY'] = self.CHFLATENCY
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_FRMSCHTIME(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_FRMSCHTIME, self).__init__(rmio, label,
            0xa8014000, 0x224,
            'FRMSCHTIME', 'MODEM_S.FRMSCHTIME', 'read-write',
            u"",
            0x00000040, 0xE000FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.FRMSCHTIME = RM_Field_MODEM_S_FRMSCHTIME_FRMSCHTIME(self)
        self.zz_fdict['FRMSCHTIME'] = self.FRMSCHTIME
        self.PMRSTSYCNEN = RM_Field_MODEM_S_FRMSCHTIME_PMRSTSYCNEN(self)
        self.zz_fdict['PMRSTSYCNEN'] = self.PMRSTSYCNEN
        self.DSARSTSYCNEN = RM_Field_MODEM_S_FRMSCHTIME_DSARSTSYCNEN(self)
        self.zz_fdict['DSARSTSYCNEN'] = self.DSARSTSYCNEN
        self.PMENDSCHEN = RM_Field_MODEM_S_FRMSCHTIME_PMENDSCHEN(self)
        self.zz_fdict['PMENDSCHEN'] = self.PMENDSCHEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_PREFILTCOEFF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_PREFILTCOEFF, self).__init__(rmio, label,
            0xa8014000, 0x228,
            'PREFILTCOEFF', 'MODEM_S.PREFILTCOEFF', 'read-write',
            u"",
            0x3B3B3B3B, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PREFILTCOEFF = RM_Field_MODEM_S_PREFILTCOEFF_PREFILTCOEFF(self)
        self.zz_fdict['PREFILTCOEFF'] = self.PREFILTCOEFF
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_RXRESTART(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_RXRESTART, self).__init__(rmio, label,
            0xa8014000, 0x22C,
            'RXRESTART', 'MODEM_S.RXRESTART', 'read-write',
            u"",
            0x00001860, 0xC0011FF1,
            0x00001000, 0x00002000,
            0x00003000)

        self.RXRESTARTUPONMARSSI = RM_Field_MODEM_S_RXRESTART_RXRESTARTUPONMARSSI(self)
        self.zz_fdict['RXRESTARTUPONMARSSI'] = self.RXRESTARTUPONMARSSI
        self.RXRESTARTMATHRESHOLD = RM_Field_MODEM_S_RXRESTART_RXRESTARTMATHRESHOLD(self)
        self.zz_fdict['RXRESTARTMATHRESHOLD'] = self.RXRESTARTMATHRESHOLD
        self.RXRESTARTMALATCHSEL = RM_Field_MODEM_S_RXRESTART_RXRESTARTMALATCHSEL(self)
        self.zz_fdict['RXRESTARTMALATCHSEL'] = self.RXRESTARTMALATCHSEL
        self.RXRESTARTMACOMPENSEL = RM_Field_MODEM_S_RXRESTART_RXRESTARTMACOMPENSEL(self)
        self.zz_fdict['RXRESTARTMACOMPENSEL'] = self.RXRESTARTMACOMPENSEL
        self.RXRESTARTMATAP = RM_Field_MODEM_S_RXRESTART_RXRESTARTMATAP(self)
        self.zz_fdict['RXRESTARTMATAP'] = self.RXRESTARTMATAP
        self.RXRESTARTB4PREDET = RM_Field_MODEM_S_RXRESTART_RXRESTARTB4PREDET(self)
        self.zz_fdict['RXRESTARTB4PREDET'] = self.RXRESTARTB4PREDET
        self.ANTSWRSTFLTTDIS = RM_Field_MODEM_S_RXRESTART_ANTSWRSTFLTTDIS(self)
        self.zz_fdict['ANTSWRSTFLTTDIS'] = self.ANTSWRSTFLTTDIS
        self.FLTRSTEN = RM_Field_MODEM_S_RXRESTART_FLTRSTEN(self)
        self.zz_fdict['FLTRSTEN'] = self.FLTRSTEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SQ(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SQ, self).__init__(rmio, label,
            0xa8014000, 0x230,
            'SQ', 'MODEM_S.SQ', 'read-write',
            u"",
            0x00000000, 0xFFFF0003,
            0x00001000, 0x00002000,
            0x00003000)

        self.SQEN = RM_Field_MODEM_S_SQ_SQEN(self)
        self.zz_fdict['SQEN'] = self.SQEN
        self.SQSWRST = RM_Field_MODEM_S_SQ_SQSWRST(self)
        self.zz_fdict['SQSWRST'] = self.SQSWRST
        self.SQTIMOUT = RM_Field_MODEM_S_SQ_SQTIMOUT(self)
        self.zz_fdict['SQTIMOUT'] = self.SQTIMOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SQEXT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SQEXT, self).__init__(rmio, label,
            0xa8014000, 0x234,
            'SQEXT', 'MODEM_S.SQEXT', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SQSTG2TIMOUT = RM_Field_MODEM_S_SQEXT_SQSTG2TIMOUT(self)
        self.zz_fdict['SQSTG2TIMOUT'] = self.SQSTG2TIMOUT
        self.SQSTG3TIMOUT = RM_Field_MODEM_S_SQEXT_SQSTG3TIMOUT(self)
        self.zz_fdict['SQSTG3TIMOUT'] = self.SQSTG3TIMOUT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SQI(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SQI, self).__init__(rmio, label,
            0xa8014000, 0x238,
            'SQI', 'MODEM_S.SQI', 'read-write',
            u"",
            0x00000000, 0x00FF0001,
            0x00001000, 0x00002000,
            0x00003000)

        self.SQISELECT = RM_Field_MODEM_S_SQI_SQISELECT(self)
        self.zz_fdict['SQISELECT'] = self.SQISELECT
        self.CHIPERROR = RM_Field_MODEM_S_SQI_CHIPERROR(self)
        self.zz_fdict['CHIPERROR'] = self.CHIPERROR
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANTDIVCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANTDIVCTRL, self).__init__(rmio, label,
            0xa8014000, 0x23C,
            'ANTDIVCTRL', 'MODEM_S.ANTDIVCTRL', 'read-write',
            u"",
            0x00000000, 0x000007FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADPRETHRESH = RM_Field_MODEM_S_ANTDIVCTRL_ADPRETHRESH(self)
        self.zz_fdict['ADPRETHRESH'] = self.ADPRETHRESH
        self.ENADPRETHRESH = RM_Field_MODEM_S_ANTDIVCTRL_ENADPRETHRESH(self)
        self.zz_fdict['ENADPRETHRESH'] = self.ENADPRETHRESH
        self.ANTDIVDISCCA = RM_Field_MODEM_S_ANTDIVCTRL_ANTDIVDISCCA(self)
        self.zz_fdict['ANTDIVDISCCA'] = self.ANTDIVDISCCA
        self.ANTDIVSELCCA = RM_Field_MODEM_S_ANTDIVCTRL_ANTDIVSELCCA(self)
        self.zz_fdict['ANTDIVSELCCA'] = self.ANTDIVSELCCA
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ANTDIVFW(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ANTDIVFW, self).__init__(rmio, label,
            0xa8014000, 0x240,
            'ANTDIVFW', 'MODEM_S.ANTDIVFW', 'read-write',
            u"",
            0x00000000, 0x80000003,
            0x00001000, 0x00002000,
            0x00003000)

        self.FWSELANT = RM_Field_MODEM_S_ANTDIVFW_FWSELANT(self)
        self.zz_fdict['FWSELANT'] = self.FWSELANT
        self.FWANTSWCMD = RM_Field_MODEM_S_ANTDIVFW_FWANTSWCMD(self)
        self.zz_fdict['FWANTSWCMD'] = self.FWANTSWCMD
        self.FWANTDIVEN = RM_Field_MODEM_S_ANTDIVFW_FWANTDIVEN(self)
        self.zz_fdict['FWANTDIVEN'] = self.FWANTDIVEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_PHDMODANTDIV(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_PHDMODANTDIV, self).__init__(rmio, label,
            0xa8014000, 0x244,
            'PHDMODANTDIV', 'MODEM_S.PHDMODANTDIV', 'read-write',
            u"",
            0x0000000F, 0x40FF1FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ANTWAIT = RM_Field_MODEM_S_PHDMODANTDIV_ANTWAIT(self)
        self.zz_fdict['ANTWAIT'] = self.ANTWAIT
        self.SKIPRSSITHD = RM_Field_MODEM_S_PHDMODANTDIV_SKIPRSSITHD(self)
        self.zz_fdict['SKIPRSSITHD'] = self.SKIPRSSITHD
        self.SKIPCORRTHD = RM_Field_MODEM_S_PHDMODANTDIV_SKIPCORRTHD(self)
        self.zz_fdict['SKIPCORRTHD'] = self.SKIPCORRTHD
        self.SKIP2ANT = RM_Field_MODEM_S_PHDMODANTDIV_SKIP2ANT(self)
        self.zz_fdict['SKIP2ANT'] = self.SKIP2ANT
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_PHANTDECSION(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_PHANTDECSION, self).__init__(rmio, label,
            0xa8014000, 0x248,
            'PHANTDECSION', 'MODEM_S.PHANTDECSION', 'read-write',
            u"",
            0x00000000, 0xF007FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CORRANDDIVTHD = RM_Field_MODEM_S_PHANTDECSION_CORRANDDIVTHD(self)
        self.zz_fdict['CORRANDDIVTHD'] = self.CORRANDDIVTHD
        self.RSSIANDDIVTHD = RM_Field_MODEM_S_PHANTDECSION_RSSIANDDIVTHD(self)
        self.zz_fdict['RSSIANDDIVTHD'] = self.RSSIANDDIVTHD
        self.RSSICORR0 = RM_Field_MODEM_S_PHANTDECSION_RSSICORR0(self)
        self.zz_fdict['RSSICORR0'] = self.RSSICORR0
        self.RSSICORR1 = RM_Field_MODEM_S_PHANTDECSION_RSSICORR1(self)
        self.zz_fdict['RSSICORR1'] = self.RSSICORR1
        self.RSSICORR2 = RM_Field_MODEM_S_PHANTDECSION_RSSICORR2(self)
        self.zz_fdict['RSSICORR2'] = self.RSSICORR2
        self.RSSICORR3 = RM_Field_MODEM_S_PHANTDECSION_RSSICORR3(self)
        self.zz_fdict['RSSICORR3'] = self.RSSICORR3
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_PHDMODCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_PHDMODCTRL, self).__init__(rmio, label,
            0xa8014000, 0x24C,
            'PHDMODCTRL', 'MODEM_S.PHDMODCTRL', 'read-write',
            u"",
            0x01DF0004, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.PMDETTHD = RM_Field_MODEM_S_PHDMODCTRL_PMDETTHD(self)
        self.zz_fdict['PMDETTHD'] = self.PMDETTHD
        self.PMTIMLOSTHD = RM_Field_MODEM_S_PHDMODCTRL_PMTIMLOSTHD(self)
        self.zz_fdict['PMTIMLOSTHD'] = self.PMTIMLOSTHD
        self.PMTIMLOSEN = RM_Field_MODEM_S_PHDMODCTRL_PMTIMLOSEN(self)
        self.zz_fdict['PMTIMLOSEN'] = self.PMTIMLOSEN
        self.RSSIFLTBYP = RM_Field_MODEM_S_PHDMODCTRL_RSSIFLTBYP(self)
        self.zz_fdict['RSSIFLTBYP'] = self.RSSIFLTBYP
        self.PMDETEN = RM_Field_MODEM_S_PHDMODCTRL_PMDETEN(self)
        self.zz_fdict['PMDETEN'] = self.PMDETEN
        self.REMODOSR = RM_Field_MODEM_S_PHDMODCTRL_REMODOSR(self)
        self.zz_fdict['REMODOSR'] = self.REMODOSR
        self.REMODDWN = RM_Field_MODEM_S_PHDMODCTRL_REMODDWN(self)
        self.zz_fdict['REMODDWN'] = self.REMODDWN
        self.REMODOUTSEL = RM_Field_MODEM_S_PHDMODCTRL_REMODOUTSEL(self)
        self.zz_fdict['REMODOUTSEL'] = self.REMODOUTSEL
        self.REMODEN = RM_Field_MODEM_S_PHDMODCTRL_REMODEN(self)
        self.zz_fdict['REMODEN'] = self.REMODEN
        self.BCRDETECTOR = RM_Field_MODEM_S_PHDMODCTRL_BCRDETECTOR(self)
        self.zz_fdict['BCRDETECTOR'] = self.BCRDETECTOR
        self.BCRTRECSCONC = RM_Field_MODEM_S_PHDMODCTRL_BCRTRECSCONC(self)
        self.zz_fdict['BCRTRECSCONC'] = self.BCRTRECSCONC
        self.BCRLEGACYCONC = RM_Field_MODEM_S_PHDMODCTRL_BCRLEGACYCONC(self)
        self.zz_fdict['BCRLEGACYCONC'] = self.BCRLEGACYCONC
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_IRCAL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_IRCAL, self).__init__(rmio, label,
            0xa8014000, 0x270,
            'IRCAL', 'MODEM_S.IRCAL', 'read-write',
            u"",
            0x00000000, 0x0000FFBF,
            0x00001000, 0x00002000,
            0x00003000)

        self.IRCALEN = RM_Field_MODEM_S_IRCAL_IRCALEN(self)
        self.zz_fdict['IRCALEN'] = self.IRCALEN
        self.MURSHF = RM_Field_MODEM_S_IRCAL_MURSHF(self)
        self.zz_fdict['MURSHF'] = self.MURSHF
        self.MUISHF = RM_Field_MODEM_S_IRCAL_MUISHF(self)
        self.zz_fdict['MUISHF'] = self.MUISHF
        self.IRCORREN = RM_Field_MODEM_S_IRCAL_IRCORREN(self)
        self.zz_fdict['IRCORREN'] = self.IRCORREN
        self.IRCALCOEFRSTCMD = RM_Field_MODEM_S_IRCAL_IRCALCOEFRSTCMD(self)
        self.zz_fdict['IRCALCOEFRSTCMD'] = self.IRCALCOEFRSTCMD
        self.IRCALIFADCDBG = RM_Field_MODEM_S_IRCAL_IRCALIFADCDBG(self)
        self.zz_fdict['IRCALIFADCDBG'] = self.IRCALIFADCDBG
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_IRCALCOEF(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_IRCALCOEF, self).__init__(rmio, label,
            0xa8014000, 0x274,
            'IRCALCOEF', 'MODEM_S.IRCALCOEF', 'read-only',
            u"",
            0x00000000, 0x7FFF7FFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CRV = RM_Field_MODEM_S_IRCALCOEF_CRV(self)
        self.zz_fdict['CRV'] = self.CRV
        self.CIV = RM_Field_MODEM_S_IRCALCOEF_CIV(self)
        self.zz_fdict['CIV'] = self.CIV
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_IRCALCOEFWR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_IRCALCOEFWR0, self).__init__(rmio, label,
            0xa8014000, 0x278,
            'IRCALCOEFWR0', 'MODEM_S.IRCALCOEFWR0', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CRVWD = RM_Field_MODEM_S_IRCALCOEFWR0_CRVWD(self)
        self.zz_fdict['CRVWD'] = self.CRVWD
        self.CRVWEN = RM_Field_MODEM_S_IRCALCOEFWR0_CRVWEN(self)
        self.zz_fdict['CRVWEN'] = self.CRVWEN
        self.CIVWD = RM_Field_MODEM_S_IRCALCOEFWR0_CIVWD(self)
        self.zz_fdict['CIVWD'] = self.CIVWD
        self.CIVWEN = RM_Field_MODEM_S_IRCALCOEFWR0_CIVWEN(self)
        self.zz_fdict['CIVWEN'] = self.CIVWEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_IRCALCOEFWR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_IRCALCOEFWR1, self).__init__(rmio, label,
            0xa8014000, 0x27C,
            'IRCALCOEFWR1', 'MODEM_S.IRCALCOEFWR1', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CRVWD = RM_Field_MODEM_S_IRCALCOEFWR1_CRVWD(self)
        self.zz_fdict['CRVWD'] = self.CRVWD
        self.CRVWEN = RM_Field_MODEM_S_IRCALCOEFWR1_CRVWEN(self)
        self.zz_fdict['CRVWEN'] = self.CRVWEN
        self.CIVWD = RM_Field_MODEM_S_IRCALCOEFWR1_CIVWD(self)
        self.zz_fdict['CIVWD'] = self.CIVWD
        self.CIVWEN = RM_Field_MODEM_S_IRCALCOEFWR1_CIVWEN(self)
        self.zz_fdict['CIVWEN'] = self.CIVWEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADCTRL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADCTRL1, self).__init__(rmio, label,
            0xa8014000, 0x280,
            'ADCTRL1', 'MODEM_S.ADCTRL1', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADCTRL1 = RM_Field_MODEM_S_ADCTRL1_ADCTRL1(self)
        self.zz_fdict['ADCTRL1'] = self.ADCTRL1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADCTRL2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADCTRL2, self).__init__(rmio, label,
            0xa8014000, 0x284,
            'ADCTRL2', 'MODEM_S.ADCTRL2', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADCTRL2 = RM_Field_MODEM_S_ADCTRL2_ADCTRL2(self)
        self.zz_fdict['ADCTRL2'] = self.ADCTRL2
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL0, self).__init__(rmio, label,
            0xa8014000, 0x288,
            'ADQUAL0', 'MODEM_S.ADQUAL0', 'read-only',
            u"",
            0x00000000, 0x03FF03FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADRSSI0 = RM_Field_MODEM_S_ADQUAL0_ADRSSI0(self)
        self.zz_fdict['ADRSSI0'] = self.ADRSSI0
        self.ADRSSI1 = RM_Field_MODEM_S_ADQUAL0_ADRSSI1(self)
        self.zz_fdict['ADRSSI1'] = self.ADRSSI1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL1, self).__init__(rmio, label,
            0xa8014000, 0x28C,
            'ADQUAL1', 'MODEM_S.ADQUAL1', 'read-only',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADCORR0 = RM_Field_MODEM_S_ADQUAL1_ADCORR0(self)
        self.zz_fdict['ADCORR0'] = self.ADCORR0
        self.ADSTAT1 = RM_Field_MODEM_S_ADQUAL1_ADSTAT1(self)
        self.zz_fdict['ADSTAT1'] = self.ADSTAT1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL2, self).__init__(rmio, label,
            0xa8014000, 0x290,
            'ADQUAL2', 'MODEM_S.ADQUAL2', 'read-only',
            u"",
            0x00000000, 0x03FF03FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADRSSI0P = RM_Field_MODEM_S_ADQUAL2_ADRSSI0P(self)
        self.zz_fdict['ADRSSI0P'] = self.ADRSSI0P
        self.ADRSSI1P = RM_Field_MODEM_S_ADQUAL2_ADRSSI1P(self)
        self.zz_fdict['ADRSSI1P'] = self.ADRSSI1P
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL3, self).__init__(rmio, label,
            0xa8014000, 0x294,
            'ADQUAL3', 'MODEM_S.ADQUAL3', 'read-only',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADCORR0P = RM_Field_MODEM_S_ADQUAL3_ADCORR0P(self)
        self.zz_fdict['ADCORR0P'] = self.ADCORR0P
        self.ADSTAT2 = RM_Field_MODEM_S_ADQUAL3_ADSTAT2(self)
        self.zz_fdict['ADSTAT2'] = self.ADSTAT2
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL4, self).__init__(rmio, label,
            0xa8014000, 0x298,
            'ADQUAL4', 'MODEM_S.ADQUAL4', 'read-write',
            u"",
            0x0200003F, 0xC3FF003F,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADAGCGRTHR = RM_Field_MODEM_S_ADQUAL4_ADAGCGRTHR(self)
        self.zz_fdict['ADAGCGRTHR'] = self.ADAGCGRTHR
        self.ADRSSIGRTHR = RM_Field_MODEM_S_ADQUAL4_ADRSSIGRTHR(self)
        self.zz_fdict['ADRSSIGRTHR'] = self.ADRSSIGRTHR
        self.ADGRMODE = RM_Field_MODEM_S_ADQUAL4_ADGRMODE(self)
        self.zz_fdict['ADGRMODE'] = self.ADGRMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL5, self).__init__(rmio, label,
            0xa8014000, 0x29C,
            'ADQUAL5', 'MODEM_S.ADQUAL5', 'read-write',
            u"",
            0x0000FFFF, 0x0001FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADDIRECTCORR = RM_Field_MODEM_S_ADQUAL5_ADDIRECTCORR(self)
        self.zz_fdict['ADDIRECTCORR'] = self.ADDIRECTCORR
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL6, self).__init__(rmio, label,
            0xa8014000, 0x2A0,
            'ADQUAL6', 'MODEM_S.ADQUAL6', 'read-write',
            u"",
            0x0000FFFF, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADBACORRTHR = RM_Field_MODEM_S_ADQUAL6_ADBACORRTHR(self)
        self.zz_fdict['ADBACORRTHR'] = self.ADBACORRTHR
        self.ADBACORRDIFF = RM_Field_MODEM_S_ADQUAL6_ADBACORRDIFF(self)
        self.zz_fdict['ADBACORRDIFF'] = self.ADBACORRDIFF
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL7, self).__init__(rmio, label,
            0xa8014000, 0x2A4,
            'ADQUAL7', 'MODEM_S.ADQUAL7', 'read-write',
            u"",
            0x000003FF, 0x03FF03FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADBARSSITHR = RM_Field_MODEM_S_ADQUAL7_ADBARSSITHR(self)
        self.zz_fdict['ADBARSSITHR'] = self.ADBARSSITHR
        self.ADBARSSIDIFF = RM_Field_MODEM_S_ADQUAL7_ADBARSSIDIFF(self)
        self.zz_fdict['ADBARSSIDIFF'] = self.ADBARSSIDIFF
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL8(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL8, self).__init__(rmio, label,
            0xa8014000, 0x2A8,
            'ADQUAL8', 'MODEM_S.ADQUAL8', 'read-write',
            u"",
            0x00000000, 0x0000033F,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADBAAGCTHR = RM_Field_MODEM_S_ADQUAL8_ADBAAGCTHR(self)
        self.zz_fdict['ADBAAGCTHR'] = self.ADBAAGCTHR
        self.ADBAMODE = RM_Field_MODEM_S_ADQUAL8_ADBAMODE(self)
        self.zz_fdict['ADBAMODE'] = self.ADBAMODE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL9(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL9, self).__init__(rmio, label,
            0xa8014000, 0x2AC,
            'ADQUAL9', 'MODEM_S.ADQUAL9', 'read-only',
            u"",
            0x00000000, 0x0001FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADCORR1 = RM_Field_MODEM_S_ADQUAL9_ADCORR1(self)
        self.zz_fdict['ADCORR1'] = self.ADCORR1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADQUAL10(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADQUAL10, self).__init__(rmio, label,
            0xa8014000, 0x2B0,
            'ADQUAL10', 'MODEM_S.ADQUAL10', 'read-only',
            u"",
            0x00000000, 0x0001FFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADCORR1P = RM_Field_MODEM_S_ADQUAL10_ADCORR1P(self)
        self.zz_fdict['ADCORR1P'] = self.ADCORR1P
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM0, self).__init__(rmio, label,
            0xa8014000, 0x2B4,
            'ADFSM0', 'MODEM_S.ADFSM0', 'read-write',
            u"",
            0x00000000, 0x7FFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADSTATEC = RM_Field_MODEM_S_ADFSM0_ADSTATEC(self)
        self.zz_fdict['ADSTATEC'] = self.ADSTATEC
        self.ADSTATEP = RM_Field_MODEM_S_ADFSM0_ADSTATEP(self)
        self.zz_fdict['ADSTATEP'] = self.ADSTATEP
        self.ADSTATEP2 = RM_Field_MODEM_S_ADFSM0_ADSTATEP2(self)
        self.zz_fdict['ADSTATEP2'] = self.ADSTATEP2
        self.ADSTATEN = RM_Field_MODEM_S_ADFSM0_ADSTATEN(self)
        self.zz_fdict['ADSTATEN'] = self.ADSTATEN
        self.ADTD0 = RM_Field_MODEM_S_ADFSM0_ADTD0(self)
        self.zz_fdict['ADTD0'] = self.ADTD0
        self.ADTD0P = RM_Field_MODEM_S_ADFSM0_ADTD0P(self)
        self.zz_fdict['ADTD0P'] = self.ADTD0P
        self.ADTD1 = RM_Field_MODEM_S_ADFSM0_ADTD1(self)
        self.zz_fdict['ADTD1'] = self.ADTD1
        self.ADTD1P = RM_Field_MODEM_S_ADFSM0_ADTD1P(self)
        self.zz_fdict['ADTD1P'] = self.ADTD1P
        self.ADAS = RM_Field_MODEM_S_ADFSM0_ADAS(self)
        self.zz_fdict['ADAS'] = self.ADAS
        self.ADBA = RM_Field_MODEM_S_ADFSM0_ADBA(self)
        self.zz_fdict['ADBA'] = self.ADBA
        self.ADSTATREAD = RM_Field_MODEM_S_ADFSM0_ADSTATREAD(self)
        self.zz_fdict['ADSTATREAD'] = self.ADSTATREAD
        self.ADSTAT1SEL = RM_Field_MODEM_S_ADFSM0_ADSTAT1SEL(self)
        self.zz_fdict['ADSTAT1SEL'] = self.ADSTAT1SEL
        self.ADSTAT2SEL = RM_Field_MODEM_S_ADFSM0_ADSTAT2SEL(self)
        self.zz_fdict['ADSTAT2SEL'] = self.ADSTAT2SEL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM1, self).__init__(rmio, label,
            0xa8014000, 0x2B8,
            'ADFSM1', 'MODEM_S.ADFSM1', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADOSETANT0 = RM_Field_MODEM_S_ADFSM1_ADOSETANT0(self)
        self.zz_fdict['ADOSETANT0'] = self.ADOSETANT0
        self.ADOSETANT1 = RM_Field_MODEM_S_ADFSM1_ADOSETANT1(self)
        self.zz_fdict['ADOSETANT1'] = self.ADOSETANT1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM2, self).__init__(rmio, label,
            0xa8014000, 0x2BC,
            'ADFSM2', 'MODEM_S.ADFSM2', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADOSWITCHANT = RM_Field_MODEM_S_ADFSM2_ADOSWITCHANT(self)
        self.zz_fdict['ADOSWITCHANT'] = self.ADOSWITCHANT
        self.ADORESTARTRX = RM_Field_MODEM_S_ADFSM2_ADORESTARTRX(self)
        self.zz_fdict['ADORESTARTRX'] = self.ADORESTARTRX
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM3(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM3, self).__init__(rmio, label,
            0xa8014000, 0x2C0,
            'ADFSM3', 'MODEM_S.ADFSM3', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADOQUAL0UPDATE = RM_Field_MODEM_S_ADFSM3_ADOQUAL0UPDATE(self)
        self.zz_fdict['ADOQUAL0UPDATE'] = self.ADOQUAL0UPDATE
        self.ADOQUAL1UPDATE = RM_Field_MODEM_S_ADFSM3_ADOQUAL1UPDATE(self)
        self.zz_fdict['ADOQUAL1UPDATE'] = self.ADOQUAL1UPDATE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM4(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM4, self).__init__(rmio, label,
            0xa8014000, 0x2C4,
            'ADFSM4', 'MODEM_S.ADFSM4', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADOQUAL0CLEAR = RM_Field_MODEM_S_ADFSM4_ADOQUAL0CLEAR(self)
        self.zz_fdict['ADOQUAL0CLEAR'] = self.ADOQUAL0CLEAR
        self.ADOQUAL1CLEAR = RM_Field_MODEM_S_ADFSM4_ADOQUAL1CLEAR(self)
        self.zz_fdict['ADOQUAL1CLEAR'] = self.ADOQUAL1CLEAR
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM5(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM5, self).__init__(rmio, label,
            0xa8014000, 0x2C8,
            'ADFSM5', 'MODEM_S.ADFSM5', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADOMUX = RM_Field_MODEM_S_ADFSM5_ADOMUX(self)
        self.zz_fdict['ADOMUX'] = self.ADOMUX
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM6(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM6, self).__init__(rmio, label,
            0xa8014000, 0x2CC,
            'ADFSM6', 'MODEM_S.ADFSM6', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW0 = RM_Field_MODEM_S_ADFSM6_ADNEXTSTATESW0(self)
        self.zz_fdict['ADNEXTSTATESW0'] = self.ADNEXTSTATESW0
        self.ADNEXTSTATESW1 = RM_Field_MODEM_S_ADFSM6_ADNEXTSTATESW1(self)
        self.zz_fdict['ADNEXTSTATESW1'] = self.ADNEXTSTATESW1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM7(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM7, self).__init__(rmio, label,
            0xa8014000, 0x2D0,
            'ADFSM7', 'MODEM_S.ADFSM7', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW2 = RM_Field_MODEM_S_ADFSM7_ADNEXTSTATESW2(self)
        self.zz_fdict['ADNEXTSTATESW2'] = self.ADNEXTSTATESW2
        self.ADNEXTSTATESW3 = RM_Field_MODEM_S_ADFSM7_ADNEXTSTATESW3(self)
        self.zz_fdict['ADNEXTSTATESW3'] = self.ADNEXTSTATESW3
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM8(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM8, self).__init__(rmio, label,
            0xa8014000, 0x2D4,
            'ADFSM8', 'MODEM_S.ADFSM8', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW4 = RM_Field_MODEM_S_ADFSM8_ADNEXTSTATESW4(self)
        self.zz_fdict['ADNEXTSTATESW4'] = self.ADNEXTSTATESW4
        self.ADNEXTSTATESW5 = RM_Field_MODEM_S_ADFSM8_ADNEXTSTATESW5(self)
        self.zz_fdict['ADNEXTSTATESW5'] = self.ADNEXTSTATESW5
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM9(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM9, self).__init__(rmio, label,
            0xa8014000, 0x2D8,
            'ADFSM9', 'MODEM_S.ADFSM9', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW6 = RM_Field_MODEM_S_ADFSM9_ADNEXTSTATESW6(self)
        self.zz_fdict['ADNEXTSTATESW6'] = self.ADNEXTSTATESW6
        self.ADNEXTSTATESW7 = RM_Field_MODEM_S_ADFSM9_ADNEXTSTATESW7(self)
        self.zz_fdict['ADNEXTSTATESW7'] = self.ADNEXTSTATESW7
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM10(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM10, self).__init__(rmio, label,
            0xa8014000, 0x2DC,
            'ADFSM10', 'MODEM_S.ADFSM10', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW8 = RM_Field_MODEM_S_ADFSM10_ADNEXTSTATESW8(self)
        self.zz_fdict['ADNEXTSTATESW8'] = self.ADNEXTSTATESW8
        self.ADNEXTSTATESW9 = RM_Field_MODEM_S_ADFSM10_ADNEXTSTATESW9(self)
        self.zz_fdict['ADNEXTSTATESW9'] = self.ADNEXTSTATESW9
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM11(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM11, self).__init__(rmio, label,
            0xa8014000, 0x2E0,
            'ADFSM11', 'MODEM_S.ADFSM11', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW10 = RM_Field_MODEM_S_ADFSM11_ADNEXTSTATESW10(self)
        self.zz_fdict['ADNEXTSTATESW10'] = self.ADNEXTSTATESW10
        self.ADNEXTSTATESW11 = RM_Field_MODEM_S_ADFSM11_ADNEXTSTATESW11(self)
        self.zz_fdict['ADNEXTSTATESW11'] = self.ADNEXTSTATESW11
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM12(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM12, self).__init__(rmio, label,
            0xa8014000, 0x2E4,
            'ADFSM12', 'MODEM_S.ADFSM12', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW12 = RM_Field_MODEM_S_ADFSM12_ADNEXTSTATESW12(self)
        self.zz_fdict['ADNEXTSTATESW12'] = self.ADNEXTSTATESW12
        self.ADNEXTSTATESW13 = RM_Field_MODEM_S_ADFSM12_ADNEXTSTATESW13(self)
        self.zz_fdict['ADNEXTSTATESW13'] = self.ADNEXTSTATESW13
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM13(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM13, self).__init__(rmio, label,
            0xa8014000, 0x2E8,
            'ADFSM13', 'MODEM_S.ADFSM13', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADNEXTSTATESW14 = RM_Field_MODEM_S_ADFSM13_ADNEXTSTATESW14(self)
        self.zz_fdict['ADNEXTSTATESW14'] = self.ADNEXTSTATESW14
        self.ADNEXTSTATESW15 = RM_Field_MODEM_S_ADFSM13_ADNEXTSTATESW15(self)
        self.zz_fdict['ADNEXTSTATESW15'] = self.ADNEXTSTATESW15
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM14(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM14, self).__init__(rmio, label,
            0xa8014000, 0x2EC,
            'ADFSM14', 'MODEM_S.ADFSM14', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND0ENA = RM_Field_MODEM_S_ADFSM14_ADFSMCOND0ENA(self)
        self.zz_fdict['ADFSMCOND0ENA'] = self.ADFSMCOND0ENA
        self.ADFSMCOND1ENA = RM_Field_MODEM_S_ADFSM14_ADFSMCOND1ENA(self)
        self.zz_fdict['ADFSMCOND1ENA'] = self.ADFSMCOND1ENA
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM15(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM15, self).__init__(rmio, label,
            0xa8014000, 0x2F0,
            'ADFSM15', 'MODEM_S.ADFSM15', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND2ENA = RM_Field_MODEM_S_ADFSM15_ADFSMCOND2ENA(self)
        self.zz_fdict['ADFSMCOND2ENA'] = self.ADFSMCOND2ENA
        self.ADFSMCOND3ENA = RM_Field_MODEM_S_ADFSM15_ADFSMCOND3ENA(self)
        self.zz_fdict['ADFSMCOND3ENA'] = self.ADFSMCOND3ENA
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM16(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM16, self).__init__(rmio, label,
            0xa8014000, 0x2F4,
            'ADFSM16', 'MODEM_S.ADFSM16', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND0ENB = RM_Field_MODEM_S_ADFSM16_ADFSMCOND0ENB(self)
        self.zz_fdict['ADFSMCOND0ENB'] = self.ADFSMCOND0ENB
        self.ADFSMCOND1ENB = RM_Field_MODEM_S_ADFSM16_ADFSMCOND1ENB(self)
        self.zz_fdict['ADFSMCOND1ENB'] = self.ADFSMCOND1ENB
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM17(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM17, self).__init__(rmio, label,
            0xa8014000, 0x2F8,
            'ADFSM17', 'MODEM_S.ADFSM17', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND2ENB = RM_Field_MODEM_S_ADFSM17_ADFSMCOND2ENB(self)
        self.zz_fdict['ADFSMCOND2ENB'] = self.ADFSMCOND2ENB
        self.ADFSMCOND3ENB = RM_Field_MODEM_S_ADFSM17_ADFSMCOND3ENB(self)
        self.zz_fdict['ADFSMCOND3ENB'] = self.ADFSMCOND3ENB
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM18(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM18, self).__init__(rmio, label,
            0xa8014000, 0x2FC,
            'ADFSM18', 'MODEM_S.ADFSM18', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCONDSEL = RM_Field_MODEM_S_ADFSM18_ADFSMCONDSEL(self)
        self.zz_fdict['ADFSMCONDSEL'] = self.ADFSMCONDSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM19(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM19, self).__init__(rmio, label,
            0xa8014000, 0x300,
            'ADFSM19', 'MODEM_S.ADFSM19', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMNEXTFORCE = RM_Field_MODEM_S_ADFSM19_ADFSMNEXTFORCE(self)
        self.zz_fdict['ADFSMNEXTFORCE'] = self.ADFSMNEXTFORCE
        self.ADFSMCONDTRUE = RM_Field_MODEM_S_ADFSM19_ADFSMCONDTRUE(self)
        self.zz_fdict['ADFSMCONDTRUE'] = self.ADFSMCONDTRUE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM20(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM20, self).__init__(rmio, label,
            0xa8014000, 0x304,
            'ADFSM20', 'MODEM_S.ADFSM20', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADITENTEREN = RM_Field_MODEM_S_ADFSM20_ADITENTEREN(self)
        self.zz_fdict['ADITENTEREN'] = self.ADITENTEREN
        self.ADITLEAVEEN = RM_Field_MODEM_S_ADFSM20_ADITLEAVEEN(self)
        self.zz_fdict['ADITLEAVEEN'] = self.ADITLEAVEEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM21(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM21, self).__init__(rmio, label,
            0xa8014000, 0x308,
            'ADFSM21', 'MODEM_S.ADFSM21', 'read-write',
            u"",
            0x00000000, 0x0001007F,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADENTERFREEZEEN = RM_Field_MODEM_S_ADFSM21_ADENTERFREEZEEN(self)
        self.zz_fdict['ADENTERFREEZEEN'] = self.ADENTERFREEZEEN
        self.ADLEAVEFREEZEEN = RM_Field_MODEM_S_ADFSM21_ADLEAVEFREEZEEN(self)
        self.zz_fdict['ADLEAVEFREEZEEN'] = self.ADLEAVEFREEZEEN
        self.ADFROZEN = RM_Field_MODEM_S_ADFSM21_ADFROZEN(self)
        self.zz_fdict['ADFROZEN'] = self.ADFROZEN
        self.ADUNFREEZENEXT = RM_Field_MODEM_S_ADFSM21_ADUNFREEZENEXT(self)
        self.zz_fdict['ADUNFREEZENEXT'] = self.ADUNFREEZENEXT
        self.ADUNFREEZE = RM_Field_MODEM_S_ADFSM21_ADUNFREEZE(self)
        self.zz_fdict['ADUNFREEZE'] = self.ADUNFREEZE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM22(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM22, self).__init__(rmio, label,
            0xa8014000, 0x30C,
            'ADFSM22', 'MODEM_S.ADFSM22', 'read-only',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADITENTERSTATUS = RM_Field_MODEM_S_ADFSM22_ADITENTERSTATUS(self)
        self.zz_fdict['ADITENTERSTATUS'] = self.ADITENTERSTATUS
        self.ADITLEAVESTATUS = RM_Field_MODEM_S_ADFSM22_ADITLEAVESTATUS(self)
        self.zz_fdict['ADITLEAVESTATUS'] = self.ADITLEAVESTATUS
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM23(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM23, self).__init__(rmio, label,
            0xa8014000, 0x310,
            'ADFSM23', 'MODEM_S.ADFSM23', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND0ENC = RM_Field_MODEM_S_ADFSM23_ADFSMCOND0ENC(self)
        self.zz_fdict['ADFSMCOND0ENC'] = self.ADFSMCOND0ENC
        self.ADFSMCOND1ENC = RM_Field_MODEM_S_ADFSM23_ADFSMCOND1ENC(self)
        self.zz_fdict['ADFSMCOND1ENC'] = self.ADFSMCOND1ENC
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM24(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM24, self).__init__(rmio, label,
            0xa8014000, 0x314,
            'ADFSM24', 'MODEM_S.ADFSM24', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND2ENC = RM_Field_MODEM_S_ADFSM24_ADFSMCOND2ENC(self)
        self.zz_fdict['ADFSMCOND2ENC'] = self.ADFSMCOND2ENC
        self.ADFSMCOND3ENC = RM_Field_MODEM_S_ADFSM24_ADFSMCOND3ENC(self)
        self.zz_fdict['ADFSMCOND3ENC'] = self.ADFSMCOND3ENC
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM25(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM25, self).__init__(rmio, label,
            0xa8014000, 0x318,
            'ADFSM25', 'MODEM_S.ADFSM25', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCONDOR0 = RM_Field_MODEM_S_ADFSM25_ADFSMCONDOR0(self)
        self.zz_fdict['ADFSMCONDOR0'] = self.ADFSMCONDOR0
        self.ADFSMCONDOR1 = RM_Field_MODEM_S_ADFSM25_ADFSMCONDOR1(self)
        self.zz_fdict['ADFSMCONDOR1'] = self.ADFSMCONDOR1
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM26(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM26, self).__init__(rmio, label,
            0xa8014000, 0x31C,
            'ADFSM26', 'MODEM_S.ADFSM26', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND0END = RM_Field_MODEM_S_ADFSM26_ADFSMCOND0END(self)
        self.zz_fdict['ADFSMCOND0END'] = self.ADFSMCOND0END
        self.ADFSMCOND1END = RM_Field_MODEM_S_ADFSM26_ADFSMCOND1END(self)
        self.zz_fdict['ADFSMCOND1END'] = self.ADFSMCOND1END
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM27(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM27, self).__init__(rmio, label,
            0xa8014000, 0x320,
            'ADFSM27', 'MODEM_S.ADFSM27', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADFSMCOND2END = RM_Field_MODEM_S_ADFSM27_ADFSMCOND2END(self)
        self.zz_fdict['ADFSMCOND2END'] = self.ADFSMCOND2END
        self.ADFSMCOND3END = RM_Field_MODEM_S_ADFSM27_ADFSMCOND3END(self)
        self.zz_fdict['ADFSMCOND3END'] = self.ADFSMCOND3END
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM28(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM28, self).__init__(rmio, label,
            0xa8014000, 0x324,
            'ADFSM28', 'MODEM_S.ADFSM28', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADOSETANTFORCE = RM_Field_MODEM_S_ADFSM28_ADOSETANTFORCE(self)
        self.zz_fdict['ADOSETANTFORCE'] = self.ADOSETANTFORCE
        self.ADORESTARTRXFORCE = RM_Field_MODEM_S_ADFSM28_ADORESTARTRXFORCE(self)
        self.zz_fdict['ADORESTARTRXFORCE'] = self.ADORESTARTRXFORCE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM29(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM29, self).__init__(rmio, label,
            0xa8014000, 0x328,
            'ADFSM29', 'MODEM_S.ADFSM29', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADOQUALUPDATEFORCE = RM_Field_MODEM_S_ADFSM29_ADOQUALUPDATEFORCE(self)
        self.zz_fdict['ADOQUALUPDATEFORCE'] = self.ADOQUALUPDATEFORCE
        self.ADOQUALCLEARFORCE = RM_Field_MODEM_S_ADFSM29_ADOQUALCLEARFORCE(self)
        self.zz_fdict['ADOQUALCLEARFORCE'] = self.ADOQUALCLEARFORCE
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_ADFSM30(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_ADFSM30, self).__init__(rmio, label,
            0xa8014000, 0x32C,
            'ADFSM30', 'MODEM_S.ADFSM30', 'read-write',
            u"",
            0x00000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ADODEMODRXREQ = RM_Field_MODEM_S_ADFSM30_ADODEMODRXREQ(self)
        self.zz_fdict['ADODEMODRXREQ'] = self.ADODEMODRXREQ
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRCTRL0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRCTRL0, self).__init__(rmio, label,
            0xa8014000, 0x330,
            'BCRCTRL0', 'MODEM_S.BCRCTRL0', 'read-write',
            u"",
            0x08857628, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.BCRNCOFF = RM_Field_MODEM_S_BCRCTRL0_BCRNCOFF(self)
        self.zz_fdict['BCRNCOFF'] = self.BCRNCOFF
        self.BCRERRRSTEN = RM_Field_MODEM_S_BCRCTRL0_BCRERRRSTEN(self)
        self.zz_fdict['BCRERRRSTEN'] = self.BCRERRRSTEN
        self.BCRFBBYP = RM_Field_MODEM_S_BCRCTRL0_BCRFBBYP(self)
        self.zz_fdict['BCRFBBYP'] = self.BCRFBBYP
        self.BCRALIGN = RM_Field_MODEM_S_BCRCTRL0_BCRALIGN(self)
        self.zz_fdict['BCRALIGN'] = self.BCRALIGN
        self.DISTOGG = RM_Field_MODEM_S_BCRCTRL0_DISTOGG(self)
        self.zz_fdict['DISTOGG'] = self.DISTOGG
        self.CRSLOW = RM_Field_MODEM_S_BCRCTRL0_CRSLOW(self)
        self.zz_fdict['CRSLOW'] = self.CRSLOW
        self.CRFAST = RM_Field_MODEM_S_BCRCTRL0_CRFAST(self)
        self.zz_fdict['CRFAST'] = self.CRFAST
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRCTRL1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRCTRL1, self).__init__(rmio, label,
            0xa8014000, 0x334,
            'BCRCTRL1', 'MODEM_S.BCRCTRL1', 'read-write',
            u"",
            0x005E07FF, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.CRGAIN = RM_Field_MODEM_S_BCRCTRL1_CRGAIN(self)
        self.zz_fdict['CRGAIN'] = self.CRGAIN
        self.CGAINX2 = RM_Field_MODEM_S_BCRCTRL1_CGAINX2(self)
        self.zz_fdict['CGAINX2'] = self.CGAINX2
        self.RXNCOCOMP = RM_Field_MODEM_S_BCRCTRL1_RXNCOCOMP(self)
        self.zz_fdict['RXNCOCOMP'] = self.RXNCOCOMP
        self.RXCOMPLAT = RM_Field_MODEM_S_BCRCTRL1_RXCOMPLAT(self)
        self.zz_fdict['RXCOMPLAT'] = self.RXCOMPLAT
        self.ESCMIDPT = RM_Field_MODEM_S_BCRCTRL1_ESCMIDPT(self)
        self.zz_fdict['ESCMIDPT'] = self.ESCMIDPT
        self.DISMIDPT = RM_Field_MODEM_S_BCRCTRL1_DISMIDPT(self)
        self.zz_fdict['DISMIDPT'] = self.DISMIDPT
        self.BCROSR = RM_Field_MODEM_S_BCRCTRL1_BCROSR(self)
        self.zz_fdict['BCROSR'] = self.BCROSR
        self.ESTOSREN = RM_Field_MODEM_S_BCRCTRL1_ESTOSREN(self)
        self.zz_fdict['ESTOSREN'] = self.ESTOSREN
        self.BCRSWSYCW = RM_Field_MODEM_S_BCRCTRL1_BCRSWSYCW(self)
        self.zz_fdict['BCRSWSYCW'] = self.BCRSWSYCW
        self.PHCOMP2FSK = RM_Field_MODEM_S_BCRCTRL1_PHCOMP2FSK(self)
        self.zz_fdict['PHCOMP2FSK'] = self.PHCOMP2FSK
        self.SLICEFBBYP = RM_Field_MODEM_S_BCRCTRL1_SLICEFBBYP(self)
        self.zz_fdict['SLICEFBBYP'] = self.SLICEFBBYP
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODCTRL(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODCTRL, self).__init__(rmio, label,
            0xa8014000, 0x338,
            'BCRDEMODCTRL', 'MODEM_S.BCRDEMODCTRL', 'read-write',
            u"",
            0x06890100, 0xFFFFDFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.BCRDEMODEN = RM_Field_MODEM_S_BCRDEMODCTRL_BCRDEMODEN(self)
        self.zz_fdict['BCRDEMODEN'] = self.BCRDEMODEN
        self.PULCORRBYP = RM_Field_MODEM_S_BCRDEMODCTRL_PULCORRBYP(self)
        self.zz_fdict['PULCORRBYP'] = self.PULCORRBYP
        self.RAWSYN = RM_Field_MODEM_S_BCRDEMODCTRL_RAWSYN(self)
        self.zz_fdict['RAWSYN'] = self.RAWSYN
        self.CONSCHKBYP = RM_Field_MODEM_S_BCRDEMODCTRL_CONSCHKBYP(self)
        self.zz_fdict['CONSCHKBYP'] = self.CONSCHKBYP
        self.PH0SIZE = RM_Field_MODEM_S_BCRDEMODCTRL_PH0SIZE(self)
        self.zz_fdict['PH0SIZE'] = self.PH0SIZE
        self.LOCKUPBYP = RM_Field_MODEM_S_BCRDEMODCTRL_LOCKUPBYP(self)
        self.zz_fdict['LOCKUPBYP'] = self.LOCKUPBYP
        self.RAWFASTMA = RM_Field_MODEM_S_BCRDEMODCTRL_RAWFASTMA(self)
        self.zz_fdict['RAWFASTMA'] = self.RAWFASTMA
        self.SPIKEREMOV = RM_Field_MODEM_S_BCRDEMODCTRL_SPIKEREMOV(self)
        self.zz_fdict['SPIKEREMOV'] = self.SPIKEREMOV
        self.RAWFLTSEL = RM_Field_MODEM_S_BCRDEMODCTRL_RAWFLTSEL(self)
        self.zz_fdict['RAWFLTSEL'] = self.RAWFLTSEL
        self.MANCHDLY = RM_Field_MODEM_S_BCRDEMODCTRL_MANCHDLY(self)
        self.zz_fdict['MANCHDLY'] = self.MANCHDLY
        self.CICDINSCALE = RM_Field_MODEM_S_BCRDEMODCTRL_CICDINSCALE(self)
        self.zz_fdict['CICDINSCALE'] = self.CICDINSCALE
        self.DATAFLTBY = RM_Field_MODEM_S_BCRDEMODCTRL_DATAFLTBY(self)
        self.zz_fdict['DATAFLTBY'] = self.DATAFLTBY
        self.PREATH = RM_Field_MODEM_S_BCRDEMODCTRL_PREATH(self)
        self.zz_fdict['PREATH'] = self.PREATH
        self.SKIPSYN = RM_Field_MODEM_S_BCRDEMODCTRL_SKIPSYN(self)
        self.zz_fdict['SKIPSYN'] = self.SKIPSYN
        self.PMPATTERN = RM_Field_MODEM_S_BCRDEMODCTRL_PMPATTERN(self)
        self.zz_fdict['PMPATTERN'] = self.PMPATTERN
        self.NONSTDPK = RM_Field_MODEM_S_BCRDEMODCTRL_NONSTDPK(self)
        self.zz_fdict['NONSTDPK'] = self.NONSTDPK
        self.SLICERFAST = RM_Field_MODEM_S_BCRDEMODCTRL_SLICERFAST(self)
        self.zz_fdict['SLICERFAST'] = self.SLICERFAST
        self.DIRECTMODE = RM_Field_MODEM_S_BCRDEMODCTRL_DIRECTMODE(self)
        self.zz_fdict['DIRECTMODE'] = self.DIRECTMODE
        self.DETECTORSEL = RM_Field_MODEM_S_BCRDEMODCTRL_DETECTORSEL(self)
        self.zz_fdict['DETECTORSEL'] = self.DETECTORSEL
        self.BBPMDETEN = RM_Field_MODEM_S_BCRDEMODCTRL_BBPMDETEN(self)
        self.zz_fdict['BBPMDETEN'] = self.BBPMDETEN
        self.MANCHPH = RM_Field_MODEM_S_BCRDEMODCTRL_MANCHPH(self)
        self.zz_fdict['MANCHPH'] = self.MANCHPH
        self.INVRXBIT = RM_Field_MODEM_S_BCRDEMODCTRL_INVRXBIT(self)
        self.zz_fdict['INVRXBIT'] = self.INVRXBIT
        self.PHSRCSEL = RM_Field_MODEM_S_BCRDEMODCTRL_PHSRCSEL(self)
        self.zz_fdict['PHSRCSEL'] = self.PHSRCSEL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODOOK(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODOOK, self).__init__(rmio, label,
            0xa8014000, 0x33C,
            'BCRDEMODOOK', 'MODEM_S.BCRDEMODOOK', 'read-write',
            u"",
            0x00A00C03, 0xFFFFFFEF,
            0x00001000, 0x00002000,
            0x00003000)

        self.OOKFRZEN = RM_Field_MODEM_S_BCRDEMODOOK_OOKFRZEN(self)
        self.zz_fdict['OOKFRZEN'] = self.OOKFRZEN
        self.RAWGAIN = RM_Field_MODEM_S_BCRDEMODOOK_RAWGAIN(self)
        self.zz_fdict['RAWGAIN'] = self.RAWGAIN
        self.NOISEFLEST = RM_Field_MODEM_S_BCRDEMODOOK_NOISEFLEST(self)
        self.zz_fdict['NOISEFLEST'] = self.NOISEFLEST
        self.PKTRUNK = RM_Field_MODEM_S_BCRDEMODOOK_PKTRUNK(self)
        self.zz_fdict['PKTRUNK'] = self.PKTRUNK
        self.MAFREQDWN = RM_Field_MODEM_S_BCRDEMODOOK_MAFREQDWN(self)
        self.zz_fdict['MAFREQDWN'] = self.MAFREQDWN
        self.SQUELCLKEN = RM_Field_MODEM_S_BCRDEMODOOK_SQUELCLKEN(self)
        self.zz_fdict['SQUELCLKEN'] = self.SQUELCLKEN
        self.BWPK = RM_Field_MODEM_S_BCRDEMODOOK_BWPK(self)
        self.zz_fdict['BWPK'] = self.BWPK
        self.ABPK = RM_Field_MODEM_S_BCRDEMODOOK_ABPK(self)
        self.zz_fdict['ABPK'] = self.ABPK
        self.DECAYSWAL = RM_Field_MODEM_S_BCRDEMODOOK_DECAYSWAL(self)
        self.zz_fdict['DECAYSWAL'] = self.DECAYSWAL
        self.DECAY = RM_Field_MODEM_S_BCRDEMODOOK_DECAY(self)
        self.zz_fdict['DECAY'] = self.DECAY
        self.ATTACK = RM_Field_MODEM_S_BCRDEMODOOK_ATTACK(self)
        self.zz_fdict['ATTACK'] = self.ATTACK
        self.SQUELCH = RM_Field_MODEM_S_BCRDEMODOOK_SQUELCH(self)
        self.zz_fdict['SQUELCH'] = self.SQUELCH
        self.RAWNDEC = RM_Field_MODEM_S_BCRDEMODOOK_RAWNDEC(self)
        self.zz_fdict['RAWNDEC'] = self.RAWNDEC
        self.BCRDEMODOOK = RM_Field_MODEM_S_BCRDEMODOOK_BCRDEMODOOK(self)
        self.zz_fdict['BCRDEMODOOK'] = self.BCRDEMODOOK
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODAFC0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODAFC0, self).__init__(rmio, label,
            0xa8014000, 0x340,
            'BCRDEMODAFC0', 'MODEM_S.BCRDEMODAFC0', 'read-write',
            u"",
            0x40000000, 0xE000807F,
            0x00001000, 0x00002000,
            0x00003000)

        self.ZEROOFF = RM_Field_MODEM_S_BCRDEMODAFC0_ZEROOFF(self)
        self.zz_fdict['ZEROOFF'] = self.ZEROOFF
        self.LARGEFREQERR = RM_Field_MODEM_S_BCRDEMODAFC0_LARGEFREQERR(self)
        self.zz_fdict['LARGEFREQERR'] = self.LARGEFREQERR
        self.AFCGAINOVRFLW = RM_Field_MODEM_S_BCRDEMODAFC0_AFCGAINOVRFLW(self)
        self.zz_fdict['AFCGAINOVRFLW'] = self.AFCGAINOVRFLW
        self.EN2TBEST = RM_Field_MODEM_S_BCRDEMODAFC0_EN2TBEST(self)
        self.zz_fdict['EN2TBEST'] = self.EN2TBEST
        self.ENAFCCLKSW = RM_Field_MODEM_S_BCRDEMODAFC0_ENAFCCLKSW(self)
        self.zz_fdict['ENAFCCLKSW'] = self.ENAFCCLKSW
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODAFC1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODAFC1, self).__init__(rmio, label,
            0xa8014000, 0x344,
            'BCRDEMODAFC1', 'MODEM_S.BCRDEMODAFC1', 'read-write',
            u"",
            0x10100012, 0xFFFCC0FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.LGWAIT = RM_Field_MODEM_S_BCRDEMODAFC1_LGWAIT(self)
        self.zz_fdict['LGWAIT'] = self.LGWAIT
        self.SHWAIT = RM_Field_MODEM_S_BCRDEMODAFC1_SHWAIT(self)
        self.zz_fdict['SHWAIT'] = self.SHWAIT
        self.GEARSW = RM_Field_MODEM_S_BCRDEMODAFC1_GEARSW(self)
        self.zz_fdict['GEARSW'] = self.GEARSW
        self.AFCMAEN = RM_Field_MODEM_S_BCRDEMODAFC1_AFCMAEN(self)
        self.zz_fdict['AFCMAEN'] = self.AFCMAEN
        self.ENFZPMEND = RM_Field_MODEM_S_BCRDEMODAFC1_ENFZPMEND(self)
        self.zz_fdict['ENFZPMEND'] = self.ENFZPMEND
        self.NONFRZEN = RM_Field_MODEM_S_BCRDEMODAFC1_NONFRZEN(self)
        self.zz_fdict['NONFRZEN'] = self.NONFRZEN
        self.ONESHOTWAITCNT = RM_Field_MODEM_S_BCRDEMODAFC1_ONESHOTWAITCNT(self)
        self.zz_fdict['ONESHOTWAITCNT'] = self.ONESHOTWAITCNT
        self.ONESHOTAFCEN = RM_Field_MODEM_S_BCRDEMODAFC1_ONESHOTAFCEN(self)
        self.zz_fdict['ONESHOTAFCEN'] = self.ONESHOTAFCEN
        self.SKIPPMDET = RM_Field_MODEM_S_BCRDEMODAFC1_SKIPPMDET(self)
        self.zz_fdict['SKIPPMDET'] = self.SKIPPMDET
        self.PMRSTEN = RM_Field_MODEM_S_BCRDEMODAFC1_PMRSTEN(self)
        self.zz_fdict['PMRSTEN'] = self.PMRSTEN
        self.ENAFCFRZ = RM_Field_MODEM_S_BCRDEMODAFC1_ENAFCFRZ(self)
        self.zz_fdict['ENAFCFRZ'] = self.ENAFCFRZ
        self.HALFPHCOMP = RM_Field_MODEM_S_BCRDEMODAFC1_HALFPHCOMP(self)
        self.zz_fdict['HALFPHCOMP'] = self.HALFPHCOMP
        self.ENAFC = RM_Field_MODEM_S_BCRDEMODAFC1_ENAFC(self)
        self.zz_fdict['ENAFC'] = self.ENAFC
        self.ENFBPLL = RM_Field_MODEM_S_BCRDEMODAFC1_ENFBPLL(self)
        self.zz_fdict['ENFBPLL'] = self.ENFBPLL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMOD4FSK0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMOD4FSK0, self).__init__(rmio, label,
            0xa8014000, 0x348,
            'BCRDEMOD4FSK0', 'MODEM_S.BCRDEMOD4FSK0', 'read-write',
            u"",
            0x00B4299A, 0xC0FFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.THD4GFSK = RM_Field_MODEM_S_BCRDEMOD4FSK0_THD4GFSK(self)
        self.zz_fdict['THD4GFSK'] = self.THD4GFSK
        self.CODE4GFSK = RM_Field_MODEM_S_BCRDEMOD4FSK0_CODE4GFSK(self)
        self.zz_fdict['CODE4GFSK'] = self.CODE4GFSK
        self.PHCOMPBYP = RM_Field_MODEM_S_BCRDEMOD4FSK0_PHCOMPBYP(self)
        self.zz_fdict['PHCOMPBYP'] = self.PHCOMPBYP
        self.EN4GFSK = RM_Field_MODEM_S_BCRDEMOD4FSK0_EN4GFSK(self)
        self.zz_fdict['EN4GFSK'] = self.EN4GFSK
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMOD4FSK1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMOD4FSK1, self).__init__(rmio, label,
            0xa8014000, 0x34C,
            'BCRDEMOD4FSK1', 'MODEM_S.BCRDEMOD4FSK1', 'read-write',
            u"",
            0x00000B1C, 0xC0FF7F7F,
            0x00001000, 0x00002000,
            0x00003000)

        self.PHCOMP4FSK0 = RM_Field_MODEM_S_BCRDEMOD4FSK1_PHCOMP4FSK0(self)
        self.zz_fdict['PHCOMP4FSK0'] = self.PHCOMP4FSK0
        self.PHCOMP4FSK1 = RM_Field_MODEM_S_BCRDEMOD4FSK1_PHCOMP4FSK1(self)
        self.zz_fdict['PHCOMP4FSK1'] = self.PHCOMP4FSK1
        self.FDEVCOMPRATIO = RM_Field_MODEM_S_BCRDEMOD4FSK1_FDEVCOMPRATIO(self)
        self.zz_fdict['FDEVCOMPRATIO'] = self.FDEVCOMPRATIO
        self.FDEVCOMPEN = RM_Field_MODEM_S_BCRDEMOD4FSK1_FDEVCOMPEN(self)
        self.zz_fdict['FDEVCOMPEN'] = self.FDEVCOMPEN
        self.S2PMAP = RM_Field_MODEM_S_BCRDEMOD4FSK1_S2PMAP(self)
        self.zz_fdict['S2PMAP'] = self.S2PMAP
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODANT(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODANT, self).__init__(rmio, label,
            0xa8014000, 0x350,
            'BCRDEMODANT', 'MODEM_S.BCRDEMODANT', 'read-write',
            u"",
            0x10020000, 0x9FFF97E0,
            0x00001000, 0x00002000,
            0x00003000)

        self.SWANTTIMER = RM_Field_MODEM_S_BCRDEMODANT_SWANTTIMER(self)
        self.zz_fdict['SWANTTIMER'] = self.SWANTTIMER
        self.BECOEN = RM_Field_MODEM_S_BCRDEMODANT_BECOEN(self)
        self.zz_fdict['BECOEN'] = self.BECOEN
        self.SKIP2PHTHD = RM_Field_MODEM_S_BCRDEMODANT_SKIP2PHTHD(self)
        self.zz_fdict['SKIP2PHTHD'] = self.SKIP2PHTHD
        self.ANWAIT = RM_Field_MODEM_S_BCRDEMODANT_ANWAIT(self)
        self.zz_fdict['ANWAIT'] = self.ANWAIT
        self.AGCGAINUPB = RM_Field_MODEM_S_BCRDEMODANT_AGCGAINUPB(self)
        self.zz_fdict['AGCGAINUPB'] = self.AGCGAINUPB
        self.SKIP2PH = RM_Field_MODEM_S_BCRDEMODANT_SKIP2PH(self)
        self.zz_fdict['SKIP2PH'] = self.SKIP2PH
        self.BYP1P5 = RM_Field_MODEM_S_BCRDEMODANT_BYP1P5(self)
        self.zz_fdict['BYP1P5'] = self.BYP1P5
        self.ANT2PMTHD = RM_Field_MODEM_S_BCRDEMODANT_ANT2PMTHD(self)
        self.zz_fdict['ANT2PMTHD'] = self.ANT2PMTHD
        self.BCRDEMODANTDIV = RM_Field_MODEM_S_BCRDEMODANT_BCRDEMODANTDIV(self)
        self.zz_fdict['BCRDEMODANTDIV'] = self.BCRDEMODANTDIV
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODRSSI(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODRSSI, self).__init__(rmio, label,
            0xa8014000, 0x354,
            'BCRDEMODRSSI', 'MODEM_S.BCRDEMODRSSI', 'read-write',
            u"",
            0x60000020, 0xFE001DFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.RSSIARRTHD = RM_Field_MODEM_S_BCRDEMODRSSI_RSSIARRTHD(self)
        self.zz_fdict['RSSIARRTHD'] = self.RSSIARRTHD
        self.RSSIMATAP = RM_Field_MODEM_S_BCRDEMODRSSI_RSSIMATAP(self)
        self.zz_fdict['RSSIMATAP'] = self.RSSIMATAP
        self.MUTERSSICNT = RM_Field_MODEM_S_BCRDEMODRSSI_MUTERSSICNT(self)
        self.zz_fdict['MUTERSSICNT'] = self.MUTERSSICNT
        self.PRWOFFSET = RM_Field_MODEM_S_BCRDEMODRSSI_PRWOFFSET(self)
        self.zz_fdict['PRWOFFSET'] = self.PRWOFFSET
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODARR0(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODARR0, self).__init__(rmio, label,
            0xa8014000, 0x358,
            'BCRDEMODARR0', 'MODEM_S.BCRDEMODARR0', 'read-write',
            u"",
            0x00600026, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SCHPRDLO = RM_Field_MODEM_S_BCRDEMODARR0_SCHPRDLO(self)
        self.zz_fdict['SCHPRDLO'] = self.SCHPRDLO
        self.EYEQUALEN = RM_Field_MODEM_S_BCRDEMODARR0_EYEQUALEN(self)
        self.zz_fdict['EYEQUALEN'] = self.EYEQUALEN
        self.SCHPRDHI = RM_Field_MODEM_S_BCRDEMODARR0_SCHPRDHI(self)
        self.zz_fdict['SCHPRDHI'] = self.SCHPRDHI
        self.ARRRSTEN = RM_Field_MODEM_S_BCRDEMODARR0_ARRRSTEN(self)
        self.zz_fdict['ARRRSTEN'] = self.ARRRSTEN
        self.ARRTOLER = RM_Field_MODEM_S_BCRDEMODARR0_ARRTOLER(self)
        self.zz_fdict['ARRTOLER'] = self.ARRTOLER
        self.DIFF0RSTEN = RM_Field_MODEM_S_BCRDEMODARR0_DIFF0RSTEN(self)
        self.zz_fdict['DIFF0RSTEN'] = self.DIFF0RSTEN
        self.PHSPIKETHD = RM_Field_MODEM_S_BCRDEMODARR0_PHSPIKETHD(self)
        self.zz_fdict['PHSPIKETHD'] = self.PHSPIKETHD
        self.ARRDETTHD = RM_Field_MODEM_S_BCRDEMODARR0_ARRDETTHD(self)
        self.zz_fdict['ARRDETTHD'] = self.ARRDETTHD
        self.SCHFRZEN = RM_Field_MODEM_S_BCRDEMODARR0_SCHFRZEN(self)
        self.zz_fdict['SCHFRZEN'] = self.SCHFRZEN
        self.EYEXESTEN = RM_Field_MODEM_S_BCRDEMODARR0_EYEXESTEN(self)
        self.zz_fdict['EYEXESTEN'] = self.EYEXESTEN
        self.EYEXESTFAST = RM_Field_MODEM_S_BCRDEMODARR0_EYEXESTFAST(self)
        self.zz_fdict['EYEXESTFAST'] = self.EYEXESTFAST
        self.ARRDETSRC = RM_Field_MODEM_S_BCRDEMODARR0_ARRDETSRC(self)
        self.zz_fdict['ARRDETSRC'] = self.ARRDETSRC
        self.ARRQPM = RM_Field_MODEM_S_BCRDEMODARR0_ARRQPM(self)
        self.zz_fdict['ARRQPM'] = self.ARRQPM
        self.ARRDETEN = RM_Field_MODEM_S_BCRDEMODARR0_ARRDETEN(self)
        self.zz_fdict['ARRDETEN'] = self.ARRDETEN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODARR1(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODARR1, self).__init__(rmio, label,
            0xa8014000, 0x35C,
            'BCRDEMODARR1', 'MODEM_S.BCRDEMODARR1', 'read-write',
            u"",
            0x80000000, 0xFFFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.ARREYEQUAL = RM_Field_MODEM_S_BCRDEMODARR1_ARREYEQUAL(self)
        self.zz_fdict['ARREYEQUAL'] = self.ARREYEQUAL
        self.EYEOPENTHD = RM_Field_MODEM_S_BCRDEMODARR1_EYEOPENTHD(self)
        self.zz_fdict['EYEOPENTHD'] = self.EYEOPENTHD
        self.SYMBWMAX = RM_Field_MODEM_S_BCRDEMODARR1_SYMBWMAX(self)
        self.zz_fdict['SYMBWMAX'] = self.SYMBWMAX
        self.SYMBWMIN = RM_Field_MODEM_S_BCRDEMODARR1_SYMBWMIN(self)
        self.zz_fdict['SYMBWMIN'] = self.SYMBWMIN
        self.BCRCFESRC = RM_Field_MODEM_S_BCRDEMODARR1_BCRCFESRC(self)
        self.zz_fdict['BCRCFESRC'] = self.BCRCFESRC
        self.CFEQUALTHD = RM_Field_MODEM_S_BCRDEMODARR1_CFEQUALTHD(self)
        self.zz_fdict['CFEQUALTHD'] = self.CFEQUALTHD
        self.KSICOMPEN = RM_Field_MODEM_S_BCRDEMODARR1_KSICOMPEN(self)
        self.zz_fdict['KSICOMPEN'] = self.KSICOMPEN
        self.ENCFEQUAL = RM_Field_MODEM_S_BCRDEMODARR1_ENCFEQUAL(self)
        self.zz_fdict['ENCFEQUAL'] = self.ENCFEQUAL
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODARR2(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODARR2, self).__init__(rmio, label,
            0xa8014000, 0x360,
            'BCRDEMODARR2', 'MODEM_S.BCRDEMODARR2', 'read-write',
            u"",
            0x00000000, 0x8000003F,
            0x00001000, 0x00002000,
            0x00003000)

        self.CONSYMOL = RM_Field_MODEM_S_BCRDEMODARR2_CONSYMOL(self)
        self.zz_fdict['CONSYMOL'] = self.CONSYMOL
        self.RAWDCHKALWAYON = RM_Field_MODEM_S_BCRDEMODARR2_RAWDCHKALWAYON(self)
        self.zz_fdict['RAWDCHKALWAYON'] = self.RAWDCHKALWAYON
        self.OUTRNGCHK = RM_Field_MODEM_S_BCRDEMODARR2_OUTRNGCHK(self)
        self.zz_fdict['OUTRNGCHK'] = self.OUTRNGCHK
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODKSI(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODKSI, self).__init__(rmio, label,
            0xa8014000, 0x364,
            'BCRDEMODKSI', 'MODEM_S.BCRDEMODKSI', 'read-write',
            u"",
            0x002C2020, 0x007F7F7F,
            0x00001000, 0x00002000,
            0x00003000)

        self.BCRKSI1 = RM_Field_MODEM_S_BCRDEMODKSI_BCRKSI1(self)
        self.zz_fdict['BCRKSI1'] = self.BCRKSI1
        self.BCRKSI2 = RM_Field_MODEM_S_BCRDEMODKSI_BCRKSI2(self)
        self.zz_fdict['BCRKSI2'] = self.BCRKSI2
        self.BCRKSI3 = RM_Field_MODEM_S_BCRDEMODKSI_BCRKSI3(self)
        self.zz_fdict['BCRKSI3'] = self.BCRKSI3
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_BCRDEMODPMEXP(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_BCRDEMODPMEXP, self).__init__(rmio, label,
            0xa8014000, 0x368,
            'BCRDEMODPMEXP', 'MODEM_S.BCRDEMODPMEXP', 'read-write',
            u"",
            0x58965555, 0xFEFFFFFF,
            0x00001000, 0x00002000,
            0x00003000)

        self.BCRPMEXP = RM_Field_MODEM_S_BCRDEMODPMEXP_BCRPMEXP(self)
        self.zz_fdict['BCRPMEXP'] = self.BCRPMEXP
        self.BCRCFECOSTTHD = RM_Field_MODEM_S_BCRDEMODPMEXP_BCRCFECOSTTHD(self)
        self.zz_fdict['BCRCFECOSTTHD'] = self.BCRCFECOSTTHD
        self.BCRPHSCALE = RM_Field_MODEM_S_BCRDEMODPMEXP_BCRPHSCALE(self)
        self.zz_fdict['BCRPHSCALE'] = self.BCRPHSCALE
        self.BCRCFESCHWIN = RM_Field_MODEM_S_BCRDEMODPMEXP_BCRCFESCHWIN(self)
        self.zz_fdict['BCRCFESCHWIN'] = self.BCRCFESCHWIN
        self.BCRPMACQWIN = RM_Field_MODEM_S_BCRDEMODPMEXP_BCRPMACQWIN(self)
        self.zz_fdict['BCRPMACQWIN'] = self.BCRPMACQWIN
        self.__dict__['zz_frozen'] = True


class RM_Register_MODEM_S_SPARE(Base_RM_Register):
    def __init__(self, rmio, label):
        self.__dict__['zz_frozen'] = False
        super(RM_Register_MODEM_S_SPARE, self).__init__(rmio, label,
            0xa8014000, 0x400,
            'SPARE', 'MODEM_S.SPARE', 'read-write',
            u"",
            0x00000000, 0x000000FF,
            0x00001000, 0x00002000,
            0x00003000)

        self.SPARE = RM_Field_MODEM_S_SPARE_SPARE(self)
        self.zz_fdict['SPARE'] = self.SPARE
        self.__dict__['zz_frozen'] = True


