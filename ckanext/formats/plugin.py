import types
from logging import getLogger

from sqlalchemy.util import OrderedDict

from ckan import logic
from ckan import model
import ckan.plugins as p
from ckan.lib.plugins import DefaultDatasetForm
from ckan.lib.navl import dictization_functions

log = getLogger(__name__)
assert not log.disabled

log.error('AJS: FORMAT HELP!')

DATASET_TYPE_NAME = 'formats'


class FormatsPlugin(p.SingletonPlugin, DefaultDatasetForm):
    p.implements(p.IDatasetForm )
    p.implements(p.IConfigurer)
#    p.implements(p.IAuthFunctions )

    ## IAuthFunctions

#    def get_auth_functions(self):
#        module_root = 'ckanext.formats.logic.auth'
#        auth_functions = _get_logic_functions(module_root)
#
#        return auth_functions


    ## IDatasetForm

    def is_fallback(self):
        return False

    def package_types(self):
        return [DATASET_TYPE_NAME]

    def search_template(self):
        log.error('AJS: formats plugin search_template')
        return 'formats/psearch.html'

    def package_form(self):
        log.error('AJS: formats plugin package_form')
        return 'formats/new_source_form.html'

    #def search_template(self):
    #    return 'source/search.html'

    def read_template(self):
        return 'package/read.html'

    def new_template(self):
        return 'formats/new.html'

    def edit_template(self):
        return 'source/edit.html'

    def update_config(self, config):
         log.error('AJS: formats plugin update_config')
         p.toolkit.add_template_directory(config, 'templates')

    def setup_template_variables(self, context, data_dict):
        #p.toolkit.c.harvest_source = p.toolkit.c.pkg_dict
        p.toolkit.c.dataset_type = DATASET_TYPE_NAME

def _get_logic_functions(module_root, logic_functions = {}):

    for module_name in ['get', 'create', 'update','delete']:
        module_path = '%s.%s' % (module_root, module_name,)
        try:
            module = __import__(module_path)
        except ImportError:
            log.debug('No auth module for action "{0}"'.format(module_name))
            continue

        for part in module_path.split('.')[1:]:
            module = getattr(module, part)

        for key, value in module.__dict__.items():
            if not key.startswith('_') and  (hasattr(value, '__call__')
                        and (value.__module__ == module_path)):
                logic_functions[key] = value

    return logic_functions

