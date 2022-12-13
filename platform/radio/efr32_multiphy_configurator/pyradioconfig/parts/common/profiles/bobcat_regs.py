from pycalcmodel.core.output import ModelOutput, ModelOutputType
from pyradioconfig.parts.common.profiles.ocelot_regs import build_modem_regs_ocelot

def build_modem_regs_bobcat(model, profile, family):
    build_modem_regs_ocelot(model, profile, family)
    build_modem_regs_bobcat_only(model, profile)
    build_rac_clkmult_regs(model, profile)

def build_modem_regs_bobcat_only(model, profile):
    if model.part_family.lower() in ["bobcat"]:
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL8_ADBAAGCTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL8.ADBAAGCTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL8_ADBAMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL8.ADBAMODE'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL8_ADBACORRTHR2, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL8.ADBACORRTHR2'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL7_ADBARSSITHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL7.ADBARSSITHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL7_ADBARSSIDIFF, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL7.ADBARSSIDIFF'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL6_ADBACORRTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL6.ADBACORRTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL6_ADBACORRDIFF, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL6.ADBACORRDIFF'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL5_ADDIRECTCORR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL5.ADDIRECTCORR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL4_ADAGCGRTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL4.ADAGCGRTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL4_ADRSSIGRTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL4.ADRSSIGRTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADQUAL4_ADGRMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADQUAL4.ADGRMODE'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADFSM0_ADSTATREAD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADFSM0.ADSTATREAD'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADFSM0_ADSTAT1SEL, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADFSM0.ADSTAT1SEL'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADFSM0_ADSTAT2SEL, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADFSM0.ADSTAT2SEL'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADCTRL2_ADCTRL2, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADCTRL2.ADCTRL2'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADCTRL1_ADCTRL1, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADCTRL1.ADCTRL1'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC1_ADPCEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC1.ADPCEN'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC1_ADPCWNDSIZECHIP, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC1.ADPCWNDSIZECHIP'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC1_ADPCCORROFFSETCHIP, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC1.ADPCCORROFFSETCHIP'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC1_ADPCTIMINGBAUDS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC1.ADPCTIMINGBAUDS'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC1_ADPCWNDCNT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC1.ADPCWNDCNT'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC2_ADPCCORRSAMPLES, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC2.ADPCCORRSAMPLES'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC2_ADENCORR32, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC2.ADENCORR32'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC2_ADPCSIGAMPTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC2.ADPCSIGAMPTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC2_ADPCWNDCNTRST, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC2.ADPCWNDCNTRST'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC2_ADPCPRETIMINGBAUDS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC2.ADPCPRETIMINGBAUDS'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSEN'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSFILTLENGTH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSFILTLENGTH'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSAMPMANT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSAMPMANT'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSAMPEXP, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSAMPEXP'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSAVGEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSAVGEN'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSAVGPER, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSAVGPER'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSAVGWAIT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSAVGWAIT'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSAVGFREEZE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSAVGFREEZE'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC3_ADBBSSSELWRDATA, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC3.ADBBSSSELWARDATA'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC4_ADBBSSAMPLUT0, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC4.ADBBSSAMPLUT0'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC4_ADBBSSAMPLUT1, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC4.ADBBSSAMPLUT1'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC4_ADBBSSAMPLUT2, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC4.ADBBSSAMPLUT2'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC4_ADBBSSAMPLUT3, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC4.ADBBSSAMPLUT3'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC5_ADBBSSAMPLUT4, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC5.ADBBSSAMPLUT4'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC5_ADBBSSAMPLUT5, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC5.ADBBSSAMPLUT5'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC5_ADBBSSAMPLUT6, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC5.ADBBSSAMPLUT6'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC5_ADBBSSAMPLUT7, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC5.ADBBSSAMPLUT7'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC6_ADBBSSAMPLUT8, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC6.ADBBSSAMPLUT8'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC6_ADBBSSAMPLUT9, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC6.ADBBSSAMPLUT9'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC6_ADBBSSAMPLUT10, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC6.ADBBSSAMPLUT10'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC6_ADBBSSAMPLUT11, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC6.ADBBSSAMPLUT11'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC7_ADBBSSAMPLUT12, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC7.ADBBSSAMPLUT12'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC7_ADBBSSAMPLUT13, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC7.ADBBSSAMPLUT13'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC7_ADBBSSAMPLUT14, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC7.ADBBSSAMPLUT14'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC7_ADBBSSAMPLUT15, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC7.ADBBSSAMPLUT15'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC8_ADPCOSR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC8.ADPCOSR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC8_ADPCANTSAMPOFFSET, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC8.ADPCANTSAMPOFFSET'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC8_ADPCANTSAMPSWITCHWAIT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC8.ADPCANTSAMPSWITCHWAIT'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC8_ADPCANTSAMPBUF, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC8.ADPCANTSAMPBUF'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC8_ADPCANTSAMPWRITE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC8.ADPCANTSAMPWRITE'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC8_ADPCANTSAMPSWITCH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC8.ADPCANTSAMPSWITCH'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC9_ADBBSSAMPTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC9.ADBBSSAMPTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC9_ADBBSSAMPAVGLIM, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC9.ADBBSSAMPAVGLIM'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC9_ADBBSSSYNCEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC9.ADBBSSSYNCEN'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC9_ADBBSSUPTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC9.ADBBSSUPTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC9_ADBBSSDNTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC9.ADBBSSDNTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC10_ADBBSSAMPJUMP, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC10.ADBBSSAMPJUMP'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC10_ADBBSSCHANGEEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC10.ADBBSSCHANGEEN'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC10_ADBBSSCHGUPTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC10.ADBBSSCHGUPTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_ADPC10_ADBBSSCHGDNTHR, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.ADPC10.ADBBSSCHGDNTHR'))
        profile.outputs.append(ModelOutput(model.vars.MODEM_CHFCTRL_CHFSWSEL, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CHFCTRL.CHFSWSEL'))        

    profile.outputs.append(ModelOutput(model.vars.MODEM_COCURRMODE_CONCURRENT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COCURRMODE.CONCURRENT' ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_LONGRANGE_LRBLE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LONGRANGE.LRBLE' ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_LONGRANGE_LRBLEDSA, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LONGRANGE.LRBLEDSA' ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_LONGRANGE_LRCORRTHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LONGRANGE.LRCORRTHD' ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_LONGRANGE_LRDEC, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LONGRANGE.LRDEC' ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_LONGRANGE_LRTIMCORRTHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LONGRANGE.LRTIMCORRTHD' ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_AFC_DISAFCCTE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.AFC.DISAFCCTE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CHFSWCTRL_CHFSWTIME, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CHFSWCTRL.CHFSWTIME'))

    #profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT0_LNAMIXRFATT1, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT0.LNAMIXRFATT1'))
    #profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT0_LNAMIXRFATT2, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT0.LNAMIXRFATT2'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT0_LNAMIXRFATT3, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT0.LNAMIXRFATT3'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT1_LNAMIXRFATT4, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT1.LNAMIXRFATT4'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT1_LNAMIXRFATT5, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT1.LNAMIXRFATT5'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT1_LNAMIXRFATT6, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT1.LNAMIXRFATT6'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT2_LNAMIXRFATT7, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT2.LNAMIXRFATT7'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT2_LNAMIXRFATT8, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT2.LNAMIXRFATT8'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT2_LNAMIXRFATT9, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT2.LNAMIXRFATT9'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT3_LNAMIXRFATT10, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT3.LNAMIXRFATT10'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT3_LNAMIXRFATT11, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT3.LNAMIXRFATT11'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT3_LNAMIXRFATT12, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT3.LNAMIXRFATT12'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT4_LNAMIXRFATT13, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT4.LNAMIXRFATT13'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT4_LNAMIXRFATT14, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT4.LNAMIXRFATT14'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT4_LNAMIXRFATT15, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT4.LNAMIXRFATT15'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT5_LNAMIXRFATT16, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT5.LNAMIXRFATT16'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT5_LNAMIXRFATT17, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT5.LNAMIXRFATT17'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT5_LNAMIXRFATT18, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT5.LNAMIXRFATT18'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT6_LNAMIXRFATT19, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT6.LNAMIXRFATT19'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT6_LNAMIXRFATT20, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT6.LNAMIXRFATT20'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT6_LNAMIXRFATT21, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT6.LNAMIXRFATT21'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT7_LNAMIXRFATT22, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT7.LNAMIXRFATT22'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT7_LNAMIXRFATT23, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT7.LNAMIXRFATT23'))
    profile.outputs.append(ModelOutput(model.vars.AGC_PNRFATT7_LNAMIXRFATT24, '', ModelOutputType.SVD_REG_FIELD, readable_name='AGC.PNRFATT7.LNAMIXRFATT24'))

    profile.outputs.append(ModelOutput(model.vars.RAC_SYLOEN_SYLODIVRLOADCCLKSEL, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.SYLOEN.SYLODIVRLOADCCLKSEL'))


def build_rac_clkmult_regs(model, profile):
    # commented out registers are defined in lynx_regs.py (Lynx calculator didn't output all registers as clkmult was not used for IFADC clocking in prod PHYs)
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTBWCAL, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTBWCAL'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTDISICO, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTDISICO'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENBBDET, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENBBDET'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENBBXLDET, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENBBXLDET'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENBBXMDET, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENBBXMDET'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENCFDET, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENCFDET'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENDITHER, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENDITHER'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENDRVADC, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENDRVADC'))
    # profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENDRVN, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENDRVN'))
    # profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENDRVP, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENDRVP'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENDRVRX2P4G, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENDRVRX2P4G'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENDRVRXSUBG, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENDRVRXSUBG'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENDRVTXDUALB, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENDRVTXDUALB'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENFBDIV, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENFBDIV'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENREFDIV, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENREFDIV'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENREG1, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENREG1'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENREG2, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENREG2'))
    # profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENREG3, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENREG3'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENROTDET, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENROTDET'))
    # profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTENBYPASS40MHZ, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTENBYPASS40MHZ'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTFREQCAL, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTFREQCAL'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTREG2ADJI, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTREG2ADJI'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTREG1ADJV, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTREG1ADJV'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTREG2ADJV, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTREG2ADJV'))
    # profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTREG3ADJV, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTREG3ADJV'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTINNIBBLE, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN1.CLKMULTINNIBBLE'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTLDFNIB, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN1.CLKMULTLDFNIB'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTLDMNIB, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN1.CLKMULTLDMNIB'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTRDNIBBLE, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN1.CLKMULTRDNIBBLE'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTLDCNIB, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN1.CLKMULTLDCNIB'))
    # profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTDRVAMPSEL, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN1.CLKMULTDRVAMPSEL'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTCTRL_CLKMULTDIVN, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTCTRL.CLKMULTDIVN'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTCTRL_CLKMULTDIVR, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTCTRL.CLKMULTDIVR'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTCTRL_CLKMULTDIVX, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTCTRL.CLKMULTDIVX'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTCTRL_CLKMULTENRESYNC, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTCTRL.CLKMULTENRESYNC'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTCTRL_CLKMULTVALID, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTCTRL.CLKMULTVALID'))

