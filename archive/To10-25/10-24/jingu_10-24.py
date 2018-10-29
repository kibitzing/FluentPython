#!/anaconda3/envs/tensorflow/bin/python
#-*- coding: utf-8 -*-
""" 
    Created by Jingu Kang on 24/10/2018.
    Copyright © 2018 Jingu Kang. All rights reserved.

    DESCRIPTION: 
        practice using closure
"""

def WizardSchoolAdmission():

    WizardBlackList = {'볼드모트', '말포이', '케실리우스','두들리'}
    WizardList = {'Harry', '해그리드', 'Dr.Strange'}

    def wizard(nameOfWizard):
        name = nameOfWizard
        if name in WizardBlackList:
            print('{}, Go to jail!'.format(name))

        elif name in WizardList:
            print('{}, you are already a wizard!'.format(name))

        else:
            WizardList.add(name)
            print('Welcome New Wizard, {}!'.format(name))

    return wizard

HogwartAdmission = WizardSchoolAdmission()
NewYorkSanctumAdmission = WizardSchoolAdmission()

HogwartAdmission('론')
HogwartAdmission('해그리드')
NewYorkSanctumAdmission('웡')
HogwartAdmission('볼드모트')
# Welcome New Wizard, 론!
# 해그리드, you are already a wizard!
# Welcome New Wizard, 웡!
# 볼드모트, Go to jail!

print(HogwartAdmission.__closure__[1].cell_contents)
# {'해그리드', 'Dr.Strange', 'Harry', '론'}