# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Media'
        db.create_table(u'dropbox_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'dropbox', ['Media'])


    def backwards(self, orm):
        # Deleting model 'Media'
        db.delete_table(u'dropbox_media')


    models = {
        u'dropbox.media': {
            'Meta': {'object_name': 'Media'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['dropbox']