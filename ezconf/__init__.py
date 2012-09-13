# coding=utf-8
from django.conf import settings
import os, json

from ezconf.models import EZSettingsData

class EZSettings(object):
    '''EZLog 配置存储模型
    
    为了能够按顺序生成HTML表单,
    配置数据是有序分组的(参考 ezlog_config.json).'''

    def __init__(self):
        self.load_settings()

    def load_settings(self):
        '''(重新)加载配置文件'''
        settings_data = EZSettingsData.objects.get(pk=1)
        self._settings = json.loads(settings_data.data)
        self._mtime = settings_data.mtime

    @property
    def settings(self):
        '''返回最新的配置数据'''
        if EZSettingsData.objects.get(pk=1).mtime > self._mtime:
            self.load_settings()
        return self._settings

    def as_dict(self):
        '''根据*分组有序*数据生成*无序字典*数据, 更方便查找.
        返回的数据中不包含用来辅助生成HTML表单的属性'''
        settings_dict = {}
        for g in self.settings:
            g_name = g['name'] # 当前组名
            settings_dict[g_name] = {}
            for f in g['fields']:
                f_name = f['name'] # 当前字段名
                settings_dict[g_name][f_name] = f['value']
        return settings_dict

    def get(self, gf, default=None):
        try:
            g,f = gf.split('.')
            return self.as_dict()[g][f]
        except (ValueError, KeyError):
            return default

    def as_json(self):
        # return a unicode instance.
        return json.dumps(self._settings, ensure_ascii=True)


    def as_form(self):
        pass

    def save(self):
        settings_data = EZSettingsData.objects.get(pk=1)
        settings_data.data = self.as_json().encode('utf-8')
        settings_data.save()

    def as_readable_json(self):
        return json.dumps(self._settings, ensure_ascii=False,
                          indent=4)

    def reset_settings_with_json_data(self, data):
        '''使用data中提供的json数据覆盖当前settings'''
        self._settings = json.loads(data)
        self.save()

    def update_setting_items_with_json_data(self, data):
        '''更新设置项目, 对于已有项目继续使用原值'''
        new_settings = json.loads(data)
        for g in new_settings:
            for f in g['fields']:
                key = '%s.%s' % (g['name'], f['name'])
                f['value'] = self.get(key, f['value'])
        self._settings = new_settings
        self.save()

try:
    from django.db.utils import DatabaseError
    ezsettings = EZSettings()
except: # maybe database not synced!
    pass
