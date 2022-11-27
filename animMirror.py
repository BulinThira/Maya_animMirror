#animMirror.py - Python Script

# DESCRIPTION: Tool for mirroring animation. Can be used on both FK and IK
# REQUIRE: Python3
# AUTHOR: BulinThira - Github

import maya.cmds as mc

#UI

def animMirror():
    if mc.window('animMirror_window', q=True, ex=True):
        mc.deleteUI('animMirror_window', window=True)
    mc.window('animMirror_window', title='Animation Mirror')
    mc.columnLayout(adj=True)
    
    mc.button(label='mirror translation', h=30, c=translate_selectCtrl)
    
    mc.button(label='mirror rotation', h=30, c=rot_selectCtrl)
    
    mc.rowLayout(numberOfColumns=2)
    mc.text('Get Specific Attribute: ')
    mc.textField('GSA_TF', h=30)
    mc.setParent('..')
    
    mc.button(label='mirror specific', h=30, c=specific_selectCtrl)
    
    
    mc.showWindow('animMirror_window')
    mc.window('animMirror_window', e=True, wh=(300,125))
    
    
tX_Selected = []
tY_Selected = []
tZ_Selected = []

rotX_Selected = []
rotY_Selected = []
rotZ_Selected = []

specific_Selected = []



def rot_selectCtrl(*args):
   sels = mc.ls(sl=True)
   for each in sels:
       
       rotX_each = mc.getAttr(f'{each}.rotateX')
       rotY_each = mc.getAttr(f'{each}.rotateY')
       rotZ_each = mc.getAttr(f'{each}.rotateZ')
       
       rotX_Selected.append(rotX_each)
       rotY_Selected.append(rotY_each)
       rotZ_Selected.append(rotZ_each)


   mc.setAttr(f'{sels[0]}.rotateX', rotX_Selected[1])
   mc.setAttr(f'{sels[1]}.rotateX', rotX_Selected[0])
   
   mc.setAttr(f'{sels[0]}.rotateY', rotY_Selected[1])
   mc.setAttr(f'{sels[1]}.rotateY', rotY_Selected[0])
   
   mc.setAttr(f'{sels[0]}.rotateZ', rotZ_Selected[1])
   mc.setAttr(f'{sels[1]}.rotateZ', rotZ_Selected[0])
   
   mc.select(cl=True)
   
   del rotX_Selected[:]
   del rotY_Selected[:]
   del rotZ_Selected[:]
   

def translate_selectCtrl(*args):
   sels = mc.ls(sl=True)
   for each in sels:
       
       tX_each = mc.getAttr(f'{each}.translateX')
       tY_each = mc.getAttr(f'{each}.translateY')
       tZ_each = mc.getAttr(f'{each}.translateZ')
       
       tX_Selected.append(tX_each)
       tY_Selected.append(tY_each)
       tZ_Selected.append(tZ_each)


   mc.setAttr(f'{sels[0]}.translateX', tX_Selected[1])
   mc.setAttr(f'{sels[1]}.translateX', tX_Selected[0])
   
   mc.setAttr(f'{sels[0]}.translateY', tY_Selected[1])
   mc.setAttr(f'{sels[1]}.translateY', tY_Selected[0])
   
   mc.setAttr(f'{sels[0]}.translateZ', tZ_Selected[1])
   mc.setAttr(f'{sels[1]}.translateZ', tZ_Selected[0])
   
   mc.select(cl=True)
   del tX_Selected[:]
   del tY_Selected[:]
   del tZ_Selected[:]

def specific_selectCtrl(*args):
    speName = mc.textField('GSA_TF', q=True, tx=True)
    
    sels = mc.ls(sl=True)
    for i in sels:
        speSel_each = mc.getAttr(f'{i}.{speName}')
        
        specific_Selected.append(speSel_each)
        
    mc.setAttr(f'{sels[0]}.{speName}', specific_Selected[1])
    mc.setAttr(f'{sels[1]}.{speName}', specific_Selected[0])
    
    mc.select(cl=True)
    del specific_Selected[:]

animMirror()
