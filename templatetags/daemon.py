from django import template
from django.apps import apps
from django.urls import reverse
from django.contrib import admin
from django.utils.text import capfirst
from django.contrib.admin.models import LogEntry


register = template.Library()


@register.simple_tag(takes_context=True)
def get_app_list(context, order=True):

    admin_site = admin.site
    app_dict = {}
    request = context['request']

    for model, model_admin in admin_site._registry.items():
        app_label = model._meta.app_label

        has_module_perms = model_admin.has_module_permission(request)
        if not has_module_perms:
            continue

        perms = model_admin.get_model_perms(request)
        if True not in perms.values():
            continue

        info = (app_label, model._meta.model_name)
        model_dict = {
            'name': capfirst(model._meta.verbose_name_plural),
            'object_name': model._meta.object_name,
            'perms': perms,
            'model_name': model._meta.model_name}

        if perms.get('change', False):
            try:
                model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info,
                    current_app=admin_site.name)
            except NoReverseMatch:
                pass
        if perms.get('add', False):
            try:
                model_dict['add_url'] = reverse('admin:%s_%s_add' % info,
                    current_app=admin_site.name)
            except NoReverseMatch:
                pass

        if app_label in app_dict:
            app_dict[app_label]['models'].append(model_dict)
        else:
            app_dict[app_label] = {
                'name': apps.get_app_config(app_label).verbose_name,
                'app_label': app_label,
                'app_url': reverse('admin:app_list', kwargs={'app_label': app_label},
                    current_app=admin_site.name),
                'has_module_perms': has_module_perms,
                'models': [model_dict]}

    if order:
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

            if request.path.startswith(app['app_url']):
                app['is_selected'] = True

                for model in app['models']:
                    if request.path.startswith(model['admin_url']):
                        model['is_selected'] = True
                        break

    return app_list
