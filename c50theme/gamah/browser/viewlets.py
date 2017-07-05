from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common

class SearchBoxViewlet(common.SearchBoxViewlet):
    """Customizing the searchbox to use the locally defined page template
    """
    def render(self):
        return self.index()
    index = ViewPageTemplateFile('searchbox.pt')
    
class LogoViewlet(common.LogoViewlet):
    """Alter the logo to adapt for accessibility
    """
    def render(self):
        return self.index()
        index = ViewPageTemplateFile('logo.pt')