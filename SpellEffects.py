import pyglet

def EffectDispatchCenterSingletonFactory():
    class EffectDispatchCenterSingletonImplementation(pyglet.event.EventDispatcher):
        def __init__(self):
            EffectDispatchCenterSingletonImplementation.register_event_type("on_spell")

        def dispatch_spell(self, user, target, type):
            self.dispatch_event("on_spell", user, target, type)

    return EffectDispatchCenterSingletonImplementation()

effectDispatchCenter = EffectDispatchCenterSingletonFactory()

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
    print("No spell")
    effectDispatchCenter.dispatch_spell(user, target, "NoSpell")

def Oops(user, target):
    user.reduceHealth(10)
    
def Heal(user, target):
    multiplier = HandleStatusEffects(user, target, "heal")
    if not multiplier: return
    target.addHealth(multiplier * 7)

def GreaterHeal(user, target):
    multiplier = HandleStatusEffects(user, target, "heal")
    if not multiplier: return
    target.addHealth(multiplier * 11)

def Strike(user, target):
    multiplier = HandleStatusEffects(user, target, "dmg")
    if not multiplier: return
    target.reduceHealth(multiplier * 10)

def OpenMind(user, target):
    multiplier = HandleStatusEffects(user, target, "debuff")
    if not multiplier: return

    if multiplier:
        target.statusEffects["onGetHit"].append(lambda tgt, type : 1.2 if type == "heal" else 1)

def Anguish(user, target):
    multiplier = HandleStatusEffects(user, target, "debuff")
    if not multiplier: return
    def Anguished(tgt, type):
        if type != "dmg":
            tgt.reduceHealth(20)
        return 1

    if multiplier:
        target.statusEffects["onGetHit"].append(Anguished)

def BloodArrow(user, target):
    multiplier = HandleStatusEffects(user, target, "dmg")
    if not multiplier: return

    user.reduceHealth(5)
    target.reduceHealth(multiplier * 10)

def Turmoil(user, target):
    multiplier = HandleStatusEffects(user, target, "debuff")
    if not multiplier: return

    target.fails += 1

def Nova(user, target):
    multiplier = HandleStatusEffects(user, target, "dmg")
    if not multiplier: return

    user.reduceHealth(multiplier * 5)
    user.other.reduceHealth(multiplier * 5)

def Equilibrium(user, target):
    if target.currentHealth > target.other.currentHealth:
        multiplier = HandleStatusEffects(user, target, "dmg")
        if not multiplier: return
        target.reduceHealth(multiplier * 10)
    else:
        multiplier = HandleStatusEffects(user, target, "heal")
        if not multiplier: return
        target.addHealth(multiplier * 10)

def OmniPower(user, target):
    # Ignores faliure and multipliers. It's just that OP

    target.reduceHealth(15)
