# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'storefront_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'storefront', ['Category'])

        # Adding model 'Product'
        db.create_table(u'storefront_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('inventory', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('hero_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('picture_thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storefront.Category'])),
        ))
        db.send_create_signal(u'storefront', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'storefront_category')

        # Deleting model 'Product'
        db.delete_table(u'storefront_product')


    models = {
        u'storefront.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'storefront.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storefront.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hero_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture_thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['storefront']