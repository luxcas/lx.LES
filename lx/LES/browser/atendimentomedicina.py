# -*- coding: utf-8 -*-


# Product imports
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

#Plone imports
from plone.memoize.instance import memoize

#Libs imports


# lx.LES imports
from lx.LES.interfaces.contents import IAtendimentoMedicina
from lx.LES.browser.utils import getFields


class AtendimentoMedicinaView(BrowserView):
    """ view do exames de sangue do paciente
    """

    @memoize
    def getNomePaciente(self):
        """Retorna o nome do paciente
        """
        nome = self.context.aq_parent.Title()
        return nome

    @memoize
    def getAtendimentosMedicina(self):
        """Retorna todos os atendimentos do paciente
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_atendimentos = '/'.join(self.context.aq_parent.getPhysicalPath())
        atendimentos = catalog(object_provides=IAtendimentoMedicina.__identifier__,
                           path=path_atendimentos,
                           sort_on='Date',
                           sort_order='reverse',)
        return atendimentos

    @memoize
    def getFields(self, schemata):
        """Retorna todos os campos do schemata
        """
        return getFields(self, schemata)
