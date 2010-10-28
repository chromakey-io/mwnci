# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Page', fields ['active', 'path', 'type']
        db.delete_unique('pages_page', ['active', 'path', 'type_id'])

        # Adding field 'Page.order'
        db.add_column('pages_page', 'order', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding unique constraint on 'Page', fields ['active', 'path', 'type', 'order']
        db.create_unique('pages_page', ['active', 'path', 'type_id', 'order'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Page', fields ['active', 'path', 'type', 'order']
        db.delete_unique('pages_page', ['active', 'path', 'type_id', 'order'])

        # Deleting field 'Page.order'
        db.delete_column('pages_page', 'order')

        # Adding unique constraint on 'Page', fields ['active', 'path', 'type']
        db.create_unique('pages_page', ['active', 'path', 'type_id'])


    models = {
        'pages.page': {
            'Meta': {'unique_together': "(['path', 'active', 'type', 'order'],)", 'object_name': 'Page'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'extra_style': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'widget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Widget']"})
        }
    }

    complete_apps = ['pages']
