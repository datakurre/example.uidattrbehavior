# -*- coding:utf-8 -*-
from Products.CMFCore.Expression import Expression
from plone.dexterity.fti import DexterityFTI
from plone.dexterity.utils import createContentInContainer
from plone.app.testing import (
    setRoles,
    TEST_USER_ID,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    IntegrationTesting,
    FunctionalTesting,
)
from plone.testing import z2
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE


class UIDAttrbehaviorTests(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import venusianconfiguration
        venusianconfiguration.enable()
        import example.uidattrbehavior
        self.loadZCML(package=example.uidattrbehavior,
                      name='configure.py')

    def setUpPloneSite(self, portal):
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')
        self.applyProfile(
            portal, 'example.uidattrbehavior:default')

        # Define minimal buyable content type
        fti = DexterityFTI('example')
        fti.title = u'example'
        fti.icon_expr = 'string:${portal_url}/document_icon.png'
        fti.icon_expr_object = Expression(fti.icon_expr)
        fti.model_source = u"""\
<model xmlns="http://namespaces.plone.org/supermodel/schema">
  <schema />
</model>"""
        fti.behaviors = (
            'plone.app.content.interfaces.INameFromTitle',
            'plone.app.dexterity.behaviors.metadata.IBasic',
            'plone.app.dexterity.behaviors.metadata.ICategorization',
            'example.uidattrbehavior.behaviors.IUIDAttrBehavior',
        )
        portal.portal_types._setObject('example', fti)

        setRoles(portal, TEST_USER_ID, ['Manager'])
        createContentInContainer(portal, 'example', title=u'Hello World')


UIDATTRBEHAVIOR_FIXTURE = UIDAttrbehaviorTests()

UIDATTRBEHAVIOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UIDATTRBEHAVIOR_FIXTURE,),
    name='UIDAttrbehaviorTests:Integration')

UIDATTRBEHAVIOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UIDATTRBEHAVIOR_FIXTURE,),
    name='UIDAttrbehaviorTests:Functional')

UIDATTRBEHAVIOR_ROBOT_TESTING = FunctionalTesting(
    bases=(UIDATTRBEHAVIOR_FIXTURE,
           REMOTE_LIBRARY_BUNDLE_FIXTURE,
           z2.ZSERVER),
    name='UIDAttrbehaviorTests:Robot')
