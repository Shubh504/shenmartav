# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.parliament_response'
        db.add_column('question_question', 'parliament_response',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.parliament_response'
        db.delete_column('question_question', 'parliament_response')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'popit.organisation': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Organisation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ended': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '300'}),
            'started': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'summary_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'summary_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'popit.person': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'date_of_death': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'description_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'question.question': {
            'Meta': {'ordering': "['-date', 'is_public']", 'object_name': 'Question'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'answer_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'answer_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parliament_response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'question_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'question_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['representative.Representative']"})
        },
        'question.questionpluginconf': {
            'Meta': {'object_name': 'QuestionPluginConf', 'db_table': "'cmsplugin_questionpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Questions'", 'max_length': '32'})
        },
        'representative.party': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Party', '_ormbases': ['popit.Organisation']},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'organisation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Organisation']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'representative.representative': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Representative', '_ormbases': ['popit.Person']},
            'answered': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'attendance_group': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'attendance_record': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_majoritarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_income': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Party']"}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Unit']"}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'representative.unit': {
            'Meta': {'object_name': 'Unit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parties': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'unit'", 'symmetrical': 'False', 'to': "orm['representative.Party']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['question']