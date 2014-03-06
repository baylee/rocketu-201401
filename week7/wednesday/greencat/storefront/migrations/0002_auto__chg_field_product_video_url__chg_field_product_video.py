# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.video_url'
        db.alter_column(u'storefront_product', 'video_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Product.video'
        db.alter_column(u'storefront_product', 'video', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Product.video_url'
        raise RuntimeError("Cannot reverse this migration. 'Product.video_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Product.video_url'
        db.alter_column(u'storefront_product', 'video_url', self.gf('django.db.models.fields.URLField')(max_length=200))

        # User chose to not deal with backwards NULL issues for 'Product.video'
        raise RuntimeError("Cannot reverse this migration. 'Product.video' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Product.video'
        db.alter_column(u'storefront_product', 'video', self.gf('django.db.models.fields.files.FileField')(max_length=100))

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
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['storefront']