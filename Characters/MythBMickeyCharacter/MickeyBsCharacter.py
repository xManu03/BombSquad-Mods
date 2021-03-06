# Mickey #Created By MythB # http://github.com/MythB ###################################
t = Appearance("Mickey")
t.colorTexture = "mickeyColor"
t.colorMaskTexture = "mickeyColorMask"
t.defaultColor = (0.5,0.5,0.5)
t.defaultHighlight = (0.5,0.5,0.5)
t.iconTexture = "mickeyIcon"
t.iconMaskTexture = "mickeyIconMask"
t.headModel =     "mickeyHead"
t.torsoModel =    "mickeyTorso"
t.pelvisModel =   "mickeyPelvis"
t.upperArmModel = "mickeyUpperArm"
t.foreArmModel =  "mickeyForeArm"
t.handModel =     "mickeyHand"
t.upperLegModel = "mickeyUpperLeg"
t.lowerLegModel = "mickeyLowerLeg"
t.toesModel =     "empty"
mickeyAttack =    ['mickeyAttack1','mickeyAttack2','mickeyAttack3']
mickeyHit = ['mickeyHit1','mickeyHit2','mickeyHit3','mickeyHit4']
mickeyDead    = ['mickeyDeath','mickeyDeath2']
mickeyJump    = ['mickeyJump']
mickeyFall   = ['mickeyFall']
t.attackSounds = mickeyAttack
t.jumpSounds = mickeyJump
t.impactSounds = mickeyHit
t.deathSounds= mickeyDead
t.pickupSounds = mickeyAttack
t.fallSounds= mickeyFall
t.style = 'agent'
