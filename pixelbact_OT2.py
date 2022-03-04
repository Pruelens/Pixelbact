

from opentrons import protocol_api

metadata = {'apiLevel': '2.11'}


def run(protocol: protocol_api.ProtocolContext):
    #plate with culture to paint with in column 1
    Plate1 = protocol.load_labware('greinerdeepwell2ml_96_wellplate_2000ul', 10)

    tiprack_p10 = protocol.load_labware('opentrons_96_filtertiprack_10ul', 11)

    PlateAgar1 = protocol.load_labware('1828grid_504_wellplate_1ul', 5)

    pipetteP10 = protocol.load_instrument('p10_single', 'left',
                                       tip_racks=[tiprack_p10])

    pipetteP10.well_bottom_clearance.aspirate = 1

    PipetteVolume=1.5
    
#Color 1
    if Color1_list==[]:
        pass
    else:
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['A1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color1_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()

#Color 2
    if Color2_list==[]:
        pass
    else:
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['B1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color2_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()

# Color 3
    if Color3_list==[]:
        pass
    else:
            
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['C1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color3_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()

# Color 4
    if Color4_list==[]:
        pass
    else:
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['D1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color4_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()

# Color 5
    if Color5_list==[]:
        pass
    else:
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['E1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color5_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()

# Color 6
    if Color6_list==[]:
        pass
    else:
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['F1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color6_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()

# Color 7
    if Color7_list==[]:
        pass
    else:
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['G1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color7_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()

# Color 8
    if Color8_list==[]:
        pass
    else:
        pipetteP10.pick_up_tip()
        pipetteP10.transfer(
            PipetteVolume,
            Plate1.wells_by_name()['H1'],
            [PlateAgar1.wells_by_name()[well_name] for well_name in Color8_list],
            blow_out=True,
            blowout_location='destination well',
            new_tip='never')
        pipetteP10.drop_tip()