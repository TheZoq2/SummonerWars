
################################
## Spell effect implementations

def CheckForFaliure(user, target, type):
    if user.fails:
        user.fails -= 1
        return True
    elif target.isProtected:
        return True


def HandleStatusEffects(user, target, type):
    if CheckForFaliure(user, target, type):
        return 0
    magnitude = 1
    if user == target:
        for effect in user.statusEffects["onTargetSelf"]:
            magnitude *= effect(target, type)
    else:
        for effect in user.statusEffects["onTargetEnemy"]:
            magnitude *= effect(target, type)
    for effect in user.statusEffects["onHitTarget"]:
        magnitude *= effect(target, type)
    for effect in target.statusEffects["onGetHit"]:
        magnitude *= effect(target, type)

    return magnitude

def NoEffect(user, target):
    pass

def FireWater(user, target):
    print("FireWater")

def WaterFire(user, target):
    print("WaterFire")

def DragonFire(user, target):
    print("DragonFire")

def Oops(user, target):
    user.currentHealth -= 10
    
def Heal(user, target):
    multiplier = HandleStatusEffects(user, target, "heal")
    if not multiplier: return
    target.currentHealth += multiplier * 10

def GreaterHeal(user, target):
    multiplier = HandleStatusEffects(user, target, "heal")
    if not multiplier: return
    target.currentHealth += multiplier * 20

def Strike(user, target):
    multiplier = HandleStatusEffects(user, target, "dmg")
    if not multiplier: return
    target.currentHealth -= multiplier * 10

def OpenMind(user, target):
    multiplier = HandleStatusEffects(user, target, "debuff")
    if not multiplier: return

    if multiplier:
        target.statusEffects["onGetHit"].append(lambda tgt, type : 1,2 if type == "heal" else 1)


def Anguish(user, target):
    multiplier = HandleStatusEffects(user, target, "debuff")
    if not multiplier: return
    def Anguished(tgt, type):
        if type != "dmg":
            tgt.currentHealth -= 20
        return 1

    if multiplier:
        target.statusEffects["onGetHit"].append(Anguished)


def BloodArrow(user, target):
    multiplier = HandleStatusEffects(user, target, "dmg")
    if not multiplier: return

    user.currentHealth -= 5
    target.currentHealth -= multiplier * 10