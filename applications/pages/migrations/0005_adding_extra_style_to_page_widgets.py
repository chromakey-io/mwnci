# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Page.extra_style'
        db.add_column('pages_page', 'extra_style', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'WidgetPosition.extra_style'
        db.add_column('pages_widgetposition', 'extra_style', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Page.extra_style'
        db.delete_column('pages_page', 'extra_style')

        # Deleting field 'WidgetPosition.extra_style'
        db.delete_column('pages_widgetposition', 'extra_style')


    models = {
        'pages.page': {
            'Meta': {'unique_together': "(['path', 'active', 'type'],)", 'object_name': 'Page'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'extra_style': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Theme']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Type']", 'null': 'True', 'blank': 'True'}),
            'widget': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pages.Widget']", 'through': "orm['pages.WidgetPosition']", 'symmetrical': 'False'})
        },
        'pages.theme': {
            'Meta': {'object_name': 'Theme'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'pages.type': {
            'Meta': {'ordering': "['order']", 'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'pages.widget': {
            'Meta': {'object_name': 'Widget'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.widgetposition': {
            'Meta': {'ordering': "['order']", 'object_name': 'WidgetPosition'},
            'extra_style': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Widget']"})
        }
    }

    complete_apps = ['pages']
