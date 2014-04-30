# -*- coding: utf-8 -*-
from venusianconfiguration import configure

import os
from zope.interface import provider
from zope import schema
from zope.schema.interfaces import IContextAwareDefaultFactory
from plone.supermodel import model
from plone.uuid.interfaces import IUUID

from plone.app.layout.viewlets.interfaces import IAboveContent

from example.uidattrbehavior.interfaces import UIDAttrBehaviorLayer

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('example.uidattrbehavior')


@provider(IContextAwareDefaultFactory)
def UIDAttrFactory(context):
    return IUUID(context)


@configure.plone.behavior.provides(
    title=_(u'UID Attr Behavior'),
    description=_(u'Provides UID attr for Dexterity content objects'))
class IUIDAttrBehavior(model.Schema):
    UID = schema.BytesLine(
        defaultFactory=UIDAttrFactory,
    )


configure.browser.viewlet(
    name='example.uidattrbehavior.viewlet',
    manager=IAboveContent,
    layer=UIDAttrBehaviorLayer,
    template=os.path.join('templates', 'demoviewlet.pt'),
    permission='zope2.View',
)
