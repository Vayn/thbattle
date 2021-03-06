# -*- coding: utf-8 -*-

from gamepack.thb import characters
from gamepack.thb.ui.ui_meta.common import gen_metafunc
from gamepack.thb.ui.ui_meta.common import passive_clickable, passive_is_action_valid
from gamepack.thb.ui.resource import resource as gres

__metaclass__ = gen_metafunc(characters.tewi)


class Luck:
    # Skill
    name = u'幸运'
    clickable = passive_clickable
    is_action_valid = passive_is_action_valid


class LuckDrawCards:
    def effect_string(act):
        return u'|G【%s】|r觉得手上没有牌就输了，于是又摸了2张牌。' % (
            act.source.ui_meta.char_name,
        )


class Tewi:
    # Character
    char_name = u'因幡帝'
    port_image = gres.tewi_port
    description = (
        u'|DB幸运的腹黑兔子 因幡帝 体力：4|r\n\n'
        u'|G幸运|r：|B锁定技|r，当你的手牌数为0时，立即摸2张牌。'
    )
