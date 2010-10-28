# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Type'
        db.create_table('pages_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('path', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('pages', ['Type'])

        # Adding model 'Theme'
        db.create_table('pages_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('template', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('pages', ['Theme'])

        # Adding model 'Media'
        db.create_table('pages_media', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('html', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pages', ['Media'])

        # Adding model 'Page'
        db.create_table('pages_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('path', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Type'], null=True, blank=True)),
            ('theme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Theme'], null=True, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('pages', ['Page'])

        # Adding unique constraint on 'Page', fields ['path', 'active', 'type']
        db.create_unique('pages_page', ['path', 'active', 'type_id'])

        # Adding model 'MediaPosition'
        db.create_table('pages_mediaposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('media', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Media'])),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Page'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
        ))
        db.send_create_signal('pages', ['MediaPosition'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Page', fields ['path', 'active', 'type']
        db.delete_unique('pages_page', ['path', 'active', 'type_id'])

        # Deleting model 'Type'
        db.delete_table('pages_type')

        # Deleting model 'Theme'
        db.delete_table('pages_theme')

        # Deleting model 'Media'
        db.delete_table('pages_media')

        # Deleting model 'Page'
        db.delete_table('pages_page')

        # Deleting model 'MediaPosition'
        db.delete_table('pages_mediaposition')


    models = {
        'pages.media': {
            'Meta': {'object_name': 'Media'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pages.mediaposition': {
            'Meta': {'object_name': 'MediaPosition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Media']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'})
        },
        'pages.page': {
            'Meta': {'unique_together': "(['path', 'active', 'type'],)", 'object_name': 'Page'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pages.Media']", 'through': "orm['pages.MediaPosition']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Theme']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Type']", 'null': 'True', 'blank': 'True'})
        },
        'pages.theme': {
            'Meta': {'object_name': 'Theme'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'pages.type': {
            'Meta': {'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['pages']
