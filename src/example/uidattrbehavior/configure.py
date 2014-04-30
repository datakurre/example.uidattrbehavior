# -*- coding: utf-8 -*-
from venusianconfiguration import (
    configure,
    scan
)

import plone.behavior
import plone.app.dexterity

from example.uidattrbehavior import behaviors

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('example.uidattrbehavior')

configure.include(package=plone.app.dexterity)
configure.include(package=plone.behavior, file_='meta.zcml')

configure.i18n.registerTranslations(directory='locales')

scan(behaviors)

configure.gs.registerProfile(
    name=u'default',
    title=_(u'UID Attr Behavior'),
    description=_(u'Provides UID attr for Dexterity content objects'),
    directory=u'profiles/default',
    provides=u'Products.GenericSetup.interfaces.EXTENSION'
)
